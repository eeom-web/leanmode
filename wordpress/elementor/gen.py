"""Builds Elementor (classic, container-based) JSON for the Lean Mode Pro pages.

Run `python3 gen.py` to regenerate dist/*.json.
"""
import hashlib
import json
import sys

import assets
import legal

_seen = set()


def eid(key):
    h = hashlib.md5(key.encode()).hexdigest()[:7]
    assert h not in _seen, key
    _seen.add(h)
    return h


# ---------------------------------------------------------------- value helpers
def px(v, unit="px"):
    return {"unit": unit, "size": v, "sizes": []}


def dims(t, r=None, b=None, l=None, unit="px"):
    if r is None:
        r, b, l = t, t, t
    return {"unit": unit, "top": str(t), "right": str(r), "bottom": str(b), "left": str(l),
            "isLinked": len({t, r, b, l}) == 1}


def gaps(col, row=None):
    row = col if row is None else row
    return {"column": str(col), "row": str(row), "isLinked": col == row, "unit": "px"}


def shadow(h, v, blur, spread, color):
    return {"horizontal": h, "vertical": v, "blur": blur, "spread": spread, "color": color}


def icon(name, lib="fa-solid"):
    return {"value": f"fas fa-{name}" if lib == "fa-solid" else f"far fa-{name}", "library": lib}


def link(url):
    return {"url": url, "is_external": "", "nofollow": "", "custom_attributes": ""}


def G(**refs):
    """__globals__ map. Values: colour ids, or 'T:<id>' for typography."""
    out = {}
    for key, val in refs.items():
        out[key] = f"globals/typography?id={val[2:]}" if val.startswith("T:") else f"globals/colors?id={val}"
    return {"__globals__": out}


def merge(*dicts):
    out = {}
    for d in dicts:
        for k, v in d.items():
            if k == "__globals__":
                out.setdefault("__globals__", {}).update(v)
            else:
                out[k] = v
    return out


def local_typo(prefix, size=None, weight=None, lh=None, ls=None, size_t=None, size_m=None, transform=None,
               decoration=None, lh_unit="em", size_unit="px"):
    p = f"{prefix}_typography" if prefix else "typography"
    d = {f"{p}_typography": "custom", f"{p}_font_family": "Instrument Sans"}
    if size is not None:
        d[f"{p}_font_size"] = px(size, size_unit)
    if size_t is not None:
        d[f"{p}_font_size_tablet"] = px(size_t, size_unit if isinstance(size_t, str) else "px")
    if size_m is not None:
        d[f"{p}_font_size_mobile"] = px(size_m, size_unit if isinstance(size_m, str) else "px")
    if weight is not None:
        d[f"{p}_font_weight"] = str(weight)
    if lh is not None:
        d[f"{p}_line_height"] = px(lh, lh_unit)
    if ls is not None:
        d[f"{p}_letter_spacing"] = px(ls, "em")
    if transform:
        d[f"{p}_text_transform"] = transform
    if decoration:
        d[f"{p}_text_decoration"] = decoration
    return d


# ---------------------------------------------------------------- element helpers
def widget(key, wtype, settings):
    return {"id": eid(key), "elType": "widget", "widgetType": wtype, "settings": settings, "elements": []}


def con(key, children, **s):
    base = {"content_width": "full", "flex_direction": "column"}
    base.update(s)
    return {"id": eid(key), "elType": "container", "settings": base, "elements": children, "isInner": True}


def section(key, children, *, bg=None, pad=(128, 96, 72), side=(32, 32, 16), tag="section", gap=0, **s):
    st = {
        "content_width": "boxed",
        "boxed_width": px(1180),
        "flex_direction": "column",
        "flex_gap": gaps(gap),
        "html_tag": tag,
        "padding": dims(pad[0], side[0], pad[0], side[0]),
        "padding_tablet": dims(pad[1], side[1], pad[1], side[1]),
        "padding_mobile": dims(pad[2], side[2], pad[2], side[2]),
    }
    if bg:
        st.update(merge({"background_background": "classic", "background_color": "#FFFFFF"}, G(background_color=bg)))
    st.update(s)
    # Backgrounds here are CSS gradients, not images: skip Elementor's background lazy-load
    # (it would hide them until the section scrolls into view).
    st["css_classes"] = " ".join(filter(None, [st.get("css_classes"), "e-no-lazyload"]))
    node = con(key, children, **st)
    node["isInner"] = False
    return node


def row(key, children, gap=64, stack="tablet", align="center", **s):
    st = {"flex_direction": "row", "flex_wrap": "nowrap", "flex_gap": gaps(gap), "flex_align_items": align}
    if stack in ("tablet", "mobile"):
        st["flex_gap_mobile"] = gaps(min(gap, 32))
        st["flex_direction_mobile"] = "column"
        st["flex_align_items_mobile"] = "stretch"
    if stack == "tablet":
        st["flex_gap_tablet"] = gaps(min(gap, 48))
        st["flex_direction_tablet"] = "column"
        st["flex_align_items_tablet"] = "stretch"
    st.update(s)
    return con(key, children, **st)


def col(key, children, width=None, width_t=100, width_m=100, gap=0, **s):
    st = {"flex_direction": "column", "flex_gap": gaps(gap)}
    if width is not None:
        st["width"] = px(width, "%")
        if width_t is not None:
            st["width_tablet"] = px(width_t, "%")
        if width_m is not None:
            st["width_mobile"] = px(width_m, "%")
    st.update(s)
    return con(key, children, **st)


def grid(key, children, cols=(3, 2, 1), rows=None, gap=20, row_gap=None, **s):
    rows = rows or tuple((len(children) + c - 1) // c for c in cols)
    st = {
        "container_type": "grid",
        "grid_columns_grid": px(cols[0], "fr"), "grid_columns_grid_tablet": px(cols[1], "fr"),
        "grid_columns_grid_mobile": px(cols[2], "fr"),
        "grid_rows_grid": px(rows[0], "fr"), "grid_rows_grid_tablet": px(rows[1], "fr"),
        "grid_rows_grid_mobile": px(rows[2], "fr"),
        "grid_gaps": gaps(gap, row_gap if row_gap is not None else gap),
        "grid_auto_flow": "row",
    }
    st.update(s)
    return con(key, children, **st)


def card_style(pad=(32, 28), radius=24, prefix="", shadow_on=True, deep=False):
    """Card look for widgets (prefix '_') or containers (prefix '')."""
    d = {
        f"{prefix}background_background": "classic", f"{prefix}background_color": "#FFFFFF",
        f"{prefix}border_border": "solid", f"{prefix}border_width": dims(1), f"{prefix}border_color": "#E3E2DB",
        f"{prefix}border_radius": dims(radius),
        f"{prefix}padding": dims(pad[0]), f"{prefix}padding_mobile": dims(pad[1]),
    }
    if shadow_on:
        d[f"{prefix}box_shadow_box_shadow_type"] = "yes"
        d[f"{prefix}box_shadow_box_shadow"] = (shadow(0, 30, 70, -28, "rgba(16,22,20,0.28)") if deep
                                              else shadow(0, 1, 2, 0, "rgba(16,22,20,0.05)"))
    return merge(d, G(**{f"{prefix}background_color": "lmpsurface", f"{prefix}border_color": "lmpline"}))


# ---------------------------------------------------------------- widget builders
def heading(key, text, tag="h2", color="lmpink", typo=None, cls=None, align=None, **extra):
    s = {"title": text, "header_size": tag, "title_color": "#101614"}
    g = {"title_color": color}
    if typo:
        g["typography_typography"] = "T:" + typo
    s = merge(s, G(**g))
    if cls:
        s["_css_classes"] = cls
    if align:
        s["align"] = align
    return widget(key, "heading", merge(s, extra))


def text(key, html, color="lmptext", typo="lmpbody", cls=None, **extra):
    g = {"text_color": color}
    if "typography_typography" not in extra:
        g["typography_typography"] = "T:" + typo
    s = merge({"editor": html, "text_color": "#414B46"}, G(**g))
    if cls:
        s["_css_classes"] = cls
    return widget(key, "text-editor", merge(s, extra))


def label(key, text_, color="lmpaccent", eyebrow=True):
    return heading(key, text_, tag="p", color=color, typo="lmplabel", cls="lmp-eyebrow" if eyebrow else None)


def button(key, text_, url, dark=False, small=False, cls=None, full_mobile=False, **extra):
    s = {
        "text": text_, "link": link(url), "size": "sm" if small else "lg",
        "selected_icon": icon("arrow-right"), "icon_align": "row-reverse", "icon_indent": px(10),
        "button_text_color": "#FFFFFF", "background_background": "classic", "background_color": "#1D5A48",
        "button_background_hover_background": "classic", "button_background_hover_color": "#164A3B",
        "hover_color": "#FFFFFF",
        "border_radius": dims(999),
        "text_padding": dims(10, 18, 10, 18) if small else dims(20, 34, 20, 34),
        "button_box_shadow_box_shadow_type": "yes",
        "button_box_shadow_box_shadow": shadow(0, 1, 2, 0, "rgba(16,22,20,0.12)"),
        "button_hover_transition_duration": px(0.2, "s"),
    }
    g = {"background_color": "lmpink" if dark else "lmpaccent",
         "button_background_hover_color": "lmpinksoft" if dark else "lmpaccenthover"}
    if small:
        s.update(local_typo("", size=14, weight=600, lh=1.2))
        s["icon_indent"] = px(8)
        s["text_padding_mobile"] = dims(10, 14, 10, 14)
    else:
        g["typography_typography"] = "T:lmpbutton"
    if full_mobile:
        s["align_mobile"] = "justify"
    if cls:
        s["_css_classes"] = cls
    return widget(key, "button", merge(s, G(**g), extra))


def icon_box(key, ic, title, desc="", *, inline=False, card=True, title_typo="lmph3", title_tag="h3",
             icon_size=20, icon_pad=14, shape="circle", stacked_colors=("lmpaccenttint", "lmpaccent"), **extra):
    s = {
        "selected_icon": icon(ic), "view": "stacked", "shape": shape,
        "title_text": title, "description_text": desc, "title_size": title_tag,
        "position": "inline-start" if inline else "block-start",
        **({"position_tablet": "inline-start", "position_mobile": "inline-start"} if inline else {}),
        "text_align": "start", "content_vertical_alignment": "top",
        "icon_size": px(icon_size), "icon_padding": px(icon_pad, "px"),
        "icon_space": px(16), "title_bottom_space": px(6 if inline else 10),
        "primary_color": "#EEF4F0", "secondary_color": "#1D5A48",
        "title_color": "#101614", "description_color": "#5D6762",
    }
    g = {"primary_color": stacked_colors[0], "secondary_color": stacked_colors[1],
         "title_color": "lmpink", "description_color": "lmpmuted",
         "title_typography_typography": "T:" + title_typo}
    s = merge(s, G(**g), local_typo("description", size=16, weight=400, lh=1.55))
    if card:
        s = merge(s, card_style(prefix="_"), {"_css_classes": "lmp-card"})
    return widget(key, "icon-box", merge(s, extra))


def icon_list(key, items, inline=True, cls=None, text_color="lmpmuted", icon_color="lmpaccent", size=14,
              gap=24, **extra):
    s = {
        "view": "inline" if inline else "traditional",
        "icon_list": [{"_id": eid(f"{key}-{i}"), "text": t,
                       "selected_icon": icon(ic) if ic else {"value": "", "library": ""},
                       **({"link": link(url)} if url else {})}
                      for i, (t, ic, url) in enumerate(items)],
        "space_between": px(gap), "icon_size": px(size), "text_indent": px(8),
        "icon_color": "#1D5A48", "text_color": "#5D6762",
    }
    s = merge(s, G(icon_color=icon_color, text_color=text_color), local_typo("icon", size=14, weight=500, lh=1.5))
    if cls:
        s["_css_classes"] = cls
    return widget(key, "icon-list", merge(s, extra))


def html(key, code, cls=None, **extra):
    s = {"html": code}
    if cls:
        s["_css_classes"] = cls
    return widget(key, "html", merge(s, extra))


def progress(key, percent, height=8):
    s = {
        "title": "", "title_display": "", "percent": px(percent, "%"), "display_percentage": "",
        "inner_text": "", "bar_color": "#1D5A48", "bar_bg_color": "#EFEEE8",
        "bar_height": px(height), "bar_border_radius": px(4), "_css_classes": "lmp-progress",
    }
    return widget(key, "progress", merge(s, G(bar_color="lmpaccent", bar_bg_color="lmpbgalt")))


def logo(key, url="/"):
    s = {"title": 'LEAN MODE <span class="lmp-pro">PRO</span>', "header_size": "p", "link": link(url),
         "title_color": "#101614", "_css_classes": "lmp-logo"}
    s = merge(s, G(title_color="lmpink"), local_typo("", size=15, weight=700, lh=1, ls=0.14, size_m=14))
    s["typography_letter_spacing_mobile"] = px(0.1, "em")
    return widget(key, "heading", s)


# ---------------------------------------------------------------- shared parts
def header(prefix, cta_url=None):
    """Sticky header. Without cta_url (e.g. on the confirmation page) it shows the logo only."""
    items = [logo(f"{prefix}-logo")]
    if cta_url:
        items.append(button(f"{prefix}-header-cta", "Get the Free Guide", cta_url, dark=True, small=True,
                            cls="lmp-header-cta"))
    return section(f"{prefix}-header", [
        html(f"{prefix}-assets", assets.assets_html(), cls="lmp-assets"),
        row(f"{prefix}-header-row", items, gap=16, stack=None, flex_justify_content="space-between"),
    ], pad=(16, 14, 12), tag="header", css_classes="lmp-header")


def footer(prefix, legal, compact=False):
    """Site footer. The compact variant is a single row (copyright + legal links) for one-screen pages."""
    copyright_ = "<p>© 2026 Lean Mode Pro. All rights reserved.</p>"
    if compact:
        return section(f"{prefix}-footer", [
            row(f"{prefix}-footer-row", [
                text(f"{prefix}-copyright", copyright_, color="lmpmuted", typo="lmpsmall"),
                icon_list(f"{prefix}-footer-links", [(t, None, u) for t, u in legal], gap=28,
                          text_color_hover="#101614"),
            ], gap=12, stack=None, flex_justify_content="space-between", flex_wrap="wrap",
                flex_direction_mobile="column-reverse", flex_align_items_mobile="flex-start"),
        ], pad=(20, 24, 28), tag="footer", border_border="solid", border_width=dims(1, 0, 0, 0),
            border_color="#E3E2DB")
    return section(f"{prefix}-footer", [
        row(f"{prefix}-footer-row", [
            logo(f"{prefix}-footer-logo"),
            icon_list(f"{prefix}-footer-links", [(t, None, u) for t, u in legal], gap=28,
                      text_color_hover="#101614"),
        ], gap=24, stack=None, flex_justify_content="space-between", flex_wrap="wrap",
            flex_direction_mobile="column", flex_align_items_mobile="flex-start"),
        text(f"{prefix}-copyright", copyright_, color="lmpmuted", typo="lmpsmall", _margin=dims(32, 0, 0, 0)),
    ], pad=(48, 48, 40), tag="footer", border_border="solid", border_width=dims(1, 0, 0, 0),
        border_color="#E3E2DB")


LEGAL = [("Blog", "/blog/"), ("Contact", "/contact/"), ("Privacy Policy", "/privacy-policy/"),
         ("Legal Notice", "/legal-notice/"), ("Disclaimer", "/disclaimer/")]


# ---------------------------------------------------------------- landing page
def landing():
    p = "home"
    hero = section(f"{p}-hero", [row(f"{p}-hero-row", [
        col(f"{p}-hero-copy", [
            heading(f"{p}-hero-badge", "Free e-book · 30-day plan", tag="p", color="lmpinksoft",
                    cls="lmp-badge", _element_width="auto", hide_mobile="hidden-mobile",
                    **merge(local_typo("", size=13, weight=600, lh=1.3),
                            {"_background_background": "classic", "_background_color": "#FFFFFF",
                             "_border_border": "solid", "_border_width": dims(1), "_border_color": "#E3E2DB",
                             "_border_radius": dims(999), "_padding": dims(7, 14, 7, 12),
                             "_margin": dims(0, 0, 24, 0)})),
            heading(f"{p}-hero-title",
                    'Your <span class="lmp-accent-word">Step-by-Step</span> <span class="lmp-nowrap">30-Day</span> Weight Loss Plan',
                    tag="h1", typo="lmpdisplay", cls="lmp-hero-title", _margin=dims(0, 0, 24, 0),
                    _margin_mobile=dims(0)),
            text(f"{p}-hero-lead", "<p>Nutrition, workouts, daily movement and practical weight loss strategies "
                                   "in one 30-day plan.</p>", color="lmpinksoft", typo="lmplead",
                 _element_width="initial", _element_custom_width=px(600), _element_custom_width_mobile=px(100, "%"),
                 _element_custom_width_tablet=px(640), hide_mobile="hidden-mobile"),
            text(f"{p}-hero-text", "<p>Instead of figuring out what to do every day, just focus on the "
                                   "next step.</p>", color="lmpmuted", _margin=dims(14, 0, 0, 0), hide_mobile="hidden-mobile"),
            button(f"{p}-hero-cta", "Get the Free 30-Day Plan", "#signup", full_mobile=True,
                   _margin=dims(36, 0, 0, 0), _element_width_mobile="inherit", hide_mobile="hidden-mobile"),
            icon_list(f"{p}-hero-facts", [("Completely free", "check", None), ("One clear step every day", "check", None),
                                          ("Delivered by email", "check", None)],
                      gap=24, _margin=dims(24, 0, 0, 0), hide_mobile="hidden-mobile"),
        ], width=54, width_m=57, flex_align_items="flex-start"),
        col(f"{p}-hero-visual", [html(f"{p}-hero-mockup", assets.mockup_html(
            sizes="(max-width:767px) 33vw, (max-width:1024px) 300px, 360px", eager=True))], width=42, width_m=39,
            css_classes="lmp-hero-visual"),
    # Phones: title and cover side by side, everything else hidden, so the signup card below
    # (title, cover and email field) fits on the first screen without scrolling.
    ], gap=48, flex_direction_mobile="row", flex_align_items_mobile="center", flex_gap_mobile=gaps(14))],
        pad=(64, 40, 32), gap=0)
    hero["settings"]["padding"] = dims(64, 32, 104, 32)
    hero["settings"]["padding_tablet"] = dims(40, 32, 72, 32)
    hero["settings"]["padding_mobile"] = dims(20, 16, 10, 16)

    signup = section(f"{p}-signup", [row(f"{p}-signup-card", [
        col(f"{p}-signup-intro", [
            label(f"{p}-signup-label", "Free guide"),
            heading(f"{p}-signup-title", "Get Your Free 30-Day Plan", tag="h2",
                    **local_typo("", size=38, weight=600, lh=1.1, ls=-0.024, size_t=34, size_m=28)),
            icon_list(f"{p}-signup-chips", [("Nutrition", "apple-alt", None), ("Workouts", "dumbbell", None),
                                             ("Daily movement", "walking", None), ("Habits", "redo-alt", None)],
                      cls="lmp-chips", text_color="lmpinksoft", gap=8, _margin=dims(4, 0, 0, 0)),
        ], width=42, gap=16, hide_mobile="hidden-mobile"),
        col(f"{p}-signup-form-col", [html(f"{p}-signup-form", assets.form_html("signup", "hero", "Get the Free Plan"))],
            width=54),
    ], gap=56, **card_style(pad=(48, 20), radius=32, deep=True), padding_tablet=dims(40))],
        pad=(0, 0, 0), _element_id="signup")

    contents_items = [
        ("apple-alt", "Meal Plans", "A simple, doable structure that makes your daily eating easier to manage."),
        ("dumbbell", "Workout Plans", "A basic training routine you can fit into your daily schedule."),
        ("walking", "Daily Movement", "Simple movement goals that help you stay more active throughout the day, beyond workouts."),
        ("lightbulb", "Weight Loss Tips", "Practical, easy-to-understand strategies you can use in everyday life."),
        ("redo-alt", "Habits", "Small steps that help you build a more structured lifestyle over 30 days."),
        ("th-large", "A System, Not Willpower", "A clear structure, so you can follow the process day by day without relying on motivation alone."),
    ]
    contents = section(f"{p}-contents", [
        col(f"{p}-contents-head", [
            heading(f"{p}-contents-title", "What's Inside the 30-Day Plan?", typo="lmph2"),
            text(f"{p}-contents-intro", "<p>Instead of making weight loss complicated, this guide breaks it into "
                                        "30 days, so you can see clearly what to do each day.</p>", typo="lmplead"),
        ], gap=18, width=64, width_t=100, width_m=100),
        grid(f"{p}-contents-grid", [icon_box(f"{p}-contents-{i}", ic, t, d) for i, (ic, t, d) in
                                    enumerate(contents_items)], cols=(3, 2, 1), gap=20,
             margin=dims(56, 0, 0, 0), margin_mobile=dims(40, 0, 0, 0)),
    ])

    steps = [(1, 3, "START", "Take the first step."), (15, 50, "KEEP GOING", "Strengthen your routine."),
             (30, 100, "MAKE IT STICK", "Start bringing what you've learned into everyday life.")]
    roadmap = section(f"{p}-roadmap", [
        col(f"{p}-roadmap-head", [
            heading(f"{p}-roadmap-title", "Not Just Information. A Roadmap.", typo="lmph2"),
            text(f"{p}-roadmap-body",
                 '<p>You can find thousands of tips about losing weight online. The problem usually isn\'t a lack '
                 'of information. It\'s not knowing where to start and what to do.</p>'
                 '<p>That\'s why the 30-day plan organizes everything into one system you follow step '
                 'by step.</p>', typo="lmplead", color="lmpinksoft"),
        ], gap=20, width=64, width_t=100, width_m=100),
        grid(f"{p}-roadmap-steps", [
            con(f"{p}-roadmap-step-{d}", [
                heading(f"{p}-roadmap-day-{d}", f"DAY {d} →", tag="p", color="lmpaccent", typo="lmplabel"),
                heading(f"{p}-roadmap-action-{d}", a, tag="h3",
                        **local_typo("", size=34, weight=600, lh=1.1, ls=-0.02, size_t=28, size_m=28),
                        _margin=dims(10, 0, 0, 0)),
                text(f"{p}-roadmap-text-{d}", f"<p>{t}</p>", color="lmpmuted", _flex_size="grow"),
                progress(f"{p}-roadmap-bar-{d}", pct),
            ], flex_gap=gaps(8), **card_style(pad=(32, 28)), css_classes="lmp-card")
            for d, pct, a, t in steps
        ], cols=(3, 3, 1), gap=20, margin=dims(56, 0, 0, 0), margin_mobile=dims(40, 0, 0, 0)),
    ], bg="lmpbgalt")

    blocks = [("bullseye", "TODAY'S FOCUS", "What matters most today?"),
              ("apple-alt", "NUTRITION", "What to pay attention to in your meals today."),
              ("walking", "MOVEMENT", "Today's movement goal."),
              ("dumbbell", "WORKOUT", "Today's planned workout."),
              ("lightbulb", "TIP OF THE DAY", "A weight loss tip that's easy to apply."),
              ("flag", "TASK OF THE DAY", "A small task to complete during the day.")]
    daily = section(f"{p}-daily", [row(f"{p}-daily-row", [
        col(f"{p}-daily-copy", [
            label(f"{p}-daily-label", "How it works"),
            heading(f"{p}-daily-title", "Every Day, Just Focus on the Next Step.", typo="lmph2"),
            text(f"{p}-daily-lead", "<p>The plan uses the same simple structure for each of the 30 days. You open "
                                    "the day's page and see at a glance what to focus on.</p>",
                 typo="lmplead", color="lmpinksoft"),
            text(f"{p}-daily-text", "<p>So you don't have to make a new plan every morning. You just follow the "
                                    "day's steps.</p>", color="lmpmuted"),
            text(f"{p}-daily-steps", "<ol><li>Open the day's page.</li><li>Follow the steps in order.</li>"
                                     "<li>Finish the day, ready for tomorrow.</li></ol>", color="lmpinksoft",
                 cls="lmp-steps", **local_typo("", size=17, weight=500, lh=1.4)),
        ], width=42, gap=18),
        col(f"{p}-daily-visual", [
            con(f"{p}-daypage", [
                row(f"{p}-daypage-head", [
                    heading(f"{p}-daypage-day", 'DAY <span class="lmp-daynum">01</span> / 30', tag="p",
                            color="lmpmuted", **local_typo("", size=14, weight=600, lh=1.2, ls=0.12)),
                    heading(f"{p}-daypage-tag", "Sample page layout", tag="p", color="lmpmuted",
                            _element_width="auto",
                            **merge(local_typo("", size=12, weight=600, lh=1.2),
                                    {"_border_border": "dashed", "_border_width": dims(1), "_border_color": "#D2D1C9",
                                     "_border_radius": dims(999), "_padding": dims(6, 12, 6, 12)})),
                ], gap=12, stack=None, flex_justify_content="space-between", flex_wrap="wrap"),
                progress(f"{p}-daypage-bar", 3, height=6),
                grid(f"{p}-daypage-grid", [
                    icon_box(f"{p}-daypage-{i}", ic, t, d, inline=True, card=False, title_typo="lmplabel",
                             icon_size=18, icon_pad=11, shape="rounded",
                             _border_border="solid", _border_width=dims(1, 0, 0, 0), _border_color="#E3E2DB",
                             _padding=dims(16, 0, 16, 0), description_typography_font_size=px(15))
                    for i, (ic, t, d) in enumerate(blocks)
                ], cols=(2, 2, 1), gap=24, row_gap=0, margin=dims(8, 0, 0, 0)),
            ], flex_gap=gaps(16), **card_style(pad=(32, 20), radius=32, deep=True)),
            text(f"{p}-daily-caption", "<p>This image only shows the layout of the daily pages. Each day's "
                                       "content is in the e-book.</p>", color="lmpmuted", typo="lmpsmall",
                 align="center"),
        ], width=54, gap=16),
    ], gap=64)])

    principles = [("Simple", "No unnecessary complexity."), ("Step by Step", "A clear next step every day."),
                  ("Fits Everyday Life", "Built to be sustainable.")]
    line = "rgba(238,242,239,0.12)"
    simplicity = section(f"{p}-simplicity", [con(f"{p}-simplicity-panel", [
        row(f"{p}-simplicity-top", [
            col(f"{p}-simplicity-copy", [
                heading(f"{p}-simplicity-title", "Don't Overcomplicate Weight Loss.", color="lmpondark",
                        **merge(local_typo("", size=68, weight=600, lh=1.0, ls=-0.034, size_t=52),
                                {"typography_font_size": {"unit": "custom", "size": "min(4.8vw, 68px)", "sizes": []},
                                 "typography_font_size_mobile": px(9, "vw")})),
                text(f"{p}-simplicity-text", "<p>You don't have to hunt for a new diet every day, memorize hundreds of "
                                             "rules or try to be perfect.</p>", color="lmpondarkmuted",
                     typo="lmplead"),
                text(f"{p}-simplicity-goal", "<p>The goal is a simple system you can follow for "
                                             "30 days.</p>", color="lmpondark", typo="lmplead"),
            ], width=56, gap=20),
            col(f"{p}-simplicity-visual", [html(f"{p}-simplicity-shift", assets.shift_html())], width=40),
        ], gap=56),
        grid(f"{p}-simplicity-principles", [
            con(f"{p}-principle-{i}", [
                heading(f"{p}-principle-title-{i}", t, tag="h3", color="lmpondark",
                        **local_typo("", size=24, weight=600, lh=1.2, ls=-0.02)),
                text(f"{p}-principle-text-{i}", f"<p>{d}</p>", color="lmpondarkmuted"),
            ], flex_gap=gaps(6),
                padding=dims(32, 32, 0, 0 if i == 0 else 32), padding_tablet=dims(28, 24, 0, 0 if i == 0 else 24),
                padding_mobile=dims(22, 0, 22, 0),
                border_border="solid", border_color=line,
                border_width=dims(0, 0, 0, 0 if i == 0 else 1),
                border_width_mobile=dims(0, 0, 0 if i == 2 else 1, 0))
            for i, (t, d) in enumerate(principles)
        ], cols=(3, 3, 1), gap=0, margin=dims(64, 0, 0, 0), margin_mobile=dims(40, 0, 0, 0),
            border_border="solid", border_width=dims(1, 0, 0, 0), border_color=line),
    ], padding=dims(80, 72, 80, 72), padding_tablet=dims(56, 40, 56, 40), padding_mobile=dims(40, 20, 40, 20),
        border_radius=dims(32), background_background="gradient", background_color="#1B3F34",
        background_color_stop=px(0, "%"), background_color_b="#0F1D19", background_color_b_stop=px(62, "%"),
        background_gradient_type="radial", background_gradient_position="top right")])

    audience = section(f"{p}-audience", [row(f"{p}-audience-row", [
        col(f"{p}-audience-head", [
            heading(f"{p}-audience-title", "Who Is This Plan For?", typo="lmph2"),
            text(f"{p}-audience-text", "<p>It's designed for people who want to lose weight, don't know where to "
                                       "start, or find it hard to stick with the plans they begin.</p>",
                 typo="lmplead"),
        ], width=40, gap=18, css_classes="lmp-sticky"),
        grid(f"{p}-audience-grid", [
            icon_box(f"{p}-audience-{i}", "check", t, "", icon_size=16, icon_pad=12,
                     stacked_colors=("lmpaccent", "lmpsurface"), icon_space=px(28), icon_space_mobile=px(16),
                     position_mobile="inline-start", content_vertical_alignment="middle",
                     **merge(local_typo("title", size=20, weight=600, lh=1.3, ls=-0.015, size_m=17),
                             {"title_bottom_space": px(0)}))
            for i, t in enumerate(["Beginners", "Anyone who wants to eat more regularly",
                                   "Anyone who wants to add movement and workouts to their routine",
                                   "Anyone who wants to make losing weight simpler"])
        ], cols=(2, 2, 1), gap=20, width=px(56, "%"), width_tablet=px(100, "%"), width_mobile=px(100, "%")),
    ], gap=64, align="flex-start")])
    # icon boxes with a global title typography must not also carry the local one
    for ib in audience["elements"][0]["elements"][1]["elements"]:
        ib["settings"]["__globals__"].pop("title_typography_typography", None)

    milestones = [("01", "START"), ("07", "BUILD A ROUTINE"), ("14", "KEEP GOING"),
                  ("21", "STRENGTHEN YOUR HABITS"), ("30", "OWN YOUR NEW ROUTINE")]
    timeline = section(f"{p}-timeline", [
        col(f"{p}-timeline-head", [
            heading(f"{p}-timeline-title", "30 Days", typo="lmph2"),
            text(f"{p}-timeline-text", "<p>An overview of how the 30 days flow.</p>",
                 typo="lmplead"),
        ], gap=16),
        grid(f"{p}-timeline-track", [
            con(f"{p}-milestone-{n}", [
                heading(f"{p}-milestone-num-{n}", f'<span class="screen-reader-text">Day </span>{n}', tag="p",
                        **local_typo("", size=52, weight=600, lh=1.05, ls=-0.03, size_t=40, size_m=36)),
                heading(f"{p}-milestone-label-{n}", lab, tag="p", color="lmpinksoft",
                        **local_typo("", size=14, weight=600, lh=1.4, ls=0.1)),
            ], flex_gap=gaps(6), css_classes="lmp-milestone",
                padding=dims(32, 16, 0, 0), padding_mobile=dims(0, 0, 0, 0))
            for n, lab in milestones
        ], cols=(5, 5, 1), gap=0, row_gap=28, css_classes="lmp-timeline",
            margin=dims(64, 0, 0, 0), margin_mobile=dims(40, 0, 0, 0)),
    ], bg="lmpbgalt")

    final = section(f"{p}-final", [row(f"{p}-final-panel", [
        col(f"{p}-final-copy", [
            label(f"{p}-final-label", "Free 30-day plan"),
            heading(f"{p}-final-title", "Start Your 30-Day Journey Today.", typo="lmph2"),
            text(f"{p}-final-text", "<p>Instead of overthinking it, start with the first step.</p>", typo="lmplead",
                 color="lmpinksoft"),
            html(f"{p}-final-form", assets.form_html("final", "final-cta", "Get the Free 30-Day Plan"),
                 _margin=dims(16, 0, 0, 0), _element_width="initial", _element_custom_width=px(580),
                 _element_custom_width_mobile=px(100, "%")),
        ], width=62, gap=18),
        col(f"{p}-final-visual", [html(f"{p}-final-mockup", assets.mockup_html(
            small=True, daycard=False, sizes="(max-width:767px) 64vw, 260px"))],
            width=34, hide_mobile="hidden-mobile"),
    ], gap=48, padding=dims(72, 72, 72, 72), padding_tablet=dims(56, 40, 56, 40), padding_mobile=dims(32, 20, 32, 20),
        border_radius=dims(32), border_border="solid", border_width=dims(1), border_color="#D5E4DA",
        **merge({"background_background": "classic", "background_color": "#E3EDE7"},
                G(background_color="lmpaccentsoft")))])

    return [header(p, "#signup"), hero, signup, contents, roadmap, daily, simplicity, audience, timeline, final,
            footer(p, LEGAL)]


# ---------------------------------------------------------------- one-screen pages (after the signup)
EBOOK_PDF = "/wp-content/uploads/2026/10/lean-mode-pro-30-day-weight-loss-plan.pdf"  # add ?v=2 etc. after a re-upload
EBOOK_PDF_NAME = "lean-mode-pro-30-day-weight-loss-plan.pdf"


def status_badge(key, text_):
    """White pill with a green check, e.g. "You're signed up"."""
    return heading(key, text_, tag="p", color="lmpinksoft", cls="lmp-badge lmp-badge--check", _element_width="auto",
                   **merge(local_typo("", size=13, weight=600, lh=1.3),
                           {"_background_background": "classic", "_background_color": "#FFFFFF",
                            "_border_border": "solid", "_border_width": dims(1), "_border_color": "#E3E2DB",
                            "_border_radius": dims(999), "_padding": dims(6, 14, 6, 8)},
                           G(_background_color="lmpsurface", _border_color="lmpline")))


def fit_title(key, html_):
    return heading(key, html_, tag="h1", **local_typo("", size=48, weight=600, lh=1.05, ls=-0.03, size_t=46,
                                                       size_m=36))


def step_list(key, steps):
    """Numbered steps: bold title followed by one sentence."""
    html_ = "<ol>" + "".join(f"<li><span><strong>{t}</strong> {d}</span></li>" for t, d in steps) + "</ol>"
    return text(key, html_, color="lmpmuted", cls="lmp-steps lmp-steps--detail",
                **local_typo("", size=16, weight=400, lh=1.55))


def fit_page(p, left, right):
    """Header, a two-column main section that fills one desktop screen (.lmp-fit) and the compact footer."""
    main = section(f"{p}-main", [row(f"{p}-row", [left, right], gap=48)], pad=(40, 48, 32), css_classes="lmp-fit",
                   flex_justify_content="center")
    main["settings"]["padding_mobile"] = dims(32, 16, 56, 16)
    return [header(p), main, footer(p, LEGAL, compact=True)]


def thanks_page():
    """Confirmation page shown after a signup (/thank-you/). On desktop it fits one screen, without scrolling."""
    p = "thanks"
    copy = col(f"{p}-copy", [
        status_badge(f"{p}-badge", "You're signed up"),
        fit_title(f"{p}-title", 'Thank you!<br>Your 30-day plan is <span class="lmp-accent-word">on its way.</span>'),
        text(f"{p}-lead", "<p>We're sending the 30-Day Weight Loss Plan to your email address.</p>",
             typo="lmplead", color="lmpinksoft"),
        heading(f"{p}-steps-title", "What to do now", typo="lmph3", _margin=dims(14, 0, 0, 0)),
        step_list(f"{p}-steps", [
            ("Check your email.",
             "Open the email from LEAN MODE PRO. If you can't see it, check your spam or promotions folder."),
            ("Confirm your signup.",
             "Click the link in the confirmation email. You'll get your plan right after you confirm."),
            ("Plan day 1.",
             "Pick the day and time you'll open the plan. You don't need to wait for a perfect day to start."),
        ]),
    ], width=56, gap=16, flex_align_items="flex-start")

    prep = col(f"{p}-prep", [
        heading(f"{p}-prep-title", "Get ready for day 1", **local_typo("", size=26, weight=600, lh=1.15, ls=-0.02,
                                                                     size_m=24)),
        text(f"{p}-prep-text", "<p>While you wait for your plan, you can get these three things ready:</p>", color="lmpinksoft",
             **local_typo("", size=16, weight=400, lh=1.55)),
        icon_list(f"{p}-prep-list", [
            ("A tape measure: you'll measure your waist on day 1.", "check", None),
            ("A water bottle: day 2 is all about water.", "check", None),
            ("A notebook or a note on your phone: to write down what you eat and your steps.", "check", None),
        ], inline=False, text_color="lmpinksoft", size=14, gap=12, icon_self_vertical_align="flex-start",
            icon_vertical_offset=px(5), **local_typo("icon", size=16, weight=500, lh=1.5)),
    ], width=40, gap=14, padding=dims(36), padding_tablet=dims(32), padding_mobile=dims(24, 20, 24, 20),
        border_radius=dims(28), border_border="solid", border_width=dims(1), border_color="#D5E4DA",
        **merge({"background_background": "classic", "background_color": "#E3EDE7"},
                G(background_color="lmpaccentsoft")))
    return fit_page(p, copy, prep)


def welcome_page():
    """Thank-you page after the email confirmation (double opt-in, /welcome/): the e-book download."""
    p = "welcome"
    copy = col(f"{p}-copy", [
        status_badge(f"{p}-badge", "Signup confirmed"),
        fit_title(f"{p}-title", 'Welcome!<br>Your plan is <span class="lmp-accent-word">ready.</span>'),
        text(f"{p}-lead", "<p>You can download the 30-Day Weight Loss Plan now.</p>",
             typo="lmplead", color="lmpinksoft"),
        row(f"{p}-download", [
            button(f"{p}-download-btn", "Download the plan", EBOOK_PDF, full_mobile=True, selected_icon=icon("arrow-down"),
                   link={"url": EBOOK_PDF, "is_external": "", "nofollow": "on",
                         "custom_attributes": f"download|{EBOOK_PDF_NAME}"}),
            text(f"{p}-download-meta", "<p>PDF · 53 pages · 0.7 MB</p>", color="lmpmuted", typo="lmpsmall"),
        ], gap=20, stack="mobile", flex_gap_mobile=gaps(12), flex_align_items_mobile="stretch",
            _margin=dims(6, 0, 0, 0)),
        heading(f"{p}-steps-title", "How to get started", typo="lmph3", _margin=dims(14, 0, 0, 0)),
        step_list(f"{p}-steps", [
            ("Save the plan.", "Download it to your phone or computer so you can open it easily every day."),
            ("Read the basics first.", "The plate method, the shopping list and the exercises are on the first pages."),
            ("Open the day's page every morning.", "One page a day, read in a few minutes."),
        ]),
    ], width=56, gap=16, flex_align_items="flex-start", css_classes="lmp-fit-copy")
    visual = col(f"{p}-visual", [html(f"{p}-mockup", assets.mockup_html(
        sizes="(max-width:767px) 66vw, (max-width:1024px) 300px, 320px", eager=True))], width=40,
        css_classes="lmp-fit-visual")
    return fit_page(p, copy, visual)


def legal_page(slug, title, home_url):
    p = f"legal-{slug}"
    main = section(f"{p}-main", [
        heading(f"{p}-back", f'<a href="{home_url}">← Back to home</a>', tag="p", color="lmpmuted",
                typo="lmpsmall"),
        heading(f"{p}-title", title, tag="h1", **local_typo("", size=52, weight=600, lh=1.08, ls=-0.026,
                                                            size_t=42, size_m=34)),
        text(f"{p}-body", legal.BODIES[slug](), cls="lmp-prose"),
    ], gap=24, pad=(96, 72, 56), boxed_width=px(760), min_height=px(60, "vh"))
    return [header(p, f"{home_url}#signup"), main, footer(p, LEGAL)]


def contact_page(home_url):
    p = "contact"
    main = section(f"{p}-main", [
        heading(f"{p}-back", f'<a href="{home_url}">← Back to home</a>', tag="p", color="lmpmuted",
                typo="lmpsmall"),
        heading(f"{p}-title", "Contact", tag="h1", **local_typo("", size=52, weight=600, lh=1.08, ls=-0.026,
                                                               size_t=42, size_m=34)),
        text(f"{p}-intro", "<p>Questions about the plan, feedback or anything else? Send us a message with the form "
                           "below or email us at <a href=\"mailto:{{lmp:email}}\">{{lmp:email}}</a>.</p>",
             cls="lmp-prose"),
        html(f"{p}-form", assets.contact_html()),
    ], gap=24, pad=(96, 72, 56), boxed_width=px(760), min_height=px(60, "vh"))
    return [header(p, f"{home_url}#signup"), main, footer(p, LEGAL)]


# Slugs of the WordPress pages this build targets. The landing page is the site's front page.
LANDING_SLUG = "free-30-day-plan"
LEGAL_PAGES = [("privacy-policy", "Privacy Policy"), ("legal-notice", "Legal Notice"), ("disclaimer", "Disclaimer")]

if __name__ == "__main__":
    import os

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
    os.makedirs(out, exist_ok=True)

    def write(name, data):
        with open(os.path.join(out, name), "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))

    write("landing.json", landing())
    write("thank-you.json", thanks_page())
    write("welcome.json", welcome_page())
    for slug, title in LEGAL_PAGES:
        write(f"{slug}.json", legal_page(slug, title, "/"))
    write("contact.json", contact_page("/"))

    # Snippets for the blog template (mu-plugin lmp-blog): brand CSS/JS, signup form and cover, stored in the
    # WordPress option `lmp_blog` on deploy.
    write("blog.json", {"assets": assets.assets_html(),
                        "form": assets.form_html("post", "blog-post", "Get the Free Plan"),
                        "mockup": assets.mockup_html(small=True, daycard=False, sizes="130px")})

    from kit import settings as kit_settings
    write("kit.json", kit_settings)
    print("written:", sorted(os.listdir(out)))

"""Builds the Lean Mode Pro e-book as print-ready HTML (A4, one element per page).

    python3 ebook/build.py          -> ebook/dist/ebook.html
    node ebook/render.mjs           -> ebook/dist/*.pdf
"""
import base64
import html
import os
import re

from content import basics as B
from content import plan as P

ROOT = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(ROOT, "fonts")

ICONS = {
    "focus": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"/>',
    "nutrition": '<path d="M12 8c-1.3-1.1-2.8-1.5-4.3-1.1C5.3 7.5 4 9.8 4 12.6 4 16.6 6.7 21 9.5 21c1.1 0 1.5-.6 2.5-.6s1.4.6 2.5.6c2.8 0 5.5-4.4 5.5-8.4 0-2.8-1.3-5.1-3.7-5.7-1.5-.4-3 0-4.3 1.1Z"/><path d="M12 8c0-2.4 1.1-4.1 3.2-4.9"/>',
    "movement": '<circle cx="6" cy="18" r="2"/><circle cx="18" cy="6" r="2"/><path d="M8 18h7.5a3.5 3.5 0 0 0 0-7h-7a3.5 3.5 0 0 1 0-7H16"/>',
    "training": '<path d="M6.5 6.5v11"/><path d="M17.5 6.5v11"/><path d="M3.5 9.5v5"/><path d="M20.5 9.5v5"/><path d="M6.5 12h11"/>',
    "tips": '<path d="M9.5 18h5"/><path d="M10.5 21h3"/><path d="M12 3a6 6 0 0 0-3.7 10.7c.7.6 1.2 1.4 1.2 2.3h5c0-.9.5-1.7 1.2-2.3A6 6 0 0 0 12 3Z"/>',
    "task": '<path d="M5.5 21V4"/><path d="M5.5 4.5h11l-2.2 4 2.2 4h-11"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "calendar": '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17"/><path d="M8 3v4"/><path d="M16 3v4"/>',
    "habits": '<path d="m17 2.5 3 3-3 3"/><path d="M4 11.5v-1a5 5 0 0 1 5-5h11"/><path d="m7 21.5-3-3 3-3"/><path d="M20 12.5v1a5 5 0 0 1-5 5H4"/>',
}


def icon(name, size=14):
    return (f'<svg class="ic" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def esc(text):
    # Keep ranges such as "1–10" or "8,000–10,000" on one line.
    text = re.sub(r"(\S*\d–\d\S*)", r"<x-nw>\1</x-nw>", html.escape(text, quote=False))
    # "p. 12" (page references) stays together.
    return re.sub(r"\bp\. (?=\d)", "p.\u00a0", text)


def label(text, ic=None):
    return f'<p class="label">{icon(ic) if ic else ""}<span>{esc(text)}</span></p>'


def box():
    return '<span class="cb"></span>'


def bar(done, total=30):
    return '<div class="bar">' + "".join(f'<i class="{"on" if i < done else ""}"></i>' for i in range(total)) + "</div>"


def lines(n):
    return '<div class="lines">' + '<span></span>' * n + "</div>"


def two(n):
    return f"{n:02d}"


# ------------------------------------------------------------------ page builders
pages = []  # (key, section_title_or_None, html)


def add(key, html_, toc=None):
    pages.append({"key": key, "toc": toc, "html": html_})


def page(inner, cls="", footer=True):
    foot = ('<footer class="foot"><span>LEAN MODE PRO</span><span>The 30-Day Weight Loss Plan</span>'
            '<span class="pn">{pageno}</span></footer>') if footer else ""
    return f'<section class="page {cls}">{inner}{foot}</section>'


def cover():
    """The cover as a full A4 page: assets/cover.jpg, 1120 x 1584 px (about 135 dpi), rendered from cover/cover.html
    (own illustration, see cover/render.mjs)."""
    with open(os.path.join(ROOT, "assets", "cover.jpg"), "rb") as fh:
        src = "data:image/jpeg;base64," + base64.b64encode(fh.read()).decode()
    add("cover", page(f'<img class="cover-img" src="{src}" alt="{esc(B.TITLE)}">', "cover-page", footer=False))


def toc_page():
    add("toc", page('<h2 class="h2">Contents</h2><div class="toc">{toc}</div>', "plain"))


def how_to():
    steps = "".join(f'<li><strong>{esc(a)}</strong><span>{esc(b)}</span></li>' for a, b in B.HOW_TO_USE)
    legend = [("focus", "TODAY'S FOCUS", "The one topic of the day"), ("nutrition", "NUTRITION", "Meal ideas"),
              ("movement", "MOVEMENT", "Step or walking goal"), ("training", "WORKOUT", "Strength or recovery"),
              ("tips", "TIP OF THE DAY", "A practical tip"), ("task", "TASK OF THE DAY", "The small step you take today")]
    leg = "".join(f'<div class="leg">{icon(i, 16)}<div><b>{a}</b><span>{b}</span></div></div>' for i, a, b in legend)
    inner = f"""
    <p class="eyebrow">Before you start</p>
    <h2 class="h2">How to use this guide</h2>
    <ol class="steps">{steps}</ol>
    <div class="callout tint"><p>{esc(B.MISSED_DAY)}</p></div>
    <h3 class="h3">On every daily page</h3>
    <div class="legend">{leg}</div>
    <div class="callout warn"><p class="label"><span>IMPORTANT</span></p><p>{esc(B.DISCLAIMER)}</p></div>
    """
    add("kullanim", page(inner, "plain"), toc="How to use this guide")


def intro():
    I = B.INTRO
    paras = "".join(f"<p>{esc(p)}</p>" for p in I["paragraphs"])
    pts = "".join(f'<li>{icon("check", 14)}<div><b>{esc(a)}</b> {esc(b)}</div></li>' for a, b in I["points"])
    phases = "".join(
        f'<div class="phase-mini"><span>PHASE {ph["n"]}</span><b>{esc(ph["name"])}</b><em>Days {ph["days"][0]}–{ph["days"][1]}</em></div>'
        for ph in P.PHASES)
    inner = f"""
    <p class="eyebrow">Introduction</p>
    <h2 class="h2">{esc(I["title"])}</h2>
    <div class="prose">{paras}</div>
    <ul class="points">{pts}</ul>
    <p class="lead">{esc(I["closing"])}</p>
    <h3 class="h3">30 days, 4 phases</h3>
    <div class="phase-row">{phases}</div>
    <p class="caption">Each phase builds on the one before. New habits are added one at a time.</p>
    <div class="callout tint"><p class="label"><span>REALISTIC EXPECTATIONS</span></p><p>{esc(I["expectation"])}</p></div>
    """
    add("giris", page(inner, "plain"), toc="Introduction: Why a 30-day plan?")


def basics():
    cards = [f'<div class="card"><h3>{esc(t)}</h3><p>{esc(x)}</p><p class="plan-line"><b>In the plan:</b> {esc(pl)}</p></div>'
             for t, x, pl in B.BASICS]
    no = "".join(f"<li>{esc(x)}</li>" for x in B.NOT_IN_PLAN)
    roadmap = "".join(f"<li><span>Day {n}</span>{esc(t)}</li>" for n, t in B.HABIT_ROADMAP)
    p1 = f"""
    <p class="eyebrow">Before day 1</p>
    <h2 class="h2">7 basics you should know</h2>
    <p class="lead">Short and simple: the reasoning behind everything you'll do in this plan.</p>
    <div class="cards">{"".join(cards[:4])}</div>
    """
    p2 = f"""
    <p class="eyebrow">Before day 1</p>
    <div class="cards">{"".join(cards[4:])}
      <div class="card dark-card"><p class="label light"><span>WHAT THIS PLAN DOESN'T HAVE</span></p><ul class="nolist">{no}</ul></div>
    </div>
    <h3 class="h3">{icon("habits", 16)} Habits are added one at a time</h3>
    <p class="note">You don't change everything at once. Each new habit builds on the one before.</p>
    <ol class="roadmap">{roadmap}</ol>
    """
    add("temel", page(p1, "plain"), toc="7 basics you should know")
    add("temel2", page(p2, "plain"))


def plate_svg():
    """Plate model as vector pie: vegetables 50 %, protein 25 %, carbs 22 %, fat 3 %."""
    import math
    parts = [(0.50, "#8fc3a8"), (0.25, "#1d5a48"), (0.22, "#d8cba8"), (0.03, "#b9a676")]
    cx = cy = 50
    rad = 44
    start = -90.0
    paths = []
    for frac, color in parts:
        end = start + frac * 360
        a0, a1 = math.radians(start), math.radians(end)
        x0, y0 = cx + rad * math.cos(a0), cy + rad * math.sin(a0)
        x1, y1 = cx + rad * math.cos(a1), cy + rad * math.sin(a1)
        large = 1 if frac > 0.5 else 0
        paths.append(f'<path d="M{cx} {cy} L{x0:.2f} {y0:.2f} A{rad} {rad} 0 {large} 1 {x1:.2f} {y1:.2f} Z" fill="{color}"/>')
        start = end
    return ('<svg viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="49" fill="#fff" stroke="#d2d1c9" stroke-width=".5"/>'
            + "".join(paths) + "</svg>")


def plate():
    T = B.PLATE
    rows = "".join(f'<tr><th>{esc(a)}</th><td class="hand">{esc(b)}</td><td>{esc(c)}</td></tr>' for a, b, c in T["hand"])
    legend = "".join(f'<li class="pl-{i}"><i></i><b>{esc(a)}</b><span>{esc(b)}</span></li>' for i, (a, b) in enumerate(T["parts"]))
    inner = f"""
    <p class="eyebrow">Nutrition</p>
    <h2 class="h2">{esc(T["title"])}</h2>
    <p class="lead">{esc(T["lead"])}</p>
    <div class="plate-wrap"><div class="plate">{plate_svg()}</div><ul class="plate-legend">{legend}</ul></div>
    <h3 class="h3">Hand portions (per main meal)</h3>
    <table class="tbl hand-tbl"><thead><tr><th>Group</th><th>Portion</th><th>About the same as</th></tr></thead><tbody>{rows}</tbody></table>
    <div class="callout tint"><p>{esc(T["adjust"])}</p></div>
    <p class="note">{esc(T["rhythm"])}</p>
    <p class="caption">{esc(T["units"])}</p>
    """
    add("tabak", page(inner, "plain"), toc="The plate method and hand portions")


def shopping():
    cols = "".join(
        f'<div class="shop"><h3>{esc(cat)}</h3><ul>{"".join(f"<li>{box()}{esc(x)}</li>" for x in items)}</ul></div>'
        for cat, items in B.SHOPPING)
    inner = f"""
    <p class="eyebrow">Preparation</p>
    <h2 class="h2">Basic shopping list</h2>
    <p class="lead">Almost every meal in the plan is made with foods from this list. You don't need to buy everything at once.</p>
    <div class="shop-grid">{cols}</div>
    <div class="callout tint"><p>{esc(B.SHOPPING_TIP)}</p></div>
    """
    add("alisveris", page(inner, "plain"), toc="Basic shopping list")


def warmup():
    wu = "".join(f"<tr><td>{esc(a)}</td><td class='r'>{esc(b)}</td></tr>" for a, b in B.WARMUP)
    mob = "".join(f"<tr><td><b>{esc(a)}</b><span class='sub'>{esc(c)}</span></td><td class='r'>{esc(b)}</td></tr>"
                  for a, b, c in B.MOBILITY)
    inner = f"""
    <p class="eyebrow">Movement</p>
    <h2 class="h2">Warm-up, mobility and brisk walking</h2>
    <div class="split">
      <div><h3 class="h3">{icon("training", 16)} Warm-up · 5 minutes</h3>
        <p class="note">Before every workout.</p>
        <table class="tbl">{wu}</table></div>
      <div><h3 class="h3">{icon("movement", 16)} Brisk walk</h3>
        <p class="note">{esc(B.INTERVAL_WALK)}</p>
        <div class="walk"><span class="w1">Easy</span><span class="w2">2 min brisk</span><span class="w3">2 min easy</span><span class="w2">2 min brisk</span><span class="w3">…</span></div></div>
    </div>
    <h3 class="h3">{icon("habits", 16)} Mobility routine · 10 minutes</h3>
    <p class="note">On active recovery days and any evening you like.</p>
    <table class="tbl mob">{mob}</table>
    """
    add("isinma", page(inner, "plain"), toc="Warm-up, mobility and brisk walking")


def exercises():
    def card(e):
        how = "".join(f"<li>{esc(x)}</li>" for x in e["how"])
        return (f'<div class="ex"><h3>{esc(e["name"])}</h3><ol>{how}</ol>'
                f'<p class="alt"><b>Easier:</b> {esc(e["easy"])}</p>'
                f'<p class="alt"><b>Harder:</b> {esc(e["hard"])}</p></div>')

    rules = "".join(f"<li>{icon('check', 12)}<span>{esc(r)}</span></li>" for r in B.TRAINING_RULES)
    p1 = f"""
    <p class="eyebrow">Training</p>
    <h2 class="h2">Exercise guide</h2>
    <p class="lead">Every workout in the plan is made up of these 8 exercises. No equipment needed; for rows, a resistance band or a backpack is enough.</p>
    <div class="ex-grid">{"".join(card(e) for e in B.EXERCISES[:4])}</div>
    """
    p2 = f"""
    <div class="ex-grid">{"".join(card(e) for e in B.EXERCISES[4:])}</div>
    <div class="callout dark"><p class="label light"><span>TRAINING RULES</span></p><ul class="rules">{rules}</ul></div>
    """
    add("egzersiz", page(p1, "plain"), toc="Exercise guide")
    add("egzersiz2", page(p2, "plain"))


def progress():
    head = "".join(f"<th>{c}</th>" for c in B.PROGRESS_COLS)
    body = "".join(f"<tr><th>{esc(r)}</th>{'<td></td>' * len(B.PROGRESS_COLS)}</tr>" for r in B.PROGRESS_ROWS)
    how = "".join(f"<li><b>{esc(a)}:</b> {esc(b)}</li>" for a, b in B.MEASURE_HOW)
    inner = f"""
    <p class="eyebrow">Progress</p>
    <h2 class="h2">Progress tracker</h2>
    <ul class="how">{how}</ul>
    <table class="tbl grid-tbl"><thead><tr><th></th>{head}</tr></thead><tbody>{body}</tbody></table>
    <p class="label"><span>NOTES AND POSITIVE CHANGES</span></p>
    {lines(4)}
    <div class="callout tint"><p class="label"><span>WHY DOES WEIGHT FLUCTUATE?</span></p><p>{esc(B.FLUCTUATION)}</p></div>
    """
    add("ilerleme", page(inner, "plain"), toc="Progress tracker")


def habit_tracker():
    head = "".join(f"<th>{d}</th>" for d in range(1, 31))
    rows = ""
    for name, start in B.HABITS:
        cells = "".join(f'<td class="{"off" if d < start else ""}"></td>' for d in range(1, 31))
        rows += f'<tr><th><b>{esc(name)}</b><span>From day {start}</span></th>{cells}</tr>'
    inner = f"""
    <p class="eyebrow">Habits</p>
    <h2 class="h2">30-day habit tracker</h2>
    <p class="lead">Habits are added one at a time throughout the plan. Every evening, tick the ones you completed; gray boxes are habits that haven't started yet.</p>
    <table class="tracker"><thead><tr><th></th>{head}</tr></thead><tbody>{rows}</tbody></table>
    <div class="callout tint"><p>You don't have to complete all of them every day. The goal is to see the rows fill up over time. An empty box doesn't stop you from ticking the next day's box.</p></div>
    """
    add("aliskanlik", page(inner, "plain"), toc="Habit tracker")


def title_case(text):
    """"BUILD THE FOUNDATION" -> "Build the Foundation" (short words stay lowercase)."""
    small = {"a", "an", "and", "as", "at", "for", "in", "of", "on", "or", "the", "to"}
    words = text.lower().split()
    return " ".join(w if i and w in small else w[0].upper() + w[1:] for i, w in enumerate(words))


def phase_page(ph):
    goals = "".join(f"<li>{icon('check', 13)}<span>{esc(g)}</span></li>" for g in ph["goals"])
    chips = "".join(f"<span class='chip'>{esc(h)}</span>" for h in ph["habits"])
    days = [d for d in P.DAYS if ph["days"][0] <= d["n"] <= ph["days"][1]]
    if ph["n"] == 4:
        days = days + [{"n": 30, "title": "What comes next?", "training": {"kind": "recovery", "name": "Celebration walk"}}]
    sched = "".join(
        f"<tr><td class='dn'>Day {d['n']}</td><td>{esc(d['title'])}</td>"
        f"<td class='r {'st' if d['training']['kind'] == 'strength' else ''}'>{esc(d['training']['name'])}</td></tr>"
        for d in days)
    inner = f"""
    <p class="phase-kicker">PHASE {ph["n"]} · DAYS {ph["days"][0]}–{ph["days"][1]}</p>
    <h2 class="phase-title">{esc(ph["name"])}</h2>
    <p class="lead">{esc(ph["lead"])}</p>
    <div class="split">
      <div><p class="label"><span>IN THIS PHASE</span></p><ul class="goals">{goals}</ul></div>
      <div><p class="label"><span>NEW HABITS</span></p><div class="chips">{chips}</div>
        <div class="callout white"><p>{esc(ph["note"])}</p></div></div>
    </div>
    <p class="label"><span>THIS PHASE AT A GLANCE</span></p>
    <table class="tbl sched">{sched}</table>
    """
    add(f"faz{ph['n']}", page(inner, "phase"),
        toc=f"Phase {ph['n']} · {title_case(ph['name'])} (Days {ph['days'][0]}–{ph['days'][1]})")


def phase_of(n):
    return next(ph for ph in P.PHASES if ph["days"][0] <= n <= ph["days"][1])


def checkin(training_day=True):
    items = ["Task done", "Movement goal done", "Followed the nutrition plan",
             "Workout done" if training_day else "Workout (none today)"]
    checks = "".join(f"<li class='{'' if training_day or i < 3 else 'muted'}'>{box()}{esc(t)}</li>" for i, t in enumerate(items))
    water = "".join("<i></i>" for _ in range(10))
    energy = "".join(f"<i>{i}</i>" for i in range(1, 6))
    return f"""
    <section class="checkin">
      <p class="label">{icon("check")}<span>END-OF-DAY CHECK-IN</span></p>
      <div class="checkin-row"><ul class="checks">{checks}</ul>
        <div class="trackers"><div><span>Water</span><div class="water">{water}</div></div>
        <div><span>Energy</span><div class="energy">{energy}</div></div></div></div>
    </section>"""


def notes():
    # Real lines (not a CSS pattern): patterns make PDF viewers slow. Extra lines are clipped.
    return ('<section class="notes"><p class="label muted-label"><span>MY NOTES</span></p>'
            '<div class="note-lines">' + "<span></span>" * 18 + "</div></section>")


def training_block(t):
    if t["kind"] == "strength":
        rows = "".join(f"<tr><td>{esc(a)}</td><td class='r'>{esc(b)}</td></tr>" for a, b in t["rows"])
        note = f"<p class='note'>{esc(t['note'])}</p>" if t.get("note") else ""
        extra = f"<p class='extra'>{esc(t['extra'])}</p>" if t.get("extra") else ""
        return f"""
        <p class="t-name">{esc(t["name"])} <span>· {esc(t["type"])}</span></p>
        <p class="t-meta">5-min warm-up first · Rest {esc(t["rest"])} between sets</p>
        <table class="tbl ex-tbl">{rows}</table>{note}{extra}"""
    return f"""<p class="t-name">{esc(t["name"])}</p><p class="t-text">{esc(t["text"])}</p>"""


def day_page(d):
    ph = phase_of(d["n"])
    meals = "".join(f"<tr><th>{esc(a)}</th><td>{esc(b)}</td></tr>" for a, b in d["meals"])
    t = d["training"]
    inner = f"""
    <header class="day-head">
      <div class="day-num"><span>DAY</span><strong>{two(d["n"])}</strong><em>/ 30</em></div>
      <div class="day-meta"><p>PHASE {ph["n"]} · {esc(ph["name"])}</p>{bar(d["n"])}</div>
    </header>
    <section class="focus">
      {label("TODAY'S FOCUS", "focus")}
      <h2>{esc(d["title"])}</h2>
      <p>{esc(d["focus"])}</p>
    </section>
    <section class="block">
      {label("NUTRITION", "nutrition")}
      <p class="rule">{esc(d["nutrition"])}</p>
      <table class="meals">{meals}</table>
    </section>
    <div class="cols">
      <section class="block move">
        {label("MOVEMENT", "movement")}
        <p class="goal">{esc(d["movement"][0])}</p>
        <p class="t-text">{esc(d["movement"][1])}</p>
      </section>
      <section class="block train {'rest' if t['kind'] != 'strength' else ''}">
        {label("WORKOUT", "training")}
        {training_block(t)}
      </section>
    </div>
    <div class="cols">
      <section class="tip">{label("TIP OF THE DAY", "tips")}<p>{esc(d["tip"])}</p></section>
      <section class="task">{label("TASK OF THE DAY", "task")}<p>{esc(d["task"])}</p></section>
    </div>
    {notes()}
    {checkin(t["kind"] == "strength")}
    """
    add(f"gun{d['n']}", page(inner, "day"),
        toc=None)


def week_review(w):
    rows = ""
    for h in P.WEEK_HABITS:
        n = 3 if h.startswith("Workout") else 7
        rows += f"<tr><th>{esc(h)}</th><td>{box() * n}</td></tr>"
    days = {1: (1, 7), 2: (8, 14), 3: (15, 21)}[w]
    meas = "".join(f"<div class='field'><span>{esc(x)}</span><i></i></div>"
                   for x in ["Weight", "Waist", "Energy (1–5)", "Average sleep"])
    qs = [("What went best this week?", 2), ("Where did I struggle most?", 2),
          ("My one focus for next week:", 1)]
    q = "".join(f"<p class='q'>{esc(a)}</p>{lines(n)}" for a, n in qs)
    inner = f"""
    <p class="eyebrow">Days {days[0]}–{days[1]}</p>
    <h2 class="h2">Week {w} review</h2>
    <p class="lead">{esc(P.WEEK_REVIEWS[w])}</p>
    <p class="label"><span>HOW MANY DAYS THIS WEEK?</span></p>
    <table class="tbl week">{rows}</table>
    <p class="label"><span>MEASUREMENTS</span></p>
    <div class="fields">{meas}</div>
    <p class="caption">Also write the values in the Progress Tracker (p. {{p:ilerleme}}).</p>
    {q}
    """
    add(f"hafta{w}", page(inner, "plain"), toc=f"Week {w} review")


def day30():
    D = P.DAY30
    meals = "".join(f"<tr><th>{esc(a)}</th><td>{esc(b)}</td></tr>" for a, b in D["meals"])
    inner = f"""
    <header class="day-head">
      <div class="day-num"><span>DAY</span><strong>30</strong><em>/ 30</em></div>
      <div class="day-meta"><p>PHASE 4 · {esc(P.PHASES[3]["name"])}</p>{bar(30)}</div>
    </header>
    <section class="focus final">
      {label("TODAY'S FOCUS", "focus")}
      <h2>{esc(D["title"])}</h2>
      <p>{esc(D["focus"])}</p>
    </section>
    <section class="block">
      {label("NUTRITION", "nutrition")}
      <p class="rule">{esc(D["nutrition"])}</p>
      <table class="meals">{meals}</table>
    </section>
    <div class="cols">
      <section class="block move">{label("MOVEMENT", "movement")}<p class="goal">{esc(D["movement"][0])}</p><p class="t-text">{esc(D["movement"][1])}</p></section>
      <section class="block train rest">{label("WORKOUT", "training")}<p class="t-text">{esc(D["training"])}</p></section>
    </div>
    <section class="task wide">{label("TASK OF THE DAY", "task")}<p>{esc(D["task"])}</p></section>
    {notes()}
    {checkin(False)}
    """
    add("gun30", page(inner, "day"), toc="Day 30: What comes next?")
    qs = "".join(f"<p class='q'>{i}. {esc(q)}</p>{lines(3)}" for i, q in enumerate(D["questions"], 1))
    add("geriye", page(f"""
    <p class="eyebrow">Day 30</p>
    <h2 class="h2">Look back</h2>
    <p class="lead">Short answers are enough. This page is for seeing what the 30 days gave you.</p>
    {qs}""", "plain"), toc="Look back")


def continue_page():
    C = P.CONTINUE
    rules = "".join(f"<li><b>{esc(a)}</b> {esc(b)}</li>" for a, b in C["rules"])
    prog = "".join(f"<tr><th>{esc(a)}</th><td>{esc(b)}</td></tr>" for a, b in C["progression"])
    head = "".join(f"<th>{esc(c)}</th>" for c in C["template_cols"])
    body = "".join(f"<tr><th>Week {i}</th>{'<td></td>' * len(C['template_cols'])}</tr>" for i in range(1, 5))
    inner = f"""
    <h2 class="h2">{esc(C["title"])}</h2>
    <p class="lead">{esc(C["lead"])}</p>
    <p class="label"><span>5 RULES FOR WHAT COMES NEXT</span></p>
    <ol class="rules-num">{rules}</ol>
    <p class="label"><span>MAKE YOUR WORKOUTS HARDER STEP BY STEP</span></p>
    <table class="tbl">{prog}</table>
    <p class="label"><span>THE NEXT 4 WEEKS</span></p>
    <table class="tbl grid-tbl tpl"><thead><tr><th></th>{head}</tr></thead><tbody>{body}</tbody></table>
    """
    add("devam", page(inner, "plain"), toc="The next 4 weeks: your plan")


def closing():
    C = P.CLOSING
    title = "<br>".join(esc(x) for x in C["title"].split("\n"))
    text = "".join(f"<p>{esc(p)}</p>" for p in C["text"])
    inner = f"""
    <div class="closing">
      <h2>{title}</h2>
      <div class="closing-text">{text}</div>
      <p class="signoff">{esc(C["signoff"])}</p>
      <div class="brand"><span>LEAN MODE PRO</span><em>leanmodepro.com</em></div>
    </div>"""
    add("kapanis", page(inner, "cover closing-page", footer=False), toc="Closing")


def build():
    cover()
    toc_page()
    how_to()
    intro()
    basics()
    plate()
    shopping()
    warmup()
    exercises()
    progress()
    habit_tracker()
    for ph in P.PHASES:
        phase_page(ph)
        for d in P.DAYS:
            if ph["days"][0] <= d["n"] <= ph["days"][1]:
                day_page(d)
        if ph["n"] < 4:
            week_review(ph["n"])
    day30()
    continue_page()
    closing()

    numbers = {p["key"]: i + 1 for i, p in enumerate(pages)}

    toc_items = []
    for p in pages:
        if p["toc"]:
            toc_items.append((p["toc"], numbers[p["key"]], p["key"].startswith("faz")))
        if p["key"].startswith("faz"):
            ph = P.PHASES[int(p["key"][3:]) - 1]
            first, last = ph["days"]
            toc_items.append((f"Days {first}–{last}", numbers[f"gun{first}"], None))
    toc_html = "".join(
        f'<div class="toc-row {"toc-phase" if strong else ""} {"toc-sub" if strong is None else ""}">'
        f'<span>{esc(t)}</span><i></i><b>{n}</b></div>' for t, n, strong in toc_items)

    out = []
    for p in pages:
        h = p["html"].replace("{toc}", toc_html).replace("{pageno}", str(numbers[p["key"]]))
        h = re.sub(r"\{p:(\w+)\}", lambda m: str(numbers[m.group(1)]), h)
        out.append(h)
    return "".join(out), len(pages)


def font_face():
    """Static Instrument Sans, one file per weight (ebook/fonts, SIL OFL).

    - Static instead of variable: variable fonts end up as slow Type 3 glyph drawings in the PDF.
    - One file per weight with Latin and Latin Extended merged: split subsets would switch fonts
      inside words with accented letters, which breaks search and copy in PDF viewers.
    """
    faces = []
    for weight in (400, 500, 600, 700):
        with open(os.path.join(FONT_DIR, f"instrument-sans-{weight}.woff2"), "rb") as fh:
            data = base64.b64encode(fh.read()).decode()
        faces.append(f"@font-face{{font-family:'Instrument Sans';font-weight:{weight};font-style:normal;"
                     f"src:url(data:font/woff2;base64,{data}) format('woff2')}}")
    return "\n".join(faces)


if __name__ == "__main__":
    body, count = build()
    with open(os.path.join(ROOT, "style.css"), encoding="utf-8") as fh:
        css = fh.read()
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>LEAN MODE PRO · The 30-Day Weight Loss Plan</title>
<meta name="author" content="LEAN MODE PRO">
<style>{font_face()}
{css}</style></head><body>{body}</body></html>"""
    os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
    with open(os.path.join(ROOT, "dist", "ebook.html"), "w", encoding="utf-8") as fh:
        fh.write(doc)
    print(f"ebook.html written, {count} pages")

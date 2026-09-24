"""Elementor site settings (kit): global colours, fonts and layout defaults."""
import json
from tokens import *

system_colors = [
    {"_id": "primary", "title": "Primär", "color": color_hex("lmpaccent")},
    {"_id": "secondary", "title": "Sekundär", "color": color_hex("lmpink")},
    {"_id": "text", "title": "Text", "color": color_hex("lmptext")},
    {"_id": "accent", "title": "Akzentfarbe", "color": color_hex("lmpaccent")},
]
custom_colors = [{"_id": k, "title": v[0], "color": v[1]} for k, v in COLORS.items()]

def sys_typo(_id, title, weight):
    return {"_id": _id, "title": title, "typography_typography": "custom",
            "typography_font_family": FONT, "typography_font_weight": str(weight)}

system_typography = [
    sys_typo("primary", "Primär", 600), sys_typo("secondary", "Sekundär", 500),
    {**sys_typo("text", "Text", 400), "typography_font_size": px(17), "typography_line_height": px(1.6, "em")},
    sys_typo("accent", "Akzent", 600),
]
custom_typography = [{"_id": k, "title": v[0], **v[1]} for k, v in TYPO.items()]

settings = {
    "system_colors": system_colors,
    "custom_colors": custom_colors,
    "system_typography": system_typography,
    "custom_typography": custom_typography,
    "default_generic_fonts": "Sans-serif",
    "body_background_background": "classic",
    "body_background_color": color_hex("lmpbg"),
    "body_color": color_hex("lmptext"),
    "body_typography_typography": "custom",
    "body_typography_font_family": FONT,
    "body_typography_font_size": px(17),
    "body_typography_line_height": px(1.6, "em"),
    "link_normal_color": color_hex("lmpaccent"),
    "link_hover_color": color_hex("lmpaccenthover"),
    "container_width": px(1180),
    "container_padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True},
    "space_between_widgets": {"column": "16", "row": "16", "isLinked": True, "unit": "px"},
    "page_title_selector": "h1.entry-title",
}

if __name__ == "__main__":
    import sys
    json.dump(settings, sys.stdout, ensure_ascii=False, indent=1)

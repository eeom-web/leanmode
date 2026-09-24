FONT = "Instrument Sans"

COLORS = {  # id -> (title, hex)
    "lmpaccent": ("Akzent Grün", "#1D5A48"),
    "lmpaccenthover": ("Akzent Hover", "#164A3B"),
    "lmpbg": ("Hintergrund", "#F6F5F1"),
    "lmpbgalt": ("Hintergrund Alt", "#EFEEE8"),
    "lmpsurface": ("Fläche Weiß", "#FFFFFF"),
    "lmpink": ("Tinte", "#101614"),
    "lmpinksoft": ("Tinte Soft", "#27302C"),
    "lmptext": ("Fließtext", "#414B46"),
    "lmpmuted": ("Gedämpft", "#5D6762"),
    "lmpline": ("Linie", "#E3E2DB"),
    "lmplinestrong": ("Linie Stark", "#D2D1C9"),
    "lmpaccentsoft": ("Akzent Soft", "#E3EDE7"),
    "lmpaccenttint": ("Akzent Hauch", "#EEF4F0"),
    "lmpmint": ("Mint", "#A9D4BF"),
    "lmpdark": ("Dunkel", "#0F1D19"),
    "lmpondark": ("Auf Dunkel", "#EEF2EF"),
    "lmpondarkmuted": ("Auf Dunkel Gedämpft", "#A7B6AF"),
}

def px(v, unit="px"):
    return {"unit": unit, "size": v, "sizes": []}

def typo(size, weight, lh, ls=None, lh_unit="em", ls_unit="em", size_t=None, size_m=None, transform=None):
    d = {
        "typography_typography": "custom",
        "typography_font_family": FONT,
        "typography_font_weight": str(weight),
        "typography_font_size": px(size),
        "typography_line_height": px(lh, lh_unit),
    }
    if ls is not None:
        d["typography_letter_spacing"] = px(ls, ls_unit)
    if size_t is not None:
        d["typography_font_size_tablet"] = px(size_t)
    if size_m is not None:
        d["typography_font_size_mobile"] = px(size_m)
    if transform:
        d["typography_text_transform"] = transform
    return d

# Global typography presets: id -> (title, settings)
TYPO = {
    "lmpdisplay": ("H1 Display", typo(76, 600, 1.02, -0.032, size_t=56, size_m=40)),
    "lmph2": ("H2 Sektion", typo(52, 600, 1.08, -0.026, size_t=42, size_m=32)),
    "lmph3": ("H3 Karte", typo(19, 600, 1.25, -0.015)),
    "lmplead": ("Lead", typo(21, 400, 1.55, size_t=19, size_m=18)),
    "lmpbody": ("Fließtext", typo(17, 400, 1.6)),
    "lmpsmall": ("Klein", typo(14, 500, 1.5)),
    "lmplabel": ("Label", typo(13, 600, 1.3, 0.12, transform="uppercase")),
    "lmpbutton": ("Button", typo(16, 600, 1.2, -0.005)),
}

def color_hex(cid):
    return COLORS[cid][1]

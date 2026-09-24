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
FONT_DIR = os.path.join(ROOT, "..", "node_modules", "@fontsource-variable", "instrument-sans", "files")

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
    # Keep ranges such as "1–10" or "8.000–10.000" on one line (U+2060 word joiner).
    text = re.sub(r"(\d)–(\d)", "\\1\u2060–\u2060\\2", html.escape(text, quote=False))
    # Ordinals such as "16. gün" stay together.
    return re.sub(r"(\d)\. (?=[a-zçğıöşü])", "\\1.\u00a0", text)


# Turkish case suffixes after numerals follow the pronunciation of the last number word,
# e.g. 3'ten (üç), 6'dan (altı), 10'da (on), 12'de (on iki).
_UNITS = {1: (False, False), 2: (False, False), 3: (False, True), 4: (False, True), 5: (False, True),
          6: (True, False), 7: (False, False), 8: (False, False), 9: (True, False)}
_TENS = {10: (True, False), 20: (False, False), 30: (True, False), 40: (True, True), 50: (False, False),
         60: (True, True), 70: (False, True), 80: (False, False), 90: (True, False)}


def with_suffix(n, kind):
    """kind: 'de' (locative), 'den' (ablative) or 'deki'."""
    back, hard = _UNITS[n % 10] if n % 10 else _TENS.get(n % 100, (False, True))
    stem = ("t" if hard else "d") + ("a" if back else "e")
    return f"{n}'" + {"de": stem, "den": stem + "n", "deki": stem + "ki"}[kind]


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
    foot = ('<footer class="foot"><span>LEAN MODE PRO</span><span>30 Günlük Kilo Verme Planı</span>'
            '<span class="pn">{pageno}</span></footer>') if footer else ""
    return f'<section class="page {cls}">{inner}{foot}</section>'


def cover():
    dots = "".join('<i class="on"></i>' if i == 0 else "<i></i>" for i in range(30))
    inner = f"""
    <div class="cover-top"><span>LEAN MODE PRO</span><span>ÜCRETSİZ E-KİTAP</span></div>
    <div class="cover-main">
      <p class="cover-kicker">30 GÜNLÜK</p>
      <h1 class="cover-title">KİLO VERME<br>PLANI</h1>
      <p class="cover-sub">Adım Adım Rehber</p>
      <p class="cover-subtitle">{esc(B.SUBTITLE)}</p>
    </div>
    <div class="cover-dots">{dots}</div>
    <p class="cover-tags">Beslenme • Antrenman • Hareket • Alışkanlıklar</p>
    """
    add("cover", page(inner, "cover", footer=False))


def toc_page():
    add("toc", page('<h2 class="h2">İçindekiler</h2><div class="toc">{toc}</div>', "plain"))


def how_to():
    steps = "".join(f'<li><strong>{esc(a)}</strong><span>{esc(b)}</span></li>' for a, b in B.HOW_TO_USE)
    legend = [("focus", "BUGÜNÜN ODAĞI", "Günün tek konusu"), ("nutrition", "BESLENME", "Öğün önerileri"),
              ("movement", "HAREKET", "Adım veya yürüyüş hedefi"), ("training", "ANTRENMAN", "Kuvvet veya toparlanma"),
              ("tips", "BUGÜNÜN İPUCU", "Pratik bir bilgi"), ("task", "GÜNÜN GÖREVİ", "Bugün yapacağın küçük adım")]
    leg = "".join(f'<div class="leg">{icon(i, 16)}<div><b>{a}</b><span>{b}</span></div></div>' for i, a, b in legend)
    inner = f"""
    <p class="eyebrow">Başlamadan önce</p>
    <h2 class="h2">Bu rehber nasıl kullanılır?</h2>
    <ol class="steps">{steps}</ol>
    <div class="callout tint"><p>{esc(B.MISSED_DAY)}</p></div>
    <h3 class="h3">Her günün sayfasında</h3>
    <div class="legend">{leg}</div>
    <div class="callout warn"><p class="label"><span>ÖNEMLİ NOT</span></p><p>{esc(B.DISCLAIMER)}</p></div>
    """
    add("kullanim", page(inner, "plain"), toc="Bu rehber nasıl kullanılır?")


def intro():
    I = B.INTRO
    paras = "".join(f"<p>{esc(p)}</p>" for p in I["paragraphs"])
    pts = "".join(f'<li>{icon("check", 14)}<div><b>{esc(a)}</b> {esc(b)}</div></li>' for a, b in I["points"])
    phases = "".join(
        f'<div class="phase-mini"><span>FAZ {ph["n"]}</span><b>{esc(ph["name"])}</b><em>Gün {ph["days"][0]}–{ph["days"][1]}</em></div>'
        for ph in P.PHASES)
    inner = f"""
    <p class="eyebrow">Giriş</p>
    <h2 class="h2">{esc(I["title"])}</h2>
    <div class="prose">{paras}</div>
    <ul class="points">{pts}</ul>
    <p class="lead">{esc(I["closing"])}</p>
    <h3 class="h3">30 gün, 4 faz</h3>
    <div class="phase-row">{phases}</div>
    <p class="caption">Her faz bir öncekinin üzerine kurulur. Yeni alışkanlıklar tek tek eklenir.</p>
    <div class="callout tint"><p class="label"><span>GERÇEKÇİ BEKLENTİ</span></p><p>{esc(I["expectation"])}</p></div>
    """
    add("giris", page(inner, "plain"), toc="Giriş: Neden 30 günlük bir plan?")


def basics():
    cards = [f'<div class="card"><h3>{esc(t)}</h3><p>{esc(x)}</p><p class="plan-line"><b>Planda:</b> {esc(pl)}</p></div>'
             for t, x, pl in B.BASICS]
    no = "".join(f"<li>{esc(x)}</li>" for x in B.NOT_IN_PLAN)
    roadmap = "".join(f"<li><span>Gün {n}</span>{esc(t)}</li>" for n, t in B.HABIT_ROADMAP)
    p1 = f"""
    <p class="eyebrow">1. günden önce</p>
    <h2 class="h2">Bilmen gereken 7 temel</h2>
    <p class="lead">Kısa ve sade: Plan boyunca yapacağın her şeyin arkasındaki mantık.</p>
    <div class="cards">{"".join(cards[:4])}</div>
    """
    p2 = f"""
    <p class="eyebrow">1. günden önce</p>
    <div class="cards">{"".join(cards[4:])}
      <div class="card dark-card"><p class="label light"><span>BU PLANDA NELER YOK?</span></p><ul class="nolist">{no}</ul></div>
    </div>
    <h3 class="h3">{icon("habits", 16)} Alışkanlıklar tek tek eklenir</h3>
    <p class="note">Her şeyi aynı anda değiştirmiyorsun. Yeni bir alışkanlık, bir öncekinin üzerine eklenir.</p>
    <ol class="roadmap">{roadmap}</ol>
    """
    add("temel", page(p1, "plain"), toc="Bilmen gereken 7 temel")
    add("temel2", page(p2, "plain"))


def plate():
    T = B.PLATE
    rows = "".join(f'<tr><th>{esc(a)}</th><td class="hand">{esc(b)}</td><td>{esc(c)}</td></tr>' for a, b, c in T["hand"])
    legend = "".join(f'<li class="pl-{i}"><i></i><b>{esc(a)}</b><span>{esc(b)}</span></li>' for i, (a, b) in enumerate(T["parts"]))
    inner = f"""
    <p class="eyebrow">Beslenme</p>
    <h2 class="h2">{esc(T["title"])}</h2>
    <p class="lead">{esc(T["lead"])}</p>
    <div class="plate-wrap"><div class="plate"><div class="plate-in"></div></div><ul class="plate-legend">{legend}</ul></div>
    <h3 class="h3">El ölçüsü (her ana öğün için)</h3>
    <table class="tbl hand-tbl"><thead><tr><th>Grup</th><th>Ölçü</th><th>Yaklaşık karşılığı</th></tr></thead><tbody>{rows}</tbody></table>
    <div class="callout tint"><p>{esc(T["adjust"])}</p></div>
    <p class="note">{esc(T["rhythm"])}</p>
    <p class="caption">{esc(T["units"])}</p>
    """
    add("tabak", page(inner, "plain"), toc="Tabak modeli ve el ölçüsü")


def shopping():
    cols = "".join(
        f'<div class="shop"><h3>{esc(cat)}</h3><ul>{"".join(f"<li>{box()}{esc(x)}</li>" for x in items)}</ul></div>'
        for cat, items in B.SHOPPING)
    inner = f"""
    <p class="eyebrow">Hazırlık</p>
    <h2 class="h2">Temel alışveriş listesi</h2>
    <p class="lead">Plandaki öğünlerin neredeyse tamamı bu listedeki yiyeceklerle hazırlanır. Hepsini aynı anda almana gerek yok.</p>
    <div class="shop-grid">{cols}</div>
    <div class="callout tint"><p>{esc(B.SHOPPING_TIP)}</p></div>
    """
    add("alisveris", page(inner, "plain"), toc="Temel alışveriş listesi")


def warmup():
    wu = "".join(f"<tr><td>{esc(a)}</td><td class='r'>{esc(b)}</td></tr>" for a, b in B.WARMUP)
    mob = "".join(f"<tr><td><b>{esc(a)}</b><span class='sub'>{esc(c)}</span></td><td class='r'>{esc(b)}</td></tr>"
                  for a, b, c in B.MOBILITY)
    inner = f"""
    <p class="eyebrow">Hareket</p>
    <h2 class="h2">Isınma, mobilite ve tempolu yürüyüş</h2>
    <div class="split">
      <div><h3 class="h3">{icon("training", 16)} Isınma · 5 dakika</h3>
        <p class="note">Her antrenmandan önce.</p>
        <table class="tbl">{wu}</table></div>
      <div><h3 class="h3">{icon("movement", 16)} Tempolu yürüyüş</h3>
        <p class="note">{esc(B.INTERVAL_WALK)}</p>
        <div class="walk"><span class="w1">Rahat</span><span class="w2">2 dk tempolu</span><span class="w3">2 dk rahat</span><span class="w2">2 dk tempolu</span><span class="w3">…</span></div></div>
    </div>
    <h3 class="h3">{icon("habits", 16)} Mobilite rutini · 10 dakika</h3>
    <p class="note">Aktif toparlanma günlerinde ve istediğin her akşam.</p>
    <table class="tbl mob">{mob}</table>
    """
    add("isinma", page(inner, "plain"), toc="Isınma, mobilite ve tempolu yürüyüş")


def exercises():
    def card(e):
        how = "".join(f"<li>{esc(x)}</li>" for x in e["how"])
        return (f'<div class="ex"><h3>{esc(e["name"])}</h3><ol>{how}</ol>'
                f'<p class="alt"><b>Kolay versiyon:</b> {esc(e["easy"])}</p>'
                f'<p class="alt"><b>Zorlaştırmak için:</b> {esc(e["hard"])}</p></div>')

    rules = "".join(f"<li>{icon('check', 12)}<span>{esc(r)}</span></li>" for r in B.TRAINING_RULES)
    p1 = f"""
    <p class="eyebrow">Antrenman</p>
    <h2 class="h2">Egzersiz rehberi</h2>
    <p class="lead">Plandaki bütün antrenmanlar bu 8 hareketten oluşur. Ekipman gerekmez; çekiş için bir lastik bant veya sırt çantası yeterli.</p>
    <div class="ex-grid">{"".join(card(e) for e in B.EXERCISES[:4])}</div>
    """
    p2 = f"""
    <div class="ex-grid">{"".join(card(e) for e in B.EXERCISES[4:])}</div>
    <div class="callout dark"><p class="label light"><span>ANTRENMAN KURALLARI</span></p><ul class="rules">{rules}</ul></div>
    """
    add("egzersiz", page(p1, "plain"), toc="Egzersiz rehberi")
    add("egzersiz2", page(p2, "plain"))


def progress():
    head = "".join(f"<th>{c}</th>" for c in B.PROGRESS_COLS)
    body = "".join(f"<tr><th>{esc(r)}</th>{'<td></td>' * len(B.PROGRESS_COLS)}</tr>" for r in B.PROGRESS_ROWS)
    how = "".join(f"<li><b>{esc(a)}:</b> {esc(b)}</li>" for a, b in B.MEASURE_HOW)
    inner = f"""
    <p class="eyebrow">İlerleme</p>
    <h2 class="h2">İlerleme tablosu</h2>
    <ul class="how">{how}</ul>
    <table class="tbl grid-tbl"><thead><tr><th></th>{head}</tr></thead><tbody>{body}</tbody></table>
    <p class="label"><span>NOTLAR VE OLUMLU DEĞİŞİKLİKLER</span></p>
    {lines(4)}
    <div class="callout tint"><p class="label"><span>KİLO NEDEN DALGALANIR?</span></p><p>{esc(B.FLUCTUATION)}</p></div>
    """
    add("ilerleme", page(inner, "plain"), toc="İlerleme tablosu")


def habit_tracker():
    head = "".join(f"<th>{d}</th>" for d in range(1, 31))
    rows = ""
    for name, start in B.HABITS:
        cells = "".join(f'<td class="{"off" if d < start else ""}"></td>' for d in range(1, 31))
        rows += f'<tr><th><b>{esc(name)}</b><span>Gün {with_suffix(start, "den")} itibaren</span></th>{cells}</tr>'
    inner = f"""
    <p class="eyebrow">Alışkanlıklar</p>
    <h2 class="h2">30 günlük alışkanlık takibi</h2>
    <p class="lead">Alışkanlıklar plan boyunca tek tek eklenir. Her akşam tamamladıklarını işaretle; gri kutular henüz başlamayan alışkanlıklar.</p>
    <table class="tracker"><thead><tr><th></th>{head}</tr></thead><tbody>{rows}</tbody></table>
    <div class="callout tint"><p>Hepsini her gün tamamlaman gerekmiyor. Amaç, satırların zamanla dolduğunu görmek. Boş bir kutu, bir sonraki günün kutusunu işaretlemene engel değil.</p></div>
    """
    add("aliskanlik", page(inner, "plain"), toc="Alışkanlık takibi")


def tr_title(text):
    """Title case with Turkish dotted/dotless i rules ("TEMELLERİ OLUŞTUR" -> "Temelleri Oluştur")."""
    def low(w):
        return w.replace("I", "ı").replace("İ", "i").lower()
    return " ".join(w[0] + low(w[1:]) for w in text.split())


def phase_page(ph):
    goals = "".join(f"<li>{icon('check', 13)}<span>{esc(g)}</span></li>" for g in ph["goals"])
    chips = "".join(f"<span class='chip'>{esc(h)}</span>" for h in ph["habits"])
    days = [d for d in P.DAYS if ph["days"][0] <= d["n"] <= ph["days"][1]]
    if ph["n"] == 4:
        days = days + [{"n": 30, "title": "Buradan sonra ne olacak?", "training": {"kind": "recovery", "name": "Kutlama yürüyüşü"}}]
    sched = "".join(
        f"<tr><td class='dn'>Gün {d['n']}</td><td>{esc(d['title'])}</td>"
        f"<td class='r {'st' if d['training']['kind'] == 'strength' else ''}'>{esc(d['training']['name'])}</td></tr>"
        for d in days)
    inner = f"""
    <p class="phase-kicker">FAZ {ph["n"]} · GÜN {ph["days"][0]}–{ph["days"][1]}</p>
    <h2 class="phase-title">{esc(ph["name"])}</h2>
    <p class="lead">{esc(ph["lead"])}</p>
    <div class="split">
      <div><p class="label"><span>BU FAZDA</span></p><ul class="goals">{goals}</ul></div>
      <div><p class="label"><span>YENİ ALIŞKANLIKLAR</span></p><div class="chips">{chips}</div>
        <div class="callout white"><p>{esc(ph["note"])}</p></div></div>
    </div>
    <p class="label"><span>BU FAZIN PROGRAMI</span></p>
    <table class="tbl sched">{sched}</table>
    """
    add(f"faz{ph['n']}", page(inner, "phase"),
        toc=f"Faz {ph['n']} · {tr_title(ph['name'])} (Gün {ph['days'][0]}–{ph['days'][1]})")


def phase_of(n):
    return next(ph for ph in P.PHASES if ph["days"][0] <= n <= ph["days"][1])


def checkin(training_day=True):
    items = ["Görev tamamlandı", "Hareket hedefi tamamlandı", "Beslenme planına uyuldu",
             "Antrenman tamamlandı" if training_day else "Antrenman (bugün yok)"]
    checks = "".join(f"<li class='{'' if training_day or i < 3 else 'muted'}'>{box()}{esc(t)}</li>" for i, t in enumerate(items))
    water = "".join("<i></i>" for _ in range(10))
    energy = "".join(f"<i>{i}</i>" for i in range(1, 6))
    return f"""
    <section class="checkin">
      <p class="label">{icon("check")}<span>GÜN SONU KONTROLÜ</span></p>
      <div class="checkin-row"><ul class="checks">{checks}</ul>
        <div class="trackers"><div><span>Su</span><div class="water">{water}</div></div>
        <div><span>Enerji</span><div class="energy">{energy}</div></div></div></div>
    </section>"""


def notes():
    return '<section class="notes"><p class="label muted-label"><span>NOTLARIM</span></p><div class="note-lines"></div></section>'


def training_block(t):
    if t["kind"] == "strength":
        rows = "".join(f"<tr><td>{esc(a)}</td><td class='r'>{esc(b)}</td></tr>" for a, b in t["rows"])
        note = f"<p class='note'>{esc(t['note'])}</p>" if t.get("note") else ""
        extra = f"<p class='extra'>{esc(t['extra'])}</p>" if t.get("extra") else ""
        return f"""
        <p class="t-name">{esc(t["name"])} <span>· {esc(t["type"])}</span></p>
        <p class="t-meta">Önce 5 dk ısınma · Setler arası {esc(t["rest"])} dinlenme</p>
        <table class="tbl ex-tbl">{rows}</table>{note}{extra}"""
    return f"""<p class="t-name">{esc(t["name"])}</p><p class="t-text">{esc(t["text"])}</p>"""


def day_page(d):
    ph = phase_of(d["n"])
    meals = "".join(f"<tr><th>{esc(a)}</th><td>{esc(b)}</td></tr>" for a, b in d["meals"])
    t = d["training"]
    inner = f"""
    <header class="day-head">
      <div class="day-num"><span>GÜN</span><strong>{two(d["n"])}</strong><em>/ 30</em></div>
      <div class="day-meta"><p>FAZ {ph["n"]} · {esc(ph["name"])}</p>{bar(d["n"])}</div>
    </header>
    <section class="focus">
      {label("BUGÜNÜN ODAĞI", "focus")}
      <h2>{esc(d["title"])}</h2>
      <p>{esc(d["focus"])}</p>
    </section>
    <section class="block">
      {label("BESLENME", "nutrition")}
      <p class="rule">{esc(d["nutrition"])}</p>
      <table class="meals">{meals}</table>
    </section>
    <div class="cols">
      <section class="block move">
        {label("HAREKET", "movement")}
        <p class="goal">{esc(d["movement"][0])}</p>
        <p class="t-text">{esc(d["movement"][1])}</p>
      </section>
      <section class="block train {'rest' if t['kind'] != 'strength' else ''}">
        {label("ANTRENMAN", "training")}
        {training_block(t)}
      </section>
    </div>
    <div class="cols">
      <section class="tip">{label("BUGÜNÜN İPUCU", "tips")}<p>{esc(d["tip"])}</p></section>
      <section class="task">{label("GÜNÜN GÖREVİ", "task")}<p>{esc(d["task"])}</p></section>
    </div>
    {notes()}
    {checkin(t["kind"] == "strength")}
    """
    add(f"gun{d['n']}", page(inner, "day"),
        toc=None)


def week_review(w):
    rows = ""
    for h in P.WEEK_HABITS:
        n = 3 if h.startswith("Antrenman") else 7
        rows += f"<tr><th>{esc(h)}</th><td>{box() * n}</td></tr>"
    days = {1: (1, 7), 2: (8, 14), 3: (15, 21)}[w]
    meas = "".join(f"<div class='field'><span>{esc(x)}</span><i></i></div>"
                   for x in ["Kilo", "Bel çevresi", "Enerji (1–5)", "Ortalama uyku"])
    qs = [("Bu hafta en iyi giden şey neydi?", 2), ("En çok nerede zorlandım?", 2),
          ("Gelecek hafta tek odak noktam:", 1)]
    q = "".join(f"<p class='q'>{esc(a)}</p>{lines(n)}" for a, n in qs)
    inner = f"""
    <p class="eyebrow">Gün {days[0]}–{days[1]}</p>
    <h2 class="h2">{w}. hafta değerlendirmesi</h2>
    <p class="lead">{esc(P.WEEK_REVIEWS[w])}</p>
    <p class="label"><span>BU HAFTA KAÇ GÜN?</span></p>
    <table class="tbl week">{rows}</table>
    <p class="label"><span>ÖLÇÜMLER</span></p>
    <div class="fields">{meas}</div>
    <p class="caption">Değerleri İlerleme Tablosu'na (s. {{p:ilerleme}}) da yaz.</p>
    {q}
    """
    add(f"hafta{w}", page(inner, "plain"), toc=f"{w}. hafta değerlendirmesi")


def day30():
    D = P.DAY30
    meals = "".join(f"<tr><th>{esc(a)}</th><td>{esc(b)}</td></tr>" for a, b in D["meals"])
    inner = f"""
    <header class="day-head">
      <div class="day-num"><span>GÜN</span><strong>30</strong><em>/ 30</em></div>
      <div class="day-meta"><p>FAZ 4 · SİSTEMİ OTURT</p>{bar(30)}</div>
    </header>
    <section class="focus final">
      {label("BUGÜNÜN ODAĞI", "focus")}
      <h2>{esc(D["title"])}</h2>
      <p>{esc(D["focus"])}</p>
    </section>
    <section class="block">
      {label("BESLENME", "nutrition")}
      <p class="rule">{esc(D["nutrition"])}</p>
      <table class="meals">{meals}</table>
    </section>
    <div class="cols">
      <section class="block move">{label("HAREKET", "movement")}<p class="goal">{esc(D["movement"][0])}</p><p class="t-text">{esc(D["movement"][1])}</p></section>
      <section class="block train rest">{label("ANTRENMAN", "training")}<p class="t-text">{esc(D["training"])}</p></section>
    </div>
    <section class="task wide">{label("GÜNÜN GÖREVİ", "task")}<p>{esc(D["task"])}</p></section>
    {notes()}
    {checkin(False)}
    """
    add("gun30", page(inner, "day"), toc="30. gün: Buradan sonra ne olacak?")
    qs = "".join(f"<p class='q'>{i}. {esc(q)}</p>{lines(3)}" for i, q in enumerate(D["questions"], 1))
    add("geriye", page(f"""
    <p class="eyebrow">30. gün</p>
    <h2 class="h2">Geriye bak</h2>
    <p class="lead">Kısa cevaplar yeterli. Bu sayfa, 30 günün sana ne kattığını görmen için.</p>
    {qs}""", "plain"), toc="Geriye bak")


def continue_page():
    C = P.CONTINUE
    rules = "".join(f"<li><b>{esc(a)}</b> {esc(b)}</li>" for a, b in C["rules"])
    prog = "".join(f"<tr><th>{esc(a)}</th><td>{esc(b)}</td></tr>" for a, b in C["progression"])
    head = "".join(f"<th>{esc(c)}</th>" for c in C["template_cols"])
    body = "".join(f"<tr><th>Hafta {i}</th>{'<td></td>' * len(C['template_cols'])}</tr>" for i in range(1, 5))
    inner = f"""
    <h2 class="h2">{esc(C["title"])}</h2>
    <p class="lead">{esc(C["lead"])}</p>
    <p class="label"><span>DEVAM İÇİN 5 KURAL</span></p>
    <ol class="rules-num">{rules}</ol>
    <p class="label"><span>ANTRENMANI ADIM ADIM ZORLAŞTIR</span></p>
    <table class="tbl">{prog}</table>
    <p class="label"><span>SONRAKİ 4 HAFTA</span></p>
    <table class="tbl grid-tbl tpl"><thead><tr><th></th>{head}</tr></thead><tbody>{body}</tbody></table>
    """
    add("devam", page(inner, "plain"), toc="Sonraki 4 hafta: Devam planı")


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
    add("kapanis", page(inner, "cover closing-page", footer=False), toc="Kapanış")


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
            toc_items.append((f"Gün {first}–{last}", numbers[f"gun{first}"], None))
    toc_html = "".join(
        f'<div class="toc-row {"toc-phase" if strong else ""} {"toc-sub" if strong is None else ""}">'
        f'<span>{esc(t)}</span><i></i><b>{n}</b></div>' for t, n, strong in toc_items)

    out = []
    for p in pages:
        h = p["html"].replace("{toc}", toc_html).replace("{pageno}", str(numbers[p["key"]]))
        h = re.sub(r"\{p:(\w+)(?::(\w+))?\}",
                   lambda m: with_suffix(numbers[m.group(1)], m.group(2)) if m.group(2) else str(numbers[m.group(1)]), h)
        out.append(h)
    return "".join(out), len(pages)


def font_face():
    faces = []
    for subset, rng in [("latin", "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"),
                        ("latin-ext", "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF")]:
        with open(os.path.join(FONT_DIR, f"instrument-sans-{subset}-wght-normal.woff2"), "rb") as fh:
            data = base64.b64encode(fh.read()).decode()
        faces.append(f"@font-face{{font-family:'Instrument Sans';font-weight:400 700;font-style:normal;"
                     f"src:url(data:font/woff2;base64,{data}) format('woff2');unicode-range:{rng}}}")
    return "\n".join(faces)


if __name__ == "__main__":
    body, count = build()
    with open(os.path.join(ROOT, "style.css"), encoding="utf-8") as fh:
        css = fh.read()
    doc = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<title>LEAN MODE PRO · 30 Günlük Kilo Verme Planı</title>
<meta name="author" content="LEAN MODE PRO">
<style>{font_face()}
{css}</style></head><body>{body}</body></html>"""
    os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
    with open(os.path.join(ROOT, "dist", "ebook.html"), "w", encoding="utf-8") as fh:
        fh.write(doc)
    print(f"ebook.html written, {count} pages")

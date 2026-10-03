"""Shrinks the e-book PDF without changing how it looks or reads.

Chromium positions every glyph on its own (`10.6080475 0 Td <0033> Tj`), about 25 bytes per character.
This rewrites each text run as one TJ array with the spacing adjustments PDF readers expect
(`[<00150033>-12<0020>]`), rounds coordinates to 3 decimals (far below a pixel), packs objects into
object streams and linearizes the file ("fast web view": browsers show page 1 before the rest has arrived).

Positions are kept exact: each adjustment is computed from the glyph widths in the embedded fonts and
corrected against the running position, so rounding errors cannot add up along a line.

Usage: python3 ebook/optimize_pdf.py [in.pdf] [out.pdf]   (default: the PDF in ebook/dist, in place)
Needs pikepdf (pip install pikepdf).
"""
import os
import sys
from decimal import Decimal

import pikepdf

DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist",
                    "lean-mode-pro-30-gunluk-kilo-verme-plani.pdf")


KAPPA = 0.5522847498  # cubic approximation of a quarter circle
GAP = 40              # |TJ adjustment| (1/1000 em) above which glyphs are positioned separately, as in the original


def num(v):
    return float(v)


def dec(v, places=3):
    """Fixed-point number without exponent (PDF has no 1E+2 notation) and without trailing zeros."""
    text = f"{v:.{places}f}".rstrip("0").rstrip(".")
    return Decimal(text if text not in ("", "-", "-0") else "0")


Y_OPERANDS = {"m": (1,), "l": (1,), "c": (1, 3, 5), "re": (1,), "Tm": (5,)}
NO_REBASE = {"cm", "Do", "sh", "BI", "ID", "EI", "d0", "d1"}


def rebase(instructions, stats):
    """Chromium prints the whole book as one tall canvas: every page wraps its content in
    `q  s 0 0 s 0 f cm ... Q` with a large f and large y coordinates (e.g. 54024.12). Moving the offset
    from the cm into the coordinates gives short numbers that compress better. The drawing is unchanged."""
    out = list(instructions)
    i = 0
    while i < len(out):
        ins = out[i]
        if str(ins.operator) == "q" and i + 1 < len(out) and str(out[i + 1].operator) == "cm":
            a, b, c, d, e, f = (num(x) for x in out[i + 1].operands)
            # find the matching Q and make sure the block can be shifted safely
            depth, j, safe = 1, i + 2, True
            while j < len(out) and depth:
                op = str(out[j].operator)
                depth += op == "q"
                depth -= op == "Q"
                if depth and op in NO_REBASE:
                    safe = False
                j += 1
            if safe and b == 0 and c == 0 and d != 0 and f != 0:
                shift = f / d                               # y_user = d*y + f  ->  d*(y + shift)
                for k in range(i + 2, j - 1):
                    op = str(out[k].operator)
                    if op in Y_OPERANDS:
                        ops = list(out[k].operands)
                        for idx in Y_OPERANDS[op]:
                            ops[idx] = num(ops[idx]) + shift
                        out[k] = pikepdf.ContentStreamInstruction(ops, out[k].operator)
                out[i + 1] = pikepdf.ContentStreamInstruction(list(out[i + 1].operands[:5]) + [0], out[i + 1].operator)
                stats["rebased"] += 1
            i = j
            continue
        i += 1
    return out


def simplify_corners(instructions, stats):
    """Skia draws each rounded corner with 4 or 8 cubic pieces. Replace a run of pieces that forms one quarter
    arc between two axis-aligned edges with a single cubic, if the result stays within 1 % of the radius."""
    out, path, cur = [], [], None

    def flush_path():
        nonlocal path
        if not path:
            return
        segs = path  # list of (op, [floats])
        new = [segs[0]]
        pos = segs[0][1][-2:]
        k = 1
        while k < len(segs):
            op, vals = segs[k]
            if op != "c":
                new.append(segs[k])
                pos = vals[-2:] if vals else pos
                k += 1
                continue
            run_end = k
            while run_end < len(segs) and segs[run_end][0] == "c":
                run_end += 1
            run = segs[k:run_end]
            p0, p3 = pos, run[-1][1][4:6]
            replaced = None
            dx, dy = p3[0] - p0[0], p3[1] - p0[1]
            if len(run) in (2, 4, 8) and abs(dx) > 1e-6 and abs(dy) > 1e-6 and abs(abs(dx) - abs(dy)) < 1e-6 * max(abs(dx), 1) * 1e3:
                # incoming edge direction decides where the sharp corner is
                prev = new[-1]
                prev_pt = new[-2][1][-2:] if len(new) >= 2 else None
                horizontal_in = None
                if prev[0] == "l" and prev_pt is not None:
                    if abs(prev_pt[1] - p0[1]) < 1e-6:
                        horizontal_in = True
                    elif abs(prev_pt[0] - p0[0]) < 1e-6:
                        horizontal_in = False
                elif run_end < len(segs) and segs[run_end][0] == "l":
                    nxt = segs[run_end][1]
                    if abs(nxt[1] - p3[1]) < 1e-6:
                        horizontal_in = False          # leaves horizontally -> came in vertically
                    elif abs(nxt[0] - p3[0]) < 1e-6:
                        horizontal_in = True
                if horizontal_in is not None:
                    corner = (p3[0], p0[1]) if horizontal_in else (p0[0], p3[1])
                    c1 = (p0[0] + KAPPA * (corner[0] - p0[0]), p0[1] + KAPPA * (corner[1] - p0[1]))
                    c2 = (p3[0] + KAPPA * (corner[0] - p3[0]), p3[1] + KAPPA * (corner[1] - p3[1]))
                    mid_new = ((p0[0] + 3 * c1[0] + 3 * c2[0] + p3[0]) / 8, (p0[1] + 3 * c1[1] + 3 * c2[1] + p3[1]) / 8)
                    mid_old = run[len(run) // 2 - 1][1][4:6]
                    radius = abs(dx)
                    # all original points must stay inside the corner box (one quarter arc, no detours)
                    inside = all(min(p0[0], p3[0]) - 1e-6 <= x <= max(p0[0], p3[0]) + 1e-6 and
                                 min(p0[1], p3[1]) - 1e-6 <= y <= max(p0[1], p3[1]) + 1e-6
                                 for _, v in run for x, y in zip(v[0::2], v[1::2]))
                    err = ((mid_new[0] - mid_old[0]) ** 2 + (mid_new[1] - mid_old[1]) ** 2) ** 0.5
                    if inside and err <= 0.01 * radius:
                        replaced = ("c", [c1[0], c1[1], c2[0], c2[1], p3[0], p3[1]])
            if replaced:
                new.append(replaced)
                stats["corners"] += 1
            else:
                new.extend(run)
            pos = p3
            k = run_end
        for op, vals in new:
            out.append(pikepdf.ContentStreamInstruction(vals, pikepdf.Operator(op)))
        path = []

    for ins in instructions:
        op = str(ins.operator)
        if op == "m":
            flush_path()
            path = [("m", [num(x) for x in ins.operands])]
        elif op in ("l", "c") and path:
            path.append((op, [num(x) for x in ins.operands]))
        else:
            flush_path()
            out.append(ins)
    flush_path()
    return out


PATH_OPS = {"m", "l", "c", "v", "y", "re"}
TEXT_OPS = {"Tm", "Td", "TD", "Tf"}


def round_all(instructions):
    """Paths to 0.01 and text positions to 0.001 units (far below a pixel). Matrices (cm) stay exact:
    some icons are drawn at tiny scales where rounding would distort them."""
    out = []
    for ins in instructions:
        op = str(ins.operator)
        places = 2 if op in PATH_OPS else 3 if op in TEXT_OPS else None
        if places is None:
            out.append(ins)
            continue
        ops = [dec(float(o), places) if isinstance(o, (float, Decimal)) else o for o in ins.operands]
        out.append(pikepdf.ContentStreamInstruction(ops, ins.operator))
    return out


def nbsp_cids(font):
    """CIDs that the font's ToUnicode map turns into U+00A0 (no-break space)."""
    import re
    if "/ToUnicode" not in font:
        return set()
    cmap = font.ToUnicode.read_bytes().decode("latin-1")
    cids = set()
    for block in re.findall(r"beginbfchar(.*?)endbfchar", cmap, re.S):
        for src, dst in re.findall(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
            if dst.upper() == "00A0":
                cids.add(int(src, 16))
    for block in re.findall(r"beginbfrange(.*?)endbfrange", cmap, re.S):
        for lo, hi, dst in re.findall(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
            lo, hi, d = int(lo, 16), int(hi, 16), int(dst, 16)
            if lo <= 0xA0 - d + lo <= hi and d <= 0xA0 <= d + (hi - lo):
                cids.add(lo + 0xA0 - d)
    return cids


def cid_widths(font):
    """CID -> advance width (1/1000 text space) of a Type0/Identity-H font."""
    desc = font.DescendantFonts[0]
    default = float(desc.get("/DW", 1000))
    widths = {}
    w = list(desc.get("/W", []))
    i = 0
    while i < len(w):
        first = int(w[i])
        if isinstance(w[i + 1], pikepdf.Array):
            for j, val in enumerate(w[i + 1]):
                widths[first + j] = float(val)
            i += 2
        else:
            last, val = int(w[i + 1]), float(w[i + 2])
            for c in range(first, last + 1):
                widths[c] = val
            i += 3
    return widths, default, nbsp_cids(font)


def rounded(operand):
    return dec(float(operand), 3) if isinstance(operand, (float, Decimal)) else operand


def text_block_to_tj(block, fonts):
    """block = instructions between BT and ET. Returns the rewritten block, or None if it does not have the
    exact shape Chromium writes: Tf, Tm, Tj, then (Td x 0, Tj) pairs, one glyph per Tj."""
    ops = [str(i.operator) for i in block]
    if len(ops) < 3 or sorted(ops[:2]) != ["Tf", "Tm"] or ops[2] != "Tj":
        return None
    if any(a != "Td" or b != "Tj" for a, b in zip(ops[3::2], ops[4::2])) or len(ops) % 2 == 0:
        return None
    tf = block[ops.index("Tf")]
    tm = block[ops.index("Tm")]
    name, size = str(tf.operands[0]), float(tf.operands[1])
    if name not in fonts or size <= 0:
        return None
    widths, default, nbsp = fonts[name]
    glyphs = [bytes(block[2].operands[0])]
    offsets = [0.0]
    for td, tj in zip(block[3::2], block[4::2]):
        if float(td.operands[1]) != 0 or len(bytes(tj.operands[0])) != 2:
            return None
        offsets.append(float(td.operands[0]))
        glyphs.append(bytes(tj.operands[0]))
    if len(bytes(block[2].operands[0])) != 2:
        return None

    result = [pikepdf.ContentStreamInstruction(list(tf.operands), tf.operator),
              pikepdf.ContentStreamInstruction([rounded(o) for o in tm.operands], tm.operator)]
    parts = [glyphs[0]]

    def emit_tj():
        arr = pikepdf.Array([pikepdf.String(p) if isinstance(p, bytes) else p for p in parts])
        result.append(pikepdf.ContentStreamInstruction([arr], pikepdf.Operator("TJ")))

    target = pen = line_start = 0.0
    for prev, glyph, dx in zip(glyphs, glyphs[1:], offsets[1:]):
        target += dx                                    # Td moves the line start by dx
        pen_after = pen + widths.get(int.from_bytes(prev, "big"), default) * size / 1000
        adjust = round((pen_after - target) * 1000 / size)
        keep_apart = int.from_bytes(glyph, "big") in nbsp or int.from_bytes(prev, "big") in nbsp
        if abs(adjust) > GAP or keep_apart:
            # A visible gap (letter-spacing, word-spacing), strong kerning or a no-break space: keep it as its own
            # positioned piece like the original. Inside one TJ, Chrome's PDF viewer (PDFium) would read such gaps as spaces
            # ("G Ü N D E N") and report the no-break space as U+00A0, which breaks searching for "1. hafta".
            emit_tj()
            result.append(pikepdf.ContentStreamInstruction([dec(target - line_start, 3), 0], pikepdf.Operator("Td")))
            line_start = pen = target
            parts = [glyph]
            continue
        pen = pen_after - adjust * size / 1000          # actual position of this glyph, used for the next one
        if adjust == 0:
            parts[-1] += glyph
        else:
            parts += [adjust, glyph]
    emit_tj()
    return result


def merge_runs(instructions, fonts, stats):
    out, block, in_text = [], [], False
    for ins in instructions:
        op = str(ins.operator)
        if op == "BT":
            in_text, block = True, []
            out.append(ins)
            continue
        if op == "ET" and in_text:
            new = text_block_to_tj(block, fonts)
            if new is None:
                stats["kept"] += 1
                new = [pikepdf.ContentStreamInstruction([rounded(o) for o in i.operands], i.operator) for i in block]
            else:
                stats["merged"] += 1
            out += new
            out.append(ins)
            in_text = False
            continue
        if in_text:
            block.append(ins)
        else:
            out.append(pikepdf.ContentStreamInstruction([rounded(o) for o in ins.operands], ins.operator))
    return out


def optimize(src, dst):
    with pikepdf.open(src, allow_overwriting_input=True) as pdf:
        before = after = 0
        stats = {"merged": 0, "kept": 0, "rebased": 0, "corners": 0}
        for page in pdf.pages:
            fonts = {}
            for name, font in (page.Resources.get("/Font") or {}).items():
                if font.get("/Subtype") == "/Type0" and font.get("/Encoding") == "/Identity-H":
                    fonts[str(name)] = cid_widths(font)
            instructions = list(pikepdf.parse_content_stream(page))
            instructions = rebase(instructions, stats)
            instructions = merge_runs(instructions, fonts, stats)
            instructions = simplify_corners(instructions, stats)
            data = pikepdf.unparse_content_stream(round_all(instructions))
            before += sum(len(c.read_bytes()) for c in (
                [page.obj.Contents] if isinstance(page.obj.Contents, pikepdf.Stream) else page.obj.Contents))
            after += len(data)
            page.obj.Contents = pdf.make_stream(data)
        pdf.remove_unreferenced_resources()
        pdf.save(dst, compress_streams=True, recompress_flate=True,
                 object_stream_mode=pikepdf.ObjectStreamMode.generate, linearize=True)
    return before, after, stats


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else DIST
    dst = sys.argv[2] if len(sys.argv) > 2 else src
    size_in = os.path.getsize(src)
    before, after, stats = optimize(src, dst)
    print(f"text runs merged {stats['merged']}, left as they were {stats['kept']}; page blocks rebased "
          f"{stats['rebased']}; corners simplified {stats['corners']}; content streams {before // 1024} KB -> {after // 1024} KB (uncompressed); "
          f"file {size_in // 1024} KB -> {os.path.getsize(dst) // 1024} KB")

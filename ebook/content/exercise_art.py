"""Own illustrations for the exercise guide: a simple side-view figure (start and end position) per exercise,
drawn as inline SVG in the brand colors. No photos, no third-party image rights.

A pose is given by a few points (neck, hip, hands, ankles); elbows and knees are placed with two-bone IK, so the
limb lengths always stay the same. Near-side limbs are dark green, far-side limbs light green.
"""
import math

W, H, FLOOR = 300, 120, 108
INK, FAR, PROP, PROP2, LINE, ARROW = "#1D5A48", "#9CC3B2", "#F6D776", "#C9CFCC", "#E3E2DB", "#E3A21A"
TORSO, THIGH, SHIN, UARM, FARM, FOOT, HEAD_R = 31, 25, 24, 18, 17, 8, 8.5


def _ik(a, b, l1, l2, bend):
    """Middle joint between a and b for segment lengths l1, l2; bend = +1 / -1 picks the side."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    d = max(1e-6, min(math.hypot(dx, dy), l1 + l2 - 1e-6))
    x = (l1 * l1 - l2 * l2 + d * d) / (2 * d)
    h = math.sqrt(max(0.0, l1 * l1 - x * x))
    ux, uy = dx / d, dy / d
    return (a[0] + ux * x - bend * uy * h, a[1] + uy * x + bend * ux * h)


def _reach(a, b, length):
    """Point on the way from a towards b at the given distance (b itself if it is closer)."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    d = math.hypot(dx, dy)
    return b if d <= length else (a[0] + dx / d * length, a[1] + dy / d * length)


def _line(p, q, color, width):
    return (f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{color}" '
            f'stroke-width="{width}" stroke-linecap="round"/>')


def figure(neck, hip, hands, ankles, knee_bend=(1, 1), elbow_bend=(-1, -1), feet=(0, 0), head=None):
    """hands/ankles/knee_bend/elbow_bend/feet: (near, far). feet = foot direction in degrees (0 = forward/right).
    head: direction of the head from the neck in degrees (default: in line with the torso)."""
    if head is None:
        head = math.degrees(math.atan2(neck[1] - hip[1], neck[0] - hip[0]))
    hc = (neck[0] + math.cos(math.radians(head)) * (HEAD_R + 3.5), neck[1] + math.sin(math.radians(head)) * (HEAD_R + 3.5))
    parts = {}
    for side, k in (("near", 0), ("far", 1)):
        ankle = _reach(hip, ankles[k], THIGH + SHIN - 0.05)
        knee = _ik(hip, ankle, THIGH, SHIN, knee_bend[k])
        toe = (ankle[0] + math.cos(math.radians(feet[k])) * FOOT, ankle[1] + math.sin(math.radians(feet[k])) * FOOT)
        hand = _reach(neck, hands[k], UARM + FARM - 0.05)
        elbow = _ik(neck, hand, UARM, FARM, elbow_bend[k])
        color = INK if side == "near" else FAR
        parts[side] = (_line(hip, knee, color, 10) + _line(knee, ankle, color, 9) + _line(ankle, toe, color, 7),
                       _line(neck, elbow, color, 8.5) + _line(elbow, hand, color, 8))
    return (parts["far"][0] + parts["far"][1] + _line(hip, neck, INK, 15) + parts["near"][0] + parts["near"][1]
            + f'<circle cx="{hc[0]:.1f}" cy="{hc[1]:.1f}" r="{HEAD_R}" fill="{INK}"/>')


def arrow(x, y=60):
    return (f'<path d="M{x - 10},{y} h18 m-7,-7 l7,7 l-7,7" fill="none" stroke="{ARROW}" stroke-width="4" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def floor(x1=8, x2=W - 8):
    return _line((x1, FLOOR + 4), (x2, FLOOR + 4), LINE, 3)


def svg(body, label, top=0):
    """top: crop the empty space above floor exercises."""
    return (f'<svg class="ex-art" viewBox="0 {top} {W} {H - top}" role="img" aria-label="{label}" '
            f'xmlns="http://www.w3.org/2000/svg">{body}</svg>')


F = FLOOR  # ankles stand on the floor line


STAND = dict(neck=(0, F - THIGH - SHIN - TORSO + 0.1), hip=(0, F - THIGH - SHIN + 0.1), hands=((3, 63), (5, 63)),
             ankles=((0, F), (2, F)), knee_bend=(-1, -1), elbow_bend=(1, 1))


def standing(x):
    """Upright start position at x."""
    move = lambda p: (p[0] + x, p[1])
    pose = dict(STAND)
    for k in ("neck", "hip"):
        pose[k] = move(pose[k])
    pose["hands"] = tuple(move(h) for h in pose["hands"])
    pose["ankles"] = tuple(move(a) for a in pose["ankles"])
    return figure(**pose)


def clock(x, y=58):
    return (f'<circle cx="{x}" cy="{y}" r="20" fill="none" stroke="{PROP2}" stroke-width="4"/>'
            f'<path d="M{x},{y - 12} v12 l8,6" fill="none" stroke="{ARROW}" stroke-width="4" stroke-linecap="round" '
            f'stroke-linejoin="round"/>')


def squat():
    down = figure(neck=(220, 50), hip=(194, 76), hands=((254, 52), (256, 54)), ankles=((214, F), (218, F)),
                  knee_bend=(-1, -1), elbow_bend=(1, 1), head=-58)
    return svg(floor() + standing(72) + arrow(140) + down, "Squat: start standing, then push the hips back and down")


def lunge():
    down = figure(neck=(210, 46), hip=(210, 77), hands=((213, 81), (211, 81)), ankles=((234, F), (180, F - 6)),
                  knee_bend=(-1, -1), elbow_bend=(1, 1), feet=(0, 55))
    return svg(floor() + standing(70) + arrow(138) + down, "Reverse lunge: step back and lower the back knee")


def push_up():
    top = figure(neck=(104, 73.5), hip=(75, 84.4), hands=((106, F), (110, F)), ankles=((29, 102), (33, 102)),
                 feet=(80, 80), head=-15)
    low = figure(neck=(266, 92), hip=(237, 97), hands=((270, F), (274, F)), ankles=((189, 103), (193, 103)),
                 elbow_bend=(1, 1), feet=(80, 80), head=-6)
    return svg(floor() + top + arrow(148, 80) + low, "Push-up: lower the chest with the body in a straight line", top=52)


def row():
    def pack(x, y):
        return f'<rect x="{x - 10}" y="{y}" width="20" height="24" rx="6" fill="{PROP}"/>'
    start = figure(neck=(82, 44), hip=(56, 64), hands=((84, 80), (86, 80)), ankles=((62, F), (66, F)),
                   knee_bend=(-1, -1), elbow_bend=(1, 1), head=-35)
    end = figure(neck=(232, 44), hip=(206, 64), hands=((222, 64), (224, 64)), ankles=((212, F), (216, F)),
                 knee_bend=(-1, -1), elbow_bend=(-1, -1), head=-35)
    return svg(floor() + pack(85, 78) + start + arrow(146) + pack(224, 62) + end,
               "Row: lean forward with a flat back and pull the backpack to the belly")


def glute_bridge():
    down = figure(neck=(30, F - 6), hip=(66, F - 6), hands=((62, F), (64, F)), ankles=((104, F), (108, F)),
                  knee_bend=(-1, -1), elbow_bend=(-1, -1), head=180, feet=(10, 10))
    up = figure(neck=(178, F - 6), hip=(214, 78), hands=((212, F), (214, F)), ankles=((254, F), (258, F)),
                knee_bend=(-1, -1), elbow_bend=(-1, -1), head=180, feet=(10, 10))
    return svg(floor() + down + arrow(144, 82) + up, "Glute bridge: lift the hips until knees, hips and shoulders line up",
               top=58)


def plank():
    body = figure(neck=(196, 86), hip=(165.6, 91.8), hands=((213, 104), (217, 104)), ankles=((117.4, 101), (121, 101)),
                  elbow_bend=(1, 1), feet=(80, 80), head=-8)
    return svg(floor() + clock(64, 84) + body, "Plank: forearms on the floor, body straight from head to heels; hold",
               top=58)


def dead_bug():
    start = figure(neck=(28, F - 6), hip=(62, F - 6), hands=((28, 66), (32, 66)), ankles=((86, 77), (90, 77)),
                   knee_bend=(-1, -1), elbow_bend=(1, 1), head=180, feet=(0, 0))
    move = figure(neck=(180, F - 6), hip=(214, F - 6), hands=((146, 94), (180, 66)), ankles=((238, 77), (262, 95)),
                  knee_bend=(-1, -1), elbow_bend=(1, 1), head=180, feet=(0, 10))
    return svg(floor() + start + arrow(130, 84) + move,
               "Dead bug: on your back, arms up and knees bent; extend the opposite arm and leg", top=54)


def wall_sit():
    wall = f'<rect x="58" y="8" width="14" height="{F - 4}" rx="3" fill="{LINE}"/>'
    body = figure(neck=(80, 53), hip=(80, 84), hands=((102, 80), (104, 80)), ankles=((105, F), (109, F)),
                  knee_bend=(-1, -1), elbow_bend=(1, 1), head=-90)
    return svg(floor(8, 200) + wall + body + clock(176), "Wall sit: back against the wall, knees at about 90 degrees; hold")


ART = {"Squat": squat, "Reverse lunge": lunge, "Push-up": push_up, "Row": row, "Glute bridge": glute_bridge,
       "Plank": plank, "Dead bug": dead_bug, "Wall sit": wall_sit}


def art(name):
    fn = ART.get(name)
    return fn() if fn else ""


if __name__ == "__main__":
    cards = "".join(f'<div style="border:1px solid #ddd;border-radius:10px;padding:10px;background:#fff">'
                    f'<b>{n}</b>{fn()}</div>' for n, fn in ART.items())
    print(f'<!doctype html><meta charset="utf-8"><body style="margin:0;background:#f6f5f1;font:14px sans-serif">'
          f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:12px;width:760px">{cards}</div>')

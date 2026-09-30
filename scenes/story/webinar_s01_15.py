"""The fifteen scenes of the webinar «IA: ¿el fin del piloto eterno? Agentes que escalan» (Amaris, 2026-10), harvested
from its deck (v2) (examples/webinar-piloto-eterno/) and drawn in the world «Luz de operación» (worlds/luz.py, the lx_* kit):
the scenes of the webinar-panel type. Names w01…w15 (w00_luz is the world's placeholder); generic aliases in ext.py:
luz-hero, luz-agenda, luz-question, luz-divider, luz-loop, luz-figures, luz-bridge, luz-ladder, luz-console, luz-wave,
luz-escala, luz-panel, panel-questions, reflections-live, luz-end. Private helpers are _wNN_*.
Slides 13 and 14 are tapped live (module/deck.js): [data-pick][data-dim] and [data-reveal], as references/scenes.md says.
"""


# ================================================================ harvested from s01_03.py (v2)
"""Group A: slides 1-3 of the webinar «IA: ¿el fin del piloto eterno?», drawn in the world «Luz de operación»
(worlds/luz.py: every object comes from its lx_* helpers and LX_* colors). v2: a far layer of depth (lx_depth) under each
scene, a gentle camera (lx_drift) on the art, labels painted last.
w01_portada  - the spark «IA» and the magenta trail spiralling round it in three laps, each tighter, until it closes on
               itself: a loop with no exit, under a tilted far orbit plane (the cover's question; slide 15 answers it).
w02_agenda   - the 55 minutes as four glass cards sized by duration (5 · 10 · 30 · 10) over a timeline of light: the
               trail runs 00:00 → 55:00 and lights each card in turn; the panel keeps its spotlights breathing.
w03_apertura - a funnel of light: sparks pass «La IA» freely and gather, curious, over the three people of the neck
               «Nosotros»; one goes through to the chat bubble, which lights.
No Amaris mark here: the engine's lockup and footer are the slides' only mark."""


def _w01_rider(d, stops, show=None, s=.7, hover=None):
    """A spark riding path d on the scene clock: stops = [(fraction of the 12 s loop, fraction of the path)].
    show: [(t, opacity)] pairs for when it is visible, or None. hover: (dy, period, phase) for a small float at rest."""
    vis_ = beat("opacity", show) if show else ""
    body = lx_spark(0, 0, s)
    if hover:
        body = f'<g>{bob(0, hover[0], hover[1], hover[2])}{body}</g>'
    return f'<g>{vis_}<g>{move(d, list(stops), D)}{body}</g></g>'


def _w01_poly(pts):
    """An open polyline path through pts, and its length in px."""
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    return d, sum(math.dist(a, b) for a, b in zip(pts, pts[1:]))


def _w01_charge(d, pairs, show, width=3):
    """The trail charging behind its rider: path d (pathLength 1) revealed as the rider goes, with a soft halo.
    pairs: [(t, fraction of the path reached)] on the 12 s loop; show: [(t, opacity)]."""
    off = beat("stroke-dashoffset", [(t, round(1 - f, 4)) for t, f in pairs])
    return (f'<g>{beat("opacity", show)}'
            f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{LX_MAGENTA}" stroke-width="{width * 4}" '
            f'stroke-linecap="round" opacity=".18">{off}</path>'
            f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{LX_MAGENTA}" stroke-width="{width}" '
            f'stroke-linecap="round">{off}</path></g>')


# ---------------------------------------------------------------- slide 1: the loop with no exit
@register("scene", "w01_portada")
def sc_w01_portada(sl, ctx):
    """The spark «IA» at the center; around it the magenta trail spirals in three laps, each tighter than the last, and
    ends on a closed ring; two dashed orbits turn and a far orbit plane, tilted, carries a small node behind and in front
    of the spiral. Loop: the rider spark spirals inwards lap after lap (2-8 s) and the trail charges behind it; the ring
    closes (7.9 s): it lights, a ripple leaves it, the spark flares and the outer laps dim; the rider keeps circling the
    closed ring; the spark «IA» pulses every 3 s. Frozen frame (10.8 s): the ring closed and lit round the spark, the
    rider on it, no way out."""
    if ORIENT() == "portrait":
        return _wq01_portada(sl, ctx)
    cx, cy, r0, r1, laps, a0 = 1190, 438, 300, 132, 3, -150
    pt = lambda r, ang: (cx + r * math.cos(math.radians(ang)), cy + r * math.sin(math.radians(ang)))
    n = 72 * laps
    spiral = [pt(r0 + (r1 - r0) * k / n, a0 + 360 * laps * k / n) for k in range(n + 1)]
    ring = [pt(r1, a0 + 5 * k) for k in range(1, 145)]
    d, total = _w01_poly(spiral + ring)              # the spiral, then two laps of the closed ring
    a = _w01_poly(spiral)[1] / total
    close = .66
    run = [(0, 0), (.16, 0), (close, a), (.97, 1), (1, 1)]
    show = [(0, 0), (.155, 0), (.165, 1), (.97, 1), (.99, 0), (1, 0)]
    # the far plane: a tilted orbit, its back half under the spiral and its front half over it, with a node riding it
    ex, ey, tilt = 366, 150, -16
    half = lambda x_from, x_to: f"M{x_from} {cy} A{ex} {ey} 0 0 1 {x_to} {cy}"
    rot = lambda inner: f'<g transform="rotate({tilt} {cx} {cy})">{inner}</g>'
    plane = lambda d_, op: f'<path d="{d_}" fill="none" stroke="{LX_LILAC}" stroke-width="1.4" stroke-dasharray="2 7" opacity="{op}"/>'
    rider_plane = (f'<g>{beat("opacity", [(0, .3), (.45, .3), (.55, .9), (.95, .9), (1, .3)])}'
                   f'<g>{move(half(cx - ex, cx + ex) + f" A{ex} {ey} 0 0 1 {cx - ex} {cy}", [(0, 0), (1, 1)], D)}'
                   f'{glow(0, 0, 12, LX_LILAC, .7)}<circle r="3" fill="var(--white)"/></g></g>')
    back = land(rot(plane(half(cx - ex, cx + ex), .3)), .1, .6, 0)
    front = land(rot(plane(half(cx + ex, cx - ex), .7) + rider_plane), .1, .6, 0)
    orbits = land(lx_orbit(cx, cy, 326, color=LX_LILAC, dash="2 12", period=60, op=.5)
                  + lx_orbit(cx, cy, 348, color=LX_LILAC, dash="1 10", period=90, rev=True, op=.3), .1, .5, 0)
    # the trail: drawn once, charged behind the rider, and its outer laps dim when the ring closes
    dim = beat("opacity", [(0, 1), (close, 1), (close + .04, .42), (.97, .42), (.99, 1), (1, 1)])
    trail = (f'<g>{dim}{lx_trail(d, begin=.25, dur=1.55, spark=False)}'
             + _w01_charge(d, [(0, 0), (.16, 0), (close, a), (.97, 1), (.99, 1), (1, 0)], show) + '</g>')
    lit_ring = (f'<g>{lx_lit(close)}<circle cx="{cx}" cy="{cy}" r="{r1}" fill="none" stroke="{LX_MAGENTA}" stroke-width="14" opacity=".18"/>'
                f'<circle cx="{cx}" cy="{cy}" r="{r1}" fill="none" stroke="{LX_MAGENTA}" stroke-width="2.4"/></g>')
    ripple = (f'<circle cx="{cx}" cy="{cy}" r="{r1}" fill="none" stroke="{LX_MAGENTA}" stroke-width="2" opacity="0">'
              + beat("r", [(0, r1), (close, r1), (close + .1, r1 + 90), (1, r1 + 90)])
              + beat("opacity", [(0, 0), (close - .002, 0), (close, .9), (close + .1, 0), (1, 0)]) + '</circle>')
    flare = f'<g opacity="0">{beat("opacity", [(0, 0), (close, 0), (close + .02, .8), (close + .14, 0), (1, 0)])}{glow(cx, cy, 120, LX_GOLD, .7)}</g>'
    # the spark «IA»: it pulses (a soft glow and a ripple every 3 s)
    heart = pop(f'<g>{loop("opacity", ".35;.9;.35", 3)}{glow(0, 0, 64, LX_GOLD, .6)}</g>'
                f'<circle r="30" fill="none" stroke="{LX_GOLD}" stroke-width="1.4">{loop("r", "30;96", 3)}'
                f'{loop("stroke-opacity", ".6;0", 3)}</circle>' + lx_spark(0, 0, 2.2), cx, cy, .2, .45)
    rider = _w01_rider(d, run, show, .8)
    ia = land(lx_label(cx, cy + 100, sl["spark"], 36, 200, "portada spark", "var(--white)", "middle"), .45, .5, 10)
    fmt = land(f'<path d="M{cx - 222} 812 h40 M{cx + 182} 812 h40" stroke="{LX_EDGE}" stroke-width="1.2"/>'
               + lx_label(cx, 818, sl["format"], 20, 340, "portada format", LX_LILAC, "middle"), .6, .5, 10)
    art = back + orbits + trail + lit_ring + ripple + front + flare + heart + rider
    g = [glow(cx, cy, 420, "var(--brand)", .6),
         lx_depth(LX_ZONE["left"], n=40, seed="portada", labels=ia + fmt),
         lx_drift(art + ia, cx, cy), fmt]
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- slide 2: the 55 minutes
def _w02_min(s):
    """«MM:SS» → minutes."""
    m, sec = str(s).split(":")
    return int(m) + int(sec) / 60


def _w02_chat_glyph(x, y, color=LX_LILAC, s=1.0):
    """A chat bubble centered at (x, y), scaled by s."""
    return (f'<path transform="translate({x:.1f} {y:.1f}) scale({s})" d="M-13 -9 h26 a4 4 0 0 1 4 4 v10 a4 4 0 0 1 -4 4 h-16 '
            f'l-7 6 v-6 h-3 a4 4 0 0 1 -4 -4 v-10 a4 4 0 0 1 4 -4 Z" fill="none" stroke="{color}" stroke-width="{1.6 / s:.2f}" '
            f'stroke-linejoin="round"/>')


def _w02_mini_loop(x, y, r=24, lit=False):
    """The pilot's loop in miniature at (x, y): a ring with three stops, dim; lit: lilac, with a spark lapping it."""
    c, rr = (LX_LILAC, 3.4) if lit else (LX_DIM, 3)
    g = (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="none" stroke="{c}" stroke-width="1.6"/>'
         + "".join(f'<circle cx="{x + r * math.cos(math.radians(a)):.1f}" cy="{y + r * math.sin(math.radians(a)):.1f}" '
                   f'r="{rr}" fill="{c}"/>' for a in (-90, 30, 150)))
    return g + (f'<g>{move(ring_path(x, y, r), [(0, 0), (1, 1)], 4)}{lx_spark(0, 0, .45)}</g>' if lit else "")


@register("scene", "w02_agenda")
def sc_w02_agenda(sl, ctx):
    """The hour as four cards of dark glass across the band, each as wide as its share of the 55 minutes: chat
    («Pregunta al chat»), contexto («El piloto eterno», «No todo es un agente»), the panel (the widest: «Cinco preguntas»,
    five question marks to light and three faceless seats under spotlights) and the cierre («Preguntas del público»,
    «Reflexiones y encuesta»); each with its big duration and its name. Under them, the timeline of light with its marks
    00:00 · 05:00 · 15:00 · 45:00 · 55:00. Loop: a spark runs the timeline, the trail charging behind it, and lights each
    card as it reaches its mark (chat 2 s, contexto 2.8 s, panel 4 s, cierre 8.2 s); in the panel's half minute it lights
    the five questions one by one; the cards stay lit, the panel's spotlights keep breathing; the spark rests on 55:00,
    which lights (9.5 s). Frozen frame: the four cards lit with their durations, the panel breathing, the spark at 55:00."""
    if ORIENT() == "portrait":
        return _wq02_agenda(sl, ctx)
    x0, x1, top, ch, ay, gap, pad = 104, 1496, 398, 312, 760, 10, 16
    blocks, steps = sl["blocks"], sl["steps"]
    marks = [_w02_min(t) for _n, t in blocks] + [_w02_min(sl["end"])]
    times = [t for _n, t in blocks] + [sl["end"]]
    span = marks[-1] - marks[0]
    X = lambda m: x0 + (x1 - x0) * (m - marks[0]) / span
    p = lambda m: (m - marks[0]) / span                      # fraction of the timeline
    lit, end_t = [.17, .23, .33, .68], .79                   # the spark reaches each card's mark, then 55:00
    talks = [steps[0:1], steps[1:3], steps[3:4], steps[4:6]]
    axis = f"M{x0} {ay} H{x1}"
    arts, labels, overs, over_t = [], [], [], []
    for k, ((block, _t), a) in enumerate(zip(blocks, lit)):
        name, _s, dur = str(block).partition(" · ")
        bx, bw = X(marks[k]) + gap / 2, X(marks[k + 1]) - X(marks[k]) - gap
        room = bw - 2 * pad
        colw = min(room, 300)                                # the panel's text column; the others use the whole card
        base = [lx_card(bx, top, bw, ch, 16),
                f'<path d="M{bx + pad:.1f} {top + 114} H{bx + pad + colw:.1f}" stroke="{LX_EDGE}" stroke-width="1.2"/>']
        on = [lx_card(bx, top, bw, ch, 16, LX_LILAC, 1.8, LX_GLASS_LIT),
              f'<path d="M{bx + 18:.1f} {top} H{bx + bw - 18:.1f}" stroke="{LX_MAGENTA}" stroke-width="2.6" stroke-linecap="round"/>',
              f'<path d="M{bx + pad:.1f} {top + 114} H{bx + pad + colw:.1f}" stroke="{LX_LILAC}" stroke-width="1.2" opacity=".6"/>']
        lab = lambda col, dcol: [lx_label(bx + pad, top + 60, dur, 32, colw, "agenda duration", dcol),
                                 lx_label(bx + pad, top + 94, name, 20, colw, "agenda name", col)]
        bt, ot = lab("var(--muted)", "var(--muted)"), lab(LX_LILAC, "var(--white)")
        bullet = len(talks[k]) > 1
        yy = top + 150
        for s in talks[k]:
            tx = bx + pad + (16 if bullet else 0)
            ln, h_ = lx_lines(tx, yy, s, colw - (16 if bullet else 0), 18 if k == 2 else 17, "agenda talk", "var(--muted)")
            lt, _h = lx_lines(tx, yy, s, colw - (16 if bullet else 0), 18 if k == 2 else 17, "agenda talk", "var(--white)")
            bt.append(ln)
            ot.append(lt)
            if bullet:
                base.append(f'<circle cx="{bx + pad + 4:.1f}" cy="{yy - 6}" r="3.5" fill="{LX_DIM}"/>')
                on.append(f'<circle cx="{bx + pad + 4:.1f}" cy="{yy - 6}" r="3.5" fill="{LX_GOLD}"/>')
            yy += h_ + 10
        mid = bx + bw / 2
        if k == 0:                                           # chat: the bubble, typing once lit
            base.append(_w02_chat_glyph(mid, top + ch - 60, LX_DIM, 1.7))
            on.append(_w02_chat_glyph(mid, top + ch - 60, LX_LILAC, 1.7)
                      + "".join(f'<circle cx="{mid - 10 + 10 * j:.1f}" cy="{top + ch - 60}" r="2.4" fill="{LX_GOLD}">'
                                f'{loop("opacity", ".2;1;.2", 1.2, j * .3)}</circle>' for j in range(3)))
        elif k == 1:                                         # contexto: the pilot's loop, in miniature
            base.append(_w02_mini_loop(bx + pad + 30, top + ch - 58, 24))
            on.append(_w02_mini_loop(bx + pad + 30, top + ch - 58, 24, True))
        elif k == 2:                                         # panel: five questions, three seats under spotlights
            qs = [a + .035 + j * .07 for j in range(5)]
            for j, q in enumerate(qs):
                qx, qy = bx + pad + 11 + j * 36, yy + 14
                ring_q = f'<circle cx="{qx:.1f}" cy="{qy:.1f}" r="11" fill="none" stroke="{{}}" stroke-width="1.4"/>'
                base.append(ring_q.format(LX_EDGE))
                on.append(ring_q.format(LX_EDGE) + f'<g>{lx_lit(q)}{glow(f"{qx:.1f}", f"{qy:.1f}", 22, LX_GOLD, .6)}'
                          f'<circle cx="{qx:.1f}" cy="{qy:.1f}" r="7" fill="{LX_GOLD}"/></g>')
            t0, t1, ty = bx + pad + colw + 40, bx + bw - 40, top + ch - 50
            seats = [t0 + (t1 - t0) * f for f in (1 / 6, 1 / 2, 5 / 6)]
            cones = "".join(f'<path d="M{x - 7:.1f} {top + 8} L{x + 7:.1f} {top + 8} L{x + 70:.1f} {ty} L{x - 70:.1f} {ty} Z" '
                            f'fill="color-mix(in srgb, var(--c2) 12%, transparent)"/>' for x in seats)
            on.insert(1, f'<g>{loop("opacity", ".45;1;.45", 3)}{cones}'
                         f'{glow(f"{(t0 + t1) / 2:.1f}", ty - 60, 190, "var(--brand)", .5)}</g>'
                         f'<rect x="{bx - 5:.1f}" y="{top - 5}" width="{bw + 10:.1f}" height="{ch + 10}" rx="20" fill="none" '
                         f'stroke="{LX_LILAC}" stroke-width="1.4">{loop("stroke-opacity", ".1;.7;.1", 3)}</rect>')
            front = lx_table(t0, t1, ty, 14) + "".join(lx_seat(x, ty, 1.0, LX_LILAC, a + .015 * (j + 1)) for j, x in enumerate(seats))
            overs.append(f'<g>{lx_lit(a)}{"".join(on)}</g>' + land(front, .66, .5, 10))
            on = None
        else:                                                # cierre: the spark of the ending
            base.append(lx_spark(bx + bw - 44, top + ch - 50, .7, LX_DIM))
            on.append(lx_spark(bx + bw - 44, top + ch - 50, .7))
        arts.append("".join(base))
        if on is not None:
            overs.append(f'<g>{lx_lit(a)}{"".join(on)}</g>')
        labels.append("".join(bt))
        over_t.append(f'<g>{lx_lit(a)}{"".join(ot)}</g>')
    # the timeline: ticks from each card's edge down to the axis, the trail, and the time marks under it
    ticks, ticks_on, times_b, times_on = [], [], [], []
    for k, (m, t) in enumerate(zip(marks, times)):
        x, at = X(m), (lit + [end_t])[k]
        anchor = "start" if k == 0 else "end" if k == len(marks) - 1 else "middle"
        ticks.append(f'<path d="M{x:.1f} {top + ch + 8} V{ay + 8}" stroke="{LX_EDGE}" stroke-width="1.2"/>')
        col = LX_GOLD if k == len(marks) - 1 else LX_MAGENTA
        ticks_on.append(f'<g>{lx_lit(at)}<path d="M{x:.1f} {top + ch + 8} V{ay + 8}" stroke="{col}" stroke-width="2"/>'
                        f'<circle cx="{x:.1f}" cy="{ay}" r="4" fill="{col}"/></g>')
        times_b.append(lx_label(x, ay + 38, t, 16, 90, "agenda time", "var(--muted)", anchor))
        times_on.append(f'<g>{lx_lit(at)}' + lx_label(x, ay + 38, t, 16, 90, "agenda time", "var(--white)", anchor) + '</g>')
    stops = [(0, 0), (lit[0], 0), (lit[1] - .005, p(marks[1])), (lit[1] + .02, p(marks[1])), (lit[2] - .005, p(marks[2])),
             (lit[2] + .02, p(marks[2])), (lit[3] - .005, p(marks[3])), (lit[3] + .02, p(marks[3])), (end_t, 1), (1, 1)]
    show = [(0, 0), (.155, 0), (.165, 1), (.97, 1), (.99, 0), (1, 0)]
    charge = _w01_charge(axis, [(t, f) for t, f in stops[:-1]] + [(.99, 1), (1, 0)], show, 2.6)
    end = f'<g>{lx_lit(end_t)}{glow(x1, ay, 24, LX_GOLD, .8)}</g>'
    art = (seq(arts, .3, .5, 14) + land("".join(ticks), .3, .5, 8) + lx_trail(axis, begin=.1, dur=1.2, spark=False)
           + charge + "".join(overs) + "".join(ticks_on) + end + _w01_rider(axis, stops, show, .8))
    text = seq(labels, .3, .5, 14) + land("".join(times_b), .3, .5, 8) + "".join(over_t) + "".join(times_on)
    g = [f'<g transform="translate(800 560) scale(3.2 1.1)">{glow(0, 0, 220, "var(--brand)", .5)}</g>',
         lx_depth((80, 262, 1440, 560), n=34, seed="agenda", labels=text),
         lx_drift(art + text, 800, 580, 1.008, 0, -4)]
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- slide 3: the neck of the bottle
def _w03_q(p0, c, p1, n=24):
    """Points of the quadratic Bézier p0 → p1 with control c."""
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * c[0] + t * t * p1[0],
             (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * c[1] + t * t * p1[1]) for t in (k / n for k in range(n + 1))]


def _w03_chip(x, y, s=40, color=LX_LILAC, sw=1.6):
    """An open chip centered at (x, y): a frame with four pins per side and an empty middle (a clear way through)."""
    pins = "".join(f'M{x - s + 12 + k * (2 * s - 24) / 3:.1f} {y - s} v-10 M{x - s + 12 + k * (2 * s - 24) / 3:.1f} {y + s} v10 '
                   f'M{x - s} {y - s + 12 + k * (2 * s - 24) / 3:.1f} h-10 M{x + s} {y - s + 12 + k * (2 * s - 24) / 3:.1f} h10 '
                   for k in range(4))
    return (f'<path d="{pins}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>'
            f'<rect x="{x - s}" y="{y - s}" width="{2 * s}" height="{2 * s}" rx="10" fill="none" stroke="{color}" stroke-width="{sw}"/>'
            f'<rect x="{x - s + 12}" y="{y - s + 12}" width="{2 * s - 24}" height="{2 * s - 24}" rx="5" fill="none" '
            f'stroke="{color}" stroke-width="1.2" stroke-dasharray="4 5" opacity=".6"/>')


@register("scene", "w03_apertura")
def sc_w03_apertura(sl, ctx):
    """A funnel of light, drawn in depth (its mouth, two cross-sections, a wall that narrows): the chip «La IA», open on
    the magenta trail with a clear way through, and a neck «Nosotros» around three faceless people; under it, the chat
    bubble. Loop: five sparks drop into the mouth one after another (2-6.7 s), cross the chip without slowing (it flashes
    at each pass) and gather over the people, curious, who light up as the light reaches them; the neck breathes and one
    more spark goes straight through, behind the middle person, down into the chat bubble, which lights (8.6 s) and
    starts typing. Frozen frame: the chip clear, five sparks floating over the people, all lit, the bubble lit."""
    if ORIENT() == "portrait":
        return _wq03_apertura(sl, ctx)
    cx, top, wm, ny0, wn, ny1, chip_y, base_y = 1190, 138, 300, 470, 130, 630, 300, 626
    w = lambda y: wn + (wm - wn) * max(0., min(1., (ny0 - y) / (ny0 - top))) ** 1.8
    ys = list(range(top, ny0 + 1, 6))
    wall = lambda sg: ("M" + " L".join(f"{cx + sg * w(y):.1f} {y}" for y in ys)
                       + f" V{ny1} Q{cx + sg * wn} {ny1 + 36} {cx + sg * 46} {ny1 + 40}")
    walls = lambda d_: (f'<path d="{d_}" fill="none" stroke="{LX_LILAC}" stroke-width="10" opacity=".08"/>'
                        f'<path d="{d_}" fill="none" stroke="{LX_LILAC}" stroke-width="1.8" stroke-linejoin="round"/>')
    mouth = (f'<ellipse cx="{cx}" cy="{top}" rx="{wm}" ry="34" fill="none" stroke="{LX_LILAC}" stroke-width="1.8"/>'
             + lx_orbit(cx, top, wm + 22, 46, LX_LILAC, dash="2 10", op=.4))
    sections = "".join(lx_orbit(cx, y, w(y), w(y) * .12, LX_LILAC, dash="2 8", op=.32) for y in (222, 380))
    arts, labels = [glow(cx, 420, 420, "var(--brand)", .55), land(mouth, .1, .5, 0),
                    land(f'<g>{bob(-3, 0, 3)}{walls(wall(-1))}</g><g>{bob(3, 0, 3)}{walls(wall(1))}</g>', .15, .55, 0),
                    land(sections, .2, .5, 0),
                    f'<g>{loop("opacity", ".25;.7;.25", 3)}{glow(cx, 560, 160, LX_LILAC, .35)}</g>',   # the neck breathes
                    lx_trail(f"M{cx} {top + 10} V{ny0 + 14}", begin=.3, dur=1.1, spark=False)], []
    # five sparks: each drops into the mouth, crosses the chip and floats over the people; a sixth goes through
    rests = [(1112, 504), (1268, 504), (1190, 498), (1150, 482), (1230, 482)]
    starts = [cx - 150, cx + 160, cx - 60, cx + 90, cx - 110]
    flashes, riders = [], []
    for k, ((rx, ry), sx) in enumerate(zip(rests, starts)):
        head = _w03_q((sx, top), (cx, top + 80), (cx, chip_y))
        tail = _w03_q((cx, chip_y), (cx, 430), (rx, ry))
        d, total = _w01_poly(head + tail[1:])
        at = _w01_poly(head)[1] / total
        a = .17 + k * .065
        flashes.append(a + .045)
        riders.append(_w01_rider(d, [(0, 0), (a, 0), (a + .045, at), (a + .13, 1), (1, 1)],
                                 [(0, 0), (a, 0), (a + .01, 1), (.97, 1), (.99, 0), (1, 0)], .62, (-5, 2.4 + k * .3, k * .5)))
    a1 = .58
    head = _w03_q((cx + 40, top), (cx, top + 80), (cx, chip_y))
    d, total = _w01_poly(head + [(cx, 714)])
    at = _w01_poly(head)[1] / total
    flashes.append(a1 + .04)
    riders.append(_w01_rider(d, [(0, 0), (a1, 0), (a1 + .04, at), (a1 + .14, 1), (1, 1)],
                             [(0, 0), (a1, 0), (a1 + .01, 1), (a1 + .135, 1), (a1 + .145, 0), (1, 0)], .62))
    # the chip: open, lit once the first spark crosses it, a flash at every pass
    fl = sorted(flashes)
    pairs = [(0, 0)] + [pt for t in fl for pt in ((t - .012, 0), (t, 1), (t + .03, 0))] + [(1, 0)]
    arts += [land(_w03_chip(cx, chip_y, 40, LX_DIM), .35, .5, -12),
             f'<g>{lx_lit(fl[0])}{_w03_chip(cx, chip_y, 40, LX_LILAC, 2)}</g>',
             f'<g opacity="0">{beat("opacity", pairs)}{glow(cx, chip_y, 76, LX_GOLD, .6)}</g>']
    chip_lab = lambda col: lx_label(cx + 64, chip_y + 9, sl["chip"], 24, 150, "apertura chip", col)
    labels += [land(chip_lab("var(--muted)"), .35, .5, -12), f'<g>{lx_lit(fl[0])}{chip_lab("var(--white)")}</g>']
    # the riders go under the people: the one that gets through passes behind the middle person
    arts += riders
    pass_t = a1 + .04 + .1 * (560 - chip_y) / (714 - chip_y)
    people = "".join(lx_seat(x, base_y, .88, LX_LILAC, t) for x, t in ((cx - 78, .30), (cx + 78, .365), (cx, .43)))
    arts += [land(people, .4, .5, 12),
             f'<g opacity="0">{beat("opacity", [(0, 0), (pass_t - .02, 0), (pass_t, .85), (pass_t + .06, 0), (1, 0)])}'
             f'{glow(cx, base_y - 60, 70, LX_GOLD, .7)}</g>']
    arts.append(land(f'<path d="M{cx - wn - 20} {ny0 + 22} h-12 M{cx - wn - 20} {ny1 - 2} h-12 M{cx - wn - 32} {ny0 + 22} '
                     f'V{ny1 - 2}" fill="none" stroke="{LX_EDGE}" stroke-width="1.2"/>', .6, .5, 0))
    labels.append(land(lx_label(cx - wn - 46, 574, sl["neck"], 26, 200, "apertura neck", "var(--white)", "end"), .6, .5, 0))
    # the chat bubble: lands dim, lights when the spark that got through reaches it, then types
    bx, bw, bt, bh = 920, 540, 712, 72
    lit_b = a1 + .14
    tail_d = f"M{bx + 36} {bt + bh - 1} l-10 20 l30 -20"
    bub = lambda edge, fill, sw, node: (
        f'<path d="{tail_d}" fill="{fill}" stroke="{edge}" stroke-width="{sw}" stroke-linejoin="round"/>'
        + lx_card(bx, bt, bw, bh, 24, edge, sw, fill)
        + f'<path d="M{bx + 37.5} {bt + bh - 1.5} h17" stroke="{fill}" stroke-width="3"/>'
        + lx_node(bx + 30, bt + bh / 2, 5, node, False))
    say = lambda col: lx_label(bx + 54, bt + bh / 2 + 7, sl["chat"], 20, bw - 150, "apertura chat", col)
    arts += [land(bub(LX_EDGE, LX_GLASS, 1.2, LX_DIM), .5, .5, 14),
             f'<g>{lx_lit(lit_b)}{glow(cx, bt + bh / 2, 150, "var(--brand)", .6)}' + bub(LX_LILAC, LX_GLASS_LIT, 1.8, LX_GOLD)
             + f'<circle cx="{bx + 30}" cy="{bt + bh / 2}" r="9" fill="none" stroke="{LX_GOLD}" stroke-width="1.2">'
             + f'{loop("opacity", "1;.1;1", 1.6)}</circle>'
             + "".join(f'<circle cx="{bx + bw - 64 + 14 * j}" cy="{bt + bh / 2}" r="3" fill="{LX_GOLD}">'
                       f'{loop("opacity", ".2;1;.2", 1.2, j * .3)}</circle>' for j in range(3)) + '</g>']
    labels += [land(say("var(--muted)"), .5, .5, 14), f'<g>{lx_lit(lit_b)}{say("var(--white)")}</g>']
    text = "".join(labels)
    g = [lx_depth(LX_ZONE["left"], n=34, seed="apertura", labels=text, avoid=[(bx, bt, bw, bh + 24)]),
         lx_drift("".join(arts) + text, cx, 455)]
    return "".join(g), D, FREEZE


# ================================================================ harvested from s04_06.py (v2)
"""Slides 4-6 of the webinar «IA: ¿el fin del piloto eterno?», drawn with the world «Luz de operación» (worlds/luz.py), v2.

w04_divisor - a large magenta orbit (the thread) keeps closing on itself around three inner orbits full of small pilot
              satellites (capacity everywhere). Each 6 s lap the spark leaves it towards «Operación», slows near it and
              bends back; the orbit closes with a flash, a ripple runs inwards and lights half the satellites; «Capacidad»
              lights (lap 1) and glows brighter (lap 2). «Operación» waits outside, dim and readable. Frozen: bright
              orbit, every satellite lit, «Capacidad» lit, the spark on its track, «Operación» dim outside.
w05_ciclo   - the pilot's loop (lx_loop at 1110, 360, r 140: the same place as slide 10) laps every 4 s with a magenta
              comet tail; each pass by «Demo» drops one more demo onto the shelf the thread draws below. At 5 s a spark
              peels off towards «Operar», which lights with a question mark; it lingers at the door, hesitates, and
              rejoins the loop at 9 s. Frozen: three demos on the shelf, «Operar» lit with its «?», the stub short of it.
w06_datos   - three public figures, static, in glass cards, and a wall of light with one tall narrow door
              («Operación»). Each card's edge lights in turn and its sparks look for the door along the wall; one crosses
              with its magenta trail, the door lights, the three edges glow together and the spark stays lit on the
              other side. Frozen: three still figures, lit edges, the door lit, one spark past it.
"""


# ---------------------------------------------------------------- slide 4: the orbit that closes on itself
_W04_C = (1190, 455)
_W04_R = 290


def _w04_pt(deg, r=_W04_R):
    a = math.radians(deg)
    return _W04_C[0] + r * math.cos(a), _W04_C[1] + r * math.sin(a)


def _w04_tan(deg):
    """The clockwise (screen) tangent of the orbit at deg."""
    a = math.radians(deg)
    return -math.sin(a), math.cos(a)


def _w04_bez(p0, p1, p2, p3, n=64):
    """The length of a cubic Bézier, sampled."""
    pts = [tuple((1 - t) ** 3 * p0[i] + 3 * (1 - t) ** 2 * t * p1[i] + 3 * (1 - t) * t * t * p2[i] + t ** 3 * p3[i]
                 for i in (0, 1)) for t in (k / n for k in range(n + 1))]
    return sum(math.dist(a, b) for a, b in zip(pts, pts[1:]))


def _w04_p(p):
    return f"{p[0]:.1f} {p[1]:.1f}"


def _w04_sat(x, y, tone=None):
    """A small pilot satellite at (x, y): unlit (tone None) a hollow glass bead; lit, its core and ring glow in tone."""
    if tone is None:
        return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{LX_GLASS}" stroke="{LX_EDGE}" stroke-width="1.2"/>'
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2" fill="{LX_DIM}"/>')
    return (glow(f"{x:.1f}", f"{y:.1f}", 20, tone, .6)
            + f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{LX_GLASS_LIT}" stroke="{tone}" stroke-width="1.4"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.8" fill="{tone}"/>')


@register("scene", "w04_divisor")
def sc_w04_divisor(sl, ctx):
    """The divider. A large orbit of light (the magenta thread, r 290) with a spark lapping it every 6 s (laps at 1.5 and
    7.5 s). Inside, three orbits carry 27 small pilot satellites that turn at their own pace: capacity everywhere. Each
    lap, just past the top, the spark leaves on a tangent towards «Operación», slows near it and bends back into the
    orbit, which flashes as it closes: a ripple runs inwards and lights half the satellites, the orbit gains a layer of
    light, «Capacidad» lights (then glows brighter). «Operación», a dim hollow node outside, notices each visit with a
    faint ring and never lights: an open question, not a verdict. Labels are painted last (lx_on_top)."""
    if ORIENT() == "portrait":
        return _wq04_divisor(sl, ctx)
    cx, cy = _W04_C
    r = _W04_R
    ring = ring_path(cx, cy, r)
    nx, ny = 1486, 150                                        # «Operación», outside the orbit
    p1, p2, ap = _w04_pt(-80), _w04_pt(-15), _w04_pt(-49, 372)  # leaves at -80°, reaches towards the node, rejoins at -15°
    t1, t2 = _w04_tan(-80), _w04_tan(-15)
    c1 = (p1[0] + 110 * t1[0], p1[1] + 110 * t1[1])
    c2, c3 = (ap[0] - 55, ap[1] + 5), (ap[0] + 55, ap[1] - 5)
    c4 = (p2[0] - 70 * t2[0], p2[1] - 70 * t2[1])
    top = (cx, cy - r)
    la, lb1, lb2, lc = r * math.radians(10), _w04_bez(p1, c1, c2, ap), _w04_bez(ap, c3, c4, p2), r * math.radians(285)
    tot = la + lb1 + lb2 + lc
    fa, fap, fp2 = la / tot, (la + lb1) / tot, (la + lb1 + lb2) / tot
    lap = (f"M{_w04_p(top)} A{r} {r} 0 0 1 {_w04_p(p1)} C{_w04_p(c1)} {_w04_p(c2)} {_w04_p(ap)} "
           f"C{_w04_p(c3)} {_w04_p(c4)} {_w04_p(p2)} A{r} {r} 0 1 1 {_w04_p(top)}")
    bend = f"M{_w04_p(p1)} C{_w04_p(c1)} {_w04_p(c2)} {_w04_p(ap)} C{_w04_p(c3)} {_w04_p(c4)} {_w04_p(p2)}"
    # one lap = 6 s from 1.5 s: top .0, leaves .3, apex 1.2, hovers to 1.6, rejoins 2.2
    stops = [(0, 0), (.05, fa), (.14, fa + .7 * (fap - fa)), (.2, fap), (.267, fap + .002), (.367, fp2), (1, 1)]
    ev = [[(1.5 + 6 * k + s) / 12 for s in (.3, 1.2, 1.6, 2.2)] for k in (0, 1)]   # leave, apex, hover end, rejoin
    h = lb1 / (lb1 + lb2)
    dash, op, flash, near = [(0, 1)], [(0, 0)], [(0, 0)], [(0, 0)]
    for e1, e2, e3, e4 in ev:
        dash += [(e1, 1), (e2, 1 - h), (e3, 1 - h), (e4, 0), (e4 + .06, 0), (e4 + .061, 1)]
        op += [(e1, 0), (e1 + .003, .95), (e4, .95), (e4 + .05, 0)]
        flash += [(e4 - .003, 0), (e4 + .015, .6), (e4 + .07, 0)]
        near += [(e2 - .01, 0), (e2 + .01, .55), (e3 + .02, 0)]
    dash, op, flash, near = dash + [(1, 1)], op + [(1, 0)], flash + [(1, 0)], near + [(1, 0)]
    close1, close2 = ev[0][3] + .005, ev[1][3] + .005
    arts, labels = [], []
    arts.append(glow(cx, cy, 380, "var(--brand)", .5))
    arts.append(land(lx_orbit(cx, cy, r + 36, dash="2 14", period=48, op=.35), .1, .5, 0))
    arts.append(lx_trail(ring, width=2.4, begin=.1, dur=1.4, spark=False))
    # brightness gained at each closing (it accumulates)
    arts.append(f'<g>{lx_lit(close1)}<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LX_MAGENTA}" '
                f'stroke-width="18" opacity=".12"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LX_MAGENTA}" '
                f'stroke-width="2.8"/></g>')
    arts.append(f'<g>{lx_lit(close2)}<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LX_MAGENTA}" '
                f'stroke-width="34" opacity=".08"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
                f'stroke="color-mix(in srgb, var(--accent) 45%, var(--white))" stroke-width="1.2"/></g>')
    arts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LX_MAGENTA}" stroke-width="7" opacity="0">'
                f'{beat("opacity", flash)}</circle>')
    # capacity everywhere: three inner orbits of small pilot satellites, each turning at its own pace; a ripple runs
    # inwards from each closing and lights half of them (radius order: the outer ones first)
    tones = (LX_LILAC, LX_MAGENTA, LX_LILAC, LX_GOLD)
    orbits = ((160, 6, 36, True, 0), (205, 9, 54, False, 20), (248, 12, 72, True, 8))
    sats = []
    for i, (ro, n, per, rev, off) in enumerate(orbits):
        base, lit = [], []
        for j in range(n):
            x, y = _w04_pt(off + j * 360 / n, ro)
            at = (close1 if (i + j) % 2 == 0 else close2) + .045 * (r - ro) / 130
            base.append(_w04_sat(x, y))
            lit.append(f'<g>{lx_lit(at, f=.012)}{_w04_sat(x, y, tones[(i + j) % 4])}</g>')
        sats.append(f'<g>{spin(cx, cy, per, rev)}'
                    f'{lx_orbit(cx, cy, ro, dash="2 10", op=.3)}{"".join(base)}{"".join(lit)}</g>')
    arts.append(seq(sats, .3, .5, 0))
    rip_r, rip_o = [(0, r)], [(0, 0)]
    for c in (close1, close2):
        rip_r += [(c, r), (c + .045, 150), (c + .047, r)]
        rip_o += [(c, 0), (c + .004, .55), (c + .045, 0)]
    arts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LX_MAGENTA}" stroke-width="2" opacity="0">'
                f'{beat("r", rip_r + [(1, r)])}{beat("opacity", rip_o + [(1, 0)])}</circle>')
    # «Operación»: a dim hollow node outside, waiting; a faint ring answers each visit of the spark
    arts.append(land(f'<circle cx="{nx}" cy="{ny}" r="15" fill="{LX_GLASS}" stroke="{LX_EDGE}" stroke-width="1.2" '
                     f'stroke-dasharray="3 4"/><circle cx="{nx}" cy="{ny}" r="4" fill="{LX_DIM}"/>'
                     f'<circle cx="{nx}" cy="{ny}" r="26" fill="none" stroke="{LX_LILAC}" stroke-width="1" opacity="0">'
                     f'{beat("opacity", near)}</circle>', .8, .5, 0))
    # the escape that bends back, drawn only while the spark tries it, and the spark itself
    arts.append(f'<path d="{bend}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{LX_MAGENTA}" '
                f'stroke-width="10" stroke-linecap="round" opacity="0">{beat("stroke-dashoffset", dash)}'
                f'{beat("opacity", [(t, v * .14) for t, v in op])}</path>'
                f'<path d="{bend}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{LX_MAGENTA}" stroke-width="2.2" '
                f'stroke-linecap="round" opacity="0">{beat("stroke-dashoffset", dash)}{beat("opacity", op)}</path>')
    arts.append(f'<g opacity="0"><set attributeName="opacity" to="1" begin="1.50s" fill="freeze"/>'
                f'{move(lap, stops, 6, begin=1.5)}{lx_spark(0, 0, .85)}</g>')
    # the labels, last: «Capacidad» large (muted, lit at the first closing, brighter at the second), «Operación» dim
    word = sl["inside"]
    z = fit(word, 48, 2 * 160 - 48, "w04 inside", floor=LX_MIN)
    wx, wy = f"{cx}", f"{cy + z * .36:.1f}"
    neon = lambda sw, o: TC(wx, wy, word, z, "none", f'{W6} stroke="{LX_MAGENTA}" stroke-width="{sw}" '
                                                     f'stroke-linejoin="round" opacity="{o}"')
    labels.append(land(TC(wx, wy, word, z, "var(--muted)", W6), .5, .5, 0))
    labels.append(f'<g>{lx_lit(close1)}{neon(z * .12, .14)}{TC(wx, wy, word, z, "var(--white)", W6)}</g>')
    labels.append(f'<g>{lx_lit(close2)}{neon(z * .2, .1)}{neon(z * .05, .5)}{TC(wx, wy, word, z, "var(--white)", W6)}</g>')
    labels.append(land(lx_label(nx, ny - 34, sl["outside"], 20, 170, "w04 outside", "var(--muted)", "middle"), .8, .5, 0))
    scene = lx_on_top([("".join(arts), "".join(labels))])
    return lx_depth(n=36, seed="w04 piloto", labels=scene) + lx_drift(scene), D, FREEZE


# ---------------------------------------------------------------- slide 5: the loop that never reaches «Operar»
def _w05_qmark(x, y, at):
    """A question mark drawn as a luminous stroke (a pictogram, not copy), centred on (x, y): it draws itself at `at`
    and stays until the loop resets."""
    d = f"M{x - 9} {y - 12} C{x - 9} {y - 26} {x + 11} {y - 26} {x + 11} {y - 12} C{x + 11} {y - 3} {x} {y - 2} {x} {y + 9}"
    run = beat("stroke-dashoffset", [(0, 1), (at, 1), (at + .03, 0), (.97, 0), (.99, 1), (1, 1)])
    return (f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{LX_MAGENTA}" stroke-width="7" '
            f'stroke-linecap="round" opacity=".18">{run}</path>'
            f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--white)" stroke-width="2.6" '
            f'stroke-linecap="round">{run}</path>'
            f'<circle cx="{x}" cy="{y + 19}" r="2.8" fill="var(--white)" opacity="0">'
            f'{beat("opacity", [(0, 0), (at + .03, 0), (at + .035, 1), (.97, 1), (.99, 0), (1, 0)])}</circle>')


@register("scene", "w05_ciclo")
def sc_w05_ciclo(sl, ctx):
    """lx_loop at (1110, 360), r 140 (slide 10 reuses this place), stops at 20 px: the spark laps Idea → POC → Demo every
    4 s with a magenta comet tail in step with it. Each pass by «Demo» (2.7, 6.7, 10.7 s) drops one more demo onto the
    shelf the magenta thread draws from «Demo» downwards: they pile up. At 5 s, as the carrier passes the ring's right
    point, a second spark peels off along the stub towards «Operar»: the door lights (6 s) and a question mark draws
    itself inside it; the spark lingers short of the door, hesitates, drifts back and rejoins the carrier at 9 s.
    Curiosity, not failure. Frozen: three demos, «Operar» lit with its «?», the dashed stub short of the door."""
    if ORIENT() == "portrait":
        return _wq05_ciclo(sl, ctx)
    cx, cy, r = 1110, 360, 140
    demo = sl["stops"][2]
    ring = ring_path(cx, cy, r)
    dx, dy = cx + r * math.cos(math.radians(150)), cy + r * math.sin(math.radians(150))
    gx = cx + r + 120                                          # the door's centre (lx_loop's gate)
    sy, cw, ch = 740, 150, 56                                  # the shelf line, one demo chip
    xs = (1010, 1180, 1350)
    tail = "".join(f'<path d="{ring}" pathLength="1" fill="none" stroke="{LX_MAGENTA}" stroke-width="{w_}" '
                   f'stroke-linecap="round" stroke-dasharray="{L} {1 - L:.2f}" opacity="{o}">'
                   f'<animate attributeName="stroke-dashoffset" values="{L};{L - 1:.2f}" dur="4s" repeatCount="indefinite"/>'
                   f'</path>' for w_, L, o in ((18, .3, .14), (8, .22, .3), (3, .16, 1)))
    halo = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LX_LILAC}" stroke-width="26" opacity=".09"/>'
    loop_ = lx_loop(cx, cy, r, sl["stops"], sl["exit"], exit_lit=.5, lap=4, size=20)
    arts = [glow(cx, cy + 60, 330, "var(--brand)", .5),
            land(halo + tail + loop_, .1, .6, 0),
            f'<path d="M896 {sy} H1452" stroke="{LX_LILAC}" stroke-width="18" opacity=".06" stroke-linecap="round"/>',
            lx_trail(f"M{dx:.1f} {dy + 14:.1f} C{dx:.1f} 600 900 610 900 {sy - 40} Q900 {sy} 940 {sy} H1450",
                     width=2.4, begin=.4, dur=1.3, spark=False)]
    top = sy - ch - 10
    arts.append(land("".join(f'<rect x="{x - cw / 2:.1f}" y="{top}" width="{cw}" height="{ch}" rx="14" fill="none" '
                             f'stroke="{LX_DIM}" stroke-width="1.2" stroke-dasharray="4 6"/>' for x in xs), .9, .5, 0))
    chips, words = [], []
    for k, x in enumerate(xs):
        at = (4 * k + 8 / 3) / 12 - .006                          # the spark passes «Demo»
        drop = (f'<animateTransform attributeName="transform" type="translate" values="0 -22;0 -22;0 0;0 0" '
                f'keyTimes="0;{at:.3f};{at + .011:.3f};1" dur="{D}s" repeatCount="indefinite"/>')
        chips.append(f'<g>{lx_lit(at, f=.012)}{drop}{glow(x, top + ch / 2, 80, LX_GOLD, .3)}'
                     + lx_card(x - cw / 2, top, cw, ch, 14, LX_LILAC, 1.6, LX_GLASS_LIT) + '</g>'
                     + f'<rect x="{x - cw / 2 - 4:.1f}" y="{top - 4}" width="{cw + 8}" height="{ch + 8}" rx="18" fill="none" '
                       f'stroke="{LX_GOLD}" stroke-width="1.6" opacity="0">'
                       f'{beat("opacity", [(0, 0), (at, 0), (at + .012, .9), (at + .06, 0), (1, 0)])}</rect>')
        words.append(f'<g>{lx_lit(at, f=.012)}{drop}'
                     + lx_label(x, top + ch / 2 + 7, demo, 20, cw - 24, "w05 demo", "var(--white)", "middle") + '</g>')
    arts += chips
    # the curious spark: it peels off at the ring's right point (5 s), lingers short of the door, hesitates, and rejoins
    # the carrier at the same point (9 s); a magenta line follows it along the stub
    x_on, x_far = cx + r, gx - 50
    run = [(0, 0), (5 / 12, 0), (5.35 / 12, .62), (6 / 12, 1), (6.6 / 12, .8), (7.1 / 12, .96), (7.8 / 12, .7),
           (9 / 12, 0), (1, 0)]
    shown = [(0, 0), (5 / 12, 0), (5 / 12 + .003, 1), (9 / 12, 1), (9 / 12 + .004, 0), (1, 0)]
    stub = f"M{x_on} {cy} H{x_far}"
    arts.append(f'<path d="{stub}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{LX_MAGENTA}" stroke-width="2.4" '
                f'stroke-linecap="round" opacity="0">{beat("stroke-dashoffset", [(t, 1 - p) for t, p in run])}'
                f'{beat("opacity", shown)}</path>'
                f'<g opacity="0">{beat("opacity", shown)}{move(stub, run, D)}{lx_spark(0, 0, .7)}</g>')
    arts.append(_w05_qmark(gx, 312, .52))
    scene = lx_on_top([("".join(arts), "".join(words))])
    return lx_depth(n=34, seed="w05 ciclo", labels=scene) + lx_drift(scene), D, FREEZE


# ---------------------------------------------------------------- slide 6: three figures and a narrow door
def _w06_curve(pts, n=24):
    """A smooth quadratic through three points as a sampled polyline: (points, length)."""
    (x0, y0), (x1, y1), (x2, y2) = pts
    ps = [((1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t * t * x2, (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t * t * y2)
          for t in (k / n for k in range(n + 1))]
    return ps, sum(math.dist(a, b) for a, b in zip(ps, ps[1:]))


def _w06_seek(o, hit, slide, t0, t1, t2):
    """A spark from o to the wall at hit (fractions t0 → t1), then along the wall by slide px, fading by t2."""
    ps, la = _w06_curve((o, ((o[0] + hit[0]) / 2 + 10, o[1]), hit))
    ps.append((hit[0], hit[1] + slide))
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in ps)
    f = la / (la + abs(slide))
    return (f'<g opacity="0">{beat("opacity", [(0, 0), (t0, 0), (t0 + .004, 1), (t1, 1), (t2, 0), (1, 0)])}'
            f'{move(d, [(0, 0), (t0, 0), (t1, f), (t2, 1), (1, 1)], D)}{lx_spark(0, 0, .6)}</g>'
            f'<circle cx="{hit[0]:.1f}" cy="{hit[1]:.1f}" r="6" fill="none" stroke="{LX_LILAC}" stroke-width="1.2" opacity="0">'
            f'{beat("opacity", [(0, 0), (t1 - .004, 0), (t1, .8), (t1 + .05, 0), (1, 0)])}</circle>')


@register("scene", "w06_datos")
def sc_w06_datos(sl, ctx):
    """Three public figures, static (lx_figure at 72 px), stacked in glass cards that never move; at x 1470 a wall of
    light with one tall narrow door («Operación», 44 x 176). Each card's edge lights in turn and seven sparks leave it
    for the wall: they hit it and slide along it looking for the door, then fade. The last one from the third card
    crosses with its magenta trail (.72 → .80): the door lights, the three edges glow together and the spark stays lit
    on the other side. The wall layer (not the figures) drifts gently."""
    if ORIENT() == "portrait":
        return _wq06_datos(sl, ctx)
    x0, w, pad, gap, vz = 832, 470, 26, 18, 72
    figs = sl["figure"]
    hs = [lx_figure(x0 + pad, 0, f["v"], f["label"], f["src"], w - 2 * pad, f.get("pre"), vz)[1] + 2 * 20 for f in figs]
    y = max(96, 455 - (sum(hs) + gap * (len(hs) - 1)) / 2)
    turns = ((.10, .30), (.33, .53), (.56, .76))
    cross_at, lit_at = .765, .80
    cards, edges, ys = [], [], []
    for (f, h), (a, b) in zip(zip(figs, hs), turns):
        cards.append(lx_card(x0, y, w, h, 18) + lx_figure(x0 + pad, y + 20, f["v"], f["label"], f["src"], w - 2 * pad,
                                                          f.get("pre"), vz)[0])
        pts = [(0, 0), (a, 0), (a + .02, 1), (b, 1)]
        pts += [(b + .03, .45), (lit_at, .45)] if b + .03 < lit_at else []
        pts += [(lit_at + .02, 1), (.97, 1), (.99, 0), (1, 0)]
        rect = lambda sw, o: (f'<rect x="{x0}" y="{y:.1f}" width="{w}" height="{h:.1f}" rx="18" fill="none" '
                              f'stroke="{LX_MAGENTA}" stroke-width="{sw}" opacity="{o}"/>')
        edges.append(f'<g opacity="0">{beat("opacity", pts)}{rect(9, .14)}{rect(2, 1)}</g>')
        ys.append(y + h / 2)
        y += h + gap
    still = [glow(1090, 455, 420, "var(--brand)", .45), seq(cards, .1, .5, 16)] + edges
    # the wall and its tall narrow door
    wx, base, gh, gw = 1470, 560, 176, 44
    wall = (f'<path d="M{wx} 104 V{base - gh - 12} M{wx} {base + 50} V806" stroke="{LX_LILAC}" stroke-width="10" opacity=".05"/>'
            f'<path d="M{wx} 104 V{base - gh - 12} M{wx} {base + 50} V806" stroke="{LX_EDGE}" stroke-width="1.4" '
            f'stroke-dasharray="3 7"/>')
    g = [land(wall + lx_gate(wx, base, sl["door"], gw, gh, lit=cross_at), .6, .5, 0)]
    # the sparks: seven per card look for the door along the wall and fade
    ox = x0 + w + 8
    hits = ((150, 36), (215, 34), (300, 36), (660, -34), (730, -36), (330, 30), (770, -30))
    for k, (a, b) in enumerate(turns):
        for j in range(7):
            hy, slide = hits[(j + 3 * k) % 7]
            t0 = a + .015 + j * .026
            if k == 2 and j == 6:
                break                                           # the third card's last spark is the one that crosses
            g.append(_w06_seek((ox, ys[k] + (j - 3) * 9), (wx - 8, hy), slide, t0, t0 + .05, t0 + .085))
    # the one that crosses: rises early (clear of the door's label), passes the door, stays lit beyond it
    gy, far = base - gh / 2 + 10, (wx + 60, base - gh / 2 + 2)
    ps, la = _w06_curve(((ox, ys[2]), (ox + 20, gy), (wx - 22, gy)))
    ps += [(wx, gy), far]
    d = "M" + " L".join(f"{x:.1f} {yy:.1f}" for x, yy in ps)
    tot = la + 22 + math.dist((wx, gy), far)
    run = beat("stroke-dashoffset", [(0, 1), (.72, 1), (lit_at, 0), (.97, 0), (.99, 1), (1, 1)])
    g.append(f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{LX_MAGENTA}" stroke-width="12" '
             f'opacity=".13" stroke-linecap="round">{run}</path>'
             f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{LX_MAGENTA}" stroke-width="2.4" '
             f'stroke-linecap="round">{run}</path>')
    g.append(f'<g opacity="0">{beat("opacity", [(0, 0), (.72, 0), (.724, 1), (lit_at, 1), (lit_at + .01, 0), (1, 0)])}'
             f'{move(d, [(0, 0), (.72, 0), (cross_at, (la + 22) / tot), (lit_at, 1), (1, 1)], D)}{lx_spark(0, 0, .7)}</g>')
    g.append(f'<g>{lx_lit(lit_at)}{lx_spark(far[0], far[1], 1.0)}</g>')
    art = "".join(still) + lx_drift("".join(g), cx=wx, cy=base - gh / 2, scale=1.015, dx=0, dy=-5)
    return lx_depth(n=30, seed="w06 datos", labels=art) + art, D, FREEZE


# ================================================================ harvested from s07_09.py (v2)
"""Slides 7-9 of the webinar «IA: ¿el fin del piloto eterno?», world «Luz de operación» (worlds/luz.py kit), v2.

w07_salto  (top)  the table Piloto | Operación, bigger: the spark comes down the thread on its right edge and stops at
                  each row; there a pulse crosses the gutter from the pilot cell to the operation cell (the pilot dims,
                  still readable; the operation lights and joins the thread). After «Mejoró un proceso» the spark reaches
                  the big KPI gauge, hops on the needle and rides it up: the arc fills in gold, the ticks light, the dial
                  blooms. 10.8 s: five rows lit, needle up.
w08_formas (left) the ladder of six rungs (Prompt at the bottom → Multiagente on top) with wide four-cell rails: a spark
                  climbs one rung every 1.56 s; each rung, its rail, its name and its sentence light and stay lit; the
                  objective cell is always empty with its gold edge; at the end a gold wave runs up the objective column
                  and the rule's dash draws. 10.8 s: six rungs lit, the objective column empty and gold.
w09_costo  (left) the console, bigger: the spark crosses it and each panel tells its pictogram — before acting the scope
                  closes, the lock clicks and only the data inside light; while acting the trace draws, a person presses
                  pause, the trace waits and resumes; when it fails a calm alert, the marker rewinds to a checkpoint and
                  the person who answers lights. Then the budget's exchange: tokens travel, the clock turns, the benefit
                  bars grow. 10.8 s: three panels and the exchange resolved.
Every visible text comes from the slide's args. Loaded after worlds/luz.py: helpers are _w07_/_w08_/_w09_. Labels are
painted after every glow, spark and lit glass (art layer first, label layer last).
"""

_w07_TXT = "color-mix(in srgb, var(--c2) 70%, var(--ink))"   # an unlit label: dim, still AA (about 5:1 on the glass)


def _w07_dim(a, f=.02):
    """Opacity of a copy lit from the start that goes dark at a and comes back when the loop resets (.97-.99)."""
    return beat("opacity", [(0, 1), (a, 1), (a + f, 0), (.97, 0), (.99, 1), (1, 1)])


def _w07_spark(d, stops, show=.13, hide=.97, s=.7):
    """A spark riding path d on the scene clock (begin 0): visible from show to hide."""
    return (f'<g opacity="0">{beat("opacity", [(0, 0), (show, 0), (show + .005, 1), (hide, 1), (hide + .005, 0), (1, 0)])}'
            f'<g>{move(d, list(stops), D)}{lx_spark(0, 0, s)}</g></g>')


def _w07_draw(d, color, width, pairs, extra=""):
    """Path d drawn along its length on the loop: pairs = [(fraction of the loop, drawn fraction 0..1)]."""
    return (f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{color}" stroke-width="{width}" {extra}>'
            + beat("stroke-dashoffset", [(t, f"{1 - v:.4f}") for t, v in pairs]) + '</path>')


def _w07_chev(x, y, color, sw=1.6):
    """A small chevron pointing right, centered at (x, y)."""
    return (f'<path d="M{x - 4:.1f} {y - 7:.1f} L{x + 4:.1f} {y:.1f} L{x - 4:.1f} {y + 7:.1f}" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')


def _w07_pulse(x0, x1, y, a, b):
    """A small magenta pulse crossing from x0 to x1 at height y between fractions a and b (hidden otherwise)."""
    d = f"M{x0:.1f} {y:.1f} H{x1:.1f}"
    op = beat("opacity", [(0, 0), (a, 0), (a + .004, 1), (b, 1), (b + .006, 0), (1, 0)])
    return (f'<g opacity="0">{op}<g>{move(d, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}'
            f'{glow(0, 0, 15, LX_MAGENTA, .8)}<circle r="4.5" fill="{LX_MAGENTA}"/></g></g>')


def _w07_gauge(cx, cy, r, rise, up):
    """The KPI gauge (lx_gauge) and its climax: at rise the spark hops on the needle and rides it up with a small
    overshoot; the arc fills in gold behind it, the ticks it passes light, and the dial blooms (the bloom stays above
    the hub: nothing glows under the label)."""
    ov = min(up + .05, 1)
    t1, t2 = rise + .075, rise + .11
    pairs = [(0, 0), (rise, 0), (t1, ov), (t2, up), (.965, up), (.995, 0), (1, 0)]
    kt = ";".join(f"{t:.3f}" for t, _v in pairs)
    arc = f"M{cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy}"
    g = [f'<g opacity="0">{beat("opacity", [(0, 0), (rise + .03, 0), (t1, 1), (t2 + .05, .62), (.97, .62), (.99, 0), (1, 0)])}'
         f'{glow(cx, f"{cy - r * .45:.1f}", f"{r * .55:.1f}", LX_GOLD, .5)}</g>',
         lx_gauge(cx, cy, r, None, pairs, size=22),
         _w07_draw(arc, LX_GOLD, 3.4, pairs, 'stroke-linecap="butt"')]
    for k in range(7):
        v = k / 6
        if v > up:
            break
        a = math.radians(180 + k * 30)
        x0, y0, x1, y1 = cx + (r - 14) * math.cos(a), cy + (r - 14) * math.sin(a), cx + (r + 2) * math.cos(a), cy + (r + 2) * math.sin(a)
        g.append(f'<g>{lx_lit(rise + (t1 - rise) * v / ov, .965)}<path d="M{x0:.1f} {y0:.1f} L{x1:.1f} {y1:.1f}" stroke="{LX_GOLD}" '
                 f'stroke-width="2.4" stroke-linecap="round"/></g>')
    vals = ";".join(f"{v * 180:.1f} {cx} {cy}" for _t, v in pairs)
    rot = (f'<animateTransform attributeName="transform" type="rotate" values="{vals}" keyTimes="{kt}" dur="{D}s" '
           f'repeatCount="indefinite" calcMode="linear"/>')
    g.append(f'<g opacity="0">{beat("opacity", [(0, 0), (rise, 0), (rise + .004, 1), (t2, 1), (t2 + .05, 0), (1, 0)])}'
             f'<g transform="rotate({up * 180:.1f} {cx} {cy})">{rot}{lx_spark(cx - r + 10, cy, .8)}</g></g>')
    return "".join(g), t1


@register("scene", "w07_salto")
def sc_w07_salto(sl, ctx):
    if ORIENT() == "portrait":
        return _wq07_salto(sl, ctx)
    head, rows = sl["head"], sl["rows"]
    n = len(rows)
    xl, xp, wp, xo, wo = 104, 244, 330, 634, 400          # label x · pilot cell · operation cell
    y0, rh, gap = 432, 66, 10                              # first row top, row height, gap
    xt = xo + wo + 22                                      # the thread, down the table's right edge
    gr, gcx = 200, 1296                                    # the gauge, bigger
    at = [.19 + k * .105 for k in range(n)]                # when each row lights
    rise, up = at[-1] + .07, .8
    ycs = [y0 + k * (rh + gap) + rh / 2 for k in range(n)]
    gcy = ycs[-1]
    top = y0 - 28
    x1 = gcx - gr
    d = f"M{xt} {top} V{gcy - 20:.1f} A20 20 0 0 0 {xt + 20} {gcy:.1f} H{x1}"
    l1 = gcy - 20 - top
    lt = l1 + math.pi * 10 + (x1 - xt - 20)
    ps = [(y - top) / lt for y in ycs[:-1]] + [(l1 + 16) / lt]
    # the spark's front on the thread: it reaches row k just before the row hands over, then goes on
    front = [(0, 0), (.125, 0)]
    for k, p in enumerate(ps):
        front += [(at[k] - .045, p), (at[k] + .01, p)]
    front += [(rise, 1), (.965, 1), (.995, 0), (1, 0)]
    gx = (xp + wp + xo) / 2
    arts, labs = [], []
    hy = y0 - 18
    hd = ""
    if head[0]:
        hd += lx_label(xl, hy, head[0], 22, xp - xl - 16, "salto head", _w07_TXT)
    hd += lx_label(xp + wp / 2, hy, head[1], 24, wp - 20, "salto head", "var(--muted)", "middle")
    hd += lx_label(xo + wo / 2, hy, head[2], 24, wo - 20, "salto head", "var(--white)", "middle")
    arts.append("")
    labs.append(hd)
    for k, (lab, pil, op) in enumerate(rows):
        yt, yc = y0 + k * (rh + gap), ycs[k]
        last = k == n - 1
        edge = LX_GOLD if last else LX_LILAC
        h0 = at[k] - .04                                   # the handover: pilot → operation, h0 .. at[k]
        conn = f"M{xp + wp} {yc:.1f} H{xo}"
        arts.append("".join([
            # pilot cell: lit edge until its row hands over, then dim
            lx_card(xp, yt, wp, rh, 12, LX_DIM),
            f'<g>{_w07_dim(at[k])}{lx_card(xp, yt, wp, rh, 12, LX_EDGE, 1.4)}</g>',
            # operation cell: dark with its indicator off
            lx_card(xo, yt, wo, rh, 12, LX_DIM),
            f'<circle cx="{xo + 24}" cy="{yc:.1f}" r="6" fill="none" stroke="{LX_EDGE}" stroke-width="1.4"/>',
            f'<path d="{conn}" stroke="{LX_DIM}" stroke-width="1.4"/>', _w07_chev(gx, yc, LX_EDGE),
            f'<path d="M{xo + wo} {yc:.1f} H{xt}" stroke="{LX_DIM}" stroke-width="1.2"/>',
            # the handover: the gutter draws in magenta, the operation lights and joins the thread
            _w07_draw(conn, LX_MAGENTA, 2, [(0, 0), (h0, 0), (at[k], 1), (.97, 1), (.99, 0), (1, 0)]),
            f'<g>{lx_lit(at[k])}'
            + lx_card(xo, yt, wo, rh, 12, edge, 1.8, LX_GLASS_LIT)
            + glow(xo + 24, f"{yc:.1f}", 18, LX_GOLD, .8)
            + f'<circle cx="{xo + 24}" cy="{yc:.1f}" r="6" fill="{LX_GOLD}"/>' + _w07_chev(gx, yc, LX_GOLD, 2)
            + f'<path d="M{xo + wo} {yc:.1f} H{xt}" stroke="{LX_MAGENTA}" stroke-width="1.8"/>'
            + f'<circle cx="{xt}" cy="{yc:.1f}" r="4.5" fill="{LX_MAGENTA}"/></g>',
            _w07_pulse(xp + wp - 6, xo + 24, yc, h0, at[k])]))
        labs.append(lx_label(xl, yc + 8, lab, 22, xp - xl - 16, "salto row", "var(--white)")
                    # pilot: white until its row hands over, then dim (the dim copy stays readable)
                    + lx_label(xp + 24, yc + 8, pil, 22, wp - 48, "salto pilot", _w07_TXT, bold=False)
                    + f'<g>{_w07_dim(at[k])}{lx_label(xp + 24, yc + 8, pil, 22, wp - 48, "salto pilot", "var(--white)", bold=False)}</g>'
                    # operation: dim until it lights; the last, «Mejoró un proceso», lights in gold
                    + f'<g>{_w07_dim(at[k])}{lx_label(xo + 48, yc + 8, op, 22, wo - 68, "salto op", _w07_TXT, bold=False)}</g>'
                    + f'<g>{lx_lit(at[k])}{lx_label(xo + 48, yc + 8, op, 22, wo - 68, "salto op", LX_GOLD if last else "var(--white)", bold=last)}</g>')
    gauge, t1 = _w07_gauge(gcx, gcy, gr, rise, up)
    arts.append(gauge)
    glab = sl.get("gauge") or ""
    labs.append(lx_label(gcx, gcy + 46, glab, 22, 2 * gr, "salto gauge", _w07_TXT, "middle")
                + f'<g>{lx_lit(t1)}{lx_label(gcx, gcy + 46, glab, 22, 2 * gr, "salto gauge", "var(--white)", "middle")}</g>'
                if glab else "")
    spine = (lx_trail(d, "color-mix(in srgb, var(--accent) 45%, transparent)", begin=.1, dur=1.4, spark=False)
             + _w07_draw(d, LX_MAGENTA, 3, front, 'stroke-linecap="round" opacity=".9"')
             + _w07_spark(d, front[:-3] + [(1, 1)], .125, rise))
    art = glow(820, 640, 220, "var(--brand)", .4) + seq(arts, .1, .5, 14) + spine
    text = seq(labs, .1, .5, 14)
    return (lx_depth(LX_ZONE["top"], 30, "x07", labels=text)
            + lx_drift(art + text, 800, 612, 1.015, 0, -5)), D, FREEZE


@register("scene", "w08_formas")
def sc_w08_formas(sl, ctx):
    if ORIENT() == "portrait":
        return _wq08_formas(sl, ctx)
    rungs, cells = sl["rungs"], sl["cells"]
    n = len(rungs)
    lx0, lw = 832, 40                                      # the ladder
    rx, cw, ch, gp = 892, 84, 24, 8                        # the rails, wider
    rw = lx_rail_w(cw, gp)
    y0, s = 100, 100                                       # ladder top, rung spacing: y 100 .. 700
    room = 1556 - rx
    at = [.12 + k * .13 for k in range(n)]                 # one rung every 1.56 s
    wave = at[-1] + .04                                    # the gold wave up the objective column
    lad, ys = lx_ladder(lx0, y0, lw, s * n, n, light_at=at)
    arts, labs = [lad], [""]
    for k, (name, desc, states) in enumerate(rungs):
        y = ys[k]
        ox, oy = rx + cw / 2, y
        w0 = wave + k * .012
        arts.append("".join([
            f'<path d="M{lx0 + lw} {y:.1f} H{rx}" stroke="{LX_EDGE}" stroke-width="1.2"/>',
            f'<g>{lx_lit(at[k])}<path d="M{lx0 + lw} {y:.1f} H{rx}" stroke="{LX_MAGENTA}" stroke-width="1.8"/>'
            f'{glow(f"{ox:.1f}", f"{oy:.1f}", 28, LX_GOLD, .3)}</g>',
            lx_rail(rx, y - ch / 2, states, cw, ch, gp, fill_at=at[k]),
            # the objective cell, lit: a gold edge over the kit's, always empty
            f'<g>{lx_lit(at[k])}<rect x="{rx}" y="{y - ch / 2:.1f}" width="{cw}" height="{ch}" rx="5" fill="none" '
            f'stroke="{LX_GOLD}" stroke-width="1.8"/></g>',
            # the wave: the objective column brightens from the bottom to the top
            f'<g opacity="0">{beat("opacity", [(0, 0), (w0, 0), (w0 + .015, 1), (w0 + .04, 0), (1, 0)])}'
            f'{glow(f"{ox:.1f}", f"{oy:.1f}", 44, LX_GOLD, .45)}</g>'
            f'<g opacity="0">{beat("opacity", [(0, 0), (w0, 0), (w0 + .015, 1), (.97, 1), (.99, 0), (1, 0)])}<rect x="{rx - 2}" y="{y - ch / 2 - 2:.1f}" width="{cw + 4}" '
            f'height="{ch + 4}" rx="7" fill="none" stroke="{LX_GOLD}" stroke-width="1.4"/></g>']))
        nx = rx + rw + 20
        dsc0, _h = lx_lines(rx, y + ch / 2 + 24, desc, room, 16, "formas rung text", _w07_TXT)
        dsc1, _h = lx_lines(rx, y + ch / 2 + 24, desc, room, 16, "formas rung text", "var(--muted)")
        labs.append(lx_label(nx, y + 8, name, 22, 1556 - nx, "formas rung name", _w07_TXT)
                    + f'<g>{lx_lit(at[k])}{lx_label(nx, y + 8, name, 22, 1556 - nx, "formas rung name", "var(--white)")}</g>'
                    + dsc0 + f'<g>{lx_lit(at[k])}{dsc1}</g>')
    hy = ys[-1] - ch / 2 - 12
    arts.append(f'<g opacity="0">{beat("opacity", [(0, 0), (wave + .05, 0), (wave + .065, 1), (.97, 1), (.99, 0), (1, 0)])}'
                f'<path d="M{rx + 10} {hy + 7:.1f} H{rx + cw - 10}" stroke="{LX_GOLD}" stroke-width="2" stroke-linecap="round"/></g>')
    labs.append("".join(lx_label(rx + j * (cw + gp) + cw / 2, hy, c, 16, cw + 6, "formas cell",
                                 LX_GOLD if j == 0 else "var(--muted)", "middle", bold=j == 0) for j, c in enumerate(cells)))
    ly = y0 + s * n + 34
    leg, _w = lx_rail_legend(rx, ly, sl["legend"], cw, ch, 17)
    arts.append("")
    labs.append(leg)
    if sl.get("rule"):
        ry = ly + ch + 38
        dash = f"M{rx} {ry - 7} h40"
        arts.append(f'<path d="{dash}" stroke="{LX_EDGE}" stroke-width="2" stroke-linecap="round"/>'
                    + _w07_draw(dash, LX_GOLD, 2.4, [(0, 0), (wave + .05, 0), (wave + .075, 1), (.97, 1), (.99, 0), (1, 0)],
                                'stroke-linecap="round"'))
        labs.append(lx_label(rx + 54, ry, sl["rule"], 20, room - 54, "formas rule", "var(--white)"))
    x_ = lx0 + lw / 2
    d = f"M{x_} {y0 + s * n} V{ys[-1]:.1f}"
    ln = y0 + s * n - ys[-1]
    stops = [(0, 0), (at[0], (y0 + s * n - ys[0]) / ln)]
    for k in range(1, n):
        stops += [(at[k] - .05, (y0 + s * n - ys[k - 1]) / ln), (at[k], (y0 + s * n - ys[k]) / ln)]
    stops.append((1, 1))
    art = (seq(arts, .1, .5, 12) + lx_trail(d, begin=.05, dur=1.0, spark=False) + _w07_spark(d, stops, .07))
    text = seq(labs, .1, .5, 12)
    return lx_depth(LX_ZONE["left"], 26, "x08", labels=text) + lx_drift(art + text), D, FREEZE


def _w09_tr(kind, pairs):
    """A transform loop with explicit times (kind translate | rotate | scale): pairs = [(fraction, "values")]."""
    kt = ";".join(f"{t:.3f}" for t, _v in pairs)
    vals = ";".join(v for _t, v in pairs)
    return (f'<animateTransform attributeName="transform" type="{kind}" values="{vals}" keyTimes="{kt}" dur="{D}s" '
            f'repeatCount="indefinite"/>')


def _w09_ring(x, y, a, color=LX_GOLD, r0=10, r1=34):
    """A click: a thin ring that grows from r0 to r1 and fades, once, from a to a + .05."""
    return (f'<circle cx="{x}" cy="{y}" r="{r0}" fill="none" stroke="{color}" stroke-width="1.6" opacity="0">'
            + beat("r", [(0, r0), (a, r0), (a + .05, r1), (1, r1)])
            + beat("opacity", [(0, 0), (a, 0), (a + .005, .9), (a + .05, 0), (1, 0)]) + '</circle>')


def _w09_before(a):
    """Antes de actuar, around (0, 0): the scope (a dashed boundary) with its open lock and the data it may touch. At a
    the boundary draws itself solid, the shackle drops and the lock clicks gold; then only the data inside light, one
    by one; the two outside stay dark."""
    bx, by, bw, bh, rr = -86, -46, 130, 108, 14
    box = (f"M{bx + rr} {by} H{bx + bw - rr} A{rr} {rr} 0 0 1 {bx + bw} {by + rr} V{by + bh - rr} "
           f"A{rr} {rr} 0 0 1 {bx + bw - rr} {by + bh} H{bx + rr} A{rr} {rr} 0 0 1 {bx} {by + bh - rr} V{by + rr} "
           f"A{rr} {rr} 0 0 1 {bx + rr} {by} Z")
    inside = [(-60, -8), (-24, -16), (-50, 34), (-4, 30)]
    outside = [(68, -22), (76, 32)]
    lx, ly = bx + bw / 2, by
    g = [f'<path d="{box}" fill="none" stroke="{LX_EDGE}" stroke-width="1.4" stroke-dasharray="4 6"/>',
         _w07_draw(box, LX_LILAC, 1.8, [(0, 0), (a, 0), (a + .05, 1), (.97, 1), (.99, 0), (1, 0)])]
    g += [f'<circle cx="{x}" cy="{y}" r="7" fill="none" stroke="{LX_EDGE}" stroke-width="1.4"/>' for x, y in inside]
    g += [f'<circle cx="{x}" cy="{y}" r="6" fill="none" stroke="{LX_DIM}" stroke-width="1.4"/>' for x, y in outside]
    shackle = f'<path d="M{lx - 9} {ly - 8} V{ly - 16} A9 9 0 0 1 {lx + 9} {ly - 16} V{ly - 8}" fill="none" stroke="{{c}}" stroke-width="2"/>'
    body = (f'<rect x="{lx - 16}" y="{ly - 8}" width="32" height="25" rx="5" fill="{LX_GLASS}" stroke="{{c}}" stroke-width="1.8"/>'
            f'<circle cx="{lx}" cy="{ly + 3}" r="3" fill="{{c}}"/>')
    drop = _w09_tr("translate", [(0, "0 -8"), (a + .05, "0 -8"), (a + .065, "0 0"), (.97, "0 0"), (.99, "0 -8"), (1, "0 -8")])
    g.append(f'<g>{_w07_dim(a + .05)}<g transform="translate(0 -8)">{shackle.format(c=LX_EDGE)}</g>{body.format(c=LX_EDGE)}</g>')
    g.append(f'<g>{lx_lit(a + .05)}{glow(lx, ly, 30, LX_GOLD, .7)}<g>{drop}{shackle.format(c=LX_GOLD)}</g>'
             f'{body.format(c=LX_GOLD)}</g>')
    g.append(_w09_ring(lx, ly + 2, a + .065))
    for k, (x, y) in enumerate(inside):
        g.append(f'<g>{lx_lit(a + .08 + k * .015)}{glow(x, y, 18, LX_MAGENTA, .7)}<circle cx="{x}" cy="{y}" r="7" fill="{LX_MAGENTA}"/></g>')
    return "".join(g)


def _w09_while(a):
    """Mientras actúa, around (0, 0): the work leaves a trace that draws itself node by node; a person holds the pause
    control. At a + .06 the person lights and presses pause: the trace waits (its head pulses), then resumes to its end
    at a + .16. The control stays lit: a human can stop it."""
    pts = [(-88, 50), (-63, 14), (-38, 30), (-13, -8), (12, 6), (36, -30)]
    seg = [math.hypot(x1 - x0, y1 - y0) for (x0, y0), (x1, y1) in zip(pts, pts[1:])]
    tot, acc = sum(seg), [0]
    for v in seg:
        acc.append(acc[-1] + v)
    f3 = acc[3] / tot
    p0, p1, p2 = a + .01, a + .06, a + .12                 # draw to node 3, pause, resume
    tn = [p0 + (p1 - p0) * acc[j] / acc[3] if j <= 3 else p2 + .04 * (acc[j] - acc[3]) / (tot - acc[3]) for j in range(len(pts))]
    dd = "M" + " L".join(f"{x} {y}" for x, y in pts)
    g = [f'<path d="{dd}" fill="none" stroke="{LX_DIM}" stroke-width="1.4" stroke-dasharray="3 5"/>',
         _w07_draw(dd, LX_LILAC, 2, [(0, 0), (p0, 0), (p1, f3), (p2, f3), (p2 + .04, 1), (.97, 1), (.99, 0), (1, 0)],
                   'stroke-linecap="round" stroke-linejoin="round"')]
    for j, (x, y) in enumerate(pts):
        g.append(f'<circle cx="{x}" cy="{y}" r="4.5" fill="none" stroke="{LX_EDGE}" stroke-width="1.2"/>'
                 f'<g>{lx_lit(tn[j])}<circle cx="{x}" cy="{y}" r="4.5" fill="{LX_GOLD}"/></g>')
    hx, hy = pts[3]
    g.append(f'<g opacity="0">{beat("opacity", [(0, 0), (p1, 0), (p1 + .01, 1), (p1 + .03, .35), (p1 + .045, 1), (p2, .5), (p2 + .01, 0), (1, 0)])}'
             f'{glow(hx, hy, 22, LX_GOLD, .9)}</g>')
    px, py = 64, 74
    g.append(lx_seat(px, py, .6, lit=p1))
    bx, by = px, -34
    btn = (f'<circle r="18" fill="{LX_GLASS}" stroke="{{c}}" stroke-width="1.8"/>'
           f'<path d="M-5 -7 V7 M5 -7 V7" stroke="{{c}}" stroke-width="2.6" stroke-linecap="round"/>')
    press = _w09_tr("scale", [(0, "1"), (p1, "1"), (p1 + .012, ".82"), (p1 + .03, "1"), (1, "1")])
    g.append(f'<g transform="translate({bx} {by})">{btn.format(c=LX_EDGE)}</g>')
    g.append(f'<g>{lx_lit(p1)}{glow(bx, by, 32, LX_GOLD, .7)}<g transform="translate({bx} {by})"><g>{press}'
             f'{btn.format(c=LX_GOLD)}</g></g></g>')
    g.append(_w09_ring(bx, by, p1 + .012, LX_GOLD, 18, 40))
    return "".join(g)


def _w09_fail(a):
    """Cuando falla, around (0, 0): work runs along a timeline of four checkpoints; at a a calm alert lights (two soft
    gold blinks, then steady), the recovery rewinds (the arrow turns back and the marker slides back to the second
    checkpoint, which lights), and the person who answers lights with a click."""
    ax, ay = -62, -30
    tri = (f'<path d="M{ax} {ay - 28} L{ax + 28} {ay + 20} L{ax - 28} {ay + 20} Z" fill="{LX_GLASS}" stroke="{{c}}" '
           f'stroke-width="1.8" stroke-linejoin="round"/><path d="M{ax} {ay - 11} V{ay + 5}" stroke="{{c}}" stroke-width="2.4" '
           f'stroke-linecap="round"/><circle cx="{ax}" cy="{ay + 13}" r="2" fill="{{c}}"/>')
    g = [tri.format(c=LX_EDGE)]
    blinks = [(0, 0), (a, 0), (a + .008, 1), (a + .018, .35), (a + .028, 1), (a + .038, .35), (a + .048, 1), (.97, 1), (.99, 0), (1, 0)]
    g.append(f'<g opacity="0">{beat("opacity", blinks)}{glow(ax, ay, 34, LX_GOLD, .6)}{tri.format(c=LX_GOLD)}</g>')
    rx_, ry_, r = 14, -32, 22
    arc = (f'<path d="M{rx_ + r * .87:.1f} {ry_ - r * .5:.1f} A{r} {r} 0 1 0 {rx_ + r:.1f} {ry_ + 6:.1f}" fill="none" '
           f'stroke="{{c}}" stroke-width="2" stroke-linecap="round"/>'
           f'<path d="M{rx_ + r * .87 - 9:.1f} {ry_ - r * .5 - 4:.1f} L{rx_ + r * .87:.1f} {ry_ - r * .5:.1f} '
           f'L{rx_ + r * .87 - 2:.1f} {ry_ - r * .5 + 9:.1f}" fill="none" stroke="{{c}}" stroke-width="2" '
           f'stroke-linecap="round" stroke-linejoin="round"/>')
    b0, b1 = a + .05, a + .11
    g.append(arc.format(c=LX_EDGE))
    turn = _w09_tr("rotate", [(0, f"0 {rx_} {ry_}"), (b0, f"0 {rx_} {ry_}"), (b1, f"-360 {rx_} {ry_}"), (1, f"-360 {rx_} {ry_}")])
    g.append(f'<g>{lx_lit(b0)}{glow(rx_, ry_, 26, LX_LILAC, .28)}<g>{turn}{arc.format(c=LX_LILAC)}</g></g>')
    tx = [-80, -52, -24, 4]
    ty = 52
    g.append(f'<path d="M{tx[0]} {ty} H{tx[-1]}" stroke="{LX_EDGE}" stroke-width="1.6"/>')
    g += [f'<circle cx="{x}" cy="{ty}" r="5" fill="{LX_GLASS}" stroke="{LX_EDGE}" stroke-width="1.4"/>' for x in tx]
    g.append(f'<g>{lx_lit(b1)}{glow(tx[1], ty, 20, LX_GOLD, .7)}<circle cx="{tx[1]}" cy="{ty}" r="5" fill="{LX_GOLD}"/></g>')
    slide = _w09_tr("translate", [(0, "0 0"), (.06, "0 0"), (a, f"{tx[-1] - tx[0]} 0"), (b0, f"{tx[-1] - tx[0]} 0"),
                                  (b1, f"{tx[1] - tx[0]} 0"), (.97, f"{tx[1] - tx[0]} 0"), (.99, "0 0"), (1, "0 0")])
    g.append(f'<g transform="translate({tx[1] - tx[0]} 0)">{slide}<circle cx="{tx[0]}" cy="{ty}" r="8" fill="none" '
             f'stroke="{LX_LILAC}" stroke-width="2"/></g>')
    px, py = 64, 72
    g.append(lx_seat(px, py, .6, lit=b1 + .01))
    g.append(_w09_ring(px, py - 56, b1 + .01, LX_LILAC, 14, 40))
    return "".join(g)


def _w09_trade(a):
    """The budget's exchange around its left edge (0, 0), about 400 x 60: six tokens, an arrow, time (a clock) and
    benefit (three bars). At a three tokens leave along the arrow (their places stay hollow), at a + .05 the clock
    lights and its hand turns, then the bars grow one by one: tokens traded for time and benefit."""
    coins = [(12 + (k % 3) * 28, -14 + (k // 3) * 28) for k in range(6)]
    ax0, ax1 = 104, 236
    g = []
    for k, (x, y) in enumerate(coins):
        g.append(f'<circle cx="{x}" cy="{y}" r="10" fill="{LX_GLASS}" stroke="{LX_LILAC}" stroke-width="1.4"/>')
        if k < 3:  # the ones that travel: lit until they leave
            g.append(f'<g>{_w07_dim(a + k * .015)}<circle cx="{x}" cy="{y}" r="10" fill="{LX_LILAC}"/></g>')
        else:
            g.append(f'<circle cx="{x}" cy="{y}" r="10" fill="{LX_LILAC}"/>')
        g.append(f'<circle cx="{x}" cy="{y}" r="4.5" fill="none" stroke="{LX_GLASS}" stroke-width="1.4"/>')
    g.append(f'<path d="M{ax0} 0 H{ax1}" stroke="{LX_EDGE}" stroke-width="1.6"/><path d="M{ax1 - 8} -7 L{ax1} 0 L{ax1 - 8} 7" '
             f'fill="none" stroke="{LX_EDGE}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>')
    g.append(f'<g>{lx_lit(a)}<path d="M{ax0} 0 H{ax1}" stroke="{LX_MAGENTA}" stroke-width="2"/><path d="M{ax1 - 8} -7 L{ax1} 0 '
             f'L{ax1 - 8} 7" fill="none" stroke="{LX_MAGENTA}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>')
    for k in range(3):
        t0 = a + k * .015
        x, y = coins[k]
        path = f"M{x} {y} L{ax0} 0 H{ax1 + 20}"
        g.append(f'<g opacity="0">{beat("opacity", [(0, 0), (t0, 0), (t0 + .004, 1), (t0 + .05, 1), (t0 + .056, 0), (1, 0)])}'
                 f'<g>{move(path, [(0, 0), (t0, 0), (t0 + .05, 1), (1, 1)], D)}{glow(0, 0, 16, LX_LILAC, .6)}'
                 f'<circle r="8" fill="{LX_LILAC}"/></g></g>')
    b = a + .05
    kx, r = 284, 26
    hand = f'<path d="M{kx} 0 V-17" stroke="{{c}}" stroke-width="2.2" stroke-linecap="round"/>'
    clock = (f'<circle cx="{kx}" cy="0" r="{r}" fill="{LX_GLASS}" stroke="{{c}}" stroke-width="1.8"/>'
             f'<path d="M{kx} 0 H{kx + 11}" stroke="{{c}}" stroke-width="2.2" stroke-linecap="round"/>')
    g.append(clock.format(c=LX_EDGE) + hand.format(c=LX_EDGE))
    turn = _w09_tr("rotate", [(0, f"0 {kx} 0"), (b, f"0 {kx} 0"), (b + .06, f"360 {kx} 0"), (1, f"360 {kx} 0")])
    g.append(f'<g>{lx_lit(b)}{glow(kx, 0, 40, LX_GOLD, .45)}{clock.format(c=LX_GOLD)}<g>{turn}{hand.format(c=LX_GOLD)}</g></g>')
    bx, base = 336, 28
    for k, hh in enumerate((22, 36, 52)):
        x = bx + k * 22
        t = b + .02 + k * .015
        grow = _w09_tr("scale", [(0, "1 0"), (t, "1 0"), (t + .03, "1 1"), (.97, "1 1"), (.99, "1 0"), (1, "1 0")])
        g.append(f'<rect x="{x}" y="{base - hh}" width="14" height="{hh}" rx="3" fill="none" stroke="{LX_EDGE}" stroke-width="1.4"/>')
        g.append(f'<g transform="translate({x} {base})"><g>{grow}<rect x="0" y="{-hh}" width="14" height="{hh}" rx="3" '
                 f'fill="{LX_GOLD if k == 2 else LX_LILAC}"/></g></g>')
    return "".join(g)


def _w09_at(x, y, s, inner):
    return f'<g transform="translate({x:.1f} {y:.1f}) scale({s})">{inner}</g>'


@register("scene", "w09_costo")
def sc_w09_costo(sl, ctx):
    if ORIENT() == "portrait":
        return _wq09_costo(sl, ctx)
    panels = sl["panels"]
    x, y, w, h = 826, 92, 730, 500                         # the console, bigger
    at = [.18, .40, .62]                                   # when the spark lights each panel
    n, pad, gap = len(panels), 18, 14
    pw = (w - 2 * pad - (n - 1) * gap) / n
    cxs = [x + pad + k * (pw + gap) + pw / 2 for k in range(n)]
    ts, isz = 20, 18
    low = y + 50 + 72                                      # where the items end (same layout as lx_console)
    for _t, items in panels:
        yy = y + 50 + 72
        for it in items:
            _s, lh_ = lx_lines(0, 0, it, pw - 50, isz, "luz console item")
            yy += lh_ + 14
        low = max(low, yy - 14)
    ty, tx0, tx1 = low + 10, 812, x + w - 12               # the thread crosses the console under the items
    d = f"M{tx0} {ty:.1f} H{tx1}"
    ps = [(c - tx0) / (tx1 - tx0) for c in cxs]
    stops = [(0, 0), (.13, 0)]
    for k, p in enumerate(ps):
        stops += [(at[k] - .02, p), (at[k] + .06, p)]
    stops += [(at[-1] + .12, 1), (1, 1)]
    icons = [_w09_before, _w09_while, _w09_fail]
    pcy = (ty + y + h - 18) / 2 + 6
    pics = "".join(_w09_at(cxs[k], pcy, 1.18, icons[k](at[k])) for k in range(min(n, 3)))
    by = y + h + 38
    txt, th = lx_lines(x + 24, by, sl["budget"], w - 24, 19, "costo budget", "var(--white)")
    bar = (f'<path d="M{x + 4} {by - 18} V{by - 18 + th:.1f}" stroke="{LX_MAGENTA}" stroke-width="2.4" stroke-linecap="round"/>')
    ta = at[-1] + .12
    bar += _w07_draw(f"M{x + 4} {by - 18} V{by - 18 + th:.1f}", LX_MAGENTA, 4, [(0, 0), (ta - .04, 0), (ta, 1), (.97, 1), (.99, 0), (1, 0)],
                     'stroke-linecap="round"')
    trade = _w09_at(x + 24, by + th + 26, 1.2, _w09_trade(ta))
    art = (glow(1191, 330, 280, "var(--brand)", .4)
           + land(lx_console(x, y, w, h, panels, light_at=at, title_size=ts, item_size=isz), .1, .6, 16)
           + land(pics, .4, .6, 10)
           + land(bar + trade, .8, .6, 12)
           + lx_trail(d, begin=.3, dur=1.4, spark=False) + _w07_spark(d, stops, .14, at[-1] + .12))
    text = land(txt, .8, .6, 12)
    return lx_depth(LX_ZONE["left"], 26, "x09", labels=text) + lx_drift(art + text), D, FREEZE


# ================================================================ harvested from s10_12.py (v2)
"""Slides 10-12 of the webinar «IA: ¿el fin del piloto eterno?», world «Luz de operación» (worlds/luz.py), v2:
w10_ola (the loop of slide 5, now carried by three agent icons with their light tails; a spark leaves the ring toward
the exit «Operar» and waits at its lit threshold: the question stays open; the static «Más del 40 %» figure, large),
w11_escala (E-S-C-A-L-A in big letters of light: the trail grows with its spark, lights each letter, its word and its
question in turn, then rises toward the panel) and w12_panel (a spotlight visits the three seats of a table in
perspective; each seat, its pool of light, its node and its card light and stay lit). Runs in the shared namespace
after worlds/luz.py: no imports, private helpers _w10_/_w11_/_w12_. Every scene: lx_depth under, lx_drift on the art,
labels last."""


def _w11_rider(d, stops, show, s=.7):
    """A spark riding path d on the scene clock (begin 0, so stops' times are the loop's own fractions).
    stops: [(t, fraction of the path)]; show: [(t, opacity)] of the rider."""
    return f'<g opacity="0">{beat("opacity", show)}<g>{move(d, stops, D)}{lx_spark(0, 0, s)}</g></g>'


def _w11_grow(d, pairs, color=LX_MAGENTA, width=2):
    """Path d drawn along with a rider on the scene clock: pairs [(t, fraction of the path drawn)] (a halo and the
    stroke). The same (t, fraction) pairs as the rider keep the trail's head under the spark."""
    off = [(t, round(1 - f, 4)) for t, f in pairs]
    return "".join(f'<path d="{d}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" fill="none" stroke="{color}" '
                   f'stroke-width="{w}" stroke-linecap="round" opacity="{op}">{beat("stroke-dashoffset", off)}</path>'
                   for w, op in ((width * 5, .13), (width, 1)))


def _w11_ripple(x, y, t, color=LX_GOLD, r1=40):
    """A ring of light that opens at (x, y) at fraction t and is gone .07 later (never visible at the 10.8 s frame)."""
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="none" stroke="{color}" stroke-width="1.6" opacity="0">'
            + beat("r", [(0, 6), (t, 6), (t + .07, r1), (1, r1)])
            + beat("opacity", [(0, 0), (t, 0), (t + .005, .9), (t + .07, 0), (1, 0)]) + '</circle>')


def _w11_len(pts):
    """Length of a polyline [(x, y), …]."""
    return sum(math.hypot(x1 - x0, y1 - y0) for (x0, y0), (x1, y1) in zip(pts, pts[1:]))


# ---------------------------------------------------------------- slide 10: la próxima ola
def _w10_bot(s=1.0):
    """An agent icon around (0, 0), s x 42 px: a dark-glass disk with a magenta edge holding a small bot head (a gold
    visor, an antenna with its gold tip, two side studs). Opaque: drawn over lx_loop's own tokens, it replaces them."""
    return (f'<g transform="scale({s})">'
            f'<circle r="21" fill="{LX_GLASS}" stroke="{LX_MAGENTA}" stroke-width="1.8"/>'
            f'<rect x="-10" y="-5" width="20" height="14" rx="4" fill="none" stroke="var(--white)" stroke-width="1.5"/>'
            f'<path d="M-5.5 2 H5.5" stroke="{LX_GOLD}" stroke-width="2.6" stroke-linecap="round"/>'
            f'<path d="M0 -5 V-10 M-13 0 V4 M13 0 V4" stroke="var(--white)" stroke-width="1.5" stroke-linecap="round"/>'
            f'<circle cy="-12.5" r="2.3" fill="{LX_GOLD}"/></g>')


def _w10_tails(cx, cy, r, n, lap):
    """The light tails of n agents lapping the ring (cx, cy, r) clockwise every lap s: magenta arcs behind each agent's
    place at t = 0 (angle -90 + 360·k/n), the whole group turning with them."""
    def pt(a):
        a = math.radians(a)
        return f"{cx + r * math.cos(a):.1f} {cy + r * math.sin(a):.1f}"
    arcs = []
    for k in range(n):
        a1 = -90 + 360 * k / n - 6
        for span, op in ((52, .14), (34, .28), (16, .5)):
            arcs.append(f'<path d="M{pt(a1 - span)} A{r} {r} 0 0 1 {pt(a1)}" fill="none" stroke="{LX_MAGENTA}" '
                        f'stroke-width="3" stroke-linecap="round" opacity="{op}"/>')
    return f'<g>{spin(cx, cy, lap)}{"".join(arcs)}</g>'


@register("scene", "w10_ola")
def sc_w10_ola(sl, ctx):
    """The same loop as slide 5 (lx_loop at 1110, 360, r 140), now lapped by three agent icons with light tails (lap
    6 s), a legend chip «Agentes» at its centre. At 3.5 s (.292) an agent passes the ring's 3 o'clock and a spark leaves
    it toward the exit, drawing the magenta trail; it reaches the threshold at 6 s (.50), «Operar» lights (.52) with a
    ring of light, and the spark waits there, breathing: the question stays open. The «Más del 40 %» figure is static.
    10.8 s: agents on the ring, the trail drawn, the spark at the lit threshold, the figure with its scope and source."""
    if ORIENT() == "portrait":
        return _wq10_ola(sl, ctx)
    cx, cy, r, lap, n_ag = 1110, 360, 140, 6, 3
    stops = sl.get("stops") or ["Idea", "POC", "Demo"]
    fig = (sl.get("figure") or [{}])[0]
    ring = ring_path(cx, cy, r)
    loop_ = (lx_loop(cx, cy, r, stops=stops, exit=sl.get("exit", "Operar"), exit_lit=.52, lap=lap, agents=n_ag)
             + _w10_tails(cx, cy, r, n_ag, lap)
             + "".join(f'<g>{move(ring, [(0, 0), (1, 1)], lap, begin=-k * lap / n_ag)}{_w10_bot()}</g>' for k in range(n_ag)))
    chip = (lx_card(cx - 80, cy - 25, 160, 50, 25, LX_EDGE, 1.2)
            + f'<g transform="translate({cx - 50} {cy})">{_w10_bot(.86)}</g>')
    chip_label = lx_label(cx - 23, cy + 6.5, sl.get("agents", "Agentes"), 18, 96, "ola agents", "var(--white)")
    # the spark leaves the ring (3 o'clock) as an agent passes, and waits at the threshold of the exit (door at x 1335)
    xa, xb, t_go, t_at = cx + r, cx + r + 72, .292, .50
    d = f"M{xa} {cy} H{xb}"
    path_ = _w11_grow(d, [(0, 0), (t_go, 0), (t_at, 1), (.97, 1), (.99, 0), (1, 0)])
    rider = _w11_rider(d, [(0, 0), (t_go, 0), (t_at, 1), (1, 1)],
                       [(0, 0), (t_go - .005, 0), (t_go + .01, 1), (.97, 1), (.99, 0), (1, 0)], .8)
    wait = f'<g>{lx_lit(t_at)}<g>{loop("opacity", "1;.35;1", 2)}{glow(xb, cy, 30, LX_GOLD, .7)}</g></g>'
    door_ring = _w11_ripple(cx + r + 120, cy - 38, .52, LX_GOLD, 110)
    fsvg, _fh = lx_figure(870, 586, fig.get("v", ""), fig.get("label", ""), fig.get("src", ""), w=500,
                          pre=fig.get("pre"), size=112)
    art = (glow(cx, cy, 250, "var(--brand)", .5)
           + land(loop_ + path_ + wait + door_ring + rider, .1, .6)
           + land(chip + chip_label, .4, .5)
           + land(fsvg, .5, .6))
    return lx_depth(LX_ZONE["left"], labels=art, avoid=[(cx - r - 40, cy - r - 40, 2 * r + 80, 2 * r + 80)]) + lx_drift(art), D, FREEZE


# ---------------------------------------------------------------- slide 11: E-S-C-A-L-A
@register("scene", "w11_escala")
def sc_w11_escala(sl, ctx):
    """Six big letters of light (lx_letter, 136 px) over a faint magenta baseline across the top band. From .07 a
    spark rides the baseline, the bright trail growing behind it; it stops under each letter at .10 + k·.133 (every
    1.6 s): a ring of light opens at its node, a glint flashes on the letter, and the letter, its stem, its word and its
    question light and stay. After the last A (.767) the trail rises to the right, toward the panel, and its node
    lights at .87. 10.8 s: ESCALA lit with its six words and questions, the trail risen, the spark at its top."""
    if ORIENT() == "portrait":
        return _wq11_escala(sl, ctx)
    letters = sl.get("letters") or []
    n = max(len(letters), 1)
    x0, x1 = 104, 1428
    cw = (x1 - x0) / n
    ly, ty, wy, qy = 566, 606, 650, 688           # letter baseline, trail, word, first question line
    top = (1490, 414)                             # where the trail rises to (toward the panel)
    c1, c2 = (x1 + 56, ty), (top[0], ty - 60)
    full = f"M{x0} {ty} H{x1} C{c1[0]} {c1[1]} {c2[0]} {c2[1]} {top[0]} {top[1]}"
    bz = [((1 - u) ** 3 * x1 + 3 * (1 - u) ** 2 * u * c1[0] + 3 * (1 - u) * u * u * c2[0] + u ** 3 * top[0],
           (1 - u) ** 3 * ty + 3 * (1 - u) ** 2 * u * c1[1] + 3 * (1 - u) * u * u * c2[1] + u ** 3 * top[1])
          for u in (k / 40 for k in range(41))]
    base_len = x1 - x0
    total = base_len + _w11_len(bz)
    ts = [.10 + k * .1333 for k in range(n)]
    t_last, t_up, t_top = ts[-1] + .02, ts[-1] + .045, ts[-1] + .1
    fr = [cw * (k + .5) / total for k in range(n)]
    stops = [(0, 0), (.07, 0)]
    for k in range(n):
        stops += [(ts[k], fr[k]), ((ts[k] + .05) if k < n - 1 else t_last, fr[k])]
    stops += [(t_up, base_len / total), (t_top, 1)]
    art = [trace(f"M{x0} {ty} H{x1}", LX_MAGENTA, 2, .1, .7, 'opacity=".35"'),
           _w11_grow(full, stops + [(.97, 1), (.99, 0), (1, 0)])]
    labels = []
    for k, row in enumerate(letters):
        ch, word, q = (list(row) + ["", "", ""])[:3]
        x, t = x0 + cw * (k + .5), ts[k]
        let_svg, z = lx_letter(x, ly, ch, 136, lit=t, room=cw - 36, where="escala letter")
        zw = fit(word, 24, cw - 16, "escala word", floor=22)
        qsvg, _qh = lx_lines(x, qy, q, cw - 8, 18, "escala question", "var(--muted)", "middle")
        art.append(f'<circle cx="{x:.1f}" cy="{ty}" r="4" fill="{LX_LILAC}"/>'
                   + f'<g>{lx_lit(t)}<path d="M{x:.1f} {ly + 10} V{ty - 8}" stroke="{LX_GOLD}" stroke-width="1.6" '
                     f'stroke-linecap="round" opacity=".7"/>{glow(f"{x:.1f}", ty, 18, LX_GOLD, .8)}'
                     f'<circle cx="{x:.1f}" cy="{ty}" r="5" fill="{LX_GOLD}"/></g>'
                   + _w11_ripple(x, ty, t)
                   + f'<g opacity="0">{beat("opacity", [(0, 0), (t, 0), (t + .015, 1), (t + .07, 0), (1, 0)])}'
                     f'{lx_spark(x + z * .34, ly - z * .72, .55)}</g>')
        labels.append(let_svg + TC(f"{x:.1f}", wy, word, zw, "var(--muted)", W6)
                      + f'<g>{lx_lit(t)}' + TC(f"{x:.1f}", wy, word, zw, "var(--white)", W6) + qsvg + '</g>')
    art.append(f'<g>{lx_lit(t_top)}{lx_node(top[0], top[1], 6, LX_MAGENTA)}</g>' + _w11_ripple(top[0], top[1], t_top, LX_MAGENTA, 46))
    art.append(_w11_rider(full, stops + [(1, 1)], [(0, 0), (.065, 0), (.08, 1), (.96, 1), (.98, 0), (1, 0)]))
    body = art[0] + art[1] + seq(art[2:2 + n], .15, .5) + "".join(art[2 + n:]) + seq(labels, .15, .5)
    return lx_depth(LX_ZONE["top"], labels=body) + lx_drift(body, 800, 612), D, FREEZE


# ---------------------------------------------------------------- slide 12: el panel
def _w12_cone(lx, ly, length, half, extra=""):
    """A spotlight cone pointing down from the lamp (lx, ly): length px long, half px wide at its base."""
    return (f'<path d="M{lx} {ly} L{lx - half} {ly + length:.1f} Q{lx} {ly + length + 26:.1f} {lx + half} {ly + length:.1f} Z" '
            f'fill="color-mix(in srgb, var(--c2) 16%, transparent)" stroke="color-mix(in srgb, var(--c2) 38%, transparent)" '
            f'stroke-width="1" {extra}/>'
            + glow(lx, f"{ly + length - 30:.1f}", half * 1.1, LX_LILAC, .35))


@register("scene", "w12_panel")
def sc_w12_panel(sl, ctx):
    """The panel table in perspective (its top from the back edge y 578 to the front edge y 606, the front slab below)
    with three faceless seats (s 1.45 at x 970, 1190, 1410) resting behind it, a lamp on its rig above. A spotlight from
    the lamp visits each seat in turn (.12, .32, .52) while the trail's spark runs along the slab to its node; each seat,
    its pool of light on the table, its node and its card (role, «Por confirmar») light and stay under a soft cone.
    10.8 s: three seats lit under their soft cones, the three cards lit and readable."""
    if ORIENT() == "portrait":
        return _wq12_panel(sl, ctx)
    seats = sl.get("seats") or []
    n = len(seats) or 1
    xs = [1190 + 220 * (k - (n - 1) / 2) for k in range(n)]
    yb, yf, s = 578, 606, 1.45
    lamp = (1190, 128)
    ts = [.12 + k * .2 for k in range(n)]
    chest = yb - 60 * s
    angs = [math.degrees(math.atan2(lamp[0] - x, chest - lamp[1])) for x in xs]
    lens_ = [math.hypot(x - lamp[0], chest - lamp[1]) for x in xs]
    rig = (f'<path d="M920 96 H1460" stroke="{LX_DIM}" stroke-width="1.4"/>'
           + "".join(f'<circle cx="{x}" cy="96" r="3" fill="{LX_DIM}"/>' for x in (920, 1055, 1325, 1460))
           + f'<path d="M{lamp[0]} 96 V110" stroke="{LX_EDGE}" stroke-width="1.4"/>'
           f'<path d="M{lamp[0] - 12} 110 H{lamp[0] + 12} L{lamp[0] + 18} {lamp[1] - 2} H{lamp[0] - 18} Z" fill="{LX_GLASS}" '
           f'stroke="{LX_EDGE}" stroke-width="1.2" stroke-linejoin="round"/>'
           + lx_node(lamp[0], lamp[1], 5, LX_LILAC))
    g = [glow(1190, 470, 440, "var(--brand)", .45), land(rig, .1, .5)]
    # soft cones that stay, one per seat, from its visit on (the lights accumulate)
    for a, t, ln in zip(angs, ts, lens_):
        g.append(f'<g>{lx_lit(t + .14)}<g opacity=".5" transform="rotate({a:.1f} {lamp[0]} {lamp[1]})">'
                 f'{_w12_cone(lamp[0], lamp[1], ln, 74)}</g></g>')
    # the moving spotlight: sweeps from seat to seat, then fades into the soft cones
    rot = [(0, angs[0]), (ts[0], angs[0])]
    for k in range(1, n):
        rot += [(ts[k - 1] + .13, angs[k - 1]), (ts[k], angs[k])]
    rot += [(1, angs[-1])]
    kt = ";".join(f"{t:.3f}" for t, _a in rot)
    vals = ";".join(f"{a:.1f} {lamp[0]} {lamp[1]}" for _t, a in rot)
    spin_ = (f'<animateTransform attributeName="transform" type="rotate" values="{vals}" keyTimes="{kt}" dur="{D}s" '
             f'repeatCount="indefinite" calcMode="linear"/>')
    g.append(f'<g opacity="0">{beat("opacity", [(0, 0), (ts[0] - .03, 0), (ts[0], 1), (ts[-1] + .14, 1), (ts[-1] + .2, 0), (1, 0)])}'
             f'<g transform="rotate({angs[-1]:.1f} {lamp[0]} {lamp[1]})">{spin_}{_w12_cone(lamp[0], lamp[1], max(lens_), 82)}</g></g>')
    g.append(f'<g>{lx_lit(ts[0])}{glow(lamp[0], lamp[1], 34, LX_LILAC, .8)}</g>')
    # seats (resting on the back edge), the table top in perspective and its front slab
    g.append(land("".join(lx_seat(x, yb, s, LX_LILAC, t) for x, t in zip(xs, ts)), .2, .6))
    top_ = (f'<path d="M870 {yb} H1510 L1540 {yf} H840 Z" fill="{LX_GLASS_LIT}" stroke="{LX_EDGE}" stroke-width="1.2" '
            f'stroke-linejoin="round"/>'
            + "".join(f'<g>{lx_lit(t)}<g transform="translate({x:.1f} {yb + 14}) scale(1 .2)">{glow(0, 0, 96, LX_LILAC, .75)}</g></g>'
                      for x, t in zip(xs, ts)))
    ty = yf + 26
    table = top_ + lx_table(840, 1540, yf, 52) + "".join(f'<circle cx="{x:.1f}" cy="{ty}" r="4" fill="{LX_LILAC}"/>' for x in xs)
    g.append(land(table, .1, .6, 10))
    trail_d = f"M826 {ty} H1526"
    g.append(lx_trail(trail_d, begin=.4, dur=1.0, spark=False))
    for x, t in zip(xs, ts):
        g.append(f'<g>{lx_lit(t)}{glow(f"{x:.1f}", ty, 18, LX_GOLD, .8)}<circle cx="{x:.1f}" cy="{ty}" r="5" fill="{LX_GOLD}"/></g>'
                 + _w11_ripple(x, ty, t))
    tl = 1526 - 826
    stops = ([(0, 0), (.04, 0)] + [p for x, t in zip(xs, ts) for p in ((t, (x - 826) / tl), (t + .13, (x - 826) / tl))]
             + [(1, (xs[-1] - 826) / tl)])
    g.append(_w11_rider(trail_d, stops, [(0, 0), (.05, 0), (.07, 1), (.96, 1), (.98, 0), (1, 0)]))
    # cards in front, painted last: role + status; the card lights when its seat does
    cw_, ch_, cy_ = 204, 110, yf + 72
    cards = []
    for (role, status), x, t in zip([(list(r) + ["", ""])[:2] for r in seats], xs, ts):
        cards.append(lx_card(x - cw_ / 2, cy_, cw_, ch_, 16)
                     + f'<g>{lx_lit(t)}' + lx_card(x - cw_ / 2, cy_, cw_, ch_, 16, LX_LILAC, 1.8, LX_GLASS_LIT) + '</g>'
                     + lx_label(x, cy_ + 46, role, 22, cw_ - 28, "panel role", "var(--white)", "middle")
                     + lx_label(x, cy_ + 82, status, 19, cw_ - 28, "panel status", "var(--muted)", "middle", bold=False))
    g.append(seq(cards, .5, .5))
    art = "".join(g)
    return lx_depth(LX_ZONE["left"], labels=art, avoid=[(830, 420, 720, 380)]) + lx_drift(art), D, FREEZE


# ================================================================ harvested from s13_15.py (v2)
"""Slides 13-15 of the webinar «IA: ¿el fin del piloto eterno?», world «Luz de operación» (worlds/luz.py), v2:
w13_preguntas (the panel's five questions on a line of light; the moderator taps the one in play, a stage light falls
on it), w14_reflexiones (the public's questions arrive in the chat first, then three face-down reflections revealed
live, then the survey) and w15_final (the trail laps the pilot's loop one last time, breaks out where the cover's loop
had no exit, crosses the bridge and lands on «Operación»). Runs in the shared namespace after worlds/luz.py: no imports,
private helpers _w13_/_w14_/_w15_.

Taps (module/deck.js, deck.css): a [data-pick][data-dim] question is marked .picked (its .pick-ring shows, the others
dim, [data-hop] hides); a [data-reveal] card turns (.revealed: .reveal-on shows, .reveal-off hides) and stays. Keys 1-9
tap the Nth [data-pick]/[data-reveal] of the slide, so those groups come first and nothing else carries the attributes.
The question text of slide 13 lives outside the dimmed groups (pointer-events none, so the tap still reaches the card):
the unpicked cards dim their glass and frame while every question keeps its full contrast."""


def _w13_rider(d, stops, show, s=.7):
    """A spark riding path d on the scene clock (stops: [(t, fraction of the path)], show: [(t, opacity)])."""
    return f'<g opacity="0">{beat("opacity", show)}<g>{move(d, stops, D)}{lx_spark(0, 0, s)}</g></g>'


def _w13_turn(k, n, rest=.14, f=.03):
    """Opacity of turn k of n equal turns of the loop: lit from k/n to k/n + rest; the last turn holds to .95 (the
    10.8 s frame) and the first one fades back in as the loop wraps."""
    a = k / n
    if k == 0:
        return [(0, 1), (rest, 1), (rest + f + .02, 0), (.97, 0), (1, 1)]
    if k == n - 1:
        return [(0, 0), (a - .02, 0), (a + f, 1), (.95, 1), (.98, 0), (1, 0)]
    return [(0, 0), (a - .02, 0), (a + f, 1), (a + rest, 1), (a + rest + f + .02, 0), (1, 0)]


def _w13_stops(fracs, rest=.14):
    """Rider stops that rest under each of len(fracs) turns and jump back to the first while hidden (.975)."""
    n, st = len(fracs), []
    for k, fr in enumerate(fracs):
        st += [(k / n, fr), (min(k / n + rest, .97), fr)]
    st[-1] = (.97, fracs[-1])
    return st + [(.975, fracs[0]), (1, fracs[0])]


_W13_SHOW = [(0, 1), (.95, 1), (.97, 0), (.985, 0), (1, 1)]


def _w13_bars(x, base, color, live, n=11):
    """A small voice meter: n thin bars standing on baseline `base` from x. live: they bounce like a voice speaking;
    otherwise they rest low and still."""
    g = []
    for i in range(n):
        lo, hi, bx = 5 + (i * 5) % 9, 16 + (i * 11) % 25, x + i * 10
        a = ""
        if live:
            per, ph = (.9, 1.2, 1.0, 1.4, 1.1)[i % 5], i * .13
            a = loop("height", f"{lo};{hi};{lo}", per, ph) + loop("y", f"{base - lo};{base - hi};{base - lo}", per, ph)
        g.append(f'<rect x="{bx:.1f}" y="{base - lo}" width="5" height="{lo}" rx="2.5" fill="{color}">{a}</rect>')
    return "".join(g)


def _w13_rise(x, y_from, y_to, t, dur=.05):
    """A drop of gold light that climbs the stem from y_from to y_to at fraction t of the loop, then fades."""
    return (f'<circle cx="{x:.1f}" cy="{y_from}" r="3.5" fill="{LX_GOLD}" opacity="0">'
            f'{beat("cy", [(0, y_from), (t, y_from), (t + dur, y_to), (1, y_to)])}'
            f'{beat("opacity", [(0, 0), (t - .005, 0), (t, 1), (t + dur, 1), (t + dur + .01, 0), (1, 0)])}</circle>')


def _w13_beam(xc, top, x0, x1, bottom):
    """The stage light of the panel (slide 12) falling on a card: a lamp at (xc, top) and two soft beams, the inner one
    brighter, widening down to the card's top edge (x0..x1 at y bottom)."""
    fill = "color-mix(in srgb, var(--c4) 9%, transparent)"
    inner = (x1 - x0) * .22
    return (f'<path d="M{xc - 12:.1f} {top} L{x0:.1f} {bottom} H{x1:.1f} L{xc + 12:.1f} {top} Z" fill="{fill}"/>'
            f'<path d="M{xc - 6:.1f} {top} L{x0 + inner:.1f} {bottom} H{x1 - inner:.1f} L{xc + 6:.1f} {top} Z" fill="{fill}"/>'
            + lx_node(xc, top - 4, 5, LX_GOLD))


# ---------------------------------------------------------------- 13 · Cinco preguntas (the panel, ~29 minutes)
@register("scene", "w13_preguntas")
def sc_w13_preguntas(sl, ctx):
    """Five tall numbered cards in a row over a magenta line of light, the questions large (28 px); under each, a
    still voice meter. Ambient (data-hop, hidden after the first tap): a spark rests under each question in turn (2.4 s
    each), its card's edge glows and its voice meter speaks; far stars drift behind (lx_depth). Tap: a stage light
    falls on the card (gold beam and lamp, halo, lit glass, pulsing gold frame, «En curso», a gold voice meter that
    keeps speaking, its node beating on the line) and the other cards dim their glass; the questions stay at full
    contrast. Frozen frame: nothing picked, the five questions readable, the spark under the fifth."""
    if ORIENT() == "portrait":
        return _wq13_preguntas(sl, ctx)
    qs = list(sl["questions"])
    if not 3 <= len(qs) <= 5:   # five cards fill the row; more (reserves) go in a column: panel-questions-list
        raise ValueError(f"panel-questions takes 3 to 5 questions, not {len(qs)}: with reserves use panel-questions-list")
    live = sl.get("live", "En curso")
    n, gap, y0, h, ly = len(qs), 22, 392, 346, 794
    w = (1408 - gap * (n - 1)) / n
    xs = [96 + k * (w + gap) for k in range(n)]
    line = f"M96 {ly} H1504"
    cards, words, hop = [], [], []
    for k, (x, q) in enumerate(zip(xs, qs)):
        xc, bx, by, base = x + w / 2, x + 46, y0 + 50, y0 + h - 30
        c = (lx_card(x, y0, w, h, 20)
             + f'<circle cx="{bx:.1f}" cy="{by}" r="22" fill="{LX_GLASS_LIT}" stroke="{LX_LILAC}" stroke-width="1.6"/>'
             + _w13_bars(x + 28, base, LX_DIM, False)
             + f'<path d="M{xc:.1f} {y0 + h} V{ly - 9}" stroke="{LX_EDGE}" stroke-width="1.2"/>'
             + lx_node(xc, ly, 5, LX_LILAC, halo=False))
        # the moderator's mark (deck.css shows .pick-ring on .picked): the stage light falls on this question
        ring = (_w13_beam(xc, y0 - 100, x + 12, x + w - 12, y0)
                + glow(f"{xc:.1f}", y0 + h / 2, f"{w * .64:.1f}", LX_GOLD, .34)
                + lx_card(x, y0, w, h, 20, LX_GOLD, 2.4, LX_GLASS_LIT)
                + f'<rect x="{x - 10:.1f}" y="{y0 - 10}" width="{w + 20:.1f}" height="{h + 20}" rx="28" fill="none" '
                  f'stroke="{LX_GOLD}" stroke-width="1.4">{loop("stroke-opacity", ".15;.8;.15", 4)}</rect>'
                + f'<circle cx="{bx:.1f}" cy="{by}" r="22" fill="{LX_GLASS_LIT}" stroke="{LX_GOLD}" stroke-width="2"/>'
                + f'<circle cx="{bx:.1f}" cy="{by}" r="29" fill="none" stroke="{LX_GOLD}" stroke-width="1" opacity=".5"/>'
                + _w13_bars(x + 28, base, LX_GOLD, True)
                + f'<path d="M{xc:.1f} {y0 + h} V{ly - 9}" stroke="{LX_GOLD}" stroke-width="2"/>'
                + f'<path d="M{xc - 74:.1f} {ly} H{xc + 74:.1f}" stroke="{LX_GOLD}" stroke-width="2" stroke-linecap="round"/>'
                + glow(f"{xc:.1f}", ly, 34, LX_GOLD, .8) + f'<circle cx="{xc:.1f}" cy="{ly}" r="6" fill="{LX_GOLD}"/>'
                + f'<circle cx="{xc:.1f}" cy="{ly}" r="8" fill="none" stroke="{LX_GOLD}" stroke-width="1.4">'
                  f'{loop("r", "8;30;30", 2)}{loop("opacity", ".9;0;0", 2)}</circle>'
                + pill(xc, y0, live, LX_GOLD, ctx, 17, 200, "w13 live"))
        c += (f'<g class="pick-ring">{ring}</g>'
              + f'<rect x="{x:.1f}" y="{y0}" width="{w:.1f}" height="{h}" rx="20" fill="var(--ink)" opacity="0"/>')
        cards.append(land(f'<g data-pick="{k}" data-dim="">{c}</g>', .1 + k * .12, .5, 16))
        txt, _th = lx_lines(x + 28, y0 + 132, q, w - 56, 28, "w13 question", "var(--white)", bold=True)
        words.append(land(TC(f"{bx:.1f}", by + 7, str(k + 1), 20, "var(--white)", W6) + txt, .1 + k * .12, .5, 16))
        # the ambient turn: this card's edge glows and its voice meter speaks while the spark rests under it
        hop.append(f'<g opacity="0">{beat("opacity", _w13_turn(k, n))}'
                   + lx_card(x, y0, w, h, 20, LX_MAGENTA, 1.8, "none")
                   + f'<path d="M{xc:.1f} {y0 + h} V{ly - 9}" stroke="{LX_MAGENTA}" stroke-width="1.6"/>'
                   + glow(f"{xc:.1f}", ly, 26, LX_MAGENTA, .6) + _w13_bars(x + 28, base, LX_MAGENTA, True) + '</g>'
                   + _w13_rise(xc, ly - 9, y0 + h, max(k / n, .01)))
    fracs = [(x + w / 2 - 96) / 1408 for x in xs]
    hop.append(_w13_rider(line, _w13_stops(fracs), _W13_SHOW))
    words_ = "".join(words)
    depth = lx_depth((80, 232, 1440, 596), n=44, seed="x13", labels=words_,
                     avoid=[(x, y0, w, h) for x in xs] + [(80, ly - 10, 1440, 20)])
    g = [depth, glow(800, 600, 640, "var(--brand)", .4), lx_trail(line, begin=.15, dur=1.2, spark=False), *cards,
         land(f'<g data-hop="" pointer-events="none">{"".join(hop)}</g>', 1.3, .4, 0),
         f'<g pointer-events="none">{words_}</g>']
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 14 · Tres reflexiones de hoy: questions first, then the synthesis
_W14_TURNS = ((0, .28), (.32, .44), (.47, .59), (.62, .74), (.77, .96))  # the chat, reflections 1-3, the survey


def _w14_on(a, b, f=.03):
    """Opacity pairs of a turn lit from a to b: the first one (a 0) fades back in as the loop wraps; one that ends at
    .95 or later holds through the 10.8 s frame and resets at .97."""
    if a <= 0:
        return [(0, 1), (b, 1), (b + f, 0), (.97, 0), (1, 1)]
    if b >= .95:
        return [(0, 0), (a, 0), (a + f, 1), (.95, 1), (.98, 0), (1, 0)]
    return [(0, 0), (a, 0), (a + f, 1), (b, 1), (b + f, 0), (1, 0)]


def _w14_hand(x, y, color):
    """A raised hand (a palm, four fingers and the thumb), centered near (x, y), about 28 px tall."""
    fingers = ((-7.6, -13, 17), (-2.7, -16, 20), (2.2, -14.5, 18.5), (7.1, -10, 13.5))
    g = "".join(f'<rect x="{x + fx:.1f}" y="{y + fy:.1f}" width="4.6" height="{fh}" rx="2.3" fill="{color}"/>'
                for fx, fy, fh in fingers)
    g += f'<rect x="{x - 7.6:.1f}" y="{y - 1:.1f}" width="19.3" height="14" rx="6" fill="{color}"/>'
    g += (f'<rect x="{x - 12.5:.1f}" y="{y - 3:.1f}" width="4.6" height="12" rx="2.3" fill="{color}" '
          f'transform="rotate(-34 {x - 10.2:.1f} {y + 9:.1f})"/>')
    return g


def _w14_person(x, y):
    """A faceless chat avatar centered at (x, y): a head and shoulders in a small glass disc."""
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="{LX_GLASS}" stroke="{LX_EDGE}" stroke-width="1.2"/>'
            f'<circle cx="{x:.1f}" cy="{y - 2.5:.1f}" r="3.4" fill="{LX_LILAC}"/>'
            f'<path d="M{x - 6:.1f} {y + 7:.1f} Q{x:.1f} {y - .5:.1f} {x + 6:.1f} {y + 7:.1f}" fill="none" stroke="{LX_LILAC}" '
            f'stroke-width="1.6" stroke-linecap="round"/>')


def _w14_chat(x, y0, w, h, ask):
    """The public's questions: a chat card whose edge pulses first; a hand rises, three messages arrive one by one
    (lines, never words), someone keeps typing. Its label «Sus preguntas, por el chat» is painted last."""
    g = [lx_card(x, y0, w, h, 20, "color-mix(in srgb, var(--accent) 45%, transparent)", 1.4),
         f'<g opacity="0">{beat("opacity", _w14_on(*_W14_TURNS[0]))}'
         + lx_card(x, y0, w, h, 20, LX_MAGENTA, 2, "none")
         + f'<rect x="{x - 9}" y="{y0 - 9}" width="{w + 18}" height="{h + 18}" rx="28" fill="none" stroke="{LX_MAGENTA}" '
           f'stroke-width="1.4">{loop("stroke-opacity", ".1;.8;.1", 2)}</rect></g>']
    for j, (a, right) in enumerate(((.04, False), (.11, True), (.18, False))):
        yy, bw = y0 + 104 + j * 50, 150
        px = x + w - 34 if right else x + 34
        bx = x + w - 52 - bw if right else x + 52
        lines = "".join(f'<rect x="{bx + 14}" y="{yy + 11 + i * 11}" width="{ln}" height="5" rx="2.5" fill="{LX_LILAC}" '
                        f'opacity=".6"/>' for i, ln in enumerate((112, 70 if j != 1 else 88)))
        g.append(f'<g>{lx_lit(a, .96)}' + _w14_person(px, yy + 18)
                 + f'<rect x="{bx}" y="{yy}" width="{bw}" height="36" rx="12" fill="{LX_GLASS_LIT}" stroke="{LX_EDGE}" '
                   f'stroke-width="1.2"/>' + lines + '</g>')
    # someone is typing (three dots) and a hand rises with its call rings
    ty = y0 + h - 44
    g += [f'<circle cx="{x + 30 + i * 13}" cy="{ty}" r="3.6" fill="{LX_LILAC}">{loop("opacity", ".2;1;.2", 1.2, i * .3)}</circle>'
          for i in range(3)]
    hx, hy = x + w - 46, ty
    g.append(f'<circle cx="{hx}" cy="{hy}" r="22" fill="{LX_GLASS_LIT}" stroke="{LX_EDGE}" stroke-width="1.2"/>'
             + _w14_hand(hx - 2, hy + 1, LX_LILAC)
             + f'<g opacity="0">{beat("opacity", _w14_on(.02, .28))}'
             + f'<circle cx="{hx}" cy="{hy}" r="22" fill="{LX_GLASS_LIT}" stroke="{LX_GOLD}" stroke-width="2"/>'
             + _w14_hand(hx - 2, hy - 1, LX_GOLD) + '</g>')
    for t in (.02, .10, .18):
        g.append(f'<circle cx="{hx}" cy="{hy}" r="22" fill="none" stroke="{LX_GOLD}" stroke-width="1.4" opacity="0">'
                 f'{beat("r", [(0, 22), (t, 22), (t + .07, 46), (1, 46)])}'
                 f'{beat("opacity", [(0, 0), (t - .005, 0), (t, .9), (t + .07, 0), (1, 0)])}</circle>')
    txt, _th = lx_lines(x + 26, y0 + 52, ask, 190, 24, "w14 ask", "var(--white)", bold=True)
    return "".join(g) + txt


def _w14_survey(x, y0, w, h, label, text, ctx):
    """The survey: a gold card with the QR frame waiting for its code (corners, three finder squares, a scan line
    once it lights); its pill «Encuesta» and «QR por confirmar» painted last."""
    qx, qy, qs = x + w / 2, y0 + 168, 124
    arm, a2 = 26, qs / 2
    corners = lambda col: "".join(
        f'<path d="M{qx + sx * a2:.1f} {qy + sy * (a2 - arm):.1f} V{qy + sy * a2:.1f} H{qx + sx * (a2 - arm):.1f}" '
        f'fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
        for sx in (-1, 1) for sy in (-1, 1))
    inner = qs - 32
    finders = "".join(f'<rect x="{qx - inner / 2 + fx + 8:.1f}" y="{qy - inner / 2 + fy + 8:.1f}" width="18" height="18" rx="3" '
                      f'fill="none" stroke="{LX_EDGE}" stroke-width="1.2"/>'
                      for fx, fy in ((0, 0), (inner - 34, 0), (0, inner - 34)))
    a_on = _W14_TURNS[4][0]
    g = (lx_card(x, y0, w, h, 20, "color-mix(in srgb, var(--c4) 55%, transparent)", 1.4)
         + f'<rect x="{x:.1f}" y="{y0}" width="{w}" height="{h}" rx="20" fill="none" stroke="{LX_GOLD}" stroke-width="3">'
           f'{loop("stroke-opacity", ".08;.45;.08", 4)}</rect>'
         + f'<g>{lx_lit(a_on)}{glow(f"{qx:.1f}", qy, 72, LX_GOLD, .3)}'
         + lx_card(x, y0, w, h, 20, LX_GOLD, 2, "none") + '</g>'
         + f'<rect x="{qx - inner / 2:.1f}" y="{qy - inner / 2:.1f}" width="{inner}" height="{inner}" rx="8" fill="none" '
           f'stroke="{LX_EDGE}" stroke-width="1.2" stroke-dasharray="4 6"/>' + finders
         + f'<g>{loop("opacity", ".55;1;.55", 4)}{corners(LX_LILAC)}</g>'
         + f'<g>{lx_lit(a_on)}{corners(LX_GOLD)}'
         + f'<rect x="{qx - a2 + 12:.1f}" y="{qy - a2 + 12:.1f}" width="{qs - 24}" height="2" rx="1" fill="{LX_GOLD}" opacity=".85">'
           f'{loop("y", f"{qy - a2 + 12:.1f};{qy + a2 - 14:.1f};{qy - a2 + 12:.1f}", 2.4)}</rect></g>'
         + lx_node(qx, qy, 5, LX_GOLD)
         + pill(qx, y0 + 50, label, LX_GOLD, ctx, 18, w - 60, "w14 survey")
         + lx_label(qx, y0 + h - 34, text, 18, w - 48, "w14 survey text", "var(--muted)", "middle", bold=False))
    return g


@register("scene", "w14_reflexiones")
def sc_w14_reflexiones(sl, ctx):
    """Five moments on one thread of light, in the order of the cierre: the chat «Sus preguntas, por el chat» at the
    left, three face-down dark-glass cards «Reflexión 1/2/3» and the survey at the right, bookends of the same width.
    Ambient: the chat pulses first (0-3.4 s: a hand rises with its call rings, three messages arrive); then a spark
    leaves it along the thread and rests under each reflection, whose edge breathes in its turn, and last under the
    survey, which lights gold and scans its QR frame. Tap (data-reveal, keys 1-3): the card turns and shows «Se anota
    en vivo» under its number with three note lines writing themselves; it stays turned. Frozen frame: the messages in
    the chat, the three cards face down, the survey lit, all readable."""
    if ORIENT() == "portrait":
        return _wq14_reflexiones(sl, ctx)
    labels = list(sl.get("reflections") or ["Reflexión 1", "Reflexión 2", "Reflexión 3"])[:3]
    live = sl.get("live", "Se anota en vivo")
    ask = sl.get("ask", "Sus preguntas, por el chat")
    s_label, s_text = (list(sl.get("survey") or ["Encuesta", "QR por confirmar"]) + ["", ""])[:2]
    y0, h, ly, gap, bw = 404, 318, 786, 26, 272
    cw = (1408 - 2 * bw - 4 * gap) / 3
    xs = [96, 96 + bw + gap] + [96 + bw + gap + k * (cw + gap) for k in (1, 2)] + [1504 - bw]
    ws = [bw, cw, cw, cw, bw]
    centers = [x + w_ / 2 for x, w_ in zip(xs, ws)]
    thread = f"M{centers[0]:.1f} {ly} H{centers[-1]:.1f}"
    stems = "".join(f'<path d="M{xc:.1f} {y0 + h} V{ly - 9}" stroke="{LX_EDGE}" stroke-width="1.2"/>'
                    + lx_node(xc, ly, 5, LX_LILAC, halo=False) for xc in centers)
    parts = [_w14_chat(xs[0], y0, bw, h, ask)]
    for k, (x, lab) in enumerate(zip(xs[1:4], labels)):
        xc, ny, num = x + cw / 2, y0 + 128, f"0{k + 1}"
        off = (f'<rect x="{x + 12:.1f}" y="{y0 + 12}" width="{cw - 24:.1f}" height="{h - 24}" rx="12" fill="none" '
               f'stroke="{LX_EDGE}" stroke-width="1.2" stroke-dasharray="5 8"/>'
               + f'<g opacity="0">{beat("opacity", _w14_on(*_W14_TURNS[k + 1]))}'
               + lx_card(x, y0, cw, h, 20, LX_MAGENTA, 1.8, "none") + '</g>'
               + lx_orbit(xc, ny, 32, color=LX_LILAC, dash="2 9", period=24, op=.6)
               + f'<g>{spin(f"{xc:.1f}", ny, 12)}<circle cx="{xc:.1f}" cy="{ny - 32}" r="3" fill="{LX_GOLD}"/></g>'
               + lx_node(xc, ny, 6, LX_LILAC)
               + lx_label(x + 28, y0 + 50, num, 18, 60, "w14 number", LX_GOLD)
               + lx_label(xc, y0 + 222, lab, 28, cw - 56, "w14 reflection", "var(--white)", "middle"))
        txt, _th = lx_lines(x + 28, y0 + 118, live, cw - 56, 26, "w14 live", "var(--white)", bold=True)
        notes = "".join(
            f'<path d="M{x + 28:.1f} {y0 + h - 104 + i * 26} H{x + 28 + (cw - 56) * f:.1f}" pathLength="1" stroke-dasharray="1" '
            f'fill="none" stroke="{LX_MAGENTA if i == 0 else LX_LILAC}" stroke-width="2" stroke-linecap="round">'
            f'{beat("stroke-dashoffset", [(0, 1), (a, 1), (a + .16, 0), (.96, 0), (1, 1)])}</path>'
            for i, (f, a) in enumerate(((1, .04), (.84, .22), (.58, .4))))
        on = (glow(f"{xc:.1f}", y0 + h / 2, f"{cw * .6:.1f}", LX_MAGENTA, .28)
              + lx_card(x, y0, cw, h, 20, LX_MAGENTA, 2, LX_GLASS_LIT) + notes
              + lx_label(x + 28, y0 + 50, num, 18, 60, "w14 number", LX_GOLD)
              + lx_label(x + 66, y0 + 50, lab, 17, cw - 94, "w14 reflection small", "var(--muted)", bold=False) + txt)
        parts.append(f'<g data-reveal="{k}">' + lx_card(x, y0, cw, h, 20)
                     + f'<g class="reveal-off">{off}</g><g class="reveal-on">{on}</g>'
                     + f'<rect x="{x:.1f}" y="{y0}" width="{cw:.1f}" height="{h}" rx="20" fill="var(--ink)" opacity="0"/></g>')
    parts.append(_w14_survey(xs[4], y0, bw, h, s_label, s_text, ctx))
    cards = seq(parts, .1, .5, 16)
    fracs = [(xc - centers[0]) / (centers[-1] - centers[0]) for xc in centers]
    stops = [(0, fracs[0])]
    for k in range(1, 5):
        stops += [(_W14_TURNS[k - 1][1], fracs[k - 1]), (_W14_TURNS[k][0], fracs[k])]
    stops += [(.97, fracs[4]), (.975, fracs[0]), (1, fracs[0])]
    depth = lx_depth((80, 350, 1440, 480), n=30, seed="x14", labels=cards,
                     avoid=[(x, y0, w_, h) for x, w_ in zip(xs, ws)] + [(80, ly - 10, 1440, 20)])
    g = [depth, glow(800, 600, 640, "var(--brand)", .4), lx_trail(thread, begin=.3, dur=1.2, spark=False),
         land(stems, .6, .4, 0), cards,
         land(f'<g pointer-events="none">{_w13_rider(thread, stops, _W13_SHOW)}</g>', 1.5, .3, 0)]
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 15 · Make it happen, together.
def _w15_run(d, a, b, width=2, extra=""):
    """A magenta stroke along d that draws itself from fraction a to b of the loop, holds lit and resets at .97."""
    return (f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{LX_MAGENTA}" stroke-width="{width}" '
            f'stroke-linecap="round" {extra}>{beat("stroke-dashoffset", [(0, 1), (a, 1), (b, 0), (.97, 0), (.985, 1), (1, 1)])}</path>')


def _w15_cubic_len(p0, p1, p2, p3, n=240):
    """Length of the cubic Bézier p0 p1 p2 p3, sampled."""
    pts = [tuple((1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * b + 3 * (1 - t) * t ** 2 * c + t ** 3 * d_
                 for a, b, c, d_ in zip(p0, p1, p2, p3)) for t in (i / n for i in range(n + 1))]
    return sum(math.dist(u, v) for u, v in zip(pts, pts[1:]))


def _w15_burst(x, y, t, r0, r1, dur=.1, color=LX_GOLD, sw=1.6):
    """A ring that bursts from r0 to r1 at fraction t of the loop and fades out."""
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r0}" fill="none" stroke="{color}" stroke-width="{sw}" opacity="0">'
            f'{beat("r", [(0, r0), (t, r0), (t + dur, r1), (1, r1)])}'
            f'{beat("opacity", [(0, 0), (t - .005, 0), (t, 1), (t + dur, 0), (1, 0)])}</circle>')


def _w15_rays(x, y, t, n=8, color=LX_GOLD):
    """n short rays around (x, y) that fly out and fade at fraction t of the loop (a flash)."""
    rays = "".join(f'<path d="M{12 * math.cos(a):.1f} {12 * math.sin(a):.1f} L{21 * math.cos(a):.1f} {21 * math.sin(a):.1f}" '
                   f'stroke="{color}" stroke-width="1.8" stroke-linecap="round" vector-effect="non-scaling-stroke"/>'
                   for a in (2 * math.pi * k / n + .3 for k in range(n)))
    return (f'<g transform="translate({x:.1f} {y:.1f})"><g opacity="0">'
            f'{beat("opacity", [(0, 0), (t - .005, 0), (t, 1), (t + .08, 0), (1, 0)])}'
            f'<animateTransform attributeName="transform" type="scale" values="1;1;2.7;2.7" keyTimes="0;{t:.3f};{t + .08:.3f};1" '
            f'dur="{D}s" repeatCount="indefinite"/>{rays}</g></g>')


def _w15_comet(d, stops, show, length, width, op):
    """A short magenta tail that follows the rider along d (pathLength 1: its head at the rider's fraction)."""
    vals = [(t, round(length - s, 4)) for t, s in stops]
    return (f'<g opacity="0">{beat("opacity", show)}<path d="{d}" pathLength="1" stroke-dasharray="{length} 3" fill="none" '
            f'stroke="{LX_MAGENTA}" stroke-width="{width}" stroke-linecap="round" opacity="{op}">'
            f'{beat("stroke-dashoffset", vals)}</path></g>')


@register("scene", "w15_final")
def sc_w15_final(sl, ctx):
    """The resolution of the cover's closed loop. The pilot's loop (lx_loop, Idea → POC → Demo, «Piloto» at its
    heart) is larger; from 1 s its own carrier paints one magenta lap. At 5 s, where the ring's exit had only a dead
    stub on slide 5, the spark breaks out with a flash, swoops down onto the bridge with a comet tail and runs along it
    lighting datos · integración · control · adopción · valor (lx_bridge, labels auto-staggered); the loop behind
    dims. At 8.4 s it lands on «Operación», which bursts gold and keeps a slow heartbeat; «Audacious Ideas, Delivered
    Beyond.» appears small at the bottom right. Below the bridge, the speaker in his ring of light. Far stars and a slow
    camera drift give depth. Frozen frame: the trail landed, «Operación» lit, the loop quiet, the speaker and the line."""
    if ORIENT() == "portrait":
        return _wq15_final(sl, ctx)
    cx, cy, r = 990, 250, 112
    x0, x1 = cx + r + 72, 1490
    by = cy + 62
    t_lap0, t_brk = 1 / D, 5 / D          # lx_loop's carrier (a 4 s lap from the top) passes the ring's right point at 1, 5, 9 s
    t_deck, t_in = t_brk + .06, .70
    p0, c1, c2, p3 = (cx + r, cy), (cx + r, cy + 44), (x0 - 58, by), (x0, by)
    out = f"M{p0[0]} {p0[1]} C{c1[0]} {c1[1]} {c2[0]} {c2[1]} {p3[0]} {p3[1]} H{x1}"
    curve = _w15_cubic_len(p0, c1, c2, p3)
    fc = curve / (curve + x1 - x0)
    lap_d = f"M{cx + r} {cy} A{r} {r} 0 1 1 {cx + r} {cy - .01}"
    pillars = list(sl.get("bridge") or LX_PILLARS)
    step = (x1 - x0) / (len(pillars) + 1)
    light = [t_deck + (t_in - t_deck) * step * (k + 1) / (x1 - x0) for k in range(len(pillars))]
    to = sl.get("to", "Operación")
    # the loop, then its magenta lap underneath (the ring paints over it); both quiet down once the spark has left
    quiet = lambda lo: beat("opacity", [(0, 1), (t_brk + .02, 1), (t_brk + .1, lo), (.96, lo), (.99, 1), (1, 1)])
    lap = (f'<g>{quiet(.35)}' + _w15_run(lap_d, t_lap0, t_brk, 10, 'opacity=".16"') + _w15_run(lap_d, t_lap0, t_brk, 2.2)
           + '</g>')
    loop_ = (f'<g>{quiet(.72)}' + lx_loop(cx, cy, r, stops=sl.get("stops") or ("Idea", "POC", "Demo"), gate=False, size=18)
             + lx_label(cx, cy + 7, sl.get("from", "Piloto"), 20, 2 * r - 50, "w15 from", "var(--muted)", "middle") + '</g>')
    bridge = lx_bridge(x0, x1, by, pillars, "", "", light_at=light, h=110, size=16)
    # the escape: halo, glow and core strokes, the comet and the rider; the flash where it breaks out
    show = [(0, 0), (t_brk - .005, 0), (t_brk, 1), (t_in, 1), (t_in + .02, 0), (1, 0)]
    stops = [(0, 0), (t_brk, 0), (t_deck, fc), (t_in, 1), (1, 1)]
    breakout = (_w15_burst(*p0, t_brk, 8, 48, .09) + _w15_burst(*p0, t_brk + .01, 8, 70, .11, LX_MAGENTA, 1.4)
                + _w15_rays(*p0, t_brk))
    # the escape draws at the rider's pace: the swoop fast, the deck slower
    pace = beat("stroke-dashoffset", [(0, 1), (t_brk, 1), (t_deck, round(1 - fc, 4)), (t_in, 0), (.97, 0), (.985, 1), (1, 1)])
    escape = "".join(
        f'<path d="{out}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{LX_MAGENTA}" stroke-width="{wd}" '
        f'stroke-linecap="round" opacity="{op}">{pace}</path>' for wd, op in ((12, .12), (5, .3), (2.4, 1)))
    comet = (_w15_comet(out, stops, show, .12, 10, .26) + _w15_comet(out, stops, show, .055, 4, .9))
    sparks = "".join(_w15_burst(x0 + step * (k + 1), by, a, 4, 24, .06) for k, a in enumerate(light))
    rider = _w13_rider(out, stops, show, .95)
    # the landing on «Operación»: bursts, rays, a gold node with a heartbeat; its label white before, gold after
    lit = (f'<g>{lx_lit(t_in)}<g>{loop("opacity", ".55;1;.55", 3)}{glow(x1, by + 20, 48, LX_GOLD, .65)}</g>'
           f'<circle cx="{x1}" cy="{by}" r="10" fill="{LX_GOLD}"/>'
           f'<circle cx="{x1}" cy="{by}" r="18" fill="none" stroke="{LX_GOLD}" stroke-width="1.6"/>'
           f'<circle cx="{x1}" cy="{by}" r="26" fill="none" stroke="{LX_GOLD}" stroke-width="1" opacity=".45"/></g>')
    landing = (_w15_burst(x1, by, t_in, 10, 58, .1) + _w15_burst(x1, by, t_in + .02, 10, 92, .14, LX_GOLD, 1.2)
               + _w15_rays(x1, by, t_in, 10))
    to_labels = (f'<g>{beat("opacity", [(0, 1), (t_in, 1), (t_in + .02, 0), (.97, 0), (.99, 1), (1, 1)])}'
                 + lx_label(x1, by - 30, to, 20, 200, "w15 to", "var(--white)", "middle") + '</g>'
                 + f'<g>{lx_lit(t_in)}' + lx_label(x1, by - 30, to, 20, 200, "w15 to", LX_GOLD, "middle") + '</g>')
    signer = lx_signer(1110, 500, 160, sl.get("name", ""), sl.get("role", ""))
    sign = (f'<g>{lx_lit(t_in + .05)}'
            + lx_label(1504, 806, sl.get("sign", ""), 17, 440, "w15 sign", "var(--muted)", "end") + '</g>')
    art = (land(lap + loop_, .1, .5, 0) + land(bridge, .3, .5, 12) + escape + comet + sparks + breakout + rider + lit + landing
           + to_labels + land(signer, .5, .6, 18) + sign)
    depth = lx_depth(LX_ZONE["left"], n=38, seed="x15", labels=art, avoid=[(1086, 476, 208, 208)])
    g = [depth, glow(1190, 440, 520, "var(--brand)", .45), lx_drift(art, 1190, 455, 1.012, 0, -5)]
    return "".join(g), D, FREEZE

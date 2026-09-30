"""Group B · slides 4, 5 and 6 of the energía deck: the problem, the shared asset, the urgency. Each scene tells one
12-second story with beat() and freezes (reduced motion, 0.9 of the loop) on the resolved frame.

- m04_tesis: a small deviation on the compressor goes unseen; days later it cascades into urgency, an emergency
  purchase and a stop. Frozen: the whole cascade lit, the line halted.
- m05_lineas: one data event on the shared asset travels to the four business lines and closes a ring between them.
  Frozen: the four lines lit by the same datum, joined.
- m06_sector: the gas supply thins, demand pressure rises, then a stop drains what is left. The figure never moves.
  Frozen: thin supply, the stop, demand in the red.

Runs inside the shared ext namespace (the energía deck's module/ext.py): helpers come from module/ext.py.
Portrait-aware (0.5.0): under ORIENT() == "portrait" each scene hands over to its _p0N_* twin (same loop, same frozen
frame, labels of 20 px or more, painted last); the desktop output stays byte-identical.
"""


_n04_end = .98   # every resolved state holds until here, then the loop resets in a quarter second


def _n04_win(a, b=_n04_end, lo=0, hi=1, f=.02):
    """beat() pairs: lo until a, hi from a + f until b, back to lo by the end of the loop."""
    pts = [(0, lo), (a, lo), (a + f, hi), (b, hi)]
    return pts + [(1, lo)] if b + f >= 1 else pts + [(b + f, lo), (1, lo)]


def _n04_trip(a, b):
    """beat() pairs: visible only while travelling from a to b."""
    return [(0, 0), (a, 0), (a + .005, 1), (b, 1), (b + .01, 0), (1, 0)]


def _n04_ping(x, y, r0, r1, col, times, span=.1, op=.8):
    """Rings that open once at each time in `times` and fade (invisible in the frozen frame)."""
    out = []
    for a in times:
        out.append(f'<circle cx="{x}" cy="{y}" r="{r0}" fill="none" stroke="{col}" stroke-width="1.5" opacity="0">'
                   f'{beat("r", [(0, r0), (a, r0), (a + span, r1), (1, r1)])}'
                   f'{beat("opacity", [(0, 0), (a, 0), (a + .005, op), (a + span, 0), (1, 0)])}</circle>')
    return "".join(out)


def _n04_icon(kind, col):
    """Line icons around 0,0: 0 clock (urgency), 1 cart (emergency purchase), 2 octagon (stop)."""
    s = f'fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
    if kind == 0:
        return f'<circle r="11" {s}/><path d="M0 -6 V0 L5 3" {s}/>'
    if kind == 1:
        return (f'<path d="M-13 -9 H-8 L-4 5 H9 L12 -5 H-6" {s}/>'
                f'<circle cx="-2" cy="10" r="2" fill="{col}"/><circle cx="7" cy="10" r="2" fill="{col}"/>')
    pts = " ".join(f"{12 * math.cos(math.radians(22.5 + 45 * k)):.1f},{12 * math.sin(math.radians(22.5 + 45 * k)):.1f}" for k in range(8))
    return f'<polygon points="{pts}" {s}/><path d="M-6 0 H6" {s}/>'


def _n04_shake(t, amp=4):
    """A short sideways jolt at t (fraction of the loop), then still."""
    kt = [0, t, t + .01, t + .02, t + .03, t + .04, 1]
    vals = ["0 0", "0 0", f"{-amp} 0", f"{amp} 0", f"{-amp / 2} 0", "0 0", "0 0"]
    return (f'<animateTransform attributeName="transform" type="translate" values="{";".join(vals)}" '
            f'keyTimes="{";".join(f"{k:.3f}" for k in kt)}" dur="{D}s" repeatCount="indefinite"/>')


# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
def _p04_tesis(sl, ctx):
    """m04 on the 900x1600 stage: the line with its four stations across the top of the art zone, the unseen deviation
    over the compressor, and the cascade stepping down the zone, each step wider and hotter. Same loop and frozen
    frame; labels painted after all the art."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    y, xs = zy + 130, tuple(zx + 90 + k * 200 for k in range(4))
    x0, x1 = zx + 30, zx + zw - 30
    halt = .61
    art, text = [glow(zx + zw / 2, zy + zh * .5, 440, "var(--brand)", .45)], []
    line = (f'<path d="M{x0} {y} H{x1}" stroke="var(--line)" stroke-width="16" stroke-linecap="round"/>'
            f'<path d="M{x0} {y} H{x1}" stroke="var(--c5)" stroke-width="16" stroke-linecap="round" opacity="0">{beat("opacity", _n04_win(halt, hi=.4))}</path>'
            f'<g>{beat("opacity", _n04_win(halt, lo=1, hi=0))}<path d="M{x0} {y} H{x1}" fill="none" stroke="var(--c4)" stroke-width="4" '
            f'stroke-dasharray="8 18">{loop("stroke-dashoffset", "0;-52", 1.6)}</path></g>')
    art.append(land(line, .1, .5, 0))
    for k, (x, name) in enumerate(zip(xs, sl["stations"])):
        art.append(pop(card(-46, -46, 92, 92, "var(--card)", "var(--c2)", 18, 1.6) + '<circle r="16" fill="var(--c1)"/>'
                       + f'<circle r="16" fill="var(--dim)" opacity="0">{beat("opacity", _n04_win(halt + k * .015))}</circle>', x, y, .25 + k * .1, .45))
        text.append(pop(TC(0, 84, name, fit(name, 22, 190, "station", floor=18), "var(--muted)", W6), x, y, .25 + k * .1, .45))
    # the small deviation: it sparks, pings twice and nobody answers
    sx, sy = xs[1], y - 88
    art.append(f'<g opacity="0">{beat("opacity", _n04_win(.06))}<g>{loop("opacity", ".5;1;.5", 1.8)}{spark(sx, sy, .95, "var(--c5)")}</g></g>'
               + _n04_ping(sx, sy, 15, 58, "var(--c5)", (.08, .16)))
    text.append(f'<g opacity="0">{beat("opacity", _n04_win(.06))}'
                + T(sx + 32, sy + 8, sl["small"], fit(sl["small"], 22, x1 - sx - 40, "unseen deviation", floor=18), "var(--muted)", W6) + '</g>')
    # the cascade, days later: each step bigger and hotter than the last
    cols = ("var(--c3)", "var(--accent)", "var(--c5)")
    boxes = ((zx + 30, y + 190, 470, 116), (zx + 150, y + 360, 540, 116), (zx + zw - 624, y + 530, 600, 160))
    trips = ((.22, .36), (.40, .49), (.52, halt))
    mids = [bx + bw / 2 for bx, _y, bw, _h in boxes]
    paths = [f"M{sx} {y + 108} C{sx} {y + 150} {mids[0]} {y + 150} {mids[0]} {boxes[0][1]}"]
    for (bx, by, bw, bh), m in zip(boxes[:2], mids[1:]):
        paths.append(f"M{bx + bw / 2} {by + bh} C{bx + bw / 2} {by + bh + 30} {m} {by + bh + 24} {m} {by + bh + 54}")
    text.append(land(T(sx + 24, y + 152, sl["gap"], fit(sl["gap"], 21, 300, "cascade gap", floor=18), "var(--muted)", W6), 1.0, .45, 0))
    bx2, by2, bw2, bh2 = boxes[2]
    art.append(f'<g opacity="0">{beat("opacity", _n04_win(halt))}{glow(bx2 + bw2 / 2, by2 + bh2 / 2, 320, "var(--c5)", .5)}</g>')
    for k, ((x, yy, w, h), col, label, (a, b), d) in enumerate(zip(boxes, cols, sl["cascade"], trips, paths)):
        wire = (f'<path d="{d}" fill="none" stroke="var(--line)" stroke-width="2.4" stroke-dasharray="4 6"/>'
                f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{col}" stroke-width="2.4">'
                f'{beat("stroke-dashoffset", [(0, 1), (a, 1), (b, 0), (_n04_end, 0), (1, 1)])}</path>')
        s = fit(label, 36 if k == 2 else 27, w - 140, "cascade step", floor=18)
        cy_ = yy + h / 2
        step = (card(x, yy, w, h, "var(--dim)", "var(--line)", 18, 1.6)
                + f'<g opacity="0">{beat("opacity", _n04_win(b))}{card(x, yy, w, h, f"color-mix(in srgb, {col} {40 if k == 2 else 22}%, var(--card))", col, 18, 3.4 if k == 2 else 2.8)}'
                + (f'<rect x="{x - 7}" y="{yy - 7}" width="{w + 14}" height="{h + 14}" rx="24" fill="none" stroke="{col}" stroke-width="1.8">{loop("stroke-opacity", ".15;.8;.15", 2.4)}</rect>' if k == 2 else "") + '</g>'
                + f'<g opacity=".5">{beat("opacity", _n04_win(b, lo=.5))}'
                + f'<g transform="translate({x + 60} {cy_})"><circle r="31" fill="none" stroke="{col}" stroke-width="2.4"/><g transform="scale(1.3)">{_n04_icon(k, col)}</g></g></g>')
        lab = (f'<g opacity=".5">{beat("opacity", _n04_win(b, lo=.5))}'
               + T(x + 110, f"{cy_ + s * .36:.1f}", label, s, "var(--white)", W6) + '</g>')
        if k == 2:
            step, lab = f'<g>{_n04_shake(b, 5)}{step}</g>', f'<g>{_n04_shake(b, 5)}{lab}</g>'
        tok = f'<g opacity="0">{beat("opacity", _n04_trip(a, b))}{move(d, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{token(col, 7 + 2 * k)}</g>'
        art.append(land(wire, .6 + k * .12, .4, 0) + land(step, .7 + k * .15, .45, 14) + tok)
        text.append(land(lab, .7 + k * .15, .45, 14))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "m04_tesis")
def sc_m04_tesis(sl, ctx):
    """The opposite of slide 3: nobody sees the small deviation on the compressor. Days later it turns into an urgency,
    then an emergency purchase, then a stop; the line halts. The frozen frame is the cost of reacting late."""
    if ORIENT() == "portrait":
        return _p04_tesis(sl, ctx)
    y, xs = 190, (900, 1100, 1300, 1480)
    halt = .61                                   # the stop: the cascade's last step lands, the gas stops
    g = [glow(1190, 470, 440, "var(--brand)", .45)]
    line = (f'<path d="M850 {y} H1530" stroke="var(--line)" stroke-width="14" stroke-linecap="round"/>'
            f'<path d="M850 {y} H1530" stroke="var(--c5)" stroke-width="14" stroke-linecap="round" opacity="0">{beat("opacity", _n04_win(halt, hi=.4))}</path>'
            f'<g>{beat("opacity", _n04_win(halt, lo=1, hi=0))}<path d="M850 {y} H1530" fill="none" stroke="var(--c4)" stroke-width="3.5" '
            f'stroke-dasharray="8 18">{loop("stroke-dashoffset", "0;-52", 1.6)}</path></g>')
    g.append(land(line, .1, .5, 0))
    for k, (x, name) in enumerate(zip(xs, sl["stations"])):
        st = (card(-38, -38, 76, 76, "var(--card)", "var(--c2)", 16, 1.5) + '<circle r="13" fill="var(--c1)"/>'
              + f'<circle r="13" fill="var(--dim)" opacity="0">{beat("opacity", _n04_win(halt + k * .015))}</circle>'
              + TC(0, 64, name, fit(name, 16, 150, "station"), "var(--muted)", W6))
        g.append(pop(st, x, y, .25 + k * .1, .45))
    # the small deviation: it sparks, pings twice and nobody answers
    sx, sy = xs[1], y - 66
    g.append(f'<g opacity="0">{beat("opacity", _n04_win(.06))}<g>{loop("opacity", ".5;1;.5", 1.8)}{spark(sx, sy, .75, "var(--c5)")}</g>'
             + T(sx + 26, sy + 6, sl["small"], fit(sl["small"], 15, 200, "unseen deviation"), "var(--muted)", W6) + '</g>'
             + _n04_ping(sx, sy, 12, 46, "var(--c5)", (.08, .16)))
    # the cascade, days later: each step bigger and hotter than the last
    cols = ("var(--c3)", "var(--accent)", "var(--c5)")
    boxes = ((860, 360, 300, 84), (1030, 505, 330, 84), (1195, 650, 355, 112))
    trips = ((.22, .36), (.40, .49), (.52, halt))
    paths = (f"M{sx} {y + 76} C{sx} {y + 124} 1010 {y + 124} 1010 360",
             "M1110 444 C1110 478 1195 472 1195 505",
             "M1290 589 C1290 622 1372 616 1372 650")
    g.append(land(T(sx + 20, y + 132, sl["gap"], fit(sl["gap"], 15, 170, "cascade gap"), "var(--muted)", W6), 1.0, .45, 0))
    g.append(f'<g opacity="0">{beat("opacity", _n04_win(halt))}{glow(1372, 706, 260, "var(--c5)", .5)}</g>')
    for k, ((x, yy, w, h), col, label, (a, b), d) in enumerate(zip(boxes, cols, sl["cascade"], trips, paths)):
        wire = (f'<path d="{d}" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 6"/>'
                f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{col}" stroke-width="2">'
                f'{beat("stroke-dashoffset", [(0, 1), (a, 1), (b, 0), (_n04_end, 0), (1, 1)])}</path>')
        s = fit(label, 28 if k == 2 else 21, w - 110, "cascade step")
        cy_ = yy + h / 2
        step = (card(x, yy, w, h, "var(--dim)", "var(--line)", 16, 1.5)
                + f'<g opacity="0">{beat("opacity", _n04_win(b))}{card(x, yy, w, h, f"color-mix(in srgb, {col} {40 if k == 2 else 22}%, var(--card))", col, 16, 3 if k == 2 else 2.5)}'
                + (f'<rect x="{x - 6}" y="{yy - 6}" width="{w + 12}" height="{h + 12}" rx="21" fill="none" stroke="{col}" stroke-width="1.5">{loop("stroke-opacity", ".15;.8;.15", 2.4)}</rect>' if k == 2 else "") + '</g>'
                + f'<g opacity=".5">{beat("opacity", _n04_win(b, lo=.5))}'
                + f'<g transform="translate({x + 46} {cy_})"><circle r="24" fill="none" stroke="{col}" stroke-width="2"/>{_n04_icon(k, col)}</g>'
                + T(x + 86, f"{cy_ + s * .36:.1f}", label, s, "var(--white)", W6) + '</g>')
        if k == 2:
            step = f'<g>{_n04_shake(b)}{step}</g>'
        tok = f'<g opacity="0">{beat("opacity", _n04_trip(a, b))}{move(d, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{token(col, 5 + 2 * k)}</g>'
        g.append(land(wire, .6 + k * .12, .4, 0) + land(step, .7 + k * .15, .45, 14) + tok)
    return "".join(g), D, FREEZE


def _p05_lineas(sl, ctx):
    """m05 on the 900x1600 stage: the asset in the middle of the art zone, the four lines in a 2x2 grid around it (same
    reading order), the ring through their centres. Same loop and frozen frame; labels painted after all the art."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    cx, cy = zx + zw / 2, zy + zh / 2
    dx, dy = 205, 300
    pos = ((cx - dx, cy - dy), (cx + dx, cy - dy), (cx - dx, cy + dy), (cx + dx, cy + dy))
    cols = ("var(--c1)", "var(--accent)", "var(--c2)", "var(--c3)")
    ev, out, hit, close = .08, .11, .27, (.34, .54)
    rx, ry = round(dx * math.sqrt(2)), round(dy * math.sqrt(2))
    ring = f"M{cx} {cy - ry} A{rx} {ry} 0 1 1 {cx - .01} {cy - ry} Z"   # through the four node centers
    HR, NW, NH = 120, 360, 124
    art, text = [glow(cx, cy, 440, "var(--brand)", .5)], []
    art.append(f'<path d="{ring}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="2.2" opacity=".85">'
               f'{beat("stroke-dashoffset", [(0, 1), (close[0], 1), (close[1], 0), (_n04_end, 0), (1, 1)])}</path>'
               f'<g opacity="0">{beat("opacity", _n04_win(close[1]))}{move(ring, [(0, 0), (close[1], 0), (_n04_end, 1), (1, 1)], D)}{token("var(--c4)", 6)}</g>')
    pipes, toks = [], []
    for k, (x, y) in enumerate(pos):
        d = f"M{cx} {cy} L{x} {y}"
        pipes.append(f'<path d="{d}" stroke="var(--line)" stroke-width="10" stroke-linecap="round"/>'
                     f'<path d="{d}" fill="none" stroke="var(--c4)" stroke-width="2.5" stroke-dasharray="4 14" opacity=".45">{loop("stroke-dashoffset", "0;-36", 2.4)}</path>')
        a, b = out + k * .012, hit + k * .012
        toks.append(f'<g opacity="0">{beat("opacity", _n04_trip(a, b))}{move(d, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{token("var(--c4)", 9)}</g>')
    art.append(land("".join(pipes), .1, .5, 0) + "".join(toks))
    trace_d = "M-58 -34 L-42 -36 L-28 -32 L-16 -36 L-7 -33 L0 -50 L7 -31 L17 -35 L30 -33 L44 -36 L58 -34"
    hub = (f'<circle r="{HR}" fill="var(--card)" stroke="var(--c4)" stroke-width="3"/>'
           f'<g transform="scale(1.3)"><path d="{trace_d}" fill="none" stroke="var(--c2)" stroke-width="1.8" stroke-linejoin="round"/>'
           f'<g opacity="0">{beat("opacity", _n04_win(ev))}{spark(0, -50, .5, "var(--c4)")}</g></g>')
    art.append(pop(hub, cx, cy, .25, .5))
    art.append(_n04_ping(cx, cy - 65, 10, 52, "var(--c4)", (ev,), .08) + _n04_ping(cx, cy, HR, HR + 60, "var(--c4)", (close[1],), .12, .7))
    text.append(pop(TCW(0, 20, sl["center"], 12, 25, "var(--white)", W6, 1.25), cx, cy, .25, .5))
    ey = cy - dy + NH / 2 + 68
    art.append(f'<g opacity="0">{beat("opacity", _n04_win(ev))}<path d="M{cx} {cy - 82} V{ey + 18}" stroke="var(--c4)" stroke-width="2"/>'
               + pill(cx, ey, sl["event"], "var(--dim)", ctx, 20, 300, "shared data event") + '</g>')
    for k, ((x, y), col, (name, sub)) in enumerate(zip(pos, cols, sl["lines"])):
        t = hit + k * .012
        node = (card(-NW / 2, -NH / 2, NW, NH, "var(--card)", col, 18, 2.4)
                + f'<g opacity="0">{beat("opacity", _n04_win(t))}'
                f'<rect x="{-NW / 2 - 8}" y="{-NH / 2 - 8}" width="{NW + 16}" height="{NH + 16}" rx="24" fill="none" stroke="var(--c4)" stroke-width="2.4"/>'
                f'<rect x="{NW / 2 - 28}" y="{-NH / 2 + 12}" width="14" height="14" rx="2" transform="rotate(45 {NW / 2 - 21} {-NH / 2 + 19})" fill="var(--c4)"/></g>')
        art.append(pop(node, x, y, .45 + k * .12, .45))
        text.append(pop(TC(0, -8, name, fit(name, 26, NW - 60, "business line", floor=18), "var(--white)", W6)
                        + TC(0, 32, sub, fit(sub, 21, NW - 40, "business line detail", floor=18), "var(--muted)", W6), x, y, .45 + k * .12, .45))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "m05_lineas")
def sc_m05_lineas(sl, ctx):
    """One data event on the shared asset (a vibration on the compressor) reaches the four business lines at once, and
    a ring closes between them: the same datum serves all four. The frozen frame keeps the four lit and joined."""
    if ORIENT() == "portrait":
        return _p05_lineas(sl, ctx)
    cx, cy = 1195, 455
    pos = ((965, 265), (1425, 265), (965, 645), (1425, 645))       # O&M, supply chain, representaciones, GLP: reading order
    cols = ("var(--c1)", "var(--accent)", "var(--c2)", "var(--c3)")
    ev, out, hit, close = .08, .11, .27, (.34, .54)
    ring = f"M{cx} {cy - 269} A325 269 0 1 1 {cx - .01} {cy - 269} Z"   # through the four node centers
    g = [glow(cx, cy, 440, "var(--brand)", .5)]
    # the ring the datum closes between the four lines, and the datum that keeps going round
    g.append(f'<path d="{ring}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity=".85">'
             f'{beat("stroke-dashoffset", [(0, 1), (close[0], 1), (close[1], 0), (_n04_end, 0), (1, 1)])}</path>'
             f'<g opacity="0">{beat("opacity", _n04_win(close[1]))}{move(ring, [(0, 0), (close[1], 0), (_n04_end, 1), (1, 1)], D)}{token("var(--c4)", 5)}</g>')
    pipes, toks = [], []
    for k, (x, y) in enumerate(pos):
        d = f"M{cx} {cy} L{x} {y}"
        pipes.append(f'<path d="{d}" stroke="var(--line)" stroke-width="8" stroke-linecap="round"/>'
                     f'<path d="{d}" fill="none" stroke="var(--c4)" stroke-width="2" stroke-dasharray="4 14" opacity=".45">{loop("stroke-dashoffset", "0;-36", 2.4)}</path>')
        a, b = out + k * .012, hit + k * .012
        toks.append(f'<g opacity="0">{beat("opacity", _n04_trip(a, b))}{move(d, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{token("var(--c4)", 7)}</g>')
    g.append(land("".join(pipes), .1, .5, 0) + "".join(toks))
    # the asset: a live trace that spikes once (the event), then pings when the ring closes
    trace_d = "M-58 -34 L-42 -36 L-28 -32 L-16 -36 L-7 -33 L0 -50 L7 -31 L17 -35 L30 -33 L44 -36 L58 -34"
    hub = (f'<circle r="92" fill="var(--card)" stroke="var(--c4)" stroke-width="2.5"/>'
           f'<path d="{trace_d}" fill="none" stroke="var(--c2)" stroke-width="1.8" stroke-linejoin="round"/>'
           f'<g opacity="0">{beat("opacity", _n04_win(ev))}{spark(0, -50, .5, "var(--c4)")}</g>'
           + TCW(0, 12, sl["center"], 12, 19, "var(--white)", W6, 1.25))
    g.append(pop(hub, cx, cy, .25, .5))
    g.append(_n04_ping(cx, cy - 50, 8, 40, "var(--c4)", (ev,), .08) + _n04_ping(cx, cy, 92, 140, "var(--c4)", (close[1],), .12, .7))
    ex, ey = cx, 322
    g.append(f'<g opacity="0">{beat("opacity", _n04_win(ev))}<path d="M{cx} {cy - 62} V{ey + 14}" stroke="var(--c4)" stroke-width="1.5"/>'
             + pill(ex, ey, sl["event"], "var(--dim)", ctx, 15, 200, "shared data event") + '</g>')
    for k, ((x, y), col, (name, sub)) in enumerate(zip(pos, cols, sl["lines"])):
        t = hit + k * .012
        node = (card(-120, -46, 240, 92, "var(--card)", col, 16, 2)
                + f'<g opacity="0">{beat("opacity", _n04_win(t))}'
                f'<rect x="-127" y="-53" width="254" height="106" rx="21" fill="none" stroke="var(--c4)" stroke-width="2"/>'
                f'<rect x="97" y="-38" width="12" height="12" rx="2" transform="rotate(45 103 -32)" fill="var(--c4)"/></g>'
                + TC(0, -6, name, fit(name, 19, 196, "business line"), "var(--white)", W6)
                + TC(0, 24, sub, fit(sub, 15, 208, "business line detail"), "var(--muted)", W6))
        g.append(pop(node, x, y, .45 + k * .12, .45))
    return "".join(g), D, FREEZE


def _p06_sector(sl, ctx):
    """m06 on the 900x1600 stage: the figure framed on top, the supply line under it across the zone (production, the
    gas band, the compressor, demand and its gauge). Same loop and frozen frame; the figure never moves; labels painted
    after all the art."""
    thin, halt = (.06, .34), .52
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    fx, (bx, by, bw, bh) = zx + zw / 2, (zx + 50, zy + 26, zw - 100, 400)
    art, text = [glow(fx, zy + zh * .45, 440, "var(--brand)", .45)], []
    hud = "".join(f'<path d="M{x0} {y0 + dy * 26} V{y0} H{x0 + dx * 26}" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity=".8"/>'
                  for x0, y0, dx, dy in ((bx, by, 1, 1), (bx + bw, by, -1, 1), (bx, by + bh, 1, -1), (bx + bw, by + bh, -1, -1)))
    fig = TC(fx, by + 215, sl["figure"], fit(sl["figure"], 150, bw - 80, "sector figure"), "var(--c4)", W6)
    lab = TCW(fx, by + 285, sl["label"], 30, 30, "var(--white)", W6, 1.25)
    art.append(land(hud, .1, .5, 0))
    text.append(land(fig + lab, .2, .5, 0))
    py, x0, x1, sx = zy + 690, zx + 130, zx + zw - 130, fx + 80
    w0 = 72
    w1 = round(w0 * .7, 1)   # −30 %: the band keeps the figure's proportion
    width = beat("stroke-width", [(0, w0), (thin[0], w0), (thin[1], w1), (_n04_end, w1), (1, w0)])
    amber = "color-mix(in srgb, var(--c4) 58%, var(--dim))"
    band = lambda a, b: (f'<path d="M{a} {py} H{b}" stroke="{amber}" stroke-width="{w1}" stroke-linecap="round">{width}</path>'
                         f'<path d="M{a} {py} H{b}" fill="none" stroke="var(--white)" stroke-opacity=".7" stroke-width="2.4" stroke-dasharray="6 14">{loop("stroke-dashoffset", "0;-40", 1.4)}</path>')
    was = "".join(f'<path d="M{x0 + 36} {py + k * w0 / 2} H{x1 - 36}" stroke="var(--c4)" stroke-width="1.6" stroke-dasharray="4 4" opacity=".9"/>' for k in (-1, 1))
    art.append(land(card(x0, py - 44, x1 - x0, 88, "var(--dim)", "var(--line)", 44, 1.6) + band(x0 + 36, sx)
                    + f'<g>{beat("opacity", [(0, 1), (halt, 1), (halt + .06, .12), (_n04_end, .12), (1, 1)])}{band(sx, x1 - 36)}</g>' + was, .45, .5, 0))
    rx, dx = zx + 60, zx + zw - 72
    rig = ('<g transform="scale(1.3)"><path d="M-16 28 L0 -30 L16 28 M-11 8 H11 M-6 -12 H6 M-26 28 H26" fill="none" stroke="var(--c2)" '
           'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>')
    plant_d = "M-32 28 V-4 L-18 -16 V-4 L-4 -16 V-4 L10 -16 V-30 H22 V28 Z"
    plant = (f'<g transform="scale(1.3)"><path d="{plant_d}" fill="var(--card)" stroke="var(--c2)" stroke-width="2" stroke-linejoin="round"/>'
             f'<path d="{plant_d}" fill="none" stroke="var(--c5)" stroke-width="2.5" stroke-linejoin="round" opacity="0">{beat("opacity", _n04_win(halt + .04))}</path></g>')
    art.append(pop(rig, rx, py - 4, .7, .45) + pop(plant, dx, py - 4, .85, .45) + _n04_ping(dx, py - 140, 60, 104, "var(--c3)", (.30, .38, .46), .1, .7))
    text.append(land(TC(rx, py + 80, sl["supply"], fit(sl["supply"], 21, 150, "sector supply", floor=18), "var(--muted)", W6)
                     + TC(dx, py + 80, sl["demand"], fit(sl["demand"], 21, 150, "sector demand", floor=18), "var(--muted)", W6), .85, .45, 0))
    angs = [(0, -70), (thin[0], -70), (thin[1], 12), (halt, 22), (halt + .05, 62), (_n04_end, 62), (1, -70)]
    needle = (f'<g><animateTransform attributeName="transform" type="rotate" values="{";".join(f"{v} 0 0" for _, v in angs)}" '
              f'keyTimes="{";".join(f"{t:.3f}" for t, _ in angs)}" dur="{D}s" repeatCount="indefinite"/>'
              f'<path d="M0 0 L0 -32" stroke="var(--white)" stroke-width="2.5" stroke-linecap="round"/></g>')
    ticks = "".join(f'<path d="M{48 * math.sin(math.radians(a)):.1f} {-48 * math.cos(math.radians(a)):.1f} L{53 * math.sin(math.radians(a)):.1f} {-53 * math.cos(math.radians(a)):.1f}" stroke="var(--c2)" stroke-width="1.5" opacity=".7"/>'
                    for a in range(-90, 91, 30))
    gauge = ('<g transform="scale(1.3)"><path d="M-40 0 A40 40 0 0 1 40 0" fill="none" stroke="var(--line)" stroke-width="6" stroke-linecap="round"/>'
             '<path d="M22.9 -32.8 A40 40 0 0 1 40 0" fill="none" stroke="var(--c5)" stroke-width="6" stroke-linecap="round"/>'
             + ticks + needle + '<circle r="5" fill="var(--white)"/></g>')
    art.append(pop(gauge, dx, py - 140, 1.0, .45))
    art.append(f'<g opacity="0">{beat("opacity", _n04_win(halt))}{glow(sx, py, 170, "var(--c5)", .35)}</g>')
    art.append(pop(card(-44, -44, 88, 88, "var(--card)", "var(--c2)", 20, 1.8) + '<circle r="13" fill="var(--c1)"/>'
                   + f'<g opacity="0">{beat("opacity", _n04_win(halt))}<circle r="16" fill="var(--c5)"/></g>', sx, py, .75, .45)
               + _n04_ping(sx, py, 36, 190, "var(--c5)", (halt, halt + .14), .14, .7))
    text.append(pop(TC(0, 80, sl["station"], fit(sl["station"], 21, 170, "sector station", floor=18), "var(--muted)", W6), sx, py, .75, .45))
    text.append(f'<g opacity="0">{beat("opacity", _n04_win(halt))}{pill(sx, py - 104, sl["chip"], "var(--c5)", ctx, 22, 240, "sector stop")}</g>')
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "m06_sector")
def sc_m06_sector(sl, ctx):
    """The figure stays still, framed like an instrument. Around it the context moves: the gas band thins to seven tenths
    of its width (the figure's own proportion), the demand gauge climbs, then the compressor stops and the little
    supply left downstream drains. The frozen frame: thin supply, the stop, demand in the red."""
    if ORIENT() == "portrait":
        return _p06_sector(sl, ctx)
    thin, halt = (.06, .34), .52
    fx, (bx, by, bw, bh) = 1190, (900, 120, 580, 300)
    g = [glow(1190, 440, 440, "var(--brand)", .45)]
    hud = "".join(f'<path d="M{x0} {y0 + dy * 22} V{y0} H{x0 + dx * 22}" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity=".8"/>'
                  for x0, y0, dx, dy in ((bx, by, 1, 1), (bx + bw, by, -1, 1), (bx, by + bh, 1, -1), (bx + bw, by + bh, -1, -1)))
    fig = TC(fx, by + 170, sl["figure"], fit(sl["figure"], 120, bw - 60, "sector figure"), "var(--c4)", W6)
    lab = TCW(fx, by + 226, sl["label"], 34, 24, "var(--white)", W6, 1.25)
    g.append(land(hud, .1, .5, 0) + land(fig + lab, .2, .5, 0))
    # the supply line: production, the gas band inside its pipe, the compressor, demand
    py, x0, x1, sx = 640, 960, 1390, 1235
    w0 = 56
    w1 = round(w0 * .7, 1)   # −30 %: the band keeps the figure's proportion
    width = beat("stroke-width", [(0, w0), (thin[0], w0), (thin[1], w1), (_n04_end, w1), (1, w0)])
    amber = "color-mix(in srgb, var(--c4) 58%, var(--dim))"
    band = lambda a, b: (f'<path d="M{a} {py} H{b}" stroke="{amber}" stroke-width="{w1}" stroke-linecap="round">{width}</path>'
                         f'<path d="M{a} {py} H{b}" fill="none" stroke="var(--white)" stroke-opacity=".7" stroke-width="2" stroke-dasharray="6 14">{loop("stroke-dashoffset", "0;-40", 1.4)}</path>')
    was = "".join(f'<path d="M{x0 + 28} {py + k * w0 / 2} H{x1 - 28}" stroke="var(--c4)" stroke-width="1.4" stroke-dasharray="4 4" opacity=".9"/>' for k in (-1, 1))
    pipe = (card(x0, py - 34, x1 - x0, 68, "var(--dim)", "var(--line)", 34, 1.5) + band(x0 + 28, sx)
            + f'<g>{beat("opacity", [(0, 1), (halt, 1), (halt + .06, .12), (_n04_end, .12), (1, 1)])}{band(sx, x1 - 28)}</g>' + was)
    g.append(land(pipe, .45, .5, 0))
    rig = (f'<path d="M-16 28 L0 -30 L16 28 M-11 8 H11 M-6 -12 H6 M-26 28 H26" fill="none" stroke="var(--c2)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
           + TC(0, 58, sl["supply"], fit(sl["supply"], 15, 110, "sector supply"), "var(--muted)", W6))
    plant_d = "M-32 28 V-4 L-18 -16 V-4 L-4 -16 V-4 L10 -16 V-30 H22 V28 Z"
    plant = (f'<path d="{plant_d}" fill="var(--card)" stroke="var(--c2)" stroke-width="2" stroke-linejoin="round"/>'
             f'<path d="{plant_d}" fill="none" stroke="var(--c5)" stroke-width="2.5" stroke-linejoin="round" opacity="0">{beat("opacity", _n04_win(halt + .04))}</path>'
             + TC(0, 58, sl["demand"], fit(sl["demand"], 15, 120, "sector demand"), "var(--muted)", W6))
    g.append(pop(rig, 905, py - 4, .7, .45) + pop(plant, 1462, py - 4, .85, .45)
             + _n04_ping(1462, py - 100, 46, 82, "var(--c3)", (.30, .38, .46), .1, .7))
    # demand pressure: the gauge climbs while the supply thins, and tips into the red at the stop
    angs = [(0, -70), (thin[0], -70), (thin[1], 12), (halt, 22), (halt + .05, 62), (_n04_end, 62), (1, -70)]
    needle = (f'<g><animateTransform attributeName="transform" type="rotate" values="{";".join(f"{v} 0 0" for _, v in angs)}" '
              f'keyTimes="{";".join(f"{t:.3f}" for t, _ in angs)}" dur="{D}s" repeatCount="indefinite"/>'
              f'<path d="M0 0 L0 -32" stroke="var(--white)" stroke-width="2.5" stroke-linecap="round"/></g>')
    ticks = "".join(f'<path d="M{48 * math.sin(math.radians(a)):.1f} {-48 * math.cos(math.radians(a)):.1f} L{53 * math.sin(math.radians(a)):.1f} {-53 * math.cos(math.radians(a)):.1f}" stroke="var(--c2)" stroke-width="1.5" opacity=".7"/>'
                    for a in range(-90, 91, 30))
    gauge = ('<path d="M-40 0 A40 40 0 0 1 40 0" fill="none" stroke="var(--line)" stroke-width="6" stroke-linecap="round"/>'
             '<path d="M22.9 -32.8 A40 40 0 0 1 40 0" fill="none" stroke="var(--c5)" stroke-width="6" stroke-linecap="round"/>'
             + ticks + needle + '<circle r="5" fill="var(--white)"/>')
    g.append(pop(gauge, 1462, py - 100, 1.0, .45))
    # the compressor stops: the ripple of the stop, and what it leaves downstream
    g.append(f'<g opacity="0">{beat("opacity", _n04_win(halt))}{glow(sx, py, 130, "var(--c5)", .35)}</g>')
    st = (card(-34, -34, 68, 68, "var(--card)", "var(--c2)", 16, 1.5) + '<circle r="10" fill="var(--c1)"/>'
          + f'<g opacity="0">{beat("opacity", _n04_win(halt))}<circle r="12" fill="var(--c5)"/></g>'
          + TC(0, 62, sl["station"], fit(sl["station"], 15, 130, "sector station"), "var(--muted)", W6))
    g.append(pop(st, sx, py, .75, .45) + _n04_ping(sx, py, 28, 150, "var(--c5)", (halt, halt + .14), .14, .7))
    g.append(f'<g opacity="0">{beat("opacity", _n04_win(halt))}{pill(sx, py - 80, sl["chip"], "var(--c5)", ctx, 17, 200, "sector stop")}</g>')
    return "".join(g), D, FREEZE

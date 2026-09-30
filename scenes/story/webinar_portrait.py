"""Portrait twins (0.6.0) of the webinar-panel scenes (story/webinar_s01_15.py, story/webinar_panel.py), world «Luz de
operación» (worlds/luz.py). Under ORIENT() == "portrait" each w01…w15 / wp_* hands over to its _wqNN_* twin here, which
tells the same story in ART_ZONE on the 900x1600 stage: labels of 20 px or more (rendered), lands by 2 s, loop 12 s,
frozen frame at 10.8 s; the desktop output stays byte-identical.

Two kinds of twin:
- a «left» scene whose art is already a tall block with large labels (w03, w04, w05, w09, w10, w12) is drawn by its own
  desktop code and scaled up (1.1-1.4x) into the art zone (_wq_reuse): the same drawing, bigger, never a copy of the code;
  its far layer of depth is redrawn over the portrait zone;
- any other scene (the «top» band, a row that must become a column, a label under 20 px) is re-laid out here.
Private helpers are _wq_*; loaded after worlds/luz.py in the scenes' shared namespace (twins are looked up at call time).
"""


def _wq_zone():
    return ART_ZONE("left")


def _wq_fit(box):
    """(tx, ty, s): the uniform scale that maps a desktop box (x, y, w, h) into the portrait art zone, centred."""
    zx, zy, zw, zh = _wq_zone()
    bx, by, bw, bh = box
    s = min(zw / bw, zh / bh)
    return zx + zw / 2 - (bx + bw / 2) * s, zy + zh / 2 - (by + bh / 2) * s, s


def _wq_gend(svg):
    """The index just after the <g> element that opens svg (balanced <g …>/</g>)."""
    depth, i = 0, 0
    while True:
        o, c = svg.find("<g", i), svg.find("</g>", i)
        while o != -1 and svg[o + 2] not in " >":
            o = svg.find("<g", o + 2)
        if o != -1 and o < c:
            depth, i = depth + 1, o + 2
        else:
            depth, i = depth - 1, c + 4
            if depth == 0:
                return i


def _wq_desk(fn, sl, ctx):
    """The desktop svg of a scene, drawn with the orientation switched off for the call (its twin redirect skipped)."""
    saved = os.environ.pop("DCD_ORIENT", None)
    try:
        return fn(sl, ctx)[0]
    finally:
        if saved is not None:
            os.environ["DCD_ORIENT"] = saved


def _wq_reuse(fn, sl, ctx, box, seed, n=24):
    """A «left» desktop scene scaled into the portrait art zone: its own far layer (the leading lx_depth group) is dropped
    and a portrait one drawn over the zone, clear of the scaled labels. Returns the marked svg triple."""
    svg = _wq_desk(fn, sl, ctx)
    if svg.startswith('<g aria-hidden="true">'):
        svg = svg[_wq_gend(svg):]
    tx, ty, s = _wq_fit(box)
    avoid = [(tx + x * s, ty + y * s, w * s, h * s) for x, y, w, h in _lx_text_boxes(svg)]
    art = f'<g transform="translate({tx:.1f} {ty:.1f}) scale({s:.4f})">{svg}</g>'
    return portrait_mark(lx_depth(_wq_zone(), n=n, seed=seed, avoid=avoid) + art), D, FREEZE


# ---------------------------------------------------------------- reused «left» scenes
def _wq03_apertura(sl, ctx):
    """w03: the funnel is already vertical; drawn 1.24x (labels 25-32 px)."""
    return _wq_reuse(sc_w03_apertura, sl, ctx, (860, 88, 660, 720), "p apertura")


def _wq04_divisor(sl, ctx):
    """w04: the orbit, the satellites and «Operación» outside, 1.24x (labels 25-60 px)."""
    return _wq_reuse(sc_w04_divisor, sl, ctx, (860, 96, 660, 700), "p divisor", 20)


def _wq05_ciclo(sl, ctx):
    """w05: the loop, its door with the «?» and the shelf of demos, 1.36x (labels 27 px)."""
    return _wq_reuse(sc_w05_ciclo, sl, ctx, (880, 150, 600, 640), "p ciclo")


def _wq09_costo(sl, ctx):
    """w09: the console of three panels, their pictograms and the budget's exchange, 1.12x (labels 20-22 px)."""
    return _wq_reuse(sc_w09_costo, sl, ctx, (820, 80, 740, 780), "p costo", 16)


def _wq10_ola(sl, ctx):
    """w10: the loop carried by agents, the spark at the lit door and the static figure, 1.32x (labels 21-148 px)."""
    return _wq_reuse(sc_w10_ola, sl, ctx, (860, 160, 600, 680), "p ola")


def _wq12_panel(sl, ctx):
    """w12: the lamp, the three seats under their cones and their cards, 1.2x (labels 23-26 px)."""
    return _wq_reuse(sc_w12_panel, sl, ctx, (850, 86, 680, 710), "p panel")


# ---------------------------------------------------------------- slide 1: the loop with no exit (lighter spiral)
def _wq01_portada(sl, ctx):
    """w01 on the portrait stage: the same spark «IA», spiral, closing ring and tilted far plane, centred in the art
    zone at 1.12x; the spiral is sampled at half the desktop's resolution (invisible at this scale, and the svg stays
    under 35 KB). Frozen frame: the ring closed and lit round the spark, the rider on it."""
    cx, cy, r0, r1, laps, a0 = 1190, 438, 300, 132, 3, -150
    pt = lambda r, ang: (cx + r * math.cos(math.radians(ang)), cy + r * math.sin(math.radians(ang)))
    n = 36 * laps
    spiral = [pt(r0 + (r1 - r0) * k / n, a0 + 360 * laps * k / n) for k in range(n + 1)]
    ring = [pt(r1, a0 + 10 * k) for k in range(1, 73)]
    d, total = _w01_poly(spiral + ring)
    a = _w01_poly(spiral)[1] / total
    close = .66
    run = [(0, 0), (.16, 0), (close, a), (.97, 1), (1, 1)]
    show = [(0, 0), (.155, 0), (.165, 1), (.97, 1), (.99, 0), (1, 0)]
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
    dim = beat("opacity", [(0, 1), (close, 1), (close + .04, .42), (.97, .42), (.99, 1), (1, 1)])
    trail = (f'<g>{dim}{lx_trail(d, begin=.25, dur=1.55, spark=False)}'
             + _w01_charge(d, [(0, 0), (.16, 0), (close, a), (.97, 1), (.99, 1), (1, 0)], show) + '</g>')
    lit_ring = (f'<g>{lx_lit(close)}<circle cx="{cx}" cy="{cy}" r="{r1}" fill="none" stroke="{LX_MAGENTA}" stroke-width="14" opacity=".18"/>'
                f'<circle cx="{cx}" cy="{cy}" r="{r1}" fill="none" stroke="{LX_MAGENTA}" stroke-width="2.4"/></g>')
    ripple = (f'<circle cx="{cx}" cy="{cy}" r="{r1}" fill="none" stroke="{LX_MAGENTA}" stroke-width="2" opacity="0">'
              + beat("r", [(0, r1), (close, r1), (close + .1, r1 + 90), (1, r1 + 90)])
              + beat("opacity", [(0, 0), (close - .002, 0), (close, .9), (close + .1, 0), (1, 0)]) + '</circle>')
    flare = f'<g opacity="0">{beat("opacity", [(0, 0), (close, 0), (close + .02, .8), (close + .14, 0), (1, 0)])}{glow(cx, cy, 120, LX_GOLD, .7)}</g>'
    heart = pop(f'<g>{loop("opacity", ".35;.9;.35", 3)}{glow(0, 0, 64, LX_GOLD, .6)}</g>'
                f'<circle r="30" fill="none" stroke="{LX_GOLD}" stroke-width="1.4">{loop("r", "30;96", 3)}'
                f'{loop("stroke-opacity", ".6;0", 3)}</circle>' + lx_spark(0, 0, 2.2), cx, cy, .2, .45)
    rider = _w01_rider(d, run, show, .8)
    ia = land(lx_label(cx, cy + 100, sl["spark"], 36, 200, "portada spark", "var(--white)", "middle"), .45, .5, 10)
    fmt = land(f'<path d="M{cx - 250} 842 h40 M{cx + 210} 842 h40" stroke="{LX_EDGE}" stroke-width="1.2"/>'
               + lx_label(cx, 848, sl["format"], 22, 400, "portada format", LX_LILAC, "middle"), .6, .5, 10)
    art = back + orbits + trail + lit_ring + ripple + front + flare + heart + rider
    tx, ty, s = _wq_fit((826, 80, 728, 790))
    inner = glow(cx, cy, 420, "var(--brand)", .6) + lx_drift(art + ia, cx, cy) + fmt
    avoid = [(tx + x * s, ty + y * s, w * s, h * s) for x, y, w, h in _lx_text_boxes(ia + fmt)]
    return portrait_mark(lx_depth(_wq_zone(), n=24, seed="p portada", avoid=avoid)
                         + f'<g transform="translate({tx:.1f} {ty:.1f}) scale({s:.4f})">{inner}</g>'), D, FREEZE


# ---------------------------------------------------------------- slide 6: three figures and a narrow door (a column)
def _wq06_datos(sl, ctx):
    """w06 re-laid out: the three static figures in glass cards down the zone (labels 21-22 px), the wall of light on the
    right with its tall narrow door «Operación»; each card's edge lights in turn and its sparks look for the door along
    the wall, the last one crosses, the door lights and the three edges glow together. Frozen: as the desktop."""
    zx, zy, zw, zh = _wq_zone()
    x0, w, pad, gap, vz = zx, 668, 24, 20, 72
    small = (22, 21, 20)
    figs = sl["figure"]
    hs = [lx_figure(x0 + pad, 0, f["v"], f["label"], f["src"], w - 2 * pad, f.get("pre"), vz, small)[1] + 36 for f in figs]
    y = zy + max(10, (zh - sum(hs) - gap * (len(hs) - 1)) / 2)
    turns = ((.10, .30), (.33, .53), (.56, .76))
    cross_at, lit_at = .765, .80
    cards, edges, ys = [], [], []
    for (f, h), (a, b) in zip(zip(figs, hs), turns):
        cards.append(lx_card(x0, y, w, h, 18) + lx_figure(x0 + pad, y + 18, f["v"], f["label"], f["src"], w - 2 * pad,
                                                          f.get("pre"), vz, small)[0])
        pts = [(0, 0), (a, 0), (a + .02, 1), (b, 1)]
        pts += [(b + .03, .45), (lit_at, .45)] if b + .03 < lit_at else []
        pts += [(lit_at + .02, 1), (.97, 1), (.99, 0), (1, 0)]
        rect = lambda sw, o: (f'<rect x="{x0}" y="{y:.1f}" width="{w}" height="{h:.1f}" rx="18" fill="none" '
                              f'stroke="{LX_MAGENTA}" stroke-width="{sw}" opacity="{o}"/>')
        edges.append(f'<g opacity="0">{beat("opacity", pts)}{rect(9, .14)}{rect(2, 1)}</g>')
        ys.append(y + h / 2)
        y += h + gap
    still = [glow(zx + zw / 2, zy + zh / 2, 460, "var(--brand)", .45), seq(cards, .1, .5, 16)] + edges
    wx, base, gh, gw = 800, zy + 540, 176, 44
    top, bot = zy + 20, zy + zh - 10
    wall = (f'<path d="M{wx} {top} V{base - gh - 12} M{wx} {base + 50} V{bot}" stroke="{LX_LILAC}" stroke-width="10" opacity=".05"/>'
            f'<path d="M{wx} {top} V{base - gh - 12} M{wx} {base + 50} V{bot}" stroke="{LX_EDGE}" stroke-width="1.4" '
            f'stroke-dasharray="3 7"/>')
    g = [land(wall + lx_gate(wx, base, sl["door"], gw, gh, lit=cross_at, size=22), .6, .5, 0)]
    ox = x0 + w + 8
    hits = ((top + 60, 36), (top + 140, 34), (top + 260, 36), (base + 200, -34), (base + 280, -36), (top + 300, 30),
            (base + 320, -30))
    for k, (a, b) in enumerate(turns):
        for j in range(5):                              # five sparks per card (seven on desktop): the svg stays under 35 KB
            if k == 2 and j == 4:
                break
            hy, slide = hits[(j + 3 * k) % 7]
            t0 = a + .015 + j * .036
            g.append(_w06_seek((ox, ys[k] + (j - 3) * 9), (wx - 8, hy), slide, t0, t0 + .05, t0 + .085))
    gy, far = base - gh / 2 + 10, (wx + 34, base - gh / 2 + 2)
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
    return portrait_mark(lx_depth(_wq_zone(), n=18, seed="p datos", labels=art) + art), D, FREEZE


# ---------------------------------------------------------------- slide 8: the ladder (names, rails and sentences stacked)
def _wq08_formas(sl, ctx):
    """w08 re-laid out on the 900-wide stage: the ladder down the left edge, each rung's name (24 px) and its rail on one
    line, its sentence (20 px) under them; the cells' names over the top rail, the legend and the rule under the ladder.
    A spark climbs one rung every 1.56 s; everything lights and stays; the gold wave runs up the objective column."""
    zx, zy, zw, zh = _wq_zone()
    rungs, cells = sl["rungs"], sl["cells"]
    n = len(rungs)
    lx0, lw = zx + 8, 34
    cw, ch, gp = 94, 24, 8
    rw = lx_rail_w(cw, gp)
    rx = zx + zw - rw                                      # the rails, right-aligned
    nx = lx0 + lw + 26                                     # names and sentences
    y0, s = zy + 36, 122
    at = [.12 + k * .13 for k in range(n)]
    wave = at[-1] + .04
    lad, ys = lx_ladder(lx0, y0, lw, s * n, n, light_at=at)
    arts, labs = [lad], [""]
    for k, (name, desc, states) in enumerate(rungs):
        y = ys[k]
        ox, oy = rx + cw / 2, y
        w0 = wave + k * .012
        arts.append("".join([
            f'<path d="M{lx0 + lw} {y:.1f} H{nx - 8}" stroke="{LX_EDGE}" stroke-width="1.2"/>',
            f'<g>{lx_lit(at[k])}<path d="M{lx0 + lw} {y:.1f} H{nx - 8}" stroke="{LX_MAGENTA}" stroke-width="1.8"/>'
            f'{glow(f"{ox:.1f}", f"{oy:.1f}", 28, LX_GOLD, .3)}</g>',
            lx_rail(rx, y - ch / 2, states, cw, ch, gp, fill_at=at[k]),
            f'<g>{lx_lit(at[k])}<rect x="{rx}" y="{y - ch / 2:.1f}" width="{cw}" height="{ch}" rx="5" fill="none" '
            f'stroke="{LX_GOLD}" stroke-width="1.8"/></g>',
            f'<g opacity="0">{beat("opacity", [(0, 0), (w0, 0), (w0 + .015, 1), (.97, 1), (.99, 0), (1, 0)])}'
            f'<rect x="{rx - 2}" y="{y - ch / 2 - 2:.1f}" width="{cw + 4}" height="{ch + 4}" rx="7" fill="none" '
            f'stroke="{LX_GOLD}" stroke-width="1.4"/>{glow(f"{ox:.1f}", f"{oy:.1f}", 30, LX_GOLD, .35)}</g>']))
        room = zx + zw - nx
        dsc, _h = lx_lines(nx, y + 36, desc, room, 20, "formas rung text", "var(--muted)")
        labs.append(lx_label(nx, y + 8, name, 24, rx - nx - 14, "formas rung name", _w07_TXT)
                    + f'<g>{lx_lit(at[k])}{lx_label(nx, y + 8, name, 24, rx - nx - 14, "formas rung name", "var(--white)")}</g>'
                    + f'<g>{beat("opacity", [(0, .55), (at[k], .55), (at[k] + .02, 1), (.97, 1), (.99, .55), (1, .55)])}{dsc}</g>')
    hy = ys[-1] - ch / 2 - 12
    labs.append("".join(lx_label(rx + j * (cw + gp) + cw / 2, hy, c, 20, cw + 6, "formas cell",
                                 LX_GOLD if j == 0 else "var(--muted)", "middle", bold=j == 0) for j, c in enumerate(cells)))
    ly = y0 + s * n + 26
    leg, _w = lx_rail_legend(nx, ly, sl["legend"], 40, ch, 20)
    arts.append("")
    labs.append(leg)
    if sl.get("rule"):
        ry = ly + ch + 40
        dash = f"M{nx} {ry - 8} h40"
        arts.append(f'<path d="{dash}" stroke="{LX_EDGE}" stroke-width="2" stroke-linecap="round"/>'
                    + _w07_draw(dash, LX_GOLD, 2.4, [(0, 0), (wave + .05, 0), (wave + .075, 1), (.97, 1), (.99, 0), (1, 0)],
                                'stroke-linecap="round"'))
        labs.append(lx_label(nx + 54, ry, sl["rule"], 22, zx + zw - nx - 54, "formas rule", "var(--white)"))
    x_ = lx0 + lw / 2
    d = f"M{x_} {y0 + s * n} V{ys[-1]:.1f}"
    ln = y0 + s * n - ys[-1]
    stops = [(0, 0), (at[0], (y0 + s * n - ys[0]) / ln)]
    for k in range(1, n):
        stops += [(at[k] - .05, (y0 + s * n - ys[k - 1]) / ln), (at[k], (y0 + s * n - ys[k]) / ln)]
    stops.append((1, 1))
    art = seq(arts, .1, .5, 12) + lx_trail(d, begin=.05, dur=1.0, spark=False) + _w07_spark(d, stops, .07)
    text = seq(labs, .1, .5, 12)
    return portrait_mark(lx_depth(_wq_zone(), 14, "p formas", labels=text) + lx_drift(art + text, 450, 1090, 1.01)), D, FREEZE


# ---------------------------------------------------------------- slide 15: loop on top, the bridge, the speaker below
def _wq15_final(sl, ctx):
    """w15 stacked: the pilot's loop at the top of the zone paints its magenta lap; at 5 s the spark breaks out at the
    ring's right point, swoops down and across onto the bridge and runs it lighting the five pillars (labels 20 px,
    staggered), lands on «Operación», which bursts gold; the speaker in his ring of light under the bridge and the
    line at the bottom. Frozen frame: the trail landed, «Operación» lit, the loop quiet, the speaker and the line."""
    zx, zy, zw, zh = _wq_zone()
    cx, cy, r = 450, zy + 166, 112
    x0, x1, by = zx + 70, zx + zw - 90, zy + 386
    t_lap0, t_brk = 1 / D, 5 / D
    t_deck, t_in = t_brk + .07, .70
    p0, c1, c2, p3 = (cx + r, cy), (cx + r + 60, cy + 150), (x0 - 70, by - 120), (x0, by)
    out = f"M{p0[0]} {p0[1]} C{c1[0]} {c1[1]} {c2[0]} {c2[1]} {p3[0]} {p3[1]} H{x1}"
    curve = _w15_cubic_len(p0, c1, c2, p3)
    fc = curve / (curve + x1 - x0)
    lap_d = f"M{cx + r} {cy} A{r} {r} 0 1 1 {cx + r} {cy - .01}"
    pillars = list(sl.get("bridge") or LX_PILLARS)
    step = (x1 - x0) / (len(pillars) + 1)
    light = [t_deck + (t_in - t_deck) * step * (k + 1) / (x1 - x0) for k in range(len(pillars))]
    to = sl.get("to", "Operación")
    quiet = lambda lo: beat("opacity", [(0, 1), (t_brk + .02, 1), (t_brk + .1, lo), (.96, lo), (.99, 1), (1, 1)])
    lap = (f'<g>{quiet(.35)}' + _w15_run(lap_d, t_lap0, t_brk, 10, 'opacity=".16"') + _w15_run(lap_d, t_lap0, t_brk, 2.2)
           + '</g>')
    loop_ = (f'<g>{quiet(.72)}' + lx_loop(cx, cy, r, stops=sl.get("stops") or ("Idea", "POC", "Demo"), gate=False, size=22)
             + lx_label(cx, cy + 8, sl.get("from", "Piloto"), 22, 2 * r - 40, "w15 from", "var(--muted)", "middle") + '</g>')
    bridge = lx_bridge(x0, x1, by, pillars, "", "", light_at=light, h=96, size=20)
    show = [(0, 0), (t_brk - .005, 0), (t_brk, 1), (t_in, 1), (t_in + .02, 0), (1, 0)]
    stops = [(0, 0), (t_brk, 0), (t_deck, fc), (t_in, 1), (1, 1)]
    breakout = (_w15_burst(*p0, t_brk, 8, 48, .09) + _w15_burst(*p0, t_brk + .01, 8, 70, .11, LX_MAGENTA, 1.4)
                + _w15_rays(*p0, t_brk))
    pace = beat("stroke-dashoffset", [(0, 1), (t_brk, 1), (t_deck, round(1 - fc, 4)), (t_in, 0), (.97, 0), (.985, 1), (1, 1)])
    escape = "".join(
        f'<path d="{out}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{LX_MAGENTA}" stroke-width="{wd}" '
        f'stroke-linecap="round" opacity="{op}">{pace}</path>' for wd, op in ((12, .12), (5, .3), (2.4, 1)))
    comet = _w15_comet(out, stops, show, .12, 10, .26) + _w15_comet(out, stops, show, .055, 4, .9)
    sparks = "".join(_w15_burst(x0 + step * (k + 1), by, a, 4, 24, .06) for k, a in enumerate(light))
    rider = _w13_rider(out, stops, show, .95)
    lit = (f'<g>{lx_lit(t_in)}<g>{loop("opacity", ".55;1;.55", 3)}{glow(x1, by + 20, 48, LX_GOLD, .65)}</g>'
           f'<circle cx="{x1}" cy="{by}" r="10" fill="{LX_GOLD}"/>'
           f'<circle cx="{x1}" cy="{by}" r="18" fill="none" stroke="{LX_GOLD}" stroke-width="1.6"/>'
           f'<circle cx="{x1}" cy="{by}" r="26" fill="none" stroke="{LX_GOLD}" stroke-width="1" opacity=".45"/></g>')
    landing = (_w15_burst(x1, by, t_in, 10, 58, .1) + _w15_burst(x1, by, t_in + .02, 10, 92, .14, LX_GOLD, 1.2)
               + _w15_rays(x1, by, t_in, 10))
    to_labels = (f'<g>{beat("opacity", [(0, 1), (t_in, 1), (t_in + .02, 0), (.97, 0), (.99, 1), (1, 1)])}'
                 + lx_label(x1 - 10, by - 34, to, 22, 200, "w15 to", "var(--white)", "middle") + '</g>'
                 + f'<g>{lx_lit(t_in)}' + lx_label(x1 - 10, by - 34, to, 22, 200, "w15 to", LX_GOLD, "middle") + '</g>')
    dsig = 150
    signer = lx_signer(cx - dsig / 2, zy + 590, dsig, sl.get("name", ""), sl.get("role", ""), (24, 20))
    sign = (f'<g>{lx_lit(t_in + .05)}'
            + lx_label(cx, zy + zh - 16, sl.get("sign", ""), 20, zw - 40, "w15 sign", "var(--muted)", "middle") + '</g>')
    art = (land(lap + loop_, .1, .5, 0) + land(bridge, .3, .5, 12) + escape + comet + sparks + breakout + rider + lit + landing
           + to_labels + land(signer, .5, .6, 18) + sign)
    depth = lx_depth(_wq_zone(), n=22, seed="p final", labels=art, avoid=[(cx - 100, zy + 570, 200, 200)])
    return portrait_mark(depth + glow(450, 1090, 520, "var(--brand)", .45) + lx_drift(art, 450, 1090, 1.012, 0, -5)), D, FREEZE


# ---------------------------------------------------------------- slide 2: the 55 minutes, down a timeline of light
def _wq02_agenda(sl, ctx):
    """w02 stacked: the four glass cards one under the other, each taller by its share of the 55 minutes (the panel the
    tallest), on a vertical timeline of light whose marks 00:00 · 05:00 · 15:00 · 45:00 · 55:00 sit at their edges.
    The spark runs the timeline down and lights each card as it reaches it (2 · 2.8 · 4 · 8.2 s); the panel lights its
    five questions and keeps its spotlights breathing; the spark rests on 55:00, which lights. Frozen: all lit."""
    zx, zy, zw, zh = _wq_zone()
    blocks, steps = sl["blocks"], sl["steps"]
    marks = [_w02_min(t) for _n, t in blocks] + [_w02_min(sl["end"])]
    times = [t for _n, t in blocks] + [sl["end"]]
    ax, bx, bw, gap, pad = zx + 76, zx + 96, zw - 96, 12, 20
    shares = [(marks[k + 1] - marks[k]) / (marks[-1] - marks[0]) for k in range(len(blocks))]
    free = zh - 10 - gap * (len(blocks) - 1) - 150 * len(blocks)
    hs = [150 + free * f for f in shares]
    tops = [zy + 4 + sum(hs[:k]) + gap * k for k in range(len(blocks))]
    Y = tops + [tops[-1] + hs[-1]]
    fr = lambda y: (y - Y[0]) / (Y[-1] - Y[0])
    lit, end_t = [.17, .23, .33, .68], .79
    talks = [steps[0:1], steps[1:3], steps[3:4], steps[4:6]]
    axis = f"M{ax} {Y[0]} V{Y[-1]:.1f}"
    arts, labels, overs, over_t = [], [], [], []
    for k, ((block, _t), a) in enumerate(zip(blocks, lit)):
        name, _s, dur = str(block).partition(" · ")
        top, ch = tops[k], hs[k]
        colw = 380 if k == 2 else bw - 2 * pad - 90
        base = [lx_card(bx, top, bw, ch, 16),
                f'<path d="M{bx + pad} {top + 94:.1f} H{bx + pad + colw}" stroke="{LX_EDGE}" stroke-width="1.2"/>']
        on = [lx_card(bx, top, bw, ch, 16, LX_LILAC, 1.8, LX_GLASS_LIT),
              f'<path d="M{bx} {top + 18:.1f} V{top + ch - 18:.1f}" stroke="{LX_MAGENTA}" stroke-width="2.6" stroke-linecap="round"/>',
              f'<path d="M{bx + pad} {top + 94:.1f} H{bx + pad + colw}" stroke="{LX_LILAC}" stroke-width="1.2" opacity=".6"/>']
        lab = lambda col, dcol: [lx_label(bx + pad, top + 48, dur, 36, colw, "agenda duration", dcol),
                                 lx_label(bx + pad, top + 82, name, 24, colw, "agenda name", col)]
        bt, ot = lab("var(--muted)", "var(--muted)"), lab(LX_LILAC, "var(--white)")
        bullet = len(talks[k]) > 1
        yy = top + 126
        for s_ in talks[k]:
            tx = bx + pad + (18 if bullet else 0)
            ln, h_ = lx_lines(tx, yy, s_, colw - (18 if bullet else 0), 22, "agenda talk", "var(--muted)")
            lt, _h = lx_lines(tx, yy, s_, colw - (18 if bullet else 0), 22, "agenda talk", "var(--white)")
            bt.append(ln)
            ot.append(lt)
            if bullet:
                base.append(f'<circle cx="{bx + pad + 5}" cy="{yy - 7:.1f}" r="4" fill="{LX_DIM}"/>')
                on.append(f'<circle cx="{bx + pad + 5}" cy="{yy - 7:.1f}" r="4" fill="{LX_GOLD}"/>')
            yy += h_ + 8
        gx, gy = bx + bw - 64, top + ch / 2
        if k == 0:
            base.append(_w02_chat_glyph(gx, gy, LX_DIM, 2))
            on.append(_w02_chat_glyph(gx, gy, LX_LILAC, 2)
                      + "".join(f'<circle cx="{gx - 12 + 12 * j:.1f}" cy="{gy:.1f}" r="2.8" fill="{LX_GOLD}">'
                                f'{loop("opacity", ".2;1;.2", 1.2, j * .3)}</circle>' for j in range(3)))
        elif k == 1:
            base.append(_w02_mini_loop(gx, gy, 30))
            on.append(_w02_mini_loop(gx, gy, 30, True))
        elif k == 2:
            qs = [a + .035 + j * .07 for j in range(5)]
            for j, q in enumerate(qs):
                qx, qy = bx + pad + 14 + j * 44, yy + 18
                ring_q = f'<circle cx="{qx:.1f}" cy="{qy:.1f}" r="14" fill="none" stroke="{{}}" stroke-width="1.4"/>'
                base.append(ring_q.format(LX_EDGE))
                on.append(ring_q.format(LX_EDGE) + f'<g>{lx_lit(q)}{glow(f"{qx:.1f}", f"{qy:.1f}", 26, LX_GOLD, .6)}'
                          f'<circle cx="{qx:.1f}" cy="{qy:.1f}" r="9" fill="{LX_GOLD}"/></g>')
            t0, t1, ty = bx + pad + colw + 30, bx + bw - 24, top + ch - 34
            seats = [t0 + (t1 - t0) * f for f in (1 / 6, 1 / 2, 5 / 6)]
            cones = "".join(f'<path d="M{x - 6:.1f} {top + 8} L{x + 6:.1f} {top + 8} L{x + 50:.1f} {ty} L{x - 50:.1f} {ty} Z" '
                            f'fill="color-mix(in srgb, var(--c2) 12%, transparent)"/>' for x in seats)
            on.insert(1, f'<g>{loop("opacity", ".45;1;.45", 3)}{cones}</g>'
                         f'<rect x="{bx - 5}" y="{top - 5:.1f}" width="{bw + 10}" height="{ch + 10:.1f}" rx="20" fill="none" '
                         f'stroke="{LX_LILAC}" stroke-width="1.4">{loop("stroke-opacity", ".1;.7;.1", 3)}</rect>')
            front = lx_table(t0 - 10, t1 + 10, ty, 14) + "".join(lx_seat(x, ty, .9, LX_LILAC, a + .015 * (j + 1)) for j, x in enumerate(seats))
            overs.append(f'<g>{lx_lit(a)}{"".join(on)}</g>' + land(front, .66, .5, 10))
            on = None
        else:
            base.append(lx_spark(gx, gy, .9, LX_DIM))
            on.append(lx_spark(gx, gy, .9))
        arts.append("".join(base))
        if on is not None:
            overs.append(f'<g>{lx_lit(a)}{"".join(on)}</g>')
        labels.append("".join(bt))
        over_t.append(f'<g>{lx_lit(a)}{"".join(ot)}</g>')
    ticks, ticks_on, times_b, times_on = [], [], [], []
    for k, (y, t) in enumerate(zip(Y, times)):
        at = (lit + [end_t])[k]
        ly = y + 22 if k == 0 else y - 8 if k == len(Y) - 1 else y - gap / 2 + 7
        ticks.append(f'<path d="M{ax - 8} {y:.1f} H{bx - 6}" stroke="{LX_EDGE}" stroke-width="1.2"/>')
        col = LX_GOLD if k == len(Y) - 1 else LX_MAGENTA
        ticks_on.append(f'<g>{lx_lit(at)}<path d="M{ax - 8} {y:.1f} H{bx - 6}" stroke="{col}" stroke-width="2"/>'
                        f'<circle cx="{ax}" cy="{y:.1f}" r="4.5" fill="{col}"/></g>')
        times_b.append(lx_label(ax - 12, ly, t, 20, 70, "agenda time", "var(--muted)", "end"))
        times_on.append(f'<g>{lx_lit(at)}' + lx_label(ax - 12, ly, t, 20, 70, "agenda time", "var(--white)", "end") + '</g>')
    ps = [fr(y) for y in Y]
    stops = [(0, 0), (lit[0], 0), (lit[1] - .005, ps[1]), (lit[1] + .02, ps[1]), (lit[2] - .005, ps[2]),
             (lit[2] + .02, ps[2]), (lit[3] - .005, ps[3]), (lit[3] + .02, ps[3]), (end_t, 1), (1, 1)]
    show = [(0, 0), (.155, 0), (.165, 1), (.97, 1), (.99, 0), (1, 0)]
    charge = _w01_charge(axis, [(t, f) for t, f in stops[:-1]] + [(.99, 1), (1, 0)], show, 2.6)
    end = f'<g>{lx_lit(end_t)}{glow(ax, f"{Y[-1]:.1f}", 24, LX_GOLD, .8)}</g>'
    art = (seq(arts, .3, .5, 14) + land("".join(ticks), .3, .5, 8) + lx_trail(axis, begin=.1, dur=1.2, spark=False)
           + charge + "".join(overs) + "".join(ticks_on) + end + _w01_rider(axis, stops, show, .8))
    text = seq(labels, .3, .5, 14) + land("".join(times_b), .3, .5, 8) + "".join(over_t) + "".join(times_on)
    g = [glow(450, 1090, 480, "var(--brand)", .45), lx_depth(_wq_zone(), n=18, seed="p agenda", labels=text),
         lx_drift(art + text, 450, 1090, 1.008, 0, -4)]
    return portrait_mark("".join(g)), D, FREEZE


# ---------------------------------------------------------------- slide 7: the table Piloto | Operación, the gauge below
def _wq07_salto(sl, ctx):
    """w07 stacked: the table (22 px) across the zone, the thread down its right edge; the spark stops at each row and
    a pulse crosses from the pilot cell to the operation cell (the pilot dims, the operation lights); after the last
    row the thread turns under the table to the big KPI gauge, the spark rides the needle up and the dial blooms."""
    zx, zy, zw, zh = _wq_zone()
    head, rows = sl["head"], sl["rows"]
    n = len(rows)
    xl, xp, wp, xo, wo = zx, zx + 150, 290, zx + 454, 336
    y0, rh, gap = zy + 64, 70, 12
    xt = xo + wo + 14
    gr, gcx = 190, 450
    at = [.19 + k * .105 for k in range(n)]
    rise, up = at[-1] + .07, .8
    ycs = [y0 + k * (rh + gap) + rh / 2 for k in range(n)]
    gcy = zy + zh - 90
    top = y0 - 28
    x1 = gcx + gr
    turn_y = ycs[-1] + rh / 2 + 40
    d = (f"M{xt} {top} V{turn_y - 20:.1f} A20 20 0 0 1 {xt - 20} {turn_y:.1f} H{x1 + 20} "
         f"A20 20 0 0 0 {x1} {turn_y + 20:.1f} V{gcy:.1f}")
    l1 = turn_y - 20 - top
    lt = l1 + math.pi * 20 + (xt - 40 - x1) + (gcy - turn_y - 20)
    ps = [(y - top) / lt for y in ycs]
    front = [(0, 0), (.125, 0)]
    for k, p in enumerate(ps):
        front += [(at[k] - .045, p), (at[k] + .01, p)]
    front += [(rise, 1), (.965, 1), (.995, 0), (1, 0)]
    gx = (xp + wp + xo) / 2
    arts, labs = [""], []
    hy = y0 - 18
    hd = lx_label(xl, hy, head[0], 22, xp - xl - 12, "salto head", _w07_TXT) if head[0] else ""
    hd += lx_label(xp + wp / 2, hy, head[1], 24, wp - 20, "salto head", "var(--muted)", "middle")
    hd += lx_label(xo + wo / 2, hy, head[2], 24, wo - 20, "salto head", "var(--white)", "middle")
    labs.append(hd)
    for k, (lab, pil, op) in enumerate(rows):
        yt, yc = y0 + k * (rh + gap), ycs[k]
        last = k == n - 1
        edge = LX_GOLD if last else LX_LILAC
        h0 = at[k] - .04
        conn = f"M{xp + wp} {yc:.1f} H{xo}"
        arts.append("".join([
            lx_card(xp, yt, wp, rh, 12, LX_DIM),
            f'<g>{_w07_dim(at[k])}{lx_card(xp, yt, wp, rh, 12, LX_EDGE, 1.4)}</g>',
            lx_card(xo, yt, wo, rh, 12, LX_DIM),
            f'<circle cx="{xo + 22}" cy="{yc:.1f}" r="6" fill="none" stroke="{LX_EDGE}" stroke-width="1.4"/>',
            f'<path d="{conn}" stroke="{LX_DIM}" stroke-width="1.4"/>', _w07_chev(gx, yc, LX_EDGE),
            f'<path d="M{xo + wo} {yc:.1f} H{xt}" stroke="{LX_DIM}" stroke-width="1.2"/>',
            _w07_draw(conn, LX_MAGENTA, 2, [(0, 0), (h0, 0), (at[k], 1), (.97, 1), (.99, 0), (1, 0)]),
            f'<g>{lx_lit(at[k])}'
            + lx_card(xo, yt, wo, rh, 12, edge, 1.8, LX_GLASS_LIT)
            + glow(xo + 22, f"{yc:.1f}", 18, LX_GOLD, .8)
            + f'<circle cx="{xo + 22}" cy="{yc:.1f}" r="6" fill="{LX_GOLD}"/>' + _w07_chev(gx, yc, LX_GOLD, 2)
            + f'<path d="M{xo + wo} {yc:.1f} H{xt}" stroke="{LX_MAGENTA}" stroke-width="1.8"/>'
            + f'<circle cx="{xt}" cy="{yc:.1f}" r="4.5" fill="{LX_MAGENTA}"/></g>',
            _w07_pulse(xp + wp - 6, xo + 22, yc, h0, at[k])]))
        labs.append(lx_label(xl, yc + 8, lab, 22, xp - xl - 12, "salto row", "var(--white)")
                    + lx_label(xp + 20, yc + 8, pil, 22, wp - 36, "salto pilot", _w07_TXT, bold=False)
                    + f'<g>{_w07_dim(at[k])}{lx_label(xp + 20, yc + 8, pil, 22, wp - 36, "salto pilot", "var(--white)", bold=False)}</g>'
                    + f'<g>{_w07_dim(at[k])}{lx_label(xo + 40, yc + 8, op, 22, wo - 52, "salto op", _w07_TXT, bold=False)}</g>'
                    + f'<g>{lx_lit(at[k])}{lx_label(xo + 40, yc + 8, op, 22, wo - 52, "salto op", LX_GOLD if last else "var(--white)", bold=last)}</g>')
    gauge, t1 = _w07_gauge(gcx, gcy, gr, rise, up)
    arts.append(gauge)
    glab = sl.get("gauge") or ""
    labs.append(lx_label(gcx, gcy + 46, glab, 24, 2 * gr, "salto gauge", _w07_TXT, "middle")
                + f'<g>{lx_lit(t1)}{lx_label(gcx, gcy + 46, glab, 24, 2 * gr, "salto gauge", "var(--white)", "middle")}</g>'
                if glab else "")
    spine = (lx_trail(d, "color-mix(in srgb, var(--accent) 45%, transparent)", begin=.1, dur=1.4, spark=False)
             + _w07_draw(d, LX_MAGENTA, 3, front, 'stroke-linecap="round" opacity=".9"')
             + _w07_spark(d, front[:-3] + [(1, 1)], .125, rise))
    art = glow(450, 1090, 360, "var(--brand)", .4) + seq(arts, .1, .5, 14) + spine
    text = seq(labs, .1, .5, 14)
    return portrait_mark(lx_depth(_wq_zone(), 16, "p salto", labels=text) + lx_drift(art + text, 450, 1090, 1.012, 0, -5)), D, FREEZE


# ---------------------------------------------------------------- slide 11: E-S-C-A-L-A down the zone
def _wq11_escala(sl, ctx):
    """w11 as a column: the six big letters of light (96 px) read down the zone as the acrostic, each with its word
    (28 px) and its question (22 px) to its right; a thread of light runs down between letters and words, its spark
    stops at each row every 1.6 s (a ring opens, a glint flashes, the letter, its word and question light and stay),
    then the trail turns towards the panel and its node lights. 10.8 s: ESCALA lit, the trail risen, the spark at the end."""
    zx, zy, zw, zh = _wq_zone()
    letters = sl.get("letters") or []
    n = max(len(letters), 1)
    rowh = (zh - 60) / n
    tx, lxc, wx = zx + 150, zx + 64, zx + 180
    ycs = [zy + 16 + rowh * (k + .5) for k in range(n)]
    y_a, y_b = ycs[0] - rowh / 2 + 10, ycs[-1]
    top = (zx + zw - 30, zy + zh - 22)
    c1, c2 = (tx, y_b + 60), (top[0] - 120, top[1])
    full = f"M{tx} {y_a:.1f} V{y_b:.1f} C{c1[0]} {c1[1]:.1f} {c2[0]} {c2[1]} {top[0]} {top[1]}"
    bz = [((1 - u) ** 3 * tx + 3 * (1 - u) ** 2 * u * c1[0] + 3 * (1 - u) * u * u * c2[0] + u ** 3 * top[0],
           (1 - u) ** 3 * y_b + 3 * (1 - u) ** 2 * u * c1[1] + 3 * (1 - u) * u * u * c2[1] + u ** 3 * top[1])
          for u in (k / 40 for k in range(41))]
    base_len = y_b - y_a
    total = base_len + _w11_len(bz)
    ts = [.10 + k * .1333 for k in range(n)]
    t_last, t_up, t_top = ts[-1] + .02, ts[-1] + .045, ts[-1] + .1
    fr = [(y - y_a) / total for y in ycs]
    stops = [(0, 0), (.07, 0)]
    for k in range(n):
        stops += [(ts[k], fr[k]), ((ts[k] + .05) if k < n - 1 else t_last, fr[k])]
    stops += [(t_up, base_len / total), (t_top, 1)]
    art = [trace(f"M{tx} {y_a:.1f} V{y_b:.1f}", LX_MAGENTA, 2, .1, .7, 'opacity=".35"'),
           _w11_grow(full, stops + [(.97, 1), (.99, 0), (1, 0)])]
    labels = []
    for k, row in enumerate(letters):
        ch, word, q = (list(row) + ["", "", ""])[:3]
        y, t = ycs[k], ts[k]
        let_svg, z = lx_letter(lxc, y + 34, ch, 96, lit=t, room=110, where="escala letter")
        zw_ = fit(word, 28, zx + zw - wx, "escala word", floor=22)
        qsvg, _qh = lx_lines(wx, y + 24, q, zx + zw - wx, 22, "escala question", "var(--muted)")
        art.append(f'<circle cx="{tx}" cy="{y:.1f}" r="4" fill="{LX_LILAC}"/>'
                   + f'<g>{lx_lit(t)}<path d="M{lxc + 44} {y:.1f} H{tx - 8}" stroke="{LX_GOLD}" stroke-width="1.6" '
                     f'stroke-linecap="round" opacity=".7"/>{glow(tx, f"{y:.1f}", 18, LX_GOLD, .8)}'
                     f'<circle cx="{tx}" cy="{y:.1f}" r="5" fill="{LX_GOLD}"/></g>'
                   + _w11_ripple(tx, y, t)
                   + f'<g opacity="0">{beat("opacity", [(0, 0), (t, 0), (t + .015, 1), (t + .07, 0), (1, 0)])}'
                     f'{lx_spark(lxc + z * .34, y + 34 - z * .72, .55)}</g>')
        labels.append(let_svg + T(wx, f"{y - 8:.1f}", word, zw_, "var(--muted)", W6)
                      + f'<g>{lx_lit(t)}' + T(wx, f"{y - 8:.1f}", word, zw_, "var(--white)", W6) + qsvg + '</g>')
    art.append(f'<g>{lx_lit(t_top)}{lx_node(top[0], top[1], 6, LX_MAGENTA)}</g>' + _w11_ripple(top[0], top[1], t_top, LX_MAGENTA, 46))
    art.append(_w11_rider(full, stops + [(1, 1)], [(0, 0), (.065, 0), (.08, 1), (.96, 1), (.98, 0), (1, 0)]))
    body = art[0] + art[1] + seq(art[2:2 + n], .15, .5) + "".join(art[2 + n:]) + seq(labels, .15, .5)
    return portrait_mark(lx_depth(_wq_zone(), n=18, seed="p escala", labels=body) + lx_drift(body, 450, 1090)), D, FREEZE


# ---------------------------------------------------------------- slide 13: the five questions in a column (live taps)
def _wq13_preguntas(sl, ctx):
    """w13 as a column: five numbered glass cards stacked on a vertical line of light, the questions large (26 px), a
    still voice meter under each number. Ambient (data-hop): the spark rests beside each question in turn (2.4 s), its
    card's edge glows and its meter speaks. Tap ([data-pick][data-dim], module/deck.js): a stage light falls on the card
    from the line (gold beam, halo, lit glass, pulsing frame, «En curso», a gold meter), the others dim; the questions keep
    full contrast. Frozen frame: nothing picked, the five questions readable, the spark beside the fifth."""
    zx, zy, zw, zh = _wq_zone()
    qs = list(sl["questions"])
    if not 3 <= len(qs) <= 5:
        raise ValueError(f"panel-questions takes 3 to 5 questions, not {len(qs)}: with reserves use panel-questions-list")
    live = sl.get("live", "En curso")
    n, gap, lx = len(qs), 16, zx + 20
    x, w = zx + 60, zw - 60
    h = (zh - 20 - gap * (n - 1)) / n
    ys = [zy + 10 + k * (h + gap) for k in range(n)]
    line = f"M{lx} {ys[0]:.1f} V{ys[-1] + h:.1f}"
    cards, words, hop = [], [], []
    for k, (y0, q) in enumerate(zip(ys, qs)):
        yc, bx, by = y0 + h / 2, x + 42, y0 + 42
        c = (lx_card(x, y0, w, h, 20)
             + f'<circle cx="{bx}" cy="{by:.1f}" r="24" fill="{LX_GLASS_LIT}" stroke="{LX_LILAC}" stroke-width="1.6"/>'
             + _w13_bars(x + 16, y0 + h - 18, LX_DIM, False, 6)
             + f'<path d="M{lx + 9} {yc:.1f} H{x}" stroke="{LX_EDGE}" stroke-width="1.2"/>'
             + lx_node(lx, yc, 5, LX_LILAC, halo=False))
        ring = (f'<path d="M{lx + 10} {yc - 8:.1f} L{x} {y0 + 6:.1f} V{y0 + h - 6:.1f} L{lx + 10} {yc + 8:.1f} Z" '
                f'fill="color-mix(in srgb, var(--c4) 12%, transparent)"/>' + lx_node(lx, yc, 5, LX_GOLD)
                + glow(f"{x + w / 2:.1f}", f"{yc:.1f}", f"{w * .45:.1f}", LX_GOLD, .3)
                + lx_card(x, y0, w, h, 20, LX_GOLD, 2.4, LX_GLASS_LIT)
                + f'<rect x="{x - 8}" y="{y0 - 8:.1f}" width="{w + 16}" height="{h + 16:.1f}" rx="26" fill="none" '
                  f'stroke="{LX_GOLD}" stroke-width="1.4">{loop("stroke-opacity", ".15;.8;.15", 4)}</rect>'
                + f'<circle cx="{bx}" cy="{by:.1f}" r="24" fill="{LX_GLASS_LIT}" stroke="{LX_GOLD}" stroke-width="2"/>'
                + f'<use href="#wq13-gold" transform="translate({x + 16} {y0 + h - 18:.1f})"/>'
                + f'<circle cx="{lx}" cy="{yc:.1f}" r="8" fill="none" stroke="{LX_GOLD}" stroke-width="1.4">'
                  f'{loop("r", "8;26;26", 2)}{loop("opacity", ".9;0;0", 2)}</circle>'
                + pill(x + w - 96, y0 + h - 26, live, LX_GOLD, ctx, 20, 160, "w13 live"))
        c += (f'<g class="pick-ring">{ring}</g>'
              + f'<rect x="{x}" y="{y0:.1f}" width="{w}" height="{h:.1f}" rx="20" fill="var(--ink)" opacity="0"/>')
        cards.append(land(f'<g data-pick="{k}" data-dim="">{c}</g>', .1 + k * .12, .5, 16))
        txt, th = lx_lines(x + 86, 0, q, w - 110, 26, "w13 question", "var(--white)", bold=True)
        z = float(re.search(r'font-size="([\d.]+)"', txt)[1])
        ty = yc - th / 2 + z * .8
        txt, _th = lx_lines(x + 86, ty, q, w - 110, 26, "w13 question", "var(--white)", bold=True)
        words.append(land(TC(bx, f"{by + 8:.1f}", str(k + 1), 22, "var(--white)", W6) + txt, .1 + k * .12, .5, 16))
        hop.append(f'<g opacity="0">{beat("opacity", _w13_turn(k, n))}'
                   + lx_card(x, y0, w, h, 20, LX_MAGENTA, 1.8, "none")
                   + f'<path d="M{lx + 9} {yc:.1f} H{x}" stroke="{LX_MAGENTA}" stroke-width="1.6"/>'
                   + glow(lx, f"{yc:.1f}", 24, LX_MAGENTA, .6)
                   + f'<use href="#wq13-magenta" transform="translate({x + 16} {y0 + h - 18:.1f})"/></g>')
    total = ys[-1] + h - ys[0]
    fracs = [(y + h / 2 - ys[0]) / total for y in ys]
    hop.append(_w13_rider(line, _w13_stops(fracs), _W13_SHOW))
    words_ = "".join(words)
    meters = (f'<defs><g id="wq13-gold">{_w13_bars(0, 0, LX_GOLD, True, 6)}</g>'   # one live meter each, shared by the cards
              f'<g id="wq13-magenta">{_w13_bars(0, 0, LX_MAGENTA, True, 6)}</g></defs>')
    g = [meters, glow(450, 1090, 520, "var(--brand)", .4), lx_trail(line, begin=.15, dur=1.2, spark=False), *cards,
         land(f'<g data-hop="" pointer-events="none">{"".join(hop)}</g>', 1.3, .4, 0),
         f'<g pointer-events="none">{words_}</g>']
    return portrait_mark("".join(g)), D, FREEZE


# ---------------------------------------------------------------- slide 14: chat on top, three cards, the survey below
def _wq_chat(x, y0, w, h, ask):
    """The public's questions, wide: «Sus preguntas, por el chat» (26 px) and the typing dots on the left, the hand with
    its call rings and three messages arriving one by one on the right; the edge pulses in its turn."""
    g = [lx_card(x, y0, w, h, 20, "color-mix(in srgb, var(--accent) 45%, transparent)", 1.4),
         f'<g opacity="0">{beat("opacity", _w14_on(*_W14_TURNS[0]))}'
         + lx_card(x, y0, w, h, 20, LX_MAGENTA, 2, "none")
         + f'<rect x="{x - 8}" y="{y0 - 8}" width="{w + 16}" height="{h + 16}" rx="26" fill="none" stroke="{LX_MAGENTA}" '
           f'stroke-width="1.4">{loop("stroke-opacity", ".1;.8;.1", 2)}</rect></g>']
    mx = x + 330
    for j, (a, right) in enumerate(((.04, False), (.11, True), (.18, False))):
        yy, bw = y0 + 26 + j * 52, 260
        px = x + w - 30 if right else mx + 14
        bx = x + w - 48 - bw if right else mx + 32
        lines = "".join(f'<rect x="{bx + 16}" y="{yy + 11 + i * 12}" width="{ln}" height="6" rx="3" fill="{LX_LILAC}" '
                        f'opacity=".6"/>' for i, ln in enumerate((200, 120 if j != 1 else 160)))
        g.append(f'<g>{lx_lit(a, .96)}' + _w14_person(px, yy + 18)
                 + f'<rect x="{bx}" y="{yy}" width="{bw}" height="38" rx="12" fill="{LX_GLASS_LIT}" stroke="{LX_EDGE}" '
                   f'stroke-width="1.2"/>' + lines + '</g>')
    ty = y0 + h - 34
    g += [f'<circle cx="{x + 30 + i * 14}" cy="{ty}" r="4" fill="{LX_LILAC}">{loop("opacity", ".2;1;.2", 1.2, i * .3)}</circle>'
          for i in range(3)]
    hx, hy = x + 270, ty - 6
    g.append(f'<circle cx="{hx}" cy="{hy}" r="22" fill="{LX_GLASS_LIT}" stroke="{LX_EDGE}" stroke-width="1.2"/>'
             + _w14_hand(hx - 2, hy + 1, LX_LILAC)
             + f'<g opacity="0">{beat("opacity", _w14_on(.02, .28))}'
             + f'<circle cx="{hx}" cy="{hy}" r="22" fill="{LX_GLASS_LIT}" stroke="{LX_GOLD}" stroke-width="2"/>'
             + _w14_hand(hx - 2, hy - 1, LX_GOLD) + '</g>')
    for t in (.02, .10, .18):
        g.append(f'<circle cx="{hx}" cy="{hy}" r="22" fill="none" stroke="{LX_GOLD}" stroke-width="1.4" opacity="0">'
                 f'{beat("r", [(0, 22), (t, 22), (t + .07, 40), (1, 40)])}'
                 f'{beat("opacity", [(0, 0), (t - .005, 0), (t, .9), (t + .07, 0), (1, 0)])}</circle>')
    txt, _th = lx_lines(x + 26, y0 + 48, ask, 280, 26, "w14 ask", "var(--white)", bold=True)
    return "".join(g) + txt


def _wq_survey(x, y0, w, h, label, text, ctx):
    """The survey, wide: the QR frame waiting for its code on the left (a scan line once it lights), its pill and
    where to answer on the right (20-22 px)."""
    qs = h - 48
    qx, qy = x + 30 + qs / 2, y0 + h / 2
    arm, a2 = 24, qs / 2
    corners = lambda col: "".join(
        f'<path d="M{qx + sx * a2:.1f} {qy + sy * (a2 - arm):.1f} V{qy + sy * a2:.1f} H{qx + sx * (a2 - arm):.1f}" '
        f'fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
        for sx in (-1, 1) for sy in (-1, 1))
    inner = qs - 32
    finders = "".join(f'<rect x="{qx - inner / 2 + fx + 8:.1f}" y="{qy - inner / 2 + fy + 8:.1f}" width="18" height="18" rx="3" '
                      f'fill="none" stroke="{LX_EDGE}" stroke-width="1.2"/>'
                      for fx, fy in ((0, 0), (inner - 34, 0), (0, inner - 34)))
    a_on = _W14_TURNS[4][0]
    tx = x + qs + 70
    lw = min(w - qs - 110, bold_width(_(str(label)), 22, current_factor()) + 48)
    txt, _th = lx_lines(tx, y0 + h / 2 + 38, text, x + w - tx - 24, 20, "w14 survey text", "var(--muted)")
    return (lx_card(x, y0, w, h, 20, "color-mix(in srgb, var(--c4) 55%, transparent)", 1.4)
            + f'<rect x="{x}" y="{y0}" width="{w}" height="{h}" rx="20" fill="none" stroke="{LX_GOLD}" stroke-width="3">'
              f'{loop("stroke-opacity", ".08;.45;.08", 4)}</rect>'
            + f'<g>{lx_lit(a_on)}{glow(f"{qx:.1f}", qy, 64, LX_GOLD, .3)}' + lx_card(x, y0, w, h, 20, LX_GOLD, 2, "none") + '</g>'
            + f'<rect x="{qx - inner / 2:.1f}" y="{qy - inner / 2:.1f}" width="{inner}" height="{inner}" rx="8" fill="none" '
              f'stroke="{LX_EDGE}" stroke-width="1.2" stroke-dasharray="4 6"/>' + finders
            + f'<g>{loop("opacity", ".55;1;.55", 4)}{corners(LX_LILAC)}</g>'
            + f'<g>{lx_lit(a_on)}{corners(LX_GOLD)}'
            + f'<rect x="{qx - a2 + 12:.1f}" y="{qy - a2 + 12:.1f}" width="{qs - 24}" height="2" rx="1" fill="{LX_GOLD}" opacity=".85">'
              f'{loop("y", f"{qy - a2 + 12:.1f};{qy + a2 - 14:.1f};{qy - a2 + 12:.1f}", 2.4)}</rect></g>'
            + lx_node(qx, qy, 5, LX_GOLD)
            + pill(tx + lw / 2, y0 + h / 2 - 16, label, LX_GOLD, ctx, 22, lw, "w14 survey") + txt)


def _wq14_reflexiones(sl, ctx):
    """w14 stacked in the order of the cierre: the chat across the top, the three face-down cards «Reflexión 1/2/3» in
    a row, the survey across the bottom, one thread of light joining them (along the cards' tops, down the right edge).
    Ambient: the chat pulses first, then the spark rests at each reflection (its edge breathes) and last at the survey,
    which lights gold and scans its QR frame. Tap ([data-reveal], keys 1-3): the card turns to «Se anota en vivo» with
    three note lines writing themselves, and stays. Frozen frame: messages in, cards face down, survey lit."""
    zx, zy, zw, zh = _wq_zone()
    labels = list(sl.get("reflections") or ["Reflexión 1", "Reflexión 2", "Reflexión 3"])[:3]
    live = sl.get("live", "Se anota en vivo")
    ask = sl.get("ask", "Sus preguntas, por el chat")
    s_label, s_text = (list(sl.get("survey") or ["Encuesta", "QR por confirmar"]) + ["", ""])[:2]
    wr = zw - 36                                           # the row's width: the thread runs down at its right
    ch_, ly, y0, h, gap = 196, zy + 222, zy + 244, 350, 20
    sy, sh = y0 + h + 44, zh - (y0 + h + 44 - zy)
    cw = (wr - 2 * gap) / 3
    xs = [zx + k * (cw + gap) for k in range(3)]
    rx = zx + wr + 18
    thread = f"M{zx + 40} {ly} H{rx - 16} A16 16 0 0 1 {rx} {ly + 16} V{sy + sh / 2:.1f}"
    L = (rx - 16 - zx - 40) + math.pi * 8 + (sy + sh / 2 - ly - 16)
    fr = lambda px: px / L
    stems = (f'<path d="M{zx + 40} {zy + ch_} V{ly - 7}" stroke="{LX_EDGE}" stroke-width="1.2"/>' + lx_node(zx + 40, ly, 5, LX_LILAC, halo=False)
             + "".join(f'<path d="M{x + cw / 2:.1f} {ly + 7} V{y0}" stroke="{LX_EDGE}" stroke-width="1.2"/>'
                       + lx_node(x + cw / 2, ly, 5, LX_LILAC, halo=False) for x in xs))
    parts = [_wq_chat(zx, zy, zw, ch_, ask)]
    for k, (x, lab) in enumerate(zip(xs, labels)):
        xc, ny, num = x + cw / 2, y0 + 130, f"0{k + 1}"
        off = (f'<rect x="{x + 12:.1f}" y="{y0 + 12}" width="{cw - 24:.1f}" height="{h - 24}" rx="12" fill="none" '
               f'stroke="{LX_EDGE}" stroke-width="1.2" stroke-dasharray="5 8"/>'
               + f'<g opacity="0">{beat("opacity", _w14_on(*_W14_TURNS[k + 1]))}'
               + lx_card(x, y0, cw, h, 20, LX_MAGENTA, 1.8, "none") + '</g>'
               + lx_orbit(xc, ny, 34, color=LX_LILAC, dash="2 9", period=24, op=.6)
               + f'<g>{spin(f"{xc:.1f}", ny, 12)}<circle cx="{xc:.1f}" cy="{ny - 34}" r="3" fill="{LX_GOLD}"/></g>'
               + lx_node(xc, ny, 6, LX_LILAC)
               + lx_label(x + 24, y0 + 48, num, 22, 60, "w14 number", LX_GOLD)
               + lx_label(xc, y0 + 250, lab, 26, cw - 32, "w14 reflection", "var(--white)", "middle"))
        txt, _th = lx_lines(x + 24, y0 + 120, live, cw - 48, 26, "w14 live", "var(--white)", bold=True)
        notes = "".join(
            f'<path d="M{x + 24:.1f} {y0 + h - 100 + i * 28} H{x + 24 + (cw - 48) * f:.1f}" pathLength="1" stroke-dasharray="1" '
            f'fill="none" stroke="{LX_MAGENTA if i == 0 else LX_LILAC}" stroke-width="2" stroke-linecap="round">'
            f'{beat("stroke-dashoffset", [(0, 1), (a, 1), (a + .16, 0), (.96, 0), (1, 1)])}</path>'
            for i, (f, a) in enumerate(((1, .04), (.84, .22), (.58, .4))))
        on = (glow(f"{xc:.1f}", y0 + h / 2, f"{cw * .6:.1f}", LX_MAGENTA, .28)
              + lx_card(x, y0, cw, h, 20, LX_MAGENTA, 2, LX_GLASS_LIT) + notes
              + lx_label(x + 24, y0 + 48, num, 22, 60, "w14 number", LX_GOLD)
              + lx_label(x + 64, y0 + 48, lab, 20, cw - 84, "w14 reflection small", "var(--muted)", bold=False) + txt)
        parts.append(f'<g data-reveal="{k}">' + lx_card(x, y0, cw, h, 20)
                     + f'<g class="reveal-off">{off}</g><g class="reveal-on">{on}</g>'
                     + f'<rect x="{x:.1f}" y="{y0}" width="{cw:.1f}" height="{h}" rx="20" fill="var(--ink)" opacity="0"/></g>')
    parts.append(_wq_survey(zx, sy, wr, sh, s_label, s_text, ctx))
    cards = seq(parts, .1, .5, 16)
    fracs = [0] + [fr(x + cw / 2 - zx - 40) for x in xs] + [1]
    stops = [(0, fracs[0])]
    for k in range(1, 5):
        stops += [(_W14_TURNS[k - 1][1], fracs[k - 1]), (_W14_TURNS[k][0], fracs[k])]
    stops += [(.97, fracs[4]), (.975, fracs[0]), (1, fracs[0])]
    g = [glow(450, 1090, 520, "var(--brand)", .4), lx_trail(thread, begin=.3, dur=1.2, spark=False),
         land(stems, .6, .4, 0), cards,
         land(f'<g pointer-events="none">{_w13_rider(thread, stops, _W13_SHOW)}</g>', 1.5, .3, 0)]
    return portrait_mark("".join(g)), D, FREEZE


# ---------------------------------------------------------------- webinar_panel.py: the question list and the reflections
def _wqp_preguntas(sl, ctx):
    """wp_preguntas in the portrait art zone: the same numbered column (3-7 questions, reserves dashed with their label),
    the questions at 20-26 px, the ambient frame visiting each in turn, the presenter's tap lighting one («En curso»)."""
    qs = sl["questions"]
    if not 3 <= len(qs) <= 7:
        raise ValueError(f"panel-questions takes 3 to 7 questions, not {len(qs)}")
    x, y, w, h = _wq_zone()
    n, gap = len(qs), 12
    rh = min(150, (h - gap * (n - 1)) / n)
    y += (h - n * rh - gap * (n - 1)) / 2
    reserve, tag, live = int(sl.get("reserve", 0)), sl.get("reserve_label", "Reserva"), sl.get("live", "En curso")
    tag_w = bold_width(_(str(tag)), 20, current_factor()) + 44 if reserve else 0
    g, rows = [glow(x + w / 2, y + h / 2, max(w, h) * .55, "var(--brand)", .35)], []
    for k, q in enumerate(qs):
        yy, spare, col = y + k * (rh + gap), k >= n - reserve, _WP_COLS[k % len(_WP_COLS)]
        mid = yy + rh / 2
        room = w - 96 - (tag_w + 16 if spare else 24)
        c = card(x, yy, w, rh, "var(--card)", "var(--line)", 16, 1.5, 'stroke-dasharray="7 7"' if spare else "")
        c += f'<rect x="{x}" y="{yy + 14:.1f}" width="4" height="{rh - 28:.1f}" rx="2" fill="{col}"/>'
        c += (f'<circle cx="{x + 44}" cy="{mid:.1f}" r="24" fill="{col}"/>'
              + TC(x + 44, f"{mid + 8:.1f}", str(k + 1), 22, ctx.brand.on(col), W6))
        c += _wp_text(x + 84, mid, q, room, rh - 16, (26, 24, 22, 20), "var(--muted)" if spare else "var(--white)")
        if spare:
            c += pill(x + w - 16 - tag_w / 2, mid, tag, "var(--dim)", ctx, 20, tag_w, "panel reserve")
        c += (f'<g class="pick-ring"><rect x="{x - 4}" y="{yy - 4:.1f}" width="{w + 8}" height="{rh + 8:.1f}" rx="20" fill="none" '
              f'stroke="var(--c4)" stroke-width="3"/><rect x="{x - 8}" y="{yy - 8:.1f}" width="{w + 16}" height="{rh + 16:.1f}" '
              f'rx="24" fill="none" stroke="var(--c4)" stroke-width="1.5">{loop("stroke-opacity", ".05;.6;.05", 2.4)}</rect>'
              + pill(x + w - 100, yy + rh - 22, live, "var(--c4)", ctx, 20, 180, "panel live") + '</g>')
        c += f'<rect x="{x}" y="{yy:.1f}" width="{w}" height="{rh:.1f}" rx="16" fill="var(--ink)" opacity="0"/>'
        rows.append(f'<g data-pick="{k}" data-dim="">{c}</g>')
    g.append(seq(rows, .1, .5, 16))
    hop = (f'<rect x="{x - 4}" y="{y - 4:.1f}" width="{w + 8}" height="{rh + 8:.1f}" rx="20" fill="none" stroke="var(--c4)" stroke-width="2">'
           f'<animateTransform attributeName="transform" type="translate" values="{";".join(f"0 {k * (rh + gap):.1f}" for k in range(n))}" '
           f'keyTimes="{";".join(f"{k / n:.3f}" for k in range(n))}" dur="{D}s" repeatCount="indefinite" calcMode="discrete"/>'
           f'{loop("stroke-opacity", ".25;1;.25", 2.4)}</rect>')
    g.append(land(f'<g data-hop="">{hop}</g>', 1.2, .4, 0))
    return portrait_mark("".join(g)), D, FREEZE


def _wqp_reflexiones(sl, ctx):
    """wp_reflexiones in the portrait art zone: the three face-down numbered cards in a column, edges lighting in turn;
    each tap turns one to its text (20-26 px) with a line writing under it; the survey across the bottom."""
    cards = list(sl.get("cards") or ["Se anota en vivo"] * 3)[:3]
    label, survey = sl.get("label", "Reflexión"), sl.get("survey")
    x, y, w, h = _wq_zone()
    sh = 140 if survey else 0
    ch = (h - sh - (28 if survey else 0) - 2 * 20) / 3
    g, parts = [glow(x + w / 2, y + h / 2, max(w, h) * .55, "var(--brand)", .35)], []
    for k, text in enumerate(cards):
        cy_ = y + k * (ch + 20)
        col = _WP_COLS[k % len(_WP_COLS)]
        num = f"0{k + 1}"
        face = (T(x + 24, cy_ + 42, num, 22, "var(--c4)", W6)
                + _wp_text(x + 24, cy_ + ch / 2 + 10, text, w - 48, ch - 80, (26, 24, 22, 20)))
        write = (f'<path d="M{x + 24} {cy_ + ch - 22:.1f} H{x + w - 24}" pathLength="1" stroke-dasharray="1" fill="none" '
                 f'stroke="{col}" stroke-width="2" stroke-linecap="round">'
                 f'{beat("stroke-dashoffset", [(0, 1), (.08 + k * .1, 1), (.4 + k * .1, 0), (.96, 0), (1, 1)])}</path>')
        cover = (card(x, cy_, w, ch, "var(--dim)", col, 16, 1.5, 'stroke-dasharray="7 7"')
                 + f'<rect x="{x}" y="{cy_:.1f}" width="{w}" height="{ch:.1f}" rx="16" fill="none" stroke="{col}" stroke-width="3">'
                 + beat("stroke-opacity", [(0, .1), (k / 3, .1), (k / 3 + .06, 1), (k / 3 + .26, 1), (k / 3 + .32, .1), (1, .1)]) + '</rect>'
                 + T(x + 24, cy_ + 42, num, 22, "var(--c4)", W6)
                 + TC(f"{x + w / 2:.1f}", f"{cy_ + ch / 2 + 10:.1f}", f"{label} {k + 1}", fit(f"{label} {k + 1}", 30, w - 48, "reflection label", floor=20),
                      "var(--white)", W6))
        c = (card(x, cy_, w, ch, "var(--card)", col, 16, 2) + f'<g class="reveal-on">{face}{write}</g>'
             + f'<g class="reveal-off">{cover}</g>'
             + f'<rect x="{x}" y="{cy_:.1f}" width="{w}" height="{ch:.1f}" rx="16" fill="var(--ink)" opacity="0"/>')
        parts.append(f'<g data-reveal="{k}">{c}</g>')
    if survey:
        s_label, s_text = survey
        sy = y + h - sh
        lw = min(280, bold_width(_(str(s_label)), 22, current_factor()) + 48)
        box = (card(x, sy, w, sh, "var(--card)", "var(--c4)", 18, 2)
               + f'<rect x="{x}" y="{sy}" width="{w}" height="{sh}" rx="18" fill="none" stroke="var(--c4)" stroke-width="4" opacity=".5">'
               + loop("stroke-opacity", ".1;.8;.1", 3) + '</rect>'
               + pill(x + 24 + lw / 2, sy + sh / 2, s_label, "var(--c4)", ctx, 22, lw, "survey label")
               + _wp_text(x + 48 + lw, sy + sh / 2, s_text, w - lw - 100, sh - 24, (24, 22, 20), lines_max=3)
               + f'<circle cx="{x + w - 30}" cy="{sy + sh / 2}" r="8" fill="var(--c4)">{loop("opacity", "1;.2;1", 2)}</circle>')
        parts.append(box)
    g.append(seq(parts, .1, .5, 16))
    return portrait_mark("".join(g)), D, FREEZE

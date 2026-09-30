"""Group A: slides 1-3 of the energía deck. Three loops, one arc.
m01_portada  - the panorama and the promise: operation, business decisions and their clients' business, one system;
               three unexpected events each get a business response and the clients never stop.
m02_afuera   - from outside: public sources feed our notebook, a hypothesis comes out, and the questions cross into
               the inside, which is theirs to tell.
m03_mecanismo - the mechanism behind slide 1, on one compressor: early signal, connected data, three decisions, risk
               defused and the line keeps running (slide 4 shows the same line when nobody looks).
Equipment, decisions and sources are drawn by position, never by text, so every language keeps the same art.
Portrait-aware (0.5.0): under ORIENT() == "portrait" each scene hands over to its _p0N_* twin, which stacks the same
story in ART_ZONE on the 900x1600 stage with labels of 20 px or more; the desktop output stays byte-identical."""


def _n01_on(a, b=1.0, f=.02):
    """Opacity 1 between fractions a and b of the loop; b >= .97 holds until the loop resets."""
    if b >= .97:
        return beat("opacity", [(0, 0), (a, 0), (a + f, 1), (.97, 1), (1, 0)])
    return beat("opacity", [(0, 0), (a, 0), (a + f, 1), (b, 1), (b + f, 0), (1, 0)])


def _n01_tr(pairs):
    """A translate loop with explicit times: pairs = [(fraction, "dx dy")] from 0 to 1."""
    kt = ";".join(f"{t:.3f}" for t, _ in pairs)
    return (f'<animateTransform attributeName="transform" type="translate" values="{";".join(v for _, v in pairs)}" '
            f'keyTimes="{kt}" dur="{D}s" repeatCount="indefinite"/>')


def _n01_arc_y(x, r, cx=1190, cy=1330):
    return cy - math.sqrt(r * r - (x - cx) ** 2)


def _n01_badge(x, y, n, lit_at, ctx):
    """A HUD step number: outlined, then filled from lit_at to the reset."""
    off = beat("opacity", [(0, 1), (lit_at, 1), (lit_at + .02, 0), (.97, 0), (1, 1)])
    return (f'<g>{off}<circle cx="{x}" cy="{y}" r="13" fill="var(--ink)" stroke="var(--c4)" stroke-width="1.5"/>' + TC(x, y + 5.5, n, 15, "var(--c4)", W6) + '</g>'
            + f'<g>{_n01_on(lit_at)}<circle cx="{x}" cy="{y}" r="13" fill="var(--c4)"/>' + TC(x, y + 5.5, n, 15, ctx.brand.on("var(--c4)"), W6) + '</g>')


# ---------------------------------------------------------------- glyphs (drawn around 0,0)
def _n01_equip(k, col="var(--c2)", live=True):
    """Station k: 0 turbina, 1 compresor, 2 bomba, 3 válvula."""
    sw = f'fill="none" stroke="{col}" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"'
    if k == 0:
        blades = "".join(f'<path transform="rotate({a})" d="M0 -5 C7 -9 9 -16 6 -22 L1 -23 C3 -16 2 -10 0 -5 Z" fill="{col}" opacity=".85"/>'
                         for a in range(0, 360, 60))
        return f'<circle r="25" {sw}/><g>{spin(0, 0, 3.2) if live else ""}{blades}</g><circle r="4.5" fill="{col}"/>'
    if k == 1:
        cyl = "".join(f'<rect x="{x0}" y="-21" width="15" height="21" rx="3" {sw}/><path d="M{x0 - 2} -24 H{x0 + 17}" {sw}/>'
                      + "".join(f'<path d="M{x0 + 3} {yy} H{x0 + 12}" {sw} opacity=".7"/>' for yy in (-15, -9, -4))
                      for x0 in (-19, 4))
        return cyl + f'<rect x="-25" y="0" width="50" height="15" rx="4" {sw}/><path d="M-29 20 H29" {sw}/>'
    if k == 2:
        imp = "".join(f'<path transform="rotate({a})" d="M0 0 Q5 -4 4 -10" {sw}/>' for a in (0, 120, 240))
        return (f'<circle cx="-2" cy="4" r="15" {sw}/><path d="M6 -8 V-23 H17 M-30 4 H-17 M-15 20 L-19 25 H15 L11 20" {sw}/>'
                f'<g transform="translate(-2 4)"><g>{spin(0, 0, 2.4) if live else ""}{imp}</g></g>')
    return (f'<path d="M-21 -11 L21 11 V-11 L-21 11 Z" {sw}/><path d="M-30 0 H-21 M21 0 H30 M0 0 V-19" {sw}/>'
            f'<ellipse cx="0" cy="-21" rx="12" ry="3.5" {sw}/>')


def _n01_decision(k, col="var(--c2)"):
    """Business decision k: 0 compras (cart), 1 bodega (warehouse), 2 mantenimiento (gear)."""
    sw = f'fill="none" stroke="{col}" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"'
    if k == 0:
        return f'<path d="M-17 -11 H-11 L-6 5 H11 L15 -6 H-9" {sw}/><circle cx="-3" cy="11" r="2.5" {sw}/><circle cx="9" cy="11" r="2.5" {sw}/>'
    if k == 1:
        return f'<path d="M-17 -1 L0 -14 L17 -1" {sw}/><rect x="-13" y="-1" width="26" height="15" rx="1" {sw}/><rect x="-5" y="5" width="10" height="9" {sw}/>'
    teeth = "".join(f'<rect x="-2.5" y="-15.5" width="5" height="6" rx="1" fill="{col}" transform="rotate({a})"/>' for a in range(0, 360, 45))
    return teeth + f'<circle r="10" {sw}/><circle r="3.5" {sw}/>'


def _n01_source(k, col="var(--c2)"):
    """Public source k: 0 web page, 1 press, 2 public data."""
    sw = f'fill="none" stroke="{col}" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"'
    if k == 0:
        return f'<rect x="-13" y="-10" width="26" height="20" rx="3" {sw}/><path d="M-13 -4 H13" {sw}/><circle cx="-9" cy="-7" r="1" fill="{col}"/><path d="M-8 2 H8 M-8 6 H3" {sw}/>'
    if k == 1:
        return f'<path d="M-12 -10 H10 V10 H-10 Q-13 10 -13 7 V-4 H-12 Z" {sw}/><rect x="-8" y="-6" width="7" height="6" {sw}/><path d="M2 -5 H7 M2 -1 H7 M-8 4 H7" {sw}/>'
    return f'<path d="M-13 11 H13" {sw}/><rect x="-10" y="1" width="5" height="9" {sw}/><rect x="-2" y="-5" width="5" height="15" {sw}/><rect x="6" y="-10" width="5" height="20" {sw}/>'


def _n01_client(k, col="var(--c2)"):
    """Their clients' business k (baseline at y 0): 0 oil and gas (derrick), 1 energy (pylon), 2 industry (factory).
    Their lights breathe and never go out: the promise of the cover."""
    sw = f'fill="none" stroke="{col}" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"'
    lit = lambda ph: loop("opacity", ".55;1;.55", 3.4, ph)
    if k == 0:
        return (f'<path d="M-20 0 L-4 -72 H4 L20 0 M-28 0 H28 M-16 -16 L13 -30 M16 -16 L-13 -30 M-12 -32 L9 -46 M12 -32 L-9 -46 M-8 -48 L6 -60 M8 -48 L-6 -60" {sw}/>'
                f'<circle cx="0" cy="-77" r="3.5" fill="var(--c4)">{lit(0)}</circle>')
    if k == 1:
        return (f'<path d="M-16 0 L-5 -70 H5 L16 0 M-26 -58 H26 M-19 -42 H19 M-12 -20 L10 -40 M12 -20 L-10 -40 M-28 0 H28" {sw}/>'
                + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="var(--c4)">{lit(j * .6)}</circle>' for j, (x, y) in enumerate(((-24, -52), (24, -52), (-17, -36), (17, -36)))))
    return (f'<path d="M-36 0 V-28 L-22 -40 V-28 L-8 -40 V-28 L6 -40 V-28 H18 V-66 H28 V0 Z" fill="var(--card)" stroke="{col}" stroke-width="1.6" stroke-linejoin="round"/>'
            + "".join(f'<rect x="{x}" y="-19" width="8" height="8" rx="1.5" fill="var(--c4)">{lit(j * .5)}</rect>' for j, x in enumerate((-30, -16, -2)))
            + f'<rect x="20" y="-19" width="6" height="10" rx="1.5" fill="var(--c4)">{lit(1.4)}</rect>')


def _n01_lens(r=20):
    return (f'<circle r="{r}" fill="var(--c4)" fill-opacity=".08" stroke="var(--c4)" stroke-width="2.2"/>'
            f'<path d="M{r * .72:.1f} {r * .72:.1f} L{r * 1.45:.1f} {r * 1.45:.1f}" stroke="var(--c4)" stroke-width="4" stroke-linecap="round"/>')


# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
from aula.svg import wrap as _p01_wrap


def _p01_chars(text, size, room):
    """The widest wrap (in characters) whose every line fits room units at size."""
    t = _(str(text))
    for n in range(40, 5, -1):
        if all(bold_width(ln, size, current_factor()) <= room for ln in _p01_wrap(t, n)):
            return n
    return 6


def _p01_portada(sl, ctx):
    """m01 on the 900x1600 stage, the same sky, horizon and ground stacked down the art zone: the three decisions on
    top, connected data and the gas line with its four stations under them, their clients' business at the bottom,
    lights always on. Same three events answered, same frozen frame; labels painted after all the art."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    cx, CY, R_PIPE, R_BUS = zx + zw / 2, zy + 1090, 700, 830
    ay = lambda x, r: CY - math.sqrt(r * r - (x - cx) ** 2)
    xs = [cx - 315, cx - 105, cx + 105, cx + 315]
    ys = [ay(x, R_PIPE) for x in xs]
    dxs = [cx - 275, cx, cx + 275]
    dy0, dh, dw = zy + 16, 138, 250
    bus_y = lambda x: ay(x, R_BUS)
    arc = lambda r, x0, x1: f"M{x0} {ay(x0, r):.1f} A{r} {r} 0 0 1 {x1} {ay(x1, r):.1f}"
    art, text = [glow(cx, zy + 360, 480, "var(--brand)", .6), glow(cx, zy + 540, 420, "var(--c4)", .12)], []
    ground = "".join(f'<path d="{arc(r, cx - w, cx + w)}" fill="none" stroke="var(--c2)" stroke-width="1.4" opacity="{op}"/>'
                     for r, w, op in ((560, 400, .16), (480, 360, .11), (400, 300, .07)))
    ground += "".join(f'<path d="M{cx + (bx - cx) * .28:.0f} {zy + 520} L{bx} {zy + 860}" stroke="var(--c2)" stroke-width="1" opacity=".07"/>'
                      for bx in range(int(zx), int(zx + zw) + 1, 117))
    art.append(land(ground, .1, .6, 0))
    # connected data: the bus arc and its threads
    b0, b1 = zx + 40, zx + zw - 40
    bus = (f'<path d="{arc(R_BUS, b0, b1)}" fill="none" stroke="var(--c2)" stroke-width="22" opacity=".05"/>'
           f'<path d="{arc(R_BUS, b0, b1)}" fill="none" stroke="var(--c2)" stroke-width="1.8" opacity=".55"/>'
           f'<path d="{arc(R_BUS, b0, b1)}" fill="none" stroke="var(--c4)" stroke-width="2.4" stroke-dasharray="2 14" opacity=".8">{loop("stroke-dashoffset", "0;-32", 1.8)}</path>')
    threads = "".join(f'<path d="M{x} {y - 50:.1f} V{bus_y(x):.1f}" stroke="var(--c2)" stroke-width="1.4" opacity=".5"/>' for x, y in zip(xs, ys))
    threads += "".join(f'<path d="M{x} {dy0 + dh} V{bus_y(x):.1f}" stroke="var(--c2)" stroke-width="1.4" opacity=".5"/>' for x in dxs)
    art.append(land(bus + threads, .45, .6, 0))
    text.append(land(TC(f"{cx + 140:.1f}", f"{bus_y(cx) - 14:.1f}", sl["link"], fit(sl["link"], 21, 200, "portada link", floor=18), "var(--c4)", W6), .45, .6, 0))
    # the gas line and the offtakes that feed their clients
    pipe = arc(R_PIPE, zx + 40, zx + zw - 40)
    art.append(f'<path d="{pipe}" fill="none" stroke="var(--c4)" stroke-width="54" stroke-linecap="round" opacity=".06"/>'
               f'<path d="{pipe}" fill="none" stroke="var(--line)" stroke-width="16" stroke-linecap="round"/>')
    art.append(trace(pipe, "var(--c2)", 1.8, .05, .8, 'opacity=".5"'))
    art.append(f'<path d="{pipe}" fill="none" stroke="var(--c4)" stroke-width="4" stroke-dasharray="8 18">{loop("stroke-dashoffset", "0;-52", 1.6)}</path>')
    art.append(f'<g>{token("var(--c4)", 6)}{move(pipe, [(0, 0), (1, 1)], 4)}</g>')
    ox, gy = [cx - 210, cx, cx + 210], zy + 760
    for k, x in enumerate(ox):
        d = f"M{x} {ay(x, R_PIPE) + 7:.1f} V{gy - 132}"
        art.append(land(f'<path d="{d}" stroke="var(--line)" stroke-width="8" stroke-linecap="round"/>'
                        f'<path d="{d}" fill="none" stroke="var(--c4)" stroke-width="3" stroke-dasharray="5 14">{loop("stroke-dashoffset", "0;-38", 1.4)}</path>', .9 + k * .1, .5, 0))
    # the operation: four stations on the line
    for k, (x, y) in enumerate(zip(xs, ys)):
        art.append(pop(card(-50, -50, 100, 100, "var(--card)", "var(--c2)", 20, 1.8) + f'<g transform="scale(1.25)">{_n01_equip(k)}</g>', x, y, .3 + k * .12, .45))
    # their names fade in together under the stations (one entrance keeps the scene under its 35 KB)
    text.append(land("".join(TC(x, f"{y + 82:.1f}", name, fit(name, 22, 190, "portada station", floor=18), "var(--muted)", W6)
                             for x, y, name in zip(xs, ys, sl["stations"])), .45, .6, 0))
    # the business: three decisions in the sky
    for k, (x, name) in enumerate(zip(dxs, sl["decisions"])):
        at = .5 + .12 * k
        art.append(land(card(x - dw / 2, dy0, dw, dh, "var(--card)", "var(--c2)", 18, 1.4)
                        + f'<g transform="translate({x} {dy0 + 40}) scale(1.3)">{_n01_decision(k)}</g>', at, .5, -16))
        text.append(land(TCW(x, dy0 + 92, name, _p01_chars(name, 22, dw - 28), 22, "var(--white)", W6, 1.2), at, .5, -16))
    # the ground: their clients' business, always lit
    art.append(land("".join(glow(x, gy - 50, 100, "var(--c4)", .16) + f'<g transform="translate({x} {gy}) scale(1.5)">{_n01_client(k)}</g>'
                            for k, x in enumerate(ox)), 1.0, .6, 16))
    lab = sl["clients"]
    s = fit(lab, 24, 560, "portada clients", floor=18)
    lw = bold_width(_(str(lab)), s, current_factor())
    dot = cx - lw / 2 - 20
    text.append(land(TC(f"{cx + 12:.1f}", gy + 70, lab, s, "var(--c4)", W6)
                     + f'<circle cx="{dot + 10:.1f}" cy="{gy + 62}" r="6" fill="{ok}"/>'
                     + f'<circle cx="{dot + 10:.1f}" cy="{gy + 62}" r="6" fill="none" stroke="{ok}" stroke-width="1.8">{loop("r", "6;15;6", 2.4)}{loop("opacity", "1;0;1", 2.4)}</circle>',
                     1.35, .5, 10))
    # the unexpected, answered: (station, decision, start) for imprevisto, urgencia, riesgo
    events = [(0, 1, .14), (2, 0, .38), (1, 2, .62)]
    halos, marks, chips, lit, tokens = [], [], [], [], []
    for (si, di, t0), word in zip(events, sl["events"]):
        x, y = xs[si], ys[si]
        up, lit_t, down, done = t0 + .03, t0 + .09, t0 + .11, t0 + .16
        path = f"M{x} {y - 50:.1f} V{bus_y(x):.1f} A{R_BUS} {R_BUS} 0 0 {1 if dxs[di] > x else 0} {dxs[di]} {bus_y(dxs[di]):.1f} V{dy0 + dh}"
        halos.append(f'<g>{_n01_on(t0, done)}<rect x="{x - 58}" y="{y - 58:.1f}" width="116" height="116" rx="26" fill="none" stroke="var(--c5)" stroke-width="2.4">'
                     f'{loop("stroke-opacity", ".25;1;.25", 1)}</rect></g>')
        marks.append(f'<g>{_n01_on(done)}<rect x="{x - 56}" y="{y - 56:.1f}" width="112" height="112" rx="25" fill="none" stroke="{ok}" stroke-width="2.2"/>'
                     f'<circle cx="{x + 46}" cy="{y - 46:.1f}" r="13" fill="{ok}"/>' + check(x + 46, y - 45.5, .65, "var(--ink)") + '</g>')
        cy_ = y - 50 - 34
        chips.append(f'<g>{_n01_on(t0, done)}' + pill(x, cy_, word, "var(--c5)", ctx, 20, 200, "portada event", 16) + '</g>'
                     f'<g>{_n01_on(done)}' + pill(x, cy_, word, ok, ctx, 20, 200, "portada event", 16) + '</g>')
        dx_ = dxs[di]
        lit.append(f'<g>{_n01_on(lit_t)}<rect x="{dx_ - dw / 2 - 3}" y="{dy0 - 3}" width="{dw + 6}" height="{dh + 6}" rx="20" fill="none" stroke="var(--c4)" stroke-width="2.4"/>'
                   f'<circle cx="{dx_ + dw / 2 - 22}" cy="{dy0 + 22}" r="13" fill="{ok}"/>' + check(dx_ + dw / 2 - 22, dy0 + 22.5, .65, "var(--ink)") + '</g>'
                   f'<rect x="{dx_ - dw / 2}" y="{dy0}" width="{dw}" height="{dh}" rx="18" fill="var(--c4)" opacity="0">'
                   f'{beat("opacity", [(0, 0), (lit_t, 0), (lit_t + .01, .16), (lit_t + .08, 0), (1, 0)])}</rect>')
        tokens.append(f'<g>{_n01_on(up, lit_t, .01)}{token("var(--c5)", 7)}{move(path, [(0, 0), (up, 0), (lit_t, 1), (1, 1)], D)}</g>'
                      f'<g>{_n01_on(down, done, .01)}{token(ok, 7)}{move(path, [(0, 1), (down, 1), (done, 0), (1, 0)], D)}</g>')
    art.append(land("".join(halos + marks + lit), 1.2, .4, 0) + "".join(tokens))
    return portrait_mark("".join(art) + "".join(text) + "".join(chips)), D, FREEZE


# ---------------------------------------------------------------- slide 1: the panorama and the promise
@register("scene", "m01_portada")
def sc_m01_portada(sl, ctx):
    """Sky, horizon, ground. In the sky, the business decisions (compras, bodega, mantenimiento proactivo); on the
    horizon, the operation (turbina, compresor, bomba, válvula) on one gas line; on the ground, their clients' business,
    fed by that line, lights always on. Connected data joins sky and horizon. Loop: three unexpected events (imprevisto
    at the turbine, urgencia at the pump, riesgo at the compressor) each send a red signal up to the decision that
    answers it and get a green response back; the clients never flicker. Frozen frame: all three answered."""
    if ORIENT() == "portrait":
        return _p01_portada(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    cx, R_PIPE, R_BUS = 1190, 900, 1030
    xs = [905, 1095, 1285, 1475]
    ys = [_n01_arc_y(x, R_PIPE) for x in xs]
    dxs = [960, 1190, 1420]
    dy0, dh, dw = 116, 112, 210
    bus_y = lambda x: _n01_arc_y(x, R_BUS)
    arc = lambda r, x0, x1: f"M{x0} {_n01_arc_y(x0, r):.1f} A{r} {r} 0 0 1 {x1} {_n01_arc_y(x1, r):.1f}"
    g = [glow(cx, 430, 480, "var(--brand)", .6), glow(cx, 560, 420, "var(--c4)", .12)]
    # the ground: curved horizon lines and rays toward it, faint
    ground = "".join(f'<path d="{arc(r, x0, 2 * cx - x0)}" fill="none" stroke="var(--c2)" stroke-width="1.2" opacity="{op}"/>'
                     for r, x0, op in ((800, 850, .16), (690, 900, .11), (590, 960, .07)))
    ground += "".join(f'<path d="M{cx + (bx - cx) * .28:.0f} 560 L{bx} 820" stroke="var(--c2)" stroke-width="1" opacity=".07"/>' for bx in range(700, 1700, 110))
    g.append(land(ground, .1, .6, 0))
    # connected data: the bus arc and its threads (up from each station, down from each decision)
    bus = (f'<path d="{arc(R_BUS, 860, 1520)}" fill="none" stroke="var(--c2)" stroke-width="18" opacity=".05"/>'
           f'<path d="{arc(R_BUS, 860, 1520)}" fill="none" stroke="var(--c2)" stroke-width="1.5" opacity=".55"/>'
           f'<path d="{arc(R_BUS, 860, 1520)}" fill="none" stroke="var(--c4)" stroke-width="2" stroke-dasharray="2 14" opacity=".8">{loop("stroke-dashoffset", "0;-32", 1.8)}</path>')
    threads = "".join(f'<path d="M{x} {y - 42:.1f} V{bus_y(x):.1f}" stroke="var(--c2)" stroke-width="1.2" opacity=".5"/>' for x, y in zip(xs, ys))
    threads += "".join(f'<path d="M{x} {dy0 + dh} V{bus_y(x):.1f}" stroke="var(--c2)" stroke-width="1.2" opacity=".5"/>' for x in dxs)
    link = T(1305, 293, sl["link"], fit(sl["link"], 15, 130, "portada link"), "var(--c4)", 'text-anchor="middle" font-weight="600"')
    g.append(land(bus + threads + link, .45, .6, 0))
    # the gas line on the horizon and the offtakes that feed their clients
    pipe = arc(R_PIPE, 850, 1530)
    g.append(f'<path d="{pipe}" fill="none" stroke="var(--c4)" stroke-width="46" stroke-linecap="round" opacity=".06"/>'
             f'<path d="{pipe}" fill="none" stroke="var(--line)" stroke-width="14" stroke-linecap="round"/>')
    g.append(trace(pipe, "var(--c2)", 1.5, .05, .8, 'opacity=".5"'))
    g.append(f'<path d="{pipe}" fill="none" stroke="var(--c4)" stroke-width="3.5" stroke-dasharray="8 18">{loop("stroke-dashoffset", "0;-52", 1.6)}</path>')
    g.append(f'<g>{token("var(--c4)", 5)}{move(pipe, [(0, 0), (1, 1)], 4)}</g>')
    ox, oy = [1000, 1190, 1380], 648
    for k, x in enumerate(ox):
        d = f"M{x} {_n01_arc_y(x, R_PIPE) + 6:.1f} V{oy}"
        g.append(land(f'<path d="{d}" stroke="var(--line)" stroke-width="7" stroke-linecap="round"/>'
                      f'<path d="{d}" fill="none" stroke="var(--c4)" stroke-width="2.5" stroke-dasharray="5 14">{loop("stroke-dashoffset", "0;-38", 1.4)}</path>', .9 + k * .1, .5, 0))
    # the operation: four stations on the line
    for k, (x, y, name) in enumerate(zip(xs, ys, sl["stations"])):
        st = card(-42, -42, 84, 84, "var(--card)", "var(--c2)", 18, 1.5) + _n01_equip(k)
        st += TC(0, 66, name, fit(name, 16, 150, "portada station"), "var(--muted)", W6)
        g.append(pop(st, x, y, .3 + k * .12, .45))
    # the business: three decisions in the sky
    decs = []
    for k, (x, name) in enumerate(zip(dxs, sl["decisions"])):
        c = card(x - dw / 2, dy0, dw, dh, "var(--card)", "var(--c2)", 16, 1.2) + f'<g transform="translate({x} {dy0 + 34})">{_n01_decision(k)}</g>'
        c += TCW(x, dy0 + 76, name, 14, 17, "var(--white)", W6, 1.2)
        decs.append(c)
    g.append(seq(decs, .5, .5, -16))
    # the ground: their clients' business, always lit
    cl = "".join(glow(x, 712, 80, "var(--c4)", .16) + f'<g transform="translate({x} 750) scale(1.15)">{_n01_client(k)}</g>' for k, x in enumerate(ox))
    g.append(land(cl, 1.0, .6, 16))
    lab = sl["clients"]
    s = fit(lab, 17, 420, "portada clients")
    lw = bold_width(_(str(lab)), s, current_factor())
    dot = cx - lw / 2 - 16
    g.append(land(T(cx + 10, 792, lab, s, "var(--c4)", 'text-anchor="middle" font-weight="600"')
                  + f'<circle cx="{dot + 10:.1f}" cy="786" r="5" fill="{ok}"/>'
                  + f'<circle cx="{dot + 10:.1f}" cy="786" r="5" fill="none" stroke="{ok}" stroke-width="1.5">{loop("r", "5;13;5", 2.4)}{loop("opacity", "1;0;1", 2.4)}</circle>',
                  1.35, .5, 10))
    # the unexpected, answered: (station, decision, start) for imprevisto, urgencia, riesgo
    events = [(0, 1, .14), (2, 0, .38), (1, 2, .62)]
    halos, marks, chips, lit, tokens = [], [], [], [], []
    for (si, di, t0), word in zip(events, sl["events"]):
        x, y = xs[si], ys[si]
        up, lit_t, down, done = t0 + .03, t0 + .09, t0 + .11, t0 + .16
        path = (f"M{x} {y - 42:.1f} V{bus_y(x):.1f} A{R_BUS} {R_BUS} 0 0 {1 if dxs[di] > x else 0} {dxs[di]} {bus_y(dxs[di]):.1f} V{dy0 + dh}")
        halos.append(f'<g>{_n01_on(t0, done)}<rect x="{x - 49}" y="{y - 49:.1f}" width="98" height="98" rx="22" fill="none" stroke="var(--c5)" stroke-width="2">'
                     f'{loop("stroke-opacity", ".25;1;.25", 1)}</rect></g>')
        marks.append(f'<g>{_n01_on(done)}<rect x="{x - 47}" y="{y - 47:.1f}" width="94" height="94" rx="21" fill="none" stroke="{ok}" stroke-width="1.8"/>'
                     f'<circle cx="{x + 38}" cy="{y - 38:.1f}" r="11" fill="{ok}"/>' + check(x + 38, y - 37.5, .55, "var(--ink)") + '</g>')
        cy_ = y - 42 - 32
        chips.append(f'<g>{_n01_on(t0, done)}' + pill(x, cy_, word, "var(--c5)", ctx, 15, 170, "portada event", 14) + '</g>'
                     f'<g>{_n01_on(done)}' + pill(x, cy_, word, ok, ctx, 15, 170, "portada event", 14) + '</g>')
        dx_ = dxs[di]
        lit.append(f'<g>{_n01_on(lit_t)}<rect x="{dx_ - dw / 2 - 3}" y="{dy0 - 3}" width="{dw + 6}" height="{dh + 6}" rx="18" fill="none" stroke="var(--c4)" stroke-width="2"/>'
                   f'<circle cx="{dx_ + dw / 2 - 20}" cy="{dy0 + 20}" r="11" fill="{ok}"/>' + check(dx_ + dw / 2 - 20, dy0 + 20.5, .55, "var(--ink)") + '</g>'
                   f'<rect x="{dx_ - dw / 2}" y="{dy0}" width="{dw}" height="{dh}" rx="16" fill="var(--c4)" opacity="0">'
                   f'{beat("opacity", [(0, 0), (lit_t, 0), (lit_t + .01, .16), (lit_t + .08, 0), (1, 0)])}</rect>')
        tokens.append(f'<g>{_n01_on(up, lit_t, .01)}{token("var(--c5)", 6)}{move(path, [(0, 0), (up, 0), (lit_t, 1), (1, 1)], D)}</g>'
                      f'<g>{_n01_on(down, done, .01)}{token(ok, 6)}{move(path, [(0, 1), (down, 1), (done, 0), (1, 0)], D)}</g>')
    g.append(land("".join(halos + marks + lit), 1.2, .4, 0) + "".join(chips) + "".join(tokens))
    return "".join(g), D, FREEZE


def _p02_afuera(sl, ctx):
    """m02 on the 900x1600 stage: the three sources and our notebook side by side on top, the hypothesis across the
    zone under them, the inside (their operation, a ghost) at the bottom with a question over every station. Same loop
    and frozen frame; labels painted after all the art."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    X1 = zx + zw
    art, text = [glow(zx + zw / 2, zy + 360, 470, "var(--brand)", .55)], []
    sw, shh = 440, 74
    sy = [zy + 14 + k * 90 for k in range(3)]
    bx, by, bw, bh = zx + sw + 36, zy + 8, X1 - zx - sw - 36, 270
    for k, (y, lab) in enumerate(zip(sy, sl["layers"])):
        at = .1 + .12 * k
        art.append(land(card(zx, y, sw, shh, "var(--card)", "var(--c2)", 14, 1.4) + f'<g transform="translate({zx + 34} {y + shh / 2}) scale(1.3)">{_n01_source(k)}</g>', at, .45, 14))
        text.append(land(T(zx + 68, y + shh / 2 + 8, lab, fit(lab, 21, sw - 84, "afuera source", floor=18), "var(--white)", W6), at, .45, 14))
    ny = lambda k: by + 70 + k * 64
    links = "".join(f'<path d="M{zx + sw} {y + shh / 2} C{zx + sw + 20} {y + shh / 2} {bx - 20} {ny(k)} {bx} {ny(k)}" fill="none" stroke="var(--c2)" stroke-width="1.8" opacity=".6"/>'
                    for k, y in enumerate(sy))
    rings = "".join(f'<circle cx="{bx + 20}" cy="{by + 30 + k * 40}" r="6.5" fill="none" stroke="var(--c2)" stroke-width="2"/>' for k in range(6))
    art.append(land(links + card(bx, by, bw, bh, "var(--card)", "var(--c2)", 16, 2) + rings, .35, .5))
    text.append(land(T(bx + 44, by + 42, sl["book"], fit(sl["book"], 22, bw - 90, "afuera notebook", floor=18), "var(--white)", W6), .35, .5))
    read = [.04, .13, .22]
    for k, (y, t) in enumerate(zip(sy, read)):
        art.append(f'<g>{_n01_on(t)}<rect x="{zx - 1}" y="{y - 1}" width="{sw + 2}" height="{shh + 2}" rx="15" fill="none" stroke="var(--c4)" stroke-width="2.4"/></g>')
        pth = f"M{zx + sw} {y + shh / 2} C{zx + sw + 20} {y + shh / 2} {bx - 20} {ny(k)} {bx} {ny(k)}"
        art.append(f'<g>{_n01_on(t + .03, t + .07, .01)}{token("var(--c4)", 6)}{move(pth, [(0, 0), (t + .03, 0), (t + .07, 1), (1, 1)], D)}</g>')
        para = "".join(f'<rect x="{bx + 44}" y="{ny(k) + j * 18 - 8}" width="{(bw - 70) * (.9 if j == 0 else .6):.0f}" height="8" rx="4" fill="var(--c2)" opacity=".6"/>' for j in range(2))
        art.append(f'<g>{_n01_on(t + .07)}{para}</g>')
    lx = zx + sw - 40
    stops = [(0, f"{lx} {sy[0] + 37}"), (.06, f"{lx} {sy[0] + 37}"), (.11, f"{lx} {sy[1] + 37}"), (.15, f"{lx} {sy[1] + 37}"),
             (.20, f"{lx} {sy[2] + 37}"), (.25, f"{lx} {sy[2] + 37}"), (.31, f"{bx + bw - 50} {by + bh - 50}"), (.97, f"{bx + bw - 50} {by + bh - 50}"), (1, f"{lx} {sy[0] + 37}")]
    art.append(land(f'<g>{_n01_tr(stops)}{_n01_lens(24)}</g>', .6, .4, 0))
    art.append(f'<g>{_n01_on(.31)}<g>{loop("opacity", ".4;1;.4", 2.2)}{spark(bx + bw - 30, by + 34, .75, "var(--c4)")}</g></g>')
    # the hypothesis comes out of the notebook
    hy, hh = by + bh + 36, 118
    hyp = (card(zx, hy, zw, hh, "var(--card)", "var(--c4)", 18, 2.2) + T(zx + 26, hy + 40, sl["case_label"], 20, "var(--c4)", W6)
           + _p01_text2(zx + 26, hy + 80, sl["case"], 24, zw - 52))
    tag = f'<g>{_n01_on(.47)}<g>{loop("opacity", ".8;1;.8", 2.6)}' + pill(X1 - 120, hy, sl["tag"], "var(--c4)", ctx, 20, 220, "afuera tag") + '</g></g>'
    text.append(f'<g>{_n01_on(.38, 1, .04)}<g>{_n01_tr([(0, "0 -110"), (.38, "0 -110"), (.44, "0 0"), (1, "0 0")])}{hyp}</g></g>' + tag)
    # the inside: theirs. A ghost of the operation behind a dashed line
    iy, ih = hy + hh + 50, 370
    gy = iy + 200
    gx = [zx + 100 + k * (zw - 200) / 3 for k in range(4)]
    inside = (card(zx, iy, zw, ih, "var(--dim)", "var(--c2)", 22, 1.8, 'fill-opacity=".45" stroke-dasharray="8 8"')
              + f'<path d="M{zx + 20} {gy} H{X1 - 20}" stroke="var(--c2)" stroke-width="1.8" stroke-dasharray="4 8" opacity=".45"/>')
    for k, x in enumerate(gx):
        inside += (f'<rect x="{x - 46:.1f}" y="{gy - 46}" width="92" height="92" rx="20" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="5 5" opacity=".75"/>'
                   f'<g transform="translate({x:.1f} {gy})" opacity=".45">{_n01_equip(k, live=False)}</g>')
    art.append(land(inside, .5, .55, 16))
    text.append(land(T(zx + 26, iy + ih - 28, sl["inside"], fit(sl["inside"], 21, zw / 2 - 20, "afuera inside", floor=18), "var(--white)", W6), .5, .55, 16))
    ask = sl["ask"]
    text.append(f'<g>{_n01_on(.74)}' + T(X1 - 26, iy + ih - 28, ask, fit(ask, 21, zw / 2 - 40, "afuera ask", floor=18), "var(--c4)", 'text-anchor="end" font-weight="600"') + '</g>')
    qy = iy + 86
    for k, x in enumerate(gx):
        a = .54 + k * .05
        q = (f'<path d="M{x:.1f} {qy + 28} V{gy - 48}" stroke="var(--c4)" stroke-width="1.8" stroke-dasharray="3 4"/>'
             f'<circle cx="{x:.1f}" cy="{qy}" r="26" fill="var(--card)" stroke="var(--c4)" stroke-width="2.2">{loop("stroke-opacity", ".4;1;.4", 2.4, k * .5)}</circle>'
             + TC(f"{x:.1f}", qy + 9, "?", 26, "var(--c4)", W6))
        art.append(f'<g>{_n01_on(a + .04)}<path d="M{zx + zw / 2} {hy + hh} L{x:.1f} {qy - 26}" stroke="var(--c4)" stroke-width="1.4" stroke-dasharray="3 6" opacity=".45"/></g>')
        text.append(f'<g>{_n01_on(a, 1, .015)}<g>{_n01_tr([(0, f"{zx + zw / 2 - x:.1f} -150"), (a, f"{zx + zw / 2 - x:.1f} -150"), (a + .05, "0 0"), (1, "0 0")])}{q}</g></g>')
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


def _p01_text2(x, y, text, size, room):
    """text in one line at the largest size down to 20 that fits room, else wrapped in two at size 20 or more."""
    z = fit(text, size, room, "afuera hypothesis", floor=20)
    if bold_width(_(str(text)), z, current_factor()) <= room:
        return T(x, y, text, z, "var(--white)", W6)
    return TCW(x, y - 12, text, _p01_chars(text, 20, room), 20, "var(--white)", W6, 1.25, "start")


# ---------------------------------------------------------------- slide 2: from outside
@register("scene", "m02_afuera")
def sc_m02_afuera(sl, ctx):
    """Outside, three public sources; a lens reads each one and it drops into our notebook, which fills. A hypothesis
    comes out, marked «por validar». Below the dashed line is the inside: their operation, drawn as a ghost, which we
    cannot see. The hypothesis sends a question to each station: the inside is theirs to tell, we come to ask. Frozen
    frame: sources read, notebook full, the hypothesis waiting to be validated, a question over every station."""
    if ORIENT() == "portrait":
        return _p02_afuera(sl, ctx)
    g = [glow(1190, 420, 470, "var(--brand)", .55)]
    sy = [116, 194, 272]
    bx, by, bw, bh = 1220, 108, 310, 236
    src = []
    for k, (y, lab) in enumerate(zip(sy, sl["layers"])):
        c = card(850, y, 320, 62, "var(--card)", "var(--c2)", 12, 1.2) + f'<g transform="translate(878 {y + 31})">{_n01_source(k)}</g>'
        c += T(906, y + 37, lab, fit(lab, 17, 244, "afuera source"), "var(--white)", W6)
        src.append(c)
    g.append(seq(src, .1, .45, 14))
    links = "".join(f'<path d="M1170 {y + 31} C1196 {y + 31} 1194 {bh / 4 * (k + 1) + by - 12:.0f} 1220 {bh / 4 * (k + 1) + by - 12:.0f}" fill="none" stroke="var(--c2)" stroke-width="1.5" opacity=".6"/>'
                    for k, y in enumerate(sy))
    rings = "".join(f'<circle cx="{bx + 18}" cy="{by + 28 + k * 34}" r="5.5" fill="none" stroke="var(--c2)" stroke-width="1.8"/>' for k in range(6))
    book = card(bx, by, bw, bh, "var(--card)", "var(--c2)", 14, 1.8) + rings + T(bx + 40, by + 38, sl["book"], fit(sl["book"], 18, bw - 60, "afuera notebook"), "var(--white)", W6)
    g.append(land(links + book, .35, .5))
    # the loop: the lens reads each source, a particle drops into the notebook and fills a paragraph
    read = [.04, .13, .22]
    for k, (y, t) in enumerate(zip(sy, read)):
        g.append(f'<g>{_n01_on(t)}<rect x="849" y="{y - 1}" width="322" height="64" rx="13" fill="none" stroke="var(--c4)" stroke-width="2"/></g>')
        ny = bh / 4 * (k + 1) + by - 12
        p = f"M1170 {y + 31} C1196 {y + 31} 1194 {ny:.0f} 1220 {ny:.0f}"
        g.append(f'<g>{_n01_on(t + .03, t + .07, .01)}{token("var(--c4)", 5)}{move(p, [(0, 0), (t + .03, 0), (t + .07, 1), (1, 1)], D)}</g>')
        para = "".join(f'<rect x="{bx + 40}" y="{by + 62 + k * 56 + j * 16}" width="{(bw - 70) * (.9 if j == 0 else .6):.0f}" height="7" rx="3.5" fill="var(--c2)" opacity=".6"/>' for j in range(2))
        g.append(f'<g>{_n01_on(t + .07)}{para}</g>')
    stops = [(0, "1120 147"), (.06, "1120 147"), (.11, "1120 225"), (.15, "1120 225"), (.20, "1120 303"), (.25, "1120 303"),
             (.31, "1478 236"), (.97, "1478 236"), (1, "1120 147")]
    g.append(land(f'<g>{_n01_tr(stops)}{_n01_lens()}</g>', .6, .4, 0))
    g.append(f'<g>{_n01_on(.31)}<g>{loop("opacity", ".4;1;.4", 2.2)}{spark(bx + bw - 28, by + 30, .6, "var(--c4)")}</g></g>')
    # the hypothesis comes out of the notebook
    hy, hh = 376, 92
    hyp = (card(850, hy, 680, hh, "var(--card)", "var(--c4)", 16, 1.8) + T(874, hy + 32, sl["case_label"], 15, "var(--c4)", W6)
           + T(874, hy + 68, sl["case"], fit(sl["case"], 20, 632, "afuera hypothesis"), "var(--white)", W6))
    tag = f'<g>{_n01_on(.47)}<g>{loop("opacity", ".8;1;.8", 2.6)}' + pill(1440, hy, sl["tag"], "var(--c4)", ctx, 15, 200, "afuera tag") + '</g></g>'
    g.append(f'<g>{_n01_on(.38, 1, .04)}<g>{_n01_tr([(0, "90 -90"), (.38, "90 -90"), (.44, "0 0"), (1, "0 0")])}{hyp}</g></g>' + tag)
    # the inside: theirs. A ghost of the operation behind a dashed line
    iy = 500
    inside = (card(850, iy, 680, 300, "var(--dim)", "var(--c2)", 20, 1.5, 'fill-opacity=".45" stroke-dasharray="8 8"')
              + f'<path d="M866 670 H1514" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="4 8" opacity=".45"/>')
    gx = [935, 1105, 1275, 1445]
    for k, x in enumerate(gx):
        inside += (f'<rect x="{x - 36}" y="634" width="72" height="72" rx="16" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="5 5" opacity=".75"/>'
                   f'<g transform="translate({x} 670) scale(.8)" opacity=".45">{_n01_equip(k, live=False)}</g>')
    inside += T(874, 776, sl["inside"], fit(sl["inside"], 17, 300, "afuera inside"), "var(--white)", W6)
    g.append(land(inside, .5, .55, 16))
    ask = sl["ask"]
    g.append(f'<g>{_n01_on(.74)}' + T(1506, 776, ask, fit(ask, 17, 300, "afuera ask"), "var(--c4)", 'text-anchor="end" font-weight="600"') + '</g>')
    for k, x in enumerate(gx):
        a = .54 + k * .05
        q = (f'<path d="M{x} 602 V632" stroke="var(--c4)" stroke-width="1.5" stroke-dasharray="3 4"/>'
             f'<circle cx="{x}" cy="580" r="20" fill="var(--card)" stroke="var(--c4)" stroke-width="1.8">{loop("stroke-opacity", ".4;1;.4", 2.4, k * .5)}</circle>'
             + TC(x, 587, "?", 21, "var(--c4)", W6))
        g.append(f'<g>{_n01_on(a + .04)}<path d="M1190 {hy + hh} L{x} 560" stroke="var(--c4)" stroke-width="1.2" stroke-dasharray="3 6" opacity=".45"/></g>')
        g.append(f'<g>{_n01_on(a, 1, .015)}<g>{_n01_tr([(0, f"{1190 - x} -130"), (a, f"{1190 - x} -130"), (a + .05, "0 0"), (1, "0 0")])}{q}</g></g>')
    return "".join(g), D, FREEZE


def _p01_badge(x, y, n, lit_at, ctx):
    """_n01_badge at phone size (r 18, a 20 px number)."""
    off = beat("opacity", [(0, 1), (lit_at, 1), (lit_at + .02, 0), (.97, 0), (1, 1)])
    return (f'<g>{off}<circle cx="{x}" cy="{y}" r="18" fill="var(--ink)" stroke="var(--c4)" stroke-width="1.8"/>' + TC(x, y + 7, n, 20, "var(--c4)", W6) + '</g>'
            + f'<g>{_n01_on(lit_at)}<circle cx="{x}" cy="{y}" r="18" fill="var(--c4)"/>' + TC(x, y + 7, n, 20, ctx.brand.on("var(--c4)"), W6) + '</g>')


def _p03_mecanismo(sl, ctx):
    """m03 on the 900x1600 stage: the same four numbered steps down the art zone, the numbers in a column on the left:
    1 the signal leaves its band far below the limit, 2 connected data, 3 three decisions side by side, 4 the line with
    the compressor answered in time. Same loop and frozen frame; labels painted after all the art."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    BX, X0, X1 = zx + 12, zx + 44, zx + zw         # the badge column, the blocks' left and right edges
    art, text = [glow(zx + zw / 2, zy + 420, 470, "var(--brand)", .55)], []
    # 1 · the signal
    cy0, ch = zy + 16, 262
    lim, band = cy0 + 116, cy0 + 196                # the limit line, the centre of the normal band
    real = [(X0 + 26 + 56 * k, band + (3, -2, 4, -1, 3, -3, 2)[k]) for k in range(7)] + [(X0 + 424, band - 8), (X0 + 468, band - 20)]
    rd = "M" + " L".join(f"{x} {y}" for x, y in real)
    dx_, dy_ = real[-1]
    tx = X1 - 34                                    # where the projection meets the limit
    proj = f"M{dx_} {dy_} C{dx_ + 110} {dy_ - 36} {tx - 70} {lim + 12} {tx} {lim}"
    art.append(land(card(X0, cy0, X1 - X0, ch, "var(--card)", "var(--c2)", 20, 1.8)
                    + f'<rect x="{X0 + 26}" y="{band - 14}" width="{X1 - X0 - 52}" height="28" rx="5" fill="var(--c2)" opacity=".08"/>'
                    + f'<path d="M{X0 + 26} {lim} H{X1 - 26}" stroke="var(--c5)" stroke-width="1.5" stroke-dasharray="5 6" opacity=".85"/>', .1, .5, 12))
    text.append(land(T(X0 + 26, cy0 + 44, sl["chart"], fit(sl["chart"], 22, 380, "mecanismo chart", floor=18), "var(--muted)", W6)
                     + T(X0 + 26, lim - 10, sl["limit"], 20, "var(--muted)", W6), .1, .5, 12))
    art.append(land(f'<path d="{rd} L{dx_} {band + 18} L{X0 + 26} {band + 18} Z" fill="var(--c3)" opacity=".12"/>', .45, .5, 0) + trace(rd, "var(--c3)", 2.4, .4, .7))
    art.append(f'<g>{token("var(--c4)", 7)}{move(rd, [(0, 0), (.10, 1), (1, 1)], D)}</g>')
    art.append(f'<g>{_n01_on(.10)}<circle cx="{dx_}" cy="{dy_}" r="12" fill="none" stroke="var(--c5)" stroke-width="2">{loop("r", "11;26;11", 2)}</circle></g>')
    by_ = band + 36
    art.append(f'<g>{_n01_on(.13)}<path d="{proj}" fill="none" stroke="var(--c4)" stroke-width="2.2" stroke-dasharray="8 8"/>'
               f'<circle cx="{tx}" cy="{lim}" r="6" fill="none" stroke="var(--c5)" stroke-width="2"/>'
               f'<path d="M{dx_} {by_ - 10} V{by_ + 10} M{tx} {by_ - 10} V{by_ + 10} M{dx_ + 6} {by_} H{tx - 6}" stroke="var(--c4)" stroke-width="1.8"/>'
               f'<path d="M{dx_ + 14} {by_ - 6} L{dx_ + 6} {by_} L{dx_ + 14} {by_ + 6} M{tx - 14} {by_ - 6} L{tx - 6} {by_} L{tx - 14} {by_ + 6}" fill="none" stroke="var(--c4)" stroke-width="1.8" stroke-linecap="round"/></g>')
    text.append(f'<g>{_n01_on(.10)}' + pill(X1 - 140, cy0 + 38, sl["deviation"], "var(--c5)", ctx, 20, 250, "mecanismo deviation", 16) + '</g>'
                + f'<g>{_n01_on(.13)}' + TC((dx_ + tx) / 2, by_ - 12, sl["margin"], fit(sl["margin"], 20, tx - dx_ - 20, "mecanismo margin", floor=18), "var(--c4)", W6) + '</g>'
                + _p01_badge(BX, cy0 + 38, "1", .10, ctx))
    # 2 · connected data
    hx, hy = zx + zw / 2, cy0 + ch + 58
    art.append(land(f'<path d="M{hx} {cy0 + ch} V{hy - 26}" stroke="var(--c2)" stroke-width="1.8" opacity=".7"/>'
                    f'<circle cx="{hx}" cy="{hy}" r="26" fill="var(--card)" stroke="var(--c4)" stroke-width="1.8"/>' + spark(hx, hy, .7, "var(--c4)"), .6, .45, 0))
    text.append(land(T(hx + 40, hy + 8, sl["link"], fit(sl["link"], 22, X1 - hx - 50, "mecanismo link", floor=18), "var(--white)", W6), .6, .45, 0)
                + _p01_badge(BX, hy, "2", .22, ctx))
    art.append(f'<g>{_n01_on(.22)}<circle cx="{hx}" cy="{hy}" r="26" fill="none" stroke="var(--c4)" stroke-width="2.4">{loop("r", "26;42;26", 2)}{loop("opacity", "1;0;1", 2)}</circle></g>')
    drop = f"M{dx_} {dy_} C{dx_} {hy - 30} {hx} {hy - 60} {hx} {hy}"
    art.append(f'<g>{_n01_on(.16, .22, .01)}{token("var(--c4)", 7)}{move(drop, [(0, 0), (.16, 0), (.22, 1), (1, 1)], D)}</g>')
    # 3 · three decisions, side by side
    ky, kh, gap = hy + 74, 134, 16
    kw = (X1 - X0 - 2 * gap) / 3
    kxs = [X0 + k * (kw + gap) for k in range(3)]
    mids = [x + kw / 2 for x in kxs]
    ly, lxs = ky + kh + 150, [X0 + 70 + k * (X1 - X0 - 140) / 3 for k in range(4)]
    c1 = lxs[1]
    fan_out = [f"M{hx} {hy + 26} C{hx} {hy + 50} {m} {ky - 30} {m} {ky}" for m in mids]
    fan_in = [f"M{m} {ky + kh} C{m} {ky + kh + 60} {c1} {ly - 104} {c1} {ly - 46}" for m in mids]
    art.append(land("".join(f'<path d="{p}" fill="none" stroke="var(--c2)" stroke-width="1.8" opacity=".55"/>' for p in fan_out + fan_in), .8, .5, 0))
    for k, (x, m, name) in enumerate(zip(kxs, mids, sl["decisions"])):
        at = .7 + .12 * k
        art.append(land(card(x, ky, kw, kh, "var(--card)", "var(--c2)", 18, 1.4) + f'<g transform="translate({m:.1f} {ky + 38}) scale(1.3)">{_n01_decision(k)}</g>', at, .5, 14))
        text.append(land(TCW(f"{m:.1f}", ky + 88, name, _p01_chars(name, 21, kw - 24), 21, "var(--white)", W6, 1.2), at, .5, 14))
    text.append(_p01_badge(BX, ky + kh / 2, "3", .30, ctx))
    for k, (x, p) in enumerate(zip(kxs, fan_out)):
        t = .32 + k * .08
        art.append(f'<g>{_n01_on(.23, .30, .01)}{token("var(--c4)", 6)}{move(p, [(0, 0), (.23, 0), (.29, 1), (1, 1)], D)}</g>')
        art.append(f'<g>{_n01_on(t)}<rect x="{x - 2:.1f}" y="{ky - 2}" width="{kw + 4:.1f}" height="{kh + 4}" rx="19" fill="none" stroke="var(--c4)" stroke-width="2.4"/>'
                   f'<circle cx="{x + kw - 24:.1f}" cy="{ky + 24}" r="13" fill="{ok}"/>' + check(f"{x + kw - 24:.1f}", ky + 24.5, .65, "var(--ink)") + '</g>')
    for p in fan_in:
        art.append(f'<g>{_n01_on(.52, .60, .01)}{token(ok, 6)}{move(p, [(0, 0), (.52, 0), (.60, 1), (1, 1)], D)}</g>')
    # 4 · the line: the compressor answered in time, the operation keeps running
    art.append(land(f'<path d="M{X0} {ly} H{X1 - 24}" stroke="var(--line)" stroke-width="16" stroke-linecap="round"/>'
                    f'<path d="M{X0} {ly} H{X1 - 24}" fill="none" stroke="var(--c4)" stroke-width="4" stroke-dasharray="8 18">{loop("stroke-dashoffset", "0;-52", 1.6)}</path>'
                    f'<path d="M{X1 - 16} {ly - 14} L{X1} {ly} L{X1 - 16} {ly + 14}" fill="none" stroke="var(--c4)" stroke-width="3.4" stroke-linecap="round"/>', .2, .5, 0))
    for k, x in enumerate(lxs):
        art.append(pop(card(-46, -46, 92, 92, "var(--card)", "var(--c2)", 20, 1.8) + f'<g transform="scale(1.1)">{_n01_equip(k)}</g>', x, ly, .35 + k * .12, .45))
    text.append(land("".join(TC(f"{x:.1f}", ly + 80, name, fit(name, 21, (X1 - X0) / 4 - 8, "mecanismo station", floor=18), "var(--muted)", W6)
                             for x, name in zip(lxs, sl["stations"])), .5, .6, 0))
    art.append(f'<g>{_n01_on(.10, .61)}<rect x="{c1 - 55:.1f}" y="{ly - 55}" width="110" height="110" rx="26" fill="none" stroke="var(--c5)" stroke-width="2.4">'
               f'{loop("stroke-opacity", ".25;1;.25", 1)}</rect></g>')
    art.append(f'<g>{_n01_on(.61)}<rect x="{c1 - 53:.1f}" y="{ly - 53}" width="106" height="106" rx="25" fill="none" stroke="{ok}" stroke-width="2.2"/>'
               f'<circle cx="{c1 + 44:.1f}" cy="{ly - 44}" r="13" fill="{ok}"/>' + check(f"{c1 + 44:.1f}", ly - 43.5, .65, "var(--ink)") + '</g>')
    py_ = ly + 136
    text.append(f'<g>{_n01_on(.61)}' + pill(c1, py_, sl["done"], ok, ctx, 20, 300, "mecanismo done", 16) + '</g>'
                + _p01_badge(BX, py_, "4", .61, ctx)
                + f'<g>{_n01_on(.65)}' + T(X1, py_ + 8, sl["sign"], fit(sl["sign"], 22, X1 - c1 - 170, "mecanismo sign", floor=18), "var(--c4)", 'text-anchor="end" font-weight="600"') + '</g>')
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- slide 3: the mechanism
@register("scene", "m03_mecanismo")
def sc_m03_mecanismo(sl, ctx):
    """The mechanism behind the cover, on one compressor, read top to bottom in four numbered steps. 1 the vibration
    leaves its normal band far below the limit: an early deviation, with time to act. 2 the signal reaches the business:
    connected data. 3 three decisions light in turn: the part is bought, moved from the warehouse, and the maintenance
    is scheduled before anything fails. 4 the response reaches the compressor: risk defused, the line keeps running.
    Frozen frame: the whole chain resolved. Slide 4 shows the same line when the deviation goes unnoticed."""
    if ORIENT() == "portrait":
        return _p03_mecanismo(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    g = [glow(1190, 440, 470, "var(--brand)", .55)]
    # 1 · the signal
    cx0, cy0, cw, ch = 850, 104, 680, 180
    real = [(874, 250), (918, 246), (962, 252), (1006, 247), (1050, 251), (1094, 245), (1138, 250), (1182, 246), (1210, 240), (1236, 232)]
    rd = "M" + " L".join(f"{x} {y}" for x, y in real)
    dx_, dy_ = real[-1]
    proj = f"M{dx_} {dy_} C1320 215 1400 196 1490 176"
    chart = (card(cx0, cy0, cw, ch, "var(--card)", "var(--c2)", 18, 1.5)
             + T(898, cy0 + 36, sl["chart"], fit(sl["chart"], 16, 300, "mecanismo chart"), "var(--muted)", W6)
             + f'<rect x="874" y="236" width="632" height="22" rx="4" fill="var(--c2)" opacity=".08"/>'
             + f'<path d="M874 176 H1506" stroke="var(--c5)" stroke-width="1.2" stroke-dasharray="4 5" opacity=".85"/>'
             + T(874, 170, sl["limit"], 15, "var(--muted)", W6))
    g.append(land(chart, .1, .5, 12))
    g.append(land(f'<path d="{rd} L{dx_} 270 L874 270 Z" fill="var(--c3)" opacity=".12"/>', .45, .5, 0) + trace(rd, "var(--c3)", 2, .4, .7))
    g.append(f'<g>{token("var(--c4)", 6)}{move(rd, [(0, 0), (.10, 1), (1, 1)], D)}</g>')
    early = (f'<g>{_n01_on(.10)}<circle cx="{dx_}" cy="{dy_}" r="10" fill="none" stroke="var(--c5)" stroke-width="1.8">{loop("r", "9;22;9", 2)}</circle>'
             + pill(1420, cy0 + 30, sl["deviation"], "var(--c5)", ctx, 15, 210, "mecanismo deviation", 14) + '</g>')
    margin = (f'<g>{_n01_on(.13)}<path d="{proj}" fill="none" stroke="var(--c4)" stroke-width="1.8" stroke-dasharray="7 7"/>'
              f'<circle cx="1490" cy="176" r="5" fill="none" stroke="var(--c5)" stroke-width="1.8"/>'
              f'<path d="M{dx_} 258 V274 M1490 258 V274 M{dx_ + 6} 266 H1484" stroke="var(--c4)" stroke-width="1.5"/>'
              f'<path d="M{dx_ + 12} 261 L{dx_ + 5} 266 L{dx_ + 12} 271 M1478 261 L1485 266 L1478 271" fill="none" stroke="var(--c4)" stroke-width="1.5" stroke-linecap="round"/>'
              + TC((dx_ + 1490) / 2, 256, sl["margin"], fit(sl["margin"], 15, 240, "mecanismo margin"), "var(--c4)", W6) + '</g>')
    g.append(early + margin + _n01_badge(876, cy0 + 30, "1", .10, ctx))
    # 2 · connected data
    hx, hy = 1190, 332
    hub = (f'<path d="M{hx} {cy0 + ch} V{hy - 20}" stroke="var(--c2)" stroke-width="1.5" opacity=".7"/>'
           f'<circle cx="{hx}" cy="{hy}" r="20" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>' + spark(hx, hy, .55, "var(--c4)")
           + T(hx + 32, hy + 6, sl["link"], fit(sl["link"], 17, 300, "mecanismo link"), "var(--white)", W6))
    g.append(land(hub, .6, .45, 0) + _n01_badge(hx - 44, hy, "2", .22, ctx))
    g.append(f'<g>{_n01_on(.22)}<circle cx="{hx}" cy="{hy}" r="20" fill="none" stroke="var(--c4)" stroke-width="2">{loop("r", "20;32;20", 2)}{loop("opacity", "1;0;1", 2)}</circle></g>')
    drop = f"M{dx_} {dy_} C{dx_} 300 {hx} 280 {hx} {hy}"
    g.append(f'<g>{_n01_on(.16, .22, .01)}{token("var(--c4)", 6)}{move(drop, [(0, 0), (.16, 0), (.22, 1), (1, 1)], D)}</g>')
    # 3 · three decisions
    ky, kh, kw = 392, 104, 216
    kxs = [850, 1082, 1314]
    mids = [x + kw / 2 for x in kxs]
    fan_out = [f"M{hx} {hy + 20} C{hx} {hy + 44} {m} {ky - 26} {m} {ky}" for m in mids]
    fan_in = [f"M{m} {ky + kh} C{m} {ky + kh + 50} 1100 {ky + kh + 44} 1100 600" for m in mids]
    g.append(land("".join(f'<path d="{p}" fill="none" stroke="var(--c2)" stroke-width="1.5" opacity=".55"/>' for p in fan_out + fan_in), .8, .5, 0))
    cards_ = []
    for k, (x, name) in enumerate(zip(kxs, sl["decisions"])):
        cards_.append(card(x, ky, kw, kh, "var(--card)", "var(--c2)", 16, 1.2) + f'<g transform="translate({x + 32} {ky + 52})">{_n01_decision(k)}</g>'
                      + TCW(x + 62, ky + 48, name, 13, 17, "var(--white)", W6, 1.2, "start"))
    g.append(seq(cards_, .7, .5, 14) + _n01_badge(834, ky + kh / 2, "3", .30, ctx))
    for k, (x, p) in enumerate(zip(kxs, fan_out)):
        t = .32 + k * .08
        g.append(f'<g>{_n01_on(.23, .30, .01)}{token("var(--c4)", 5)}{move(p, [(0, 0), (.23, 0), (.29, 1), (1, 1)], D)}</g>')
        g.append(f'<g>{_n01_on(t)}<rect x="{x - 2}" y="{ky - 2}" width="{kw + 4}" height="{kh + 4}" rx="17" fill="none" stroke="var(--c4)" stroke-width="2"/>'
                 f'<circle cx="{x + kw - 22}" cy="{ky + 22}" r="11" fill="{ok}"/>' + check(x + kw - 22, ky + 22.5, .55, "var(--ink)") + '</g>')
    for p in fan_in:
        g.append(f'<g>{_n01_on(.52, .60, .01)}{token(ok, 5)}{move(p, [(0, 0), (.52, 0), (.60, 1), (1, 1)], D)}</g>')
    # 4 · the line: the compressor answered in time, the operation keeps running
    ly, lxs = 640, [900, 1100, 1300, 1480]
    line = (f'<path d="M850 {ly} H1530" stroke="var(--line)" stroke-width="14" stroke-linecap="round"/>'
            f'<path d="M850 {ly} H1530" fill="none" stroke="var(--c4)" stroke-width="3.5" stroke-dasharray="8 18">{loop("stroke-dashoffset", "0;-52", 1.6)}</path>'
            f'<path d="M1540 {ly - 12} L1556 {ly} L1540 {ly + 12}" fill="none" stroke="var(--c4)" stroke-width="3" stroke-linecap="round"/>')
    g.append(land(line, .2, .5, 0))
    for k, (x, name) in enumerate(zip(lxs, sl["stations"])):
        st = card(-40, -40, 80, 80, "var(--card)", "var(--c2)", 18, 1.5) + f'<g transform="scale(.9)">{_n01_equip(k)}</g>'
        st += TC(0, 64, name, fit(name, 16, 150, "mecanismo station"), "var(--muted)", W6)
        g.append(pop(st, x, ly, .35 + k * .12, .45))
    c1 = lxs[1]
    g.append(f'<g>{_n01_on(.10, .61)}<rect x="{c1 - 47}" y="{ly - 47}" width="94" height="94" rx="22" fill="none" stroke="var(--c5)" stroke-width="2">'
             f'{loop("stroke-opacity", ".25;1;.25", 1)}</rect></g>')
    g.append(f'<g>{_n01_on(.61)}<rect x="{c1 - 45}" y="{ly - 45}" width="90" height="90" rx="21" fill="none" stroke="{ok}" stroke-width="1.8"/>'
             f'<circle cx="{c1 + 36}" cy="{ly - 36}" r="11" fill="{ok}"/>' + check(c1 + 36, ly - 35.5, .55, "var(--ink)")
             + pill(c1, 752, sl["done"], ok, ctx, 15, 240, "mecanismo done", 14) + '</g>')
    g.append(_n01_badge(c1 - 116, 752, "4", .61, ctx))
    g.append(f'<g>{_n01_on(.65)}' + T(1530, 758, sl["sign"], fit(sl["sign"], 17, 260, "mecanismo sign"), "var(--c4)", 'text-anchor="end" font-weight="600"') + '</g>')
    return "".join(g), D, FREEZE

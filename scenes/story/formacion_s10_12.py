"""Bench d of the class «Presentaciones de prospección de alto impacto»: slides 10 (la prueba), 11 (casos de éxito) and
12 (el relato). Runs in the shared ext namespace: it reuses the energía kit (the faceless bust _n10_bust, the ping
_n10_ping, the beats _n13_on / _n13_off / _n13_ride and the wrap _q04_even) without redefining it. Each scene lands
inside 2 s and tells a 12-second story with beat(); the frame at 0.9 of the loop (10.8 s) is the resolved one, held
until the rewind at _N13_RESET."""


def _v10_draw(d, a, b, col, w=2.5):
    """A stroke that draws itself between a and b of the loop and holds until the rewind."""
    return (f'<g opacity="0">{_n13_on(a - .004, f=.004)}<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{col}" '
            f'stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{beat("stroke-dashoffset", [(0, 1), (a, 1), (b, 0), (1, 0)])}</path></g>')


def _v10_win(a, b, f=.01):
    """Opacity shown only between a and b of the loop."""
    return beat("opacity", [(0, 0), (a, 0), (a + f, 1), (b, 1), (b + f, 0), (1, 0)])


def _v10_text(x, cy, text, size, room, fill="var(--white)", anchor="start"):
    """text wrapped to room at size, its block centered on cy (TCW: each language wraps its own way)."""
    n = _q04_even(text, size, room)
    lines = len(_q04_wrap(_(str(text)), n))
    y = cy - (lines - 1) * size * 1.3 / 2 + size * .36
    return TCW(f"{x:.1f}", f"{y:.1f}", text, n, size, fill, W6, 1.3, anchor)


def _v10_tag(x, cy, text, fill, ctx, size=17):
    """A pill whose left edge is at x."""
    s = fit(text, size, 300, "v10 tag")
    w = bold_width(_(str(text)), s, current_factor()) + 36
    return pill(x + w / 2, cy, text, fill, ctx, s, w + 2, "v10 tag")


def _v10_screen(ok):
    """The prototype: a small screen on its stand, its bottom at (0, 0): a live trend and a green light."""
    return ('<rect x="-44" y="-72" width="88" height="62" rx="8" fill="var(--ink)" stroke="var(--c4)" stroke-width="2"/>'
            '<path d="M-34 -24 L-20 -32 L-8 -28 L6 -44 L18 -38 L32 -56" fill="none" stroke="var(--c4)" stroke-width="2" stroke-linejoin="round"/>'
            f'<circle cx="30" cy="-62" r="4" fill="{ok}"/>'
            '<path d="M-6 -10 L-10 0 H10 L6 -10" fill="var(--c2)" opacity=".7"/>')


# ---------------------------------------------------------------- portrait twins (the mobile build, DCD_ORIENT=portrait)
def _pv10_prueba(sl, ctx):
    """v10 on the 900x1600 stage: the two path cards stacked on the left, the client and the table below on the right;
    the reference curves down to the table, the timeline runs along the table's top. Same beats, same frozen frame."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    top = zy + 740                                       # the table's top (y 1380)
    t1a, t1b = .07, .20
    t2, t3 = .27, .46
    t4a, t4b, t5 = .50, .62, .66
    g = [glow(zx + zw / 2, zy + 420, 520, "var(--brand)", .45)]
    tx0, tx1 = zx + 450, zx + zw                         # the table
    bust = f'<g transform="translate({tx1 - 110} {top - 120}) scale(-2.9 2.9)">{_n10_bust(SKIN_LIGHT, "var(--c1)", HAIR, "long")}</g>'
    client = (f'<clipPath id="pv10-cut"><rect x="{tx0 + 60}" y="{top - 330}" width="{tx1 - tx0 - 60}" height="330"/></clipPath>'
              f'<g clip-path="url(#pv10-cut)"><g>{bob(0, 2, 6)}{bust}</g></g>')
    table = (card(tx0, top, tx1 - tx0, 16, "var(--card)", "var(--c2)", 6, 1.5)
             + f'<path d="M{tx0 + 30} {top + 16} V{zy + zh - 20} M{tx1 - 30} {top + 16} V{zy + zh - 20}" stroke="var(--c2)" stroke-width="2" opacity=".55"/>')
    q = sl["ask"]
    s = fit(q, 23, 330, "v10 question", floor=18)
    bw = bold_width(_(str(q)), s, current_factor()) + 80
    by = top - 330
    bub = bubble(tx1 - bw, by, bw, q, ctx, "var(--c1)", s, "v10 question") + f'<path d="M{tx1 - 150} {by + 55} L{tx1 - 160} {by + 80} L{tx1 - 130} {by + 55} Z" fill="var(--c1)"/>'
    g.append(land(client + table, .1, .6, 20))
    # path 1: a client reference you can name
    rx, ry, rw, rh = zx, zy + 50, 420, 150
    icy = ry + rh / 2
    ref = (card(rx, ry, rw, rh, "var(--card)", "var(--c2)", 18, 1.5)
           + f'<circle cx="{rx + 56}" cy="{icy}" r="34" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.5"/>' + person(rx + 56, icy + 13, .8, "var(--c2)")
           + _v10_text(rx + 108, icy, sl["paths"][0], 22, rw - 124)
           + f'<g opacity="0">{_n13_on(t1b)}<circle cx="{rx + 82}" cy="{icy - 26}" r="13" fill="{ok}"/>{check(rx + 82, icy - 25, .6, "var(--ink)")}</g>')
    lx = tx0 + 40                                        # where the reference lands on the table
    p1 = f"M{rx + rw} {icy} C{rx + rw + 40} {icy} {lx - 30} {top - 300} {lx} {top - 4}"
    base1 = f'<path d="{p1}" fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="3 9" opacity=".6"/>'
    tag = (f'<g opacity="0">{_n13_on(t1b)}<rect x="{lx - 34}" y="{top - 50}" width="68" height="48" rx="9" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.5"/>'
           + person(lx - 10, top - 14, .52, "var(--c2)") + f'<circle cx="{lx + 16}" cy="{top - 27}" r="10" fill="{ok}"/>{check(lx + 16, top - 26, .45, "var(--ink)")}</g>')
    path1 = _v10_draw(p1, t1a, t1b, "var(--c2)") + _n13_ride(p1, t1a, t1b, 7) + tag + _n10_ping(lx, top - 24, 12, 52, t1b, "var(--c2)")
    # path 2: a prototype fitted to them, on a timeline along the table's top
    px, py, pw, ph = zx, zy + 290, 420, 110
    pcy = py + ph / 2
    xs = (zx + 70, zx + 300, tx0 + 250)                  # Discovery, Prototipo, Decisión (on the table)
    proto = (card(px, py, pw, ph, "var(--card)", "var(--c4)", 18, 1.5)
             + f'<g transform="translate({px + 56} {pcy + 28}) scale(.56)">{_v10_screen(ok)}</g>'
             + _v10_text(px + 108, pcy, sl["paths"][1], 22, pw - 124))
    base2 = f'<path d="M{xs[0]} {py + ph} V{top} H{xs[2]}" fill="none" stroke="var(--c4)" stroke-width="1.5" stroke-dasharray="3 9" opacity=".55"/>'
    path2 = (_v10_draw(f"M{xs[0]} {py + ph} V{top}", t2 - .05, t2, "var(--c4)")
             + _v10_draw(f"M{xs[0]} {top} H{xs[1]}", t2, t3, "var(--c4)")
             + _v10_draw(f"M{xs[1]} {top} H{xs[2]}", t4a, t4b, "var(--c4)"))
    span = sl["span"]
    ss = fit(span, 21, 190, "v10 span", floor=18)
    mid = (xs[0] + xs[1]) / 2
    rail = (f'<g>{_n13_off(t2)}{pill(mid, top - 40, span, "var(--dim)", ctx, ss, 200, "v10 span")}</g>'
            + f'<g opacity="0">{_n13_on(t2)}{pill(mid, top - 40, span, "var(--c4)", ctx, ss, 200, "v10 span")}</g>')
    lit = (t2, t3, t5)
    for k, (x, name) in enumerate(zip(xs, sl["steps"])):
        col = ok if k == 2 else "var(--c4)"
        rail += (f'<circle cx="{x}" cy="{top}" r="13" fill="var(--card)" stroke="{col}" stroke-width="2"/>'
                 f'<g opacity="0">{_n13_on(lit[k])}<circle cx="{x}" cy="{top}" r="13" fill="{col}"/></g>'
                 + TC(x, top + 52, name, fit(name, 22, 180, "v10 step", floor=18), "var(--white)", W6) + _n10_ping(x, top, 13, 44, lit[k], col))
    dev = (f'<g opacity="0">{_n13_on(t3)}{move(f"M{xs[1]} {top - 2} H{xs[2]}", [(0, 0), (t4a, 0), (t4b, 1), (1, 1)], D)}'
           f'<g transform="scale(1.35)">{_v10_screen(ok)}</g></g>')
    decide = sl["decide"]
    sd = fit(decide, 23, 280, "v10 decision", floor=18)
    dec = f'<g opacity="0">{_n13_on(t5)}{pill(xs[2], top - 150, decide, "var(--c4)", ctx, sd, 300, "v10 decision")}</g>'
    g.append(land(ref + base1, .2, .5, 16))
    g.append(land(proto + base2 + rail, .35, .5, 16))
    g += [path1, path2, dev, land(bub, .5, .5, 10), dec, _n10_ping(xs[2], top - 50, 40, 100, t4b)]
    return portrait_mark("".join(g)), D, FREEZE


# ---------------------------------------------------------------- 10 · la prueba
@register("scene", "v10_prueba")
def v10_prueba(sl, ctx):
    """Proof, as two paths to the client's table. The client asks «¿Y cómo sé que funciona?». The first path, a client
    reference you can name, runs from its card to the table and leaves a name tag there. The second runs a small
    timeline: discovery, one week, the prototype, which travels to the table and lands with «¿Lo construimos?»: their
    decision. Frozen frame: both paths drawn, the reference tag and the prototype on the table, the question open."""
    if ORIENT() == "portrait":
        return _pv10_prueba(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    top = 600                                            # the table's top: both paths end on it
    t1a, t1b = .07, .20                                  # the reference travels to the table
    t2, t3 = .27, .46                                    # discovery, then a week later the prototype
    t4a, t4b, t5 = .50, .62, .66                         # it travels to the table; the decision
    g = [glow(1200, 440, 440, "var(--brand)", .45)]
    # the client, behind the table, asking
    bust = f'<g transform="translate(1458 492) scale(-2.2 2.2)">{_n10_bust(SKIN_LIGHT, "var(--c1)", HAIR, "long")}</g>'
    client = (f'<clipPath id="v10-cut"><rect x="1290" y="330" width="290" height="{top - 330}"/></clipPath>'
              f'<g clip-path="url(#v10-cut)"><g>{bob(0, 2, 6)}{bust}</g></g>')
    table = (card(1140, top, 420, 14, "var(--card)", "var(--c2)", 6, 1.5)
             + f'<path d="M1232 {top + 14} V790 M1532 {top + 14} V790" stroke="var(--c2)" stroke-width="2" opacity=".55"/>')
    q = sl["ask"]
    s = fit(q, 20, 300, "v10 question")
    bw = bold_width(_(str(q)), s, current_factor()) + 76
    bub = bubble(1552 - bw, 290, bw, q, ctx, "var(--c1)", s, "v10 question") + '<path d="M1428 345 L1420 368 L1446 345 Z" fill="var(--c1)"/>'
    g.append(land(client + table, .1, .6, 20))
    g.append(land(bub, .5, .5, 10))

    # path 1: a client reference you can name
    rx, ry, rw, rh = 830, 150, 320, 104
    icy = ry + rh / 2
    ref = (card(rx, ry, rw, rh, "var(--card)", "var(--c2)", 16, 1.5)
           + f'<circle cx="{rx + 44}" cy="{icy}" r="26" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.5"/>' + person(rx + 44, icy + 10, .62, "var(--c2)")
           + _v10_text(rx + 86, icy, sl["paths"][0], 18, rw - 100)
           + f'<g opacity="0">{_n13_on(t1b)}<circle cx="{rx + 64}" cy="{icy - 20}" r="11" fill="{ok}"/>{check(rx + 64, icy - 19, .5, "var(--ink)")}</g>')
    p1 = f"M{rx + rw} {icy} C{rx + rw + 50} {icy} 1168 {top - 170} 1172 {top - 4}"
    base1 = f'<path d="{p1}" fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="3 9" opacity=".6"/>'
    tag = (f'<g opacity="0">{_n13_on(t1b)}<rect x="1144" y="{top - 40}" width="56" height="38" rx="8" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.5"/>'
           + person(1164, top - 12, .42, "var(--c2)") + f'<circle cx="1186" cy="{top - 21}" r="8" fill="{ok}"/>{check(1186, top - 20, .36, "var(--ink)")}</g>')
    path1 = _v10_draw(p1, t1a, t1b, "var(--c2)") + _n13_ride(p1, t1a, t1b, 6) + tag + _n10_ping(1172, top - 20, 10, 42, t1b, "var(--c2)")

    # path 2: a prototype fitted to them, on a small timeline
    px, py, pw, ph = 830, 392, 320, 76
    pcy = py + ph / 2
    xs = (875, 1050, 1296)                               # Discovery, Prototipo, Decisión (on the table)
    proto = (card(px, py, pw, ph, "var(--card)", "var(--c4)", 16, 1.5)
             + f'<g transform="translate({px + 44} {pcy + 22}) scale(.42)">{_v10_screen(ok)}</g>'
             + _v10_text(px + 86, pcy, sl["paths"][1], 18, pw - 100))
    base2 = f'<path d="M{xs[0]} {py + ph} V{top} H{xs[2]}" fill="none" stroke="var(--c4)" stroke-width="1.5" stroke-dasharray="3 9" opacity=".55"/>'
    path2 = (_v10_draw(f"M{xs[0]} {py + ph} V{top}", t2 - .05, t2, "var(--c4)")
             + _v10_draw(f"M{xs[0]} {top} H{xs[1]}", t2, t3, "var(--c4)")
             + _v10_draw(f"M{xs[1]} {top} H{xs[2]}", t4a, t4b, "var(--c4)"))
    span = sl["span"]
    ss = fit(span, 16, 150, "v10 span")
    mid = (xs[0] + xs[1]) / 2
    rail = (f'<g>{_n13_off(t2)}{pill(mid, top - 30, span, "var(--dim)", ctx, ss, 160, "v10 span")}</g>'
            + f'<g opacity="0">{_n13_on(t2)}{pill(mid, top - 30, span, "var(--c4)", ctx, ss, 160, "v10 span")}</g>')
    lit = (t2, t3, t5)
    for k, (x, name) in enumerate(zip(xs, sl["steps"])):
        col = ok if k == 2 else "var(--c4)"
        rail += (f'<circle cx="{x}" cy="{top}" r="10" fill="var(--card)" stroke="{col}" stroke-width="2"/>'
                 f'<g opacity="0">{_n13_on(lit[k])}<circle cx="{x}" cy="{top}" r="10" fill="{col}"/></g>'
                 + TC(x, top + 40, name, fit(name, 17, 150, "v10 step"), "var(--white)", W6) + _n10_ping(x, top, 10, 34, lit[k], col))
    # the prototype: born at «Prototipo» a week later, it travels to the table and lands there
    dev = (f'<g opacity="0">{_n13_on(t3)}{move(f"M{xs[1]} {top - 2} H{xs[2]}", [(0, 0), (t4a, 0), (t4b, 1), (1, 1)], D)}'
           f'{_v10_screen(ok)}</g>')
    decide = sl["decide"]
    sd = fit(decide, 19, 230, "v10 decision")
    dec = f'<g opacity="0">{_n13_on(t5)}{pill(xs[2], top - 112, decide, "var(--c4)", ctx, sd, 240, "v10 decision")}</g>'

    g.append(land(ref + base1, .2, .5, 16))
    g.append(land(proto + base2 + rail, .35, .5, 16))
    g += [path1, path2, dev, dec, _n10_ping(xs[2], top - 36, 30, 80, t4b)]
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 11 · casos de éxito
def _v11_firm(x, y, col, filled):
    """A company: a small building, its base at (x, y)."""
    body = (f'<rect x="{x - 15}" y="{y - 44}" width="30" height="44" rx="3" fill="{col if filled else "none"}" stroke="{col}" stroke-width="1.8"/>'
            + "".join(f'<rect x="{x - 9 + i * 11}" y="{y - 36 + j * 12}" width="6" height="6" rx="1" fill="{"var(--ink)" if filled else col}"/>'
                      for i in range(2) for j in range(2)))
    return body


def _pv11_kpi(sl, ctx):
    """v11 on the 900x1600 stage: the card on top with its four fields in a 2x2 grid, the still figure in a wide frame
    under it (figure and label left, the four companies and the source right). Same beats, same frozen frame."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    x, y, w, h = zx, zy + 10, zw, 540
    ts, tw = (.13, .27, .41, .55), .69
    g = [glow(zx + zw / 2, zy + 360, 520, "var(--brand)", .45)]
    c = (card(x, y, w, h, "var(--card)", "var(--c2)", 22, 1.5)
         + f'<g opacity="0">{_n13_on(tw)}{card(x, y, w, h, "none", ok, 22, 2.5)}</g>'
         + f'<g>{_n13_off(tw)}{_v10_tag(x + 30, y + 50, sl["case_label"], "var(--dim)", ctx, 21)}</g>'
         + f'<g opacity="0">{_n13_on(tw)}{_v10_tag(x + 30, y + 50, sl["success"], ok, ctx, 21)}</g>'
         + f'<g opacity="0">{_n13_on(tw)}<circle cx="{x + w - 50}" cy="{y + 50}" r="21" fill="{ok}"/>{check(x + w - 50, y + 51, 1, "var(--ink)")}</g>'
         + _n10_ping(x + w - 50, y + 50, 21, 70, tw, ok)
         + T(x + 30, y + 124, sl["case"], fit(sl["case"], 30, w - 60, "v11 case", floor=20), "var(--white)", W6)
         + f'<path d="M{x + 30} {y + 152} H{x + w - 30}" stroke="var(--line)" stroke-width="1.5"/>')
    rows = []
    fw, fh = (w - 60 - 20) / 2, 162
    for k, (label, value) in enumerate(sl["fields"][:4]):
        fx, fy = x + 30 + (k % 2) * (fw + 20), y + 176 + (k // 2) * (fh + 20)
        ex = sl.get("example") if k == 1 else None
        ew = 0
        if ex:
            se = fit(ex, 20, 140, "v11 example", floor=18)
            ew = bold_width(_(str(ex)), se, current_factor()) + 32
        r = (card(fx, fy, fw, fh, "none", "var(--line)", 16, 1.5, 'stroke-dasharray="6 6"')
             + f'<g>{_n13_off(ts[k])}' + T(fx + 24, fy + 56, label, fit(label, 22, fw - 48, "v11 field", floor=18), "var(--muted)", W6)
             + f'<path d="M{fx + 24} {fy + 116} H{fx + fw - 24}" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="4 6"/></g>'
             + f'<g opacity="0">{_n13_on(ts[k])}' + card(fx, fy, fw, fh, "var(--dim)", "var(--c2)", 16, 1.5)
             + f'<circle cx="{fx + 38}" cy="{fy + 48}" r="16" fill="{ok}"/>{check(fx + 38, fy + 49, .75, "var(--ink)")}'
             + T(fx + 66, fy + 55, label, fit(label, 21, fw - 84 - (ew + 12 if ew else 0), "v11 field", floor=18), "var(--muted)", W6)
             + T(fx + 24, fy + 118, value, fit(value, 25, fw - 48, "v11 value", floor=20), "var(--white)", W6))
        if ex:                                           # the figure of the example is illustrative, and says so
            r += pill(fx + fw - 16 - ew / 2, fy + 48, ex, "var(--c3)", ctx, se, ew + 2, "v11 example")
        r += '</g>' + _n10_ping(fx + 38, fy + 48, 16, 50, ts[k], ok)
        rows.append(r)
    g.append(land(c, .1, .55, 16))
    g.append(seq(rows, .35, .45, 12, 1.4))
    # the figure: static, in its frame, with its source; the lit company answers when the case becomes a success
    fx, fy, fw, fh = zx, y + h + 30, zw, zh - h - 50
    lcx = fx + 210
    fig, lab = sl["figure"], sl["label"]
    f = (card(fx, fy, fw, fh, "var(--card)", "var(--c4)", 22, 1.5)
         + TC(lcx, fy + 108, fig, fit(fig, 66, 360, "v11 figure", floor=20), "var(--c4)", W6)
         + _v10_text(lcx, fy + 210, lab, 22, 360, "var(--white)", "middle"))
    bx0, bx1 = fx + 440, fx + fw - 40
    step = (bx1 - bx0) / 4
    for k in range(4):
        f += f'<g transform="translate({bx0 + step * (k + .5):.1f} {fy + 200}) scale(1.6)">{_v11_firm(0, 0, "var(--c4)" if k == 0 else "var(--muted)", k == 0)}</g>'
    f += _n10_ping(bx0 + step * .5, fy + 164, 40, 80, tw + .02, "var(--c4)")
    if sl.get("source"):
        f += TC((bx0 + bx1) / 2, fy + 262, sl["source"], fit(sl["source"], 21, bx1 - bx0, "v11 source", floor=18), "var(--muted)", W6)
    g.append(land(f, .3, .6, 14))
    return portrait_mark("".join(g)), D, FREEZE


@register("scene", "v11_kpi")
def v11_kpi(sl, ctx):
    """A use case becomes a success case. The card «Caso de uso · Responder dudas por chat» has four empty fields; they
    fill one at a time: the indicator, how much it moved (an example, labeled so), its owner and its date. With the four
    in place the card turns green and becomes «Caso de éxito», and the one lit company of «1 de cada 4» answers with a
    ping. The figure beside it never moves. Frozen frame: the success case complete, the figure fixed."""
    if ORIENT() == "portrait":
        return _pv11_kpi(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    x, y, w, h = 830, 136, 420, 612
    ts = (.13, .27, .41, .55)                            # the four fields
    tw = .69                                             # it becomes a success case
    g = [glow(1190, 440, 440, "var(--brand)", .45)]
    c = (card(x, y, w, h, "var(--card)", "var(--c2)", 20, 1.5)
         + f'<g opacity="0">{_n13_on(tw)}{card(x, y, w, h, "none", ok, 20, 2.5)}</g>'
         + f'<g>{_n13_off(tw)}{_v10_tag(x + 28, y + 44, sl["case_label"], "var(--dim)", ctx)}</g>'
         + f'<g opacity="0">{_n13_on(tw)}{_v10_tag(x + 28, y + 44, sl["success"], ok, ctx)}</g>'
         + f'<g opacity="0">{_n13_on(tw)}<circle cx="{x + w - 40}" cy="{y + 44}" r="17" fill="{ok}"/>{check(x + w - 40, y + 45, .8, "var(--ink)")}</g>'
         + _n10_ping(x + w - 40, y + 44, 17, 60, tw, ok)
         + T(x + 28, y + 106, sl["case"], fit(sl["case"], 25, w - 56, "v11 case"), "var(--white)", W6)
         + f'<path d="M{x + 28} {y + 134} H{x + w - 28}" stroke="var(--line)" stroke-width="1.5"/>')
    rows = []
    for k, (label, value) in enumerate(sl["fields"][:4]):
        ry, rh = y + 158 + k * 106, 90
        r = (card(x + 20, ry, w - 40, rh, "none", "var(--line)", 14, 1.5, 'stroke-dasharray="6 6"')
             + f'<g>{_n13_off(ts[k])}' + T(x + 44, ry + 36, label, fit(label, 17, w - 90, "v11 field"), "var(--muted)", W6)
             + f'<path d="M{x + 44} {ry + 66} H{x + w - 60}" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="4 6"/></g>'
             + f'<g opacity="0">{_n13_on(ts[k])}' + card(x + 20, ry, w - 40, rh, "var(--dim)", "var(--c2)", 14, 1.5)
             + f'<circle cx="{x + 52}" cy="{ry + rh / 2}" r="13" fill="{ok}"/>{check(x + 52, ry + rh / 2 + 1, .6, "var(--ink)")}'
             + T(x + 80, ry + 34, label, fit(label, 16, w - 200, "v11 field"), "var(--muted)", W6)
             + T(x + 80, ry + 66, value, fit(value, 22, w - 124, "v11 value"), "var(--white)", W6))
        if k == 1 and sl.get("example"):                 # the figure of the example is illustrative, and says so
            ex = sl["example"]
            se = fit(ex, 15, 120, "v11 example")
            ew = bold_width(_(str(ex)), se, current_factor()) + 32
            r += pill(x + w - 40 - ew / 2, ry + 28, ex, "var(--c3)", ctx, se, ew + 2, "v11 example")
        r += '</g>' + _n10_ping(x + 52, ry + rh / 2, 13, 40, ts[k], ok)
        rows.append(r)
    g.append(land(c, .1, .55, 16))
    g.append(seq(rows, .35, .45, 12, 1.4))

    # the figure: static, in its frame, with its source; the lit company answers when the case becomes a success
    fx, fy, fw, fh = 1290, 206, 270, 470
    fcx = fx + fw / 2
    fig, lab = sl["figure"], sl["label"]
    f = (card(fx, fy, fw, fh, "var(--card)", "var(--c4)", 20, 1.5)
         + TC(fcx, fy + 92, fig, fit(fig, 60, fw - 36, "v11 figure"), "var(--c4)", W6)
         + _v10_text(fcx, fy + 170, lab, 19, fw - 44, "var(--white)", "middle"))
    for k in range(4):
        f += _v11_firm(fx + 51 + k * 56, fy + 340, "var(--c4)" if k == 0 else "var(--muted)", k == 0)
    f += _n10_ping(fx + 51, fy + 318, 26, 56, tw + .02, "var(--c4)")
    if sl.get("source"):
        f += TC(fcx, fy + 420, sl["source"], fit(sl["source"], 15, fw - 40, "v11 source"), "var(--muted)", W6)
    g.append(land(f, .3, .6, 14))
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 12 · el relato
def _pv12_titulos(sl, ctx):
    """v12 on the 900x1600 stage: the reader on top (left) with the «≤10 palabras» rule (right), the five titles in a
    full-width column under them, the thread on their left. Same beats (read, snap, rewrite, mend, close), same frame."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    titles, weak, fix = list(sl["titles"]), sl.get("weak", 1), sl["fix"]
    n = len(titles)
    nx, cx0 = zx + 30, zx + 76
    cw = zx + zw - cx0
    y0 = zy + 280
    pitch = min(128, (zy + zh - 10 - y0) / max(n, 1))
    ch = pitch - 22
    ys = [y0 + k * pitch for k in range(n)]
    cy = [v + ch / 2 for v in ys]
    chip_x = cx0 + cw - 44
    room = cw - 30 - 96
    read = [(.07, .16), (.17, .46), (.48, .56), (.58, .66), (.68, .76)][:n]
    snap, strike, new, mend = .19, .30, .40, .44
    gclose = (.77, .83)
    g = [glow(zx + zw / 2, zy + 420, 520, "var(--brand)", .45)]
    lim = sl["limit"]
    sl_ = fit(lim, 22, 240, "v12 limit", floor=18)
    lw = bold_width(_(str(lim)), sl_, current_factor()) + 40
    head = pill(zx + zw - lw / 2, y0 - 44, lim, "var(--c4)", ctx, sl_, lw + 2, "v12 limit")
    thread = f'<path d="M{nx} {cy[0]} V{cy[-1]}" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="3 8" opacity=".6"/>'
    words = lambda s: str(len(_(str(s)).split()))
    ts = lambda s: fit(s, 23, room, "v12 title", floor=18)
    cards = []
    for k, t in enumerate(titles):
        c = (card(cx0, ys[k], cw, ch, "var(--card)", "var(--c2)", 16, 1.5)
             + f'<path d="M{nx + 20} {cy[k]} H{cx0}" stroke="var(--c2)" stroke-width="1.5" opacity=".6"/>'
             + f'<circle cx="{chip_x}" cy="{cy[k]}" r="24" fill="var(--dim)" stroke="var(--line)" stroke-width="1.2"/>')
        if k == weak:
            c += (f'<g>{_n13_off(new - .03)}' + T(cx0 + 26, cy[k] + 8, t, ts(t), "var(--white)", W6)
                  + TC(chip_x, cy[k] + 7, words(t), 21, "var(--white)", W6) + '</g>'
                  + f'<g opacity="0">{_n13_on(new)}' + T(cx0 + 26, cy[k] + 8, fix, ts(fix), "var(--white)", W6)
                  + TC(chip_x, cy[k] + 7, words(fix), 21, "var(--white)", W6) + '</g>')
            sw = bold_width(_(str(t)), ts(t), current_factor())
            c += (f'<path d="M{cx0 + 20} {cy[k] + 1} H{cx0 + 32 + sw}" pathLength="1" stroke-dasharray="1" stroke="var(--c5)" stroke-width="3.5" stroke-linecap="round">'
                  f'{beat("stroke-dashoffset", [(0, 1), (strike, 1), (strike + .04, 0), (1, 0)])}{_v10_win(strike, new - .03)}</path>')
            c += f'<g opacity="0">{_v10_win(snap, new)}{card(cx0, ys[k], cw, ch, "none", "var(--c5)", 16, 2.5)}</g>'
        else:
            c += T(cx0 + 26, cy[k] + 8, t, ts(t), "var(--white)", W6) + TC(chip_x, cy[k] + 7, words(t), 21, "var(--white)", W6)
        a, b = read[k]
        c += f'<g opacity="0">{_v10_win(a, b)}{card(cx0 - 4, ys[k] - 4, cw + 8, ch + 8, "none", "var(--c4)", 19, 2)}</g>'
        cards.append(c)
    nodes = (f'<g>{_n13_off(gclose[1])}'
             + "".join(f'<circle cx="{nx}" cy="{cy[k]}" r="20" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.5"/>'
                       + TC(nx, cy[k] + 7, str(k + 1), 20, "var(--white)", W6) for k in range(n)) + '</g>')
    nodes_ok = (f'<g opacity="0">{_n13_on(gclose[1])}'
                + "".join(f'<circle cx="{nx}" cy="{cy[k]}" r="20" fill="{ok}"/>' + TC(nx, cy[k] + 7, str(k + 1), 20, "var(--ink)", W6) for k in range(n))
                + '</g>')
    segs = []
    for k in range(n - 1):
        d = f"M{nx} {cy[k] + 20} V{cy[k + 1] - 20}"
        a, b = read[k + 1][0] - .02, read[k + 1][0]
        if k != weak - 1:
            segs.append(_v10_draw(d, a, b, "var(--c4)", 3.5))
            continue
        m = (cy[k] + cy[k + 1]) / 2
        segs += [f'<g opacity="0">{_v10_win(a - .004, snap, .004)}<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" '
                 f'stroke-width="3.5" stroke-linecap="round">{beat("stroke-dashoffset", [(0, 1), (a, 1), (b, 0), (1, 0)])}</path></g>',
                 f'<g opacity="0">{_v10_win(snap, mend)}<path d="M{nx} {cy[k] + 20} V{m - 14} L{nx - 9} {m - 4} M{nx + 9} {m + 4} L{nx} {m + 14} V{cy[k + 1] - 20}" '
                 f'fill="none" stroke="var(--c5)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></g>',
                 _n10_ping(nx, m, 10, 40, snap, "var(--c5)"), _v10_draw(d, mend, mend + .03, "var(--c4)", 3.5)]
    closing = _v10_draw(f"M{nx} {cy[0]} V{cy[-1]}", *gclose, ok, 4.5) + _n10_ping(nx, cy[-1], 20, 60, gclose[1], ok)
    # the reader, top left, facing the titles; her voice goes right; «?» then a check beside her
    rx, ry = zx + 130, zy + 120
    reader = f'<g>{bob(0, 2.5, 4)}<g transform="translate({rx} {ry}) scale(2.2)">{_n10_bust(SKIN_BROWN, "var(--accent)", HAIR, "long")}</g></g>'
    vx, vy = rx + 76, ry - 44
    voice = "".join(f'<path d="M{vx + k * 14} {vy - 14 - k * 11} Q{vx + 12 + k * 18} {vy} {vx + k * 14} {vy + 14 + k * 11}" fill="none" stroke="var(--c2)" stroke-width="2.5" '
                    f'stroke-linecap="round">{loop("opacity", ".15;.9;.15", 1.6, k * .25)}</path>' for k in range(3))
    mx, my = rx + 190, ry - 50
    lost = f'<g opacity="0">{_v10_win(snap, mend)}{pill(mx, my, "?", "var(--c5)", ctx, 28, 72, "v12 lost")}</g>'
    done = (f'<g opacity="0">{_n13_on(gclose[1])}<circle cx="{mx}" cy="{my}" r="26" fill="{ok}"/>{check(mx, my + 1, 1.1, "var(--ink)")}</g>'
            + _n10_ping(mx, my, 26, 64, gclose[1], ok))
    g.append(land(head + thread, .1, .5, 10))
    g.append(seq(cards, .15, .5, 14, 1.3))
    g.append(land(nodes, .5, .5, 0))
    g.append(land(reader + voice, .3, .6, 20))
    g += segs + [closing, nodes_ok, lost, done]
    return portrait_mark("".join(g)), D, FREEZE


@register("scene", "v12_titulos")
def v12_titulos(sl, ctx):
    """The titles, read in order. A faceless reader reads a column of short titles aloud, one after another, and the
    thread between them draws itself. The weak one («Nuestras capacidades») breaks it: the line snaps red and the reader
    loses the story. The title is rewritten («Tu meta del trimestre, en tres pasos»), the thread mends and the reading
    goes on to the end, where the whole thread closes green. Beside each title, its word count under «≤10 palabras».
    Frozen frame: every title joined by one continuous thread."""
    if ORIENT() == "portrait":
        return _pv12_titulos(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    titles, weak, fix = list(sl["titles"]), sl.get("weak", 1), sl["fix"]
    n = len(titles)
    nx, cx0, cw, ch, pitch, y0 = 840, 868, 470, 72, 116, 168
    ys = [y0 + k * pitch for k in range(n)]
    cy = [v + ch / 2 for v in ys]
    chip_x = cx0 + cw - 38
    room = cw - 24 - 80
    read = [(.07, .16), (.17, .46), (.48, .56), (.58, .66), (.68, .76)][:n]
    snap, strike, new, mend = .19, .30, .40, .44      # the break, the rewrite, the thread mended
    gclose = (.77, .83)
    g = [glow(1150, 440, 460, "var(--brand)", .45)]

    # the counter: the rule and, under it, each title's word count
    lim = sl["limit"]
    sl_ = fit(lim, 17, 190, "v12 limit")
    lw = bold_width(_(str(lim)), sl_, current_factor()) + 36
    head = pill(cx0 + cw - lw / 2, y0 - 34, lim, "var(--c4)", ctx, sl_, lw + 2, "v12 limit")

    # the thread: faint and dashed; nodes numbered
    thread = f'<path d="M{nx} {cy[0]} V{cy[-1]}" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="3 8" opacity=".6"/>'
    words = lambda s: str(len(_(str(s)).split()))
    cards = []
    for k, t in enumerate(titles):
        c = (card(cx0, ys[k], cw, ch, "var(--card)", "var(--c2)", 14, 1.5)
             + f'<path d="M{nx + 15} {cy[k]} H{cx0}" stroke="var(--c2)" stroke-width="1.5" opacity=".6"/>'
             + f'<circle cx="{chip_x}" cy="{cy[k]}" r="18" fill="var(--dim)" stroke="var(--line)" stroke-width="1.2"/>')
        if k == weak:
            c += (f'<g>{_n13_off(new - .03)}' + T(cx0 + 24, cy[k] + 7, t, fit(t, 20, room, "v12 title"), "var(--white)", W6)
                  + TC(chip_x, cy[k] + 6, words(t), 16, "var(--white)", W6) + '</g>'
                  + f'<g opacity="0">{_n13_on(new)}' + T(cx0 + 24, cy[k] + 7, fix, fit(fix, 20, room, "v12 title"), "var(--white)", W6)
                  + TC(chip_x, cy[k] + 6, words(fix), 16, "var(--white)", W6) + '</g>')
            sw = bold_width(_(str(t)), fit(t, 20, room, "v12 title"), current_factor())
            c += (f'<path d="M{cx0 + 18} {cy[k] + 1} H{cx0 + 30 + sw}" pathLength="1" stroke-dasharray="1" stroke="var(--c5)" stroke-width="3" stroke-linecap="round">'
                  f'{beat("stroke-dashoffset", [(0, 1), (strike, 1), (strike + .04, 0), (1, 0)])}{_v10_win(strike, new - .03)}</path>')
            c += f'<g opacity="0">{_v10_win(snap, new)}{card(cx0, ys[k], cw, ch, "none", "var(--c5)", 14, 2.5)}</g>'
        else:
            c += (T(cx0 + 24, cy[k] + 7, t, fit(t, 20, room, "v12 title"), "var(--white)", W6)
                  + TC(chip_x, cy[k] + 6, words(t), 16, "var(--white)", W6))
        a, b = read[k]
        c += f'<g opacity="0">{_v10_win(a, b)}{card(cx0 - 4, ys[k] - 4, cw + 8, ch + 8, "none", "var(--c4)", 17, 2)}</g>'
        cards.append(c)
    nodes = (f'<g>{_n13_off(gclose[1])}'
             + "".join(f'<circle cx="{nx}" cy="{cy[k]}" r="15" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.5"/>'
                       + TC(nx, cy[k] + 5.5, str(k + 1), 15, "var(--white)", W6) for k in range(n)) + '</g>')
    nodes_ok = (f'<g opacity="0">{_n13_on(gclose[1])}'
                + "".join(f'<circle cx="{nx}" cy="{cy[k]}" r="15" fill="{ok}"/>' + TC(nx, cy[k] + 5.5, str(k + 1), 15, "var(--ink)", W6) for k in range(n))
                + '</g>')

    # the reading: each segment draws as the reader moves on; the first one snaps red at the weak title, then mends
    segs = []
    for k in range(n - 1):
        d = f"M{nx} {cy[k] + 15} V{cy[k + 1] - 15}"
        a, b = read[k + 1][0] - .02, read[k + 1][0]     # drawn as the reader moves on to the next title
        if k != weak - 1:
            segs.append(_v10_draw(d, a, b, "var(--c4)", 3))
            continue
        m = (cy[k] + cy[k + 1]) / 2
        segs += [f'<g opacity="0">{_v10_win(a - .004, snap, .004)}<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" '
                 f'stroke-width="3" stroke-linecap="round">{beat("stroke-dashoffset", [(0, 1), (a, 1), (b, 0), (1, 0)])}</path></g>',
                 f'<g opacity="0">{_v10_win(snap, mend)}<path d="M{nx} {cy[k] + 15} V{m - 12} L{nx - 7} {m - 3} M{nx + 7} {m + 3} L{nx} {m + 12} V{cy[k + 1] - 15}" '
                 f'fill="none" stroke="var(--c5)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>',
                 _n10_ping(nx, m, 8, 34, snap, "var(--c5)"), _v10_draw(d, mend, mend + .03, "var(--c4)", 3)]
    closing = _v10_draw(f"M{nx} {cy[0]} V{cy[-1]}", *gclose, ok, 4) + _n10_ping(nx, cy[-1], 15, 50, gclose[1], ok)

    # the reader: faceless, reading aloud; a red «?» when the thread breaks, a green check when it closes
    rx, ry = 1470, 506
    reader = f'<g>{bob(0, 2.5, 4)}<g transform="translate({rx} {ry}) scale(-2.1 2.1)">{_n10_bust(SKIN_BROWN, "var(--accent)", HAIR, "long")}</g></g>'
    voice = "".join(f'<path d="M{1404 - k * 12} {452 - k * 9} Q{1394 - k * 16} {462} {1404 - k * 12} {472 + k * 9}" fill="none" stroke="var(--c2)" stroke-width="2" '
                    f'stroke-linecap="round">{loop("opacity", ".15;.9;.15", 1.6, k * .25)}</path>' for k in range(3))
    lost = f'<g opacity="0">{_v10_win(snap, mend)}{pill(1398, 372, "?", "var(--c5)", ctx, 22, 60, "v12 lost")}</g>'
    done = (f'<g opacity="0">{_n13_on(gclose[1])}<circle cx="1398" cy="372" r="20" fill="{ok}"/>{check(1398, 373, .85, "var(--ink)")}</g>'
            + _n10_ping(1398, 372, 20, 50, gclose[1], ok))

    g.append(land(head + thread, .1, .5, 10))
    g.append(seq(cards, .15, .5, 14, 1.3))
    g.append(land(nodes, .5, .5, 0))
    g.append(land(reader + voice, .3, .6, 20))
    g += segs + [closing, nodes_ok, lost, done]
    return "".join(g), D, FREEZE

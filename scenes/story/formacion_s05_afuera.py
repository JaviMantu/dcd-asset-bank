"""Class VR2 · slide 5: from outside, with universal business areas (sales, finance, operations, people)."""


def _v05_biz(k, col="var(--c2)"):
    """Business area k, drawn around 0,0: 0 ventas (cart), 1 finanzas (bars and coin), 2 operaciones (gear), 3 personas."""
    sw = f'fill="none" stroke="{col}" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"'
    if k == 0:
        return (f'<path d="M-22 -14 H-15 L-9 10 H15 L20 -7 H-12" {sw}/>'
                f'<circle cx="-6" cy="17" r="3" {sw}/><circle cx="12" cy="17" r="3" {sw}/>')
    if k == 1:
        return (f'<path d="M-20 18 H20" {sw}/><rect x="-17" y="2" width="7" height="14" rx="1.5" {sw}/>'
                f'<rect x="-6" y="-6" width="7" height="22" rx="1.5" {sw}/><rect x="5" y="-14" width="7" height="30" rx="1.5" {sw}/>'
                f'<path d="M-18 -8 L-6 -16 L4 -12 L18 -22" {sw}/>')
    if k == 2:
        teeth = "".join(f'<rect transform="rotate({a})" x="-3" y="-21" width="6" height="7" rx="1.5" {sw}/>' for a in range(0, 360, 45))
        return f'<circle r="14" {sw}/><circle r="5" {sw}/>' + teeth
    return (f'<circle cx="-9" cy="-9" r="6" {sw}/><path d="M-20 14 C-20 3 2 3 2 14" {sw}/>'
            f'<circle cx="10" cy="-6" r="5" {sw}/><path d="M1 15 C2 6 20 6 20 15" {sw}/>')


@register("scene", "v05_afuera")
def sc_v05_afuera(sl, ctx):
    """Slide 5 of the class VR2: m02_afuera with universal business areas instead of the energía deck's gas stations.
    Outside, three public sources; a lens reads each one and it drops into our notebook, which fills. A hypothesis
    comes out, marked «por validar». Below the dashed line is the inside: their operation, drawn as a ghost, which we
    cannot see. The hypothesis sends a question to each station: the inside is theirs to tell, we come to ask. Frozen
    frame: sources read, notebook full, the hypothesis waiting to be validated, a question over every station."""
    if ORIENT() == "portrait":
        return _pv05_afuera(sl, ctx)
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
                   f'<g transform="translate({x} 670)" opacity=".7">{_v05_biz(k)}</g>'
                   + TC(x, 734, sl["areas"][k], fit(sl["areas"][k], 15, 150, "afuera area", floor=15), "var(--white)", W6))
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




# ---------------------------------------------------------------- portrait twin (the mobile build, DCD_ORIENT=portrait)
def _pv05_afuera(sl, ctx):
    """v05 on the 900x1600 stage: sources and dossier side by side on top, the hypothesis across, the inside below the
    dashed line with its four areas in a 2x2 grid; same beats, same frozen frame."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    g = [glow(zx + zw / 2, zy + 300, 480, "var(--brand)", .55)]
    sw_, sh_ = 390, 78
    sy = [zy + 8 + k * 90 for k in range(3)]
    bx, by, bw, bh = zx + sw_ + 40, zy + 8, zw - sw_ - 40, 258
    src = []
    for k, (y, lab) in enumerate(zip(sy, sl["layers"])):
        c = card(zx, y, sw_, sh_, "var(--card)", "var(--c2)", 12, 1.2) + f'<g transform="translate({zx + 34} {y + sh_ / 2}) scale(1.3)">{_n01_source(k)}</g>'
        c += _sm_text(zx + 70, y + sh_ / 2, lab, 23, sw_ - 90, lines_max=2)
        src.append(c)
    g.append(seq(src, .1, .45, 14))
    ny = lambda k: by + 70 + k * 62 + 8
    lp = lambda k, y: f"M{zx + sw_} {y + sh_ / 2} C{zx + sw_ + 22} {y + sh_ / 2} {bx - 22} {ny(k):.0f} {bx} {ny(k):.0f}"
    links = "".join(f'<path d="{lp(k, y)}" fill="none" stroke="var(--c2)" stroke-width="1.6" opacity=".6"/>' for k, y in enumerate(sy))
    rings = "".join(f'<circle cx="{bx + 20}" cy="{by + 30 + k * 38}" r="6" fill="none" stroke="var(--c2)" stroke-width="2"/>' for k in range(6))
    book = (card(bx, by, bw, bh, "var(--card)", "var(--c2)", 14, 1.8) + rings
            + T(bx + 44, by + 44, sl["book"], fit(sl["book"], 24, bw - 100, "afuera notebook", floor=20), "var(--white)", W6))
    g.append(land(links + book, .35, .5))
    read = [.04, .13, .22]
    for k, (y, t) in enumerate(zip(sy, read)):
        g.append(f'<g>{_n01_on(t)}<rect x="{zx - 1}" y="{y - 1}" width="{sw_ + 2}" height="{sh_ + 2}" rx="13" fill="none" stroke="var(--c4)" stroke-width="2.4"/></g>')
        g.append(f'<g>{_n01_on(t + .03, t + .07, .01)}{token("var(--c4)", 6)}{move(lp(k, y), [(0, 0), (t + .03, 0), (t + .07, 1), (1, 1)], D)}</g>')
        para = "".join(f'<rect x="{bx + 44}" y="{ny(k) - 8 + j * 18}" width="{(bw - 70) * (.9 if j == 0 else .6):.0f}" height="8" rx="4" fill="var(--c2)" opacity=".6"/>' for j in range(2))
        g.append(f'<g>{_n01_on(t + .07)}{para}</g>')
    lx = zx + sw_ - 40
    stops = [(0, f"{lx} {sy[0] + 36}"), (.06, f"{lx} {sy[0] + 36}"), (.11, f"{lx} {sy[1] + 36}"), (.15, f"{lx} {sy[1] + 36}"),
             (.20, f"{lx} {sy[2] + 36}"), (.25, f"{lx} {sy[2] + 36}"), (.31, f"{bx + bw - 40} {by + bh - 50}"), (.97, f"{bx + bw - 40} {by + bh - 50}"),
             (1, f"{lx} {sy[0] + 36}")]
    g.append(land(f'<g>{_n01_tr(stops)}<g transform="scale(1.3)">{_n01_lens()}</g></g>', .6, .4, 0))
    g.append(f'<g>{_n01_on(.31)}<g>{loop("opacity", ".4;1;.4", 2.2)}{spark(bx + bw - 32, by + 34, .75, "var(--c4)")}</g></g>')
    hy, hh = by + bh + 34, 116
    hyp = (card(zx, hy, zw, hh, "var(--card)", "var(--c4)", 16, 1.8) + T(zx + 26, hy + 38, sl["case_label"], 21, "var(--c4)", W6)
           + _sm_text(zx + 26, hy + 80, sl["case"], 26, zw - 52, lines_max=2))
    tag = f'<g>{_n01_on(.47)}<g>{loop("opacity", ".8;1;.8", 2.6)}' + pill(zx + zw - 130, hy, sl["tag"], "var(--c4)", ctx, 21, 240, "afuera tag") + '</g></g>'
    g.append(f'<g>{_n01_on(.38, 1, .04)}<g>{_n01_tr([(0, "90 -90"), (.38, "90 -90"), (.44, "0 0"), (1, "0 0")])}{hyp}</g></g>' + tag)
    iy = hy + hh + 44
    ih = zy + zh - iy
    rows = [iy + 120, iy + 290]
    inside = card(zx, iy, zw, ih, "var(--dim)", "var(--c2)", 20, 1.5, 'fill-opacity=".45" stroke-dasharray="8 8"')
    inside += "".join(f'<path d="M{zx + 16} {r} H{zx + zw - 16}" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="4 8" opacity=".45"/>' for r in rows)
    gx = [zx + zw * .27, zx + zw * .73]
    pts = [(gx[k % 2], rows[k // 2]) for k in range(4)]
    for k, (x, y) in enumerate(pts):
        inside += (f'<rect x="{x - 44:.0f}" y="{y - 44}" width="88" height="88" rx="18" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="5 5" opacity=".75"/>'
                   f'<g transform="translate({x:.0f} {y}) scale(1.25)" opacity=".7">{_v05_biz(k)}</g>'
                   + TC(f"{x:.0f}", y + 76, sl["areas"][k], fit(sl["areas"][k], 22, 260, "afuera area", floor=20), "var(--white)", W6))
    inside += T(zx + 24, iy + ih - 22, sl["inside"], fit(sl["inside"], 22, 420, "afuera inside", floor=20), "var(--white)", W6)
    g.append(land(inside, .5, .55, 16))
    ask = sl["ask"]
    g.append(f'<g>{_n01_on(.74)}' + T(zx + zw - 24, iy + ih - 22, ask, fit(ask, 22, 330, "afuera ask", floor=20), "var(--c4)", 'text-anchor="end" font-weight="600"') + '</g>')
    hx, hb = zx + zw / 2, hy + hh
    for k, (x, y) in enumerate(pts):
        a = .54 + k * .05
        qx, qy = x + 78, y - 44
        q = (f'<path d="M{qx - 22:.0f} {qy + 16} L{x + 40:.0f} {y - 30}" stroke="var(--c4)" stroke-width="1.6" stroke-dasharray="3 4"/>'
             f'<circle cx="{qx:.0f}" cy="{qy}" r="24" fill="var(--card)" stroke="var(--c4)" stroke-width="2">{loop("stroke-opacity", ".4;1;.4", 2.4, k * .5)}</circle>'
             + TC(f"{qx:.0f}", qy + 9, "?", 26, "var(--c4)", W6))
        g.append(f'<g>{_n01_on(a + .04)}<path d="M{hx:.0f} {hb} L{qx:.0f} {qy - 24}" stroke="var(--c4)" stroke-width="1.3" stroke-dasharray="3 6" opacity=".45"/></g>')
        g.append(f'<g>{_n01_on(a, 1, .015)}<g>{_n01_tr([(0, f"{hx - qx:.0f} {hb - qy:.0f}"), (a, f"{hx - qx:.0f} {hb - qy:.0f}"), (a + .05, "0 0"), (1, "0 0")])}{q}</g></g>')
    return portrait_mark("".join(g)), D, FREEZE

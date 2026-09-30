"""Portrait twins of the fifteen «papel» scenes of story/fidelizacion_s01_15.py (p01_portada … p15_lema), 0.6.0.

Each desktop scene hands over on its first line (`if ORIENT() == "portrait": return _ppNN_…(sl, ctx)`). The twin tells
the same story on the 900x1600 stage, stacked in ART_ZONE (x 40-860, y 640-1540; the text block owns y < 640): same
args, same 12-second loop timed with beat() at the same fractions, the same resolved frame at 10.8 s, labels >= 20 px.
Rows become columns or 2x2 grids; nothing is dropped. Helpers of the desktop file (_p01_on, _p04_in, _p13_on, …) and of
energia_s04_06.py (_n04_win, _n04_ping) are looked up at call time, so load order does not matter.
"""


def _pp_t(x, y, s, size=22, where="portrait label", room=300, fill=None, anchor="start", bold=True):
    """A label on paper at >= 20 px (the phone floor): px_text with a higher floor."""
    z = fit(s, max(size, 20), room, where, floor=20, bold=bold)
    return (TC if anchor == "middle" else T)(f"{x:.1f}", f"{y:.1f}", s, z, fill or PX_INK, W6 if bold else "")


def _pp_out(sl, g):
    """The twin's svg: shifted to the layout's art zone (the stacked stage puts both layouts at 40, 640) and marked."""
    zx, zy, _w, _h = ART_ZONE(sl.get("layout") or "left")
    svg = "".join(g)
    if (zx, zy) != (40, 640):
        svg = f'<g transform="translate({zx - 40} {zy - 640})">{svg}</g>'
    return portrait_mark(svg), D, FREEZE


def _pp_scale(inner, x, y, s):
    """inner drawn around (0, 0), placed at (x, y) and scaled by s."""
    return f'<g transform="translate({x:.1f} {y:.1f}) scale({s})">{inner}</g>'


def _pp_minimap(lit_now, lit_at, x, y, s=.8, step=110):
    """The strategy map, small: three route icons on a short ribbon (the desktop's _p04_minimap, phone sized)."""
    g = [f'<path d="M{x} {y} L{x + 2 * step} {y}" stroke="{PX_RIBBON}" stroke-width="3" stroke-linecap="round"/>']
    for k in range(3):
        cx = x + k * step
        g.append(px_icon(k, cx, y, s, lit=k in lit_now))
        if k in lit_at:
            g.append(f'<g>{_p04_on(lit_at[k])}{px_icon(k, cx, y, s, lit=True)}</g>')
    return "".join(g)


# ==================================================================================================== 01-03
def _pp01_portada(sl, ctx):
    """p01 stacked: the client's logo on top, the paper week under it; the Friday sheet folds into the plane, which flies
    over the week drawing the ribbon and lands on Monday as the sealed envelope with its hour."""
    days, hour = sl["days"], sl["hour"]
    g = [land(px_logo_client(450, 660, 300), .1, .6)]
    x0, y0, cw, bot = 75, 960, 150, 1440
    cal = px_sheet(x0 - 14, y0 - 14, cw * 5 + 28, bot - y0 + 28, PX_PAPER, 31)
    cal += f'<path d="M{x0} {y0 + 66} H{x0 + cw * 5}" stroke="{PX_EDGE}" stroke-width="1.6"/>'
    cal += "".join(f'<path d="M{x0 + k * cw} {y0 + 10} V{bot - 10}" stroke="{PX_EDGE}" stroke-width="1.2"/>' for k in range(1, 5))
    cal += "".join(_pp_t(x0 + k * cw + cw / 2, y0 + 44, d, 24, "portada day", cw - 20, anchor="middle") for k, d in enumerate(days))
    cal += "".join(f'<circle cx="{x0 + 20 + k * 40}" cy="{y0 - 1}" r="6" fill="none" stroke="{PX_EDGE}" stroke-width="1.4"/>'
                   for k in range(19) if x0 + 20 + k * 40 < x0 + cw * 5 - 10)
    cal += "".join(px_lines(x0 + k * cw + 20, y0 + 116 + (k % 2) * 48, cw - 40, 3 + (k % 2), 26, width=6) for k in (1, 2, 3))
    g.append(land(cal, .35, .6))
    fx, fy = x0 + 4 * cw + cw / 2, 1140
    sheet = px_sheet(fx - 56, fy - 70, 112, 140, PX_PAPER_2, 33) + px_lines(fx - 40, fy - 44, 80, 5, 21, width=6)
    fold = _p01_tr([(0, "1 1"), (.14, "1 1"), (.22, ".2 .6"), (.97, ".2 .6"), (1, "1 1")], "scale")
    g.append(land(f'<g>{beat("opacity", [(0, 1), (.19, 1), (.22, 0), (.97, 0), (1, 1)])}'
                  f'<g transform="translate({fx} {fy})"><g>{fold}<g transform="translate({-fx} {-fy})">{sheet}</g></g></g></g>', .7, .5))
    mx = x0 + cw / 2
    path = f"M{fx} {fy - 2} C{fx - 50} 830 {mx + 200} 770 {mx + 6} 1110"
    g.append(_p01_draw(path, .22, .56, PX_RIBBON, 3.5, 'opacity=".95"'))
    plane = f'<g transform="scale(-1 1)">{px_plane(0, 0, .8)}</g>'
    g.append(f'<g>{_p01_on(.19)}<g>{move(path, [(0, 0), (.22, 0), (.56, 1), (1, 1)], D)}{plane}</g></g>')
    ex, ey, ew, eh = mx - 66, 1180, 132, 86
    g.append(_p01_drop(px_envelope(ex, ey, ew, eh, sealed=False), .58, -36))
    seal = (f'<circle cx="{mx}" cy="{ey + eh * .52:.1f}" r="13" fill="{PX_RIBBON}"/>'
            f'<circle cx="{mx - 4}" cy="{ey + eh * .52 - 4:.1f}" r="3.5" fill="var(--white)" opacity=".55"/>')
    g.append(f'<g>{_p01_on(.68, 1, .015)}{seal}</g>')
    g.append(f'<g>{_p01_on(.7)}{_pp_t(mx, 1330, hour, 28, "portada hour", cw - 20, anchor="middle")}</g>')
    return _pp_out(sl, g)


def _pp02_viernes(sl, ctx):
    """p02 stacked: the cork board fills the zone in a 3x3 grid, the 3:30 clock pinned on its corner; the yellow
    post-its drop until the board is full, then the red one glides in to the center and gets its pin."""
    bx, by, bw, bh = 60, 760, 780, 770
    board = (px_sheet(bx, by, bw, bh, P02_FRAME, 51)
             + f'<path d="{px_sheet_path(bx + 22, by + 22, bw - 44, bh - 44, 52, 1.6)}" fill="{P02_CORK}" stroke="none"/>'
             + "".join(f'<circle cx="{bx + 32 + (k * 97) % (bw - 64)}" cy="{by + 36 + (k * 61) % (bh - 72)}" r="1.8" '
                       f'fill="{P02_FRAME}" opacity=".35"/>' for k in range(60)))
    g = [land(board, .1, .55), pop(_p02_clock(0, 0, 54), 790, 712, .45, .45)]
    cols, rows = (200, 450, 700), (900, 1145, 1390)
    cells = [(cols[0], rows[0], -4), (cols[1], rows[0], 3), (cols[2], rows[0], -2), (cols[0], rows[1], 2), (cols[2], rows[1], -3),
             (cols[0], rows[2], -2), (cols[1], rows[2], 3), (cols[2], rows[2], 4)]
    w, h = 200, 176
    parts = [px_postit(cx - w / 2, cy - h / 2, w, h, PX_POSTIT, 60 + k, r, lab, 23) + px_pin(cx, cy - h / 2 + 16)
             for k, ((cx, cy, r), lab) in enumerate(zip(cells, sl["postits"]))]
    g.append(seq(parts[:3], .55, .5, 18))
    for k, p in enumerate(parts[3:]):
        g.append(_p01_drop(p, .08 + k * .075, -60))
    rw, rh = 240, 200
    rx, ry = cols[1] - rw / 2, rows[1] - rh / 2
    red = px_postit(rx, ry, rw, rh, PX_POSTIT_RED, 41, -3, sl["urgent"], 26, ctx.brand.on("var(--c5)"))
    px, py = cols[1], ry + 18
    shake = _p01_tr([(0, "0"), (.66, "0"), (.675, "-2.5"), (.69, "1.5"), (.705, "0"), (1, "0")], "rotate")
    arrive = _p01_tr([(0, "380 -260"), (.56, "380 -260"), (.63, "0 0"), (.97, "0 0"), (1, "380 -260")])
    g.append(f'<g>{_p01_on(.56, 1, .02)}<g>{arrive}<g transform="translate({px} {py + 70})"><g>{shake}'
             f'<g transform="translate({-px} {-py - 70})">{red}</g></g></g></g></g>')
    g.append(_p01_drop(px_pin(px, py, "var(--c4)"), .66, -40))
    return _pp_out(sl, g)


def _pp03_estrategia(sl, ctx):
    """p03 stacked: the red post-it and the calm person on top, the folded map under them; the map unfolds panel by
    panel and the ribbon leaves the post-it to trace the route through the three icon stops, no words."""
    mx, my, pw, ph, n = 90, 920, 180, 580, 4
    panels = []
    for k in range(n):
        x = mx + k * pw
        fill = PX_PAPER if k % 2 == 0 else "color-mix(in srgb, var(--white) 84%, var(--c4))"
        art = px_sheet(x, my, pw, ph, fill, 70 + k)
        art += "".join(f'<path d="M{x} {my + 70 + j * 110} H{x + pw}" stroke="{PX_EDGE}" stroke-width="1" opacity=".6"/>' for j in range(5))
        art += f'<path d="M{x + pw * .5} {my + 10} V{my + ph - 10}" stroke="{PX_EDGE}" stroke-width="1" opacity=".5" stroke-dasharray="4 7"/>'
        art += f'<path d="M{x + (k % 2 == 0) * pw} {my + 8} V{my + ph - 8}" stroke="{PX_SHADOW}" stroke-width="1.2" opacity=".35"/>'
        if k == 0:
            panels.append(art)
            continue
        a = .06 + (k - 1) * .07
        unf = _p01_tr([(0, "0 1"), (a, "0 1"), (a + .06, "1 1"), (.97, "1 1"), (1, "0 1")], "scale")
        panels.append(f'<g>{_p01_on(a, 1, .01)}<g transform="translate({x} 0)"><g>{unf}<g transform="translate({-x} 0)">{art}</g></g></g></g>')
    river = (f'<path d="M{mx + 10} {my + 170} C{mx + 200} {my + 120} {mx + 300} {my + 290} {mx + 470} {my + 230} '
             f'S{mx + 640} {my + 130} {mx + pw * n - 10} {my + 180}" fill="none" stroke="var(--c2)" stroke-width="6" opacity=".55"/>')
    folded = "".join(px_sheet(mx + 7 * j, my + 7 * j, pw, ph, PX_PAPER_2, 80 + j) for j in (2, 1))
    g = [land(f'<g>{beat("opacity", [(0, 1), (.06, 1), (.08, 0), (.97, 0), (1, 1)])}{folded}</g>' + panels[0], .3, .55)]
    g.append("".join(panels[1:]) + f'<g>{_p01_on(.27, 1, .03)}{river}</g>')
    stops = [(230, 1330), (450, 1070), (680, 1310)]
    route = (f"M205 866 C205 1000 150 {stops[0][1]} {stops[0][0]} {stops[0][1]} "
             f"C330 {stops[0][1]} 330 {stops[1][1]} {stops[1][0]} {stops[1][1]} "
             f"C570 {stops[1][1]} 560 {stops[2][1]} {stops[2][0]} {stops[2][1]}")
    g.append(_p01_draw(route, .32, .74, PX_RIBBON, 5))
    for k, ((x, y), a) in enumerate(zip(stops, (.42, .56, .72))):
        grow = _p01_tr([(0, ".4 .4"), (a, ".4 .4"), (a + .04, "1.08 1.08"), (a + .06, "1 1"), (1, "1 1")], "scale")
        g.append(f'<g>{_p01_on(a, 1, .02)}<g transform="translate({x} {y})"><g>{grow}<g transform="translate({-x} {-y})">'
                 f'{px_icon(k, x, y, 1.5)}</g></g></g></g>')
    rw, rh = 230, 180
    red = px_postit(90, 680, rw, rh, PX_POSTIT_RED, 41, -4, sl["urgent"], 25, ctx.brand.on("var(--c5)"))
    g.append(land(red + px_pin(90 + rw / 2, 698, "var(--c4)"), .1, .55))
    walker = (f'<g>{bob(0, -2.5, 4.4)}<path d="M-30 18 Q-30 -14 0 -14 Q30 -14 30 18 Z" fill="{PX_PAPER_2}" stroke="{PX_EDGE}" stroke-width="1.2"/>'
              f'<circle cx="0" cy="-36" r="17" fill="{PX_PAPER_2}" stroke="{PX_EDGE}" stroke-width="1.2"/></g>')
    g.append(land(f'<ellipse cx="455" cy="866" rx="50" ry="8" fill="{PX_SHADOW}"/>' + _pp_scale(walker, 450, 830, 1.7), .5, .5))
    return _pp_out(sl, g)


# ==================================================================================================== 04-06
def _pp04_hole(x, y, w, h, label=None):
    g = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="none" stroke="{PX_MUTED_INK}" '
         f'stroke-width="1.5" stroke-dasharray="6 5"/>')
    if label:
        g += _pp_t(x + w / 2, y + h / 2 + 7, label, 20, "template hole", w - 20, PX_MUTED_INK, "middle", False)
    return g


def _pp04_explicar(sl, ctx):
    """p04 stacked: on top, the one-line ask and the hollow template it gets back, and the small strategy map; below,
    the chat sheet whose three holes the three context cards fill one by one; it reads as a procedure, stop 0 lights."""
    ask, ins, cards, done = sl["ask"], sl["insert"], sl["cards"], sl["done"]
    left = (_p04_bubble(60, 660, 330, 64, ask, 31, PX_PAPER, 22)
            + px_sheet(60, 760, 330, 250, PX_PAPER, 32) + px_lines(84, 784, 270, 2, 20)
            + "".join(_pp04_hole(84, 832 + k * 58, 282, 48, ins) for k in range(3)))
    sheet = (px_sheet(60, 1060, 780, 460, PX_PAPER, 33)
             + _p04_bubble(490, 1074, 330, 58, ask, 34, PX_PAPER_2, 22)
             + "".join(_pp04_hole(88, 1150 + k * 108, 724, 94) for k in range(3)))
    thread = px_ribbon("M392 890 C440 890 420 1030 452 1058", 3, .7, .5)
    g = [land(left, .1, .5), land(sheet, .3, .55), thread, land(_pp_minimap((), {}, 540, 860), .9, .5, 10)]
    for k, lab in enumerate(cards):
        a = .20 + k * .16
        x, y = 88, 1150 + k * 108
        c = (px_sheet(x, y, 724, 94, PX_PAPER_2, 40 + k)
             + f'<rect x="{x + 18}" y="{y + 16}" width="14" height="62" rx="3" fill="{_P04_TABS[k]}"/>'
             + _pp_t(x + 52, y + 44, lab, 26, "context card", 640)
             + px_lines(x + 52, y + 62, 560, 2, 14))
        g.append(f'<g>{_p04_on(a)}<g>{_p04_in(a, -60, -40)}{c}</g></g>')
    fin = (f'<path d="M92 1486 L103 1499 L125 1472" fill="none" stroke="{PX_RIBBON}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
           + _pp_t(140, 1500, done, 24, "procedure done", 680))
    g.append(f'<g>{_p04_on(.70)}{fin}</g>')
    g.append(_pp_minimap((), {0: .76}, 540, 860))
    return _pp_out(sl, g)


def _pp05_revisar(sl, ctx):
    """p05 stacked: the draft and the procedure side by side on top, the fixed figure under them, the small map at the
    bottom. The lens stops on the unsourced number, the strike crosses it, the ribbon carries it to the procedure,
    which gains its new step; stop 1 lights. The figure never moves."""
    draft, inv, nosrc, proc, steps, new = sl["draft"], sl["invented"], sl["nosource"], sl["proc"], sl["steps"], sl["step"]
    hi = "color-mix(in srgb, var(--c4) 55%, var(--white))"
    doc = (px_sheet(60, 660, 440, 420, PX_PAPER, 41)
           + _pp_t(84, 706, draft, 24, "draft title", 390)
           + px_lines(84, 736, 390, 3, 26)
           + '<rect x="84" y="866" width="100" height="6" rx="3" fill="' + PX_MUTED_INK + '" opacity=".45"/>'
           + f'<rect x="196" y="846" width="124" height="46" rx="5" fill="{hi}"/>'
           + _pp_t(258, 880, inv, 30, "invented number", 112, anchor="middle")
           + f'<rect x="332" y="866" width="140" height="6" rx="3" fill="{PX_MUTED_INK}" opacity=".45"/>'
           + px_lines(84, 920, 390, 6, 26))
    card_ = (px_sheet(510, 660, 330, 420, PX_PAPER_2, 42)
             + _pp_t(534, 706, proc, 24, "procedure title", 284)
             + "".join(f'<rect x="534" y="{738 + k * 54}" width="10" height="30" rx="2" fill="{_P04_TABS[k]}"/>'
                       + _pp_t(554, 760 + k * 54, s, 20, "procedure step", 276) for k, s in enumerate(steps)))
    fig = (px_sheet(60, 1120, 780, 280, PX_PAPER, 43) + px_pin(450, 1134)
           + TC(450, 1250, sl["figure"], fit(sl["figure"], 80, 700, "figure", floor=20), PX_INK, W6)
           + TCW(450, 1310, sl["label"], 42, 24, PX_INK, W6, 1.25))
    g = [land(doc, .1, .5), land(card_, .3, .5), land(fig, .5, .5, 0), land(_pp_minimap((0,), {}, 340, 1470), .9, .5, 10)]
    lens_ = (f'<g><animateTransform attributeName="transform" type="translate" '
             f'values="110 740;110 740;440 776;130 820;258 868;258 868;160 960;160 960;110 740" keyTimes="0;.18;.28;.37;.45;.55;.60;.97;1" '
             f'dur="{D}s" repeatCount="indefinite"/>{px_lens(0, 0, 36)}</g>')
    g.append(land(lens_, .8, .45, 0))
    strike = (f'<path d="M190 872 L326 863" pathLength="1" stroke-dasharray="1" stroke="{PX_RIBBON}" stroke-width="5" '
              f'stroke-linecap="round" fill="none">{_p04_draw(.48)}</path>')
    g.append(strike + f'<g>{_p04_on(.50)}{pill(420, 822, nosrc, "var(--c5)", ctx, 20, 150, "no source tag")}</g>')
    thread = (f'<path d="M322 890 C400 910 440 930 524 930" pathLength="1" stroke-dasharray="1" stroke="{PX_RIBBON}" '
              f'stroke-width="3.5" stroke-linecap="round" fill="none">{_p04_draw(.56)}</path>')
    line = (f'<rect x="524" y="900" width="304" height="60" rx="8" fill="none" stroke="{PX_RIBBON}" stroke-width="2.4"/>'
            + f'<path d="M538 930 L547 940 L563 920" fill="none" stroke="{PX_RIBBON}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
            + _pp_t(572, 938, new, 20, "new procedure step", 248))
    g.append(thread + f'<g>{_p04_on(.62)}<g>{_p04_in(.62, 0, 14)}{line}</g></g>')
    g.append(_pp_minimap((0,), {1: .72}, 340, 1470))
    return _pp_out(sl, g)


def _pp06_ruta(sl, ctx):
    """p06 stacked: the three accordion panels become three rows, each with its stop's drawing and its word; they
    unfold one after another and none closes, the padlock settles on the second, the ribbon threads the three."""
    words = sl["words"]
    W_, H_ = 760, 250
    panels = []
    for k in range(3):
        y, a = 680 + k * 280, .20 + k * .2
        c = 8 * (-1 if k % 2 else 1)
        fold = (f'<animateTransform attributeName="transform" type="skewX" values="{c};{c};0;0;{c}" '
                f'keyTimes="0;{a:.3f};{a + .06:.3f};.97;1" dur="{D}s" repeatCount="indefinite"/>')
        shade_ = f'<rect x="0" y="0" width="{W_}" height="{H_}" fill="var(--ink)" opacity=".16">{beat("opacity", [(0, .16), (a, .16), (a + .06, 0), (.97, 0), (1, .16)])}</rect>'
        word = (f'<g>{_p04_on(a + .05)}{_pp_t(460, 140, words[k], 48, "route word", 400, anchor="middle")}'
                f'<path d="M400 168 L520 168" stroke="{PX_RIBBON}" stroke-width="3" stroke-linecap="round"/></g>')
        body = px_sheet(0, 0, W_, H_, PX_PAPER, 50 + k) + px_icon(k, 130, H_ / 2, 1.8) + word + shade_
        panels.append(f'<g transform="translate(80 {y + H_ / 2})"><g>{fold}<g transform="translate(0 {-H_ / 2})">{body}</g></g></g>')
    g = [seq(panels, .1, .55, 20)]
    g.append(px_ribbon("M58 660 C34 780 82 880 58 1000 S34 1200 58 1300 S82 1440 58 1530", 3.5, .8, 1.0))
    g.append(f'<g>{_p04_on(.50)}<g>{_p04_in(.50, 0, -60, .07)}{_p06_lock(770, 1070)}</g></g>')
    return _pp_out(sl, g)


# ==================================================================================================== 07-09
def _pp07_automatizar(sl, ctx):
    """p07 stacked: four paper steps across the zone, rising left to right; the spark climbs and each step lights and
    stays lit; the small map lights its third stop; the note is pinned in the free corner."""
    steps = sl.get("steps", ["Prompt guardado", "Asistente", "Flujo entre sistemas", "Software propio"])
    note = sl.get("note", "Casi siempre, una mezcla")
    w, bottom = 190, 1520
    xs = [60 + k * 200 for k in range(4)]
    tops = [1300 - k * 130 for k in range(4)]
    lit_at = [.14, .30, .46, .62]
    parts = []
    for k in range(4):
        x, top, cx = xs[k], tops[k], xs[k] + w / 2
        z = fit(max(steps[k].split(), key=len), 24, w - 30, "automatizar step", floor=20)
        body = px_sheet(x, top, w, bottom - top, PX_PAPER, 41 + k)
        body += TCW(f"{cx:.1f}", f"{top + 38}", steps[k], max(6, int((w - 30) / (z * .56))), z, PX_INK, W6, 1.15)
        body += f'<g transform="translate({cx:.1f} {top + 136}) scale(1.35)">{_p07_glyph(k)}</g>'
        edge = (f'<path d="{px_sheet_path(x, top, w, bottom - top, 41 + k)}" fill="none" stroke="{PX_RIBBON}" stroke-width="3.5" '
                f'stroke-linejoin="round"/>')
        parts.append(body + f'<g>{_p07_on(lit_at[k])}{edge}</g>')
    g = [seq(parts, .1, .5, 22)]
    path = "M155 1278 Q255 1148 355 1148 Q455 1018 555 1018 Q655 888 755 888"
    shown = beat("opacity", [(0, 0), (.10, 0), (.12, 1), (.96, 1), (.97, 0), (1, 0)])
    stops = [(0, 0), (.22, 0), (.30, 1 / 3), (.38, 1 / 3), (.46, 2 / 3), (.54, 2 / 3), (.62, 1), (1, 1)]
    g.append(f'<g>{shown}{move(path, stops, D)}{glow(0, 0, 40, "var(--c4)", .7)}{spark(0, 0, 1.3, "var(--c4)")}</g>')
    mx, my = [640, 730, 820], 700
    mini = f'<path d="M{mx[0]} {my} H{mx[2]}" stroke="{PX_RIBBON}" stroke-width="3" stroke-linecap="round"/>'
    mini += px_icon(0, mx[0], my, .6, True) + px_icon(1, mx[1], my, .6, True) + px_icon(2, mx[2], my, .6, False)
    mini += f'<g>{_p07_on(.70)}{px_icon(2, mx[2], my, .6, True)}</g>'
    g.append(land(mini, .6, .5, 0))
    postit = px_postit(60, 680, 290, 150, PX_POSTIT, 7, -4, note, 26) + px_pin(205, 694)
    g.append(f'<g>{_p07_on(.76)}<g>{_p07_tr([(0, "0 -24"), (.76, "0 -24"), (.80, "0 0"), (1, "0 0")])}{postit}</g></g>')
    return _pp_out(sl, g)


def _pp08_lunes(sl, ctx):
    """p08 stacked: the calendar of four Mondays in a row on top, the status board below; at 8:00 the sealed envelope
    flies to the board, a Monday gets its check and a bar lands, four times; the envelope comes back sealed each time."""
    mondays = sl.get("mondays", ["Lun 1", "Lun 2", "Lun 3", "Lun 4"])
    hour = sl.get("hour", "8:00")
    fly = [.20, .37, .54, .71]
    cx0, cy0, cw, chh = 60, 690, 780, 380
    cal = px_sheet(cx0, cy0, cw, chh, PX_PAPER, 31)
    cal += "".join(f'<rect x="{x - 6}" y="{cy0 - 16}" width="12" height="30" rx="6" fill="none" stroke="{PX_INK}" stroke-width="2"/>'
                   for x in (cx0 + 100, cx0 + cw - 100))
    cal += _pp_t(cx0 + cw / 2, cy0 + 54, sl.get("calendar", "Lunes"), 30, "lunes calendar title", cw - 80, anchor="middle")
    cal += f'<path d="M{cx0 + 24} {cy0 + 74} H{cx0 + cw - 24}" stroke="{PX_RIBBON}" stroke-width="2.4"/>'
    cells = []
    for k in range(4):
        x, y = cx0 + 22 + k * 186, cy0 + 94
        c = f'<rect x="{x}" y="{y}" width="176" height="266" rx="6" fill="none" stroke="{PX_MUTED_INK}" stroke-width="1.4" opacity=".6"/>'
        c += _pp_t(x + 16, y + 38, mondays[k], 24, "lunes cell", 146)
        c += _pp_t(x + 16, y + 68, hour, 20, "lunes cell hour", 146, PX_MUTED_INK, bold=False)
        c += (f'<g>{_p07_on(fly[k] + .07)}<path d="M{x + 52} {y + 170} L{x + 78} {y + 198} L{x + 126} {y + 140}" fill="none" '
              f'stroke="{PX_RIBBON}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></g>')
        cells.append(c)
    g = [land(cal, .1, .5), seq(cells, .3, .45, 14, 1.3)]
    bx, by, bw, bh = 330, 1120, 510, 410
    board = px_sheet(bx, by, bw, bh, PX_PAPER, 33) + px_pin(bx + bw / 2, by + 18)
    board += _pp_t(bx + bw / 2, by + 66, sl.get("board", "Estado del proyecto"), 26, "lunes board title", bw - 50, anchor="middle")
    for j, f in enumerate((.92, .74, .58, .40)):
        y = by + 102 + j * 74
        board += px_lines(bx + 30, y, 200, 1, 0, None, ".45", 8)
        board += f'<rect x="{bx + 30}" y="{y + 22}" width="{bw - 60}" height="20" rx="10" fill="none" stroke="{PX_MUTED_INK}" stroke-width="1.2" opacity=".7"/>'
        board += f'<g>{_p07_on(fly[j] + .08)}<rect x="{bx + 30}" y="{y + 22}" width="{(bw - 60) * f:.0f}" height="20" rx="10" fill="{PX_RIBBON}"/></g>'
    g.append(land(board, .5, .5))
    g.append(land(_p08_clock(104, 1196, 22) + T(138, 1206, hour, fit(hour, 30, 150, "lunes hour", floor=20), "var(--white)", W6), .8, .45, 0))
    ex, ey, ew, eh = 70, 1330, 190, 124
    dx, dy = bx + bw / 2 - (ex + ew / 2), by + 230 - (ey + eh / 2)
    tr, op = [(0, "0 0")], [(0, 1)]
    for a in fly:
        tr += [(a, "0 0"), (a + .07, f"{dx:.0f} {dy:.0f}"), (a + .075, "0 0")]
        op += [(a + .05, 1), (a + .07, 0), (a + .08, 0), (a + .10, 1)]
    tr.append((1, "0 0"))
    op.append((1, 1))
    g.append(land(f'<g>{beat("opacity", op)}<g>{_p07_tr(tr)}{px_envelope(ex, ey, ew, eh, True)}</g></g>', 1.0, .5))
    return _pp_out(sl, g)


def _pp09_describir(sl, ctx):
    """p09 stacked: the folded report lands; its cover lifts and the sheet unfolds like a map into a 2x2 of four panels,
    other jobs that repeat, and the ribbon joins them in reading order; it folds back before the reset."""
    cover_t = sl.get("cover", "El informe")
    panels = sl.get("panels", ["Acta", "Correo", "Solicitud", "Reporte"])
    pw, ph = 390, 420
    pos = [(60 + (k % 2) * pw, 670 + (k // 2) * ph) for k in range(4)]
    out_at = [0, .30, .44, .58]
    shade2 = f"color-mix(in srgb, {PX_PAPER} 92%, var(--ink))"
    stack = []
    for k in (3, 2, 1, 0):
        (x, y), cx = pos[k], pos[k][0] + pw / 2
        p = px_sheet(x, y, pw, ph, PX_PAPER if k in (0, 3) else shade2, 51 + k)
        p += f'<g transform="translate({cx:.1f} {y + 170}) scale(1.6)">{_p09_glyph(k)}</g>'
        p += f'<circle cx="{cx:.1f}" cy="{y + 290}" r="8" fill="{PX_RIBBON}"/>'
        p += _pp_t(cx, y + 362, panels[k], 30, "describir panel", pw - 40, anchor="middle")
        if k:
            off = f"{pos[0][0] - x + 6 * k} {pos[0][1] - y + 6 * k}"
            a = out_at[k]
            p = f'<g>{_p07_tr([(0, off), (a, off), (a + .08, "0 0"), (.92, "0 0"), (.985, off), (1, off)])}{p}</g>'
        stack.append(p)
    g = [land("".join(stack), .1, .55)]
    dot = [(x + pw / 2, y + 290) for x, y in pos]
    joins = [f"M{dot[0][0] + 12:.0f} {dot[0][1]} C{dot[0][0] + 120:.0f} {dot[0][1] - 40} {dot[1][0] - 120:.0f} {dot[1][1] + 40} {dot[1][0] - 12:.0f} {dot[1][1]}",
             f"M{dot[1][0] - 12:.0f} {dot[1][1]} C{dot[1][0] - 175:.0f} {dot[1][1]} {dot[2][0] + 165:.0f} {dot[2][1] - 8} {dot[2][0] + 12:.0f} {dot[2][1] - 2}",
             f"M{dot[2][0] + 12:.0f} {dot[2][1] + 2} C{dot[2][0] + 120:.0f} {dot[2][1] + 40} {dot[3][0] - 120:.0f} {dot[3][1] - 40} {dot[3][0] - 12:.0f} {dot[3][1]}"]
    for k, d in zip((1, 2, 3), joins):
        a = out_at[k] + .09
        dash = beat("stroke-dashoffset", [(0, 1), (a, 1), (a + .06, 0), (.90, 0), (.92, 1), (1, 1)])
        g.append(f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{PX_RIBBON}" stroke-width="3.5" '
                 f'stroke-linecap="round">{dash}</path>')
    (x, y), cx = pos[0], pos[0][0] + pw / 2
    cover = (px_sheet(x, y, pw, ph, PX_PAPER, 50)
             + _pp_t(cx, y + 66, cover_t, 30, "describir cover", pw - 40, anchor="middle")
             + px_lines(x + 30, y + 110, pw - 60, 6, 32, None, ".45", 8)
             + f'<path d="M{x + 30} {y + 330} H{x + pw - 30}" stroke="{PX_RIBBON}" stroke-width="3.5" stroke-linecap="round"/>')
    lift = beat("opacity", [(0, 1), (.20, 1), (.25, 0), (.975, 0), (1, 1)])
    move_up = _p07_tr([(0, "0 0"), (.20, "0 0"), (.25, "-30 -40"), (.975, "-30 -40"), (1, "0 0")])
    g.append(land(f'<g>{lift}<g>{move_up}{cover}</g></g>', .3, .5))
    return _pp_out(sl, g)


# ==================================================================================================== 10-12
def _pp10_costo(sl, ctx):
    """p10 stacked: the fixed figure on top, the two-bar chart under it; only the coin shrinks on its way to the
    sliver, the ribbon underlines the gap. The figure and the bars never move."""
    fig, label, years = sl["figure"], sl["label"], sl["years"]
    frame = (px_sheet(60, 670, 780, 240, PX_PAPER_2, 41)
             + TC(450, 800, fig, fit(fig, 100, 720, "cost figure", floor=20), PX_INK, W6)
             + TC(450, 862, label, fit(label, 26, 720, "cost figure label", floor=20), PX_MUTED_INK, W6))
    pulse = (f'<rect x="76" y="686" width="748" height="208" rx="6" fill="none" stroke="{PX_RIBBON}" stroke-width="1.8">'
             f'{loop("stroke-opacity", ".1;.55;.1", 4)}</rect>')
    g = [land(frame + pulse, .1, .5)]
    base, bx0, bx1, bw, top = 1410, 150, 530, 200, 1030
    h1 = base - top
    h2 = max(h1 / 280, 3)
    bar_fill = "color-mix(in srgb, var(--c2) 45%, var(--white))"
    chart = px_sheet(60, 950, 780, 580, PX_PAPER, 42) + f'<path d="M100 {base} H800" stroke="{PX_EDGE}" stroke-width="1.8"/>'
    bar1 = (px_sheet(bx0, top, bw, h1, bar_fill, 43, shadow=False)
            + f'<path d="{px_sheet_path(bx0, top, bw, h1, 43)}" fill="none" stroke="{PX_INK}" stroke-width="1.2" opacity=".5"/>')
    bar2 = f'<rect x="{bx1}" y="{base - h2:.1f}" width="{bw}" height="{h2:.1f}" fill="{bar_fill}" stroke="{PX_INK}" stroke-width="1.4"/>'
    yl = "".join(_pp_t(x + bw / 2, base + 56, y, 30, "chart year", 180, anchor="middle") for x, y in zip((bx0, bx1), years))
    g.append(land(chart, .25, .5) + land(bar1, .45, .5, 0) + land(bar2 + yl, .6, .5, 0))
    gap = f"M{bx0 + bw + 6} {top + 4} C{bx0 + bw + 130} {top + 12} {bx1 - 50} {base - 170} {bx1 - 6} {base - 8}"
    g.append(f'<g>{loop("opacity", ".75;1;.75", 5)}{px_ribbon(gap, 3.5, .9, .8)}</g>')
    sx, sy = bx1 + bw / 2, base - 6
    g.append(_n04_ping(sx, sy, 12, 90, PX_RIBBON, (.42, .62), .12, .7))
    p0, p1, fl = (bx0 + bw / 2, top - 34), (sx, base - 56), (.17, .40)
    tr = _p10_tr("translate", [(0, f"{p0[0]} {p0[1]}"), (fl[0], f"{p0[0]} {p0[1]}"), (fl[0] + (fl[1] - fl[0]) * .5, f"{(p0[0] + p1[0]) / 2} {p0[1] - 40}"),
                               (fl[1], f"{p1[0]} {p1[1]}"), (.98, f"{p1[0]} {p1[1]}"), (1, f"{p0[0]} {p0[1]}")])
    sc = _p10_tr("scale", [(0, "1"), (fl[0], "1"), (fl[1], ".4"), (.98, ".4"), (1, "1")])
    g.append(land(f'<g>{tr}<g>{sc}<g>{bob(0, -6, 3)}{_p10_coin(34)}</g></g></g>', 1.2, .45, 0))
    return _pp_out(sl, g)


def _pp11_ruido(sl, ctx):
    """p11 stacked: the feed of loud posts on top, the two evidence notes side by side under it; the ribbon strikes the
    posts one by one, then each note, its figures fixed from the start, gets its pin."""
    g = [land(px_sheet(60, 660, 780, 440, PX_PAPER_2, 51) + _pp_t(86, 704, sl["feed"], 22, "feed header", 700, PX_MUTED_INK), .1, .5)]
    y0 = 724
    for k, (post, t) in enumerate(zip(sl["posts"], (.12, .22, .32))):
        lines = _p11_wrap(post, 28, 680)
        hh = 64 + 34 * len(lines)
        card_ = (px_sheet(84, y0, 732, hh, PX_PAPER, 52 + k, shadow=False)
                 + f'<circle cx="114" cy="{y0 + 28}" r="14" fill="color-mix(in srgb, var(--c2) 45%, var(--white))" stroke="{PX_INK}" stroke-width="1.2"/>'
                 + px_lines(140, y0 + 20, 150, 2, 13, None, ".4", 5)
                 + "".join(T(104, y0 + 82 + i * 34, line, 28, PX_INK, W6) for i, line in enumerate(lines)))
        g.append(land(card_, .3 + k * .15, .45))
        for i, line in enumerate(lines):
            ym, x1 = y0 + 72 + i * 34, 104 + min(680, bold_width(_(line), 28, current_factor())) + 10
            d = f"M96 {ym + 3} C{96 + (x1 - 96) * .3:.0f} {ym - 6} {96 + (x1 - 96) * .6:.0f} {ym + 8} {x1:.0f} {ym - 2}"
            ti = t + i * .03
            g.append(f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{PX_RIBBON}" stroke-width="6" stroke-linecap="round">'
                     f'{beat("stroke-dashoffset", [(0, 1), (ti, 1), (ti + .03, 0), (.98, 0), (1, 1)])}</path>')
        y0 += hh + 14
    for k, (note, t) in enumerate(zip(sl["cards"], (.44, .56))):
        x, y, w, h = (60, 460)[k], 1140, 380, 380
        body = (px_sheet(x, y, w, h, PX_PAPER if k == 0 else PX_PAPER_LILA, 55 + k)
                + _pp_t(x + 24, y + 62, note["title"], 26, "evidence note title", w - 48)
                + f'<path d="M{x + 24} {y + 82} H{x + 130}" stroke="{PX_RIBBON}" stroke-width="3.5" stroke-linecap="round"/>'
                + "".join(_pp_t(x + 24, y + 136 + j * 50, line, 30, "evidence figure", w - 48) for j, line in enumerate(note["lines"])))
        if note.get("small"):
            body += _pp_t(x + 24, y + 244, note["small"], 20, "evidence scope", w - 48, PX_MUTED_INK, bold=False)
        body += _pp_scale((_p11_doc if k == 0 else _p11_research)(0, 0), x + w - 80, y + h - 70, 1.3)
        g.append(land(f'<g transform="rotate({(-1.5, 1.2)[k]} {x + w / 2} {y + h / 2})">{body}</g>', .5 + k * .2, .5))
        px, py = x + w / 2, y + 18
        g.append(f'<g opacity="0">{beat("opacity", _n04_win(t, f=.01))}<g>{_p10_tr("translate", [(0, "0 -34"), (t, "0 -34"), (t + .02, "0 0"), (1, "0 0")])}'
                 f'{px_pin(px, py)}</g></g>' + _n04_ping(px, py, 8, 50, PX_RIBBON, (t + .02,), .1, .8))
    return _pp_out(sl, g)


def _pp12_exito(sl, ctx):
    """p12 stacked: the roll of nine use cases unrolls on top in two columns; the picked line lifts on its strip and flies
    down to the success case card, which grows from it; its four fields fill one by one (the KPI static, with its tag),
    the gauge's needle moves from «before» to «after», the pin lands."""
    cases, pick = sl["cases"], sl["pick"]
    kpi = sl["kpi"] if isinstance(sl["kpi"], dict) else {"k": "KPI", "v": sl["kpi"]}
    fields = [*sl["fields"], kpi]
    ip = cases.index(pick)
    x0, w, y0, y1 = 60, 780, 700, 1000
    unroll = (.02, .16)
    per = (len(cases) + 1) // 2
    at = [(x0 + 44 + (k // per) * 380, y0 + 56 + (k % per) * 50) for k in range(len(cases))]
    fade = [(0, 1), (.25, 1), (.29, .35), (_P12_RESET, .35), (.985, 1), (1, 1)]
    mark = lambda x, y: (f'<rect x="{x - 24}" y="{y - 13}" width="12" height="12" rx="2" fill="{PX_MUTED_INK}" opacity=".6"/>'
                         f'<path d="M{x - 24} {y + 17} H{x + 330}" stroke="{PX_EDGE}" stroke-width="1.2" stroke-dasharray="3 6"/>')
    marks = "".join(mark(x, y) for k, (x, y) in enumerate(at) if k != ip)
    words = "".join(_pp_t(x, y, c, 20, "p12 use case", 330, PX_MUTED_INK, bold=False) for k, (c, (x, y)) in enumerate(zip(cases, at)) if k != ip)
    ox, oy = at[ip]
    own = (f'<g>{beat("opacity", [(0, 1), (.19, 1), (.2, 0), (_P12_RESET, 0), (.985, 1), (1, 1)])}' + mark(ox, oy)
           + _pp_t(ox, oy, pick, 20, "p12 use case", 330, PX_MUTED_INK, bold=False) + '</g>')
    sw = min(350, bold_width(_(str(pick)), 20, current_factor()) + 30)
    slot = (f'<g opacity="0">{_p12_hold(.26)}<rect x="{ox - 14}" y="{oy - 27}" width="{sw:.0f}" height="40" rx="4" fill="none" '
            f'stroke="{PX_RIBBON}" stroke-width="1.8" stroke-dasharray="6 5"/></g>')
    clip_h = beat("height", [(0, 26), (unroll[0], 26), (unroll[1], y1 - y0 + 12), (.975, y1 - y0 + 12), (.995, 26), (1, 26)])
    sheet = (f'<defs><clipPath id="pp12-roll-clip"><rect x="{x0 - 20}" y="{y0}" width="{w + 40}" height="{y1 - y0 + 12}">{clip_h}</rect></clipPath></defs>'
             f'<g clip-path="url(#pp12-roll-clip)">{px_sheet(x0, y0, w, y1 - y0, PX_PAPER, 61)}'
             f'<g>{beat("opacity", fade)}{marks}</g>{words}{own}{slot}</g>')
    curl = (f'<g>{_p10_tr("translate", [(0, "0 0"), (unroll[0], "0 0"), (unroll[1], f"0 {y1 - y0 - 26}"), (.975, f"0 {y1 - y0 - 26}"), (.995, "0 0"), (1, "0 0")])}'
            f'<rect x="{x0 - 6}" y="{y0 + 16}" width="{w + 12}" height="18" rx="9" fill="{PX_PAPER_2}" stroke="{PX_EDGE}" stroke-width="1.2"/></g>')
    roller = (f'<rect x="{x0 + PX_SH[0] - 20}" y="{y0 - 30 + PX_SH[1]}" width="{w + 40}" height="44" rx="22" fill="{PX_SHADOW}"/>'
              f'<rect x="{x0 - 20}" y="{y0 - 30}" width="{w + 40}" height="44" rx="22" fill="{PX_PAPER_2}" stroke="{PX_EDGE}" stroke-width="1.4"/>'
              f'<ellipse cx="{x0}" cy="{y0 - 8}" rx="9" ry="22" fill="none" stroke="{PX_EDGE}" stroke-width="1.4"/>'
              f'<ellipse cx="{x0 + w}" cy="{y0 - 8}" rx="9" ry="22" fill="none" stroke="{PX_EDGE}" stroke-width="1.4"/>')
    g = [land(sheet + curl + roller, .1, .5, -14)]
    cx0, cy0, cw, ch = 60, 1060, 780, 460
    tx, ty, room = cx0 + 28, cy0 + 96, cw - 56
    card_ = (px_sheet(cx0, cy0, cw, ch, "var(--white)", 62) + _pp_t(tx, cy0 + 50, sl["card"], 22, "p12 card label", room, PX_RIBBON)
             + "".join(f'<path d="M{tx} {cy0 + 194 + j * 80} H{cx0 + cw - 28}" stroke="{PX_EDGE}" stroke-width="1.4" stroke-dasharray="4 6"/>'
                       for j in range(len(fields) - 1)))
    g.append(f'<g opacity="0">{_p12_hold(.33, f=.02)}<g transform="translate({tx} {ty})"><g>'
             + _p10_tr("scale", [(0, ".15"), (.33, ".15"), (.38, "1"), (_P12_RESET, "1"), (.985, ".15"), (1, ".15")])
             + f'<g transform="translate({-tx} {-ty})">{card_}</g></g></g></g>')
    gx, gy = cx0 + cw - 105, cy0 + 262
    for j, (fld, t) in enumerate(zip(fields, (.41, .48, .55, .62))):
        yl = cy0 + 150 + j * 80
        row = (_pp_t(tx, yl, fld["k"], 20, "p12 field label", 200, PX_MUTED_INK)
               + _pp_t(tx, yl + 30, fld["v"], 22, "p12 field value", 560 if j < 2 else room, PX_INK, bold=False))
        if fld.get("tag"):
            tw_ = bold_width(_(str(fld["tag"])), 20, current_factor()) + 36
            row += pill(cx0 + cw - 28 - tw_ / 2, yl - 7, fld["tag"], "var(--c4)", ctx, 20, 140, "p12 example tag")
        g.append(f'<g opacity="0">{_p12_hold(t)}<g>'
                 + _p10_tr("translate", [(0, "0 10"), (t, "0 10"), (t + .03, "0 0"), (_P12_RESET, "0 0"), (.985, "0 10"), (1, "0 10")])
                 + row + '</g></g>')
    g.append(f'<g opacity="0">{_p12_hold(.62)}{_pp_scale(_p12_gauge(0, 0, 42, sl["gauge"], .67, .75), gx, gy, 1.34)}</g>')
    g.append(_n04_ping(gx, gy - 40, 12, 70, PX_RIBBON, (.75,), .1, .7))
    strip = (px_sheet(-14, -27, sw, 40, "var(--white)", 63) + '<path d="M-14 -27 h7 v40 h-7 Z" fill="' + PX_RIBBON + '"/>'
             + _pp_t(0, 0, pick, 20, "p12 lifted case", 330))
    dx, dy = tx - ox, ty - oy
    fly = [(0, "0 0"), (.25, "0 0"), (.30, f"{dx * .5 + 120:.0f} {dy * .5:.0f}"), (.34, f"{dx} {dy}"), (_P12_RESET, f"{dx} {dy}"), (.985, "0 0"), (1, "0 0")]
    sc = [(0, "1"), (.25, "1"), (.34, "1.12"), (_P12_RESET, "1.12"), (.985, "1"), (1, "1")]
    g.append(f'<g opacity="0">{_p12_hold(.19, f=.01)}<g transform="translate({ox} {oy})"><g>{_p10_tr("translate", fly)}'
             f'<g>{_p10_tr("scale", sc)}{strip}</g></g></g></g>')
    g.append(_n04_ping(ox + sw / 2 - 14, oy - 7, 12, 90, PX_RIBBON, (.2,), .1, .8))
    px_, py_ = cx0 + cw / 2, cy0 + 22
    g.append(f'<g opacity="0">{beat("opacity", _n04_win(.76, f=.01))}<g>{_p10_tr("translate", [(0, "0 -34"), (.76, "0 -34"), (.78, "0 0"), (1, "0 0")])}'
             f'{px_pin(px_, py_)}</g></g>' + _n04_ping(px_, py_, 8, 52, PX_RIBBON, (.78,), .1, .8))
    return _pp_out(sl, g)


# ==================================================================================================== 13-15
def _pp13_turno(sl, ctx):
    """p13 stacked: the diagnosis sheet of seven lenses full width, the task card walking its right column and ticking
    lens by lens; under it the three trays (the ticked «how» ones light), the final line and the two-minute clock."""
    lenses, trays = sl["lenses"], sl["trays"]
    x0, y0, w, h = 60, 660, 780, 580
    ix, qx, bx = x0 + 40, x0 + 78, 560
    rows, y = [], y0 + 54
    for k, ln in enumerate(lenses):
        if k and ln.get("hint") and not lenses[k - 1].get("hint"):
            y += 14
            rows.append({"divider": y - 34})
        cy = y + 8 if ln.get("hint") else y - 7
        rows.append({"k": k, "y": y, "cy": cy, "band": 76 if ln.get("hint") else 50})
        y += 88 if ln.get("hint") else 58
    lens_rows = [r for r in rows if "k" in r]
    g = [land(px_sheet(x0, y0, w, h, PX_PAPER, 35), .1, .5)]
    parts = []
    for r in rows:
        if "divider" in r:
            parts.append(f'<path d="M{x0 + 26} {r["divider"]} H{x0 + w - 26}" stroke="{PX_EDGE}" stroke-width="1.4" stroke-dasharray="4 6"/>')
            continue
        ln = lenses[r["k"]]
        p = (_pp_scale(_p13_icon(ln["icon"], 0, 0), ix, r["cy"], 1.3)
             + _pp_t(qx, r["y"], ln["q"], 22, "p13 lens question", bx - qx - 16)
             + f'<rect x="{bx}" y="{r["cy"] - 15}" width="30" height="30" rx="4" fill="var(--white)" stroke="{PX_MUTED_INK}" stroke-width="1.4"/>')
        if ln.get("hint"):
            p += _pp_t(qx, r["y"] + 28, ln["hint"], 20, "p13 lens hint", bx - qx - 16, PX_MUTED_INK, bold=False)
        parts.append(p)
    g.append(seq(parts, .25, .45, 10, 1.6))
    t_at = [.16 + .07 * k for k in range(len(lens_rows))]
    cw, chh, cx = 236, 80, 604
    tops = [r["cy"] - chh / 2 for r in lens_rows]
    tr = [(0, "0 0")]
    for k in range(1, len(tops)):
        tr += [(t_at[k] - .04, f"0 {tops[k - 1] - tops[0]:.0f}"), (t_at[k] - .01, f"0 {tops[k] - tops[0]:.0f}")]
    tr += [(_P13_RESET, f"0 {tops[-1] - tops[0]:.0f}"), (.985, "0 0"), (1, "0 0")]
    for k, (r, t) in enumerate(zip(lens_rows, t_at)):
        b = t_at[k + 1] - .04 if k + 1 < len(t_at) else .62
        band = (f'<path d="M{x0 + 12} {r["cy"] - r["band"] / 2:.0f} h{w - 24} v{r["band"]} h{-(w - 24)} Z" '
                f'fill="color-mix(in srgb, var(--c4) 26%, transparent)"/>')
        g.insert(2, f'<g opacity="0">{_p13_on(t - .012, b, .012)}{band}</g>')
        if lenses[r["k"]].get("tick"):
            g.append(f'<g opacity="0">{_p13_on(t)}{check(bx + 15, r["cy"], 1.1, PX_RIBBON)}</g>'
                     + _n04_ping(bx + 15, r["cy"], 12, 46, PX_RIBBON, (t,), .08, .8))
        else:
            g.append(f'<g opacity="0">{_p13_on(t)}<path d="M{bx + 8} {r["cy"]} H{bx + 22}" stroke="{PX_MUTED_INK}" '
                     f'stroke-width="2.8" stroke-linecap="round"/></g>')
    g.append(land(f'<g>{_p13_tr("translate", tr)}{px_postit(cx, tops[0], cw, chh, PX_POSTIT, 34, -1.5, sl["task"], 20)}</g>', .6, .5, 0, 16))
    hows = [r for r in lens_rows if lenses[r["k"]].get("hint")][-len(trays):]
    ty0, th, tw, tg = 1270, 106, 250, 15
    for j, (lab, r) in enumerate(zip(trays, hows)):
        tx = x0 + j * (tw + tg)
        tray = px_sheet(tx, ty0, tw, th, PX_PAPER_2, 36 + j) + f'<path d="M{tx + 8} {ty0 + th - 10} H{tx + tw - 8}" stroke="{PX_EDGE}" stroke-width="1.4"/>'
        body = _pp_scale(_p13_icon(lenses[r["k"]]["icon"], 0, 0), tx + 34, ty0 + 34, 1.3) + _pp_t(tx + tw / 2, ty0 + 84, lab, 20, "p13 tray", tw - 20, anchor="middle")
        lit = ""
        if lenses[r["k"]].get("tick"):
            t = .635 + .04 * j
            glowp = (f'<path d="{px_sheet_path(tx, ty0, tw, th, 36 + j)}" fill="color-mix(in srgb, var(--accent) 14%, var(--white))" '
                     f'stroke="{PX_RIBBON}" stroke-width="2.8" stroke-linejoin="round"/>' + check(tx + tw - 24, ty0 + 26, .85, PX_RIBBON))
            lit = f'<g opacity="0">{_p13_on(t)}{glowp}</g>' + _n04_ping(tx + tw / 2, ty0 + th / 2, 30, 130, PX_RIBBON, (t,), .1, .6)
        g.append(land(tray + lit + body, .5 + .1 * j, .45, 12))
    fy = 1396
    fin = px_sheet(x0, fy, w, 58, PX_PAPER, 39) + _pp_t(x0 + 24, fy + 38, sl["close"], 21, "p13 final line", w - 48)
    g.append(f'<g opacity="0">{_p13_on(.75)}'
             + _p13_tr("translate", [(0, "0 12"), (.75, "0 12"), (.78, "0 0"), (_P13_RESET, "0 0"), (.985, "0 12"), (1, "0 12")])
             + fin + '</g>')
    g.append(f'<path d="M{x0 + 24} {fy + 47} H{x0 + w - 24}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{PX_RIBBON}" '
             f'stroke-width="2.8" stroke-linecap="round">{beat("stroke-dashoffset", [(0, 1), (.77, 1), (.84, 0), (_P13_RESET, 0), (.985, 1), (1, 1)])}</path>')
    ccx, ccy = 800, 1500
    g.append(land(_p13_clock(ccx, ccy, 30), .8, .5, 12))
    g.append(land(T(ccx - 46, ccy + 8, sl["clock"], fit(sl["clock"], 24, 360, "p13 clock", floor=20), "var(--white)", f'text-anchor="end" {W6}'), .9, .45, 0))
    return _pp_out(sl, g)


def _pp14_tiempo(sl, ctx):
    """p14 stacked: the three wordless ideas and the bulb above, the paper week below; the ribbon cuts Monday's block
    out, the piece settles beside the calendar leaving its hole, the bulb pops up from the hole and lights, and the
    ideas appear around it: two people talking, a plan, a plant that grows."""
    ok = ctx.brand.c("dark.ok")
    x0, y0, w, h = 220, 1070, 620, 380
    hy = y0 + 56
    cw = (w - 32) / 5
    cols = [x0 + 16 + k * cw for k in range(5)]
    cal = [px_sheet(x0, y0, w, h, PX_PAPER, 41),
           f'<rect x="{cols[0]:.1f}" y="{hy + 4}" width="{cw:.1f}" height="200" fill="var(--c4)" opacity=".22"/>',
           f'<path d="M{x0 + 16} {hy} H{x0 + w - 16}" stroke="{PX_INK}" stroke-width="1.4"/>']
    for k, day in enumerate(sl["days"][:5]):
        cal.append(_pp_t(cols[k] + cw / 2, hy - 18, day, 22, "p14 day", cw - 10, PX_RIBBON if k == 0 else PX_INK, "middle"))
        if k:
            cal.append(f'<path d="M{cols[k]:.1f} {hy + 8} V{y0 + h - 14}" stroke="{PX_EDGE}" stroke-width="1.2"/>')
    for r in (1, 2):
        cal.append(f'<path d="M{x0 + 16} {hy + r * 100} H{x0 + w - 16}" stroke="{PX_EDGE}" stroke-width="1.2" stroke-dasharray="3 5"/>')
    busy = ((1, 0, 60, "var(--c2)"), (1, 1, 90, "var(--c3)"), (2, 0, 90, "var(--c2)"), (3, 1, 50, "var(--c3)"), (3, 2, 80, "var(--c2)"),
            (4, 0, 70, "var(--c3)"), (4, 2, 90, "var(--c2)"), (2, 2, 60, "var(--c3)"))
    for c, r, hh, col in busy:
        bx, by = cols[c] + 6, hy + 8 + r * 100
        cal.append(f'<rect x="{bx:.1f}" y="{by}" width="{cw - 12:.1f}" height="{hh}" rx="6" fill="color-mix(in srgb, {col} 45%, var(--white))"/>'
                   + px_lines(bx + 10, by + 14, cw - 36, 2, 14, PX_MUTED_INK, ".4", 5))
    g = [land("".join(cal), .1, .55)]
    bx, by, bw, bh = cols[0] + 6, hy + 8, cw - 12, 88
    hole = (f'<rect x="{bx:.1f}" y="{by}" width="{bw:.1f}" height="{bh}" rx="3" fill="color-mix(in srgb, var(--ink) 88%, var(--c1))"/>'
            f'<path d="M{bx:.1f} {by + bh} V{by} H{bx + bw:.1f}" fill="none" stroke="{PX_SHADOW}" stroke-width="9" stroke-linejoin="round"/>')
    g.append(f'<g opacity="0">{_p13_on(.29)}{hole}</g>')
    cut = (f'<path d="M{bx:.1f} {by} H{bx + bw:.1f} V{by + bh} H{bx:.1f} Z" pathLength="1" stroke-dasharray="1" fill="none" stroke="{PX_RIBBON}" '
           f'stroke-width="3" stroke-linejoin="round">{beat("stroke-dashoffset", [(0, 1), (.18, 1), (.28, 0), (_P13_RESET, 0), (.985, 1), (1, 1)])}</path>')
    title, dur = sl["block"]
    pcx, pcy = bx + bw / 2, by + bh / 2
    piece = (px_sheet(bx, by, bw, bh, PX_POSTIT, 42)
             + _pp_t(pcx, by + 38, title, 20, "p14 block", bw - 10, anchor="middle")
             + _pp_t(pcx, by + 66, dur, 20, "p14 block", bw - 10, PX_MUTED_INK, "middle"))
    dx, dy = 70 - bx, 1340 - by
    lift = [(0, "0 0"), (.3, "0 0"), (.33, "12 -36"), (.4, f"{dx:.0f} {dy:.0f}"), (_P13_RESET, f"{dx:.0f} {dy:.0f}"), (.985, "0 0"), (1, "0 0")]
    turn = [(0, f"0 {pcx:.1f} {pcy:.1f}"), (.3, f"0 {pcx:.1f} {pcy:.1f}"), (.4, f"-9 {pcx:.1f} {pcy:.1f}"),
            (_P13_RESET, f"-9 {pcx:.1f} {pcy:.1f}"), (.985, f"0 {pcx:.1f} {pcy:.1f}"), (1, f"0 {pcx:.1f} {pcy:.1f}")]
    g.append(land(f'<g>{_p13_tr("translate", lift)}<g>{_p13_tr("rotate", turn)}{piece}</g></g>', .35, .45, 0))
    g.append(cut)
    bulb_x, bulb_y = 450, 1000
    stalk = f"M{pcx:.1f} {pcy:.1f} C{pcx:.1f} {pcy - 90:.1f} {bulb_x} {bulb_y + 80} {bulb_x} {bulb_y}"
    g.append(f'<path d="{stalk}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{PX_RIBBON}" stroke-width="3.5" stroke-linecap="round">'
             f'{beat("stroke-dashoffset", [(0, 1), (.4, 1), (.52, 0), (_P13_RESET, 0), (.985, 1), (1, 1)])}</path>')
    g.append(f'<g opacity="0">{_p13_on(.55, f=.04)}{glow(bulb_x, bulb_y - 105, 200, "var(--c4)", .7)}</g>')
    unlit, lit = _p14_bulb()
    g.append(f'<g opacity="0">{_p13_on(.4)}'
             f'<animateMotion dur="{D}s" repeatCount="indefinite" path="{stalk}" keyTimes="0;.4;.52;1" keyPoints="0;0;1;1" calcMode="linear"/>'
             f'<g>{_p13_tr("scale", [(0, ".4 .4"), (.4, ".4 .4"), (.52, "1 1"), (1, "1 1")])}<g transform="scale(1.25)">'
             f'{unlit}<g opacity="0">{_p13_on(.55, f=.04)}{lit}</g></g></g></g>')
    g.append(_p13_pop(_pp_scale(_p14_pair(), 0, 0, 1.3), 170, 830, .62))
    g.append(_p13_pop(_pp_scale(_p14_plan(), 0, 0, 1.3), 730, 790, .7))
    g.append(_p13_pop(_pp_scale(_p14_plant(.78, ok), 0, 0, 1.3), 730, 996, .78))
    return _pp_out(sl, g)


def _pp15_lema(sl, ctx):
    """p15 stacked: the client's logo on top, the strategy map under it (three stops on the ribbon), the signer and the
    sign at the bottom; the paper plane returns, flies the route lighting each stop and lands on the last one."""
    g = [land(px_logo_client(450, 660, 300), .1, .5)]
    mx, my, mw, mh = 60, 880, 780, 330
    stops = ((180, my + 190), (450, my + 110), (720, my + 190))
    route = [stops[0], ((280, my + 100), (360, my + 90), stops[1]), ((550, my + 120), (620, my + 200), stops[2])]
    sheet = (px_sheet(mx, my, mw, mh, PX_PAPER, 51)
             + "".join(f'<path d="M{x} {my + 8} V{my + mh - 8}" stroke="{PX_EDGE}" stroke-width="1.2" stroke-dasharray="4 6"/>' for x in (320, 580)))
    g.append(land(sheet, .25, .5))
    g.append(px_ribbon(f"M{mx + 24} {my + mh - 24} C{mx + 60} {my + mh - 32} {stops[0][0] - 50} {stops[0][1] + 24} {stops[0][0]} {stops[0][1]}", 3.5, .45, .35, 'opacity=".6"'))
    g.append(px_ribbon(_p15_d(route), 4.5, .7, .9))
    icons = [px_icon(k, x, y, 1.25) + _pp_t(x, y + 82, lab, 26, "p15 stop", 240, anchor="middle")
             for k, ((x, y), lab) in enumerate(zip(stops, sl["stops"][:3]))]
    g.append(seq(icons, .45, .45, 14, 1.4))
    lift = 76
    fly = [(80, my + 40), ((130, my + 24), (150, my + 100), (stops[0][0], stops[0][1] - lift)),
           ((280, my + 100 - lift), (360, my + 90 - lift), (stops[1][0], stops[1][1] - lift)),
           ((560, my + 40), (650, stops[2][1] - 64), (stops[2][0], stops[2][1] - 64))]
    fr = _p15_bez(fly)
    t0, t1 = .14, .7
    for k, ((x, y), f) in enumerate(zip(stops, fr)):
        g.append(f'<g opacity="0">{_p13_on(t0 + (t1 - t0) * f)}{px_icon(k, x, y, 1.25, lit=True)}</g>')
    g.append(f'<g opacity="0">{_p13_on(t0 - .02)}'
             f'<animateMotion dur="{D}s" repeatCount="indefinite" path="{_p15_d(fly)}" rotate="auto" keyTimes="0;{t0};{t1};1" keyPoints="0;0;1;1" '
             f'calcMode="linear"/>{px_plane(0, 0, .85)}</g>')
    ring = (f'<ellipse cx="{stops[2][0]}" cy="{stops[2][1] - 46}" rx="50" ry="9" fill="none" stroke="{PX_RIBBON}" stroke-width="1.8">'
            f'{beat("rx", [(0, 22), (t1, 22), (t1 + .06, 66), (1, 66)])}</ellipse>')
    g.append(f'<g opacity="0">{beat("opacity", [(0, 0), (t1, 0), (t1 + .01, .9), (t1 + .06, 0), (1, 0)])}{ring}</g>')
    g.append(land(px_signer(390, 1250, 120, sl["name"], sl["role"], ctx, (26, 22), 780, 20), .6, .5))
    s = sl["sign"]
    g.append(f'<g opacity="0">{_p13_on(t1 + .05, f=.04)}'
             + TC(450, 1512, s, fit(s, 24, 780, "p15 sign", floor=20), "var(--muted)", f'font-style="italic" {W6}') + '</g>')
    return _pp_out(sl, g)

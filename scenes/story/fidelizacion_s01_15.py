"""Harvested from the fidelización Demo Day deck (cierre-training, 2026-09): the fifteen scenes of a closing keynote,
drawn with the world «papel» (worlds/papel.py: px_* kit, loaded before this file). Aliases in ext.py:

  paper-hero        p01_portada      a sheet on Friday folds into a paper plane, crosses the week, lands as a sealed envelope
  pinned-request    p02_viernes      a cork board fills with post-its; at 3:30 the red one arrives and is pinned
  strategy-map      p03_estrategia   the red post-it at the start of a map that unfolds; the ribbon traces three icon stops
  explain-cards     p04_explicar     a one-line ask gets a hollow template; three context cards fill it: a procedure
  review-lens       p05_revisar      the lens stops on an unsourced number and strikes it; the procedure gains a step
  route-named       p06_ruta         three accordion panels with the map's icons open and get their words; a padlock
  automation-stairs p07_automatizar  four paper steps of automation lit by a climbing spark; «casi siempre, una mezcla»
  mondays-sent      p08_lunes        at 8:00 the sealed envelope flies to the board, a Monday gets its check, four times
  unfold-describe   p09_describir    the folded sheet unfolds into four panels, other jobs that repeat
  cost-drop         p10_costo        a static figure and two bars; only a coin shrinks on its way to the sliver
  noise-vs-evidence p11_ruido        the ribbon strikes a feed of loud posts; two notes with static figures get pinned
  success-case      p12_exito        a roll of named use cases; one becomes the success case card, KPI and gauge
  diagnostic        p13_turno        a self-diagnosis sheet of seven lenses; a task card ticks them; trays light up
  time-freed        p14_tiempo       the ribbon cuts the freed block out of the week; a paper bulb lights; three ideas
  lema-signer       p15_lema         the client's logo leads; the plane flies the map and lands; the signer signs

The strategy map (px_icon, three stops) is a continuity object: 3 draws it, 4 to 7 carry it small and light one stop
each, 6 names it, 15 flies it. Every loop is one 12-second story timed with beat(); the 10.8 s frame is its resolved
state. Private helpers are _pNN_*; labels come from the slide args. Reuses _n04_win / _n04_ping (energia_s04_06.py).
"""


# ==================================================================================================== slides 01-03
def _p01_on(a, b=1.0, f=.02):
    """Opacity 1 between fractions a and b of the loop; b >= .97 holds until the loop resets."""
    if b >= .97:
        return beat("opacity", [(0, 0), (a, 0), (a + f, 1), (.97, 1), (1, 0)])
    return beat("opacity", [(0, 0), (a, 0), (a + f, 1), (b, 1), (b + f, 0), (1, 0)])


def _p01_tr(pairs, typ="translate"):
    """A transform loop with explicit times: pairs = [(fraction, value)] from 0 to 1."""
    kt = ";".join(f"{t:.3f}" for t, _ in pairs)
    return (f'<animateTransform attributeName="transform" type="{typ}" values="{";".join(v for _, v in pairs)}" '
            f'keyTimes="{kt}" dur="{D}s" repeatCount="indefinite"/>')


def _p01_drop(inner, a, dy=-70, dx=0):
    """inner falls into its final pose at fraction a of the loop and stays until the reset."""
    return (f'<g>{_p01_on(a, 1, .03)}<g>{_p01_tr([(0, f"{dx} {dy}"), (a, f"{dx} {dy}"), (a + .045, "0 0"), (.97, "0 0"), (1, f"{dx} {dy}")])}'
            f'{inner}</g></g>')


def _p01_draw(d, a, b, color=PX_RIBBON, width=3, extra=""):
    """A stroke that draws itself between fractions a and b of the loop and stays drawn until the reset."""
    return (f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{color}" stroke-width="{width}" '
            f'stroke-linecap="round" stroke-linejoin="round" {extra}>'
            f'{beat("stroke-dashoffset", [(0, 1), (a, 1), (b, 0), (.97, 0), (1, 1)])}</path>')


# ---------------------------------------------------------------- slide 1: the report that sends itself
@register("scene", "p01_portada")
def sc_p01_portada(sl, ctx):
    """The client leads, its logo on top. Below, a paper week (Lun-Vie). Loop: the report sheet waiting on Friday
    folds into the paper plane, which flies over the week drawing the magenta ribbon and lands on Monday, where a sealed
    envelope appears with its hour. Frozen frame: envelope sealed on Monday, plane resting on it, ribbon drawn."""
    if ORIENT() == "portrait":
        return _pp01_portada(sl, ctx)
    days, hour = sl["days"], sl["hour"]
    g = [land(px_logo_client(1190, 96, 320), .1, .6)]
    # the paper week
    x0, y0, cw, top, bot = 862, 400, 132, 400, 744
    cal = px_sheet(x0 - 12, y0 - 12, cw * 5 + 24, bot - y0 + 24, PX_PAPER, 31)
    cal += f'<path d="M{x0} {y0 + 58} H{x0 + cw * 5}" stroke="{PX_EDGE}" stroke-width="1.6"/>'
    cal += "".join(f'<path d="M{x0 + k * cw} {y0 + 8} V{bot - 8}" stroke="{PX_EDGE}" stroke-width="1.2"/>' for k in range(1, 5))
    cal += "".join(px_text(x0 + k * cw + cw / 2, y0 + 38, d, 19, "portada day", cw - 20, PX_INK, "middle")
                   for k, d in enumerate(days))
    cal += "".join(f'<circle cx="{x0 + 18 + k * 34}" cy="{top - 1}" r="5" fill="none" stroke="{PX_EDGE}" stroke-width="1.4"/>'
                   for k in range(0, 20, 1) if x0 + 18 + k * 34 < x0 + cw * 5 - 10)
    cal += "".join(px_lines(x0 + k * cw + 18, y0 + 92 + (k % 2) * 40, cw - 36, 3 + (k % 2), 22, width=5) for k in (1, 2, 3))
    g.append(land(cal, .35, .6))
    # the report waiting on Friday: it lands with the week, then folds into the plane (.14-.22)
    fx = x0 + 4 * cw + cw / 2
    sheet = px_sheet(fx - 46, 500, 92, 116, PX_PAPER_2, 33) + px_lines(fx - 32, 522, 64, 5, 17, width=5)
    fold = _p01_tr([(0, "1 1"), (.14, "1 1"), (.22, ".2 .6"), (.97, ".2 .6"), (1, "1 1")], "scale")
    g.append(land(f'<g>{beat("opacity", [(0, 1), (.19, 1), (.22, 0), (.97, 0), (1, 1)])}'
                  f'<g transform="translate({fx} 558)"><g>{fold}<g transform="translate({-fx} -558)">{sheet}</g></g></g></g>', .7, .5))
    # the flight: Friday -> over the week -> Monday, the ribbon drawn behind the plane
    mx = x0 + cw / 2
    path = f"M{fx} 556 C{fx - 40} 300 {mx + 170} 250 {mx + 6} 520"
    g.append(_p01_draw(path, .22, .56, PX_RIBBON, 3, 'opacity=".95"'))
    plane = f'<g transform="scale(-1 1)">{px_plane(0, 0, .62)}</g>'
    g.append(f'<g>{_p01_on(.19)}<g>{move(path, [(0, 0), (.22, 0), (.56, 1), (1, 1)], D)}{plane}</g></g>')
    # Monday: the envelope arrives (.58), then its seal and hour (.68)
    ex, ey, ew, eh = mx - 54, 586, 108, 70
    env = px_envelope(ex, ey, ew, eh, sealed=False)
    g.append(_p01_drop(env, .58, -30))
    seal = (f'<circle cx="{mx}" cy="{ey + eh * .52:.1f}" r="11" fill="{PX_RIBBON}"/>'
            f'<circle cx="{mx - 3}" cy="{ey + eh * .52 - 3:.1f}" r="3" fill="var(--white)" opacity=".55"/>')
    g.append(f'<g>{_p01_on(.68, 1, .015)}{seal}</g>')
    g.append(f'<g>{_p01_on(.7)}{px_text(mx, 700, hour, 20, "portada hour", cw - 24, PX_INK, "middle")}</g>')
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- slide 2: Friday, 3:30 pm
def _p02_note(x, y, w, h, label, fill=PX_POSTIT, fg=PX_INK, seed=3, rot=0, size=17):
    """A post-it with its wrapped label (the kit's px_postit: every line >= 15 px), rotated as one piece of paper."""
    return px_postit(x, y, w, h, fill, seed, rot, label, size, fg)


def _p02_clock(cx, cy, r):
    """A paper clock fixed at 3:30 (hour hand halfway between 3 and 4, minute hand on 6)."""
    ticks = "".join(f'<path d="M{cx} {cy - r + 8} V{cy - r + (18 if k % 3 == 0 else 13)}" stroke="{PX_INK}" '
                    f'stroke-width="{2 if k % 3 == 0 else 1.3}" transform="rotate({k * 30} {cx} {cy})"/>' for k in range(12))
    return (f'<circle cx="{cx + PX_SH[0]}" cy="{cy + PX_SH[1]}" r="{r}" fill="{PX_SHADOW}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{PX_PAPER}" stroke="{PX_EDGE}" stroke-width="1.4"/>' + ticks
            + f'<path d="M{cx} {cy} L{cx} {cy - r * .48:.1f}" stroke="{PX_INK}" stroke-width="3.2" stroke-linecap="round" transform="rotate(105 {cx} {cy})"/>'
            + f'<path d="M{cx} {cy} L{cx} {cy + r * .72:.1f}" stroke="{PX_INK}" stroke-width="2" stroke-linecap="round"/>'
            + f'<circle cx="{cx}" cy="{cy}" r="4" fill="{PX_RIBBON}"/>')


P02_CORK = "color-mix(in srgb, color-mix(in srgb, var(--c3) 62%, var(--ink)) 78%, var(--white))"
P02_FRAME = "color-mix(in srgb, var(--c3) 48%, var(--ink))"


def _p02_red(x, y, sl, ctx, rot=-3):
    """The red post-it of the Monday report (slides 2 and 3), with its pin; (x, y) is its top-left corner."""
    w, h = 196, 160
    note = _p02_note(x, y, w, h, sl["urgent"], PX_POSTIT_RED, ctx.brand.on("var(--c5)"), 41, rot, 21)
    return note, (x + w / 2, y + 16)


@register("scene", "p02_viernes")
def sc_p02_viernes(sl, ctx):
    """A cork board already busy, a paper clock at 3:30. Loop: yellow post-its keep dropping onto the board until it is
    full; then the red one, «Informe · lunes 8:00», glides in from the right and the pin nails it in the center.
    Frozen frame: board full, red post-it pinned."""
    if ORIENT() == "portrait":
        return _pp02_viernes(sl, ctx)
    bx, by, bw, bh = 856, 142, 596, 640
    board = (px_sheet(bx, by, bw, bh, P02_FRAME, 51)
             + f'<path d="{px_sheet_path(bx + 20, by + 20, bw - 40, bh - 40, 52, 1.6)}" fill="{P02_CORK}" stroke="none"/>'
             + "".join(f'<circle cx="{bx + 30 + (k * 97) % (bw - 60)}" cy="{by + 34 + (k * 61) % (bh - 70)}" r="1.6" '
                       f'fill="{P02_FRAME}" opacity=".35"/>' for k in range(60)))
    g = [land(board, .1, .55)]
    g.append(pop(_p02_clock(0, 0, 62), 1478, 196, .45, .45))
    notes = sl["postits"]
    cells = [(962, 262, -4), (1154, 250, 3), (1346, 272, -2), (948, 462, 2), (1362, 470, -3),
             (966, 668, -2), (1154, 664, 3), (1352, 672, 4)]
    w, h = 158, 138
    parts = [_p02_note(cx - w / 2, cy - h / 2, w, h, lab, seed=60 + k, rot=r) + px_pin(cx, cy - h / 2 + 14)
             for k, ((cx, cy, r), lab) in enumerate(zip(cells, notes))]
    g.append(seq(parts[:3], .55, .5, 18))
    for k, p in enumerate(parts[3:]):
        g.append(_p01_drop(p, .08 + k * .075, -60))
    # the red one: glides in from the right at .56, the pin drops at .66, a small shake
    red, (px, py) = _p02_red(1154 - 98, 466 - 80, sl, ctx)
    shake = _p01_tr([(0, "0"), (.66, "0"), (.675, "-2.5"), (.69, "1.5"), (.705, "0"), (1, "0")], "rotate")
    arrive = _p01_tr([(0, "420 -230"), (.56, "420 -230"), (.63, "0 0"), (.97, "0 0"), (1, "420 -230")])
    g.append(f'<g>{_p01_on(.56, 1, .02)}<g>{arrive}<g transform="translate({px} {py + 60})"><g>{shake}'
             f'<g transform="translate({-px} {-py - 60})">{red}</g></g></g></g></g>')
    g.append(_p01_drop(px_pin(px, py, "var(--c4)"), .66, -40))
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- slide 3: the route
@register("scene", "p03_estrategia")
def sc_p03_estrategia(sl, ctx):
    """The red post-it of slide 2, pinned at the left; a person stands calm beside it; a folded paper map. Loop: the map
    unfolds panel by panel, the magenta ribbon leaves the post-it and traces a route; at each stop a route icon appears
    (chat with cards, lens, envelope with gear), no words. Frozen frame: map open, route traced, three icons, post-it at
    the start."""
    if ORIENT() == "portrait":
        return _pp03_estrategia(sl, ctx)
    mx, my, pw, ph, n = 958, 186, 146, 540, 4
    panels = []
    for k in range(n):
        x = mx + k * pw
        fill = PX_PAPER if k % 2 == 0 else "color-mix(in srgb, var(--white) 84%, var(--c4))"
        art = px_sheet(x, my, pw, ph, fill, 70 + k, shadow=True)
        # faint roads, rivers and a grid: the map's own drawing, cut by the folds
        art += "".join(f'<path d="M{x} {my + 60 + j * 120} H{x + pw}" stroke="{PX_EDGE}" stroke-width="1" opacity=".6"/>' for j in range(5))
        art += f'<path d="M{x + pw * .5} {my + 10} V{my + ph - 10}" stroke="{PX_EDGE}" stroke-width="1" opacity=".5" stroke-dasharray="4 7"/>'
        art += f'<path d="M{x + (k % 2 == 0) * pw} {my + 8} V{my + ph - 8}" stroke="{PX_SHADOW}" stroke-width="1.2" opacity=".35"/>'
        if k == 0:
            panels.append(art)
            continue
        a = .06 + (k - 1) * .07
        unf = _p01_tr([(0, "0 1"), (a, "0 1"), (a + .06, "1 1"), (.97, "1 1"), (1, "0 1")], "scale")
        panels.append(f'<g>{_p01_on(a, 1, .01)}<g transform="translate({x} 0)"><g>{unf}<g transform="translate({-x} 0)">{art}</g></g></g></g>')
    river = (f'<path d="M{mx + 10} {my + 150} C{mx + 180} {my + 110} {mx + 260} {my + 260} {mx + 420} {my + 210} '
             f'S{mx + 560} {my + 120} {mx + pw * n - 10} {my + 160}" fill="none" stroke="var(--c2)" stroke-width="5" opacity=".55"/>')
    river = f'<g>{_p01_on(.27, 1, .03)}{river}</g>'
    folded = "".join(px_sheet(mx + 6 * j, my + 6 * j, pw, ph, PX_PAPER_2, 80 + j) for j in (2, 1))
    g = [land(f'<g>{beat("opacity", [(0, 1), (.06, 1), (.08, 0), (.97, 0), (1, 1)])}{folded}</g>' + panels[0], .3, .55)]
    g.append("".join(panels[1:]) + river)
    # the route: from the post-it through the three stops
    stops = [(1098, 612), (1262, 330), (1440, 560)]
    route = (f"M992 470 C1046 482 1030 {stops[0][1]} {stops[0][0]} {stops[0][1]} "
             f"C1186 612 1166 {stops[1][1]} {stops[1][0]} {stops[1][1]} "
             f"C1368 330 1330 {stops[2][1]} {stops[2][0]} {stops[2][1]}")
    g.append(_p01_draw(route, .32, .74, PX_RIBBON, 4.5))
    for k, ((x, y), a) in enumerate(zip(stops, (.42, .56, .72))):
        grow = _p01_tr([(0, ".4 .4"), (a, ".4 .4"), (a + .04, "1.08 1.08"), (a + .06, "1 1"), (1, "1 1")], "scale")
        g.append(f'<g>{_p01_on(a, 1, .02)}<g transform="translate({x} {y})"><g>{grow}<g transform="translate({-x} {-y})">'
                 f'{px_icon(k, x, y, 1.2)}</g></g></g></g>')
    # the red post-it pinned at the start, and a calm person beside it
    red, (px, py) = _p02_red(826, 386, sl, ctx, -4)
    g.append(land(red + px_pin(px, py, "var(--c4)"), .1, .55))
    walker = (f'<g>{bob(0, -2.5, 4.4)}<path d="M-30 18 Q-30 -14 0 -14 Q30 -14 30 18 Z" fill="{PX_PAPER_2}" stroke="{PX_EDGE}" stroke-width="1.2"/>'
              f'<circle cx="0" cy="-36" r="17" fill="{PX_PAPER_2}" stroke="{PX_EDGE}" stroke-width="1.2"/></g>')
    g.append(land(f'<ellipse cx="{888 + 5}" cy="{716}" rx="36" ry="6" fill="{PX_SHADOW}"/>'
                  f'<g transform="translate(888 690) scale(1.25)">{walker}</g>', .5, .5))
    return "".join(g), D, FREEZE


# ==================================================================================================== slides 04-06
_P04_TABS = ("var(--c1)", "var(--c3)", "var(--accent)")   # the three small cards of route icon 0


def _p04_on(a, f=.03):
    """Opacity 0 until fraction a of the loop, then 1 until the reset at .97."""
    return beat("opacity", [(0, 0), (a, 0), (a + f, 1), (.97, 1), (1, 0)])


def _p04_in(a, dx, dy, f=.05):
    """Travel from (dx, dy) to the final pose between fractions a and a+f, held until the reset."""
    return (f'<animateTransform attributeName="transform" type="translate" values="{dx} {dy};{dx} {dy};0 0;0 0;{dx} {dy}" '
            f'keyTimes="0;{a:.3f};{a + f:.3f};.97;1" dur="{D}s" repeatCount="indefinite"/>')


def _p04_draw(a, f=.06):
    """A stroke (pathLength=1, dasharray 1) that draws between a and a+f and stays until the reset."""
    return beat("stroke-dashoffset", [(0, 1), (a, 1), (a + f, 0), (.97, 0), (1, 1)])


def _p04_minimap(lit_now, lit_at, x=880, y=748):
    """The strategy map, small: three route icons on a short ribbon; lit_now already walked, lit_at lights at a fraction."""
    g = [f'<path d="M{x} {y} L{x + 170} {y}" stroke="{PX_RIBBON}" stroke-width="3" stroke-linecap="round"/>']
    for k in range(3):
        cx = x + k * 85
        g.append(px_icon(k, cx, y, .55, lit=k in lit_now))
        if k in lit_at:
            g.append(f'<g>{_p04_on(lit_at[k])}{px_icon(k, cx, y, .55, lit=True)}</g>')
    return "".join(g)


def _p04_hole(x, y, w, h, label=None):
    g = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="none" stroke="{PX_MUTED_INK}" '
         f'stroke-width="1.5" stroke-dasharray="6 5"/>')
    if label:
        g += px_text(x + w / 2, y + h / 2 + 6, label, 16, "template hole", w - 20, PX_MUTED_INK, "middle", False)
    return g


def _p04_bubble(x, y, w, h, text, seed, fill=PX_PAPER, size=18):
    """A paper chat bubble: a cut sheet and its tail, one line of ink text."""
    tail = f'<path d="M{x + 22} {y + h - 1} L{x + 18} {y + h + 16} L{x + 42} {y + h - 1} Z" fill="{fill}" stroke="{PX_EDGE}" stroke-width="1.2" stroke-linejoin="round"/>'
    return (px_sheet(x, y, w, h, fill, seed) + tail
            + f'<path d="M{x + 23} {y + h - 2} L{x + 41} {y + h - 2}" stroke="{fill}" stroke-width="3"/>'
            + px_text(x + 18, y + h / 2 + 6, text, size, "chat bubble", w - 36))


@register("scene", "p04_explicar")
def sc_p04_explicar(sl, ctx):
    """Left, small: the one-line ask and the hollow template it gets back. Right: the chat sheet whose three holes are
    filled, one by one, by the three context cards; then it reads as a written procedure and map stop 0 lights."""
    if ORIENT() == "portrait":
        return _pp04_explicar(sl, ctx)
    ask, ins, cards, done = sl["ask"], sl["insert"], sl["cards"], sl["done"]
    left = (_p04_bubble(850, 150, 220, 56, ask, 31)
            + px_sheet(850, 250, 220, 300, PX_PAPER, 32)
            + px_lines(870, 272, 170, 2, 16)
            + "".join(_p04_hole(870, 320 + k * 72, 180, 54, ins) for k in range(3)))
    sheet = (px_sheet(1125, 120, 425, 650, PX_PAPER, 33)
             + _p04_bubble(1290, 140, 235, 52, ask, 34, PX_PAPER_2, 17)
             + "".join(_p04_hole(1150, 225 + k * 138, 375, 118) for k in range(3)))
    thread = px_ribbon("M1074 420 C1102 420 1094 300 1122 300", 3, .7, .5)
    g = [land(left, .1, .5), land(sheet, .3, .55), thread, land(_p04_minimap((), {}), .9, .5, 10)]
    # the story: three cards, one by one, into the holes
    for k, lab in enumerate(cards):
        a = .20 + k * .16
        x, y = 1150, 225 + k * 138
        c = (px_sheet(x, y, 375, 118, PX_PAPER_2, 40 + k)
             + f'<rect x="{x + 16}" y="{y + 18}" width="12" height="82" rx="3" fill="{_P04_TABS[k]}"/>'
             + px_text(x + 44, y + 44, lab, 21, "context card", 310)
             + px_lines(x + 44, y + 64, 290, 2, 18))
        g.append(f'<g>{_p04_on(a)}<g>{_p04_in(a, -70, -34)}{c}</g></g>')
    # the sheet reads as a procedure: a check and its name, then the first stop of the map lights
    fin = (f'<path d="M1160 712 L1170 724 L1190 700" fill="none" stroke="{PX_RIBBON}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
           + px_text(1204, 720, done, 21, "procedure done", 320))
    g.append(f'<g>{_p04_on(.70)}{fin}</g>')
    g.append(_p04_minimap((), {0: .76}))
    return "".join(g), D, FREEZE


@register("scene", "p05_revisar")
def sc_p05_revisar(sl, ctx):
    """The lens walks the draft and stops on the number with no source; a magenta strike crosses it out, the ribbon
    carries it to the procedure, which gains a new line; map stop 1 lights. The figure frame never moves."""
    if ORIENT() == "portrait":
        return _pp05_revisar(sl, ctx)
    draft, inv, nosrc, proc, steps, new = sl["draft"], sl["invented"], sl["nosource"], sl["proc"], sl["steps"], sl["step"]
    hi = "color-mix(in srgb, var(--c4) 55%, var(--white))"
    doc = (px_sheet(850, 130, 390, 500, PX_PAPER, 41)
           + px_text(878, 174, draft, 21, "draft title", 330)
           + px_lines(878, 204, 330, 3, 26)
           + f'<rect x="878" y="325" width="92" height="6" rx="3" fill="{PX_MUTED_INK}" opacity=".45"/>'
           + f'<rect x="982" y="310" width="100" height="38" rx="5" fill="{hi}"/>'
           + px_text(1032, 338, inv, 24, "invented number", 90, anchor="middle")
           + f'<rect x="1094" y="325" width="110" height="6" rx="3" fill="{PX_MUTED_INK}" opacity=".45"/>'
           + px_lines(878, 378, 330, 6, 26))
    card_ = (px_sheet(1270, 130, 280, 330, PX_PAPER_2, 42)
             + px_text(1292, 172, proc, 21, "procedure title", 236)
             + "".join(f'<rect x="1292" y="{196 + k * 44}" width="10" height="24" rx="2" fill="{_P04_TABS[k]}"/>'
                       + px_text(1312, 214 + k * 44, s, 17, "procedure step", 226) for k, s in enumerate(steps)))
    fig = (px_sheet(1270, 500, 280, 240, PX_PAPER, 43) + px_pin(1410, 512)
           + px_text(1410, 600, sl["figure"], 58, "figure", 240, anchor="middle")
           + TCW(1410, 640, sl["label"], 28, 17, PX_INK, W6, 1.25))
    g = [land(doc, .1, .5), land(card_, .3, .5), land(fig, .5, .5, 0), land(_p04_minimap((0,), {}), .9, .5, 10)]
    # the lens: from the top of the draft, across the lines, to the number, and it stays there
    lens_ = (f'<g><animateTransform attributeName="transform" type="translate" '
             f'values="905 214;905 214;1175 246;925 292;1032 330;1032 330;955 418;955 418;905 214" keyTimes="0;.18;.28;.37;.45;.55;.60;.97;1" '
             f'dur="{D}s" repeatCount="indefinite"/>{px_lens(0, 0, 32)}</g>')
    g.append(land(lens_, .8, .45, 0))
    strike = (f'<path d="M976 333 L1088 325" pathLength="1" stroke-dasharray="1" stroke="{PX_RIBBON}" stroke-width="4" '
              f'stroke-linecap="round" fill="none">{_p04_draw(.48)}</path>')
    g.append(strike + f'<g>{_p04_on(.50)}{pill(1150, 287, nosrc, "var(--c5)", ctx, 16, 150, "no source tag")}</g>')
    thread = (f'<path d="M1090 352 C1180 372 1200 350 1286 346" pathLength="1" stroke-dasharray="1" stroke="{PX_RIBBON}" '
              f'stroke-width="3" stroke-linecap="round" fill="none">{_p04_draw(.56)}</path>')
    line = (f'<rect x="1284" y="322" width="252" height="48" rx="8" fill="none" stroke="{PX_RIBBON}" stroke-width="2"/>'
            + f'<path d="M1296 346 L1304 355 L1318 337" fill="none" stroke="{PX_RIBBON}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
            + px_text(1328, 353, new, 17, "new procedure step", 200))
    g.append(thread + f'<g>{_p04_on(.62)}<g>{_p04_in(.62, 0, 14)}{line}</g></g>')
    g.append(_p04_minimap((0,), {1: .72}))
    return "".join(g), D, FREEZE


def _p06_fold(sign, a, f=.06):
    """The accordion fold of a panel: skewed while closed, flat from fraction a on, until the reset."""
    c = 11 * sign
    return (f'<animateTransform attributeName="transform" type="skewY" values="{c};{c};0;0;{c}" '
            f'keyTimes="0;{a:.3f};{a + f:.3f};.97;1" dur="{D}s" repeatCount="indefinite"/>')


def _p06_lock(x, y):
    """A small padlock in ink with a magenta body, drawn around (x, y)."""
    return (f'<path d="M{x - 10} {y - 2} V{y - 12} A10 10 0 0 1 {x + 10} {y - 12} V{y - 2}" fill="none" stroke="{PX_INK}" stroke-width="3" stroke-linecap="round"/>'
            f'<rect x="{x - 16}" y="{y - 3}" width="32" height="26" rx="4" fill="{PX_RIBBON}" stroke="{PX_INK}" stroke-width="1.5"/>'
            f'<circle cx="{x}" cy="{y + 8}" r="3.4" fill="var(--white)"/>')


@register("scene", "p06_ruta")
def sc_p06_ruta(sl, ctx):
    """Three accordion paper panels with the drawings of the three stops open one after another and none closes; each
    gets its word, a padlock settles on the second (a person reviews) and the ribbon threads the three."""
    if ORIENT() == "portrait":
        return _pp06_ruta(sl, ctx)
    words = sl["words"]
    g, W_, H_ = [], 215, 450
    panels = []
    for k in range(3):
        x, a = 850 + k * 240, .20 + k * .2
        shade_ = f'<rect x="0" y="0" width="{W_}" height="{H_}" fill="var(--ink)" opacity=".16">{beat("opacity", [(0, .16), (a, .16), (a + .06, 0), (.97, 0), (1, .16)])}</rect>'
        word = f'<g>{_p04_on(a + .05)}{px_text(W_ / 2, 330, words[k], 30, "route word", W_ - 30, anchor="middle")}' \
               f'<path d="M{W_ / 2 - 40} 350 L{W_ / 2 + 40} 350" stroke="{PX_RIBBON}" stroke-width="2" stroke-linecap="round"/></g>'
        body = (px_sheet(0, 0, W_, H_, PX_PAPER, 50 + k) + px_icon(k, W_ / 2, 150, 1.7) + word + shade_)
        panels.append(f'<g transform="translate({x} 170)"><g>{_p06_fold(-1 if k % 2 else 1, a)}{body}</g></g>')
    g.append(seq(panels, .1, .55, 20))
    g.append(px_ribbon("M836 590 C920 560 1000 620 1090 590 S1250 560 1330 590 S1480 620 1556 580", 3, .8, 1.0))
    lock = f'<g>{_p04_on(.50)}<g>{_p04_in(.50, 0, -60, .07)}{_p06_lock(1090 + W_ / 2, 432)}</g></g>'
    g.append(lock)
    return "".join(g), D, FREEZE


# ==================================================================================================== slides 07-09
def _p07_on(a, f=.02):
    """Opacity 0 until fraction a of the loop, then 1 until the reset at .97."""
    return beat("opacity", [(0, 0), (a, 0), (a + f, 1), (.97, 1), (1, 0)])


def _p07_tr(pairs):
    """A translate loop with explicit times: pairs = [(fraction, "dx dy")] from 0 to 1."""
    kt = ";".join(f"{t:.3f}" for t, _ in pairs)
    return (f'<animateTransform attributeName="transform" type="translate" values="{";".join(v for _, v in pairs)}" '
            f'keyTimes="{kt}" dur="{D}s" repeatCount="indefinite"/>')


_P07_SW = f'fill="none" stroke="{PX_INK}" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"'


def _p07_glyph(k):
    """Tiny drawing of step k around (0, 0): 0 saved prompt card, 1 chat bubble with a spark, 2 two boxes and an arrow,
    3 a small dashboard."""
    sw = _P07_SW
    if k == 0:
        return (f'<rect x="-30" y="-22" width="60" height="44" rx="5" {sw}/>'
                f'<path d="M-20 -8 H12 M-20 2 H18 M-20 12 H4" {sw} opacity=".7"/>'
                f'<path d="M16 -22 V-6 L21 -10 L26 -6 V-22" fill="{PX_RIBBON}" stroke="none"/>')
    if k == 1:
        return (f'<path d="M-30 -20 H26 Q30 -20 30 -16 V8 Q30 12 26 12 H-6 L-16 22 V12 H-26 Q-30 12 -30 8 V-16 Q-30 -20 -26 -20 Z" {sw}/>'
                + spark(0, -4, .55, PX_RIBBON))
    if k == 2:
        return (f'<rect x="-40" y="-14" width="26" height="26" rx="4" {sw}/><rect x="14" y="-14" width="26" height="26" rx="4" {sw}/>'
                f'<path d="M-10 -1 H8 M2 -7 L9 -1 L2 5" {sw} stroke="{PX_RIBBON}"/>')
    return (f'<rect x="-36" y="-26" width="72" height="52" rx="5" {sw}/><path d="M-36 -14 H36" {sw} opacity=".7"/>'
            + "".join(f'<rect x="{-28 + j * 11}" y="{18 - hh}" width="7" height="{hh}" rx="1" fill="{PX_INK}" opacity=".75"/>'
                      for j, hh in enumerate((10, 18, 14)))
            + f'<path d="M6 12 L14 2 L21 7 L30 -6" fill="none" stroke="{PX_RIBBON}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')


# ---------------------------------------------------------------- slide 7: the staircase of automation
@register("scene", "p07_automatizar")
def sc_p07_automatizar(sl, ctx):
    """Four paper steps rising left to right, from least to most effort. A spark climbs them and each step lights with a
    magenta edge and stays lit; the third stop of the strategy map lights; the note «casi siempre, una mezcla» is pinned.
    Frozen frame: four steps lit and the note."""
    if ORIENT() == "portrait":
        return _pp07_automatizar(sl, ctx)
    steps = sl.get("steps", ["Prompt guardado", "Asistente", "Flujo entre sistemas", "Software propio"])
    note = sl.get("note", "Casi siempre, una mezcla")
    w, bottom = 172, 800
    xs = [832 + k * 180 for k in range(4)]
    tops = [650 - k * 112 for k in range(4)]
    lit_at = [.14, .30, .46, .62]
    g = []
    # the staircase lands step by step
    parts = []
    for k in range(4):
        x, top, cx = xs[k], tops[k], xs[k] + w / 2
        z = fit(max(steps[k].split(), key=len), 18, w - 30, "automatizar step")
        body = px_sheet(x, top, w, bottom - top, PX_PAPER, 41 + k)
        body += TCW(f"{cx:.1f}", f"{top + 32}", steps[k], 12, z, PX_INK, W6, 1.15)
        body += f'<g transform="translate({cx:.1f} {top + 104}) scale(1.1)">{_p07_glyph(k)}</g>'
        edge = (f'<path d="{px_sheet_path(x, top, w, bottom - top, 41 + k)}" fill="none" stroke="{PX_RIBBON}" stroke-width="3" '
                f'stroke-linejoin="round"/>')
        body += f'<g>{_p07_on(lit_at[k])}{edge}</g>'
        parts.append(body)
    g.append(seq(parts, .1, .5, 22))
    # the spark climbs from step to step
    path = "M916 628 Q1006 516 1096 516 Q1186 404 1276 404 Q1366 292 1456 292"
    shown = beat("opacity", [(0, 0), (.10, 0), (.12, 1), (.96, 1), (.97, 0), (1, 0)])
    stops = [(0, 0), (.22, 0), (.30, 1 / 3), (.38, 1 / 3), (.46, 2 / 3), (.54, 2 / 3), (.62, 1), (1, 1)]
    g.append(f'<g>{shown}{move(path, stops, D)}{glow(0, 0, 34, "var(--c4)", .7)}{spark(0, 0, 1.1, "var(--c4)")}</g>')
    # the strategy map in the corner: explicar and revisar walked, automatizar lights now
    mx, my = [1380, 1450, 1520], 146
    mini = f'<path d="M{mx[0]} {my} H{mx[2]}" stroke="{PX_RIBBON}" stroke-width="3" stroke-linecap="round"/>'
    mini += px_icon(0, mx[0], my, .55, True) + px_icon(1, mx[1], my, .55, True) + px_icon(2, mx[2], my, .55, False)
    mini += f'<g>{_p07_on(.70)}{px_icon(2, mx[2], my, .55, True)}</g>'
    g.append(land(mini, .6, .5, 0))
    # the note pins at the top once the four steps are lit
    z = fit(max(note.split(), key=len), 22, 180, "automatizar note")
    postit = (f'<g transform="rotate(-4 977 230)">' + px_sheet(870, 168, 214, 124, PX_POSTIT, 7)
              + TCW("977", "224", note, 14, z, PX_INK, W6, 1.2) + '</g>' + px_pin(977, 180))
    g.append(f'<g>{_p07_on(.76)}<g>{_p07_tr([(0, "0 -24"), (.76, "0 -24"), (.80, "0 0"), (1, "0 0")])}{postit}</g></g>')
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- slide 8: every Monday at 8:00
def _p08_clock(x, y, r=17):
    """A clock at eight: minute hand up, hour hand toward the 8."""
    sw = 'stroke="var(--white)" stroke-width="1.8" stroke-linecap="round"'
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" {sw}/>'
            f'<path d="M{x} {y} V{y - r * .7:.1f} M{x} {y} L{x - r * .45:.1f} {y + r * .26:.1f}" {sw}/>')


@register("scene", "p08_lunes")
def sc_p08_lunes(sl, ctx):
    """A paper calendar with four Mondays and the sealed envelope of slide 1. At 8:00 the envelope flies to the status
    board, the Monday gets a magenta check and one bar lands on the board; then the next Monday, four times. The envelope
    is back and sealed each time: it will keep going out. Frozen frame: four Mondays checked, the board complete."""
    if ORIENT() == "portrait":
        return _pp08_lunes(sl, ctx)
    mondays = sl.get("mondays", ["Lun 1", "Lun 2", "Lun 3", "Lun 4"])
    hour = sl.get("hour", "8:00")
    cal_t = sl.get("calendar", "Lunes")
    board_t = sl.get("board", "Estado del proyecto")
    fly = [.20, .37, .54, .71]
    g = []
    # the calendar: rings, title, four Monday cells
    cx0, cy0, cw, chh = 836, 150, 380, 480
    cal = px_sheet(cx0, cy0, cw, chh, PX_PAPER, 31)
    cal += "".join(f'<rect x="{x - 5}" y="{cy0 - 14}" width="10" height="26" rx="5" fill="none" stroke="{PX_INK}" stroke-width="1.8"/>'
                   for x in (cx0 + 70, cx0 + cw - 70))
    cal += px_text(cx0 + cw / 2, cy0 + 48, cal_t, 22, "lunes calendar title", cw - 60, PX_INK, "middle")
    cal += f'<path d="M{cx0 + 24} {cy0 + 66} H{cx0 + cw - 24}" stroke="{PX_RIBBON}" stroke-width="2"/>'
    cells = []
    for k in range(4):
        x, y = cx0 + 22 + (k % 2) * 176, cy0 + 86 + (k // 2) * 188
        c = f'<rect x="{x}" y="{y}" width="160" height="172" rx="6" fill="none" stroke="{PX_MUTED_INK}" stroke-width="1.4" opacity=".6"/>'
        c += px_text(x + 16, y + 32, mondays[k], 19, "lunes cell", 128)
        c += px_text(x + 16, y + 56, hour, 16, "lunes cell hour", 128, PX_MUTED_INK, bold=False)
        c += f'<g>{_p07_on(fly[k] + .07)}<path d="M{x + 58} {y + 110} L{x + 78} {y + 132} L{x + 116} {y + 86}" fill="none" stroke="{PX_RIBBON}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></g>'
        cells.append(c)
    g.append(land(cal, .1, .5))
    g.append(seq(cells, .3, .45, 14, 1.3))
    # the status board, pinned; its four tracks are empty until the reports arrive
    bx, by, bw, bh = 1262, 196, 280, 430
    board = px_sheet(bx, by, bw, bh, PX_PAPER, 33) + px_pin(bx + bw / 2, by + 16)
    board += px_text(bx + bw / 2, by + 64, board_t, 21, "lunes board title", bw - 40, PX_INK, "middle")
    fills = [.92, .74, .58, .40]
    for j in range(4):
        y = by + 110 + j * 76
        board += px_lines(bx + 28, y, 120, 1, 0, None, ".45", 7)
        board += f'<rect x="{bx + 28}" y="{y + 20}" width="{bw - 56}" height="16" rx="8" fill="none" stroke="{PX_MUTED_INK}" stroke-width="1.2" opacity=".7"/>'
        bar = f'<rect x="{bx + 28}" y="{y + 20}" width="{(bw - 56) * fills[j]:.0f}" height="16" rx="8" fill="{PX_RIBBON}"/>'
        board += f'<g>{_p07_on(fly[j] + .08)}{bar}</g>'
    g.append(land(board, .5, .5))
    # 8:00 on the stage, next to the envelope
    g.append(land(_p08_clock(1050, 706) + T(1080, 714, hour, fit(hour, 24, 110, "lunes hour"), "var(--white)", W6), .8, .45, 0))
    # the sealed envelope: flies to the board at 8:00, comes back sealed for the next Monday
    ex, ey, ew, eh = 866, 666, 136, 88
    dx, dy = bx + bw / 2 - (ex + ew / 2), by + 250 - (ey + eh / 2)
    tr, op = [(0, "0 0")], [(0, 1)]
    for a in fly:
        tr += [(a, "0 0"), (a + .07, f"{dx:.0f} {dy:.0f}"), (a + .075, "0 0")]
        op += [(a + .05, 1), (a + .07, 0), (a + .08, 0), (a + .10, 1)]
    tr.append((1, "0 0"))
    op.append((1, 1))
    env = f'<g>{beat("opacity", op)}<g>{_p07_tr(tr)}{px_envelope(ex, ey, ew, eh, True)}</g></g>'
    g.append(land(env, 1.0, .5))
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- slide 9: the sheet that unfolds
def _p09_glyph(k):
    """Tiny drawing of repeated job k around (0, 0): 0 acta (sheet with a checklist), 1 correo (envelope),
    2 solicitud (form with a stamp), 3 reporte (small bar chart)."""
    sw = _P07_SW
    if k == 0:
        rows = "".join(f'<rect x="-20" y="{-22 + j * 17}" width="10" height="10" rx="2" {sw}/><path d="M-4 {-17 + j * 17} H22" {sw} opacity=".7"/>'
                       for j in range(3))
        ticks = "".join(f'<path d="M-18 {-17 + j * 17} L-15 {-14 + j * 17} L-10 {-21 + j * 17}" fill="none" stroke="{PX_RIBBON}" stroke-width="2" stroke-linecap="round"/>'
                        for j in range(2))
        return f'<rect x="-32" y="-38" width="64" height="76" rx="4" {sw}/>' + rows + ticks
    if k == 1:
        return (f'<rect x="-38" y="-24" width="76" height="50" rx="4" {sw}/><path d="M-38 -24 L0 6 L38 -24" {sw}/>'
                f'<circle cx="0" cy="6" r="6" fill="{PX_RIBBON}"/>')
    if k == 2:
        return (f'<rect x="-32" y="-38" width="64" height="76" rx="4" {sw}/>'
                f'<path d="M-22 -24 H22 M-22 -8 H22" {sw} opacity=".7"/><rect x="-22" y="4" width="44" height="12" rx="3" {sw} opacity=".7"/>'
                f'<circle cx="16" cy="26" r="9" fill="none" stroke="{PX_RIBBON}" stroke-width="2"/>'
                f'<path d="M11 26 L15 30 L21 22" fill="none" stroke="{PX_RIBBON}" stroke-width="2" stroke-linecap="round"/>')
    return (f'<rect x="-34" y="-34" width="68" height="68" rx="4" {sw}/><path d="M-24 22 H24" {sw}/>'
            + "".join(f'<rect x="{-20 + j * 14}" y="{20 - hh}" width="9" height="{hh}" rx="1.5" fill="{PX_INK}" opacity=".75"/>' for j, hh in enumerate((14, 24, 18)))
            + f'<path d="M-18 -10 L-4 -18 L8 -12 L22 -24" fill="none" stroke="{PX_RIBBON}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')


@register("scene", "p09_describir")
def sc_p09_describir(sl, ctx):
    """The report sheet lands folded. Its cover lifts and the sheet unfolds like a map into four panels, each another job
    that repeats (acta, correo, solicitud, reporte), and the magenta ribbon joins them one by one. Before the reset it
    folds back under the cover. Frozen frame: the sheet open, four panels joined by the ribbon."""
    if ORIENT() == "portrait":
        return _pp09_describir(sl, ctx)
    cover_t = sl.get("cover", "El informe")
    panels = sl.get("panels", ["Acta", "Correo", "Solicitud", "Reporte"])
    pw, x0, y0, ph = 172, 846, 226, 420
    xs = [x0 + k * pw for k in range(4)]
    out_at = [0, .30, .44, .58]
    shade2 = f"color-mix(in srgb, {PX_PAPER} 92%, var(--ink))"
    g = []
    stack = []
    for k in (3, 2, 1, 0):  # the last panel lies at the bottom of the fold
        x, cx = xs[k], xs[k] + pw / 2
        p = px_sheet(x, y0, pw, ph, PX_PAPER if k % 2 == 0 else shade2, 51 + k)
        p += f'<g transform="translate({cx:.1f} {y0 + 190})">{_p09_glyph(k)}</g>'
        p += px_text(cx, y0 + 352, panels[k], 21, "describir panel", pw - 30, PX_INK, "middle")
        p += f'<circle cx="{cx:.1f}" cy="{y0 + 292}" r="6" fill="{PX_RIBBON}"/>'
        if k:
            off = f"{-(k * pw) + 5 * k} 0"  # folded under panel 0, a few millimetres showing
            a = out_at[k]
            p = f'<g>{_p07_tr([(0, off), (a, off), (a + .08, "0 0"), (.92, "0 0"), (.985, off), (1, off)])}{p}</g>'
        stack.append(p)
    g.append(land("".join(stack), .1, .55))
    # the ribbon joins the panels as they open (dash beat, markup holds the full stroke)
    ry = y0 + 292
    for k in (1, 2, 3):
        a0, a1 = xs[k - 1] + pw / 2, xs[k] + pw / 2
        d = f"M{a0 + 8:.0f} {ry} C{a0 + 60:.0f} {ry - 26} {a1 - 60:.0f} {ry + 26} {a1 - 8:.0f} {ry}"
        a = out_at[k] + .09
        dash = beat("stroke-dashoffset", [(0, 1), (a, 1), (a + .06, 0), (.90, 0), (.92, 1), (1, 1)])
        g.append(f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{PX_RIBBON}" stroke-width="3" '
                 f'stroke-linecap="round">{dash}</path>')
    # the cover: the Monday report, folded on top; it lifts away and comes back when the sheet folds again
    cx = xs[0] + pw / 2
    cover = px_sheet(xs[0], y0, pw, ph, PX_PAPER, 50)
    cover += px_text(cx, y0 + 58, cover_t, 21, "describir cover", pw - 30, PX_INK, "middle")
    cover += px_lines(xs[0] + 24, y0 + 96, pw - 48, 6, 30, None, ".45", 7)
    cover += f'<path d="M{xs[0] + 24} {y0 + 300} H{xs[0] + pw - 24}" stroke="{PX_RIBBON}" stroke-width="3" stroke-linecap="round"/>'
    lift = beat("opacity", [(0, 1), (.20, 1), (.25, 0), (.975, 0), (1, 1)])
    move_up = _p07_tr([(0, "0 0"), (.20, "0 0"), (.25, "-30 -40"), (.975, "-30 -40"), (1, "0 0")])
    g.append(land(f'<g>{lift}<g>{move_up}{cover}</g></g>', .3, .5))
    return "".join(g), D, FREEZE


# ==================================================================================================== slides 10-12
def _p10_tr(typ, pairs):
    """A looping transform with explicit times: pairs = [(fraction of the loop, "value")]. Put it on a bare <g>."""
    kt = ";".join(f"{t:.3f}" for t, _v in pairs)
    vals = ";".join(v for _t, v in pairs)
    return (f'<animateTransform attributeName="transform" type="{typ}" values="{vals}" keyTimes="{kt}" dur="{D}s" '
            f'repeatCount="indefinite" additive="sum"/>')


def _p10_coin(r=26):
    """A paper coin around 0,0 (no currency sign: prices never go on a deck)."""
    return (f'<circle r="{r}" fill="color-mix(in srgb, var(--c4) 55%, var(--white))" stroke="{PX_INK}" stroke-width="1.6"/>'
            f'<circle r="{r * .68:.1f}" fill="none" stroke="{PX_INK}" stroke-width="1.2" opacity=".6"/>'
            f'<path d="M{-r * .3:.1f} {-r * .2:.1f} L0 {-r * .42:.1f} L{r * .3:.1f} {-r * .2:.1f}" fill="none" stroke="{PX_INK}" '
            f'stroke-width="1.4" stroke-linecap="round" opacity=".6"/>')


@register("scene", "p10_costo")
def sc_p10_costo(sl, ctx):
    """The figure and the bars never move; a coin shrinks on its way to the sliver, the ribbon underlines the gap."""
    if ORIENT() == "portrait":
        return _pp10_costo(sl, ctx)
    a = sl["args"] if "args" in sl else sl
    fig, label, years = a["figure"], a["label"], a["years"]
    g = []
    # the fixed figure in its paper frame
    frame = (px_sheet(880, 110, 640, 190, PX_PAPER_2, 41)
             + TC(1200, 212, fig, fit(fig, 80, 580, "cost figure"), PX_INK, W6)
             + TC(1200, 262, label, fit(label, 21, 580, "cost figure label"), PX_MUTED_INK, W6))
    pulse = (f'<rect x="894" y="124" width="612" height="162" rx="6" fill="none" stroke="{PX_RIBBON}" stroke-width="1.5">'
             f'{loop("stroke-opacity", ".1;.55;.1", 4)}</rect>')
    g.append(land(frame + pulse, .1, .5))
    # the chart: baseline, the tall 2022 bar, the 2024 sliver (illustrative 1/280), the years
    base, bx0, bx1, bw, top = 730, 980, 1290, 150, 380
    h1 = base - top
    h2 = max(h1 / 280, 2.5)
    bar_fill = "color-mix(in srgb, var(--c2) 45%, var(--white))"
    chart = (px_sheet(880, 330, 640, 480, PX_PAPER, 42)
             + f'<path d="M920 {base} H1480" stroke="{PX_EDGE}" stroke-width="1.6"/>')
    bar1 = px_sheet(bx0, top, bw, h1, bar_fill, 43, shadow=False) + f'<path d="{px_sheet_path(bx0, top, bw, h1, 43)}" fill="none" stroke="{PX_INK}" stroke-width="1.2" opacity=".5"/>'
    bar2 = f'<rect x="{bx1}" y="{base - h2:.1f}" width="{bw}" height="{h2:.1f}" fill="{bar_fill}" stroke="{PX_INK}" stroke-width="1.4"/>'
    yl = "".join(px_text(x + bw / 2, base + 44, y, 22, "chart year", 140, PX_INK, "middle") for x, y in zip((bx0, bx1), years))
    g.append(land(chart, .25, .5) + land(bar1, .45, .5, 0) + land(bar2 + yl, .6, .5, 0))
    # the ribbon underlines the gap: from the top of the tall bar down to the sliver
    gap = f"M{bx0 + bw + 6} {top + 4} C{bx0 + bw + 110} {top + 12} {bx1 - 40} {base - 150} {bx1 - 6} {base - 8}"
    g.append(f'<g>{loop("opacity", ".75;1;.75", 5)}{px_ribbon(gap, 3, .9, .8)}</g>')
    # soft pulse at the sliver when the coin arrives (invisible in the frozen frame)
    sx, sy = bx1 + bw / 2, base - 6
    g.append(_n04_ping(sx, sy, 10, 70, PX_RIBBON, (.42, .62), .12, .7))
    # the coin: over the tall bar, it flies and shrinks to hover over the sliver, then bobs there
    p0, p1, fly = (bx0 + bw / 2, top - 22), (sx, base - 44), (.17, .40)
    tr = _p10_tr("translate", [(0, f"{p0[0]} {p0[1]}"), (fly[0], f"{p0[0]} {p0[1]}"), (fly[0] + (fly[1] - fly[0]) * .5, f"{(p0[0] + p1[0]) / 2} {p0[1] - 30}"),
                               (fly[1], f"{p1[0]} {p1[1]}"), (.98, f"{p1[0]} {p1[1]}"), (1, f"{p0[0]} {p0[1]}")])
    sc = _p10_tr("scale", [(0, "1"), (fly[0], "1"), (fly[1], ".4"), (.98, ".4"), (1, "1")])
    coin = f'<g>{tr}<g>{sc}<g>{bob(0, -6, 3)}{_p10_coin()}</g></g></g>'
    g.append(land(coin, 1.2, .45, 0))
    return "".join(g), D, FREEZE


def _p11_doc(x, y):
    """A small document with a pen, around (x, y)."""
    return (f'<rect x="{x - 22}" y="{y - 28}" width="44" height="56" rx="3" fill="var(--white)" stroke="{PX_INK}" stroke-width="1.6"/>'
            + "".join(f'<path d="M{x - 13} {y - 14 + k * 10} H{x + (13 if k % 2 == 0 else 4)}" stroke="{PX_MUTED_INK}" stroke-width="2" stroke-linecap="round"/>' for k in range(4))
            + f'<path d="M{x + 14} {y + 26} L{x + 36} {y - 4}" stroke="{PX_RIBBON}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M{x + 14} {y + 26} L{x + 12} {y + 32}" stroke="{PX_INK}" stroke-width="2" stroke-linecap="round"/>')


def _p11_research(x, y):
    """A small chart under a lens, around (x, y)."""
    return (f'<path d="M{x - 30} {y + 26} H{x + 20}" stroke="{PX_INK}" stroke-width="1.6"/>'
            + "".join(f'<rect x="{x - 26 + k * 13}" y="{y + 26 - hh}" width="9" height="{hh}" fill="color-mix(in srgb, var(--c2) 45%, var(--white))" stroke="{PX_INK}" stroke-width="1.2"/>'
                      for k, hh in enumerate((14, 24, 34, 20)))
            + px_lens(x + 10, y - 10, 16))


def _p11_wrap(text, size, room):
    """Greedy word wrap by the bold width model, so each line gets its own strike (TCW hides where it breaks)."""
    text = _(str(text))
    if bold_width(text, size, current_factor()) > room and ", " in text:   # a post breaks after its comma
        head, tail = text.split(", ", 1)
        return [head + ","] + _p11_wrap(tail, size, room)
    lines = [""]
    for w in text.split():
        cand = (lines[-1] + " " + w).strip()
        if lines[-1] and bold_width(cand, size, current_factor()) > room:
            lines.append(w)
        else:
            lines[-1] = cand
    return lines


@register("scene", "p11_ruido")
def sc_p11_ruido(sl, ctx):
    """Noise on the left (a feed of exaggerated posts), evidence on the right (two notes with their fixed figures).
    The ribbon strikes the posts one by one, then each note gets its pin."""
    if ORIENT() == "portrait":
        return _pp11_ruido(sl, ctx)
    a = sl["args"] if "args" in sl else sl
    g = []
    # the feed
    feed = (px_sheet(840, 120, 340, 680, PX_PAPER_2, 51)
            + px_text(866, 164, a["feed"], 18, "feed header", 290, PX_MUTED_INK))
    g.append(land(feed, .1, .5))
    strikes = (.12, .22, .32)
    for k, (post, t) in enumerate(zip(a["posts"], strikes)):
        y0 = 190 + k * 200
        lines = _p11_wrap(post, 22, 260)
        card_ = (px_sheet(862, y0, 296, 180, PX_PAPER, 52 + k, shadow=False)
                 + f'<circle cx="892" cy="{y0 + 32}" r="13" fill="color-mix(in srgb, var(--c2) 45%, var(--white))" stroke="{PX_INK}" stroke-width="1.2"/>'
                 + px_lines(916, y0 + 24, 130, 2, 13, None, ".4", 5)
                 + "".join(T(880, y0 + 84 + i * 30, line, 22, PX_INK, W6) for i, line in enumerate(lines))
                 + px_lines(880, y0 + 156, 90, 1, 0, None, ".3", 5))
        g.append(land(card_, .3 + k * .15, .45))
        for i, line in enumerate(lines):   # one ribbon stroke through the middle of each line, as wide as the line
            ym, x1 = y0 + 76 + i * 30, 880 + min(260, bold_width(_(line), 22, current_factor())) + 10
            d = f"M872 {ym + 3} C{872 + (x1 - 872) * .3:.0f} {ym - 5} {872 + (x1 - 872) * .6:.0f} {ym + 7} {x1:.0f} {ym - 2}"
            ti = t + i * .03
            g.append(f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{PX_RIBBON}" stroke-width="5" stroke-linecap="round">'
                     f'{beat("stroke-dashoffset", [(0, 1), (ti, 1), (ti + .03, 0), (.98, 0), (1, 1)])}</path>')
    # the two notes, figures fixed from the start; each one gets its pin
    pins = (.44, .56)
    for k, (note, t) in enumerate(zip(a["cards"], pins)):
        x, y, h = 1215, (140, 490)[k], (300, 310)[k]
        body = (px_sheet(x, y, 320, h, PX_PAPER if k == 0 else PX_PAPER_LILA, 55 + k)
                + px_text(x + 24, y + 62, note["title"], 24, "evidence note title", 272, PX_INK)
                + f'<path d="M{x + 24} {y + 80} H{x + 120}" stroke="{PX_RIBBON}" stroke-width="3" stroke-linecap="round"/>'
                + "".join(px_text(x + 24, y + 136 + j * 48, line, 28, "evidence figure", 272, PX_INK) for j, line in enumerate(note["lines"])))
        if note.get("small"):
            body += px_text(x + 24, y + 244, note["small"], 17, "evidence scope", 272, PX_MUTED_INK, bold=False)
        body += (_p11_doc if k == 0 else _p11_research)(x + 262, y + h - 50)
        rot = (-1.5, 1.2)[k]
        g.append(land(f'<g transform="rotate({rot} {x + 160} {y + h / 2})">{body}</g>', .5 + k * .2, .5))
        px, py = x + 160, y + 18
        pin = (f'<g opacity="0">{beat("opacity", _n04_win(t, f=.01))}<g>{_p10_tr("translate", [(0, "0 -34"), (t, "0 -34"), (t + .02, "0 0"), (1, "0 0")])}'
               f'{px_pin(px, py)}</g></g>')
        g.append(pin + _n04_ping(px, py, 8, 44, PX_RIBBON, (t + .02,), .1, .8))
    return "".join(g), D, FREEZE


_P12_RESET = .965


def _p12_hold(a, b=_P12_RESET, lo=0, hi=1, f=.02):
    """beat() opacity pairs: lo until a, hi from a + f until the rewind (b), lo again by b + f."""
    return beat("opacity", [(0, lo), (a, lo), (a + f, hi), (b, hi), (b + f, lo), (1, lo)])


def _p12_gauge(gx, gy, r, marks, t0, t1):
    """A small paper gauge (a half dial): «before» zone on the left, «after» zone on the right; its needle sweeps from
    one to the other between t0 and t1 and stays there until the rewind. marks = (before label, after label)."""
    def pt(deg, rr):
        a = math.radians(deg)
        return f"{gx + rr * math.sin(a):.1f} {gy - rr * math.cos(a):.1f}"
    dial = f"M{gx - r} {gy} A{r} {r} 0 0 1 {gx + r} {gy} Z"
    zone = lambda a, b, col: (f'<path d="M{pt(a, r - 10)} A{r - 10} {r - 10} 0 0 1 {pt(b, r - 10)}" fill="none" stroke="{col}" '
                              f'stroke-width="8" stroke-linecap="round"/>')
    ticks = "".join(f'<path d="M{pt(d, r - 20)} L{pt(d, r - 26)}" stroke="{PX_EDGE}" stroke-width="1.6"/>' for d in (-45, 0, 45))
    sweep = _p10_tr("rotate", [(0, "-62"), (t0, "-62"), (t1, "62"), (_P12_RESET, "62"), (.985, "-62"), (1, "-62")])
    needle = (f'<g transform="translate({gx} {gy})"><g>{sweep}'
              f'<path d="M0 6 V{-(r - 14)}" stroke="{PX_INK}" stroke-width="2.6" stroke-linecap="round"/></g>'
              f'<circle r="5" fill="{PX_RIBBON}"/></g>')
    labels = "".join(px_text(gx + s * r, gy + 26, lab, 15, "p12 gauge zone", 110, PX_MUTED_INK, "middle")
                     for s, lab in zip((-1, 1), marks))
    return (f'<path d="{dial}" transform="translate(4 5)" fill="{PX_SHADOW}"/>'
            f'<path d="{dial}" fill="{PX_PAPER_2}" stroke="{PX_EDGE}" stroke-width="1.4" stroke-linejoin="round"/>'
            + zone(-86, -30, "color-mix(in srgb, var(--c2) 70%, var(--white))") + zone(30, 86, PX_RIBBON) + ticks + needle + labels)


@register("scene", "p12_exito")
def sc_p12_exito(sl, ctx):
    """A paper roll unrolls with nine named use cases (0.2-1.9 s). One of them, «Automatizar el reporte de avance», lifts
    on its magenta strip (2.3 s), flies out of the roll (3-4.1 s) and the success case card grows from it, in front
    (4-4.4 s): the line becomes the card's title. Its four fields fill one by one and stay: what changed (4.9 s), when
    (5.8 s), who (6.6 s) and the KPI with its «ejemplo» tag (7.4 s, static from the start); a paper gauge shows up with the
    KPI and its needle moves from the «before» zone to the «after» zone (8-9 s); the pin lands (9.5 s). Only non-text
    marks of the roll fade; its words keep full ink (AA). Frozen frame: the roll behind, the full card with its four
    fields and tag, the needle in the «after» zone."""
    if ORIENT() == "portrait":
        return _pp12_exito(sl, ctx)
    a = sl["args"] if "args" in sl else sl
    cases, pick = a["cases"], a["pick"]
    kpi = a["kpi"] if isinstance(a["kpi"], dict) else {"k": "KPI", "v": a["kpi"]}
    fields = [*a["fields"], kpi]   # what changed, when, who, then the KPI: four rows
    ip = cases.index(pick)
    g = []

    # the roll: a sheet revealed by a clip that grows down; its curl travels with the edge
    x0, w, y0, y1, gap, top = 846, 330, 132, 790, 66, 204
    unroll = (.02, .16)
    ys = [top + k * gap for k in range(len(cases))]
    fade = [(0, 1), (.25, 1), (.29, .35), (_P12_RESET, .35), (.985, 1), (1, 1)]
    mark = lambda y: (f'<rect x="{x0 + 22}" y="{y - 11}" width="10" height="10" rx="2" fill="{PX_MUTED_INK}" opacity=".6"/>'
                      f'<path d="M{x0 + 22} {y + 17} H{x0 + w - 22}" stroke="{PX_EDGE}" stroke-width="1.2" stroke-dasharray="3 6"/>')
    marks = "".join(mark(y) for k, y in enumerate(ys) if k != ip)
    # ponytail: the use-case words never fade (a faded label failed check-ui at 1.6:1); only bullets and rules do
    words = "".join(px_text(x0 + 44, y, c, 17, "p12 use case", w - 62, PX_MUTED_INK, bold=False)
                    for k, (c, y) in enumerate(zip(cases, ys)) if k != ip)
    # the picked line sits in the roll like the others until its strip lifts (then only its empty slot stays)
    yp = ys[ip]
    own = f'<g>{beat("opacity", [(0, 1), (.19, 1), (.2, 0), (_P12_RESET, 0), (.985, 1), (1, 1)])}' + mark(yp) + \
          px_text(x0 + 44, yp, pick, 17, "p12 use case", w - 62, PX_MUTED_INK, bold=False) + '</g>'
    sw = min(w - 44, bold_width(_(str(pick)), 17, current_factor()) + 30)
    slot = (f'<g opacity="0">{_p12_hold(.26)}<rect x="{x0 + 30}" y="{yp - 25}" width="{min(sw, w - 64):.0f}" height="36" rx="4" fill="none" '
            f'stroke="{PX_RIBBON}" stroke-width="1.6" stroke-dasharray="6 5"/></g>')
    clip_h = beat("height", [(0, 26), (unroll[0], 26), (unroll[1], y1 - y0 + 12), (.975, y1 - y0 + 12), (.995, 26), (1, 26)])
    sheet = (f'<defs><clipPath id="p12-roll-clip"><rect x="{x0 - 20}" y="{y0}" width="{w + 40}" height="{y1 - y0 + 12}">{clip_h}</rect></clipPath></defs>'
             f'<g clip-path="url(#p12-roll-clip)">{px_sheet(x0, y0, w, y1 - y0, PX_PAPER, 61)}'
             f'<g>{beat("opacity", fade)}{marks}</g>{words}{own}{slot}</g>')
    curl = (f'<g>{_p10_tr("translate", [(0, "0 0"), (unroll[0], "0 0"), (unroll[1], f"0 {y1 - y0 - 26}"), (.975, f"0 {y1 - y0 - 26}"), (.995, "0 0"), (1, "0 0")])}'
            f'<rect x="{x0 - 6}" y="{y0 + 16}" width="{w + 12}" height="18" rx="9" fill="{PX_PAPER_2}" stroke="{PX_EDGE}" stroke-width="1.2"/></g>')
    roller = (f'<rect x="{x0 - 24}" y="{y0 - 30}" width="{w + 48}" height="44" rx="22" fill="{PX_PAPER_2}" stroke="{PX_EDGE}" stroke-width="1.4"/>'
              f'<ellipse cx="{x0 - 4}" cy="{y0 - 8}" rx="9" ry="22" fill="none" stroke="{PX_EDGE}" stroke-width="1.4"/>'
              f'<ellipse cx="{x0 + w + 4}" cy="{y0 - 8}" rx="9" ry="22" fill="none" stroke="{PX_EDGE}" stroke-width="1.4"/>')
    roll_sh = f'<rect x="{x0 - 24 + PX_SH[0]}" y="{y0 - 30 + PX_SH[1]}" width="{w + 48}" height="44" rx="22" fill="{PX_SHADOW}"/>'
    g.append(land(roll_sh + sheet + curl + roller, .1, .5, -14))

    # the success case card, in front: it grows from the spot where the strip lands (its title)
    cx0, cy0, cw, ch = 1150, 172, 402, 588
    tx, ty, room = cx0 + 28, cy0 + 96, cw - 56
    grow, show = (.33, .38), .33
    head = px_text(tx, cy0 + 50, a["card"], 17, "p12 card label", room, PX_RIBBON)
    rules = "".join(f'<path d="M{tx} {cy0 + 190 + j * 86} H{cx0 + cw - 28}" stroke="{PX_EDGE}" stroke-width="1.4" stroke-dasharray="4 6"/>'
                    for j in range(len(fields)))
    card_ = px_sheet(cx0, cy0, cw, ch, "var(--white)", 62) + head + rules
    g.append(f'<g opacity="0">{_p12_hold(show, f=.02)}<g transform="translate({tx} {ty})"><g>'
             + _p10_tr("scale", [(0, ".15"), (grow[0], ".15"), (grow[1], "1"), (_P12_RESET, "1"), (.985, ".15"), (1, ".15")])
             + f'<g transform="translate({-tx} {-ty})">{card_}</g></g></g></g>')

    # the four fields fill one by one and stay; the KPI is static from the moment it shows (never counts)
    times = (.41, .48, .55, .62)
    for j, (fld, t) in enumerate(zip(fields, times)):
        yl = cy0 + 150 + j * 86
        row = (px_text(tx, yl, fld["k"], 16, "p12 field label", 160, PX_MUTED_INK)
               + px_text(tx, yl + 30, fld["v"], 19, "p12 field value", room, PX_INK, bold=False))
        if fld.get("tag"):
            row += pill(cx0 + cw - 28 - (bold_width(_(str(fld["tag"])), 15, current_factor()) + 36) / 2, yl - 6, fld["tag"],
                        "var(--c4)", ctx, 15, 120, "p12 example tag")
        g.append(f'<g opacity="0">{_p12_hold(t)}<g>'
                 + _p10_tr("translate", [(0, "0 10"), (t, "0 10"), (t + .03, "0 0"), (_P12_RESET, "0 0"), (.985, "0 10"), (1, "0 10")])
                 + row + '</g></g>')

    # the gauge shows up with the KPI; its needle moves from «before» to «after»
    gx, gy = cx0 + cw / 2, cy0 + ch - 64
    g.append(f'<g opacity="0">{_p12_hold(times[-1])}{_p12_gauge(gx, gy, 50, a["gauge"], .67, .75)}</g>')
    g.append(_n04_ping(gx, gy - 30, 10, 60, PX_RIBBON, (.75,), .1, .7))

    # the strip: the picked line, magenta band on its edge, lifts (2.3 s) and flies to the card's title spot
    ox, oy = x0 + 44, yp
    strip = (px_sheet(-14, -25, sw, 36, "var(--white)", 63)
             + f'<path d="M-14 -25 h6 v36 h-6 Z" fill="{PX_RIBBON}"/>'
             + px_text(0, 0, pick, 17, "p12 lifted case", w - 62, PX_INK))
    dx, dy = tx - ox, ty - oy
    fly = [(0, "0 0"), (.25, "0 0"), (.30, f"{dx * .5:.0f} {dy * .5 - 70:.0f}"), (.34, f"{dx} {dy}"), (_P12_RESET, f"{dx} {dy}"),
           (.985, "0 0"), (1, "0 0")]
    sc = [(0, "1"), (.25, "1"), (.34, "1.12"), (_P12_RESET, "1.12"), (.985, "1"), (1, "1")]
    g.append(f'<g opacity="0">{_p12_hold(.19, f=.01)}<g transform="translate({ox} {oy})"><g>{_p10_tr("translate", fly)}'
             f'<g>{_p10_tr("scale", sc)}{strip}</g></g></g></g>')
    g.append(_n04_ping(ox + sw / 2 - 14, oy - 7, 12, 80, PX_RIBBON, (.2,), .1, .8))

    # the pin lands on the card
    px_, py_ = cx0 + cw / 2, cy0 + 22
    pin_t = .76
    g.append(f'<g opacity="0">{beat("opacity", _n04_win(pin_t, f=.01))}<g>{_p10_tr("translate", [(0, "0 -34"), (pin_t, "0 -34"), (pin_t + .02, "0 0"), (1, "0 0")])}'
             f'{px_pin(px_, py_)}</g></g>' + _n04_ping(px_, py_, 8, 48, PX_RIBBON, (pin_t + .02,), .1, .8))
    return "".join(g), D, FREEZE


# ==================================================================================================== slides 13-15
_P13_RESET = .965


def _p13_on(a, b=_P13_RESET, f=.02, hi=1):
    """Hidden until a, shown from a + f until b, hidden again by b + f."""
    return beat("opacity", [(0, 0), (a, 0), (a + f, hi), (b, hi), (min(b + f, .999), 0), (1, 0)])


def _p13_tr(typ, pairs):
    """An additive transform loop with explicit times: pairs = [(fraction, 'values')]."""
    kt = ";".join(f"{t:.3f}" for t, _v in pairs)
    vals = ";".join(v for _t, v in pairs)
    return (f'<animateTransform attributeName="transform" type="{typ}" additive="sum" values="{vals}" keyTimes="{kt}" '
            f'dur="{D}s" repeatCount="indefinite"/>')


def _p13_pop(inner, x, y, a, f=.03):
    """inner (drawn around 0,0) appears at (x, y) at a, growing from .6, and stays until the rewind."""
    return (f'<g transform="translate({x:.1f} {y:.1f})"><g opacity="0">{_p13_on(a, f=f)}'
            + _p13_tr("scale", [(0, ".6 .6"), (a, ".6 .6"), (a + f, "1 1"), (_P13_RESET, "1 1"), (.985, ".6 .6"), (1, ".6 .6")])
            + inner + '</g></g>')


# ---------------------------------------------------------------- 13 · Tu turno: diagnostica qué de tu semana puede cambiar
def _p13_clock(cx, cy, r):
    """A small paper clock (the two minutes of the exercise): its hand turns once per loop and the magenta arc fills behind it."""
    ticks = "".join(f'<path d="M0 {-r + 7} V{-r + (15 if k % 3 == 0 else 11)}" stroke="{PX_INK}" stroke-width="{2 if k % 3 == 0 else 1.2}" '
                    f'stroke-linecap="round" transform="rotate({k * 30})"/>' for k in range(12))
    arc = (f'<circle r="{r - 22}" fill="none" stroke="{PX_RIBBON}" stroke-width="6" opacity=".55" pathLength="1" stroke-dasharray="1" '
           f'transform="rotate(-90)">{beat("stroke-dashoffset", [(0, 1), (.999, 0), (1, 1)])}</circle>')
    hand = (f'<g><animateTransform attributeName="transform" type="rotate" values="0;360" keyTimes="0;1" dur="{D}s" repeatCount="indefinite"/>'
            f'<path d="M0 6 V{-r + 16}" stroke="{PX_INK}" stroke-width="2.4" stroke-linecap="round"/></g>')
    return (f'<g transform="translate({cx} {cy})">'
            f'<circle cx="{PX_SH[0]}" cy="{PX_SH[1]}" r="{r}" fill="{PX_SHADOW}"/>'
            f'<circle r="{r}" fill="{PX_PAPER}" stroke="{PX_EDGE}" stroke-width="1.2"/>'
            f'<rect x="-9" y="{-r - 12}" width="18" height="10" rx="3" fill="{PX_PAPER_2}" stroke="{PX_EDGE}" stroke-width="1.2"/>'
            + ticks + arc + hand + f'<circle r="4" fill="{PX_RIBBON}"/></g>')


def _p13_icon(kind, x, y):
    """A round paper token at (x, y) with the line icon of one lens of the diagnosis."""
    s = f'fill="none" stroke="{PX_INK}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
    m = s.replace(PX_INK, PX_RIBBON)

    def gear(gx, gy, r, col):   # a line gear that stays crisp at icon size (the kit's px_gear fills up below r 10)
        return (f'<circle cx="{gx}" cy="{gy}" r="{r}" fill="none" stroke="{col}" stroke-width="1.6"/>'
                f'<circle cx="{gx}" cy="{gy}" r="{r * .35:.1f}" fill="{col}"/>'
                + "".join(f'<path d="M{gx} {gy - r - .6:.1f} V{gy - r - 3.2:.1f}" stroke="{col}" stroke-width="2.2" stroke-linecap="round" '
                          f'transform="rotate({d} {gx} {gy})"/>' for d in range(0, 360, 45)))
    art = {
        "friccion": f'<path d="M2 -10 L-5 1 H1 L-2 10 L6 -2 H0 Z" {m}/>',                                      # a spark: it grinds
        "repite": (f'<path d="M-8 -1 A8 8 0 0 1 6 -6" {s}/><path d="M7 -11 V-5 H1" {s}/>'                         # arrows in a loop
                   f'<path d="M8 1 A8 8 0 0 1 -6 6" {s}/><path d="M-7 11 V5 H-1" {s}/>'),
        "tediosa": (f'<path d="M-6 -10 H6 M-6 10 H6 M-5 -10 C-5 -3 5 3 5 10 M5 -10 C5 -3 -5 3 -5 10" {s}/>'       # an hourglass
                    f'<path d="M-3 8 H3" {m}/>'),
        "mecanica": gear(0, 0, 6.5, PX_INK),                                                                   # a gear
        "ia": spark(0, 0, .52, PX_RIBBON) + f'<path d="M5 7 L8 10 L13 4" {s}/>',                                # AI drafts, you check
        "auto": (f'<rect x="-11" y="-7" width="17" height="12" rx="1.5" {s}/><path d="M-11 -7 L-2.5 0 L6 -7" {s}/>'
                 + gear(7, 6, 3.4, PX_RIBBON)),                                                              # envelope with a gear
        "proceso": (f'<path d="M-11 -6 H-4 M-11 6 H-4 M-4 -6 L2 0 L-4 6 M2 0 H11" {s}/>'                        # two steps become one
                    f'<circle cx="2" cy="0" r="2.4" fill="{PX_RIBBON}"/>'),
    }[kind]
    return (f'<circle cx="{x + 3}" cy="{y + 4}" r="17" fill="{PX_SHADOW}"/>'
            f'<circle cx="{x}" cy="{y}" r="17" fill="{PX_PAPER_2}" stroke="{PX_EDGE}" stroke-width="1.2"/>'
            f'<g transform="translate({x} {y})">{art}</g>')


def _p13_card(x, y, w, h, label):
    """The task card: a post-it with its label wrapped in lines of at least 15 px (the kit's px_postit)."""
    return px_postit(x, y, w, h, PX_POSTIT, 34, -1.5, label, 16)


@register("scene", "p13_turno")
def sc_p13_turno(sl, ctx):
    """A paper diagnosis sheet any reader can use from the page alone: seven lenses, each with its icon, all visible from the
    entrance; three output trays under it and a two-minute paper clock. The task card «Consolidar el informe semanal»
    goes down lens by lens (1.9-7 s) and ticks the ones that apply, the ticks accumulating (the seventh stays unticked);
    then the trays of the ticked «how» lenses light up (7.6-8.1 s) and the final line appears (9 s). Frozen frame: the
    seven lenses with their marks, two trays lit, the final line."""
    if ORIENT() == "portrait":
        return _pp13_turno(sl, ctx)
    a = sl["args"] if "args" in sl else sl
    lenses, trays = a["lenses"], a["trays"]
    x0, y0, w, h = 836, 92, 560, 452
    ix, qx, bx = x0 + 34, x0 + 62, x0 + w - 52
    # rows: the four «is it worth it» lenses, a divider, then the three «how» lenses with their hint
    rows = []
    y = y0 + 44
    for k, ln in enumerate(lenses):
        if k and ln.get("hint") and not lenses[k - 1].get("hint"):
            y += 12
            rows.append({"divider": y - 30})
        cy = y + 6 if ln.get("hint") else y - 6
        rows.append({"k": k, "y": y, "cy": cy, "band": 58 if ln.get("hint") else 40})
        y += 70 if ln.get("hint") else 48
    lens_rows = [r for r in rows if "k" in r]
    g = [land(px_sheet(x0, y0, w, h, PX_PAPER, 35), .1, .5)]
    parts = []
    for r in rows:
        if "divider" in r:
            parts.append(f'<path d="M{x0 + 26} {r["divider"]} H{x0 + w - 26}" stroke="{PX_EDGE}" stroke-width="1.4" stroke-dasharray="4 6"/>')
            continue
        ln = lenses[r["k"]]
        p = (_p13_icon(ln["icon"], ix, r["cy"])
             + px_text(qx, r["y"], ln["q"], 19, "p13 lens question", bx - qx - 16, PX_INK)
             + f'<rect x="{bx}" y="{r["cy"] - 13}" width="26" height="26" rx="4" fill="var(--white)" stroke="{PX_MUTED_INK}" stroke-width="1.4"/>')
        if ln.get("hint"):
            p += px_text(qx, r["y"] + 24, ln["hint"], 16, "p13 lens hint", bx - qx - 16, PX_MUTED_INK, bold=False)
        parts.append(p)
    g.append(seq(parts, .25, .45, 10, 1.6))

    # the task card goes down lens by lens; a soft band marks the lens it is reading; each tick stays
    t_at = [.16 + .07 * k for k in range(len(lens_rows))]
    cw, chh, cx = 164, 64, x0 + w - 4
    tops = [r["cy"] - chh / 2 for r in lens_rows]
    tr = [(0, "0 0")]
    for k in range(1, len(tops)):
        tr += [(t_at[k] - .04, f"0 {tops[k - 1] - tops[0]:.0f}"), (t_at[k] - .01, f"0 {tops[k] - tops[0]:.0f}")]
    tr += [(_P13_RESET, f"0 {tops[-1] - tops[0]:.0f}"), (.985, "0 0"), (1, "0 0")]
    band_end = .62
    for k, (r, t) in enumerate(zip(lens_rows, t_at)):
        b = t_at[k + 1] - .04 if k + 1 < len(t_at) else band_end
        band = (f'<path d="M{x0 + 12} {r["cy"] - r["band"] / 2:.0f} h{w - 24} v{r["band"]} h{-(w - 24)} Z" '
                f'fill="color-mix(in srgb, var(--c4) 26%, transparent)"/>')
        g.insert(2, f'<g opacity="0">{_p13_on(t - .012, b, .012)}{band}</g>')
        if lenses[r["k"]].get("tick"):
            g.append(f'<g opacity="0">{_p13_on(t)}{check(bx + 13, r["cy"], .95, PX_RIBBON)}</g>'
                     + _n04_ping(bx + 13, r["cy"], 10, 40, PX_RIBBON, (t,), .08, .8))
        else:
            g.append(f'<g opacity="0">{_p13_on(t)}<path d="M{bx + 7} {r["cy"]} H{bx + 19}" stroke="{PX_MUTED_INK}" '
                     f'stroke-width="2.4" stroke-linecap="round"/></g>')
    g.append(land(f'<g>{_p13_tr("translate", tr)}{_p13_card(cx, tops[0], cw, chh, a["task"])}</g>', .6, .5, 0, 16))

    # the three trays: each belongs to one «how» lens (the last three) and lights once its lens got the tick
    hows = [r for r in lens_rows if lenses[r["k"]].get("hint")][-len(trays):]
    ty0, th, tw, tg = 566, 84, 228, 16
    for j, (lab, r) in enumerate(zip(trays, hows)):
        tx = x0 + j * (tw + tg)
        tray = px_sheet(tx, ty0, tw, th, PX_PAPER_2, 36 + j)
        lip = f'<path d="M{tx + 8} {ty0 + th - 16} H{tx + tw - 8}" stroke="{PX_EDGE}" stroke-width="1.4"/>'
        body = _p13_icon(lenses[r["k"]]["icon"], tx + 32, ty0 + 38) + px_text(tx + 58, ty0 + 45, lab, 17, "p13 tray", tw - 70, PX_INK)
        lit = ""
        if lenses[r["k"]].get("tick"):
            t = .635 + .04 * j
            glowp = (f'<path d="{px_sheet_path(tx, ty0, tw, th, 36 + j)}" fill="color-mix(in srgb, var(--accent) 14%, var(--white))" '
                     f'stroke="{PX_RIBBON}" stroke-width="2.4" stroke-linejoin="round"/>' + check(tx + tw - 20, ty0 + 20, .7, PX_RIBBON))
            lit = f'<g opacity="0">{_p13_on(t)}{glowp}</g>' + _n04_ping(tx + tw / 2, ty0 + th / 2, 30, 120, PX_RIBBON, (t,), .1, .6)
        g.append(land(tray + lip + lit + body, .5 + .1 * j, .45, 12))

    # the final line: describe it in one sentence
    fy = 672
    fin = (px_sheet(x0, fy, 716, 54, PX_PAPER, 39)
           + px_text(x0 + 24, fy + 35, a["close"], 19, "p13 final line", 668, PX_INK))
    g.append(f'<g opacity="0">{_p13_on(.75)}'
             + _p13_tr("translate", [(0, "0 12"), (.75, "0 12"), (.78, "0 0"), (_P13_RESET, "0 0"), (.985, "0 12"), (1, "0 12")])
             + fin + '</g>')
    g.append(f'<path d="M{x0 + 24} {fy + 44} H{x0 + 692}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{PX_RIBBON}" '
             f'stroke-width="2.4" stroke-linecap="round">{beat("stroke-dashoffset", [(0, 1), (.77, 1), (.84, 0), (_P13_RESET, 0), (.985, 1), (1, 1)])}</path>')

    # the two-minute clock, a small paper accent, and its label on the stage
    ccx, ccy = 1508, 782
    g.append(land(_p13_clock(ccx, ccy, 34), .8, .5, 12))
    lab = a["clock"]
    g.append(land(T(ccx - 52, ccy + 7, lab, fit(lab, 19, 220, "p13 clock"), "var(--white)", f'text-anchor="end" {W6}'), .9, .45, 0))
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 14 · ¿Qué harías con el tiempo del lunes?
def _p14_bulb():
    """The pop-up paper bulb, its base at (0, 0), glass above; returns (unlit, lit overlay)."""
    glass = "M-17 -26 C-17 -40 -42 -52 -42 -84 C-42 -108 -23 -126 0 -126 C23 -126 42 -108 42 -84 C42 -52 17 -40 17 -26 Z"
    base = (f'<rect x="-17" y="-26" width="34" height="26" rx="4" fill="{PX_PAPER_2}" stroke="{PX_EDGE}" stroke-width="1.4"/>'
            f'<path d="M-17 -17 H17 M-17 -9 H17" stroke="{PX_EDGE}" stroke-width="1.4"/>')
    fil = f'<path d="M-9 -28 V-54 Q0 -72 9 -54 V-28" fill="none" stroke="{PX_INK}" stroke-width="1.8" stroke-linejoin="round"/>'
    unlit = f'<path d="{glass}" transform="translate({PX_SH[0]} {PX_SH[1]})" fill="{PX_SHADOW}"/>' + f'<path d="{glass}" fill="{PX_PAPER}" stroke="{PX_EDGE}" stroke-width="1.4"/>' + fil + base
    rays = "".join(f'<path d="M0 -140 V-156" stroke="var(--c4)" stroke-width="3" stroke-linecap="round" transform="rotate({a} 0 -84)"/>'
                   for a in (-80, -45, 0, 45, 80))
    lit = (f'<path d="{glass}" fill="color-mix(in srgb, var(--c4) 70%, var(--white))" stroke="var(--c3)" stroke-width="1.4"/>'
           + fil.replace(PX_INK, "var(--c3)") + base + rays)
    return unlit, lit


def _p14_pair():
    """Two faceless people talking, a small empty speech bubble between them."""
    return (px_sheet(-70, -58, 140, 116, PX_PAPER, 43)
            + person(-30, 36, .9, "var(--c1)") + person(30, 36, .9, "var(--accent)")
            + f'<path d="M-16 -44 H16 Q22 -44 22 -38 V-24 Q22 -18 16 -18 H4 L-2 -10 V-18 H-16 Q-22 -18 -22 -24 V-38 Q-22 -44 -16 -44 Z" '
              f'fill="var(--white)" stroke="{PX_INK}" stroke-width="1.4"/>'
            + "".join(f'<circle cx="{c}" cy="-31" r="2.2" fill="{PX_INK}"/>' for c in (-8, 0, 8)))


def _p14_plan():
    """A sketch sheet: a floor plan in ink, a magenta arrow drawn over it."""
    return ('<g transform="rotate(5)">' + px_sheet(-62, -52, 124, 104, PX_PAPER_LILA, 44)
            + f'<path d="M-44 -34 H44 V34 H-44 Z M-4 -34 V6 H44 M-44 6 H-22" fill="none" stroke="{PX_INK}" stroke-width="1.6"/>'
            + f'<path d="M-32 24 C-16 16 4 22 24 -18" fill="none" stroke="{PX_RIBBON}" stroke-width="2.2" stroke-linecap="round"/>'
            + f'<path d="M14 -16 L25 -20 L27 -8" fill="none" stroke="{PX_RIBBON}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></g>')


def _p14_plant(a, ok):
    """A small plant in a paper pot; its stem and leaves grow from a, once it appears."""
    grow = _p13_tr("scale", [(0, "1 .2"), (a, "1 .2"), (a + .08, "1 1"), (_P13_RESET, "1 1"), (.985, "1 .2"), (1, "1 .2")])
    leaves = (f'<path d="M0 0 V-62" stroke="{ok}" stroke-width="2.4" stroke-linecap="round"/>'
              f'<path d="M0 -26 C-26 -28 -34 -46 -30 -56 C-12 -54 -2 -42 0 -26 Z" fill="{ok}"/>'
              f'<path d="M0 -44 C22 -48 32 -64 28 -76 C10 -72 0 -60 0 -44 Z" fill="{ok}"/>')
    return (f'<path d="M-26 0 H26 L20 40 H-20 Z" transform="translate(5 7)" fill="{PX_SHADOW}"/>'
            f'<g transform="translate(0 2)"><g>{grow}{leaves}</g></g>'
            f'<path d="M-26 0 H26 L20 40 H-20 Z" fill="var(--c3)" stroke="{PX_EDGE}" stroke-width="1.2"/>'
            f'<rect x="-30" y="-4" width="60" height="12" rx="2" fill="{PX_PAPER_2}" stroke="{PX_EDGE}" stroke-width="1.2"/>')


@register("scene", "p14_tiempo")
def sc_p14_tiempo(sl, ctx):
    """The paper week, Monday morning highlighted with its two-hour report. The magenta ribbon cuts the block out
    (2.2-3.4 s); the piece lifts and settles beside the calendar, leaving the hole and its shadow (3.6-4.8 s); a paper
    bulb pops up from the hole on the ribbon (4.8-6.2 s) and lights (6.6 s); three wordless ideas appear around it: two
    people talking (7.4 s), a plan (8.4 s), a plant that grows (9.4 s). Frozen frame: the cut hole, the lit bulb and the
    three ideas."""
    if ORIENT() == "portrait":
        return _pp14_tiempo(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    x0, y0, w, h = 960, 430, 580, 370
    hy = y0 + 54
    cw = (w - 32) / 5
    cols = [x0 + 16 + k * cw for k in range(5)]
    cal = [px_sheet(x0, y0, w, h, PX_PAPER, 41),
           f'<rect x="{cols[0]:.1f}" y="{hy + 4}" width="{cw:.1f}" height="196" fill="var(--c4)" opacity=".22"/>',
           f'<path d="M{x0 + 16} {hy} H{x0 + w - 16}" stroke="{PX_INK}" stroke-width="1.4"/>']
    for k, day in enumerate(sl["days"][:5]):
        cal.append(px_text(cols[k] + cw / 2, hy - 18, day, 19, "p14 day", cw - 12, PX_RIBBON if k == 0 else PX_INK, "middle"))
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

    # the Monday block, the hole it leaves and the magenta cut around it
    bx, by, bw, bh = cols[0] + 6, hy + 8, cw - 12, 88
    hole = (f'<rect x="{bx:.1f}" y="{by}" width="{bw:.1f}" height="{bh}" rx="3" fill="color-mix(in srgb, var(--ink) 88%, var(--c1))"/>'
            f'<path d="M{bx:.1f} {by + bh} V{by} H{bx + bw:.1f}" fill="none" stroke="{PX_SHADOW}" stroke-width="9" stroke-linejoin="round"/>')
    g.append(f'<g opacity="0">{_p13_on(.29)}{hole}</g>')
    cut = (f'<path d="M{bx:.1f} {by} H{bx + bw:.1f} V{by + bh} H{bx:.1f} Z" pathLength="1" stroke-dasharray="1" fill="none" stroke="{PX_RIBBON}" '
           f'stroke-width="2.4" stroke-linejoin="round">{beat("stroke-dashoffset", [(0, 1), (.18, 1), (.28, 0), (_P13_RESET, 0), (.985, 1), (1, 1)])}</path>')
    title, dur = sl["block"]
    pcx, pcy = bx + bw / 2, by + bh / 2
    piece = (px_sheet(bx, by, bw, bh, PX_POSTIT, 42)
             + px_text(pcx, by + 38, title, 17, "p14 block", bw - 14, PX_INK, "middle")
             + px_text(pcx, by + 64, dur, 17, "p14 block", bw - 14, PX_MUTED_INK, "middle"))
    lift = [(0, "0 0"), (.3, "0 0"), (.33, "12 -36"), (.4, "-150 196"), (_P13_RESET, "-150 196"), (.985, "0 0"), (1, "0 0")]
    turn = [(0, f"0 {pcx:.1f} {pcy:.1f}"), (.3, f"0 {pcx:.1f} {pcy:.1f}"), (.4, f"-9 {pcx:.1f} {pcy:.1f}"),
            (_P13_RESET, f"-9 {pcx:.1f} {pcy:.1f}"), (.985, f"0 {pcx:.1f} {pcy:.1f}"), (1, f"0 {pcx:.1f} {pcy:.1f}")]
    g.append(land(f'<g>{_p13_tr("translate", lift)}<g>{_p13_tr("rotate", turn)}{piece}</g></g>', .35, .45, 0))
    g.append(cut)

    # from the hole the bulb pops up on the ribbon, then it lights
    bulb_x, bulb_y = 1130, 360
    stalk = f"M{pcx:.1f} {pcy:.1f} C{pcx:.1f} {pcy - 90:.1f} {bulb_x} {bulb_y + 80} {bulb_x} {bulb_y}"
    g.append(f'<path d="{stalk}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{PX_RIBBON}" stroke-width="3" stroke-linecap="round">'
             f'{beat("stroke-dashoffset", [(0, 1), (.4, 1), (.52, 0), (_P13_RESET, 0), (.985, 1), (1, 1)])}</path>')
    g.append(f'<g opacity="0">{_p13_on(.55, f=.04)}{glow(bulb_x, bulb_y - 84, 170, "var(--c4)", .7)}</g>')
    unlit, lit = _p14_bulb()
    g.append(f'<g opacity="0">{_p13_on(.4)}'
             f'<animateMotion dur="{D}s" repeatCount="indefinite" path="{stalk}" keyTimes="0;.4;.52;1" keyPoints="0;0;1;1" calcMode="linear"/>'
             f'<g>{_p13_tr("scale", [(0, ".4 .4"), (.4, ".4 .4"), (.52, "1 1"), (1, "1 1")])}'
             f'{unlit}<g opacity="0">{_p13_on(.55, f=.04)}{lit}</g></g></g>')

    # three wordless ideas around the light: a conversation, a plan, a plant that grows
    g.append(_p13_pop(_p14_pair(), 915, 250, .62))
    g.append(_p13_pop(_p14_plan(), 1290, 170, .7))
    g.append(_p13_pop(_p14_plant(.78, ok), 1440, 320, .78))
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 15 · Si puedes describirlo, la IA puede construirlo.
def _p15_bez(p):
    """Arc-length fractions at the end of each cubic segment of p = [start, (c1, c2, end), …]."""
    lens, cur = [], p[0]
    for c1, c2, e in p[1:]:
        pts = [tuple((1 - t) ** 3 * cur[i] + 3 * (1 - t) ** 2 * t * c1[i] + 3 * (1 - t) * t * t * c2[i] + t ** 3 * e[i] for i in (0, 1))
               for t in [k / 60 for k in range(61)]]
        lens.append(sum(((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** .5 for a, b in zip(pts, pts[1:])))
        cur = e
    tot, acc, out = sum(lens), 0, []
    for L in lens:
        acc += L
        out.append(acc / tot)
    return out


def _p15_d(p):
    return f"M{p[0][0]} {p[0][1]} " + " ".join(f"C{a[0]} {a[1]} {b[0]} {b[1]} {c[0]} {c[1]}" for a, b, c in p[1:])




@register("scene", "p15_lema")
def sc_p15_lema(sl, ctx):
    """The close. The client leads: its logo, the strongest element of the art, top-center on its white paper chip;
    below it the strategy map of slide 3, three stops joined by the magenta ribbon, and the signer (a trainer) (the one
    Amaris mark of the slide is the engine's footer lockup). The paper plane of the cover returns (1.4 s), flies the
    route lighting each stop as it passes (explicas, revisas, automatizas) and lands on the last one (8.4 s);
    «Audacious Ideas, Delivered Beyond.» appears in the corner (9 s). Frozen frame: the plane landed, the logo, the
    trainer with his name and role, the sign."""
    if ORIENT() == "portrait":
        return _pp15_lema(sl, ctx)
    g = [land(px_logo_client(1190, 92, 340), .1, .5)]

    # the strategy map: a folded paper sheet, three stops on the ribbon route
    mx, my, mw, mh = 860, 338, 660, 258
    stops = ((960, my + 160), (1190, my + 104), (1420, my + 160))
    route = [stops[0], ((1040, my + 96), (1110, my + 88), stops[1]), ((1280, my + 120), (1340, my + 184), stops[2])]
    sheet = (px_sheet(mx, my, mw, mh, PX_PAPER, 51)
             + "".join(f'<path d="M{x} {my + 8} V{my + mh - 8}" stroke="{PX_EDGE}" stroke-width="1.2" stroke-dasharray="4 6"/>' for x in (1080, 1300)))
    g.append(land(sheet, .25, .5))
    g.append(px_ribbon(f"M{mx + 24} {my + mh - 24} C{mx + 60} {my + mh - 32} {stops[0][0] - 40} {stops[0][1] + 20} {stops[0][0]} {stops[0][1]}", 3, .45, .35, 'opacity=".6"'))
    g.append(px_ribbon(_p15_d(route), 4, .7, .9))
    icons = []
    for k, ((x, y), lab) in enumerate(zip(stops, sl["stops"][:3])):
        icons.append(px_icon(k, x, y) + px_text(x, y + 70, lab, 19, "p15 stop", 200, PX_INK, "middle"))
    g.append(seq(icons, .45, .45, 14, 1.4))

    # the plane returns, flies the route above the stops and lands on the last one; each stop lights as it passes
    lift = 66
    fly = [(840, my + 44), ((890, my + 28), (930, my + 84), (stops[0][0], stops[0][1] - lift)),
           ((1040, my + 96 - lift), (1110, my + 88 - lift), (stops[1][0], stops[1][1] - lift)),
           ((1290, my + 48), (1370, stops[2][1] - 56), (stops[2][0], stops[2][1] - 56))]
    fr = _p15_bez(fly)
    t0, t1 = .14, .7
    at = [t0 + (t1 - t0) * f for f in fr]  # when the plane is over each stop
    for k, ((x, y), t) in enumerate(zip(stops, at)):
        g.append(f'<g opacity="0">{_p13_on(t)}{px_icon(k, x, y, lit=True)}</g>')
    g.append(f'<g opacity="0">{_p13_on(t0 - .02)}'
             f'<animateMotion dur="{D}s" repeatCount="indefinite" path="{_p15_d(fly)}" rotate="auto" keyTimes="0;{t0};{t1};1" keyPoints="0;0;1;1" '
             f'calcMode="linear"/>'
             f'{px_plane(0, 0, .72)}</g>')
    land_ring = (f'<ellipse cx="{stops[2][0]}" cy="{stops[2][1] - 40}" rx="46" ry="8" fill="none" stroke="{PX_RIBBON}" stroke-width="1.6">'
                 f'{beat("rx", [(0, 20), (t1, 20), (t1 + .06, 60), (1, 60)])}</ellipse>')
    g.append(f'<g opacity="0">{beat("opacity", [(0, 0), (t1, 0), (t1 + .01, .9), (t1 + .06, 0), (1, 0)])}{land_ring}</g>')

    # the signer signs (the footer lockup is the slide's one Amaris mark); the line in the corner once the plane has landed
    g.append(land(px_signer(900, 618, 112, sl["name"], sl["role"], ctx), .6, .5))
    s = sl["sign"]
    g.append(f'<g opacity="0">{_p13_on(t1 + .05, f=.04)}'
             + T(1540, 796, s, fit(s, 18, 380, "p15 sign"), "var(--muted)", f'text-anchor="end" font-style="italic" {W6}') + '</g>')
    return "".join(g), D, FREEZE

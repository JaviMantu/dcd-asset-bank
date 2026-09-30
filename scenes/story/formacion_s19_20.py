"""Bench g: slides 19-20 of the class «Presentaciones de prospección de alto impacto». The close calls back to the opening.
v19_tiempo - the same Tuesday-to-Thursday week as slide 2 (v02_martes); the two hours «Para preparar» hold three chores
             (moving boxes, finding a template, fixing the format) that dissolve one by one into three client tasks;
             a thread carries them to Thursday 10:00, which lights up «Lista».
v20_lema   - the Thursday table of slide 1 (v01_portada): you and the prospect's manager in conversation, the tailored
             cover on the screen behind; her three worries of slide 4 check in on the table; the signature appears.
Timing helpers come from the harvested energía scenes (_n01_on, _n01_tr); private helpers here are _v19_* / _v20_*."""


_V19_GREY = "color-mix(in srgb, var(--white) 14%, var(--ink))"   # the grey of slides 1-2


def _v19_y(h):
    """Hour h on the calendar of slide 2."""
    return 200 + (h - 9) * 62


def _v19_off(a, f=.03):
    """Shown until a, gone until the reset, back for the next lap."""
    return beat("opacity", [(0, 1), (a, 1), (a + f, 0), (.97, 0), (1, 1)])


def _v19_block(x, y0, y1, w, lab, fill, stroke, where):
    return (card(x + 2, y0 + 2, w - 4, y1 - y0 - 4, fill, stroke, 8, 1.4)
            + TC(x + w / 2, (y0 + y1) / 2 + 6, lab, fit(lab, 16, w - 20, where, floor=15), "var(--white)", W6))


# ---------------------------------------------------------------- slide 19: the hours you get back
@register("scene", "v19_tiempo")
def sc_v19_tiempo(sl, ctx):
    """The week of slide 2, Tuesday 4 pm. The two hours to prepare hold «Mover cajas», «Buscar una plantilla» and
    «Ajustar el formato»; each dissolves into small boxes and in its place lights a task for the client: «Leer al
    cliente», «Preparar las preguntas», «Pensar su caso de éxito». A thread takes them to Thursday 10:00, which gets its
    check: «Lista». Frozen frame: the three new blocks lit, the meeting ready."""
    if ORIENT() == "portrait":
        return _pv19_tiempo(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    xs, cw = [900, 1118, 1336], 206
    g = [glow(1220, 450, 460, "var(--brand)", .5)]
    grid = "".join(f'<path d="M900 {_v19_y(h)} H1542" stroke="var(--line)" stroke-width="1"/>' for h in range(9, 19))
    grid += "".join(T(886, _v19_y(h) + 5, f"{h}:00", 15, "var(--muted)", 'text-anchor="end"') for h in range(9, 19))
    grid += "".join(TC(x + cw / 2, 182, d, fit(d, 19, cw - 12, "tiempo day"), "var(--white)", W6) for x, d in zip(xs, sl["days"]))
    g.append(land(grid, .1, .5, 0))
    # the clock of slide 2, at 4:00
    cx, cy = 852, 146
    clock = (f'<circle cx="{cx}" cy="{cy}" r="28" fill="var(--card)" stroke="var(--c2)" stroke-width="1.6"/>'
             f'<path d="M{cx} {cy} L{cx + 11.3:.1f} {cy + 6.5:.1f}" stroke="var(--white)" stroke-width="3" stroke-linecap="round"/>'
             f'<path d="M{cx} {cy} V{cy - 19}" stroke="var(--white)" stroke-width="2" stroke-linecap="round"/>'
             f'<circle cx="{cx}" cy="{cy}" r="2.5" fill="var(--c5)"/>')
    g.append(land(clock, .2, .45, 0))
    # Tuesday before 4 pm is gone; the now line
    ny = _v19_y(16)
    past = (f'<rect x="{xs[0]}" y="{_v19_y(9) + 2}" width="{cw}" height="{ny - _v19_y(9) - 4}" rx="10" fill="{_V19_GREY}" opacity=".7"/>'
            + TC(xs[0] + cw / 2, (_v19_y(9) + ny) / 2 - 20, sl["past"], 16, "var(--muted)", W6))
    now = (f'<path d="M{xs[0] - 6} {ny} H{xs[0] + cw}" stroke="var(--c5)" stroke-width="2"/>'
           f'<circle cx="{xs[0] - 6}" cy="{ny}" r="5" fill="var(--c5)"/>'
           + pill(xs[0] + cw / 2, ny - 26, sl["now"], "var(--c5)", ctx, 16, cw - 10, "tiempo now", 14))
    g.append(land(past, .3, .5, 0) + land(now, .5, .45, -10))
    # the rest of the week, already full
    blocks = []
    for day, h0, h1, lab in sl["busy"]:
        x, y0, y1 = xs[day], _v19_y(h0), _v19_y(h1)
        body = (TCW(x + cw / 2, (y0 + y1) / 2 - 4, lab, 20, 16, "var(--white)", W6, 1.2) if y1 - y0 >= 70
                else TC(x + cw / 2, (y0 + y1) / 2 + 6, lab, fit(lab, 16, cw - 24, "tiempo busy"), "var(--white)", W6))
        blocks.append(card(x + 2, y0 + 2, cw - 4, y1 - y0 - 4, "color-mix(in srgb, var(--c2) 20%, var(--ink))", "var(--line)", 8, 1.2) + body)
    g.append(seq(blocks, .35, .45, 10, 1.5))
    # Thursday 10:00, the prospect meeting, glowing as on slide 2
    mx, my0, my1 = xs[2], _v19_y(10), _v19_y(10.5)
    meet = (f'<rect x="{mx - 6}" y="{my0 - 6}" width="{cw + 12}" height="{my1 - my0 + 12}" rx="12" fill="var(--c4)" opacity=".2">'
            f'{loop("opacity", ".08;.35;.08", 2.2)}</rect>'
            + card(mx + 2, my0 + 2, cw - 4, my1 - my0 - 4, "var(--c4)", "var(--c4)", 7, 0)
            + TC(mx + cw / 2, my0 + 21, sl["meet_time"], 16, ctx.brand.on("var(--c4)"), W6)
            + TCW(mx + cw / 2, my1 + 30, sl["meet"], 20, 17, "var(--c4)", W6, 1.25))
    g.append(land(meet, .7, .5, 0))
    # the two hours to prepare: the dashed frame of slide 2 and its label above it
    fd, f0, f1 = sl["free"]
    fx, fy0, fy1 = xs[fd], _v19_y(f0), _v19_y(f1)
    frame = (f'<rect x="{fx + 1}" y="{fy0 + 1}" width="{cw - 2}" height="{fy1 - fy0 - 2}" rx="9" fill="none" stroke="var(--c4)" '
             f'stroke-width="2" stroke-dasharray="7 6">{loop("stroke-dashoffset", "0;-26", 1.4)}</rect>'
             + TC(fx + cw / 2, fy0 - 14, sl["prep"], fit(sl["prep"], 16, cw - 8, "tiempo prep", floor=15), "var(--c4)", W6))
    g.append(land(frame, .9, .45, 0))
    # three chores dissolve, one by one, into three tasks for the client
    n = len(sl["before"])
    hh = (fy1 - fy0) / n
    shows = [.20 + k * .14 for k in range(n)]
    olds, news = [], []
    for k, (old, new) in enumerate(zip(sl["before"], sl["after"])):
        y0, y1, a = fy0 + k * hh, fy0 + (k + 1) * hh, shows[k]
        crumbs = "".join(f'<rect x="{fx + cw / 2 + dx - 4}" y="{(y0 + y1) / 2 - 4:.1f}" width="8" height="8" rx="1.5" fill="none" stroke="var(--muted)" stroke-width="1.3" opacity="0">'
                         + beat("opacity", [(0, 0), (a, 0), (a + .01, .9), (a + .07, 0), (1, 0)])
                         + _n01_tr([(0, "0 0"), (a, "0 0"), (a + .07, f"{dx * .9:.0f} {-26 - abs(dx) * .3:.0f}"), (1, f"{dx * .9:.0f} {-26 - abs(dx) * .3:.0f}")])
                         + '</rect>' for dx in (-60, -24, 16, 52))
        olds.append(f'<g>{_v19_off(a)}' + _v19_block(fx, y0, y1, cw, old, _V19_GREY, "var(--line)", "tiempo before") + '</g>' + crumbs)
        news.append(f'<g>{_n01_on(a + .03, 1, .03)}'
                    + _v19_block(fx, y0, y1, cw, new, "color-mix(in srgb, var(--c4) 24%, var(--ink))", "var(--c4)", "tiempo after") + '</g>')
    g.append(land("".join(olds), 1.0, .45, 0) + "".join(news))
    # the thread to Thursday; the meeting is ready
    lx, ly = mx + cw / 2, 392
    t0 = shows[-1] + .09
    thread = f"M{fx + cw - 2} {(fy0 + fy1) / 2:.0f} C{mx + 80} {(fy0 + fy1) / 2:.0f} {lx} {ly + 170} {lx} {ly + 30}"
    g.append(f'<g>{_n01_on(t0)}<path d="{thread}" fill="none" stroke="var(--c4)" stroke-width="1.6" stroke-dasharray="3 6" opacity=".9"/>'
             f'<path d="M{lx - 7} {ly + 40} L{lx} {ly + 30} L{lx + 7} {ly + 40}" fill="none" stroke="var(--c4)" stroke-width="1.8" stroke-linecap="round"/></g>')
    g.append(f'<g>{_n01_on(t0, t0 + .08, .01)}{token("var(--c4)", 6)}{move(thread, [(0, 0), (t0, 0), (t0 + .08, 1), (1, 1)], D)}</g>')
    t1 = t0 + .08
    rs = fit(sl["ready"], 17, 120, "tiempo ready", floor=15)
    rw = bold_width(_(str(sl["ready"])), rs, current_factor()) + 62
    ready = (card(lx - rw / 2, ly - 18, rw, 36, ok, ok, 18, 0)
             + f'<circle cx="{lx - rw / 2 + 19}" cy="{ly}" r="11" fill="var(--ink)"/>' + check(lx - rw / 2 + 19, ly + .5, .5, ok)
             + T(lx - rw / 2 + 38, ly + rs * .36, sl["ready"], rs, ctx.brand.on(ok), W6))
    g.append(f'<g>{_n01_on(t1, 1, .03)}<rect x="{mx - 4}" y="152" width="{cw + 8}" height="{_v19_y(18) - 150}" rx="14" fill="var(--c4)" '
             f'fill-opacity=".05" stroke="var(--c4)" stroke-width="2"/>'
             + TC(mx + cw / 2, 182, sl["days"][2], fit(sl["days"][2], 19, cw - 12, "tiempo day"), "var(--c4)", W6) + ready + '</g>')
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- slide 20: the conversation, on Thursday
def _v20_you(skin, jacket, hair):
    """You: a faceless bust, three-quarter view facing right, short hair (the _n10_bust line, without the headset)."""
    jd = "M-46 60 C-46 32 -31 16 -9 13 C-3 12 7 12 13 13 C35 16 50 32 50 60 Z"
    return (f'<path d="{jd}" fill="{jacket}"/><path d="{jd}" {_N10_RIM}/>'
            '<path d="M-5 13 L3 26 L11 13 Z" fill="var(--white)" opacity=".92"/>'
            f'<path d="M-6 -6 C-5 2 -5 8 -6 14 C-1 17 6 17 10 14 C8 8 8 2 8 -6 Z" fill="{shade(skin, 14)}"/>'
            f'<path d="M-10 -22 C-11 -39 2 -45 13 -40.5 C21 -37 23 -28 21 -20 C20 -13.5 17 -7.5 12 -4 C6.5 -.5 -1.5 -1.5 -6.5 -7 '
            f'C-10 -11.5 -10 -16.5 -10 -22 Z" fill="{skin}"/>'
            f'<ellipse cx="-5.5" cy="-19" rx="2.5" ry="4" fill="{shade(skin, 14)}"/>'
            f'<path d="M-13 -20 C-15 -41 3 -50 16 -42.5 C21.5 -39 23 -34 22 -30.5 C17.5 -35 10 -36.5 4 -35.5 C-1 -34.5 -4.5 -31.5 -6 -26 '
            f'C-7 -23 -8.5 -20.5 -10.5 -17.5 Z" fill="{hair}"/><path d="M-12 -28 C-10 -41 4 -46 15 -41.5" {_N10_RIM}/>')


def _v20_waves(cx, cy, side, turns):
    """Three speech arcs opening from (cx, cy) toward side (+1 right, -1 left), shown in the turns [(a, b)]."""
    arcs = ""
    for k, r in enumerate((12, 22, 32)):
        dx, dy = r * .7 * side, r * .7
        arcs += (f'<path d="M{cx + dx:.1f} {cy - dy:.1f} A{r} {r} 0 0 {1 if side > 0 else 0} {cx + dx:.1f} {cy + dy:.1f}" fill="none" '
                 f'stroke="var(--c4)" stroke-width="2" stroke-linecap="round">{loop("opacity", ".25;1;.25", 1.2, k * .3)}</path>')
    pairs = [(0, 0)]
    for a, b in turns:
        pairs += [(a, 0), (a + .015, 1), (b, 1), (min(b + .015, .999), 0)]
    return f'<g opacity="0">{beat("opacity", pairs + [(1, 0)])}{arcs}</g>'


@register("scene", "v20_lema")
def sc_v20_lema(sl, ctx):
    """The Thursday table of slide 1. The cover made for her, lit on the screen behind; you on the left, the prospect's
    manager on the right, faceless, talking by turns (speech arcs both ways, then both at once). As they talk, her three
    worries of slide 4 check in one by one on the table, softly; last, the signature. Frozen frame: the conversation,
    the three checks, the signature."""
    if ORIENT() == "portrait":
        return _pv20_lema(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    g = [glow(1190, 420, 480, "var(--brand)", .55)]
    # the screen with the cover of slide 1, lit
    X, Y, W_, H_ = 985, 100, 420, 284
    cover = (card(X - 14, Y - 14, W_ + 28, H_ + 28, "var(--dim)", "var(--line)", 20, 1.2)
             + card(X, Y, W_, H_, "var(--card)", "var(--c2)", 14, 1.5)
             + f'<rect x="{X - 3}" y="{Y - 3}" width="{W_ + 6}" height="{H_ + 6}" rx="17" fill="none" stroke="var(--c4)" stroke-width="2">'
             f'{loop("stroke-opacity", ".45;1;.45", 2.6)}</rect>'
             + T(X + 26, Y + 44, sl["for_whom"], fit(sl["for_whom"], 17, 300, "lema cover for"), "var(--c4)", W6)
             + TCW(X + 26, Y + 98, sl["promise"], 26, 24, "var(--white)", W6, 1.2, "start")
             + T(X + 26, Y + 178, sl["cover_sub"], fit(sl["cover_sub"], 18, 370, "lema cover sub"), "var(--muted)")
             + f'<rect x="{X + W_ - 70}" y="{Y + 18}" width="46" height="46" rx="12" fill="var(--c3)"/>'
             f'<path d="M{X + W_ - 58} {Y + 52} Q{X + W_ - 47} {Y + 26} {X + W_ - 36} {Y + 52}" fill="none" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/>')
    ms = fit(sl["meeting"], 17, 300, "lema meeting")
    pw = bold_width(_(str(sl["meeting"])), ms, current_factor()) + 36
    cover += pill(X + 26 + pw / 2, Y + H_ - 44, sl["meeting"], "var(--c4)", ctx, 17, 336, "lema meeting")
    g.append(land(cover, .1, .55, 0))
    # warmth between them
    g.append(f'<g>{loop("opacity", ".35;1;.35", 4)}{glow(1190, 500, 130, "var(--c4)", .22)}</g>')
    # you (left, facing right) and her, the manager of slide 1 (right, facing left)
    you = f'<g>{bob(0, 2, 4.6)}<g transform="translate(990 548) scale(2.2)">{_v20_you(SKIN_LIGHT, "var(--c2)", HAIR)}</g></g>'
    her = f'<g>{bob(0, 2, 4.4, 1.3)}<g transform="translate(1390 548) scale(-2.2 2.2)">{_n10_bust(SKIN_BROWN, "var(--c1)", HAIR, "long")}</g></g>'
    g.append(land(you, .25, .55, 14) + land(her, .35, .55, 14))
    # speech both ways: by turns, then together
    both = (.74, .97)
    g.append(_v20_waves(1052, 506, 1, [(.02, .12), (.24, .34), (.46, .56), both]))
    g.append(_v20_waves(1328, 506, -1, [(.13, .23), (.35, .45), (.57, .67), both]))
    # the Thursday table of slide 1
    table = (f'<path d="M850 668 H1560 V752 H840 Z" fill="color-mix(in srgb, var(--c1) 14%, var(--ink))"/>'
             f'<path d="M850 668 H1560" stroke="var(--c2)" stroke-width="1.5" opacity=".6"/>')
    g.append(land(table, .1, .5, 0))
    # her three worries of slide 4 check in, softly, on the table
    size, gap = 17, 20
    ws = [bold_width(_(str(w)), fit(w, size, 220, "lema worry", floor=15), current_factor()) + 62 for w in sl["worries"]]
    x = 1200 - (sum(ws) + gap * (len(ws) - 1)) / 2
    chips = []
    for k, (w, text) in enumerate(zip(ws, sl["worries"])):
        a, cy = .18 + k * .22, 710
        s = fit(text, size, 220, "lema worry", floor=15)
        chips.append(card(x, cy - 20, w, 40, "var(--card)", "var(--line)", 20, 1.2)
                     + f'<circle cx="{x + 21}" cy="{cy}" r="11" fill="none" stroke="var(--muted)" stroke-width="1.5"/>'
                     + T(x + 40, cy + s * .36, text, s, "var(--white)", W6)
                     + f'<g>{_n01_on(a, 1, .05)}<rect x="{x:.1f}" y="{cy - 20}" width="{w:.1f}" height="40" rx="20" fill="none" stroke="{ok}" stroke-width="1.8"/>'
                     f'<circle cx="{x + 21:.1f}" cy="{cy}" r="11" fill="{ok}"/>' + check(x + 21, cy + .5, .5, "var(--ink)") + '</g>')
        x += w + gap
    g.append(seq(chips, .6, .45, 10, 1.4))
    # the signature, in the art
    sg = fit(sl["sign"], 24, 620, "lema sign", floor=15)
    sw = bold_width(_(str(sl["sign"])), sg, current_factor())
    g.append(f'<g>{_n01_on(.76, 1, .05)}' + TC(1200, 802, sl["sign"], sg, "var(--white)", W6)
             + f'<path d="M{1200 - sw / 2:.0f} 772 H{1200 + sw / 2:.0f}" stroke="var(--c4)" stroke-width="1.5" opacity=".7"/></g>')
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- portrait twins (900x1600 stage, art zone below y 640)
def _pv19_block(x, y0, y1, w, lab, fill, stroke, where):
    return (card(x + 2, y0 + 2, w - 4, y1 - y0 - 4, fill, stroke, 8, 1.4)
            + TC(x + w / 2, (y0 + y1) / 2 + 7, lab, fit(lab, 21, w - 16, where, floor=18), "var(--white)", W6))


def _pv19_tiempo(sl, ctx):
    """v19 on the phone: the same three-day week, taller hours (84 px) over the art zone; the same chores dissolve into
    the same client tasks, the thread runs to Thursday 10:00 and «Lista» lands. Same beats as desktop."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    cw, gap = 242, 10
    x0 = zx + zw - 3 * cw - 2 * gap
    xs = [x0 + k * (cw + gap) for k in range(3)]
    Y = lambda h: zy + 116 + (h - 9) * 82
    g = [glow(zx + zw / 2, zy + 460, 460, "var(--brand)", .5)]
    grid = "".join(f'<path d="M{x0} {Y(h)} H{zx + zw}" stroke="var(--line)" stroke-width="1"/>' for h in range(9, 19))
    grid += "".join(T(x0 - 10, Y(h) + 7, f"{h}:00", 20, "var(--muted)", 'text-anchor="end"') for h in range(9, 19))
    grid += "".join(TC(x + cw / 2, zy + 96, d, fit(d, 24, cw - 12, "tiempo day", floor=18), "var(--white)", W6) for x, d in zip(xs, sl["days"]))
    g.append(land(grid, .1, .5, 0))
    cx, cy = zx + 34, zy + 40
    clock = (f'<circle cx="{cx}" cy="{cy}" r="30" fill="var(--card)" stroke="var(--c2)" stroke-width="1.8"/>'
             f'<path d="M{cx} {cy} L{cx + 12.1:.1f} {cy + 7:.1f}" stroke="var(--white)" stroke-width="3" stroke-linecap="round"/>'
             f'<path d="M{cx} {cy} V{cy - 20}" stroke="var(--white)" stroke-width="2" stroke-linecap="round"/>'
             f'<circle cx="{cx}" cy="{cy}" r="2.5" fill="var(--c5)"/>')
    g.append(land(clock, .2, .45, 0))
    ny = Y(16)
    past = (f'<rect x="{xs[0]}" y="{Y(9) + 2}" width="{cw}" height="{ny - Y(9) - 4}" rx="10" fill="{_V19_GREY}" opacity=".7"/>'
            + TC(xs[0] + cw / 2, (Y(9) + ny) / 2 - 20, sl["past"], 22, "var(--muted)", W6))
    now = (f'<path d="M{xs[0] + 4} {ny} H{xs[0] + cw}" stroke="var(--c5)" stroke-width="2.4"/>'
           f'<circle cx="{xs[0] + 8}" cy="{ny}" r="6" fill="var(--c5)"/>'
           + pill(xs[0] + cw / 2, ny - 30, sl["now"], "var(--c5)", ctx, 21, cw - 8, "tiempo now", 14))
    g.append(land(past, .3, .5, 0) + land(now, .5, .45, -10))
    blocks = []
    for day, h0, h1, lab in sl["busy"]:
        x, y0, y1 = xs[day], Y(h0), Y(h1)
        body = (TCW(x + cw / 2, (y0 + y1) / 2 - 5, lab, 17, 21, "var(--white)", W6, 1.2) if y1 - y0 >= 120
                else TC(x + cw / 2, (y0 + y1) / 2 + 7, lab, fit(lab, 21, cw - 20, "tiempo busy", floor=18), "var(--white)", W6))
        blocks.append(card(x + 2, y0 + 2, cw - 4, y1 - y0 - 4, "color-mix(in srgb, var(--c2) 20%, var(--ink))", "var(--line)", 8, 1.2) + body)
    g.append(seq(blocks, .35, .45, 10, 1.5))
    mx, my0, my1 = xs[2], Y(10), Y(10.5)
    meet = (f'<rect x="{mx - 6}" y="{my0 - 6}" width="{cw + 12}" height="{my1 - my0 + 12}" rx="12" fill="var(--c4)" opacity=".2">'
            f'{loop("opacity", ".08;.35;.08", 2.2)}</rect>'
            + card(mx + 2, my0 + 2, cw - 4, my1 - my0 - 4, "var(--c4)", "var(--c4)", 7, 0)
            + TC(mx + cw / 2, my0 + 29, sl["meet_time"], 21, ctx.brand.on("var(--c4)"), W6)
            + TCW(mx + cw / 2, my1 + 34, sl["meet"], 19, 21, "var(--c4)", W6, 1.25))
    g.append(land(meet, .7, .5, 0))
    fd, f0, f1 = sl["free"]
    fx, fy0, fy1 = xs[fd], Y(f0), Y(f1)
    frame = (f'<rect x="{fx + 1}" y="{fy0 + 1}" width="{cw - 2}" height="{fy1 - fy0 - 2}" rx="9" fill="none" stroke="var(--c4)" '
             f'stroke-width="2.4" stroke-dasharray="7 6">{loop("stroke-dashoffset", "0;-26", 1.4)}</rect>'
             + TCW(fx + cw / 2, fy0 - 38, sl["prep"], 16, 20, "var(--c4)", W6, 1.15))
    g.append(land(frame, .9, .45, 0))
    n = len(sl["before"])
    hh = (fy1 - fy0) / n
    shows = [.20 + k * .14 for k in range(n)]
    olds, news = [], []
    for k, (old, new) in enumerate(zip(sl["before"], sl["after"])):
        y0, y1, a = fy0 + k * hh, fy0 + (k + 1) * hh, shows[k]
        crumbs = "".join(f'<rect x="{fx + cw / 2 + dx - 5}" y="{(y0 + y1) / 2 - 5:.1f}" width="10" height="10" rx="2" fill="none" stroke="var(--muted)" stroke-width="1.4" opacity="0">'
                         + beat("opacity", [(0, 0), (a, 0), (a + .01, .9), (a + .07, 0), (1, 0)])
                         + _n01_tr([(0, "0 0"), (a, "0 0"), (a + .07, f"{dx * .9:.0f} {-30 - abs(dx) * .3:.0f}"), (1, f"{dx * .9:.0f} {-30 - abs(dx) * .3:.0f}")])
                         + '</rect>' for dx in (-70, -28, 18, 60))
        olds.append(f'<g>{_v19_off(a)}' + _pv19_block(fx, y0, y1, cw, old, _V19_GREY, "var(--line)", "tiempo before") + '</g>' + crumbs)
        news.append(f'<g>{_n01_on(a + .03, 1, .03)}'
                    + _pv19_block(fx, y0, y1, cw, new, "color-mix(in srgb, var(--c4) 24%, var(--ink))", "var(--c4)", "tiempo after") + '</g>')
    g.append(land("".join(olds), 1.0, .45, 0) + "".join(news))
    lx, ly = mx + cw / 2, Y(12.6)
    t0 = shows[-1] + .09
    thread = f"M{fx + cw - 2} {(fy0 + fy1) / 2:.0f} C{mx + 90} {(fy0 + fy1) / 2:.0f} {lx} {ly + 200} {lx} {ly + 34}"
    g.append(f'<g>{_n01_on(t0)}<path d="{thread}" fill="none" stroke="var(--c4)" stroke-width="2" stroke-dasharray="3 6" opacity=".9"/>'
             f'<path d="M{lx - 8} {ly + 46} L{lx} {ly + 34} L{lx + 8} {ly + 46}" fill="none" stroke="var(--c4)" stroke-width="2.2" stroke-linecap="round"/></g>')
    g.append(f'<g>{_n01_on(t0, t0 + .08, .01)}{token("var(--c4)", 7)}{move(thread, [(0, 0), (t0, 0), (t0 + .08, 1), (1, 1)], D)}</g>')
    t1 = t0 + .08
    rs = fit(sl["ready"], 24, 150, "tiempo ready", floor=18)
    rw = bold_width(_(str(sl["ready"])), rs, current_factor()) + 76
    ready = (card(lx - rw / 2, ly - 23, rw, 46, ok, ok, 23, 0)
             + f'<circle cx="{lx - rw / 2 + 24}" cy="{ly}" r="14" fill="var(--ink)"/>' + check(lx - rw / 2 + 24, ly + .5, .65, ok)
             + T(lx - rw / 2 + 48, ly + rs * .36, sl["ready"], rs, ctx.brand.on(ok), W6))
    g.append(f'<g>{_n01_on(t1, 1, .03)}<rect x="{mx - 4}" y="{zy + 64}" width="{cw + 8}" height="{Y(18) - zy - 60}" rx="14" fill="var(--c4)" '
             f'fill-opacity=".05" stroke="var(--c4)" stroke-width="2.4"/>'
             + TC(mx + cw / 2, zy + 96, sl["days"][2], fit(sl["days"][2], 24, cw - 12, "tiempo day", floor=18), "var(--c4)", W6) + ready + '</g>')
    return portrait_mark("".join(g)), D, FREEZE


def _pv20_lema(sl, ctx):
    """v20 stacked: the lit cover on the screen on top, you and the manager face to face under it, the table with her
    three worries checking in, the signature at the bottom. Same beats as desktop."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    cx = zx + zw / 2
    g = [glow(cx, zy + 300, 480, "var(--brand)", .55)]
    X, Y, W_, H_ = zx + 70, zy + 30, zw - 140, 360
    cover = (card(X - 16, Y - 16, W_ + 32, H_ + 32, "var(--dim)", "var(--line)", 20, 1.2)
             + card(X, Y, W_, H_, "var(--card)", "var(--c2)", 14, 1.6)
             + f'<rect x="{X - 3}" y="{Y - 3}" width="{W_ + 6}" height="{H_ + 6}" rx="17" fill="none" stroke="var(--c4)" stroke-width="2.4">'
             f'{loop("stroke-opacity", ".45;1;.45", 2.6)}</rect>'
             + T(X + 30, Y + 52, sl["for_whom"], fit(sl["for_whom"], 22, W_ - 130, "lema cover for", floor=18), "var(--c4)", W6)
             + TCW(X + 30, Y + 116, sl["promise"], 30, 32, "var(--white)", W6, 1.2, "start")
             + T(X + 30, Y + 220, sl["cover_sub"], fit(sl["cover_sub"], 22, W_ - 60, "lema cover sub", floor=18), "var(--muted)")
             + f'<rect x="{X + W_ - 80}" y="{Y + 20}" width="54" height="54" rx="14" fill="var(--c3)"/>'
             f'<path d="M{X + W_ - 66} {Y + 60} Q{X + W_ - 53} {Y + 30} {X + W_ - 40} {Y + 60}" fill="none" stroke="var(--ink)" stroke-width="3.4" stroke-linecap="round"/>')
    ms = fit(sl["meeting"], 22, W_ - 100, "lema meeting", floor=18)
    pw = bold_width(_(str(sl["meeting"])), ms, current_factor()) + 36
    cover += pill(X + 30 + pw / 2, Y + H_ - 52, sl["meeting"], "var(--c4)", ctx, 22, W_ - 60, "lema meeting")
    g.append(land(cover, .1, .55, 0))
    py = zy + 560
    g.append(f'<g>{loop("opacity", ".35;1;.35", 4)}{glow(cx, py - 40, 130, "var(--c4)", .22)}</g>')
    you = f'<g>{bob(0, 2, 4.6)}<g transform="translate({cx - 210} {py}) scale(2.2)">{_v20_you(SKIN_LIGHT, "var(--c2)", HAIR)}</g></g>'
    her = f'<g>{bob(0, 2, 4.4, 1.3)}<g transform="translate({cx + 210} {py}) scale(-2.2 2.2)">{_n10_bust(SKIN_BROWN, "var(--c1)", HAIR, "long")}</g></g>'
    g.append(land(you, .25, .55, 14) + land(her, .35, .55, 14))
    both = (.74, .97)
    g.append(_v20_waves(cx - 148, py - 42, 1, [(.02, .12), (.24, .34), (.46, .56), both]))
    g.append(_v20_waves(cx + 128, py - 42, -1, [(.13, .23), (.35, .45), (.57, .67), both]))
    ty = py + 136
    table = (f'<path d="M{zx + 10} {ty} H{zx + zw - 10} V{ty + 104} H{zx} Z" fill="color-mix(in srgb, var(--c1) 14%, var(--ink))"/>'
             f'<path d="M{zx + 10} {ty} H{zx + zw - 10}" stroke="var(--c2)" stroke-width="1.5" opacity=".6"/>')
    g.append(land(table, .1, .5, 0))
    size, gap = 22, 18
    sizes = [fit(w, size, 280, "lema worry", floor=18) for w in sl["worries"]]
    ws = [bold_width(_(str(w)), s, current_factor()) + 72 for w, s in zip(sl["worries"], sizes)]
    x = cx - (sum(ws) + gap * (len(ws) - 1)) / 2
    chips, cy = [], ty + 52
    for k, (w, text, s) in enumerate(zip(ws, sl["worries"], sizes)):
        a = .18 + k * .22
        chips.append(card(x, cy - 25, w, 50, "var(--card)", "var(--line)", 25, 1.4)
                     + f'<circle cx="{x + 26}" cy="{cy}" r="14" fill="none" stroke="var(--muted)" stroke-width="1.6"/>'
                     + T(x + 50, cy + s * .36, text, s, "var(--white)", W6)
                     + f'<g>{_n01_on(a, 1, .05)}<rect x="{x:.1f}" y="{cy - 25}" width="{w:.1f}" height="50" rx="25" fill="none" stroke="{ok}" stroke-width="2"/>'
                     f'<circle cx="{x + 26:.1f}" cy="{cy}" r="14" fill="{ok}"/>' + check(x + 26, cy + .5, .65, "var(--ink)") + '</g>')
        x += w + gap
    g.append(seq(chips, .6, .45, 10, 1.4))
    sg = fit(sl["sign"], 32, zw - 40, "lema sign", floor=18)
    sw = bold_width(_(str(sl["sign"])), sg, current_factor())
    g.append(f'<g>{_n01_on(.76, 1, .05)}' + TC(cx, zy + 860, sl["sign"], sg, "var(--white)", W6)
             + f'<path d="M{cx - sw / 2:.0f} {zy + 822} H{cx + sw / 2:.0f}" stroke="var(--c4)" stroke-width="1.8" opacity=".7"/></g>')
    return portrait_mark("".join(g)), D, FREEZE

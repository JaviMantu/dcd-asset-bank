"""Bench a: slides 1-3 of the class «Presentaciones de prospección de alto impacto». Three loops, one arc.
v01_portada   - the template deck steps back; a cover for one prospect builds in front (their promise, the Thursday
                meeting) and the manager across the table leans in.
v02_martes    - the week from Tuesday 4 pm: mails and other meetings fill the calendar, two hours stay free
                («Para preparar») and Thursday 10:00, the prospect meeting, glows.
v03_plantilla - one line in the chat returns ten generic titles; what fits any consultancy gets underlined, the figure
                gets «¿fuente?» and the logo gets covered: «¿De quién es?»."""


def _v01_on(a, b=1.0, f=.02):
    """Opacity 1 between fractions a and b of the loop; b >= .97 holds until the loop resets."""
    if b >= .97:
        return beat("opacity", [(0, 0), (a, 0), (a + f, 1), (.97, 1), (1, 0)])
    return beat("opacity", [(0, 0), (a, 0), (a + f, 1), (b, 1), (b + f, 0), (1, 0)])


def _v01_tr(pairs, typ="translate"):
    """An animateTransform loop with explicit times: pairs = [(fraction, value)] from 0 to 1."""
    kt = ";".join(f"{t:.3f}" for t, _ in pairs)
    return (f'<animateTransform attributeName="transform" type="{typ}" values="{";".join(v for _, v in pairs)}" '
            f'keyTimes="{kt}" dur="{D}s" repeatCount="indefinite"/>')


_V01_GREY = "color-mix(in srgb, var(--white) 14%, var(--ink))"


# ---------------------------------------------------------------- slide 1: the cover made for one prospect
@register("scene", "v01_portada")
def sc_v01_portada(sl, ctx):
    """A generic template deck (grey, «Quiénes somos», «Líderes en tecnología», an empty logo hole) stands on the
    table, then fades back; in front a cover builds for one prospect: who it is for, their promise, their logo, the
    Thursday meeting. The manager across the table, faceless, leans in. Frozen frame: the tailored cover lit, the
    template dim behind, the manager leaning in."""
    if ORIENT() == "portrait":
        return _pv01_portada(sl, ctx)
    g = [glow(1150, 420, 470, "var(--brand)", .55)]
    X, Y, W_, H_ = 880, 250, 420, 300
    # the manager across the table (reused faceless bust, mirrored to face the cover); leans in at .44-.52
    lean = _v01_tr([(0, "0 1450 650"), (.32, "0 1450 650"), (.40, "-7 1450 650"), (.97, "-7 1450 650"), (1, "0 1450 650")], "rotate")
    man = (f'<g>{lean}<g>{bob(0, 2, 4.4)}<g transform="translate(1440 526) scale(-2.2 2.2)">'
           f'{_n10_bust(SKIN_BROWN, "var(--c1)", HAIR, "long")}</g></g></g>')
    g.append(land(man, .25, .6, 14))
    # the table and the screen stand
    table = (f'<path d="M850 650 H1560 V800 H840 Z" fill="color-mix(in srgb, var(--c1) 14%, var(--ink))"/>'
             f'<path d="M850 650 H1560" stroke="var(--c2)" stroke-width="1.5" opacity=".6"/>'
             f'<path d="M{X + W_ / 2} {Y + H_} V650 M{X + W_ / 2 - 60} 650 H{X + W_ / 2 + 60}" stroke="var(--c2)" stroke-width="2" stroke-linecap="round" opacity=".7"/>')
    g.append(land(table, .1, .5, 0))
    # the template: in front at the start of the loop, then it steps back and dims (.04-.10)
    grey_t = "color-mix(in srgb, var(--white) 55%, var(--ink))"
    txt_t = "color-mix(in srgb, var(--white) 72%, var(--ink))"
    tpl_bg = (card(0, 0, W_, H_, _V01_GREY, "var(--line)", 14, 1.2)
              + f'<rect x="298" y="22" width="98" height="52" rx="8" fill="none" stroke="{grey_t}" stroke-width="1.5" stroke-dasharray="5 5"/>'
              + bars(28, 130, 364, 4, 22, grey_t, ".45")
              + "".join(f'<rect x="{28 + k * 124}" y="{226}" width="108" height="48" rx="8" fill="none" stroke="{grey_t}" stroke-width="1.2" opacity=".6"/>' for k in range(3)))
    tpl_tx = (T(28, 58, sl["tpl_title"], fit(sl["tpl_title"], 26, 250, "portada template title"), txt_t, W6)
              + T(28, 94, sl["tpl_line"], fit(sl["tpl_line"], 19, 250, "portada template line"), txt_t)
              + TC(347, 54, sl["tpl_logo"], 15, txt_t, W6))
    back = _v01_tr([(0, "0 0"), (.03, "0 0"), (.08, "-40 -150"), (.97, "-40 -150"), (1, "0 0")])
    shrink = _v01_tr([(0, "1"), (.03, "1"), (.08, ".86"), (.97, ".86"), (1, "1")], "scale")
    dim = beat("opacity", [(0, 1), (.03, 1), (.08, .42), (.97, .42), (1, 1)])
    g.append(land(f'<g transform="translate({X} {Y})"><g>{back}<g>{shrink}<g>{dim}{tpl_bg}</g>{tpl_tx}</g></g></g>', .1, .5, 0))
    # the cover for one prospect builds in front
    ok_lit = (f'<rect x="{X - 3}" y="{Y - 3}" width="{W_ + 6}" height="{H_ + 6}" rx="17" fill="none" stroke="var(--c4)" stroke-width="2">'
              f'{loop("stroke-opacity", ".45;1;.45", 2.6)}</rect>')
    cover = [(.06, card(X, Y, W_, H_, "var(--card)", "var(--c2)", 14, 1.5)),
             (.09, T(X + 26, Y + 44, sl["for_whom"], fit(sl["for_whom"], 17, 300, "portada cover for"), "var(--c4)", W6)),
             (.12, TCW(X + 26, Y + 100, sl["promise"], 24, 26, "var(--white)", W6, 1.2, "start")),
             (.17, T(X + 26, Y + 186, sl["cover_sub"], fit(sl["cover_sub"], 18, 370, "portada cover sub"), "var(--muted)")),
             (.17, f'<rect x="{X + W_ - 70}" y="{Y + 18}" width="46" height="46" rx="12" fill="var(--c3)"/>'
                   f'<path d="M{X + W_ - 58} {Y + 52} Q{X + W_ - 47} {Y + 26} {X + W_ - 36} {Y + 52}" fill="none" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/>'),
             (.40, ok_lit)]
    for t, part in cover:
        g.append(f'<g>{_v01_on(t, 1, .03)}{part}</g>')
    meet = sl["meeting"]
    s = fit(meet, 17, 300, "portada meeting")
    pw = bold_width(_(str(meet)), s, current_factor()) + 36
    g.append(f'<g>{_v01_on(.24, 1, .03)}' + pill(X + 26 + pw / 2, Y + H_ - 50, meet, "var(--c4)", ctx, 17, 336, "portada meeting") + '</g>')
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- slide 2: the week from Tuesday 4 pm
def _v02_y(h):
    return 200 + (h - 9) * 62


@register("scene", "v02_martes")
def sc_v02_martes(sl, ctx):
    """The manager's week, Tuesday to Thursday, 9:00 to 18:00. Tuesday before 4 pm is gone; a clock ticks. Mails, a
    meeting with another client, lunch and a call fill the slots one by one; two hours stay free on Wednesday and get
    marked «Para preparar»; a thread runs from them to Thursday 10:00, the prospect meeting that glows from the start.
    Frozen frame: the week full, the two hours marked, Thursday highlighted."""
    if ORIENT() == "portrait":
        return _pv02_martes(sl, ctx)
    xs, cw = [900, 1118, 1336], 206
    g = [glow(1220, 450, 460, "var(--brand)", .5)]
    # grid: day headers, hour labels, hour lines
    grid = "".join(f'<path d="M900 {_v02_y(h)} H1542" stroke="var(--line)" stroke-width="1"/>' for h in range(9, 19))
    grid += "".join(T(886, _v02_y(h) + 5, f"{h}:00", 15, "var(--muted)", 'text-anchor="end"') for h in range(9, 19))
    grid += "".join(TC(x + cw / 2, 182, d, fit(d, 19, cw - 12, "martes day"), "var(--white)", W6) for x, d in zip(xs, sl["days"]))
    g.append(land(grid, .1, .5, 0))
    # the clock ticks once a second at 4:00
    cx, cy = 852, 146
    tick = (f'<animateTransform attributeName="transform" type="rotate" values="{";".join(f"{k * 30} {cx} {cy}" for k in range(12))}" '
            f'keyTimes="{";".join(f"{k / 12:.4f}" for k in range(12))}" dur="12s" repeatCount="indefinite" calcMode="discrete"/>')
    clock = (f'<circle cx="{cx}" cy="{cy}" r="28" fill="var(--card)" stroke="var(--c2)" stroke-width="1.6"/>'
             + "".join(f'<circle cx="{cx + 22 * math.sin(math.radians(a)):.1f}" cy="{cy - 22 * math.cos(math.radians(a)):.1f}" r="1.4" fill="var(--c2)"/>' for a in range(0, 360, 90))
             + f'<path d="M{cx} {cy} L{cx + 13 * math.sin(math.radians(120)):.1f} {cy - 13 * math.cos(math.radians(120)):.1f}" stroke="var(--white)" stroke-width="3" stroke-linecap="round"/>'
             + f'<path d="M{cx} {cy} V{cy - 19}" stroke="var(--white)" stroke-width="2" stroke-linecap="round"/>'
             + f'<g>{tick}<path d="M{cx} {cy + 4} V{cy - 22}" stroke="var(--c5)" stroke-width="1.4" stroke-linecap="round"/></g>'
             + f'<circle cx="{cx}" cy="{cy}" r="2.5" fill="var(--c5)"/>')
    g.append(pop(f'<g transform="translate({-cx} {-cy})">{clock}</g>', cx, cy, .2, .45))
    # Tuesday before 4 pm is gone; the now line
    ny = _v02_y(16)
    past = (f'<rect x="{xs[0]}" y="{_v02_y(9) + 2}" width="{cw}" height="{ny - _v02_y(9) - 4}" rx="10" fill="{_V01_GREY}" opacity=".7"/>'
            + TC(xs[0] + cw / 2, (_v02_y(9) + ny) / 2 - 20, sl["past"], 16, "var(--muted)", W6))
    now = (f'<path d="M{xs[0] - 6} {ny} H{xs[0] + cw}" stroke="var(--c5)" stroke-width="2"/>'
           f'<circle cx="{xs[0] - 6}" cy="{ny}" r="5" fill="var(--c5)"/>'
           + pill(xs[0] + cw / 2, ny - 26, sl["now"], "var(--c5)", ctx, 16, cw - 10, "martes now", 14))
    g.append(land(past, .3, .5, 0) + land(now, .5, .45, -10))
    # Thursday 10:00: the prospect meeting glows from the start
    mx, my0, my1 = xs[2], _v02_y(10), _v02_y(10.5)
    meet = (f'<rect x="{mx - 6}" y="{my0 - 6}" width="{cw + 12}" height="{my1 - my0 + 12}" rx="12" fill="var(--c4)" opacity=".2">'
            f'{loop("opacity", ".08;.35;.08", 2.2)}</rect>'
            + card(mx + 2, my0 + 2, cw - 4, my1 - my0 - 4, "var(--c4)", "var(--c4)", 7, 0)
            + TC(mx + cw / 2, my0 + 21, sl["meet_time"], 16, ctx.brand.on("var(--c4)"), W6)
            + TCW(mx + cw / 2, my1 + 30, sl["meet"], 20, 17, "var(--c4)", W6, 1.25))
    g.append(land(meet, .7, .5, 0))
    # the week fills, block by block
    for k, (day, h0, h1, lab) in enumerate(sl["busy"]):
        x, y0, y1 = xs[day], _v02_y(h0), _v02_y(h1)
        t = .06 + k * .05
        n_lines = 1 if (y1 - y0) < 70 else 2
        blk = (card(x + 2, y0 + 2, cw - 4, y1 - y0 - 4, "color-mix(in srgb, var(--c2) 20%, var(--ink))", "var(--line)", 8, 1.2)
               + (TCW(x + cw / 2, (y0 + y1) / 2 - 4, lab, 20, 16, "var(--white)", W6, 1.2) if n_lines == 2
                  else TC(x + cw / 2, (y0 + y1) / 2 + 6, lab, fit(lab, 16, cw - 24, "martes block"), "var(--white)", W6)))
        g.append(f'<g>{_v01_on(t, 1, .025)}<g>{_v01_tr([(0, "0 -24"), (t, "0 -24"), (t + .03, "0 0"), (1, "0 0")])}{blk}</g></g>')
    # the two free hours: dashed, then marked «Para preparar»
    fd, f0, f1 = sl["free"]
    fx, fy0, fy1 = xs[fd], _v02_y(f0), _v02_y(f1)
    g.append(f'<g>{_v01_on(.44)}<rect x="{fx + 2}" y="{fy0 + 2}" width="{cw - 4}" height="{fy1 - fy0 - 4}" rx="8" fill="none" '
             f'stroke="var(--c4)" stroke-width="2" stroke-dasharray="7 6">{loop("stroke-dashoffset", "0;-26", 1.4)}</rect></g>')
    g.append(f'<g>{_v01_on(.52)}<rect x="{fx + 2}" y="{fy0 + 2}" width="{cw - 4}" height="{fy1 - fy0 - 4}" rx="8" fill="var(--c4)" opacity=".14"/>'
             + TC(fx + cw / 2, (fy0 + fy1) / 2 - 4, sl["prep"], fit(sl["prep"], 19, cw - 24, "martes prep"), "var(--c4)", W6)
             + TC(fx + cw / 2, (fy0 + fy1) / 2 + 22, sl["prep_hours"], 16, "var(--white)", W6) + '</g>')
    # from the free hours to Thursday: the thread, then Thursday lights up
    thread = f"M{fx + cw - 2} {(fy0 + fy1) / 2:.0f} C{mx + 70} {(fy0 + fy1) / 2:.0f} {mx + cw / 2} {my1 + 180} {mx + cw / 2} {my1 + 64}"
    g.append(f'<g>{_v01_on(.60)}<path d="{thread}" fill="none" stroke="var(--c4)" stroke-width="1.6" stroke-dasharray="3 6" opacity=".9"/>'
             f'<path d="M{mx + cw / 2 - 7} {my1 + 74} L{mx + cw / 2} {my1 + 64} L{mx + cw / 2 + 7} {my1 + 74}" fill="none" stroke="var(--c4)" stroke-width="1.8" stroke-linecap="round"/></g>')
    g.append(f'<g>{_v01_on(.60, .68, .01)}{token("var(--c4)", 6)}{move(thread, [(0, 0), (.60, 0), (.68, 1), (1, 1)], D)}</g>')
    g.append(f'<g>{_v01_on(.68)}<rect x="{mx - 4}" y="152" width="{cw + 8}" height="{_v02_y(18) - 150}" rx="14" fill="var(--c4)" fill-opacity=".05" '
             f'stroke="var(--c4)" stroke-width="2"/>' + TC(mx + cw / 2, 182, sl["days"][2], fit(sl["days"][2], 19, cw - 12, "martes day"), "var(--c4)", W6) + '</g>')
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- slide 3: the deck anyone could sign
def _v03_under(x, y, title, mark, size, t, color="var(--c5)"):
    """A stroke that draws itself under `mark` inside `title` (drawn at x, baseline y, bold) at fraction t, and holds."""
    tt, mm = _(str(title)), _(str(mark))
    i = tt.find(mm)
    if i < 0:
        i, mm = 0, tt
    f = current_factor()
    x0 = x + bold_width(tt[:i], size, f)
    x1 = x0 + bold_width(mm, size, f)
    return (f'<path d="M{x0:.1f} {y + 7} H{x1:.1f}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round">'
            + beat("stroke-dashoffset", [(0, 1), (t, 1), (t + .05, 0), (.97, 0), (1, 1)]) + '</path>')


def _v03_tag(cx, cy, text):
    """A light red tag (ink text, AA) centered at (cx, cy), as wide as its text."""
    ts = fit(text, 16, 112, "plantilla nosource")
    w = bold_width(_(str(text)), ts, current_factor()) + 28
    return (card(cx - w / 2, cy - 18, w, 36, "color-mix(in srgb, var(--c5) 45%, var(--white))", "var(--c5)", 18, 1.5)
            + TC(f"{cx:.1f}", f"{cy + ts * .36:.1f}", text, ts, "var(--ink)", W6))


@register("scene", "v03_plantilla")
def sc_v03_plantilla(sl, ctx):
    """One line in the chat: «Hazme una presentación de Amaris». Ten slides answer, each with a title any consultancy
    could sign. The phrases that fit anyone get underlined one by one («Líderes», «Soluciones integrales», «valor»,
    «Innovación y excelencia»); the figure with no source gets «¿fuente?»; last, the logo gets covered: «¿De quién es?».
    Frozen frame: every generic phrase underlined, the figure tagged, the logo covered."""
    if ORIENT() == "portrait":
        return _pv03_plantilla(sl, ctx)
    g = [glow(1190, 470, 470, "var(--brand)", .5)]
    req = sl["request"]
    bw = min(620, bold_width(_(str(req)), 19, current_factor()) + 90)
    g.append(land(bubble(1530 - bw, 100, bw, req, ctx, "var(--c1)", 19, "plantilla request"), .1, .45, -12))
    xs, w, h = [850, 1200], 330, 100
    ys = [186 + r * 120 for r in range(5)]
    grey_t = "color-mix(in srgb, var(--white) 78%, var(--ink))"
    frames, titles, marks = [], [], []
    for k, item in enumerate(sl["generic"][:10]):
        x, y = xs[k % 2], ys[k // 2]
        frames.append(card(x, y, w, h, _V01_GREY, "var(--line)", 10, 1.2)
                      + T(x + w - 16, y + h - 14, str(k + 1), 15, "var(--muted)", 'text-anchor="end"'))
        ts = fit(item["t"], 19, 290 if k else 200, "plantilla title")
        tx, ty = x + 20, y + 42
        titles.append(f'<g>{_v01_on(.02 + k * .012, 1, .02)}' + T(tx, ty, item["t"], ts, "var(--white)", W6)
                      + bars(tx, y + 62, 220, 2, 14, grey_t, ".35") + '</g>')
        if item.get("u"):
            marks.append(_v03_under(tx, ty, item["t"], item["u"], ts, item["at"]))
        if item.get("logo"):
            frames[-1] += (f'<rect x="{x + w - 118}" y="{y + 14}" width="92" height="44" rx="7" fill="none" stroke="{grey_t}" stroke-width="1.5" stroke-dasharray="5 5"/>'
                           + f'<g>{beat("opacity", [(0, 1), (item["at"], 1), (item["at"] + .02, 0), (.97, 0), (1, 1)])}'
                           + TC(x + w - 72, y + 42, item["logo"], 15, grey_t, W6) + '</g>')
            ws = fit(sl["whose"], 17, 116, "plantilla whose")
            cover = (card(-66, -30, 132, 60, "var(--c4)", "var(--c4)", 6, 0)
                     + TC(0, ws * .36, sl["whose"], ws, ctx.brand.on("var(--c4)"), W6))
            marks.append(f'<g>{_v01_on(item["at"], 1, .03)}<g transform="translate({x + w - 72} {y + 36}) rotate(-4)">{cover}</g></g>')
        if item.get("fig"):
            marks.append(f'<g>{_v01_on(item["at"], 1, .03)}<g>{loop("opacity", ".8;1;.8", 2.2)}'
                         + _v03_tag(x + w - 70, y, sl["nosource"]) + '</g></g>'
                         + _v03_under(tx, ty, item["t"], item["fig"], ts, item["at"] - .04))
    g.append(seq(frames, .3, .45, 12))
    g.append("".join(titles) + "".join(marks))
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- portrait twins (the mobile build, DCD_ORIENT=portrait)
def _pv01_portada(sl, ctx):
    """v01 on the 900x1600 stage: the cover stands on the table with the manager beside it, larger labels; same beats."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    X, Y, W_, H_ = zx + 20, zy + 120, 560, 430
    tb = zy + 700                                    # the table top
    g = [glow(zx + zw / 2, zy + 360, 480, "var(--brand)", .55)]
    mx = X + W_ + 140
    lean = _v01_tr([(0, f"0 {mx} {tb}"), (.32, f"0 {mx} {tb}"), (.40, f"-7 {mx} {tb}"), (.97, f"-7 {mx} {tb}"), (1, f"0 {mx} {tb}")], "rotate")
    man = (f'<g>{lean}<g>{bob(0, 2, 4.4)}<g transform="translate({mx} {tb - 132}) scale(-2.2 2.2)">'
           f'{_n10_bust(SKIN_BROWN, "var(--c1)", HAIR, "long")}</g></g></g>')
    g.append(land(man, .25, .6, 14))
    table = (f'<path d="M{zx} {tb} H{zx + zw} V{zy + zh - 30} H{zx - 10} Z" fill="color-mix(in srgb, var(--c1) 14%, var(--ink))"/>'
             f'<path d="M{zx} {tb} H{zx + zw}" stroke="var(--c2)" stroke-width="1.5" opacity=".6"/>'
             f'<path d="M{X + W_ / 2} {Y + H_} V{tb} M{X + W_ / 2 - 70} {tb} H{X + W_ / 2 + 70}" stroke="var(--c2)" stroke-width="2" stroke-linecap="round" opacity=".7"/>')
    g.append(land(table, .1, .5, 0))
    grey_t = "color-mix(in srgb, var(--white) 55%, var(--ink))"
    txt_t = "color-mix(in srgb, var(--white) 72%, var(--ink))"
    tpl_bg = (card(0, 0, W_, H_, _V01_GREY, "var(--line)", 14, 1.2)
              + f'<rect x="{W_ - 150}" y="26" width="124" height="60" rx="8" fill="none" stroke="{grey_t}" stroke-width="1.5" stroke-dasharray="5 5"/>'
              + bars(30, 180, W_ - 60, 4, 30, grey_t, ".45")
              + "".join(f'<rect x="{30 + k * 170}" y="{320}" width="150" height="70" rx="8" fill="none" stroke="{grey_t}" stroke-width="1.2" opacity=".6"/>' for k in range(3)))
    tpl_tx = (T(30, 70, sl["tpl_title"], fit(sl["tpl_title"], 32, W_ - 200, "portada template title", floor=24), txt_t, W6)
              + T(30, 122, sl["tpl_line"], fit(sl["tpl_line"], 26, W_ - 200, "portada template line", floor=24), txt_t)
              + TC(W_ - 88, 64, sl["tpl_logo"], fit(sl["tpl_logo"], 24, 110, "portada template logo", floor=24), txt_t, W6))
    back = _v01_tr([(0, "0 0"), (.03, "0 0"), (.08, "-10 -150"), (.97, "-10 -150"), (1, "0 0")])   # both template lines stay above the cover
    shrink = _v01_tr([(0, "1"), (.03, "1"), (.08, ".86"), (.97, ".86"), (1, "1")], "scale")
    dim = beat("opacity", [(0, 1), (.03, 1), (.08, .42), (.97, .42), (1, 1)])
    g.append(land(f'<g transform="translate({X} {Y})"><g>{back}<g>{shrink}<g>{dim}{tpl_bg}</g>{tpl_tx}</g></g></g>', .1, .5, 0))
    ok_lit = (f'<rect x="{X - 3}" y="{Y - 3}" width="{W_ + 6}" height="{H_ + 6}" rx="17" fill="none" stroke="var(--c4)" stroke-width="2.4">'
              f'{loop("stroke-opacity", ".45;1;.45", 2.6)}</rect>')
    pr = sl["promise"]
    cover = [(.06, card(X, Y, W_, H_, "var(--card)", "var(--c2)", 14, 1.5)),
             (.09, T(X + 28, Y + 54, sl["for_whom"], fit(sl["for_whom"], 24, W_ - 130, "portada cover for", floor=20), "var(--c4)", W6)),
             (.12, TCW(X + 28, Y + 124, pr, _p01_chars(pr, 34, W_ - 56), 34, "var(--white)", W6, 1.2, "start")),
             (.17, T(X + 28, Y + 272, sl["cover_sub"], fit(sl["cover_sub"], 24, W_ - 56, "portada cover sub", floor=20), "var(--muted)")),
             (.17, f'<rect x="{X + W_ - 84}" y="{Y + 22}" width="58" height="58" rx="14" fill="var(--c3)"/>'
                   f'<path d="M{X + W_ - 70} {Y + 64} Q{X + W_ - 55} {Y + 32} {X + W_ - 40} {Y + 64}" fill="none" stroke="var(--ink)" stroke-width="3.5" stroke-linecap="round"/>'),
             (.40, ok_lit)]
    for t, part in cover:
        g.append(f'<g>{_v01_on(t, 1, .03)}{part}</g>')
    meet = sl["meeting"]
    s = fit(meet, 24, W_ - 80, "portada meeting", floor=20)
    pw = bold_width(_(str(meet)), s, current_factor()) + 36
    g.append(f'<g>{_v01_on(.24, 1, .03)}' + pill(X + 28 + pw / 2, Y + H_ - 60, meet, "var(--c4)", ctx, 24, W_ - 56, "portada meeting") + '</g>')
    return portrait_mark("".join(g)), D, FREEZE


def _pv02_martes(sl, ctx):
    """v02 on the 900x1600 stage: the same three days, taller hours and larger labels; same beats and frozen frame."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    cw, gap = 236, 12
    xs = [zx + zw - 3 * cw - 2 * gap + k * (cw + gap) for k in range(3)]
    y0, hh = zy + 100, 84
    Y = lambda h: y0 + (h - 9) * hh
    g = [glow(zx + zw / 2, zy + 450, 480, "var(--brand)", .5)]
    x_end = xs[2] + cw
    grid = "".join(f'<path d="M{xs[0]} {Y(h)} H{x_end}" stroke="var(--line)" stroke-width="1"/>' for h in range(9, 19))
    grid += "".join(T(xs[0] - 12, Y(h) + 7, f"{h}:00", 20, "var(--muted)", 'text-anchor="end"') for h in range(9, 19))
    hy = y0 - 26
    grid += "".join(TC(x + cw / 2, hy, d, fit(d, 26, cw - 12, "martes day", floor=20), "var(--white)", W6) for x, d in zip(xs, sl["days"]))
    g.append(land(grid, .1, .5, 0))
    cx, cy = zx + 34, zy + 40
    tick = (f'<animateTransform attributeName="transform" type="rotate" values="{";".join(f"{k * 30} {cx} {cy}" for k in range(12))}" '
            f'keyTimes="{";".join(f"{k / 12:.4f}" for k in range(12))}" dur="12s" repeatCount="indefinite" calcMode="discrete"/>')
    clock = (f'<circle cx="{cx}" cy="{cy}" r="30" fill="var(--card)" stroke="var(--c2)" stroke-width="1.6"/>'
             + "".join(f'<circle cx="{cx + 23 * math.sin(math.radians(a)):.1f}" cy="{cy - 23 * math.cos(math.radians(a)):.1f}" r="1.5" fill="var(--c2)"/>' for a in range(0, 360, 90))
             + f'<path d="M{cx} {cy} L{cx + 14 * math.sin(math.radians(120)):.1f} {cy - 14 * math.cos(math.radians(120)):.1f}" stroke="var(--white)" stroke-width="3" stroke-linecap="round"/>'
             + f'<path d="M{cx} {cy} V{cy - 20}" stroke="var(--white)" stroke-width="2" stroke-linecap="round"/>'
             + f'<g>{tick}<path d="M{cx} {cy + 4} V{cy - 23}" stroke="var(--c5)" stroke-width="1.4" stroke-linecap="round"/></g>'
             + f'<circle cx="{cx}" cy="{cy}" r="2.5" fill="var(--c5)"/>')
    g.append(pop(f'<g transform="translate({-cx} {-cy})">{clock}</g>', cx, cy, .2, .45))
    ny = Y(16)
    past = (f'<rect x="{xs[0]}" y="{Y(9) + 2}" width="{cw}" height="{ny - Y(9) - 4}" rx="10" fill="{_V01_GREY}" opacity=".7"/>'
            + TC(xs[0] + cw / 2, (Y(9) + ny) / 2 - 20, sl["past"], fit(sl["past"], 22, cw - 20, "martes past", floor=20), "var(--muted)", W6))
    now = (f'<path d="M{xs[0] - 6} {ny} H{xs[0] + cw}" stroke="var(--c5)" stroke-width="2.4"/>'
           f'<circle cx="{xs[0] - 6}" cy="{ny}" r="6" fill="var(--c5)"/>'
           + pill(xs[0] + cw / 2, ny - 30, sl["now"], "var(--c5)", ctx, 22, cw - 8, "martes now", 14))
    g.append(land(past, .3, .5, 0) + land(now, .5, .45, -10))
    mx, my0, my1 = xs[2], Y(10), Y(10.5)
    ml = sl["meet"]
    mz, mch, mn = _sm_fitwrap(ml, 22, cw - 16, 3)
    meet = (f'<rect x="{mx - 6}" y="{my0 - 6}" width="{cw + 12}" height="{my1 - my0 + 12}" rx="12" fill="var(--c4)" opacity=".2">'
            f'{loop("opacity", ".08;.35;.08", 2.2)}</rect>'
            + card(mx + 2, my0 + 2, cw - 4, my1 - my0 - 4, "var(--c4)", "var(--c4)", 7, 0)
            + TC(mx + cw / 2, my0 + 29, sl["meet_time"], 22, ctx.brand.on("var(--c4)"), W6)
            + TCW(mx + cw / 2, my1 + 34, ml, mch, mz, "var(--c4)", W6, 1.2))
    g.append(land(meet, .7, .5, 0))
    for k, (day, h0, h1, lab) in enumerate(sl["busy"]):
        x, ya, yb = xs[day], Y(h0), Y(h1)
        t = .06 + k * .05
        blk = (card(x + 2, ya + 2, cw - 4, yb - ya - 4, "color-mix(in srgb, var(--c2) 20%, var(--ink))", "var(--line)", 8, 1.2)
               + _sm_text(x + cw / 2, (ya + yb) / 2, lab, 22, cw - 24, anchor="middle", lines_max=2))
        g.append(f'<g>{_v01_on(t, 1, .025)}<g>{_v01_tr([(0, "0 -24"), (t, "0 -24"), (t + .03, "0 0"), (1, "0 0")])}{blk}</g></g>')
    fd, f0, f1 = sl["free"]
    fx, fy0, fy1 = xs[fd], Y(f0), Y(f1)
    fm = (fy0 + fy1) / 2
    g.append(f'<g>{_v01_on(.44)}<rect x="{fx + 2}" y="{fy0 + 2}" width="{cw - 4}" height="{fy1 - fy0 - 4}" rx="8" fill="none" '
             f'stroke="var(--c4)" stroke-width="2.4" stroke-dasharray="7 6">{loop("stroke-dashoffset", "0;-26", 1.4)}</rect></g>')
    g.append(f'<g>{_v01_on(.52)}<rect x="{fx + 2}" y="{fy0 + 2}" width="{cw - 4}" height="{fy1 - fy0 - 4}" rx="8" fill="var(--c4)" opacity=".14"/>'
             + TC(fx + cw / 2, fm - 6, sl["prep"], fit(sl["prep"], 24, cw - 24, "martes prep", floor=20), "var(--c4)", W6)
             + TC(fx + cw / 2, fm + 26, sl["prep_hours"], 22, "var(--white)", W6) + '</g>')
    tip = my1 + 34 + (mn - 1) * mz * 1.2 + 26
    thread = f"M{fx + cw - 2} {fm:.0f} C{mx + 80} {fm:.0f} {mx + cw / 2} {tip + 200:.0f} {mx + cw / 2} {tip:.0f}"
    g.append(f'<g>{_v01_on(.60)}<path d="{thread}" fill="none" stroke="var(--c4)" stroke-width="2" stroke-dasharray="3 6" opacity=".9"/>'
             f'<path d="M{mx + cw / 2 - 8} {tip + 11:.0f} L{mx + cw / 2} {tip:.0f} L{mx + cw / 2 + 8} {tip + 11:.0f}" fill="none" stroke="var(--c4)" stroke-width="2" stroke-linecap="round"/></g>')
    g.append(f'<g>{_v01_on(.60, .68, .01)}{token("var(--c4)", 7)}{move(thread, [(0, 0), (.60, 0), (.68, 1), (1, 1)], D)}</g>')
    g.append(f'<g>{_v01_on(.68)}<rect x="{mx - 4}" y="{hy - 34}" width="{cw + 8}" height="{Y(18) - hy + 42}" rx="14" fill="var(--c4)" fill-opacity=".05" '
             f'stroke="var(--c4)" stroke-width="2.4"/>' + TC(mx + cw / 2, hy, sl["days"][2], fit(sl["days"][2], 26, cw - 12, "martes day", floor=20), "var(--c4)", W6) + '</g>')
    return portrait_mark("".join(g)), D, FREEZE


def _pv03_tag(cx, cy, text):
    """_v03_tag at phone size: a light red tag (ink text) centered at (cx, cy)."""
    ts = fit(text, 22, 150, "plantilla nosource", floor=20)
    w = bold_width(_(str(text)), ts, current_factor()) + 32
    return (card(cx - w / 2, cy - 22, w, 44, "color-mix(in srgb, var(--c5) 45%, var(--white))", "var(--c5)", 22, 1.5)
            + TC(f"{cx:.1f}", f"{cy + ts * .36:.1f}", text, ts, "var(--ink)", W6))


def _pv03_plantilla(sl, ctx):
    """v03 on the 900x1600 stage: the request on top, the ten slides in two columns of five, larger titles; same beats."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    g = [glow(zx + zw / 2, zy + 460, 480, "var(--brand)", .5)]
    req = sl["request"]
    bw = min(zw, bold_width(_(str(req)), 22, current_factor()) + 100)
    g.append(land(bubble(zx + zw - bw, zy + 6, bw, req, ctx, "var(--c1)", 22, "plantilla request"), .1, .45, -12))
    w, h, gx = 400, 146, 20
    xs = [zx, zx + w + gx]
    ys = [zy + 88 + r * 162 for r in range(5)]
    grey_t = "color-mix(in srgb, var(--white) 78%, var(--ink))"
    frames, titles, marks = [], [], []
    for k, item in enumerate(sl["generic"][:10]):
        x, y = xs[k % 2], ys[k // 2]
        frames.append(card(x, y, w, h, _V01_GREY, "var(--line)", 10, 1.2)
                      + T(x + w - 16, y + h - 14, str(k + 1), 20, "var(--muted)", 'text-anchor="end"'))
        ts = fit(item["t"], 26, (w - 40) if not item.get("logo") else (w - 180), "plantilla title", floor=20)
        tx, ty = x + 20, y + 52
        titles.append(f'<g>{_v01_on(.02 + k * .012, 1, .02)}' + T(tx, ty, item["t"], ts, "var(--white)", W6)
                      + bars(tx, y + 82, 200, 2, 18, grey_t, ".35") + '</g>')
        if item.get("u"):
            marks.append(_v03_under(tx, ty, item["t"], item["u"], ts, item["at"]))
        if item.get("logo"):
            lx = x + w - 90
            frames[-1] += (f'<rect x="{lx - 70}" y="{y + 16}" width="140" height="60" rx="8" fill="none" stroke="{grey_t}" stroke-width="1.5" stroke-dasharray="5 5"/>'
                           + f'<g>{beat("opacity", [(0, 1), (item["at"], 1), (item["at"] + .02, 0), (.97, 0), (1, 1)])}'
                           + TC(lx, y + 54, item["logo"], 22, grey_t, W6) + '</g>')
            ws = fit(sl["whose"], 22, 156, "plantilla whose", floor=20)
            cover = (card(-86, -36, 172, 72, "var(--c4)", "var(--c4)", 8, 0)
                     + TC(0, ws * .36, sl["whose"], ws, ctx.brand.on("var(--c4)"), W6))
            marks.append(f'<g>{_v01_on(item["at"], 1, .03)}<g transform="translate({lx} {y + 46}) rotate(-4)">{cover}</g></g>')
        if item.get("fig"):
            marks.append(f'<g>{_v01_on(item["at"], 1, .03)}<g>{loop("opacity", ".8;1;.8", 2.2)}'
                         + _pv03_tag(x + w - 120, y + h - 38, sl["nosource"]) + '</g></g>'
                         + _v03_under(tx, ty, item["t"], item["fig"], ts, item["at"] - .04))
    g.append(seq(frames, .3, .45, 12))
    g.append("".join(titles) + "".join(marks))
    return portrait_mark("".join(g)), D, FREEZE

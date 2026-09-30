"""Group E of the pagos deck: slide 13 (the discovery, whose prototype is slide 14 in miniature), 14 (merchant tickets
that answer themselves: the prototype grown up) and 15 (the optional open question: energía's m15_chain with pagos args,
nothing to adapt). Runs in the shared namespace (the pagos deck's module/ext.py), so the ext.py helpers (_swap, _leg, _lock) and the
energía v4 ones (_n13_on, _n13_off, _n13_lit, _n13_ride, _N13_RESET, _n14_woman, _n14_man) are at hand without imports.
Every loop is one 12-second story timed with beat(); the reduced-motion frame (0.9 of the loop, 10.8 s) is its resolved
state."""


def _q13_doc(x, y, color="var(--c2)"):
    """A thin document icon whose baseline row is y: the source an answer comes from."""
    return (f'<path d="M{x} {y - 13} h8 l5 5 v12 h-13 Z M{x + 3} {y - 3} h7 M{x + 3} {y + 1} h7" fill="none" stroke="{color}" '
            f'stroke-width="1.3" stroke-linejoin="round"/>')


# ---------------------------------------------------------------- 13 · Empecemos con un discovery
def _pn13_chev(x, y, down=False):
    d = f"M{x - 8:.0f} {y - 9:.0f} L{x:.0f} {y:.0f} L{x + 8:.0f} {y - 9:.0f}" if down else f"M{x - 9:.0f} {y - 8:.0f} L{x:.0f} {y:.0f} L{x - 9:.0f} {y + 8:.0f}"
    return f'<path d="{d}" fill="none" stroke="var(--c2)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'


def _pn13_twin(sl, ctx):
    """discovery-b in portrait: the four steps as a 2x2 read row by row (today, this week / a week later, their call),
    redrawn at 1:1 on the 900x1600 stage so every label is 20 units or more, a time rail under each row and the hand-offs
    between the steps. Same beats (fractions of D) as the desktop story; same frozen frame."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "top")
    ok = ctx.brand.c("dark.ok")
    cols = ("var(--c1)", "var(--c3)", "var(--c2)", "var(--accent)", "var(--c4)")
    gp = 28
    w = int((zw - gp) / 2)
    Y1, h1 = zy + 8, 330
    Y2, h2 = Y1 + h1 + 90, 400
    ax, bx, cx, dx = zx, zx + w + gp, zx, zx + w + gp
    opts = sl["cards"][:5]
    n, pick = len(opts), sl.get("pick", 0)
    t_pick, starts = .217, (0, .25, .5, .75)
    ch = lambda t, s, room, where: fit(t, s, room, where, floor=20)

    # today: their options; a frame weighs each one, then settles on the one they choose
    st, oh, y0a = 66, 56, Y1 + 8
    a = "".join(card(ax, y0a + k * st, w, oh, "var(--card)", col, 14, 1.5) + f'<circle cx="{ax + 28:.0f}" cy="{y0a + 28 + k * st}" r="8" fill="{col}"/>'
                + T(f"{ax + 48:.0f}", y0a + 36 + k * st, name, ch(name, 22, w - 96, "n13 option"), "var(--white)", W6)
                for k, (name, col) in enumerate(zip(opts, cols)))
    yc = y0a + 28 + pick * st
    chosen = (f'<g opacity="0">{_n13_on(t_pick)}<rect x="{ax:.0f}" y="{y0a + pick * st}" width="{w:.0f}" height="{oh}" rx="14" fill="none" stroke="var(--c4)" stroke-width="2.5"/>'
              f'<circle cx="{ax + w - 26:.0f}" cy="{yc}" r="12" fill="{ok}"/>' + check(f"{ax + w - 26:.0f}", yc + 1, .6, "var(--ink)") + '</g>')
    order = [k for k in range(n) if k != pick] + [pick]
    hops = [.083 + i * (t_pick - .083) / (n - 1) for i in range(n)]
    scan = (f'<rect x="{ax - 5:.0f}" y="{y0a - 5}" width="{w + 10:.0f}" height="{oh + 10}" rx="17" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
            f'<animateTransform attributeName="transform" type="translate" values="0 {pick * st};{";".join(f"0 {k * st}" for k in order)}" '
            f'keyTimes="0;{";".join(f"{t:.3f}" for t in hops)}" dur="{D}s" repeatCount="indefinite" calcMode="discrete"/>'
            f'{beat("opacity", [(0, 0), (.08, 0), (.083, 1), (_N13_RESET, 1), (.985, 0), (1, 0)])}</rect>')

    # this week: the discovery workshop fills in the pain, how to solve it and the KPI, one check at a time
    wtitle, wrows = sl["workshop"]
    b = card(bx, Y1, w, h1, "var(--card)", "var(--c2)", 18, 1.5) + pill(bx + w / 2, Y1 + 40, wtitle, "var(--c2)", ctx, 22, w - 40, "n13 workshop")
    for j, (verb, text) in enumerate(wrows[:3]):
        y, t = Y1 + 104 + j * 80, .3 + j * .067
        tx, room = f"{bx + 22:.0f}", w - 44
        b += T(tx, y, verb, 20, "var(--c4)", W6) + f'<circle cx="{bx + w - 36:.0f}" cy="{y - 7}" r="14" fill="none" stroke="var(--line)" stroke-width="1.5"/>'
        if j == 0:  # the template line becomes the pain they chose
            b += (f'<g>{_n13_off(t)}' + T(tx, y + 30, text, ch(text, 21, room, "n13 workshop row"), "var(--muted)", W6) + '</g>'
                  f'<g opacity="0">{_n13_on(t)}' + T(tx, y + 30, opts[pick], ch(opts[pick], 21, room, "n13 workshop row"), "var(--white)", W6) + '</g>')
        else:
            b += f'<g>{_n13_lit(t, .6)}' + T(tx, y + 30, text, ch(text, 21, room, "n13 workshop row"), "var(--white)", W6) + '</g>'
        b += f'<g opacity="0">{_n13_on(t)}<circle cx="{bx + w - 36:.0f}" cy="{y - 7}" r="14" fill="{ok}"/>' + check(f"{bx + w - 36:.0f}", y - 6, .65, "var(--ink)") + '</g>'

    # a week later: the prototype comes alive, slide 14 in miniature (the same ticket, space, lock and source)
    live, drop, ask_a, ans_a, solved, kpi_t = .533, .55, .57, .61, .645, .69
    c = (card(cx, Y2, w, h2, "var(--card)", "var(--c3)", 18, 1.5) + f'<path d="M{cx} {Y2 + 50} H{cx + w:.0f}" stroke="var(--line)" stroke-width="1.5"/>'
         + "".join(f'<circle cx="{cx + 24 + k * 18}" cy="{Y2 + 25}" r="5" fill="var(--line)"/>' for k in range(3))
         + f'<g opacity="0">{_n13_on(live)}' + "".join(f'<circle cx="{cx + 24 + k * 18}" cy="{Y2 + 25}" r="5" fill="{col}"/>' for k, col in enumerate(("var(--c5)", "var(--c4)", ok))) + '</g>'
         + T(cx + 84, Y2 + 33, sl["proto"], ch(sl["proto"], 22, w - 220, "n13 prototype"), "var(--white)", W6)
         + f'<g opacity="0">{_n13_on(live)}' + pill(cx + w - 68, Y2 + 25, sl["live"], ok, ctx, 20, 124, "n13 live", 14) + '</g>')
    px, pw = cx + 14, w - 28
    ty, th = Y2 + 62, 74
    sdot = f"{px + pw - 18:.0f}"
    tk = (card(px, ty, pw, th, "var(--dim)", "var(--line)", 12, 1.2)
          + T(px + 14, ty + 30, sl["ticket"], ch(sl["ticket"], 21, pw - 28, "n13 ticket"), "var(--white)", W6)
          + f'<g>{_n13_off(solved, f=.01)}<circle cx="{sdot}" cy="{ty + 54}" r="6" fill="var(--c2)"/>' + T(px + 14, ty + 60, sl["new"], 20, "var(--muted)", W6) + '</g>'
          + f'<g opacity="0">{_n13_on(solved, f=.01)}<circle cx="{sdot}" cy="{ty + 54}" r="6" fill="{ok}"/>'
          + T(px + 14, ty + 60, sl["solved"], ch(sl["solved"], 20, pw - 28, "n13 status"), ok, W6) + '</g>'
          + f'<rect x="{px}" y="{ty}" width="{pw:.0f}" height="{th}" rx="12" fill="none" stroke="{ok}" stroke-width="2.5" stroke-opacity="0">'
          f'{beat("stroke-opacity", [(0, 0), (solved, 0), (solved + .01, 1), (solved + .07, 0), (1, 0)])}</rect>')
    c += (f'<g>{_n13_off(drop)}' + card(px, ty, pw, th, "none", "var(--line)", 12, 1.5, 'stroke-dasharray="6 6"') + '</g>'
          f'<g opacity="0">{_n13_on(drop)}<g><animateTransform attributeName="transform" type="translate" values="0 -14;0 -14;0 0;0 0" '
          f'keyTimes="0;{drop};{drop + .025};1" dur="{D}s" repeatCount="indefinite"/>{tk}</g></g>')
    # the restricted space the agent answers from, with its lock and its source
    qy, qh = ty + th + 12, 130
    gx, gy = px + pw - 46, qy + 88
    dy_ = qy + 96
    ds = ch(sl["doc"], 20, pw - 140, "n13 doc")
    dw_ = bold_width(_(str(sl["doc"])), ds, current_factor())
    docrow = lambda col, fg: _q13_doc(px + 14, dy_, col) + T(px + 36, dy_, sl["doc"], ds, fg, W6)
    dash = f'M{px + 44 + dw_:.0f} {dy_ - 6} H{gx - 40:.0f}'
    c += (card(px, qy, pw, qh, "var(--dim)", "var(--accent)", 14, 1.4) + _lock(px + pw - 22, qy + 24)
          + T(px + 14, qy + 32, sl["space"], ch(sl["space"], 21, pw - 60, "n13 space"), "var(--white)", W6)
          + docrow("var(--c2)", "var(--muted)") + f'<path d="{dash}" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 5"/>'
          + card(gx - 32, gy - 22, 64, 44, "var(--card)", "var(--accent)", 12, 1.4) + spark(f"{gx:.0f}", gy, .75, "var(--accent)")
          + f'<rect x="{gx - 38:.0f}" y="{gy - 28}" width="76" height="56" rx="15" fill="none" stroke="var(--c4)" stroke-width="2.5" stroke-opacity="0">'
          f'{beat("stroke-opacity", [(0, 0), (ask_a + .02, 0), (ask_a + .03, 1), (ans_a + .03, 1), (ans_a + .04, 0), (1, 0)])}</rect>'
          + f'<g opacity="0">{_n13_on(ask_a + .03)}<rect x="{px + 6}" y="{dy_ - 22}" width="{gx - 44 - px:.0f}" height="30" rx="8" fill="var(--c4)" opacity=".14"/>'
          + docrow("var(--c4)", "var(--c4)") + f'<path d="{dash}" stroke="var(--c4)" stroke-width="1.5" stroke-dasharray="3 5">{loop("stroke-dashoffset", "0;-16", 1)}</path></g>')
    leg = f"M{sdot} {ty + th} C{sdot} {ty + th + 30} {gx:.0f} {gy - 50} {gx:.0f} {gy - 24}"
    c += _n13_ride(leg, ask_a, ask_a + .035, 6) + _n13_ride(f"M{gx:.0f} {gy - 24} C{gx:.0f} {gy - 50} {sdot} {ty + th + 30} {sdot} {ty + th}", ans_a, ans_a + .035, 6)
    # the KPI of the success case, on screen once the ticket closes by itself
    ky = Y2 + h2 - 70
    c += (card(px, ky, pw, 56, "none", "var(--line)", 12, 1.5, 'stroke-dasharray="6 6"')
          + f'<g opacity="0">{_n13_on(kpi_t)}' + card(px, ky, pw, 56, "var(--dim)", ok, 12, 1.5)
          + T(px + 12, ky + 35, sl["kpi"], ch(sl["kpi"], 21, pw - 50, "n13 kpi"), "var(--white)", W6)
          + f'<circle cx="{px + pw - 22:.0f}" cy="{ky + 28}" r="13" fill="{ok}"/>' + check(f"{px + pw - 22:.0f}", ky + 29, .6, "var(--ink)") + '</g>')
    boot = (f'<g opacity="0">{beat("opacity", [(0, 0), (live, 0), (live + .03, 1), (.6, .45), (_N13_RESET, .45), (.985, 0), (1, 0)])}'
            + glow(cx + w / 2, Y2 + h2 / 2, 280, "var(--c3)", .5) + '</g>')
    c += (f'<rect x="{cx + 2}" y="{Y2 + 52}" width="{w - 4:.0f}" height="2" fill="var(--c3)" opacity="0">'
          f'{beat("opacity", [(0, 0), (live, 0), (live + .004, .8), (.585, .8), (.59, 0), (1, 0)])}'
          f'<animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 {h2 - 56};0 {h2 - 56}" keyTimes="0;{live};.585;1" dur="{D}s" repeatCount="indefinite"/></rect>')

    # then: their call, with a proposal fitted to them among the four ways to start
    ask_, ways = sl["offer"]
    dd = card(dx, Y2, w, h2, "var(--card)", ok, 18, 1.5) + T(f"{dx + 22:.0f}", Y2 + 52, ask_, ch(ask_, 24, w - 44, "n13 offer"), "var(--white)", W6)
    for j, way in enumerate(ways[:4]):
        y, t = Y2 + 112 + j * 52, .783 + j * .025
        wx = f"{dx + 32:.0f}"
        dd += (f'<circle cx="{wx}" cy="{y}" r="8" fill="none" stroke="var(--line)" stroke-width="1.5"/>'
               f'<g opacity="0">{_n13_on(t)}<circle cx="{wx}" cy="{y}" r="8" fill="{ok}"/></g>'
               f'<g>{_n13_lit(t)}' + T(f"{dx + 52:.0f}", y + 7, way, ch(way, 22, w - 76, "n13 way"), "var(--white)", W6) + '</g>')
    s = ch(sl["decide"], 21, w - 60, "n13 decision")
    qw = min(w - 24, bold_width(_(str(sl["decide"])), s, current_factor()) + 36)
    py_ = Y2 + h2 - 52
    dd += (f'<g>{_n13_off(.875)}' + card(dx + (w - qw) / 2, py_ - (s + 20) / 2, qw, s + 20, "none", "var(--line)", (s + 20) / 2, 1.5, 'stroke-dasharray="5 5"') + '</g>'
           + f'<g opacity="0">{_n13_on(.875)}' + pill(dx + w / 2, py_, sl["decide"], ok, ctx, 21, w - 24, "n13 decision") + '</g>')

    # the step on stage lights up
    boxes = ((bx, Y1, h1), (cx, Y2, h2), (dx, Y2, h2))
    frames = "".join(f'<rect x="{x - 6:.0f}" y="{y - 6}" width="{w + 12:.0f}" height="{hh + 12}" rx="22" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity="0">'
                     f'{_n13_on(t0 + .01, (t1 if t1 < 1 else _N13_RESET) - .01, .02, .75)}</rect>'
                     for (x, y, hh), t0, t1 in zip(boxes, starts[1:], starts[2:] + (1,)))
    # the hand-offs: the chosen pain to the workshop, the workshop down to the prototype, the prototype to their call
    ya1, ya2 = Y1 + h1 / 2, Y2 + h2 / 2
    link1 = f"M{ax + w + 4:.0f} {yc} C{ax + w + 18:.0f} {yc} {bx - 18:.0f} {ya1:.0f} {bx - 6:.0f} {ya1:.0f}"
    down = f"M{bx + 40:.0f} {Y1 + h1 + 6} C{bx + 40:.0f} {Y1 + h1 + 50} {cx + w - 40:.0f} {Y2 - 50} {cx + w - 40:.0f} {Y2 - 10}"
    across = f"M{cx + w + 6:.0f} {ya2:.0f} H{dx - 8:.0f}"
    dsh = lambda d: f'<path d="{d}" fill="none" stroke="var(--c2)" stroke-width="2.4" stroke-dasharray="4 7">{loop("stroke-dashoffset", "0;-22", 1.6)}</path>'
    arrows = (f'<g opacity="0">{_n13_on(t_pick)}{dsh(link1)}</g>' + dsh(down) + dsh(across)
              + _pn13_chev(bx - 4, ya1) + _pn13_chev(cx + w - 40, Y2 - 6, True) + _pn13_chev(dx - 4, ya2))
    rides = _n13_ride(link1, .222, .283, 7) + _n13_ride(down, .483, .525, 7) + _n13_ride(across, .733, .775, 7)

    # the time rail, one per row: today and this week, then a week later and their call
    reach = (0, .292, .542, .792)
    xm = [ax + w / 2, bx + w / 2, cx + w / 2, dx + w / 2]
    ry = (Y1 + h1 + 26, Y2 + h2 + 26)
    rail, now = "", ""
    for r, (k0, k1, t0) in enumerate(((0, 1, .25), (2, 3, .75))):
        d = f"M{xm[k0]:.0f} {ry[r]} H{xm[k1]:.0f}"
        rail += (f'<path d="{d}" stroke="var(--line)" stroke-width="2.4"/>'
                 f'<path d="{d}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="0" fill="none" stroke="var(--c4)" stroke-width="2.4">'
                 + beat("stroke-dashoffset", [(0, 1), (t0, 1), (reach[k1], 0), (_N13_RESET, 0), (.985, 1), (1, 1)]) + '</path>')
        op = [(0, 1), (.5, 1), (.51, 0), (.97, 0), (.985, 1), (1, 1)] if not r else [(0, 0), (reach[2], 0), (reach[2] + .01, 1), (_N13_RESET, 1), (.985, 0), (1, 0)]
        mv = [(0, 0), (t0, 0), (reach[k1], 1), (.93, 1), (.96, 0), (1, 0)] if not r else [(0, 0), (t0, 0), (reach[k1], 1), (1, 1)]
        now += f'<g opacity="{r}">{beat("opacity", op)}{move(d, mv, D)}{token("var(--c4)", 8)}</g>'
    for k, t in enumerate(sl["when"][:4]):
        y = ry[k // 2]
        rail += f'<circle cx="{xm[k]:.0f}" cy="{y}" r="8" fill="var(--card)" stroke="var(--c4)" stroke-width="1.8"/>'
        dot = f'<circle cx="{xm[k]:.0f}" cy="{y}" r="4" fill="var(--c4)"/>'
        rail += dot if not k else f'<g opacity="0">{_n13_on(reach[k])}{dot}</g>'
        lab = TC(f"{xm[k]:.0f}", y + 33, t, ch(t, 22, w, "n13 when"), "var(--c4)", W6)
        now += lab if not k else f'<g>{_n13_lit(reach[k], .5)}{lab}</g>'
    art = (seq([a, b, boot + c, dd], .1, .5, 18) + land(arrows + chosen + scan + frames, .9, .4, 0) + rides + land(rail + now, .7, .45, 0))
    return _pz_clip(art, "pn13"), D, FREEZE


@register("scene", "n13_discovery")
def sc_n13_discovery(sl, ctx):
    """energía's m13_discovery for the pagos deck, one 12-second story along a time rail. Today (0-3 s) a frame weighs their options
    and settles on one: «Atención a comercios». This week (3-6 s) the discovery workshop takes it, sees how to solve it with
    technology and agrees the KPI of the success case. A week later (6-9 s) the prototype comes alive as slide 14 in
    miniature: a merchant question drops into the queue, the governed knowledge agent answers it from its restricted space
    and its source, the ticket closes as self-served and the KPI shows. Then (9-11.6 s) they decide, with a proposal fitted
    to them among the four ways to start. Frozen frame: the pain chosen, the workshop done, the ticket self-served with its
    source lit, the KPI on screen and the proposal ready for their decision."""
    if ORIENT() == "portrait":
        return _pn13_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    cols = ("var(--c1)", "var(--c3)", "var(--c2)", "var(--accent)", "var(--c4)")
    y0, h = 420, 300
    X = ((96, 280), (416, 360), (816, 380), (1236, 268))
    (ax, aw), (bx, bw), (cx, cw), (dx, dw) = X
    opts = sl["cards"][:5]
    n, pick = len(opts), sl.get("pick", 0)
    t_pick, starts = .217, (0, .25, .5, .75)  # the frame settles at 2.6 s; the four steps start at 0, 3, 6 and 9 s

    # today: their options; a frame weighs each one, then settles on the one they choose
    a = "".join(card(ax, y0 + k * 60, aw, 50, "var(--card)", col, 14, 1.5) + f'<circle cx="{ax + 26}" cy="{y0 + 25 + k * 60}" r="7" fill="{col}"/>'
                + T(ax + 44, y0 + 31 + k * 60, name, fit(name, 17, aw - 84, "n13 option"), "var(--white)", W6)
                for k, (name, col) in enumerate(zip(opts, cols)))
    yc = y0 + 25 + pick * 60
    chosen = (f'<g opacity="0">{_n13_on(t_pick)}<rect x="{ax}" y="{y0 + pick * 60}" width="{aw}" height="50" rx="14" fill="none" stroke="var(--c4)" stroke-width="2.5"/>'
              f'<circle cx="{ax + aw - 24}" cy="{yc}" r="11" fill="{ok}"/>' + check(ax + aw - 24, yc + 1, .55, "var(--ink)") + '</g>')
    order = [k for k in range(n) if k != pick] + [pick]
    hops = [.083 + i * (t_pick - .083) / (n - 1) for i in range(n)]  # 1.0 s, then every 0.4 s
    scan = (f'<rect x="{ax - 5}" y="{y0 - 5}" width="{aw + 10}" height="60" rx="17" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
            f'<animateTransform attributeName="transform" type="translate" values="0 {pick * 60};{";".join(f"0 {k * 60}" for k in order)}" '
            f'keyTimes="0;{";".join(f"{t:.3f}" for t in hops)}" dur="{D}s" repeatCount="indefinite" calcMode="discrete"/>'
            f'{beat("opacity", [(0, 0), (.08, 0), (.083, 1), (_N13_RESET, 1), (.985, 0), (1, 0)])}</rect>')

    # this week: the discovery workshop fills in the pain, how to solve it and the KPI, one check at a time
    wtitle, wrows = sl["workshop"]
    b = card(bx, y0, bw, h, "var(--card)", "var(--c2)", 18, 1.5) + pill(bx + bw / 2, y0 + 38, wtitle, "var(--c2)", ctx, 17, bw - 40, "n13 workshop")
    for j, (verb, text) in enumerate(wrows[:3]):
        y, t = y0 + 96 + j * 70, .3 + j * .067  # 3.6, 4.4 and 5.2 s
        room = bw - 84
        b += T(bx + 24, y, verb, 15, "var(--c4)", W6) + f'<circle cx="{bx + bw - 36}" cy="{y + 10}" r="13" fill="none" stroke="var(--line)" stroke-width="1.5"/>'
        if j == 0:  # the template line becomes the pain they chose
            b += (f'<g>{_n13_off(t)}' + T(bx + 24, y + 28, text, fit(text, 18, room, "n13 workshop row"), "var(--muted)", W6) + '</g>'
                  f'<g opacity="0">{_n13_on(t)}' + T(bx + 24, y + 28, opts[pick], fit(opts[pick], 18, room, "n13 workshop row"), "var(--white)", W6) + '</g>')
        else:
            b += f'<g>{_n13_lit(t, .6)}' + T(bx + 24, y + 28, text, fit(text, 18, room, "n13 workshop row"), "var(--white)", W6) + '</g>'
        b += f'<g opacity="0">{_n13_on(t)}<circle cx="{bx + bw - 36}" cy="{y + 10}" r="13" fill="{ok}"/>' + check(bx + bw - 36, y + 11, .6, "var(--ink)") + '</g>'

    # a week later: the prototype comes alive, slide 14 in miniature (the same ticket, space, lock and source)
    live, drop, ask_a, ans_a, solved, kpi_t = .533, .55, .57, .61, .645, .69  # 6.4, 6.6, 6.8, 7.3, 7.7 and 8.3 s
    c = (card(cx, y0, cw, h, "var(--card)", "var(--c3)", 18, 1.5) + f'<path d="M{cx} {y0 + 44} H{cx + cw}" stroke="var(--line)" stroke-width="1.5"/>'
         + "".join(f'<circle cx="{cx + 24 + k * 18}" cy="{y0 + 22}" r="5" fill="var(--line)"/>' for k in range(3))
         + f'<g opacity="0">{_n13_on(live)}' + "".join(f'<circle cx="{cx + 24 + k * 18}" cy="{y0 + 22}" r="5" fill="{col}"/>' for k, col in enumerate(("var(--c5)", "var(--c4)", ok))) + '</g>'
         + T(cx + 84, y0 + 28, sl["proto"], fit(sl["proto"], 17, cw - 200, "n13 prototype"), "var(--white)", W6)
         + f'<g opacity="0">{_n13_on(live)}' + pill(cx + cw - 64, y0 + 22, sl["live"], ok, ctx, 15, 110, "n13 live", 14) + '</g>')
    px, pw = cx + 16, cw - 32
    ty, th = y0 + 58, 56
    # the queue slot waits, dashed, until a merchant question drops in; it closes as self-served
    tk = (card(px, ty, pw, th, "var(--dim)", "var(--line)", 12, 1.2)
          + T(px + 16, ty + 23, sl["ticket"], fit(sl["ticket"], 15, pw - 48, "n13 ticket"), "var(--white)", W6)
          + f'<g>{_n13_off(solved, f=.01)}<circle cx="{px + pw - 18}" cy="{ty + 17}" r="5" fill="var(--c2)"/>' + T(px + 16, ty + 45, sl["new"], 15, "var(--muted)", W6) + '</g>'
          + f'<g opacity="0">{_n13_on(solved, f=.01)}<circle cx="{px + pw - 18}" cy="{ty + 17}" r="5" fill="{ok}"/>'
          + T(px + 16, ty + 45, sl["solved"], fit(sl["solved"], 15, pw - 40, "n13 status"), ok, W6) + '</g>'
          + f'<rect x="{px}" y="{ty}" width="{pw}" height="{th}" rx="12" fill="none" stroke="{ok}" stroke-width="2.5" stroke-opacity="0">'
          f'{beat("stroke-opacity", [(0, 0), (solved, 0), (solved + .01, 1), (solved + .07, 0), (1, 0)])}</rect>')
    c += (f'<g>{_n13_off(drop)}' + card(px, ty, pw, th, "none", "var(--line)", 12, 1.5, 'stroke-dasharray="6 6"') + '</g>'
          f'<g opacity="0">{_n13_on(drop)}<g><animateTransform attributeName="transform" type="translate" values="0 -14;0 -14;0 0;0 0" '
          f'keyTimes="0;{drop};{drop + .025};1" dur="{D}s" repeatCount="indefinite"/>{tk}</g></g>')
    # the restricted space the agent answers from, with its lock and its source
    qy = ty + th + 12
    gx, gy = px + pw - 48, qy + 60  # the agent's center
    dy_ = qy + 66
    c += (card(px, qy, pw, 92, "var(--dim)", "var(--accent)", 14, 1.4) + _lock(px + pw - 22, qy + 22)
          + T(px + 16, qy + 28, sl["space"], fit(sl["space"], 15, pw - 64, "n13 space"), "var(--white)", W6)
          + _q13_doc(px + 16, dy_) + T(px + 38, dy_, sl["doc"], fit(sl["doc"], 15, pw - 150, "n13 doc"), "var(--muted)", W6)
          + f'<path d="M{px + 46 + bold_width(_(str(sl["doc"])), 15, current_factor()):.0f} {dy_ - 5} H{gx - 40}" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 5"/>'
          + card(gx - 32, gy - 20, 64, 40, "var(--card)", "var(--accent)", 12, 1.4) + spark(gx, gy, .7, "var(--accent)")
          + f'<rect x="{gx - 38}" y="{gy - 26}" width="76" height="52" rx="15" fill="none" stroke="var(--c4)" stroke-width="2.5" stroke-opacity="0">'
          f'{beat("stroke-opacity", [(0, 0), (ask_a + .02, 0), (ask_a + .03, 1), (ans_a + .03, 1), (ans_a + .04, 0), (1, 0)])}</rect>'
          + f'<g opacity="0">{_n13_on(ask_a + .03)}<rect x="{px + 8}" y="{dy_ - 18}" width="{gx - 44 - px}" height="26" rx="8" fill="var(--c4)" opacity=".14"/>'
          + _q13_doc(px + 16, dy_, "var(--c4)") + T(px + 38, dy_, sl["doc"], fit(sl["doc"], 15, pw - 150, "n13 doc"), "var(--c4)", W6)
          + f'<path d="M{px + 46 + bold_width(_(str(sl["doc"])), 15, current_factor()):.0f} {dy_ - 5} H{gx - 40}" stroke="var(--c4)" stroke-width="1.5" stroke-dasharray="3 5">'
          f'{loop("stroke-dashoffset", "0;-16", 1)}</path></g>')
    # the question goes down to the agent and the answer comes back up
    leg = f"M{px + pw - 18} {ty + th} C{px + pw - 18} {ty + th + 30} {gx} {gy - 50} {gx} {gy - 22}"
    c += _n13_ride(leg, ask_a, ask_a + .035, 5) + _n13_ride(f"M{gx} {gy - 22} C{gx} {gy - 50} {px + pw - 18} {ty + th + 30} {px + pw - 18} {ty + th}", ans_a, ans_a + .035, 5)
    # the KPI of the success case, on screen once the ticket closes by itself
    ky = y0 + 230
    c += (card(px, ky, pw, 52, "none", "var(--line)", 12, 1.5, 'stroke-dasharray="6 6"')
          + f'<g opacity="0">{_n13_on(kpi_t)}' + card(px, ky, pw, 52, "var(--dim)", ok, 12, 1.5)
          + T(px + 16, ky + 32, sl["kpi"], fit(sl["kpi"], 16, pw - 70, "n13 kpi"), "var(--white)", W6)
          + f'<circle cx="{px + pw - 26}" cy="{ky + 26}" r="12" fill="{ok}"/>' + check(px + pw - 26, ky + 27, .55, "var(--ink)") + '</g>')

    # the boot: a warm light behind the window and one scan line down its body as it goes live
    boot = (f'<g opacity="0">{beat("opacity", [(0, 0), (live, 0), (live + .03, 1), (.6, .45), (_N13_RESET, .45), (.985, 0), (1, 0)])}'
            + glow(cx + cw / 2, y0 + h / 2, 300, "var(--c3)", .5) + '</g>')
    c += (f'<rect x="{cx + 2}" y="{y0 + 46}" width="{cw - 4}" height="2" fill="var(--c3)" opacity="0">'
          f'{beat("opacity", [(0, 0), (live, 0), (live + .004, .8), (.585, .8), (.59, 0), (1, 0)])}'
          f'<animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 {h - 50};0 {h - 50}" keyTimes="0;{live};.585;1" dur="{D}s" repeatCount="indefinite"/></rect>')

    # then: their call, with a proposal fitted to them among the four ways to start
    ask_, ways = sl["offer"]
    dd = card(dx, y0, dw, h, "var(--card)", ok, 18, 1.5) + T(dx + 22, y0 + 48, ask_, fit(ask_, 20, dw - 44, "n13 offer"), "var(--white)", W6)
    for j, way in enumerate(ways[:4]):
        y, t = y0 + 92 + j * 38, .783 + j * .025  # 9.4, 9.7, 10.0 and 10.3 s
        dd += (f'<circle cx="{dx + 30}" cy="{y}" r="6" fill="none" stroke="var(--line)" stroke-width="1.5"/>'
               f'<g opacity="0">{_n13_on(t)}<circle cx="{dx + 30}" cy="{y}" r="6" fill="{ok}"/></g>'
               f'<g>{_n13_lit(t)}' + T(dx + 46, y + 6, way, fit(way, 17, dw - 70, "n13 way"), "var(--white)", W6) + '</g>')
    s = fit(sl["decide"], 16, dw - 60, "n13 decision")
    qw = min(dw - 24, bold_width(_(str(sl["decide"])), s, current_factor()) + 36)
    dd += (f'<g>{_n13_off(.875)}' + card(dx + (dw - qw) / 2, y0 + 244, qw, s + 20, "none", "var(--line)", (s + 20) / 2, 1.5, 'stroke-dasharray="5 5"') + '</g>'
           + f'<g opacity="0">{_n13_on(.875)}' + pill(dx + dw / 2, y0 + 244 + (s + 20) / 2, sl["decide"], ok, ctx, 16, dw - 24, "n13 decision") + '</g>')

    # the step on stage lights up; what each step produces rides to the next one
    frames = "".join(f'<rect x="{x - 6}" y="{y0 - 6}" width="{w + 12}" height="{h + 12}" rx="22" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity="0">'
                     f'{_n13_on(t0 + .01, (t1 if t1 < 1 else _N13_RESET) - .01, .02, .75)}</rect>'
                     for (x, w), t0, t1 in zip(X[1:], starts[1:], starts[2:] + (1,)))
    ya = y0 + 150
    link1 = f"M{ax + aw + 4} {yc} C{ax + aw + 26} {yc} {bx - 26} {ya} {bx - 8} {ya}"
    arrows = (f'<g opacity="0">{_n13_on(t_pick)}<path d="{link1}" fill="none" stroke="var(--c2)" stroke-width="2" stroke-dasharray="4 7">{loop("stroke-dashoffset", "0;-22", 1.6)}</path></g>'
              + "".join(f'<path d="M{x0 + 8} {ya} H{x1 - 10}" stroke="var(--c2)" stroke-width="2" stroke-dasharray="4 7">{loop("stroke-dashoffset", "0;-22", 1.6)}</path>'
                        for x0, x1 in ((bx + bw, cx), (cx + cw, dx)))
              + "".join(f'<path d="M{x1 - 14} {ya - 7} L{x1 - 5} {ya} L{x1 - 14} {ya + 7}" fill="none" stroke="var(--c2)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
                        for x1 in (bx, cx, dx)))
    rides = (_n13_ride(link1, .222, .283) + _n13_ride(f"M{bx + bw} {ya} H{cx - 6}", .483, .525)
             + _n13_ride(f"M{cx + cw} {ya} H{dx - 6}", .733, .775))

    # the time rail: today, this week, a week later, then their call
    yr = y0 + h + 34
    xm = [x + w / 2 for x, w in X]
    fr = [(m - xm[0]) / (xm[-1] - xm[0]) for m in xm]
    reach = (0, .292, .542, .792)
    rail = (f'<path d="M{xm[0]} {yr} H{xm[-1]}" stroke="var(--line)" stroke-width="2"/>'
            f'<path d="M{xm[0]} {yr} H{xm[-1]}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="0" fill="none" stroke="var(--c4)" stroke-width="2">'
            + beat("stroke-dashoffset", [(0, 1), (.25, 1), (reach[1], 1 - fr[1]), (.5, 1 - fr[1]), (reach[2], 1 - fr[2]), (.75, 1 - fr[2]), (reach[3], 0),
                                         (_N13_RESET, 0), (.985, 1), (1, 1)]) + '</path>')
    for k, (m, t, (x, w)) in enumerate(zip(xm, sl["when"], X)):
        rail += f'<circle cx="{m}" cy="{yr}" r="7" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>'
        rail += f'<circle cx="{m}" cy="{yr}" r="3.5" fill="var(--c4)"/>' if not k else f'<g opacity="0">{_n13_on(reach[k])}<circle cx="{m}" cy="{yr}" r="3.5" fill="var(--c4)"/></g>'
        lab = TC(m, yr + 36, t, fit(t, 17, w, "n13 when"), "var(--c4)", W6)
        rail += lab if not k else f'<g>{_n13_lit(reach[k], .5)}{lab}</g>'
    now = (f'<g>{move(f"M{xm[0]} {yr} H{xm[-1]}", [(0, 0), (.25, 0), (reach[1], fr[1]), (.5, fr[1]), (reach[2], fr[2]), (.75, fr[2]), (reach[3], 1), (_N13_RESET, 1), (.985, 0), (1, 0)], D)}'
           + token("var(--c4)", 7) + '</g>')
    return (glow(800, 580, 560, "var(--brand)", .4) + boot + seq([a, b, c, dd], .1, .5, 18) + land(arrows + chosen + scan + frames, .9, .4, 0)
            + rides + land(rail + now, .7, .45, 0)), D, FREEZE


# ---------------------------------------------------------------- 14 · Más tiempo para cada negocio
def _pn14_twin(sl, ctx):
    """tickets-live in portrait: the same wall screen redrawn as a stack so every label is 20 units or more (the queue of
    four at full width, the restricted space with its agent, lock and sources under it, IT's monitoring at the foot), the
    sign above it and the two operators, seen from behind, at a console that crops them at the foot of the art zone. The
    simple questions ride down the left gutter to the agent and back; the sensitive one leaves by the screen's right edge
    to his tablet and his tap rides back up to close it. Same beats as the desktop story; same frozen frame."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    ok = ctx.brand.c("dark.ok")
    ch = lambda t, s, room, where: fit(t, s, room, where, floor=20)
    sx, sy, sw = zx, zy + 44, zw
    qx, qw, qh = sx + 56, sw - 72, 62                  # the queue, with a gutter on its left for the legs
    ys = [sy + 94 + k * 70 for k in range(4)]
    bx, by, bw, bh = qx, ys[3] + qh + 10, qw, 160      # the space
    mx, my, mw, mh = sx + 16, by + bh + 10, sw - 32, 100  # IT's band
    sh = my + mh + 12 - sy
    sb = sy + sh
    asks = (.10, .26, .42)
    done = [a + .13 for a in asks]
    t_route, t_ctx, t_tap, t_back, t_closed, t_calm = .64, .72, .77, .79, .83, .86
    g = [glow(sx + sw / 2, sy + sh / 2, 420, "var(--brand)", .5)]
    sign = T(sx + sw - 8, zy + 28, sl["sign"], ch(sl["sign"], 22, zw - 40, "n14 sign"), "var(--c4)", 'text-anchor="end" font-weight="600"')

    screen = (card(sx, sy, sw, sh, "var(--card)", "var(--c2)", 22, 1.2) + f'<path d="M{sx} {sy + 50} H{sx + sw}" stroke="var(--line)" stroke-width="1.5"/>'
              + f'<rect x="{sx + 2}" y="{sy + 52}" width="{sw - 4}" height="2" fill="var(--c2)" opacity=".18">'
              f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {sh - 58}" dur="5s" repeatCount="indefinite"/></rect>'
              + "".join(f'<circle cx="{sx + 26 + k * 18}" cy="{sy + 26}" r="5" fill="{col}"/>' for k, col in enumerate(("var(--c5)", "var(--c4)", ok)))
              + T(sx + 86, sy + 34, sl["screen"], ch(sl["screen"], 22, sw - 260, "n14 screen"), "var(--white)", W6)
              + pill(sx + sw - 70, sy + 26, sl["live"], ok, ctx, 20, 130, "n14 live", 14))
    head = T(qx, sy + 80, sl["queue"], 20, "var(--muted)", W6)
    dot = lambda y, col: f'<circle cx="{qx + qw - 20}" cy="{y + 20}" r="6" fill="{col}"/>'
    stat = lambda y, lab, col: T(qx + 16, y + 52, lab, ch(lab, 20, qw - 32, "n14 status"), col, W6)
    tickets = []
    for k, (q, y) in enumerate(zip(sl["tickets"][:4], ys)):
        c = card(qx, y, qw, qh, "var(--dim)", "var(--line)", 12, 1.2) + T(qx + 16, y + 26, q, ch(q, 21, qw - 52, "n14 ticket"), "var(--white)", W6)
        new = dot(y, "var(--c2)") + T(qx + 16, y + 52, sl["new"], 20, "var(--muted)", W6)
        r = done[k] if k < 3 else t_closed
        if k < 3:
            c += _swap([(0, 1), (r, 1), (r + .01, 0), (.97, 0), (1, 1)], new)
            c += _swap([(0, 0), (r, 0), (r + .01, 1), (.97, 1), (1, 0)], dot(y, ok) + stat(y, sl["solved"], ok))
        else:
            c += _swap([(0, 1), (t_route, 1), (t_route + .01, 0), (.97, 0), (1, 1)], new)
            c += _swap([(0, 0), (t_route, 0), (t_route + .01, 1), (r, 1), (r + .01, 0), (1, 0)],
                       dot(y, "var(--accent)") + stat(y, sl["routed"], "var(--c2)")
                       + f'<rect x="{qx}" y="{y}" width="{qw}" height="{qh}" rx="12" fill="none" stroke="var(--accent)" stroke-width="2.5">{loop("stroke-opacity", ".3;1;.3", 1.2)}</rect>')
            c += _swap([(0, 0), (r, 0), (r + .01, 1), (.97, 1), (1, 0)], dot(y, ok) + stat(y, sl["closed"], ok))
        c += (f'<rect x="{qx}" y="{y}" width="{qw}" height="{qh}" rx="12" fill="none" stroke="{ok}" stroke-width="2.5" stroke-opacity="0">'
              f'{beat("stroke-opacity", [(0, 0), (r, 0), (r + .01, 1), (r + .07, 0), (1, 0)])}</rect>')
        tickets.append(c)
    calm = _swap([(0, 0), (t_calm, 0), (t_calm + .02, 1), (.97, 1), (1, 0)], pill(qx + qw - 80, sy + 71, sl["calm"], ok, ctx, 20, 160, "n14 calm", 14))

    # the space the agent answers from: restricted, with its lock and its sources
    ax, ay = bx + 80, by + 98
    space = (card(bx, by, bw, bh, "var(--card)", "var(--accent)", 16, 1.6) + _lock(bx + bw - 24, by + 24)
             + T(bx + 18, by + 32, sl["space"], ch(sl["space"], 21, bw - 70, "n14 space"), "var(--white)", W6)
             + T(bx + 18, by + 58, sl["space_sub"], ch(sl["space_sub"], 20, bw - 36, "n14 space sub"), "var(--muted)", W6)
             + card(ax - 50, ay - 26, 100, 56, "var(--dim)", "var(--accent)", 14, 1.4) + spark(ax, ay + 2, .8, "var(--accent)")
             + T(bx + 18, by + bh - 10, sl["agent"], ch(sl["agent"], 20, 270, "n14 agent"), "var(--c4)", W6))
    dx0 = bx + 300
    dys = [by + 100 + j * 28 for j in range(3)]
    lit = ""
    for j, (lab, a) in enumerate(zip(sl["docs"][:3], asks)):
        ds = ch(lab, 20, bw - 340, "n14 doc")
        space += _q13_doc(dx0, dys[j]) + T(dx0 + 22, dys[j], lab, ds, "var(--muted)", W6)
        lit += _swap([(0, 0), (a + .05, 0), (a + .06, 1), (a + .13, 1), (a + .14, 0), (1, 0)],
                     f'<rect x="{dx0 - 8}" y="{dys[j] - 20}" width="{bw - 310}" height="27" rx="8" fill="var(--c4)" opacity=".14"/>'
                     + _q13_doc(dx0, dys[j], "var(--c4)") + T(dx0 + 22, dys[j], lab, ds, "var(--c4)", W6))
    answering = [(0, 0)]
    for a, b in [(a + .06, a + .12) for a in asks] + [(.63, .66)]:
        answering += [(a, 0), (a + .01, 1), (b, 1), (b + .01, 0)]
    answering.append((1, 0))
    ring = f'<rect x="{ax - 56}" y="{ay - 32}" width="112" height="68" rx="18" fill="none" stroke="var(--c4)" stroke-width="3" stroke-opacity="0">{beat("stroke-opacity", answering)}</rect>'
    lock_on = (f'<circle cx="{bx + bw - 24}" cy="{by + 24}" r="16" fill="none" stroke="var(--accent)" stroke-width="2" opacity="0">'
               f'{beat("opacity", [(0, 0), (.63, 0), (.64, 1), (.7, 0), (1, 0)])}{beat("r", [(0, 14), (.63, 14), (.7, 30), (1, 30)])}</circle>')

    # the legs: down the left gutter to the agent and back
    gx_ = sx + 30
    down = lambda y: f"M{qx} {y} C{gx_} {y} {gx_} {y + 20} {gx_} {y + 40} V{ay - 30} C{gx_} {ay} {gx_ + 20} {ay} {ax - 50} {ay}"
    up = lambda y: f"M{ax - 50} {ay} C{gx_ + 20} {ay} {gx_} {ay} {gx_} {ay - 30} V{y + 40} C{gx_} {y + 20} {gx_} {y} {qx} {y}"
    legs = "".join(_leg(down(ys[k] + qh / 2), a, a + .06) + _leg(up(ys[k] + qh / 2), a + .06, a + .12) for k, a in enumerate(asks))
    y4 = ys[3] + qh / 2
    legs += _leg(down(y4), .58, .63)

    # IT monitoring and control: the self-served share as a bar (no number), usage per space, the record
    tw, fw = 260, [78, 117, 156, 195]
    share = beat("width", [(0, fw[0]), (done[0], fw[0]), (done[0] + .01, fw[1]), (done[1], fw[1]), (done[1] + .01, fw[2]), (done[2], fw[2]),
                           (done[2] + .01, fw[3]), (.97, fw[3]), (1, fw[0])])
    bx2 = mx + 196
    band = (card(mx, my, mw, mh, "var(--dim)", "var(--line)", 14, 1.2) + T(mx + 16, my + 30, sl["monitor"], ch(sl["monitor"], 21, 440, "n14 monitor"), "var(--c4)", W6)
            + T(mx + 16, my + 62, sl["share"], ch(sl["share"], 20, 172, "n14 share"), "var(--white)", W6)
            + f'<rect x="{bx2}" y="{my + 50}" width="{tw}" height="12" rx="6" fill="var(--line)"/>'
            + f'<rect x="{bx2}" y="{my + 50}" width="{fw[3]}" height="12" rx="6" fill="{ok}">{share}</rect>'
            + T(mx + 16, my + 90, sl["usage"], ch(sl["usage"], 20, 172, "n14 usage"), "var(--white)", W6))
    for j, (w0, w1) in enumerate(((.7, .45), (.4, .75), (.55, .3))):
        x0 = bx2 + j * 91
        band += (f'<rect x="{x0}" y="{my + 80}" width="78" height="9" rx="4.5" fill="var(--line)"/>'
                 f'<rect x="{x0}" y="{my + 80}" width="{78 * w0:.0f}" height="9" rx="4.5" fill="var(--c2)">{loop("width", f"{78 * w0:.0f};{78 * w1:.0f};{78 * w0:.0f}", 5 + j, j)}</rect>')
    rx_ = mx + 490
    for j, row in enumerate(sl["rows"][:2]):
        yy = my + 62 + j * 28
        band += (f'<g>{loop("opacity", ".5;1;.5", 4, j * 1.5)}<circle cx="{rx_}" cy="{yy - 6}" r="9" fill="{ok}"/>{check(rx_, yy - 5, .5, "var(--ink)")}</g>'
                 + T(rx_ + 18, yy, row, ch(row, 20, mx + mw - rx_ - 30, "n14 record"), "var(--white)", W6))
    wall = (screen + land(head, .3, .4, 8) + seq(tickets, .35, .45, 12, 1.4) + land(space, .5, .5, 12) + land(band, .7, .5, 10)
            + calm + lit + ring + lock_on)
    ccx, ccy = sx + sw / 2, sy + sh / 2

    # the operator's tablet: the routed case arrives with its context, «Resolver», his tap, then resolved
    tap = (_swap([(0, 0), (t_ctx, 0), (t_ctx + .01, 1), (.97, 1), (1, 0)], bars(-48, -27, 92, 2, 12, "var(--accent)", ".9"))
           + _swap([(0, 0), (t_ctx, 0), (t_ctx + .01, 1), (t_back - .005, 1), (t_back, 0), (1, 0)], pill(0, 16, sl["review"], "var(--c4)", ctx, 20, 114, "n14 review", 10))
           + _swap([(0, 0), (t_back - .005, 0), (t_back, 1), (.97, 1), (1, 0)], f'<rect x="-36" y="2" width="72" height="28" rx="14" fill="{ok}"/>' + check(0, 17, .65, "var(--ink)"))
           + f'<circle cx="0" cy="16" r="6" fill="none" stroke="var(--white)" stroke-width="1.5" opacity="0">{beat("r", [(0, 6), (t_tap, 6), (t_tap + .08, 34), (1, 34)])}'
           f'{beat("opacity", [(0, 0), (t_tap, 0), (t_tap + .01, 1), (t_tap + .08, 0), (1, 0)])}</circle>')
    mnx, mny = zx + 540, sb + 80
    wmx, wmy = zx + 170, sb + 84
    desk = mny + 100
    tbx, tby = mnx + 112 + 16 * math.sin(math.radians(10)), mny + 62 + 16 * math.cos(math.radians(10))
    ex = sx + sw - 8  # the screen's right edge, where the sensitive case leaves for his tablet
    route = (f"M{ax + 50} {ay - 14} C{ax + 90} {ay - 14} {ax + 90} {by + 70} {ax + 130} {by + 70} H{ex - 12} C{ex} {by + 70} {ex} {by + 80} {ex} {by + 96} "
             f"V{sb + 4} C{ex} {sb + 50} {tbx + 30:.0f} {tby - 100:.0f} {tbx - 8:.0f} {tby - 56:.0f}")
    back_d = (f"M{tbx - 12:.0f} {tby - 56:.0f} C{tbx - 24:.0f} {tby - 110:.0f} {ex + 4} {sb + 40} {ex + 4} {sb} "
              f"V{y4 + 24} C{ex + 4} {y4} {qx + qw + 6} {y4} {qx + qw} {y4}")
    back = (f'<g opacity="0">{beat("opacity", [(0, 0), (t_back, 0), (t_back + .005, .9), (t_closed, .9), (t_closed + .03, 0), (1, 0)])}'
            f'<path d="{back_d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="1.5" stroke-linecap="round">'
            f'{beat("stroke-dashoffset", [(0, 1), (t_back, 1), (t_closed, 0), (1, 0)])}</path></g>' + _leg(back_d, t_back, t_closed))
    people = (f'<clipPath id="pn14-desk"><rect x="0" y="0" width="900" height="{desk + 2:.0f}"/></clipPath>'
              f'<g clip-path="url(#pn14-desk)">' + land(_n14_woman(wmx, wmy, .95, SKIN_BROWN, "var(--accent)"), .25, .6, 40)
              + land(_n14_man(mnx, mny, 1.0, SKIN_LIGHT, "var(--c1)", tap), .4, .6, 40) + '</g>')
    leds = "".join(f'<circle cx="{zx + 40 + k * 26}" cy="{desk + 8}" r="2.2" fill="var(--c2)" opacity=".45"/>' for k in range(8))
    sbar = lambda col: f'<rect x="{zx + zw - 150}" y="{desk + 5}" width="120" height="7" rx="3.5" fill="{col}"/>'
    status = (_swap([(0, 0), (t_route, 0), (t_route + .01, 1), (t_closed, 1), (t_closed + .01, 0), (1, 0)], sbar("var(--accent)"))
              + _swap([(0, 0), (t_calm, 0), (t_calm + .02, 1), (.97, 1), (1, 0)], sbar(ok)))
    console = land(f'<path d="M{zx} {desk} H{zx + zw} L{zx + zw - 8} {desk + 18} H{zx + 8} Z" fill="var(--card)"/>' + sbar("var(--line)")
                   + f'<path d="M{zx} {desk} H{zx + zw}" stroke="var(--c2)" stroke-width="1.5" opacity=".7"/>' + leds + status, .2, .5, 20)
    art = (g[0] + pop(f'<g transform="translate({-ccx} {-ccy})">{wall}</g>', ccx, ccy, .05, .6)
           + legs + land(sign, 1.4, .45, 10) + back + people + _leg(route, t_route, t_ctx) + console)
    return _pz_clip(art, "pn14"), D, FREEZE


@register("scene", "n14_tickets")
def sc_n14_tickets(sl, ctx):
    """ext.py `tickets` with four polishes. (1) It opens as slide 13's prototype grown up: the wall screen pops from the
    prototype's size with the same three lights, «En vivo», ticket, space, lock and source. (2) Each answer is visible as
    cause: the question rides to the agent, the source it answers from lights up in the space, the answer rides back and
    the ticket flashes as it closes. The sensitive one lights the lock and rides to the person's tablet with its context;
    his tap rides back and closes it: people decide. (3) Every label is 15 px or more. (4) The operators, seen from behind
    (energía v4), stand at a console that crops them above the footer. IT watches the self-served share (a bar, never a
    number), usage per space and the record. Frozen frame (0.9 of the loop): a calm queue, all four resolved."""
    if ORIENT() == "portrait":
        return _pn14_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    sx, sy, sw, sh = 832, 98, 720, 456
    desk = 796  # the console's top edge: the operators stand behind it, nothing is drawn below 830
    g = [glow(1192, 320, 480, "var(--brand)", .55)]
    cone = (f'<path d="M{sx + 40} {sy + sh} L{sx + sw - 30} {sy + sh} L1560 {desk} L820 {desk} Z" fill="var(--c2)" opacity=".07">'
            f'{loop("opacity", ".04;.12;.04", 5)}</path>')
    hud = "".join(f'<path d="M{x0} {y0 + dy * 22} V{y0} H{x0 + dx * 22}" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity=".8" transform="translate({dx * -8} {dy * -8})"/>'
                  for x0, y0, dx, dy in ((sx, sy, 1, 1), (sx + sw, sy, -1, 1), (sx, sy + sh, 1, -1), (sx + sw, sy + sh, -1, -1)))
    hud += (f'<rect x="{sx + 2}" y="{sy + 46}" width="{sw - 4}" height="2" fill="var(--c2)" opacity=".18">'
            f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {sh - 52}" dur="5s" repeatCount="indefinite"/></rect>')
    # the header of slide 13's prototype window, grown up: the same three lights and «En vivo»
    screen = (card(sx, sy, sw, sh, "var(--card)", "var(--c2)", 22, 1.2) + hud
              + f'<path d="M{sx} {sy + 44} H{sx + sw}" stroke="var(--line)" stroke-width="1.5"/>'
              + "".join(f'<circle cx="{sx + 24 + k * 18}" cy="{sy + 22}" r="5" fill="{col}"/>' for k, col in enumerate(("var(--c5)", "var(--c4)", ok)))
              + T(sx + 84, sy + 28, sl["screen"], fit(sl["screen"], 17, 440, "n14 screen"), "var(--white)", W6)
              + pill(sx + sw - 64, sy + 22, sl["live"], ok, ctx, 15, 110, "n14 live", 14))
    # the queue: four tickets; each status swaps on its beat (new, then self-served; the sensitive one: routed, then closed)
    qx, qw, qh = sx + 16, 338, 54
    ys = [sy + 94 + k * 62 for k in range(4)]
    asks = (.10, .26, .42)            # the three simple questions leave for the agent here
    done = [a + .13 for a in asks]    # and close here: 2.8, 4.7 and 6.6 s
    t_route, t_ctx, t_tap, t_back, t_closed, t_calm = .64, .72, .77, .79, .83, .86
    head = T(qx, sy + 72, sl["queue"], 15, "var(--muted)", W6)
    tickets = []
    for k, (q, y) in enumerate(zip(sl["tickets"][:4], ys)):
        c = card(qx, y, qw, qh, "var(--dim)", "var(--line)", 12, 1.2) + T(qx + 16, y + 22, q, fit(q, 15, qw - 44, "n14 ticket"), "var(--white)", W6)
        new = f'<circle cx="{qx + qw - 18}" cy="{y + 17}" r="5" fill="var(--c2)"/>' + T(qx + 16, y + 44, sl["new"], 15, "var(--muted)", W6)
        res = lambda lab: f'<circle cx="{qx + qw - 18}" cy="{y + 17}" r="5" fill="{ok}"/>' + T(qx + 16, y + 44, lab, fit(lab, 15, qw - 40, "n14 status"), ok, W6)
        r = done[k] if k < 3 else t_closed
        flash = (f'<rect x="{qx}" y="{y}" width="{qw}" height="{qh}" rx="12" fill="none" stroke="{ok}" stroke-width="2.5" stroke-opacity="0">'
                 f'{beat("stroke-opacity", [(0, 0), (r, 0), (r + .01, 1), (r + .07, 0), (1, 0)])}</rect>')
        if k < 3:
            c += _swap([(0, 1), (r, 1), (r + .01, 0), (.97, 0), (1, 1)], new)
            c += _swap([(0, 0), (r, 0), (r + .01, 1), (.97, 1), (1, 0)], res(sl["solved"]))
        else:
            c += _swap([(0, 1), (t_route, 1), (t_route + .01, 0), (.97, 0), (1, 1)], new)
            c += _swap([(0, 0), (t_route, 0), (t_route + .01, 1), (r, 1), (r + .01, 0), (1, 0)],
                       f'<circle cx="{qx + qw - 18}" cy="{y + 17}" r="5" fill="var(--accent)"/>' + T(qx + 16, y + 44, sl["routed"], fit(sl["routed"], 15, qw - 40, "n14 status"), "var(--c2)", W6)
                       + f'<rect x="{qx}" y="{y}" width="{qw}" height="{qh}" rx="12" fill="none" stroke="var(--accent)" stroke-width="2.5">{loop("stroke-opacity", ".3;1;.3", 1.2)}</rect>')
            c += _swap([(0, 0), (r, 0), (r + .01, 1), (.97, 1), (1, 0)], res(sl["closed"]))
        tickets.append(c + flash)
    calm = _swap([(0, 0), (t_calm, 0), (t_calm + .02, 1), (.97, 1), (1, 0)], pill(qx + qw - 58, sy + 66, sl["calm"], ok, ctx, 15, 130, "n14 calm", 14))
    # the space the agent answers from: restricted, with its lock and its sources
    bx, by, bw, bh = qx + qw + 14, sy + 50, 336, 284
    ax, ay = bx + bw / 2, by + 122
    space = (card(bx, by, bw, bh, "var(--card)", "var(--accent)", 16, 1.6) + _lock(bx + bw - 24, by + 24)
             + T(bx + 18, by + 30, sl["space"], fit(sl["space"], 15, bw - 70, "n14 space"), "var(--white)", W6)
             + T(bx + 18, by + 52, sl["space_sub"], fit(sl["space_sub"], 15, bw - 32, "n14 space sub"), "var(--muted)", W6)
             + card(ax - 50, ay - 32, 100, 64, "var(--dim)", "var(--accent)", 14, 1.4) + spark(ax, ay, .9, "var(--accent)")
             + TC(ax, ay + 54, sl["agent"], fit(sl["agent"], 15, bw - 40, "n14 agent"), "var(--c4)", W6))
    dys = [by + 212 + j * 26 for j in range(3)]
    lit = ""
    for j, (lab, a) in enumerate(zip(sl["docs"][:3], asks)):
        space += _q13_doc(bx + 18, dys[j]) + T(bx + 40, dys[j], lab, fit(lab, 15, bw - 60, "n14 doc"), "var(--muted)", W6)
        # the source this answer comes from lights up while the agent answers
        lit += _swap([(0, 0), (a + .05, 0), (a + .06, 1), (a + .13, 1), (a + .14, 0), (1, 0)],
                     f'<rect x="{bx + 10}" y="{dys[j] - 18}" width="{bw - 20}" height="25" rx="8" fill="var(--c4)" opacity=".14"/>'
                     + _q13_doc(bx + 18, dys[j], "var(--c4)") + T(bx + 40, dys[j], lab, fit(lab, 15, bw - 60, "n14 doc"), "var(--c4)", W6))
    answering = [(0, 0)]
    for a, b in [(a + .06, a + .12) for a in asks] + [(.63, .66)]:
        answering += [(a, 0), (a + .01, 1), (b, 1), (b + .01, 0)]
    answering.append((1, 0))
    ring = f'<rect x="{ax - 56}" y="{ay - 38}" width="112" height="76" rx="18" fill="none" stroke="var(--c4)" stroke-width="3" stroke-opacity="0">{beat("stroke-opacity", answering)}</rect>'
    # the sensitive one: the lock lights, the space keeps it, a person takes it
    lock_on = (f'<circle cx="{bx + bw - 24}" cy="{by + 24}" r="16" fill="none" stroke="var(--accent)" stroke-width="2" opacity="0">'
               f'{beat("opacity", [(0, 0), (.63, 0), (.64, 1), (.7, 0), (1, 0)])}{beat("r", [(0, 14), (.63, 14), (.7, 30), (1, 30)])}</circle>')
    # the legs: question to the agent, answer back; the sensitive one leaves the screen by its right edge to the tablet
    legs = ""
    for k, a in enumerate(asks):
        y = ys[k] + qh / 2
        legs += (_leg(f"M{qx + qw} {y} C{qx + qw + 60} {y} {ax - 110} {ay} {ax - 50} {ay}", a, a + .06)
                 + _leg(f"M{ax - 50} {ay} C{ax - 110} {ay} {qx + qw + 60} {y} {qx + qw} {y}", a + .06, a + .12))
    y4 = ys[3] + qh / 2
    legs += _leg(f"M{qx + qw} {y4} C{qx + qw + 60} {y4} {ax - 110} {ay} {ax - 50} {ay}", .58, .63)
    # IT monitoring and control: the self-served share as a bar (no number), usage per space, the record
    mx, my, mw, mh = qx, sy + 348, sw - 32, 96
    tw, fw = 300, [90, 135, 180, 225]
    share = beat("width", [(0, fw[0]), (done[0], fw[0]), (done[0] + .01, fw[1]), (done[1], fw[1]), (done[1] + .01, fw[2]), (done[2], fw[2]),
                           (done[2] + .01, fw[3]), (.97, fw[3]), (1, fw[0])])
    band = (card(mx, my, mw, mh, "var(--dim)", "var(--line)", 14, 1.2) + T(mx + 16, my + 26, sl["monitor"], fit(sl["monitor"], 15, 440, "n14 monitor"), "var(--c4)", W6)
            + T(mx + 16, my + 54, sl["share"], fit(sl["share"], 15, 130, "n14 share"), "var(--white)", W6)
            + f'<rect x="{mx + 152}" y="{my + 44}" width="{tw}" height="10" rx="5" fill="var(--line)"/>'
            + f'<rect x="{mx + 152}" y="{my + 44}" width="{fw[3]}" height="10" rx="5" fill="{ok}">{share}</rect>'
            + T(mx + 16, my + 82, sl["usage"], fit(sl["usage"], 15, 130, "n14 usage"), "var(--white)", W6))
    for j, (w0, w1) in enumerate(((.7, .45), (.4, .75), (.55, .3))):
        x0 = mx + 152 + j * 104
        band += (f'<rect x="{x0}" y="{my + 72}" width="90" height="8" rx="4" fill="var(--line)"/>'
                 f'<rect x="{x0}" y="{my + 72}" width="{90 * w0:.0f}" height="8" rx="4" fill="var(--c2)">{loop("width", f"{90 * w0:.0f};{90 * w1:.0f};{90 * w0:.0f}", 5 + j, j)}</rect>')
    rx_ = mx + 492
    for j, row in enumerate(sl["rows"][:2]):
        yy = my + 54 + j * 28
        band += (f'<g>{loop("opacity", ".5;1;.5", 4, j * 1.5)}<circle cx="{rx_}" cy="{yy - 5}" r="8" fill="{ok}"/>{check(rx_, yy - 4, .45, "var(--ink)")}</g>'
                 + T(rx_ + 16, yy, row, fit(row, 15, mx + mw - rx_ - 28, "n14 record"), "var(--white)", W6))
    wall = (screen + land(head, .3, .4, 8) + seq(tickets, .35, .45, 12, 1.4) + land(space, .5, .5, 12) + land(band, .7, .5, 10)
            + calm + lit + ring + lock_on)
    ccx, ccy = sx + sw / 2, sy + sh / 2

    # the operator's tablet: the routed case arrives with its context, «Resolver», his tap, then resolved
    tap = (_swap([(0, 0), (t_ctx, 0), (t_ctx + .01, 1), (.97, 1), (1, 0)], bars(-48, -27, 92, 2, 12, "var(--accent)", ".9"))
           + _swap([(0, 0), (t_ctx, 0), (t_ctx + .01, 1), (t_back - .005, 1), (t_back, 0), (1, 0)], pill(0, 16, sl["review"], "var(--c4)", ctx, 15, 110, "n14 review", 12))
           + _swap([(0, 0), (t_back - .005, 0), (t_back, 1), (.97, 1), (1, 0)], f'<rect x="-34" y="4" width="68" height="24" rx="12" fill="{ok}"/>' + check(0, 17, .6, "var(--ink)"))
           + f'<circle cx="0" cy="16" r="6" fill="none" stroke="var(--white)" stroke-width="1.5" opacity="0">{beat("r", [(0, 6), (t_tap, 6), (t_tap + .08, 34), (1, 34)])}'
           f'{beat("opacity", [(0, 0), (t_tap, 0), (t_tap + .01, 1), (t_tap + .08, 0), (1, 0)])}</circle>')
    wmx, wmy, mnx, mny = 905, 676, 1250, 690
    tbx, tby = mnx + 112 + 16 * math.sin(math.radians(10)), mny + 62 + 16 * math.cos(math.radians(10))  # the tablet's button on stage
    route = (f"M{ax + 50} {ay} C{sx + sw - 10} {ay} {sx + sw - 8} {sy + sh - 60} {sx + sw - 8} {sy + sh} "
             f"C{sx + sw - 8} {sy + sh + 70} {tbx + 30:.0f} {tby - 110:.0f} {tbx - 8:.0f} {tby - 56:.0f}")
    # his decision rides back up, behind his head and left of the signature, to the ticket it closes
    back_d = f"M{tbx - 12:.0f} {tby - 56:.0f} C{tbx - 34:.0f} {tby - 128:.0f} {qx + qw + 24} {tby - 128:.0f} {qx + qw + 18} {sy + sh + 6} S{qx + qw + 4} {y4 + 30} {qx + qw + 2} {y4}"
    back = (f'<g opacity="0">{beat("opacity", [(0, 0), (t_back, 0), (t_back + .005, .9), (t_closed, .9), (t_closed + .03, 0), (1, 0)])}'
            f'<path d="{back_d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="1.5" stroke-linecap="round">'
            f'{beat("stroke-dashoffset", [(0, 1), (t_back, 1), (t_closed, 0), (1, 0)])}</path></g>' + _leg(back_d, t_back, t_closed))
    people = (f'<clipPath id="q14-desk"><rect x="760" y="0" width="840" height="{desk + 2}"/></clipPath>'
              f'<g clip-path="url(#q14-desk)">' + land(_n14_woman(wmx, wmy, 1.1, SKIN_BROWN, "var(--accent)"), .25, .6, 40)
              + land(_n14_man(mnx, mny, 1.0, SKIN_LIGHT, "var(--c1)", tap), .4, .6, 40) + '</g>')
    leds = "".join(f'<circle cx="{860 + k * 26}" cy="{desk + 19}" r="2.2" fill="var(--c2)" opacity=".45"/>' for k in range(8))
    status = (_swap([(0, 0), (t_route, 0), (t_route + .01, 1), (t_closed, 1), (t_closed + .01, 0), (1, 0)], f'<rect x="1336" y="{desk + 15}" width="120" height="8" rx="4" fill="var(--accent)"/>')
              + _swap([(0, 0), (t_calm, 0), (t_calm + .02, 1), (.97, 1), (1, 0)], f'<rect x="1336" y="{desk + 15}" width="120" height="8" rx="4" fill="{ok}"/>'))
    console = land(f'<path d="M820 {desk} H1560 L1548 830 H832 Z" fill="var(--card)"/>'
                   f'<rect x="1336" y="{desk + 15}" width="120" height="8" rx="4" fill="var(--line)"/>'
                   f'<path d="M820 {desk} H1560" stroke="var(--c2)" stroke-width="1.5" opacity=".7"/>'
                   f'<path d="M820 {desk + 1} H1560" stroke="var(--c2)" stroke-width="6" opacity=".08"/>' + leds + status, .2, .5, 20)
    sign = T(sx + sw, sy + sh + 36, sl["sign"], fit(sl["sign"], 20, 330, "n14 sign"), "var(--c4)", 'text-anchor="end" font-weight="600"')
    return (g[0] + land(cone, .2, .6, 0) + pop(f'<g transform="translate({-ccx} {-ccy})">{wall}</g>', ccx, ccy, .05, .6)
            + legs + land(sign, 1.4, .45, 10) + back + people + _leg(route, t_route, t_ctx) + console), D, FREEZE

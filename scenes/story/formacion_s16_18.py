"""Bench f, slides 16-18 of the class deck.
v16_entrega  the skill's pipeline: Construye (four slides fill with their scene), Revisa (five checks light under a
             scan line), Entrega (two files drop out, each «Se abre sin internet"); a faceless presenter steps forward
             holding the file: «Tú presentas».
v17_turno    a desk, a laptop with the skill open, a 15-minute timer ring that fills; three steps check in order on the
             screen and «Títulos aprobados» stays highlighted.
v18_parejas  two faceless people face each other; one reads a short list of titles (speech waves), three 40 s timers
             fill in turn (leer, reformular, compromiso); the listener asks one «?», says the story back (a thread
             from the list lights), and the note «Cliente · fecha · conversación» is written."""


def _v16_on(a, lo=0, hi=1, f=.02):
    """Opacity lo until fraction a, hi from a until the reset."""
    return beat("opacity", [(0, lo), (a, lo), (a + f, hi), (.97, hi), (1, lo)])


def _v16_win(a, b, f=.02):
    """Visible between fractions a and b only."""
    return beat("opacity", [(0, 0), (a, 0), (a + f, 1), (b, 1), (b + f, 0), (1, 0)])


def _v16_slide(a, dx, dy, f=.04):
    """Translate from (dx, dy) to rest at fraction a, back at the reset."""
    return (f'<animateTransform attributeName="transform" type="translate" values="{dx} {dy};{dx} {dy};0 0;0 0;{dx} {dy}" '
            f'keyTimes="0;{a:.3f};{a + f:.3f};.97;1" dur="{D}s" repeatCount="indefinite"/>')


def _v16_hop(path, a, b, color="var(--c4)", r=6):
    """A token that runs path between fractions a and b, then hides."""
    return (f'<g>{beat("opacity", [(0, 0), (a, 0), (a + .005, 1), (b, 1), (b + .01, 0), (1, 0)])}{token(color, r)}'
            f'{move(path, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}</g>')


def _v16_ring(cx, cy, r, a, b, color="var(--c4)", sw=5, p=1.0):
    """A timer ring: a dim track, and an arc that fills p of the circle between fractions a and b and holds."""
    end = round(1 - p, 3)
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="var(--dim)" stroke-width="{sw}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="{sw}" pathLength="1" '
            f'stroke-dasharray="1" transform="rotate(-90 {cx} {cy})">'
            + beat("stroke-dashoffset", [(0, 1), (a, 1), (b, end), (.97, end), (1, 1)]) + '</circle>')


def _v16_badge(x, y, a, ok, r=13):
    """The ok badge with its check: appears at a and holds."""
    return f'<g>{_v16_on(a)}<circle cx="{x}" cy="{y}" r="{r}" fill="{ok}"/>{check(x, y + 1, r / 15, "var(--ink)")}</g>'


def _v16_label(x, y, text, size, room, where, fill="var(--white)", extra=W6):
    """A label that shrinks to fit its room but never under 15 px."""
    return T(x, y, text, fit(text, size, room, where, floor=15), fill, extra)


def _v16_file(x, y, w, name, sub, offline, ctx, accent):
    """An output file card: a page icon, its name, what it carries and the «opens offline» tag."""
    icon = (f'<path d="M{x + w - 44} {y + 16} h18 l10 10 v26 h-28 Z" fill="none" stroke="{accent}" stroke-width="1.6" stroke-linejoin="round"/>'
            f'<path d="M{x + w - 26} {y + 16} v10 h10" fill="none" stroke="{accent}" stroke-width="1.6"/>')
    return (card(x, y, w, 150, "var(--card)", accent, 14, 1.6) + icon
            + _v16_label(x + 16, y + 40, name, 18, w - 70, "entrega file name")
            + _v16_label(x + 16, y + 68, sub, 16, w - 32, "entrega file sub", "var(--muted)", "")
            + pill(x + w / 2, y + 116, offline, "var(--c2)", ctx, 15, w - 20, "entrega offline"))


def _v16_glyph(k, x, y, w, h):
    """The scene a built slide shows (k 0-3): people, a rising line, bars, a thread of three stops."""
    c = "var(--c4)"
    if k == 0:
        return "".join(_user(x + w * f, y + h * .62, .75, c) for f in (.3, .5, .7))
    if k == 1:
        return f'<path d="M{x + 12} {y + h - 10} L{x + w * .35:.0f} {y + h * .55:.0f} L{x + w * .6:.0f} {y + h * .7:.0f} L{x + w - 12} {y + 10}" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
    if k == 2:
        return "".join(f'<rect x="{x + 16 + i * (w - 32) / 4:.0f}" y="{y + h - 8 - hh:.0f}" width="{(w - 32) / 4 - 10:.0f}" height="{hh:.0f}" rx="3" fill="{c}" opacity=".85"/>'
                       for i, hh in enumerate((h * .3, h * .5, h * .42, h * .72)))
    return (f'<path d="M{x + 20} {y + h / 2} H{x + w - 20}" stroke="{c}" stroke-width="1.6"/>'
            + "".join(f'<circle cx="{x + 20 + i * (w - 40) / 2:.0f}" cy="{y + h / 2}" r="7" fill="{c}"/>' for i in range(3)))


# ---------------------------------------------------------------- 16 · the skill builds, checks and delivers; you present
@register("scene", "v16_entrega")
def sc_v16_entrega(sl, ctx):
    """Construye: four empty slides fill with their scene, one by one. Revisa: a scan line runs down five checks and
    each turns green. Entrega: two files drop out, each tagged «Se abre sin internet». Then a faceless presenter steps
    forward into the light holding the file: «Tú presentas». Frozen: all checks green, two files, presenter."""
    if ORIENT() == "portrait":
        return _pv16_entrega(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    g = [glow(1190, 420, 470, "var(--brand)", .45)]
    heads = sl["phases"]
    cols = ((830, 180), (1034, 290), (1340, 220))    # x, width of Construye · Revisa · Entrega
    top, bot = 160, 548
    lit = (.03, .27, .57)
    # stage headers: dim, then each lights when its turn comes and stays lit. The light (a glow and a yellow ring) is
    # painted before the pill, so nothing covers the label and it reads white on the dim pill in both states.
    for (x, w), head, a in zip(cols, heads, lit):
        cx = x + w / 2
        s = fit(head, 18, w - 36, "entrega stage")
        pw, ph = min(w, bold_width(_(str(head)), s, current_factor()) + 36) + 8, s + 28
        g.append(f'<g>{_v16_on(a)}{glow(cx, 116, pw * .6, "var(--c4)", .35)}'
                 f'<rect x="{cx - pw / 2:.1f}" y="{116 - ph / 2}" width="{pw:.1f}" height="{ph}" rx="{ph / 2}" fill="none" stroke="var(--c4)" stroke-width="2"/></g>')
        g.append(land(pill(cx, 116, head, "var(--dim)", ctx, 18, w, "entrega stage"), .1, .5))
    for x, a in ((1022, .25), (1332, .55)):          # chevrons between stages flash as the work passes
        chev = f'<path d="M{x - 5} 106 L{x + 4} 116 L{x - 5} 126" fill="none" stroke="var(--c2)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
        g.append(land(chev, .3, .4))
        g.append(f'<g>{beat("opacity", [(0, 0), (a, 0), (a + .01, 1), (a + .04, 1), (a + .06, 0), (1, 0)])}{glow(x, 116, 26, "var(--c4)", .9)}</g>')
    # ---- Construye: four slides, each fills with its scene
    x0, w0 = cols[0]
    th, gap = 86, 14
    frames = ""
    for k in range(4):
        y = top + k * (th + gap)
        frames += (card(x0, y, w0, th, "var(--dim)", "var(--line)", 10, 1.4)
                   + f'<rect x="{x0 + 12}" y="{y + 12}" width="{w0 * .45:.0f}" height="6" rx="3" fill="var(--c2)" opacity=".5"/>'
                   + f'<rect x="{x0 + 12}" y="{y + 26}" width="{w0 - 24}" height="{th - 38}" rx="6" fill="none" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="5 5" opacity=".6"/>')
    g.append(land(frames, .2, .5))
    for k in range(4):
        y = top + k * (th + gap)
        a = .05 + k * .05
        g.append(f'<g>{_v16_on(a)}{card(x0, y, w0, th, "var(--card)", "var(--c4)", 10, 1.4)}'
                 f'<rect x="{x0 + 12}" y="{y + 12}" width="{w0 * .45:.0f}" height="6" rx="3" fill="var(--c2)"/>'
                 f'{_v16_glyph(k, x0 + 12, y + 26, w0 - 24, th - 38)}</g>')
        g.append(f'<g>{_v16_win(a, a + .04)}{spark(x0 + w0 - 16, y + 16, .55, "var(--c4)")}</g>')
    # ---- Revisa: five checks under a scan line
    x1, w1 = cols[1]
    g.append(land(card(x1, top, w1, bot - top, "var(--card)", "var(--line)", 14, 1.4), .3, .5))
    checks = sl["checks"]
    rows = ""
    for k, lab in enumerate(checks):
        y = top + 50 + k * 72
        rows += (f'<circle cx="{x1 + 30}" cy="{y}" r="13" fill="none" stroke="var(--c2)" stroke-width="1.6" opacity=".7"/>'
                 + _v16_label(x1 + 54, y + 6, lab, 17, w1 - 66, "entrega check"))
        g.append(_v16_badge(x1 + 30, y, .31 + k * .05, ok))
    # the scan band is painted under the labels
    scan = (f'<g><rect x="{x1 + 10}" y="-26" width="{w1 - 20}" height="52" rx="10" fill="var(--c4)" opacity=".13"/>'
            f'<rect x="{x1 + 10}" y="-26" width="4" height="52" rx="2" fill="var(--c4)"/>'
            f'<animateTransform attributeName="transform" type="translate" values="0 {top + 50};0 {top + 50};0 {top + 50 + 4 * 72};0 {top + 50 + 4 * 72}" '
            f'keyTimes="0;.29;.53;1" dur="{D}s" repeatCount="indefinite"/></g>')
    g.append(f'<g>{_v16_win(.29, .54)}{scan}</g>')
    g.append(land(rows, .4, .5))
    # ---- Entrega: two files drop out
    x2, w2 = cols[2]
    g.append(land(card(x2, top, w2, bot - top, "none", "var(--line)", 14, 1.4, 'stroke-dasharray="6 6"'), .5, .5))
    for k, ((name, sub), a, acc) in enumerate(zip(sl["files"], (.60, .67), ("var(--c4)", "var(--c2)"))):
        y = top + 26 + k * 184
        g.append(f'<g>{_v16_on(a)}<g>{_v16_slide(a, 0, -34)}{_v16_file(x2, y, w2, name, sub, sl["offline"], ctx, acc)}</g></g>')
    # ---- the presenter steps forward with the file
    px, py = 1080, 706
    g.append(f'<g>{_v16_on(.74, f=.04)}{glow(px, py - 20, 190, "var(--c4)", .3)}</g>')
    bust = f'<g transform="translate({px} {py}) scale(1.9)">{_n10_bust(SKIN_BROWN, "var(--accent)", _N10_HAIR2, "long")}</g>'
    held = (card(px + 30, py + 44, 190, 44, "var(--card)", "var(--c4)", 10, 1.6)
            + _v16_label(px + 46, py + 72, sl["files"][0][0], 16, 160, "entrega held file"))
    g.append(f'<g>{_v16_on(.74, f=.04)}<g>{_v16_slide(.74, 70, 14, .06)}{bust}</g></g>')
    g.append(f'<g>{_v16_on(.80)}{held}</g>')
    g.append(_v16_hop(f"M{x2 + 60} {top + 176} C{x2 + 40} {top + 420} {px + 260} {py + 20} {px + 130} {py + 66}", .75, .80))
    g.append(f'<g>{_v16_on(.82)}<g>{_v16_slide(.82, 0, 12)}{pill(1400, 700, sl["you"], "var(--c4)", ctx, 22, 280, "entrega you")}</g></g>')
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 17 · your next prospect, in fifteen minutes
@register("scene", "v17_turno")
def sc_v17_turno(sl, ctx):
    """A desk and a laptop with the skill open; a 15-minute timer ring fills through the loop. On the screen three
    steps work and check in order: a real client of this month, context and facts, approved titles; the last one
    stays highlighted. Frozen: timer near full, three steps checked, «Títulos aprobados» highlighted."""
    if ORIENT() == "portrait":
        return _pv17_turno(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    g = [glow(1100, 400, 440, "var(--brand)", .45)]
    # desk
    desk = (f'<rect x="822" y="640" width="736" height="16" rx="6" fill="var(--dim)" stroke="var(--line)" stroke-width="1.2"/>'
            f'<path d="M870 656 V800 M1510 656 V800" stroke="var(--line)" stroke-width="2" stroke-linecap="round"/>'
            # a mug and a notebook
            f'<path d="M1416 584 h56 v44 a12 12 0 0 1 -12 12 h-32 a12 12 0 0 1 -12 -12 Z" fill="var(--card)" stroke="var(--c2)" stroke-width="1.6"/>'
            f'<path d="M1472 596 a13 13 0 0 1 0 26" fill="none" stroke="var(--c2)" stroke-width="1.6"/>'
            f'<path d="M1432 570 q6 -8 0 -16 M1452 570 q6 -8 0 -16" fill="none" stroke="var(--c2)" stroke-width="1.4" stroke-linecap="round" opacity=".6"/>'
            f'<rect x="1494" y="618" width="60" height="22" rx="4" fill="var(--card)" stroke="var(--c2)" stroke-width="1.4" transform="rotate(-6 1524 629)"/>')
    g.append(land(desk, .1, .5))
    # laptop
    sx, sy, sw, sh = 840, 200, 520, 400
    lap = (card(sx, sy, sw, sh, "var(--ink)", "var(--c2)", 18, 1.6)
           + card(sx + 14, sy + 14, sw - 28, sh - 28, "var(--card)", "var(--line)", 10, 1)
           + f'<path d="M{sx - 14} {sy + sh + 24} L{sx + 6} {sy + sh} H{sx + sw - 6} L{sx + sw + 14} {sy + sh + 24} Z" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.6" stroke-linejoin="round"/>'
           + f'<path d="M{sx + sw / 2 - 40} {sy + sh + 12} H{sx + sw / 2 + 40}" stroke="var(--c2)" stroke-width="1.6" stroke-linecap="round" opacity=".6"/>'
           # the skill's header bar
           + f'<path d="M{sx + 14} {sy + 70} H{sx + sw - 14}" stroke="var(--line)" stroke-width="1.2"/>'
           + spark(sx + 44, sy + 42, .7, "var(--c4)")
           + _v16_label(sx + 66, sy + 50, sl["app"], 20, sw - 170, "turno app")
           + "".join(f'<circle cx="{sx + sw - 40 - k * 16}" cy="{sy + 42}" r="4" fill="var(--c2)" opacity=".5"/>' for k in range(3)))
    g.append(land(lap, .2, .55))
    # three steps on the screen
    rx, rw, rh = sx + 36, sw - 72, 76
    done = (.22, .47, .72)
    for k, (lab, a) in enumerate(zip(sl["steps"], done)):
        y = sy + 100 + k * 94
        row = (card(rx, y, rw, rh, "var(--dim)", "var(--line)", 12, 1.2)
               + f'<circle cx="{rx + 34}" cy="{y + rh / 2}" r="15" fill="none" stroke="var(--c2)" stroke-width="1.6"/>'
               + _v16_label(rx + 64, y + rh / 2 + 8, lab, 22, rw - 84, "turno step"))
        g.append(land(row, .4 + k * .12, .5))
        start = done[k - 1] if k else .03
        dots = "".join(f'<circle cx="{rx + rw - 60 + j * 16}" cy="{y + rh / 2}" r="4" fill="var(--c4)">{loop("opacity", ".2;1;.2", 1.2, j * .3)}</circle>' for j in range(3))
        g.append(f'<g>{_v16_win(start, a - .01)}<rect x="{rx}" y="{y}" width="5" height="{rh}" rx="2.5" fill="var(--c4)"/>{dots}</g>')
        g.append(f'<g>{_v16_on(a)}<rect x="{rx}" y="{y}" width="{rw}" height="{rh}" rx="12" fill="none" stroke="var(--c2)" stroke-width="1.6"/></g>')
        g.append(_v16_badge(rx + 34, y + rh / 2, a, ok, 15))
    # the goal stays highlighted
    y3 = sy + 100 + 2 * 94
    g.append(f'<g>{_v16_on(.75)}{glow(rx + rw / 2, y3 + rh / 2, 220, "var(--c4)", .28)}'
             f'<rect x="{rx - 4}" y="{y3 - 4}" width="{rw + 8}" height="{rh + 8}" rx="14" fill="none" stroke="var(--c4)" stroke-width="2">'
             f'{loop("stroke-opacity", ".55;1;.55", 2.4)}</rect>'
             f'<g>{loop("opacity", ".5;1;.5", 2.2)}{spark(rx + rw - 18, y3 + 12, .6, "var(--c4)")}</g></g>')
    # the timer ring: fills through the loop, the label never moves
    tx, ty, tr = 1462, 214, 74
    g.append(land(f'<circle cx="{tx}" cy="{ty}" r="{tr + 16}" fill="var(--card)" stroke="var(--line)" stroke-width="1.2"/>'
                  + "".join(f'<path d="M{tx + (tr + 9) * math.sin(k * math.pi / 6):.1f} {ty - (tr + 9) * math.cos(k * math.pi / 6):.1f} '
                            f'L{tx + (tr + 13) * math.sin(k * math.pi / 6):.1f} {ty - (tr + 13) * math.cos(k * math.pi / 6):.1f}" stroke="var(--c2)" stroke-width="1.4"/>' for k in range(12))
                  + _v16_ring(tx, ty, tr, .02, .88, "var(--c4)", 7, .94)
                  + TC(tx, ty + 12, sl["timer"], fit(sl["timer"], 32, tr * 1.6, "turno timer", floor=15), "var(--white)", 'font-weight="700"'), .1, .5))
    return "".join(g), D, FREEZE


def _v18_waves(x, y, d, a, b):
    """Three speech arcs opening toward direction d (1 right, -1 left), pulsing between fractions a and b."""
    arcs = "".join(f'<path d="M{x + d * k * 14} {y - 10 - k * 7} q{d * (8 + k * 3)} {10 + k * 7} 0 {20 + k * 14}" fill="none" stroke="var(--c4)" '
                   f'stroke-width="1.8" stroke-linecap="round">{loop("opacity", ".15;1;.15", 1.2, k * .3)}</path>' for k in range(3))
    return f'<g>{_v16_win(a, b)}{arcs}</g>'


# ---------------------------------------------------------------- 18 · read your titles to someone: does it land?
@register("scene", "v18_parejas")
def sc_v18_parejas(sl, ctx):
    """Two faceless people face each other over the list of titles. Timer 1 «leer»: the reader's speech waves run and
    each title lights as it is read; the listener asks one «?». Timer 2 «reformular»: the listener says the story back,
    a thread from the list to the listener lights and a check «Se entiende» lands. Timer 3 «compromiso»: the note
    «Cliente · fecha · conversación» is written. Frozen: three timers done, story understood, the note."""
    if ORIENT() == "portrait":
        return _pv18_parejas(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    g = [glow(1190, 520, 440, "var(--brand)", .45)]
    # three 40-second timers, in turn
    phases = ((.04, .30), (.34, .60), (.64, .88))
    for k, (lab, (a, b)) in enumerate(zip(sl["timers"], phases)):
        cx, cy = 945 + k * 245, 148
        g.append(land(_v16_ring(cx, cy, 30, a, b, "var(--c4)", 5)
                      + _v16_label(cx, 214, lab, 17, 230, "parejas timer", extra=W6 + ' text-anchor="middle"'), .1 + k * .12, .5))
        g.append(_v16_badge(cx, cy, b, ok, 14))
    # the two people: the reader faces right, the listener (mirrored) faces left
    lx, rxp, py, s = 930, 1450, 640, 2.2
    reader = f'<g transform="translate({lx} {py}) scale({s})">{_n10_bust(SKIN_LIGHT, "var(--c1)", HAIR, "long")}</g>'
    # ponytail: the listener reuses the short-haired bust without its headset (cut at the headset path)
    listener_bust = _n10_bust(SKIN_BROWN, "var(--accent)", _N10_HAIR2, "short").split('<path d="M-15 -22')[0]
    listener = f'<g transform="translate({rxp} {py}) scale({-s} {s})">{listener_bust}</g>'
    table = f'<path d="M830 776 H1550" stroke="var(--line)" stroke-width="2" stroke-linecap="round"/>'
    halos = glow(lx + 10, py - 60, 130, "var(--c2)", .3) + glow(rxp - 10, py - 60, 130, "var(--c2)", .3)
    g.append(land(halos + table + reader + listener, .2, .55))
    # the list of titles between them
    shx, shy, shw, shh = 1060, 640, 260, 132
    sheet = (card(shx, shy, shw, shh, "var(--card)", "var(--c2)", 12, 1.4)
             + _v16_label(shx + 16, shy + 28, sl["list_label"], 16, shw - 32, "parejas list label", "var(--muted)")
             + "".join(_v16_label(shx + 16, shy + 56 + i * 26, t, 16, shw - 32, "parejas title") for i, t in enumerate(sl["list"])))
    g.append(land(sheet, .4, .5))
    for i in range(len(sl["list"])):   # each title lights as it is read
        yy = shy + 56 + i * 26
        a = .07 + i * .07
        g.append(f'<g>{_v16_win(a, a + .07)}<rect x="{shx + 8}" y="{yy - 17}" width="{shw - 16}" height="24" rx="6" fill="var(--c4)" opacity=".22"/></g>')
    # speech waves: the reader reads (timer 1), the listener says it back (timer 2)
    g.append(_v18_waves(lx + 60, py - 40, 1, .05, .29))
    g.append(_v18_waves(rxp - 60, py - 40, -1, .36, .58))
    # one question from the listener
    qx, qy = rxp - 10, py - 172
    q = (f'<path d="M{qx - 30} {qy - 30} h60 a14 14 0 0 1 14 14 v32 a14 14 0 0 1 -14 14 h-24 l-10 14 l-4 -14 h-22 a14 14 0 0 1 -14 -14 v-32 a14 14 0 0 1 14 -14 Z" '
         f'fill="var(--card)" stroke="var(--c4)" stroke-width="1.6"/>' + TC(qx, qy + 12, "?", 32, "var(--c4)", 'font-weight="700"'))
    g.append(f'<g>{_v16_win(.24, .52)}<g>{_v16_slide(.24, 0, 10)}{q}</g></g>')
    # the story comes back: a thread from the list to the listener, then the check
    thread = f"M{shx + shw} {shy + 60} C{shx + shw + 60} {shy + 40} {rxp - 110} {py - 20} {rxp - 66} {py - 44}"
    g.append(f'<path d="{thread}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="1.8">'
             + beat("stroke-dashoffset", [(0, 1), (.38, 1), (.50, 0), (.97, 0), (1, 1)]) + '</path>')
    g.append(_v16_hop(thread, .38, .50))
    g.append(f'<g>{_v16_on(.54)}<g>{_v16_slide(.54, 0, 10)}{pill(qx - 14, qy, sl["understood"], ok, ctx, 18, 200, "parejas understood")}</g></g>')
    # the commitment note is written
    nx, ny, nw, nh = 1030, 272, 320, 140
    note = (card(nx, ny, nw, nh, "var(--card)", "var(--c4)", 12, 1.6)
            + _v16_label(nx + 18, ny + 34, sl["note"], 17, nw - 36, "parejas note"))
    g.append(f'<g>{_v16_on(.64)}<g>{_v16_slide(.64, 0, 14)}{note}</g></g>')
    for i in range(3):
        w = (nw - 36) * (.85, .7, .9)[i]
        g.append(f'<path d="M{nx + 18} {ny + 64 + i * 24} h{w:.0f}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c2)" stroke-width="2" stroke-linecap="round">'
                 + beat("stroke-dashoffset", [(0, 1), (.68 + i * .06, 1), (.72 + i * .06, 0), (.97, 0), (1, 1)]) + '</path>')
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- portrait twins (900x1600 stage, art zone below y 640)
def _pv_label(x, y, text, size, room, where, fill="var(--white)", extra=W6):
    """A portrait label: fits its room, never under 18 px."""
    return T(x, y, text, fit(text, size, room, where, floor=18), fill, extra)


def _pv16_file(x, y, w, h, name, sub, offline, ctx, accent):
    """_v16_file at phone size."""
    icon = (f'<path d="M{x + w - 50} {y + 18} h22 l12 12 v30 h-34 Z" fill="none" stroke="{accent}" stroke-width="1.8" stroke-linejoin="round"/>'
            f'<path d="M{x + w - 28} {y + 18} v12 h12" fill="none" stroke="{accent}" stroke-width="1.8"/>')
    return (card(x, y, w, h, "var(--card)", accent, 14, 1.8) + icon
            + _pv_label(x + 18, y + 44, name, 24, w - 80, "entrega file name")
            + _pv_label(x + 18, y + 76, sub, 21, w - 36, "entrega file sub", "var(--muted)", "")
            + pill(x + w / 2, y + h - 36, offline, "var(--c2)", ctx, 20, w - 24, "entrega offline"))


def _pv16_entrega(sl, ctx):
    """v16 stacked: Construye (a 2x2 of slides) beside Revisa (five checks under the scan line), Entrega below with the
    two files side by side, the presenter at the bottom with the file and «Tú presentas». Same beats as desktop."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    g = [glow(zx + zw / 2, zy + 420, 470, "var(--brand)", .45)]
    heads = sl["phases"]
    top, bot = zy + 76, zy + 456                       # row A: Construye | Revisa
    x0, w0 = zx, 370
    x1, w1 = zx + 390, zw - 390
    fy = bot + 64                                      # row B: Entrega
    hdr = ((x0 + w0 / 2, zy + 34, w0), (x1 + w1 / 2, zy + 34, w1), (zx + zw / 2, bot + 34, 360))
    for (cx, cy, room), head, a in zip(hdr, heads, (.03, .27, .57)):
        s = fit(head, 24, room - 40, "entrega stage", floor=18)
        pw, ph = min(room, bold_width(_(str(head)), s, current_factor()) + 40) + 8, s + 28
        g.append(f'<g>{_v16_on(a)}{glow(cx, cy, pw * .6, "var(--c4)", .35)}'
                 f'<rect x="{cx - pw / 2:.1f}" y="{cy - ph / 2}" width="{pw:.1f}" height="{ph}" rx="{ph / 2}" fill="none" stroke="var(--c4)" stroke-width="2"/></g>')
        g.append(land(pill(cx, cy, head, "var(--dim)", ctx, 24, room, "entrega stage"), .1, .5))
    chevs = ((x0 + w0 + 10, zy + 34, 0, .25), (zx + zw / 2 - 110, bot + 34, 90, .55))
    for x, y, rot, a in chevs:
        chev = f'<path d="M{x - 6} {y - 12} L{x + 5} {y} L{x - 6} {y + 12}" fill="none" stroke="var(--c2)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" transform="rotate({rot} {x} {y})"/>'
        g.append(land(chev, .3, .4))
        g.append(f'<g>{beat("opacity", [(0, 0), (a, 0), (a + .01, 1), (a + .04, 1), (a + .06, 0), (1, 0)])}{glow(x, y, 30, "var(--c4)", .9)}</g>')
    # ---- Construye: a 2x2 of slides, each fills with its scene
    tw, th, gap = (w0 - 14) / 2, (bot - top - 14) / 2, 14
    pos = [(x0 + (k % 2) * (tw + gap), top + (k // 2) * (th + gap)) for k in range(4)]
    frames = "".join(card(x, y, tw, th, "var(--dim)", "var(--line)", 12, 1.4)
                     + f'<rect x="{x + 14}" y="{y + 16}" width="{tw * .5:.0f}" height="8" rx="4" fill="var(--c2)" opacity=".5"/>'
                     + f'<rect x="{x + 14}" y="{y + 36}" width="{tw - 28:.0f}" height="{th - 52:.0f}" rx="8" fill="none" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="5 5" opacity=".6"/>'
                     for x, y in pos)
    g.append(land(frames, .2, .5))
    for k, (x, y) in enumerate(pos):
        a = .05 + k * .05
        g.append(f'<g>{_v16_on(a)}{card(x, y, tw, th, "var(--card)", "var(--c4)", 12, 1.6)}'
                 f'<rect x="{x + 14}" y="{y + 16}" width="{tw * .5:.0f}" height="8" rx="4" fill="var(--c2)"/>'
                 f'{_v16_glyph(k, x + 14, y + 36, tw - 28, th - 52)}</g>')
        g.append(f'<g>{_v16_win(a, a + .04)}{spark(x + tw - 20, y + 20, .7, "var(--c4)")}</g>')
    # ---- Revisa: five checks under a scan line
    g.append(land(card(x1, top, w1, bot - top, "var(--card)", "var(--line)", 14, 1.4), .3, .5))
    rows, step = "", (bot - top - 60) / 4
    for k, lab in enumerate(sl["checks"]):
        y = top + 30 + k * step
        rows += (f'<circle cx="{x1 + 32}" cy="{y:.1f}" r="15" fill="none" stroke="var(--c2)" stroke-width="1.8" opacity=".7"/>'
                 + _pv_label(x1 + 60, y + 8, lab, 22, w1 - 74, "entrega check"))
        g.append(_v16_badge(x1 + 32, round(y, 1), .31 + k * .05, ok, 15))
    y0, y4 = top + 30, top + 30 + 4 * step
    scan = (f'<g><rect x="{x1 + 10}" y="-28" width="{w1 - 20}" height="56" rx="10" fill="var(--c4)" opacity=".13"/>'
            f'<rect x="{x1 + 10}" y="-28" width="4" height="56" rx="2" fill="var(--c4)"/>'
            f'<animateTransform attributeName="transform" type="translate" values="0 {y0};0 {y0};0 {y4:.0f};0 {y4:.0f}" '
            f'keyTimes="0;.29;.53;1" dur="{D}s" repeatCount="indefinite"/></g>')
    g.append(f'<g>{_v16_win(.29, .54)}{scan}</g>')
    g.append(land(rows, .4, .5))
    # ---- Entrega: two files drop out, side by side
    g.append(land(card(zx, fy, zw, 196, "none", "var(--line)", 14, 1.4, 'stroke-dasharray="6 6"'), .5, .5))
    fw = (zw - 36) / 2
    for k, ((name, sub), a, acc) in enumerate(zip(sl["files"], (.60, .67), ("var(--c4)", "var(--c2)"))):
        g.append(f'<g>{_v16_on(a)}<g>{_v16_slide(a, 0, -34)}{_pv16_file(zx + 12 + k * (fw + 12), fy + 12, fw, 172, name, sub, sl["offline"], ctx, acc)}</g></g>')
    # ---- the presenter steps forward with the file
    px, py = zx + 170, zy + 796
    g.append(f'<g>{_v16_on(.74, f=.04)}{glow(px, py - 20, 170, "var(--c4)", .3)}</g>')
    bust = f'<g transform="translate({px} {py}) scale(1.4)">{_n10_bust(SKIN_BROWN, "var(--accent)", _N10_HAIR2, "long")}</g>'
    hx, hw = px + 44, 290
    held = card(hx, py + 20, hw, 54, "var(--card)", "var(--c4)", 12, 1.8) + _pv_label(hx + 18, py + 55, sl["files"][0][0], 22, hw - 36, "entrega held file")
    g.append(f'<g>{_v16_on(.74, f=.04)}<g>{_v16_slide(.74, 70, 14, .06)}{bust}</g></g>')
    g.append(f'<g>{_v16_on(.80)}{held}</g>')
    g.append(_v16_hop(f"M{zx + 12 + fw / 2:.0f} {fy + 184} C{zx + 60} {fy + 260} {hx + 260} {py - 30} {hx + 150} {py + 20}", .75, .80))
    g.append(f'<g>{_v16_on(.82)}<g>{_v16_slide(.82, 0, 12)}{pill(zx + zw - 150, py - 50, sl["you"], "var(--c4)", ctx, 28, 290, "entrega you")}</g></g>')
    return portrait_mark("".join(g)), D, FREEZE


def _pv17_turno(sl, ctx):
    """v17 stacked: the 15-minute timer on top, the laptop with the skill and its three steps below, on the desk with
    the mug and the notebook. Same beats: steps check in order, «Títulos aprobados» stays highlighted."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    g = [glow(zx + zw / 2, zy + 460, 440, "var(--brand)", .45)]
    dy = zy + 810                                      # desk top
    desk = (f'<rect x="{zx}" y="{dy}" width="{zw}" height="16" rx="6" fill="var(--dim)" stroke="var(--line)" stroke-width="1.2"/>'
            f'<path d="M{zx + 50} {dy + 16} V{dy + 70} M{zx + zw - 50} {dy + 16} V{dy + 70}" stroke="var(--line)" stroke-width="2" stroke-linecap="round"/>'
            f'<g transform="translate({zx + zw - 112} {dy - 56})">'
            f'<path d="M0 0 h48 v40 a10 10 0 0 1 -10 10 h-28 a10 10 0 0 1 -10 -10 Z" transform="translate(0 6)" fill="var(--card)" stroke="var(--c2)" stroke-width="1.6"/>'
            f'<path d="M48 16 a12 12 0 0 1 0 24" fill="none" stroke="var(--c2)" stroke-width="1.6"/>'
            f'<path d="M14 -2 q6 -8 0 -16 M32 -2 q6 -8 0 -16" fill="none" stroke="var(--c2)" stroke-width="1.4" stroke-linecap="round" opacity=".6"/></g>'
            f'<rect x="{zx + zw - 58}" y="{dy - 20}" width="56" height="20" rx="4" fill="var(--card)" stroke="var(--c2)" stroke-width="1.4" transform="rotate(-6 {zx + zw - 30} {dy - 10})"/>')
    g.append(land(desk, .1, .5))
    # laptop
    sx, sy, sw, sh = zx + 20, zy + 250, 640, 520
    lap = (card(sx, sy, sw, sh, "var(--ink)", "var(--c2)", 18, 1.6)
           + card(sx + 14, sy + 14, sw - 28, sh - 28, "var(--card)", "var(--line)", 10, 1)
           + f'<path d="M{sx - 14} {dy} L{sx + 6} {sy + sh} H{sx + sw - 6} L{sx + sw + 14} {dy} Z" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.6" stroke-linejoin="round"/>'
           + f'<path d="M{sx + 14} {sy + 84} H{sx + sw - 14}" stroke="var(--line)" stroke-width="1.2"/>'
           + spark(sx + 50, sy + 49, .9, "var(--c4)")
           + _pv_label(sx + 78, sy + 58, sl["app"], 26, sw - 190, "turno app")
           + "".join(f'<circle cx="{sx + sw - 44 - k * 18}" cy="{sy + 49}" r="5" fill="var(--c2)" opacity=".5"/>' for k in range(3)))
    g.append(land(lap, .2, .55))
    rx, rw, rh = sx + 36, sw - 72, 104
    done = (.22, .47, .72)
    ys = [sy + 116 + k * 128 for k in range(3)]
    for k, (lab, a, y) in enumerate(zip(sl["steps"], done, ys)):
        row = (card(rx, y, rw, rh, "var(--dim)", "var(--line)", 12, 1.2)
               + f'<circle cx="{rx + 38}" cy="{y + rh / 2}" r="18" fill="none" stroke="var(--c2)" stroke-width="1.8"/>'
               + _pv_label(rx + 72, y + rh / 2 + 9, lab, 26, rw - 150, "turno step"))
        g.append(land(row, .4 + k * .12, .5))
        start = done[k - 1] if k else .03
        dots = "".join(f'<circle cx="{rx + rw - 58 + j * 18}" cy="{y + rh / 2}" r="5" fill="var(--c4)">{loop("opacity", ".2;1;.2", 1.2, j * .3)}</circle>' for j in range(3))
        g.append(f'<g>{_v16_win(start, a - .01)}<rect x="{rx}" y="{y}" width="6" height="{rh}" rx="3" fill="var(--c4)"/>{dots}</g>')
        g.append(f'<g>{_v16_on(a)}<rect x="{rx}" y="{y}" width="{rw}" height="{rh}" rx="12" fill="none" stroke="var(--c2)" stroke-width="1.8"/></g>')
        g.append(_v16_badge(rx + 38, y + rh / 2, a, ok, 18))
    y3 = ys[2]
    g.append(f'<g>{_v16_on(.75)}{glow(rx + rw / 2, y3 + rh / 2, 260, "var(--c4)", .28)}'
             f'<rect x="{rx - 5}" y="{y3 - 5}" width="{rw + 10}" height="{rh + 10}" rx="15" fill="none" stroke="var(--c4)" stroke-width="2.4">'
             f'{loop("stroke-opacity", ".55;1;.55", 2.4)}</rect>'
             f'<g>{loop("opacity", ".5;1;.5", 2.2)}{spark(rx + rw - 20, y3 + 14, .75, "var(--c4)")}</g></g>')
    # the timer ring, above the laptop
    tx, ty, tr = zx + zw / 2, zy + 118, 96
    g.append(land(f'<circle cx="{tx}" cy="{ty}" r="{tr + 18}" fill="var(--card)" stroke="var(--line)" stroke-width="1.2"/>'
                  + "".join(f'<path d="M{tx + (tr + 10) * math.sin(k * math.pi / 6):.1f} {ty - (tr + 10) * math.cos(k * math.pi / 6):.1f} '
                            f'L{tx + (tr + 15) * math.sin(k * math.pi / 6):.1f} {ty - (tr + 15) * math.cos(k * math.pi / 6):.1f}" stroke="var(--c2)" stroke-width="1.6"/>' for k in range(12))
                  + _v16_ring(tx, ty, tr, .02, .88, "var(--c4)", 9, .94)
                  + TC(tx, ty + 14, sl["timer"], fit(sl["timer"], 40, tr * 1.6, "turno timer", floor=18), "var(--white)", 'font-weight="700"'), .1, .5))
    return portrait_mark("".join(g)), D, FREEZE


def _pv18_parejas(sl, ctx):
    """v18 stacked: the three 40 s timers on top, the note under them, the two people face to face, the list of titles
    below them. Same beats: titles light as read, one «?», the story comes back, «Se entiende», the note is written."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    g = [glow(zx + zw / 2, zy + 520, 440, "var(--brand)", .45)]
    phases = ((.04, .30), (.34, .60), (.64, .88))
    for k, (lab, (a, b)) in enumerate(zip(sl["timers"], phases)):
        cx, cy = zx + zw / 6 + k * zw / 3, zy + 56
        g.append(land(_v16_ring(cx, cy, 38, a, b, "var(--c4)", 6)
                      + _pv_label(cx, cy + 82, lab, 22, zw / 3 - 16, "parejas timer", extra=W6 + ' text-anchor="middle"'), .1 + k * .12, .5))
        g.append(_v16_badge(cx, cy, b, ok, 17))
    lx, rxp, py, s = zx + 150, zx + zw - 150, zy + 540, 2.3
    reader = f'<g transform="translate({lx} {py}) scale({s})">{_n10_bust(SKIN_LIGHT, "var(--c1)", HAIR, "long")}</g>'
    listener_bust = _n10_bust(SKIN_BROWN, "var(--accent)", _N10_HAIR2, "short").split('<path d="M-15 -22')[0]
    listener = f'<g transform="translate({rxp} {py}) scale({-s} {s})">{listener_bust}</g>'
    table = f'<path d="M{zx} {py + 142} H{zx + zw}" stroke="var(--line)" stroke-width="2" stroke-linecap="round"/>'
    halos = glow(lx + 10, py - 60, 140, "var(--c2)", .3) + glow(rxp - 10, py - 60, 140, "var(--c2)", .3)
    g.append(land(halos + table + reader + listener, .2, .55))
    # the list of titles, under them
    shx, shy, shw, shh = zx + 110, py + 166, zw - 220, 186
    sheet = (card(shx, shy, shw, shh, "var(--card)", "var(--c2)", 12, 1.6)
             + _pv_label(shx + 20, shy + 36, sl["list_label"], 20, shw - 40, "parejas list label", "var(--muted)")
             + "".join(_pv_label(shx + 20, shy + 76 + i * 38, t, 22, shw - 40, "parejas title") for i, t in enumerate(sl["list"])))
    g.append(land(sheet, .4, .5))
    for i in range(len(sl["list"])):
        yy, a = shy + 76 + i * 38, .07 + i * .07
        g.append(f'<g>{_v16_win(a, a + .07)}<rect x="{shx + 10}" y="{yy - 25}" width="{shw - 20}" height="34" rx="8" fill="var(--c4)" opacity=".22"/></g>')
    g.append(_v18_waves(lx + 70, py - 50, 1, .05, .29))
    g.append(_v18_waves(rxp - 70, py - 50, -1, .36, .58))
    qx, qy = rxp - 10, py - 190
    q = (f'<path d="M{qx - 30} {qy - 30} h60 a14 14 0 0 1 14 14 v32 a14 14 0 0 1 -14 14 h-24 l-10 14 l-4 -14 h-22 a14 14 0 0 1 -14 -14 v-32 a14 14 0 0 1 14 -14 Z" '
         f'fill="var(--card)" stroke="var(--c4)" stroke-width="1.8"/>' + TC(qx, qy + 12, "?", 34, "var(--c4)", 'font-weight="700"'))
    g.append(f'<g>{_v16_win(.24, .52)}<g>{_v16_slide(.24, 0, 10)}{q}</g></g>')
    thread = f"M{rxp - 130} {shy} C{rxp - 170} {py + 60} {rxp - 170} {py - 30} {rxp - 76} {py - 44}"
    g.append(f'<path d="{thread}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="2.2">'
             + beat("stroke-dashoffset", [(0, 1), (.38, 1), (.50, 0), (.97, 0), (1, 1)]) + '</path>')
    g.append(_v16_hop(thread, .38, .50))
    g.append(f'<g>{_v16_on(.54)}<g>{_v16_slide(.54, 0, 10)}{pill(qx - 40, qy, sl["understood"], ok, ctx, 24, 240, "parejas understood")}</g></g>')
    # the commitment note is written, between the timers and the people
    nx, ny, nw, nh = zx + 170, zy + 168, zw - 340, 150
    note = card(nx, ny, nw, nh, "var(--card)", "var(--c4)", 12, 1.8) + _pv_label(nx + 20, ny + 38, sl["note"], 22, nw - 40, "parejas note")
    g.append(f'<g>{_v16_on(.64)}<g>{_v16_slide(.64, 0, 14)}{note}</g></g>')
    for i in range(3):
        w = (nw - 40) * (.85, .7, .9)[i]
        g.append(f'<path d="M{nx + 20} {ny + 72 + i * 26} h{w:.0f}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c2)" stroke-width="2.4" stroke-linecap="round">'
                 + beat("stroke-dashoffset", [(0, 1), (.68 + i * .06, 1), (.72 + i * .06, 0), (.97, 0), (1, 1)]) + '</path>')
    return portrait_mark("".join(g)), D, FREEZE

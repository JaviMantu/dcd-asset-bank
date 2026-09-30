"""The salud deck · slides 7 (four hypotheses) and 14 (the close: tomorrow's care center).

Runs inside the shared ext namespace (module/ext.py), after the harvested scenes, so it reuses their timing helpers
(_n07_* of energía's slide 7, _n13_* of energía's group E) and energía's faceless operator (_n14_man) without redefining
them. Every loop is one 12-second story; the reduced-motion frame (10.8 s) is its resolved state. No figures."""


# ---------------------------------------------------------------- 7 · four hypotheses, each one comes alive in turn
def _b07_chat(a, ok):
    """Atención al cliente: at night a customer asks; the AI answers in the chat at once, with its spark."""
    moon = ('<path d="M14 4 A11 11 0 1 0 26 20 A8.5 8.5 0 1 1 14 4 Z" fill="var(--c4)" opacity=".85"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="var(--c4)">{loop("opacity", ".2;1;.2", 2.2, k * .7)}</circle>'
                      for k, (x, y) in enumerate(((36, 6), (44, 20), (30, 30)))))
    ask = (card(76, 4, 120, 34, "var(--c1)", "var(--c1)", 12, 0)
           + '<rect x="90" y="14" width="88" height="5" rx="2.5" fill="var(--white)" opacity=".8"/>'
           + '<rect x="90" y="24" width="56" height="5" rx="2.5" fill="var(--white)" opacity=".8"/>')
    wait = f'<circle cx="196" cy="4" r="4.5" fill="var(--c4)">{_n07_key("opacity", [(0, 1), (a + .7, 1), (a + .8, 0), (_N07_RESET[0], 0), (_N07_RESET[1], 1)])}</circle>'
    typing = (f'<g opacity="0">{_n07_key("opacity", [(a + .15, 0), (a + .2, 1), (a + .7, 1), (a + .75, 0)])}'
              + card(0, 52, 70, 32, "var(--dim)", "var(--line)", 12, 1)
              + "".join(f'<circle cx="{20 + 15 * k}" cy="68" r="3.5" fill="var(--c2)">{loop("opacity", ".25;1;.25", .8, k * .2)}</circle>' for k in range(3))
              + '</g>')
    reply = (f'<g opacity="0">{_n07_hold(a + .75)}' + card(0, 52, 168, 52, "var(--dim)", "var(--c4)", 12, 1.2)
             + spark(18, 68, .45)
             + "".join(f'<rect x="34" y="{62 + 13 * k}" width="{w}" height="5" rx="2.5" fill="var(--c2)" opacity=".7">'
                       f'{_n07_key("width", [(a + .8 + .15 * k, 0), (a + 1.1 + .15 * k, w), (_N07_RESET[0], w), (_N07_RESET[1], 0)])}</rect>'
                       for k, w in enumerate((118, 84, 100)))
             + '</g>')
    return moon + ask + wait + typing + reply + _n07_badge(186, 104, a + 1.5, ok)


def _b07_docs(a, ok, skin):
    """Reembolsos: three loose documents; the AI reads each one, checks it and files it; the file reaches a person
    ready, before anyone retypes it."""
    folder = (card(104, 34, 50, 58, "var(--dim)", "var(--c2)", 5, 1.2)
              + '<path d="M104 44 H124 L130 36 H154" fill="none" stroke="var(--c2)" stroke-width="1.2"/>')
    docs, spots = [], ((0, 14, -8), (22, 26, 4), (44, 12, 10))
    for k, (x, y, rot) in enumerate(spots):
        t = a + .55 + .22 * k
        page = (f'<g transform="rotate({rot} {x + 17} {y + 22})">' + card(x, y, 34, 44, "var(--card)", "var(--c2)", 4, 1.2)
                + "".join(f'<rect x="{x + 6}" y="{y + 9 + 8 * j}" width="{w}" height="4" rx="2" fill="var(--c2)" opacity=".55"/>'
                          for j, w in enumerate((20, 16, 22, 12)))
                + f'<g opacity="0">{_n07_hold(t - .15, .1)}<circle cx="{x + 30}" cy="{y + 6}" r="7" fill="{ok}"/>{check(x + 30, y + 6.5, .45, "var(--ink)")}</g>'
                + '</g>')
        dx, dy = 112 - x, 44 - y
        into = _n07_key("opacity", [(t + .3, 1), (t + .4, 0), (_N07_RESET[0], 0), (_N07_RESET[1], 1)])
        docs.append(f'<g>{into}{_n07_tr([(t, "0 0"), (t + .35, f"{dx} {dy}"), (_N07_RESET[0], f"{dx} {dy}"), (_N07_RESET[1], "0 0")])}{page}</g>')
    full = (f'<g opacity="0">{_n07_hold(a + 1.35)}' + card(104, 34, 50, 58, "var(--dim)", "var(--c4)", 5, 1.5)
            + '<path d="M104 44 H124 L130 36 H154" fill="none" stroke="var(--c4)" stroke-width="1.5"/>'
            + "".join(f'<rect x="112" y="{54 + 9 * j}" width="{w}" height="4" rx="2" fill="var(--c4)" opacity=".7"/>' for j, w in enumerate((32, 24, 30, 18)))
            + '</g>')
    scan = (f'<g opacity="0">{_n07_key("opacity", [(a + .1, 0), (a + .15, 1), (a + .55, 1), (a + .6, 0)])}'
            f'<g>{_n07_tr([(a + .1, "0 0"), (a + .55, "0 64")])}<path d="M-4 10 H84" stroke="var(--c4)" stroke-width="1.5"/>{spark(84, 10, .35)}</g></g>')
    hand = (f'<path d="M156 64 H170" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="3 4">{loop("stroke-dashoffset", "0;-14", 1)}</path>'
            + f'<g opacity="0">{_n07_key("opacity", [(a + 1.25, 0), (a + 1.3, 1), (a + 1.5, 1), (a + 1.55, 0)])}'
              f'{_n07_move("M154 64 H176", [(a + 1.3, 0), (a + 1.5, 1)])}{token("var(--c4)", 4)}</g>')
    person = _n07_bust(184, 56, .9, skin, "var(--c3)") + _n07_ping(184, 64, 20, 34, a + 1.5)
    return folder + scan + "".join(docs) + full + hand + person + _n07_badge(186, 104, a + 1.6, ok)


def _b07_care(a, ok):
    """Cuidado proactivo: the health app shows a signal; it becomes a reminder and then an appointment on the calendar, in time."""
    phone = (card(0, 6, 56, 100, "var(--dim)", "var(--c2)", 10, 1.2)
             + '<rect x="20" y="12" width="16" height="3" rx="1.5" fill="var(--c2)" opacity=".6"/>')
    ecg = "M6 62 H16 L21 50 L27 74 L32 56 L36 62 H50"
    beat_ = (f'<path d="{ecg}" fill="none" stroke="var(--c2)" stroke-width="1.6" stroke-linejoin="round" opacity=".8"/>'
             + f'<path d="{ecg}" fill="none" stroke="var(--c4)" stroke-width="2" stroke-linejoin="round" opacity="0">{_n07_hold(a + .1)}</path>'
             + _n07_ping(21, 50, 3, 18, a + .1) + _n07_ping(21, 50, 3, 18, a + .45))
    bell = ('<g transform="translate(92 42)"><path d="M-11 6 C-11 -2 -9 -11 0 -11 C9 -11 11 -2 11 6 L14 10 H-14 Z" fill="none" '
            'stroke="var(--c2)" stroke-width="1.5" stroke-linejoin="round"/><circle cx="0" cy="14" r="3" fill="var(--c2)"/></g>')
    bell_on = (f'<g opacity="0">{_n07_hold(a + .6)}<g transform="translate(92 42)">'
               '<path d="M-11 6 C-11 -2 -9 -11 0 -11 C9 -11 11 -2 11 6 L14 10 H-14 Z" fill="var(--c4)" fill-opacity=".25" '
               'stroke="var(--c4)" stroke-width="1.8" stroke-linejoin="round"/><circle cx="0" cy="14" r="3" fill="var(--c4)"/></g></g>'
               + _n07_ping(92, 44, 14, 28, a + .6))
    cells = "".join(f'<rect x="{134 + 20 * (k % 3)}" y="{40 + 18 * (k // 3)}" width="14" height="12" rx="3" fill="var(--c2)" opacity=".3"/>'
                    for k in range(6))
    cal = (card(126, 14, 70, 82, "var(--dim)", "var(--c2)", 8, 1.2) + '<path d="M126 32 H196" stroke="var(--c2)" stroke-width="1.2"/>'
           + '<path d="M144 8 V20 M178 8 V20" stroke="var(--c2)" stroke-width="2" stroke-linecap="round"/>' + cells
           + f'<rect x="154" y="58" width="14" height="12" rx="3" fill="var(--c4)" opacity="0">{_n07_hold(a + 1.15)}</rect>'
           + _n07_ping(161, 64, 8, 22, a + 1.15))
    hops = (f'<g opacity="0">{_n07_key("opacity", [(a + .3, 0), (a + .35, 1), (a + .6, 1), (a + .62, 0)])}'
            f'{_n07_move("M40 50 C56 30 70 34 80 40", [(a + .35, 0), (a + .6, 1)])}{token("var(--c4)", 4)}</g>'
            f'<g opacity="0">{_n07_key("opacity", [(a + .8, 0), (a + .85, 1), (a + 1.12, 1), (a + 1.15, 0)])}'
            f'{_n07_move("M106 44 C126 44 140 60 160 64", [(a + .85, 0), (a + 1.12, 1)])}{token("var(--c4)", 4)}</g>')
    return phone + beat_ + bell + bell_on + cal + hops + _n07_badge(186, 104, a + 1.45, ok)


# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
def _pb07_text(x, y, text, size, room, fill, lines=3, lh=1.3):
    """text wrapped into room at the largest size (never under 20: the phone floor) that fits in `lines` lines."""
    z = size
    while z > 20 and len(_n07_wrap(_(str(text)), _n07_chars(text, z, room))) > lines:
        z -= 1
    return TCW(x, y, text, _n07_chars(text, z, room), z, fill, W6, lh, "start")


def _pb07_twin(sl, ctx):
    """b07 on the 900x1600 stage (after m07's twin): the three hypotheses as full-width rows, text on the left and their
    small story on the right, the enabler under them, a spine on the left carrying its pulse into each row.
    Same loop, same frozen frame, every card keeps its «?»."""
    ok = ctx.brand.c("dark.ok")
    cols = ("var(--c1)", "var(--c3)", "var(--c2)", "var(--accent)")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    SX, X0 = zx + 20, zx + 44
    W, RH, GAP = zx + zw - X0, 180, 10
    ys = [zy + 22 + k * (RH + GAP) for k in range(3)]      # 22 below the zone's top: the «?» must not reach the text
    BY, BH = ys[-1] + RH + 22, 290
    wins = ((2.2, 4.6), (4.6, 7.0), (7.0, 9.4), (9.4, _N07_RESET[0]))
    R = _N07_RESET
    room = W - 24 - 290

    def qmark(cx, cy, a):
        return (f'<circle cx="{cx}" cy="{cy}" r="20" fill="var(--card)" stroke="var(--c4)" stroke-width="1.8"/>'
                + TC(cx, cy + 8.5, "?", 24, "var(--c4)", W6) + _n07_ping(cx, cy, 20, 40, a + .05))   # one ping: the budget

    def spot(x, y, w, h, a, b):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="none" stroke="var(--c4)" stroke-width="2.4" opacity="0">{_n07_win(a, b)}</rect>'

    art, text = [glow(zx + zw / 2, zy + zh * .45, 470, "var(--brand)", .45)], []
    stories = (_b07_chat(wins[0][0], ok), _b07_docs(wins[1][0], ok, _N07_SKIN_MID), _b07_care(wins[2][0], ok))
    f = current_factor()
    for k in range(3):
        y, (area, idea, gain), (a, b), at = ys[k], sl["cards"][k], wins[k], .1 + .12 * k
        art.append(land(card(X0, y, W, RH, "var(--card)", "var(--line)", 18, 1.2)
                        + f'<rect x="{X0 + 18}" y="{y - 2}" width="{W * .4:.0f}" height="4" rx="2" fill="{cols[k]}"/>'
                        + f'<g transform="translate({X0 + W - 240} {y + 30}) scale(1.1)">{stories[k]}</g>'
                        + spot(X0, y, W, RH, a, b) + qmark(X0 + W - 30, y, a), at, .5, 16))
        rw = bold_width(_(str(sl["ret"])), 20, f)
        text.append(land(T(X0 + 24, y + 40, area, fit(area, 26, room, "hypothesis area", floor=20), "var(--white)", W6)
                         + _pb07_text(X0 + 24, y + 72, idea, 21, room, "var(--muted)", 3, 1.25)
                         + T(X0 + 24, y + 164, sl["ret"], 20, "var(--muted)", W6)
                         + T(f"{X0 + 36 + rw:.0f}", y + 164, gain, fit(gain, 24, room - rw - 12, "hypothesis return", floor=20), "var(--c4)", W6),
                         at, .5, 16))
    # the enabler: its delivery cycle, four steps and a track the change runs along
    area, idea, gain = sl["cards"][3]
    a4 = wins[3][0]
    mid = X0 + W / 2
    nodes = [mid + (k - 1.5) * 150 for k in range(4)]
    ny, trk = BY + 156, BY + 200
    pipe = (f'<path d="M{nodes[0]} {ny} H{nodes[-1]}" stroke="var(--line)" stroke-width="2"/>'
            + "".join(card(x - 32, ny - 32, 64, 64, "var(--dim)", "var(--line)", 14, 1.2) + f'<g transform="translate({x:.0f} {ny}) scale(1.25)">{_n07_glyph(k)}</g>'
                      + f'<rect x="{x - 32:.0f}" y="{ny - 32}" width="64" height="64" rx="14" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_n07_hold(a4 + .12 + .17 * k, .1)}</rect>'
                      for k, x in enumerate(nodes))
            + f'<path d="M{nodes[0]} {trk} H{nodes[-1]}" stroke="var(--line)" stroke-width="2"/>'
            + f'<path d="M{nodes[0]} {trk} H{nodes[-1]}" stroke="var(--c4)" stroke-width="2" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">'
              f'{_n07_key("stroke-dashoffset", [(a4 + .1, 1), (a4 + .66, 0), (R[0], 0), (R[1], 1)])}</path>'
            + f'<g opacity="0">{_n07_key("opacity", [(a4 + .05, 0), (a4 + .1, 1), (a4 + .66, 1), (a4 + .72, 0)])}'
              f'{_n07_move(f"M{nodes[0]} {trk} H{nodes[-1]}", [(a4 + .1, 0), (a4 + .66, 1)])}{token("var(--c4)", 6)}</g>')
    art.append(land(card(X0, BY, W, BH, "var(--card)", "var(--line)", 18, 1.2)
                    + f'<rect x="{X0 + 18}" y="{BY - 2}" width="{W * .6:.0f}" height="4" rx="2" fill="{cols[3]}"/>'
                    + pipe + spot(X0, BY, W, BH, *wins[3]) + qmark(X0 + W - 30, BY, a4), .46, .5, 16))
    text.append(land(T(X0 + 24, BY + 42, area, fit(area, 26, W - 100, "hypothesis area", floor=20), "var(--white)", W6)
                     + _pb07_text(X0 + 24, BY + 76, idea, 21, W - 48, "var(--muted)", 1)
                     + TC(f"{mid:.0f}", BY + 236, sl["cycle"], fit(sl["cycle"], 20, W - 48, "hypothesis cycle", floor=20), "var(--muted)", W6)
                     + T(X0 + 24, BY + 272, gain, fit(gain, 24, W - 48, "hypothesis enabler", floor=20), "var(--c4)", W6), .46, .5, 16))
    # the enabler powers the three: a pulse climbs the spine into each row
    spine = []
    for k, y in enumerate(ys):
        py, t = y + RH / 2, .08 * k
        d = f"M{SX} {BY} V{py} H{X0}"
        spine.append(f'<path d="{d}" fill="none" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="3 5" opacity=".6"/>'
                     f'<path d="{d}" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_n07_hold(a4 + .75 + t, .12)}</path>'
                     f'<g opacity="0">{_n07_key("opacity", [(a4 + .7 + t, 0), (a4 + .75 + t, 1), (a4 + 1.05 + t, 1), (a4 + 1.12 + t, 0)])}'
                     f'{_n07_move(d, [(a4 + .72 + t, 0), (a4 + 1.05 + t, 1)])}{token("var(--c4)", 5)}</g>'
                     f'<circle cx="{X0}" cy="{py}" r="5" fill="var(--c4)" opacity="0">{_n07_hold(a4 + 1.05 + t, .1)}</circle>')
    spine.append(f'<circle cx="{SX}" cy="{BY}" r="5" fill="var(--c4)"/>')
    art.append(land("".join(spine), 1.2, .45, 0))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "b07_hipotesis")
def sc_b07_hipotesis(sl, ctx):
    """Three hypotheses with a possible return stand on a fourth, technology, that enables them. The loop visits each
    card in turn and plays its small story: at night the question in the chat gets its answer at once; the loose
    reimbursement documents are read, checked and filed before they reach a person; the app's signal becomes a reminder
    and an appointment on the calendar. Then the enabler runs its delivery cycle and powers the three. Every card keeps
    its «?»: hypotheses to validate together."""
    if ORIENT() == "portrait":
        return _pb07_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    cols = ("var(--c1)", "var(--c3)", "var(--c2)", "var(--accent)")
    W, H, Y0, GAP = 232, 386, 104, 14
    xs = [830 + k * (W + GAP) for k in range(3)]
    BX, BY, BW, BH = 830, 548, 724, 216
    wins = ((2.2, 4.6), (4.6, 7.0), (7.0, 9.4), (9.4, _N07_RESET[0]))
    R = _N07_RESET

    def qmark(cx, cy, a):
        return (f'<circle cx="{cx}" cy="{cy}" r="15" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>'
                + TC(cx, cy + 6.5, "?", 18, "var(--c4)", W6) + _n07_ping(cx, cy, 15, 30, a + .05) + _n07_ping(cx, cy, 15, 30, a + .45))

    def spot(x, y, w, h, a, b):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_n07_win(a, b)}</rect>'

    g = [glow(1192, 430, 470, "var(--brand)", .45)]
    stories = (_b07_chat(wins[0][0], ok), _b07_docs(wins[1][0], ok, _N07_SKIN_MID), _b07_care(wins[2][0], ok))
    parts = []
    for k in range(3):
        x, (area, idea, gain), (a, b) = xs[k], sl["cards"][k], wins[k]
        c = (card(x, Y0, W, H, "var(--card)", "var(--line)", 18, 1.2)
             + f'<rect x="{x + 18}" y="{Y0 - 2}" width="{W - 70}" height="4" rx="2" fill="{cols[k]}"/>'
             + T(x + 18, Y0 + 46, area, fit(area, 18, W - 66, "hypothesis area"), "var(--white)", W6)
             + TCW(x + 18, Y0 + 80, idea, _n07_chars(idea, 16, W - 36), 16, "var(--muted)", W6, 1.35, "start")
             + f'<g transform="translate({x + 18} {Y0 + 178})">{stories[k]}</g>'
             + T(x + 18, Y0 + 326, sl["ret"], fit(sl["ret"], 15, W - 36, "hypothesis return label"), "var(--muted)", W6)
             + T(x + 18, Y0 + 354, gain, fit(gain, 18, W - 36, "hypothesis return"), "var(--c4)", W6)
             + spot(x, Y0, W, H, a, b) + qmark(x + W - 30, Y0, a))
        parts.append(c)
    area, idea, gain = sl["cards"][3]
    a4 = wins[3][0]
    nodes = [1226 + 86 * k for k in range(4)]
    ny = BY + 100
    pipe = (f'<path d="M{nodes[0]} {ny} H{nodes[-1]}" stroke="var(--line)" stroke-width="2"/>'
            + "".join(card(x - 26, ny - 26, 52, 52, "var(--dim)", "var(--line)", 12, 1.2) + f'<g transform="translate({x} {ny})">{_n07_glyph(k)}</g>'
                      + f'<rect x="{x - 26}" y="{ny - 26}" width="52" height="52" rx="12" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity="0">{_n07_hold(a4 + .12 + .17 * k, .1)}</rect>'
                      for k, x in enumerate(nodes))
            + f'<g opacity="0">{_n07_key("opacity", [(a4 + .05, 0), (a4 + .1, 1), (a4 + .66, 1), (a4 + .72, 0)])}'
              f'{_n07_move(f"M{nodes[0]} {ny + 40} H{nodes[-1]}", [(a4 + .1, 0), (a4 + .66, 1)])}{token("var(--c4)", 5)}</g>'
            + f'<path d="M{nodes[0]} {ny + 40} H{nodes[-1]}" stroke="var(--c4)" stroke-width="1.5" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">'
              f'{_n07_key("stroke-dashoffset", [(a4 + .1, 1), (a4 + .66, 0), (R[0], 0), (R[1], 1)])}</path>')
    base = (card(BX, BY, BW, BH, "var(--card)", "var(--line)", 18, 1.2)
            + f'<rect x="{BX + 18}" y="{BY - 2}" width="{BW - 76}" height="4" rx="2" fill="{cols[3]}"/>'
            + T(BX + 18, BY + 46, area, fit(area, 18, 300, "hypothesis area"), "var(--white)", W6)
            + TCW(BX + 18, BY + 80, idea, _n07_chars(idea, 16, 340), 16, "var(--muted)", W6, 1.35, "start")
            + T(BX + 18, BY + 184, gain, fit(gain, 18, 340, "hypothesis enabler"), "var(--c4)", W6)
            + TC((nodes[0] + nodes[-1]) / 2, BY + 184, sl["cycle"], fit(sl["cycle"], 15, 320, "hypothesis cycle"), "var(--muted)", W6)
            + pipe + spot(BX, BY, BW, BH, *wins[3]) + qmark(BX + BW - 30, BY, a4))
    parts.append(base)
    pillars = []
    for k, x in enumerate(xs):
        cx = x + W / 2
        pillars.append(f'<path d="M{cx} {BY} V{Y0 + H}" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="3 5" opacity=".6"/>'
                       f'<path d="M{cx} {BY} V{Y0 + H}" stroke="var(--c4)" stroke-width="2" opacity="0">{_n07_hold(a4 + .75 + .08 * k, .12)}</path>'
                       f'<g opacity="0">{_n07_key("opacity", [(a4 + .7 + .08 * k, 0), (a4 + .75 + .08 * k, 1), (a4 + 1.05 + .08 * k, 1), (a4 + 1.12 + .08 * k, 0)])}'
                       f'{_n07_move(f"M{cx} {BY} V{Y0 + H}", [(a4 + .72 + .08 * k, 0), (a4 + 1.05 + .08 * k, 1)])}{token("var(--c4)", 4)}</g>'
                       f'<circle cx="{cx}" cy="{Y0 + H}" r="4" fill="var(--c4)" opacity="0">{_n07_hold(a4 + 1.05 + .08 * k, .1)}</circle>'
                       f'<circle cx="{cx}" cy="{BY}" r="4" fill="var(--c4)"/>')
    g.append(seq(parts, .1, .5, 16))
    g.append(land("".join(pillars), 1.2, .45, 0))
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 14 · tomorrow's care center (the close)
_B14_END = .965  # = _N13_RESET of energia_s13_15.py; every resolved state holds until .965, after the frozen frame (.9)


def _b14_ok_dot(x, y, at, ok, r=10):
    return f'<g opacity="0">{_n13_on(at)}<circle cx="{x}" cy="{y}" r="{r}" fill="{ok}"/>{check(x, y + 1, r / 15, "var(--ink)")}</g>'


def _b14_ping(x, y, r0, r1, at, color="var(--c4)", dur=.05):
    return (f'<circle cx="{x}" cy="{y}" r="{r0}" fill="none" stroke="{color}" stroke-width="1.5" opacity="0">'
            f'{beat("r", [(0, r0), (at, r0), (at + dur, r1), (1, r1)])}'
            f'{beat("opacity", [(0, 0), (at, 0), (at + .003, .9), (at + dur, 0), (1, 0)])}</circle>')


def _b14_icon(k, x, y):
    """Row glyphs around (x, y): 0 the AI's spark, 1 a person, 2 a phone."""
    st = 'fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"'
    if k == 0:
        return spark(x, y, .5)
    if k == 1:
        return f'<circle cx="{x}" cy="{y - 5}" r="4.5" {st}/><path d="M{x - 8} {y + 9} C{x - 8} {y + 1} {x + 8} {y + 1} {x + 8} {y + 9}" {st}/>'
    return f'<rect x="{x - 6}" y="{y - 10}" width="12" height="20" rx="3" {st}/><path d="M{x - 2} {y + 6} H{x + 2}" {st}/>'


# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
def _pb14_twin(sl, ctx):
    """b14 on the 900x1600 stage: the wall screen full width (the app's signals and the three steps on the left, the queue
    and the governed knowledge on the right, the gutter between them), and under it the care-team person with the
    tablet and the client's phone, both x1.34 so their labels read. Same beats, same frozen frame."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    sx, sy, sw, sh = zx, zy + 10, zw, 530
    L, LW = sx + 16, 420
    R, RW = L + LW + 16, sw - LW - 48
    gut = L + LW + 8
    UP, FC, AL, SG, TAP, OKD, APP, NOTE, DONE = .168, .205, .245, .285, .355, .40, .445, .495, .52
    Q = ((.555, .595), (.635, .675))
    S0, S1, S2 = .715, .745, .79
    art, text = [glow(zx + zw / 2, sy + 260, 460, "var(--brand)", .5)], []

    # ---- the wall screen
    hud = "".join(f'<path d="M{x0 + dx * 6} {y0 + dy * 30} V{y0 + dy * 6} H{x0 + dx * 30}" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity=".8"/>'
                  for x0, y0, dx, dy in ((sx, sy, 1, 1), (sx + sw, sy, -1, 1), (sx, sy + sh, 1, -1), (sx + sw, sy + sh, -1, -1)))
    screen = (card(sx, sy, sw, sh, "var(--card)", "var(--c2)", 22, 1.2) + hud
              + f'<path d="M{sx} {sy + 54} H{sx + sw}" stroke="var(--line)" stroke-width="1.5"/>'
              + f'<circle cx="{sx + 28}" cy="{sy + 27}" r="8" fill="var(--c5)">{blink(1.4)}</circle>'
              + T(sx + 48, sy + 35, sl["screen"], fit(sl["screen"], 22, 420, "care center screen", floor=20), "var(--white)", W6)
              + pill(sx + sw - 80, sy + 27, sl["live"], ok, ctx, 20, 150, "care center live", 16))
    # left pane: the app's signals (the real trace stays in the band, the forecast leaves it)
    ax, ay, aw, ah = L, sy + 66, LW, 186
    real = [(0, 106), (30, 102), (60, 108), (90, 100), (120, 104), (150, 96), (180, 100), (210, 92), (240, 88), (262, 86)]
    d = "M" + " L".join(f"{ax + 16 + x} {ay + y}" for x, y in real)
    fx0, fy0 = ax + 16 + real[-1][0], ay + real[-1][1]
    fc = f"M{fx0} {fy0} L{fx0 + 56} {ay + 72} L{ax + aw - 16} {ay + 52}"
    cross = (fx0 + 42, ay + 76)
    chart = (card(ax, ay, aw, ah, "var(--dim)", "var(--line)", 14, 1.5)
             + f'<rect x="{ax + 16}" y="{ay + 76}" width="{aw - 32}" height="52" rx="6" fill="var(--c3)" opacity=".08"/>'
             + f'<path d="M{ax + 16} {ay + 76} H{ax + aw - 16}" stroke="var(--c5)" stroke-width="1.4" stroke-dasharray="4 5" opacity=".85"/>')
    chart_lab = (T(ax + 16, ay + 32, sl["chart"], fit(sl["chart"], 20, 230, "care center chart", floor=20), "var(--muted)", W6)
                 + T(ax + aw - 16, ay + 32, sl["forecast"], fit(sl["forecast"], 20, 150, "care center forecast", floor=20), "var(--c4)", 'text-anchor="end" font-weight="600"'))
    lines = (land(f'<path d="{d} L{fx0} {ay + 134} L{ax + 16} {ay + 134} Z" fill="var(--c3)" opacity=".14"/>', .5, .6, 0)
             + trace(d, "var(--c3)", 2.4, .45, .8)
             + f'<g>{beat("opacity", [(0, 1), (DONE, 1), (DONE + .03, .3), (_B14_END, .3), (_B14_END + .02, 1), (1, 1)])}'
               f'<path d="{fc}" pathLength="1" fill="none" stroke="var(--c4)" stroke-width="2.2" stroke-dasharray="1" stroke-linecap="round">'
               f'{beat("stroke-dashoffset", [(0, 1), (FC, 1), (AL, 0), (_B14_END, 0), (_B14_END + .02, 1), (1, 1)])}</path></g>')
    alert = (f'<g opacity="0">{_n13_on(AL, DONE)}'
             f'<circle cx="{cross[0]}" cy="{cross[1]}" r="10" fill="none" stroke="var(--c5)" stroke-width="1.8">{loop("r", "8;22;8", 2.2)}</circle>'
             + pill(ax + aw - 124, ay + ah - 28, sl["alert"], "var(--c5)", ctx, 20, 232, "care center alert", 14) + '</g>'
             + f'<g opacity="0">{_n13_on(DONE)}' + pill(ax + aw - 124, ay + ah - 28, sl["done"], ok, ctx, 20, 232, "care center done", 14) + '</g>')
    # the three steps the signal turns into
    rows, row_y = [], []
    for k, (label, at) in enumerate(zip(sl["steps"], (SG, OKD, APP))):
        y = ay + ah + 12 + 62 * k
        row_y.append(y + 27)
        rows.append(f'<g opacity=".32">{_n13_lit(at, .32)}' + card(L, y, LW, 54, "var(--dim)", "var(--line)", 10, 1.2)
                    + f'<g transform="translate({L + 24} {y + 27}) scale(1.3)">{_b14_icon(k, 0, 0)}</g>'
                    + T(L + 46, y + 34, label, fit(label, 20, LW - 84, "care center step", floor=20), "var(--white)", W6) + '</g>'
                    + f'<rect x="{L}" y="{y}" width="{LW}" height="54" rx="10" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity="0">'
                      f'{beat("opacity", [(0, 0), (at, 0), (at + .01, 1), (at + .06, 1), (at + .09, 0), (1, 0)])}</rect>'
                    + _b14_ok_dot(L + LW - 22, y + 27, at + .01, ok, 12))
    # right pane: the queue, answered from the governed knowledge
    tk_y = [ay + 30 + 98 * k for k in range(3)]
    kb_y = tk_y[-1] + 100
    right = [T(R, ay + 18, sl["queue"], fit(sl["queue"], 20, RW, "care center queue", floor=20), "var(--muted)", W6)]
    for k, (q, y) in enumerate(zip(sl["tickets"], tk_y)):
        right.append(card(R, y, RW, 88, "var(--dim)", "var(--line)", 10, 1.2)
                     + TCW(R + 14, y + 28, q, _n07_chars(q, 20, RW - 50), 20, "var(--white)", W6, 1.15, "start"))
        at = Q[k][1] if k < 2 else S2 + .01
        right.append(f'<g>{_n13_off(at if k < 2 else S0)}' + T(R + 14, y + 78, sl["new"], 20, "var(--muted)", W6) + '</g>')
        if k < 2:
            right.append(f'<g opacity="0">{_n13_on(at)}' + T(R + 14, y + 78, sl["solved"], fit(sl["solved"], 20, RW - 60, "care center solved", floor=20), ok, W6)
                         + '</g>' + _b14_ok_dot(R + RW - 22, y + 70, at, ok, 12)
                         + _b14_ping(R + RW / 2, y + 44, 24, 70, at, ok, .05))
        else:
            right.append(f'<g opacity="0">{_n13_on(S0, S2 + .01)}' + T(R + 14, y + 78, sl["sensitive"], fit(sl["sensitive"], 20, RW - 28, "care center sensitive", floor=20), "var(--c5)", W6)
                         + f'<rect x="{R}" y="{y}" width="{RW}" height="88" rx="10" fill="none" stroke="var(--c5)" stroke-width="1.8"/></g>'
                         + f'<g opacity="0">{_n13_on(S2 + .01)}' + T(R + 14, y + 78, sl["routed"], fit(sl["routed"], 20, RW - 28, "care center routed", floor=20), "var(--c4)", W6) + '</g>')
    kb = (card(R, kb_y, RW, 116, "var(--card)", "var(--c2)", 12, 1.2)
          + T(R + 14, kb_y + 32, sl["space"], fit(sl["space"], 20, RW - 64, "care center knowledge", floor=20), "var(--white)", W6)
          + f'<g transform="translate({R + RW - 26} {kb_y + 22}) scale(1.3)"><rect x="-8" y="-3" width="16" height="12" rx="2.5" fill="none" stroke="var(--c2)" stroke-width="1.5"/>'
            '<path d="M-5 -3 V-6 A5 5 0 0 1 5 -6 V-3" fill="none" stroke="var(--c2)" stroke-width="1.5"/></g>')
    for j, name in enumerate(sl["docs"]):
        y = kb_y + 68 + 32 * j
        a0, a1 = Q[j]
        s_ = fit(name, 20, RW - 60, "care center doc", floor=20)
        kb += (f'<path d="M{R + 16} {y - 16} h10 l5 5 v13 h-15 Z" fill="none" stroke="var(--c2)" stroke-width="1.4"/>'
               + T(R + 42, y, name, s_, "var(--muted)", W6)
               + f'<g opacity="0">{beat("opacity", [(0, 0), (a0, 0), (a0 + .01, 1), (a1 + .02, 1), (a1 + .05, 0), (1, 0)])}'
                 f'<rect x="{R + 8}" y="{y - 23}" width="{RW - 16}" height="31" rx="7" fill="var(--c4)" opacity=".16"/>'
                 + T(R + 42, y, name, s_, "var(--c4)", W6) + '</g>'
               + _n13_ride(f"M{R + RW - 30} {y - 8} C{R + RW + 8} {y - 50} {R + RW + 8} {tk_y[j] + 80} {R + RW - 40} {tk_y[j] + 44}", a0 + .01, a1, 6))
    wall = screen + land(chart + chart_lab + "".join(rows) + "".join(right) + kb, .3, .45, 10) + lines + alert
    ccx, ccy = sx + sw / 2, sy + sh / 2
    art.append(pop(f'<g transform="translate({-ccx} {-ccy})">{wall}</g>', ccx, ccy, .05, .6))

    # ---- the client's phone (the desktop phone, x1.34): the app, where the signal starts and the appointment lands
    ps, pw, ph = 1.34, 176, 256
    PX, PY = zx + zw - 20 - pw * ps, sy + sh + 12
    at_ = lambda x, y: (PX + x * ps, PY + y * ps)
    ecg = "M18 206 H52 L60 188 L70 222 L78 198 L86 206 H158"
    phone = (card(0, 0, pw, ph, "var(--ink)", "var(--c2)", 26, 1.5)
             + card(8, 8, pw - 16, ph - 16, "var(--card)", "var(--line)", 20, 1)
             + '<rect x="70" y="16" width="36" height="5" rx="2.5" fill="var(--c2)" opacity=".5"/>'
             + T(22, 48, sl["app"], fit(sl["app"], 16, 80, "care center app", floor=15), "var(--white)", W6)
             + '<g transform="translate(146 42) scale(.8)"><path d="M0 8 C-9 1 -12 -4 -8 -8 C-5 -11 -1 -10 0 -6 C1 -10 5 -11 8 -8 C12 -4 9 1 0 8 Z" fill="var(--accent)"/></g>'
             + bars(22, 76, pw - 44, 3, 18, "var(--c2)", ".35")
             + f'<path d="{ecg}" fill="none" stroke="var(--c2)" stroke-width="1.6" stroke-linejoin="round" opacity=".8"/>'
             + f'<circle cx="60" cy="188" r="3.5" fill="var(--c4)">{loop("opacity", ".35;1;.35", 1.6)}</circle>'
             + _b14_ping(60, 188, 4, 30, UP))
    note = (f'<g opacity="0">{_n13_on(NOTE)}'
            + card(14, 62, pw - 28, 96, "var(--dim)", "var(--c4)", 12, 1.5)
            + '<g transform="translate(34 88)"><rect x="-10" y="-9" width="20" height="18" rx="3" fill="none" stroke="var(--c4)" stroke-width="1.5"/>'
              '<path d="M-10 -3 H10 M-5 -12 V-6 M5 -12 V-6" stroke="var(--c4)" stroke-width="1.5" stroke-linecap="round"/></g>'
            + T(52, 94, sl["note"][0], fit(sl["note"][0], 15, pw - 72, "care center note", floor=15), "var(--white)", W6)
            + T(26, 120, sl["note"][1], fit(sl["note"][1], 15, pw - 52, "care center note", floor=15), "var(--white)", W6)
            + T(26, 144, sl["note"][2], fit(sl["note"][2], 15, pw - 52, "care center note", floor=15), "var(--c4)", W6)
            + '</g>' + _b14_ping(pw / 2, 110, 30, 90, NOTE))
    art.append(land(f'<g transform="translate({PX:.0f} {PY:.0f}) scale({ps})">{phone}{note}</g>', .5, .5, 20))
    pcx = at_(pw / 2, 0)[0]
    floor_y = sy + sh - 12
    art.append(land(f'<path d="M{pcx:.0f} {sy + sh} V{PY:.0f}" stroke="var(--c2)" stroke-width="1.8" stroke-dasharray="3 6" opacity=".7">{loop("stroke-dashoffset", "0;-18", 1.2)}</path>', .9, .4, 0))
    art.append(_n13_ride(f"M{pcx:.0f} {at_(0, 150)[1]:.0f} V{floor_y} H{gut} V{cross[1]} H{cross[0]}", UP, FC, 7)
               + _n13_ride(f"M{L + LW - 22} {row_y[2]} H{gut} V{floor_y} H{pcx:.0f} V{at_(0, 82)[1]:.0f}", APP + .005, NOTE, 7))

    # ---- the care-team person with the tablet: «Aprobar», then approved, then the sensitive case with its context
    case = (f'<g opacity="0">{_n13_on(S2)}<rect x="-58" y="-36" width="116" height="74" rx="6" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>'
            + T(-46, -10, sl["case"][0], fit(sl["case"][0], 16, 96, "care center case", floor=15), "var(--white)", W6)
            + T(-46, 12, sl["case"][1], fit(sl["case"][1], 15, 96, "care center case", floor=15), "var(--c4)", W6)
            + '<rect x="-46" y="22" width="60" height="5" rx="2.5" fill="var(--c2)" opacity=".6"/></g>')
    tap = (f'<g>{_n13_off(TAP)}' + pill(0, 16, sl["approve"], "var(--c4)", ctx, 15, 110, "care center approve", 12) + '</g>'
           f'<g opacity="0">{_n13_on(TAP + .005, S2)}<rect x="-34" y="4" width="68" height="24" rx="12" fill="{ok}"/>' + check(0, 17, .6, "var(--ink)") + '</g>'
           f'<circle cx="30" cy="16" r="6" fill="none" stroke="var(--white)" stroke-width="1.5">{beat("r", [(0, 6), (TAP - .015, 6), (TAP + .06, 34), (1, 34)])}'
           f'{beat("opacity", [(0, 0), (TAP - .015, 0), (TAP - .01, 1), (TAP + .06, 0), (1, 0)])}</circle>' + case)
    ms, desk = 1.34, zy + zh - 20
    mnx, mny = zx + 200, desk - 170
    bx_, by_ = mnx + ms * (112 + 16 * math.sin(math.radians(10))), mny + ms * (62 + 16 * math.cos(math.radians(10)))
    beam_up = f"M{bx_:.0f} {by_ - 18:.0f} C{bx_ + 30:.0f} {by_ - 120:.0f} {gut} {sy + sh + 70} {gut} {sy + sh} V{row_y[1]} H{L + LW - 22}"
    art.append(f'<g opacity="0">{beat("opacity", [(0, 0), (TAP, 0), (TAP + .003, .9), (OKD, .9), (OKD + .03, 0), (1, 0)])}'
               f'<path d="{beam_up}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="2" stroke-linecap="round">'
               f'{beat("stroke-dashoffset", [(0, 1), (TAP, 1), (OKD, 0), (1, 0)])}</path></g>'
               + _n13_ride(beam_up, TAP, OKD, 7))
    beam_down = f"M{R + 10} {tk_y[2] + 44} H{gut} V{sy + sh} C{gut} {sy + sh + 70} {bx_ + 30:.0f} {by_ - 120:.0f} {bx_ - 20:.0f} {by_ - 50:.0f}"
    art.append(_n13_ride(beam_down, S1, S2, 7) + _b14_ping(R + RW / 2, tk_y[2] + 44, 24, 80, S0, "var(--c5)", .05))
    art.append(f'<clipPath id="pb14-desk"><rect x="0" y="0" width="900" height="{desk + 2}"/></clipPath>'
               f'<g clip-path="url(#pb14-desk)">' + land(_n14_man(mnx, mny, ms, SKIN_BROWN, "var(--c1)", tap), .4, .6, 40) + '</g>')
    leds = "".join(f'<circle cx="{zx + 30 + k * 30}" cy="{desk + 12}" r="2.6" fill="var(--c2)" opacity=".45"/>' for k in range(6))
    art.append(land(f'<path d="M{zx} {desk} H{PX - 16:.0f} L{PX - 26:.0f} {desk + 20} H{zx + 10} Z" fill="var(--card)"/>'
                    f'<path d="M{zx} {desk} H{PX - 16:.0f}" stroke="var(--c2)" stroke-width="1.5" opacity=".7"/>' + leds, .2, .5, 20))
    text.append(land(T(zx + 16, sy + sh + 50, sl["sign"], fit(sl["sign"], 24, PX - zx - 40, "care center sign", floor=20), "var(--c4)", W6), 1.4, .45, 10))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "b14_cuidado")
def sc_b14_cuidado(sl, ctx):
    """The close, tomorrow's care center, as one 12-second loop at the level of energía's control room. The app, on the
    client's phone, sends a signal up to the care center's wall screen; the forecast leaves the healthy band: the need is
    anticipated. The AI suggests a teleconsultation, a faceless care-team person approves it on the tablet (the pulse
    flies up the gutter to the screen) and the appointment drops into the app before the client asks. Then the queue:
    two simple questions are answered by themselves from the governed knowledge; the sensitive one, a rejected
    reimbursement, goes down to the same person with its context. The frozen frame (.9) is the resolved one."""
    if ORIENT() == "portrait":
        return _pb14_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    sx, sy, sw, sh = 830, 90, 720, 402
    lx, lw, rx, rw = 846, 360, 1222, 312
    gut = (lx + lw + rx) / 2  # the gutter between the two panes: every pulse to and from the person travels in it
    desk, mnx, mny = 796, 996, 690
    # beats, fractions of the loop
    UP, FC, AL, SG, TAP, OKD, APP, NOTE, DONE = .168, .205, .245, .285, .355, .40, .445, .495, .52
    Q = ((.555, .595), (.635, .675))  # the two simple questions: knowledge lights, the answer lands
    S0, S1, S2 = .715, .745, .79      # the sensitive one: flagged, sent down, on the tablet
    g = [glow(1190, 290, 470, "var(--brand)", .5)]

    # ---- the wall screen
    hud = "".join(f'<path d="M{x0} {y0 + dy * 22} V{y0} H{x0 + dx * 22}" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity=".8" transform="translate({dx * -8} {dy * -8})"/>'
                  for x0, y0, dx, dy in ((sx, sy, 1, 1), (sx + sw, sy, -1, 1), (sx, sy + sh, 1, -1), (sx + sw, sy + sh, -1, -1)))
    hud += (f'<rect x="{sx + 2}" y="{sy + 46}" width="{sw - 4}" height="2" fill="var(--c2)" opacity=".16">'
            f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {sh - 52}" dur="5s" repeatCount="indefinite"/></rect>')
    screen = (card(sx, sy, sw, sh, "var(--card)", "var(--c2)", 22, 1.2) + hud
              + f'<path d="M{sx} {sy + 44} H{sx + sw}" stroke="var(--line)" stroke-width="1.5"/>'
              + f'<circle cx="{sx + 24}" cy="{sy + 22}" r="7" fill="var(--c5)">{blink(1.4)}</circle>'
              + T(sx + 42, sy + 28, sl["screen"], fit(sl["screen"], 16, 360, "care center screen"), "var(--white)", W6)
              + pill(sx + sw - 62, sy + 22, sl["live"], ok, ctx, 15, 110, "care center live", 14))

    # left pane: the app's signals (the real trace stays in the band, the forecast leaves it)
    ax, ay, aw, ah = lx, sy + 56, lw, 150
    real = [(0, 96), (26, 92), (52, 98), (78, 90), (104, 94), (130, 86), (156, 90), (182, 82), (208, 78), (224, 76)]
    d = "M" + " L".join(f"{ax + 16 + x} {ay + y}" for x, y in real)
    fx0, fy0 = ax + 16 + real[-1][0], ay + real[-1][1]
    fc = f"M{fx0} {fy0} L{fx0 + 50} {ay + 62} L{ax + aw - 16} {ay + 44}"
    cross = (fx0 + 38, ay + 66)
    chart = (card(ax, ay, aw, ah, "var(--dim)", "var(--line)", 14, 1.5)
             + T(ax + 16, ay + 28, sl["chart"], fit(sl["chart"], 15, 200, "care center chart"), "var(--muted)", W6)
             + T(ax + aw - 16, ay + 28, sl["forecast"], fit(sl["forecast"], 15, 130, "care center forecast"), "var(--c4)", 'text-anchor="end" font-weight="600"')
             + f'<rect x="{ax + 16}" y="{ay + 66}" width="{aw - 32}" height="48" rx="6" fill="var(--c3)" opacity=".08"/>'
             + f'<path d="M{ax + 16} {ay + 66} H{ax + aw - 16}" stroke="var(--c5)" stroke-width="1.2" stroke-dasharray="4 5" opacity=".85"/>')
    lines = (land(f'<path d="{d} L{fx0} {ay + 124} L{ax + 16} {ay + 124} Z" fill="var(--c3)" opacity=".14"/>', .5, .6, 0)
             + trace(d, "var(--c3)", 2, .45, .8)
             + f'<g>{beat("opacity", [(0, 1), (DONE, 1), (DONE + .03, .3), (_B14_END, .3), (_B14_END + .02, 1), (1, 1)])}'
               f'<path d="{fc}" pathLength="1" fill="none" stroke="var(--c4)" stroke-width="1.8" stroke-dasharray="1" stroke-linecap="round">'
               f'{beat("stroke-dashoffset", [(0, 1), (FC, 1), (AL, 0), (_B14_END, 0), (_B14_END + .02, 1), (1, 1)])}</path></g>'
             + f'<path d="{fc}" fill="none" stroke="var(--card)" stroke-width="3" stroke-dasharray="2 7" opacity="0">{_n13_on(AL)}</path>')
    alert = (f'<g opacity="0">{_n13_on(AL, DONE)}'
             f'<circle cx="{cross[0]}" cy="{cross[1]}" r="10" fill="none" stroke="var(--c5)" stroke-width="1.5">{loop("r", "8;20;8", 2.2)}</circle>'
             + pill(ax + aw - 104, ay + ah - 24, sl["alert"], "var(--c5)", ctx, 15, 190, "care center alert", 14) + '</g>'
             + f'<g opacity="0">{_n13_on(DONE)}' + pill(ax + aw - 104, ay + ah - 24, sl["done"], ok, ctx, 15, 190, "care center done", 14) + '</g>')
    # the three steps the signal turns into
    rows = []
    for k, (text, at) in enumerate(zip(sl["steps"], (SG, OKD, APP))):
        y = ay + ah + 12 + 48 * k
        rows.append(f'<g opacity=".32">{_n13_lit(at, .32)}' + card(lx, y, lw, 40, "var(--dim)", "var(--line)", 10, 1.2)
                    + _b14_icon(k, lx + 22, y + 20)
                    + T(lx + 42, y + 26, text, fit(text, 15, lw - 84, "care center step"), "var(--white)", W6) + '</g>'
                    + f'<rect x="{lx}" y="{y}" width="{lw}" height="40" rx="10" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity="0">'
                      f'{beat("opacity", [(0, 0), (at, 0), (at + .01, 1), (at + .06, 1), (at + .09, 0), (1, 0)])}</rect>'
                    + _b14_ok_dot(lx + lw - 22, y + 20, at + .01, ok))
    row_y = [ay + ah + 12 + 48 * k + 20 for k in range(3)]

    # right pane: the queue, answered from the governed knowledge
    qs = sl["tickets"]
    tk_y = [sy + 88 + 66 * k for k in range(3)]
    kb_y = tk_y[-1] + 66
    queue = T(rx, sy + 76, sl["queue"], fit(sl["queue"], 15, 200, "care center queue"), "var(--muted)", W6)
    tickets = []
    for k, (q, y) in enumerate(zip(qs, tk_y)):
        tickets.append(card(rx, y, rw, 58, "var(--dim)", "var(--line)", 10, 1.2)
                       + T(rx + 14, y + 24, q, fit(q, 15, rw - 28, "care center ticket"), "var(--white)", W6))
        at = Q[k][1] if k < 2 else S2 + .01
        tickets.append(f'<g>{_n13_off(at if k < 2 else S0)}' + T(rx + 14, y + 46, sl["new"], 15, "var(--muted)", W6) + '</g>')
        if k < 2:
            tickets.append(f'<g opacity="0">{_n13_on(at)}' + T(rx + 14, y + 46, sl["solved"], fit(sl["solved"], 15, rw - 60, "care center solved"), ok, W6)
                           + '</g>' + _b14_ok_dot(rx + rw - 20, y + 29, at, ok, 9)
                           + _b14_ping(rx + rw / 2, y + 29, 20, 60, at, ok, .05))
        else:
            tickets.append(f'<g opacity="0">{_n13_on(S0, S2 + .01)}' + T(rx + 14, y + 46, sl["sensitive"], fit(sl["sensitive"], 15, rw - 28, "care center sensitive"), "var(--c5)", W6) + '</g>'
                           + f'<g opacity="0">{_n13_on(S2 + .01)}' + T(rx + 14, y + 46, sl["routed"], fit(sl["routed"], 15, rw - 28, "care center routed"), "var(--c4)", W6) + '</g>'
                           + f'<rect x="{rx}" y="{y}" width="{rw}" height="58" rx="10" fill="none" stroke="var(--c5)" stroke-width="1.5" opacity="0">{_n13_on(S0, S2 + .01)}</rect>')
    kb = (card(rx, kb_y, rw, 92, "var(--card)", "var(--c2)", 12, 1.2)
          + T(rx + 14, kb_y + 26, sl["space"], fit(sl["space"], 15, rw - 60, "care center knowledge"), "var(--white)", W6)
          + f'<g transform="translate({rx + rw - 24} {kb_y + 20})"><rect x="-8" y="-3" width="16" height="12" rx="2.5" fill="none" stroke="var(--c2)" stroke-width="1.5"/>'
            '<path d="M-5 -3 V-6 A5 5 0 0 1 5 -6 V-3" fill="none" stroke="var(--c2)" stroke-width="1.5"/></g>')
    for j, name in enumerate(sl["docs"]):
        y = kb_y + 52 + 24 * j
        a0, a1 = Q[j]
        kb += (f'<path d="M{rx + 16} {y - 12} h8 l4 4 v10 h-12 Z" fill="none" stroke="var(--c2)" stroke-width="1.3"/>'
               + T(rx + 38, y, name, fit(name, 15, rw - 56, "care center doc"), "var(--muted)", W6)
               + f'<g opacity="0">{beat("opacity", [(0, 0), (a0, 0), (a0 + .01, 1), (a1 + .02, 1), (a1 + .05, 0), (1, 0)])}'
                 f'<rect x="{rx + 8}" y="{y - 17}" width="{rw - 16}" height="23" rx="6" fill="var(--c4)" opacity=".16"/>'
                 + T(rx + 38, y, name, fit(name, 15, rw - 56, "care center doc"), "var(--c4)", W6) + '</g>'
               + _n13_ride(f"M{rx + rw - 40} {y - 6} C{rx + rw - 10} {y - 40} {rx + rw - 10} {tk_y[j] + 60} {rx + rw - 40} {tk_y[j] + 30}", a0 + .01, a1, 5))
    right = queue + "".join(tickets) + kb

    # ---- the client's phone: the app, where the signal starts and the appointment lands
    px, py, pw, ph = 1356, 540, 176, 256
    pcx = px + pw / 2
    ecg = f"M{px + 18} {py + 206} H{px + 52} L{px + 60} {py + 188} L{px + 70} {py + 222} L{px + 78} {py + 198} L{px + 86} {py + 206} H{pw + px - 18}"
    note_y = py + 62
    phone = (card(px, py, pw, ph, "var(--ink)", "var(--c2)", 26, 1.5)
             + card(px + 8, py + 8, pw - 16, ph - 16, "var(--card)", "var(--line)", 20, 1)
             + f'<rect x="{pcx - 18}" y="{py + 16}" width="36" height="5" rx="2.5" fill="var(--c2)" opacity=".5"/>'
             + T(px + 22, py + 48, sl["app"], fit(sl["app"], 16, 80, "care center app"), "var(--white)", W6)
             + f'<g transform="translate({px + pw - 30} {py + 42}) scale(.8)"><path d="M0 8 C-9 1 -12 -4 -8 -8 C-5 -11 -1 -10 0 -6 C1 -10 5 -11 8 -8 C12 -4 9 1 0 8 Z" fill="var(--accent)"/></g>'
             + bars(px + 22, py + 76, pw - 44, 3, 18, "var(--c2)", ".35")
             + f'<path d="{ecg}" fill="none" stroke="var(--c2)" stroke-width="1.6" stroke-linejoin="round" opacity=".8"/>'
             + f'<g>{loop("opacity", ".35;1;.35", 1.6)}<circle cx="{px + 60}" cy="{py + 188}" r="3.5" fill="var(--c4)"/></g>'
             + _b14_ping(px + 60, py + 188, 4, 30, UP - .03) + _b14_ping(px + 60, py + 188, 4, 30, UP))
    note = (f'<g opacity="0">{_n13_on(NOTE)}'
            + card(px + 14, note_y, pw - 28, 96, "var(--dim)", "var(--c4)", 12, 1.5)
            + f'<g transform="translate({px + 34} {note_y + 26})"><rect x="-10" y="-9" width="20" height="18" rx="3" fill="none" stroke="var(--c4)" stroke-width="1.5"/>'
              '<path d="M-10 -3 H10 M-5 -12 V-6 M5 -12 V-6" stroke="var(--c4)" stroke-width="1.5" stroke-linecap="round"/></g>'
            + T(px + 52, note_y + 32, sl["note"][0], fit(sl["note"][0], 15, pw - 72, "care center note"), "var(--white)", W6)
            + T(px + 26, note_y + 58, sl["note"][1], fit(sl["note"][1], 15, pw - 52, "care center note"), "var(--white)", W6)
            + T(px + 26, note_y + 82, sl["note"][2], fit(sl["note"][2], 15, pw - 52, "care center note"), "var(--c4)", W6)
            + '</g>' + _b14_ping(pcx, note_y + 48, 30, 90, NOTE))
    # the link between the app and the care center, and what travels on it
    lk_top, lk_bot = sy + sh, py
    link = f'<path d="M{pcx} {lk_top} V{lk_bot}" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="3 6" opacity=".7">{loop("stroke-dashoffset", "0;-18", 1.2)}</path>'
    floor_y = sy + sh - 14  # under both panes, inside the screen
    up = _n13_ride(f"M{pcx} {py + 150} V{floor_y} H{gut} V{cross[1]} H{cross[0]}", UP, FC, 6)
    down = _n13_ride(f"M{lx + lw - 22} {row_y[2]} H{gut} V{floor_y} H{pcx} V{note_y + 20}", APP + .005, NOTE, 6)

    # ---- the care-team person with the tablet: «Aprobar», then approved, then the sensitive case with its context
    case = (f'<g opacity="0">{_n13_on(S2)}<rect x="-58" y="-36" width="116" height="74" rx="6" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>'
            + T(-46, -10, sl["case"][0], fit(sl["case"][0], 16, 92, "care center case"), "var(--white)", W6)
            + T(-46, 12, sl["case"][1], fit(sl["case"][1], 15, 92, "care center case"), "var(--c4)", W6)
            + '<rect x="-46" y="22" width="60" height="5" rx="2.5" fill="var(--c2)" opacity=".6"/></g>')
    tap = (f'<g>{_n13_off(TAP)}' + pill(0, 16, sl["approve"], "var(--c4)", ctx, 15, 110, "care center approve", 12) + '</g>'
           f'<g opacity="0">{_n13_on(TAP + .005, S2)}<rect x="-34" y="4" width="68" height="24" rx="12" fill="{ok}"/>' + check(0, 17, .6, "var(--ink)") + '</g>'
           f'<circle cx="30" cy="16" r="6" fill="none" stroke="var(--white)" stroke-width="1.5">{beat("r", [(0, 6), (TAP - .015, 6), (TAP + .06, 34), (1, 34)])}'
           f'{beat("opacity", [(0, 0), (TAP - .015, 0), (TAP - .01, 1), (TAP + .06, 0), (1, 0)])}</circle>' + case)
    bx_, by_ = mnx + 112 + 16 * math.sin(math.radians(10)), mny + 62 + 16 * math.cos(math.radians(10))
    beam_up = f"M{bx_:.0f} {by_ - 14:.0f} C{bx_ + 40:.0f} {by_ - 120:.0f} {gut} {sy + sh + 60} {gut} {sy + sh} V{row_y[1]} H{lx + lw - 22}"
    beam = (f'<g opacity="0">{beat("opacity", [(0, 0), (TAP, 0), (TAP + .003, .9), (OKD, .9), (OKD + .03, 0), (1, 0)])}'
            f'<path d="{beam_up}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="1.5" stroke-linecap="round">'
            f'{beat("stroke-dashoffset", [(0, 1), (TAP, 1), (OKD, 0), (1, 0)])}</path></g>'
            + _n13_ride(beam_up, TAP, OKD, 6))
    beam_down = f"M{rx + 10} {tk_y[2] + 29} H{gut} V{sy + sh} C{gut} {sy + sh + 60} {bx_ + 40:.0f} {by_ - 120:.0f} {bx_ - 20:.0f} {by_ - 40:.0f}"
    sens = _n13_ride(beam_down, S1, S2, 6) + _b14_ping(rx + rw / 2, tk_y[2] + 29, 20, 70, S0, "var(--c5)", .05)
    people = (f'<clipPath id="b14-desk"><rect x="760" y="0" width="840" height="{desk + 2}"/></clipPath>'
              f'<g clip-path="url(#b14-desk)">' + land(_n14_man(mnx, mny, 1.0, SKIN_BROWN, "var(--c1)", tap), .4, .6, 40) + '</g>')
    leds = "".join(f'<circle cx="{860 + k * 26}" cy="{desk + 19}" r="2.2" fill="var(--c2)" opacity=".45"/>' for k in range(6))
    console = land(f'<path d="M820 {desk} H1330 L1318 830 H832 Z" fill="var(--card)"/>'
                   f'<path d="M820 {desk} H1330" stroke="var(--c2)" stroke-width="1.5" opacity=".7"/>' + leds, .2, .5, 20)
    sign = T(sx, sy + sh + 36, sl["sign"], fit(sl["sign"], 20, 360, "care center sign"), "var(--c4)", W6)
    wall = screen + land(chart + "".join(rows) + right, .3, .45, 10) + lines + alert
    ccx, ccy = sx + sw / 2, sy + sh / 2
    return (g[0] + pop(f'<g transform="translate({-ccx} {-ccy})">{wall}</g>', ccx, ccy, .05, .6)
            + land(phone + note, .5, .5, 20) + land(link, .9, .4, 0) + land(sign, 1.4, .45, 10)
            + people + console + up + down + beam + sens), D, FREEZE

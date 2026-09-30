"""Group C · slides 7, 8 and 9 of the energía deck: four hypotheses, the IT delivery cycle and the evidence.

Each scene tells one 12-second story in loop, keyed on seconds of the loop, and every resolved state holds until
_N07_RESET, so the reduced-motion frame (10.8 s) shows the story told: 7, the four hypotheses answered, the enabler
feeding the other three; 8, the change in production, every checkpoint decided by a person, the other three enabled;
9, the tool stuck on the old way, the new way of working reaching value. The figure 70 % is static markup.
Portrait-aware (0.5.0): m07 and m09 hand over to _p07_hipotesis and _p09_evidencia under ORIENT() == "portrait";
m08 (0.6.0) hands over to _pm08_twin, the cycle as a column (its desktop scene stays over 35 KB, untouched)."""
from aula.svg import wrap as _n07_wrap

_N07_RESET = (11.45, 11.8)  # the resolved states fade back to rest before the loop starts over
_N07_EASE = "0.45 0 0.55 1"
_N07_SKIN_MID = f"color-mix(in srgb, {SKIN_BROWN} 55%, {SKIN_LIGHT})"


# ---------------------------------------------------------------- timing, keyed on seconds of the loop
def _n07_kt(pts):
    """[(s, value)] -> (keyTimes, values, n): flat before the first and after the last, strictly increasing."""
    pts = sorted(pts, key=lambda p: p[0])
    if pts[0][0] > 0:
        pts.insert(0, (0, pts[0][1]))
    if pts[-1][0] < D:
        pts.append((D, pts[-1][1]))
    kt, last = [], None
    for t, _v in pts:
        f = 0.0 if last is None else min(1.0, max(t / D, last + .0005))
        kt.append(f)
        last = f
    kt[-1] = 1.0
    return ";".join(f"{k:.4f}" for k in kt), ";".join(str(v) for _t, v in pts), len(pts)


def _n07_key(attr, pts, mode="linear"):
    kt, vals, _n = _n07_kt(pts)
    return f'<animate attributeName="{attr}" values="{vals}" keyTimes="{kt}" dur="{D}s" repeatCount="indefinite" calcMode="{mode}"/>'


def _n07_tr(pts, typ="translate"):
    """An eased transform keyed on seconds: pts = [(s, "x y")]."""
    kt, vals, n = _n07_kt(pts)
    return (f'<animateTransform attributeName="transform" type="{typ}" values="{vals}" keyTimes="{kt}" dur="{D}s" '
            f'repeatCount="indefinite" calcMode="spline" keySplines="{";".join([_N07_EASE] * (n - 1))}"/>')


def _n07_hold(on, fade=.15, lo=0, hi=1):
    """lo until `on`, hi until the reset: a resolved state that the frozen frame keeps."""
    r0, r1 = _N07_RESET
    return _n07_key("opacity", [(on, lo), (on + fade, hi), (r0, hi), (r1, lo)])


def _n07_win(a, b, fade=.25):
    """Visible between a and b seconds."""
    return _n07_key("opacity", [(a, 0), (a + fade, 1), (b - fade, 1), (b, 0)])


def _n07_move(path, pts):
    """Travel along path: pts = [(s, fraction of the path)]."""
    return move(path, [(t / D, f) for t, f in pts], D)


def _n07_ping(x, y, r0, r1, at, color="var(--c4)", sw=1.5, dur=.6):
    """A ring that opens once at `at` seconds."""
    return (f'<circle cx="{x}" cy="{y}" r="{r0}" fill="none" stroke="{color}" stroke-width="{sw}" opacity="0">'
            + _n07_key("r", [(at, r0), (at + dur, r1), (at + dur + .01, r0)])
            + _n07_key("opacity", [(at - .01, 0), (at, .9), (at + dur, 0)]) + '</circle>')


def _n07_badge(x, y, at, ok, r=11):
    """The ok badge with its check: appears at `at` and holds."""
    return f'<g opacity="0">{_n07_hold(at)}<circle cx="{x}" cy="{y}" r="{r}" fill="{ok}"/>{check(x, y + 1, r / 15, "var(--ink)")}</g>'


def _n07_chars(text, size, room):
    """The widest wrap (in characters) whose every line fits room units at size."""
    s = _(str(text))
    for n in range(48, 7, -1):
        if all(bold_width(line, size, current_factor()) <= room for line in _n07_wrap(s, n)):
            return n
    return 8


def _n07_bust(x, y, s, skin, shirt, long_hair=False):
    """A faceless head and shoulders around the head's center, in the style of _woman and _man."""
    rim = 'fill="none" stroke="var(--c2)" stroke-width="1.2" opacity=".55"'
    back = (f'<path d="M-11 -2 C-13 -15 -4 -18 1 -17.5 C8 -17 13 -12 12 -2 L12 13 C7 16 -7 16 -12 13 Z" fill="{HAIR}"/>'
            if long_hair else "")
    body = (f'<path d="M-21 31 C-21 19 -13 14 0 14 C13 14 21 19 21 31 Z" fill="{shirt}"/><path d="M-21 31 C-21 19 -13 14 0 14 C13 14 21 19 21 31" {rim}/>'
            f'<rect x="-3.5" y="8" width="7" height="7" fill="{shade(skin, 14)}"/>'
            f'<ellipse cx="0" cy="0" rx="9" ry="10.5" fill="{skin}"/>'
            f'<path d="M-9.6 -1 C-10.4 -12 -3 -15.5 2 -15 C8 -14.6 10.8 -8.5 9.8 -2 C6.5 -8.4 -2 -9.2 -9.6 -1 Z" fill="{HAIR}"/>')
    return f'<g transform="translate({x} {y}) scale({s})">{back}{body}</g>'


# ---------------------------------------------------------------- 7 · four hypotheses, three with a return and one enabler
def _n07_alarms(a, R):
    """Confiabilidad: four alarms in arrival order; the AI scans them and lifts the one that matters to the top."""
    r0, r1 = R
    scan, lift, done = a + .15, a + .75, a + 1.3
    rows = ((118, False), (86, False), (140, True), (64, False))
    shift = (28, 28, -56, 0)
    out = []
    for k, ((w, hot), dy) in enumerate(zip(rows, shift)):
        y = 6 + 28 * k
        dot = (f'<circle cx="12" cy="{y + 10}" r="4.5" fill="var(--c5)">{loop("r", "4;6;4", 1.2)}</circle>' if hot else
               f'<circle cx="12" cy="{y + 10}" r="4" fill="var(--c2)">{loop("opacity", ".35;1;.35", 1.4, k * .45)}</circle>')
        row = (card(0, y, 196, 20, "var(--dim)", "var(--line)", 6, 1) + dot
               + f'<rect x="26" y="{y + 7}" width="{w}" height="6" rx="3" fill="{"var(--c5)" if hot else "var(--c2)"}" opacity="{".85" if hot else ".45"}"/>')
        if not hot:
            row = f'<g>{_n07_key("opacity", [(done, 1), (done + .3, .45), (r0, .45), (r1, 1)])}{row}</g>'
        out.append(f'<g>{_n07_tr([(lift, "0 0"), (lift + .5, f"0 {dy}"), (r0, f"0 {dy}"), (r1, "0 0")])}{row}</g>')
    beam = (f'<g opacity="0">{_n07_key("opacity", [(scan, 0), (scan + .05, 1), (scan + .5, 1), (scan + .6, 0)])}'
            f'<g>{_n07_tr([(scan, "0 0"), (scan + .55, "0 116")])}<path d="M0 2 H196" stroke="var(--c4)" stroke-width="1.5"/>'
            f'{spark(188, 2, .35)}</g></g>')
    first = (f'<g opacity="0">{_n07_hold(done)}<rect x="-3" y="3" width="202" height="26" rx="8" fill="none" stroke="var(--c4)" stroke-width="1.5"/>'
             f'<g transform="translate(180 15) scale(.24)">{lens(0, 0)}</g></g>')
    return "".join(out) + beam + first


def _n07_spare(a, ok):
    """Supply chain: the equipment will need the part; it leaves the warehouse and is there before anyone asks."""
    route = "M40 86 C78 118 124 114 140 94"
    wh = ('<path d="M8 58 L34 36 L60 58" fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-linejoin="round"/>'
          + card(12, 58, 44, 38, "var(--dim)", "var(--c2)", 3, 1.2)
          + '<rect x="27" y="74" width="14" height="22" rx="2" fill="none" stroke="var(--c2)" stroke-width="1.2"/>')
    eq = (f'<circle cx="160" cy="62" r="26" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.2"/>'
          f'<g>{spin(160, 62, 3)}<path d="M160 52 V72 M151.3 57 L168.7 67 M151.3 67 L168.7 57" stroke="var(--c2)" stroke-width="1.5" stroke-linecap="round"/></g>'
          f'<circle cx="160" cy="62" r="10" fill="none" stroke="var(--c2)" stroke-width="1.5"/>')
    path = (f'<path d="{route}" fill="none" stroke="var(--c2)" stroke-width="1.8" stroke-dasharray="4 6">'
            f'{loop("stroke-dashoffset", "0;-18", 1.2)}</path>')
    need = _n07_ping(160, 62, 26, 44, a + .15, "var(--c4)") + _n07_ping(160, 62, 26, 44, a + .55, "var(--c4)")
    hint = f'<g opacity="0">{_n07_key("opacity", [(a + .1, 0), (a + .2, 1), (a + 1.2, 1), (a + 1.4, 0)])}{spark(160, 24, .45)}</g>'
    part = (f'<g>{_n07_move(route, [(a + .55, 0), (a + 1.4, 1)])}'
            '<rect x="-8" y="-8" width="16" height="16" rx="2.5" fill="var(--c4)" fill-opacity=".3" stroke="var(--c4)" stroke-width="1.6"/>'
            '<path d="M-8 -2 H8 M0 -8 V-2" stroke="var(--c4)" stroke-width="1.2"/></g>')
    return wh + eq + path + need + hint + part + _n07_badge(186, 36, a + 1.45, ok)


def _n07_papers(a, ok):
    """Procesos y documentos: the AI reads the document and fills the form; nobody retypes it."""
    lines = "".join(f'<rect x="14" y="{24 + 12 * k}" width="{w}" height="5" rx="2.5" fill="var(--c2)" opacity=".5"/>'
                    for k, w in enumerate((38, 30, 40, 24, 34)))
    page = (card(4, 8, 60, 82, "var(--dim)", "var(--c2)", 6, 1.2) + lines
            + '<path d="M50 8 L64 22" stroke="var(--c2)" stroke-width="1.2"/>')
    scan = (f'<g opacity="0">{_n07_key("opacity", [(a + .15, 0), (a + .2, 1), (a + .7, 1), (a + .8, 0)])}'
            f'<g>{_n07_tr([(a + .15, "0 0"), (a + .75, "0 74")])}<path d="M0 12 H68" stroke="var(--c4)" stroke-width="1.5"/></g>'
            f'{spark(64, 8, .4)}</g>')
    form = []
    for k in range(3):
        y, t = 12 + 30 * k, a + .8 + .22 * k
        fly = f"M66 {30 + 16 * k} C88 {30 + 16 * k} 96 {y + 9} 128 {y + 9}"
        form.append(f'<rect x="100" y="{y + 6}" width="20" height="6" rx="3" fill="var(--c2)" opacity=".5"/>'
                    + card(128, y, 68, 18, "var(--ink)", "var(--line)", 4, 1)
                    + f'<rect x="132" y="{y + 6}" width="58" height="6" rx="3" fill="var(--c2)">{_n07_key("width", [(t + .15, 0), (t + .45, 58), (_N07_RESET[0], 58), (_N07_RESET[1], 0)])}</rect>'
                    + f'<g opacity="0">{_n07_key("opacity", [(t - .01, 0), (t, 1), (t + .2, 1), (t + .21, 0)])}{_n07_move(fly, [(t, 0), (t + .2, 1)])}<circle r="3.5" fill="var(--c4)"/></g>')
    return page + scan + "".join(form) + _n07_badge(186, 104, a + 1.6, ok)


def _n07_glyph(k):
    """The four steps of the delivery cycle as glyphs around 0,0: requirement, code, test, deploy (icons.py «entrega»)."""
    return icon(icons("entrega")[k], 0, 0, 30, "var(--c2)", 1.5)


# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
def _p07_text(x, y, text, size, room, fill, lines=2, lh=1.3, anchor="start"):
    """text wrapped into room at the largest size (never under 18: the phone floor) that fits in `lines` lines."""
    z = size
    while z > 18 and len(_n07_wrap(_(str(text)), _n07_chars(text, z, room))) > lines:
        z -= 1
    return TCW(x, y, text, _n07_chars(text, z, room), z, fill, W6, lh, anchor)


def _p07_hipotesis(sl, ctx):
    """m07 on the 900x1600 stage: the three hypotheses as full-width rows (text on the left, their small story on the
    right), the enabler under them, a spine on the left carrying its pulse into each row. Same loop and frozen frame."""
    ok = ctx.brand.c("dark.ok")
    cols = ("var(--c1)", "var(--c3)", "var(--c2)", "var(--accent)")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    SX, X0 = zx + 20, zx + 44                        # the spine, the cards' left edge
    W, RH, GAP = zx + zw - X0, 168, 12
    ys = [zy + 22 + k * (RH + GAP) for k in range(3)]      # 22 below the zone's top: the «?» must not reach the text
    BY, BH = ys[-1] + RH + 26, 304
    wins = ((2.2, 4.6), (4.6, 7.0), (7.0, 9.4), (9.4, _N07_RESET[0]))
    R = _N07_RESET
    room = W - 24 - 262                               # the text column of a row; the story sits on the right

    def qmark(cx, cy, a):
        return (f'<circle cx="{cx}" cy="{cy}" r="20" fill="var(--card)" stroke="var(--c4)" stroke-width="1.8"/>'
                + TC(cx, cy + 8.5, "?", 24, "var(--c4)", W6) + _n07_ping(cx, cy, 20, 38, a + .05) + _n07_ping(cx, cy, 20, 38, a + .45))

    def spot(x, y, w, h, a, b):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="none" stroke="var(--c4)" stroke-width="2.4" opacity="0">{_n07_win(a, b)}</rect>'

    art, text = [glow(zx + zw / 2, zy + zh * .45, 470, "var(--brand)", .45)], []
    stories = (_n07_alarms(wins[0][0], R), _n07_spare(wins[1][0], ok), _n07_papers(wins[2][0], ok))
    f = current_factor()
    for k in range(3):
        y, (area, idea, gain), (a, b), at = ys[k], sl["cards"][k], wins[k], .1 + .12 * k
        art.append(land(card(X0, y, W, RH, "var(--card)", "var(--line)", 18, 1.2)
                        + f'<rect x="{X0 + 18}" y="{y - 2}" width="{W * .4:.0f}" height="4" rx="2" fill="{cols[k]}"/>'
                        + f'<g transform="translate({X0 + W - 244} {y + 22}) scale(1.1)">{stories[k]}</g>'
                        + spot(X0, y, W, RH, a, b) + qmark(X0 + W - 30, y, a), at, .5, 16))
        rs = 20
        rw = bold_width(_(str(sl["ret"])), rs, f)
        text.append(land(T(X0 + 24, y + 42, area, fit(area, 26, room, "hypothesis area", floor=18), "var(--white)", W6)
                         + _p07_text(X0 + 24, y + 76, idea, 21, room, "var(--muted)")
                         + T(X0 + 24, y + 148, sl["ret"], rs, "var(--muted)", W6)
                         + T(f"{X0 + 36 + rw:.1f}", y + 148, gain, fit(gain, 24, room - rw - 12, "hypothesis return", floor=18), "var(--c4)", W6),
                         at, .5, 16))
    # the enabler: its delivery cycle, four steps and a track the change runs along
    area, idea, gain = sl["cards"][3]
    a4 = wins[3][0]
    mid = X0 + W / 2
    nodes = [mid + (k - 1.5) * 150 for k in range(4)]
    ny, trk = BY + 170, BY + 214
    pipe = (f'<path d="M{nodes[0]} {ny} H{nodes[-1]}" stroke="var(--line)" stroke-width="2"/>'
            + "".join(card(x - 32, ny - 32, 64, 64, "var(--dim)", "var(--line)", 14, 1.2) + icon(icons("entrega")[k], x, ny, 38, "var(--c2)", 1.5)
                      + f'<rect x="{x - 32}" y="{ny - 32}" width="64" height="64" rx="14" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_n07_hold(a4 + .12 + .17 * k, .1)}</rect>'
                      for k, x in enumerate(nodes))
            + f'<path d="M{nodes[0]} {trk} H{nodes[-1]}" stroke="var(--line)" stroke-width="2"/>'
            + f'<path d="M{nodes[0]} {trk} H{nodes[-1]}" stroke="var(--c4)" stroke-width="2" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">'
              f'{_n07_key("stroke-dashoffset", [(a4 + .1, 1), (a4 + .66, 0), (R[0], 0), (R[1], 1)])}</path>'
            + f'<g opacity="0">{_n07_key("opacity", [(a4 + .05, 0), (a4 + .1, 1), (a4 + .66, 1), (a4 + .72, 0)])}'
              f'{_n07_move(f"M{nodes[0]} {trk} H{nodes[-1]}", [(a4 + .1, 0), (a4 + .66, 1)])}{token("var(--c4)", 6)}</g>')
    art.append(land(card(X0, BY, W, BH, "var(--card)", "var(--line)", 18, 1.2)
                    + f'<rect x="{X0 + 18}" y="{BY - 2}" width="{W * .6:.0f}" height="4" rx="2" fill="{cols[3]}"/>'
                    + pipe + spot(X0, BY, W, BH, *wins[3]) + qmark(X0 + W - 30, BY, a4), .46, .5, 16))
    text.append(land(T(X0 + 24, BY + 44, area, fit(area, 26, W - 100, "hypothesis area", floor=18), "var(--white)", W6)
                     + _p07_text(X0 + 24, BY + 80, idea, 21, W - 48, "var(--muted)")
                     + TC(f"{mid:.1f}", BY + 250, sl["cycle"], fit(sl["cycle"], 20, W - 48, "hypothesis cycle", floor=18), "var(--muted)", W6)
                     + T(X0 + 24, BY + 288, gain, fit(gain, 24, W - 48, "hypothesis enabler", floor=18), "var(--c4)", W6), .46, .5, 16))
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


@register("scene", "m07_hipotesis")
def sc_m07_hipotesis(sl, ctx):
    """Three hypotheses with a possible return stand on a fourth, technology, that enables them. The loop visits each
    card in turn and plays its small story (the alarm that matters goes first, the spare part is there before it is
    asked for, the document fills its own form); then the enabler runs its delivery cycle and powers the three.
    Every card keeps its «?»: hypotheses to validate together."""
    if ORIENT() == "portrait":
        return _p07_hipotesis(sl, ctx)
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
    stories = (_n07_alarms(wins[0][0], R), _n07_spare(wins[1][0], ok), _n07_papers(wins[2][0], ok))
    parts = []
    for k in range(3):
        x, (area, idea, gain), (a, b) = xs[k], sl["cards"][k], wins[k]
        c = (card(x, Y0, W, H, "var(--card)", "var(--line)", 18, 1.2)
             + f'<rect x="{x + 18}" y="{Y0 - 2}" width="{W - 70}" height="4" rx="2" fill="{cols[k]}"/>'
             + T(x + 18, Y0 + 46, area, fit(area, 18, W - 36, "hypothesis area"), "var(--white)", W6)
             + TCW(x + 18, Y0 + 80, idea, _n07_chars(idea, 16, W - 36), 16, "var(--muted)", W6, 1.35, "start")
             + f'<g transform="translate({x + 18} {Y0 + 170})">{stories[k]}</g>'
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
    # the enabler powers the three: a pulse climbs each pillar into its card
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


# ---------------------------------------------------------------- 8 · the delivery cycle: agents do, people decide
def _pm08_twin(sl, ctx):
    """m08 on the 900x1600 stage: the cycle turned into a column. The agent rail runs down the left, one node per step;
    the four steps stack in the middle, each with its glyph and a bar the agent fills while the change is in it; the
    track runs down their right edge with its three checkpoints, and the person who decides at each one stands beside
    it. The ruler (request to production) and the three enabled areas sit under the column. Same seconds as the
    desktop loop, same frozen frame: the change in production, every checkpoint decided, the other three enabled."""
    ok = ctx.brand.c("dark.ok")
    R = _N07_RESET
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    RX, X0, TW, TH, TX, PX = zx + 32, zx + 72, 420, 88, zx + 540, zx + 640
    t0, t1 = zy + 60, zy + 500                           # the track, top to bottom
    tys = [zy + 72 + 112 * k for k in range(4)]          # the steps' tops
    cys = [y + TH // 2 for y in tys]
    cpy = [y + TH + 12 for y in tys[:3]]                 # the checkpoints, in the gaps between steps
    go, live = 2.0, 9.95
    tile_on = ((2.3, 3.35), (4.45, 5.5), (6.6, 7.65), (8.75, 9.8))
    cp_on = ((3.6, 4.15), (5.75, 6.3), (7.9, 8.45))
    decided = [a + .3 for a, _b in cp_on]
    span = t1 - t0
    stops = [(go, 0)]
    for k in range(4):
        f = round((cys[k] - t0) / span, 4)
        stops += [(tile_on[k][0], f), (tile_on[k][1], f)]
        if k < 3:
            f = round((cpy[k] - t0) / span, 4)
            stops += [(cp_on[k][0], f), (cp_on[k][1], f)]
    stops.append((live, 1))
    art, text = [glow(zx + zw / 2, zy + 300, 420, "var(--brand)", .4)], []
    # the header: the agents, and the hypothesis still to validate
    text.append(land(T(zx, zy + 34, sl["agents"], fit(sl["agents"], 24, 470, "agent rail", floor=20), "var(--c4)", W6)
                     + T(zx + zw - 40, zy + 34, sl["tag"], fit(sl["tag"], 21, 250, "hypothesis tag", floor=20), "var(--muted)", 'text-anchor="end" font-weight="600"')
                     + f'<circle cx="{zx + zw - 14}" cy="{zy + 27}" r="15" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>'
                     + TC(zx + zw - 14, zy + 34, "?", 20, "var(--c4)", W6), .1, .5, -12))
    # the agent rail, down the left: a node per step that wakes while the change is in it
    rail = (f'<path d="M{RX} {t0} V{t1}" stroke="var(--c4)" stroke-width="1.2" opacity=".35"/>'
            f'<path d="M{RX} {t0} V{t1}" stroke="var(--c4)" stroke-width="1.2" stroke-dasharray="2 10" opacity=".8">{loop("stroke-dashoffset", "0;-24", 1.6)}</path>')
    for k, cy in enumerate(cys):
        a, b = tile_on[k]
        rail += (f'<circle cx="{RX}" cy="{cy}" r="18" fill="var(--ink)" stroke="var(--c4)" stroke-width="1.2"/>'
                 f'<g transform="translate({RX} {cy})"><g>{_n07_tr([(a - .1, "1"), (a + .1, "1.35"), (b - .1, "1.35"), (b + .1, "1")], "scale")}{spark(0, 0, .6)}</g></g>'
                 + _n07_ping(RX, cy, 18, 34, a)
                 + f'<path d="M{RX + 20} {cy} H{X0 - 4}" stroke="var(--c4)" stroke-width="1.5" stroke-dasharray="3 4" opacity="0">{_n07_win(a - .1, b + .1, .12)}</path>')
    art.append(land(rail, .1, .5, 0))
    # the four steps: glyph, name, and the bar the agent fills (it stays full: the work is done)
    tiles, names = [], []
    bw = TW - 116
    for k, (y, cy, name) in enumerate(zip(tys, cys, sl["steps"])):
        a, b = tile_on[k]
        tiles.append(card(X0, y, TW, TH, "var(--card)", "var(--c2)", 14, 1.2) + icon(icons("entrega")[k], X0 + 48, cy, 44, "var(--c2)", 1.5)
                     + f'<rect x="{X0 + 96}" y="{cy + 14}" width="{bw}" height="6" rx="3" fill="var(--line)"/>'
                     + f'<rect x="{X0 + 96}" y="{cy + 14}" width="{bw}" height="6" rx="3" fill="var(--c4)">'
                     + _n07_key("width", [(a + .1, 0), (b - .1, bw), (R[0], bw), (R[1], 0)]) + '</rect>'
                     + f'<rect x="{X0}" y="{y}" width="{TW}" height="{TH}" rx="14" fill="none" stroke="var(--c4)" stroke-width="2.4" opacity="0">{_n07_win(a - .1, b + .1, .12)}</rect>'
                     + f'<path d="M{X0 + TW} {cy} H{TX}" stroke="var(--line)" stroke-width="1.5"/>')
        names.append(T(X0 + 96, cy - 4, name, fit(name, 24, bw, "delivery step", floor=20), "var(--white)", W6))
    art.append(seq(tiles, .2, .45, 16))
    text.append(land("".join(names), .3, .5, 16))
    # the track, its checkpoints, and the person who decides at each one
    track = (f'<path d="M{TX} {t0} V{t1}" stroke="var(--line)" stroke-width="2"/>'
             f'<path d="M{TX} {t0} V{t1}" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="4 12" opacity=".6">{loop("stroke-dashoffset", "0;-32", 1.8)}</path>')
    people = ""
    looks = ((_N07_SKIN_MID, "var(--c3)", True), (SKIN_BROWN, "var(--c1)", False), (SKIN_LIGHT, "var(--accent)", True))
    for k, y in enumerate(cpy):
        a, _b = cp_on[k]
        track += (f'<circle cx="{TX}" cy="{y}" r="16" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.5"/><circle cx="{TX}" cy="{y}" r="5" fill="var(--c2)"/>'
                  + _n07_ping(TX, y, 16, 34, a) + _n07_badge(TX, y, decided[k], ok, 16))
        skin, shirt, hair = looks[k]
        people += (f'<path d="M{TX + 18} {y} H{PX - 34}" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="2 4" opacity=".7"/>'
                   + _n07_bust(PX, y - 8, 1.25, skin, shirt, hair)
                   + f'<circle cx="{PX}" cy="{y + 2}" r="40" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_n07_win(a, decided[k] + .3, .12)}</circle>')
    art.append(land(track, .45, .4, 0) + land(people, .75, .55, 16))
    text.append(land(TCW(PX + 60, cys[3] + 4, sl["people"], _n07_chars(sl["people"], 21, 250), 21, "var(--white)", W6, 1.25), .75, .55, 16))
    art.append(f'<g opacity="0">{_n07_key("opacity", [(go, 0), (go + .15, 1), (live, 1), (live + .12, 0)])}'
               f'{_n07_move(f"M{TX} {t0} V{t1}", stops)}{token("var(--c4)", 7)}</g>')
    # the measure: a ruler from the request to production that fills while the change travels
    ry = zy + 574
    ew = bold_width(_(str(sl["end"])), 20, current_factor()) + 32
    text.append(land(T(zx, ry - 24, sl["start"], fit(sl["start"], 21, 380, "ruler start", floor=20), "var(--muted)", W6)
                     + f'<g>{_n07_key("opacity", [(live, 1), (live + .1, 0), (R[0], 0), (R[1], 1)])}'
                     + T(zx + zw, ry - 24, sl["end"], fit(sl["end"], 21, 380, "ruler end", floor=20), "var(--muted)", 'text-anchor="end" font-weight="600"') + '</g>'
                     + f'<g opacity="0">{_n07_hold(live, .1)}' + pill(zx + zw - ew / 2, ry - 31, sl["end"], ok, ctx, 20, ew, "ruler end", 16) + '</g>'
                     + TC(zx + zw / 2, ry + 38, sl["measure"], fit(sl["measure"], 22, 600, "ruler measure", floor=20), "var(--c4)", W6), 1.05, .45, 10))
    art.append(land(f'<path d="M{zx} {ry} H{zx + zw}" stroke="var(--line)" stroke-width="2"/>'
                    f'<path d="M{zx + 1} {ry - 10} V{ry + 10} M{zx + zw - 1} {ry - 10} V{ry + 10}" stroke="var(--c2)" stroke-width="1.5"/>'
                    f'<path d="M{zx + 2} {ry} H{zx + zw - 2}" stroke="var(--c4)" stroke-width="3" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">'
                    f'{_n07_key("stroke-dashoffset", [(go, 1), (live, 0), (R[0], 0), (R[1], 1)])}</path>', 1.05, .45, 10))
    # production enables the other three
    ey, aw = ry + 70, (zw - 64) // 3
    cols = ("var(--c1)", "var(--c3)", "var(--c2)")
    en = (card(zx, ey, zw, 206, "var(--card)", "var(--line)", 18, 1.2)
          + f'<path d="M{zx + zw - 30} {ry + 12} V{ey}" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="3 5"/>')
    en_t = T(zx + 24, ey + 40, sl["enables"], fit(sl["enables"], 23, zw - 48, "enabler title", floor=20), "var(--white)", W6)
    for k, name in enumerate(sl["areas"]):
        x, y, at = zx + 20 + (aw + 12) * k, ey + 62, live + .18 + .1 * k
        en += (card(x, y, aw, 124, "var(--dim)", "var(--line)", 12, 1.2) + f'<rect x="{x}" y="{y + 18}" width="4" height="88" rx="2" fill="{cols[k]}"/>'
               + f'<rect x="{x}" y="{y}" width="{aw}" height="124" rx="12" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_n07_hold(at, .1)}</rect>'
               + f'<g opacity="0">{_n07_hold(at, .1)}{spark(x + aw - 22, y + 22, .5)}</g>' + _n07_ping(x + aw - 22, y + 22, 6, 24, at, dur=.35))
        en_t += _p07_text(x + 20, y + 58, name, 22, aw - 50, "var(--white)")
    art.append(land(en, 1.25, .5, 14))
    text.append(land(en_t, 1.25, .5, 14))
    art.append(f'<g opacity="0">{_n07_key("opacity", [(live, 0), (live + .03, 1), (live + .2, 1), (live + .24, 0)])}'
               f'{_n07_move(f"M{zx + zw - 30} {ry + 12} V{ey}", [(live + .02, 0), (live + .2, 1)])}{token("var(--c4)", 6)}</g>')
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "m08_ti")
def sc_m08_ti(sl, ctx):
    """A change request travels the cycle: requirement, code, test, deploy. A rail of agents works above each step
    while the change is in it; below, at each checkpoint, a person decides and the change moves on. The ruler under the
    cycle is the measure (from the request to production) and fills while it travels; in production, the change
    enables the other three hypotheses."""
    if ORIENT() == "portrait":
        return _pm08_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    R = _N07_RESET
    TW, TY, TH, TRK = 136, 196, 114, 334
    xs = [832 + 196 * k for k in range(4)]
    cxs = [x + TW / 2 for x in xs]
    cps = [x + TW + 30 for x in xs[:3]]
    # the change: (seconds, x) stops along the track; tiles hold it, checkpoints wait for a person
    go = 2.0
    tile_on = ((2.3, 3.35), (4.45, 5.5), (6.6, 7.65), (8.75, 9.8))
    cp_on = ((3.6, 4.15), (5.75, 6.3), (7.9, 8.45))
    stops = [(go, 832)]
    for k in range(4):
        stops += [(tile_on[k][0], cxs[k]), (tile_on[k][1], cxs[k])]
        if k < 3:
            stops += [(cp_on[k][0], cps[k] - 24), (cp_on[k][1], cps[k] - 24)]
    live = 9.95
    stops.append((live, 1556))
    decided = [a + .3 for a, _b in cp_on]

    g = [glow(1190, 330, 460, "var(--brand)", .45)]
    # the agent rail, above the cycle
    rail = (T(832, 118, sl["agents"], fit(sl["agents"], 16, 400, "agent rail"), "var(--c4)", W6)
            + T(1518, 118, sl["tag"], fit(sl["tag"], 15, 240, "hypothesis tag"), "var(--muted)", 'text-anchor="end" font-weight="600"')
            + '<circle cx="1541" cy="113" r="13" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>' + TC(1541, 119, "?", 16, "var(--c4)", W6)
            + '<path d="M832 146 H1556" stroke="var(--c4)" stroke-width="1.2" opacity=".35"/>'
            + f'<path d="M832 146 H1556" stroke="var(--c4)" stroke-width="1.2" stroke-dasharray="2 10" opacity=".8">{loop("stroke-dashoffset", "0;-24", 1.6)}</path>')
    agents = []
    for k, cx in enumerate(cxs):
        a, b = tile_on[k]
        agents.append(f'<circle cx="{cx}" cy="146" r="14" fill="var(--ink)" stroke="var(--c4)" stroke-width="1.2"/>'
                      f'<g><g transform="translate({cx} 146)"><g>{_n07_tr([(a - .1, "1"), (a + .1, "1.35"), (b - .1, "1.35"), (b + .1, "1")], "scale")}'
                      f'{spark(0, 0, .5)}</g></g></g>'
                      + _n07_ping(cx, 146, 14, 28, a) +
                      f'<path d="M{cx} 162 V{TY - 4}" stroke="var(--c4)" stroke-width="1.5" stroke-dasharray="3 4" opacity="0">'
                      f'{_n07_win(a - .1, b + .1, .12)}{loop("stroke-dashoffset", "0;-14", .6)}</path>')
    # the four steps, each with the agent's work drawn in while the change is in it
    tiles = []
    for k, (x, cx, name) in enumerate(zip(xs, cxs, sl["steps"])):
        a, b = tile_on[k]
        dur = b - a
        work = ""
        if k == 0:  # the requirement is written
            work = (card(cx - 22, 208, 44, 54, "var(--dim)", "var(--c2)", 5, 1.2)
                    + f'<path d="M{cx + 10} 208 L{cx + 22} 220" stroke="var(--c2)" stroke-width="1.2"/>'
                    + "".join(f'<rect x="{cx - 14}" y="{224 + 9 * j}" width="{w}" height="4" rx="2" fill="{"var(--c4)" if j == 0 else "var(--c2)"}">'
                              f'{_n07_key("width", [(a + .15 + .22 * j, 0), (a + .37 + .22 * j, w), (R[0], w), (R[1], 0)])}</rect>'
                              for j, w in enumerate((16, 28, 22, 26))))
        elif k == 1:  # the code is typed
            work = (card(cx - 34, 210, 68, 50, "var(--dim)", "var(--c2)", 5, 1.2)
                    + "".join(f'<rect x="{cx - 26 + ind}" y="{220 + 10 * j}" width="{w}" height="4" rx="2" fill="{c}">'
                              f'{_n07_key("width", [(a + .1 + .22 * j, 0), (a + .32 + .22 * j, w), (R[0], w), (R[1], 0)])}</rect>'
                              for j, (ind, w, c) in enumerate(((0, 30, "var(--c4)"), (8, 36, "var(--c2)"), (8, 24, "var(--c2)"), (0, 16, "var(--c4)")))))
        elif k == 2:  # the tests pass, one by one
            for j in range(3):
                y = 218 + 17 * j
                work += (f'<rect x="{cx - 12}" y="{y - 3}" width="38" height="6" rx="3" fill="var(--c2)" opacity=".5"/>'
                         f'<circle cx="{cx - 24}" cy="{y}" r="6" fill="none" stroke="var(--c2)" stroke-width="1.2"/>'
                         f'<g opacity="0">{_n07_hold(a + .2 + .28 * j, .08)}<circle cx="{cx - 24}" cy="{y}" r="6.5" fill="{ok}"/>{check(cx - 24, y + .5, .42, "var(--ink)")}</g>')
        else:  # the release goes live, rack by rack
            for j in range(3):
                y = 212 + 17 * j
                work += (card(cx - 28, y, 56, 13, "var(--dim)", "var(--c2)", 3, 1.2)
                         + f'<rect x="{cx - 22}" y="{y + 5}" width="22" height="3" rx="1.5" fill="var(--c2)" opacity=".5"/>'
                         + f'<circle cx="{cx + 19}" cy="{y + 6.5}" r="3" fill="var(--line)"/>'
                         + f'<circle cx="{cx + 19}" cy="{y + 6.5}" r="3" fill="{ok}" opacity="0">{_n07_hold(a + .15 + .2 * j, .08)}</circle>')
        t = (card(x, TY, TW, TH, "var(--card)", "var(--c2)", 14, 1.2) + work
             + TC(cx, TY + 96, name, fit(name, 16, TW - 16, "delivery step"), "var(--white)", W6)
             + f'<rect x="{x}" y="{TY}" width="{TW}" height="{TH}" rx="14" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_n07_win(a - .1, b + .1, .12)}</rect>')
        tiles.append(t)
    # the track, the checkpoints and the people who decide at them
    track = (f'<path d="M832 {TRK} H1556" stroke="var(--line)" stroke-width="2"/>'
             f'<path d="M832 {TRK} H1556" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="4 12" opacity=".6">{loop("stroke-dashoffset", "0;-32", 1.8)}</path>')
    gates, people = [], []
    tablet = ('<rect x="-34" y="4" width="68" height="24" rx="12" fill="none" stroke="var(--c4)" stroke-width="2.5"/>'
              f'<g opacity="0">{_n07_hold(decided[1], .1)}<rect x="-34" y="4" width="68" height="24" rx="12" fill="{ok}"/>{check(0, 17, .8, "var(--ink)")}</g>')
    who = (lambda x: _woman(x - 44, 420, .38, _N07_SKIN_MID, "var(--c3)"),
           lambda x: _man(x - 6, 420, .38, SKIN_BROWN, "var(--c1)", tablet),
           lambda x: _woman(x - 44, 420, .38, SKIN_LIGHT, "var(--accent)"))
    for k, x in enumerate(cps):
        a, b = cp_on[k]
        gates.append(f'<circle cx="{x}" cy="{TRK}" r="14" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.5"/>'
                     f'<circle cx="{x}" cy="{TRK}" r="4" fill="var(--c2)"/>'
                     + _n07_ping(x, TRK, 14, 30, a, "var(--c4)") + _n07_badge(x, TRK, decided[k], ok, 14))
        people.append(f'<path d="M{x} {TRK + 16} V{TRK + 34}" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="2 4" opacity=".7"/>' + who[k](x))
    change = (f'<g opacity="0">{_n07_key("opacity", [(go, 0), (go + .15, 1), (live, 1), (live + .12, 0)])}'
              f'{_n07_move(f"M832 {TRK} H1556", [(t, (x - 832) / 724) for t, x in stops])}{token("var(--c4)", 6)}</g>')
    who_lbl = ('<path d="M900 487 H1488" stroke="var(--line)" stroke-width="1.5"/>'
               + TC(1194, 516, sl["people"], fit(sl["people"], 16, 600, "people rail"), "var(--white)", W6))
    # the measure: a ruler from the request to production that fills while the change travels
    ry = 574
    ruler = (T(832, ry - 22, sl["start"], fit(sl["start"], 15, 300, "ruler start"), "var(--muted)", W6)
             + f'<g>{_n07_key("opacity", [(live, 1), (live + .1, 0), (R[0], 0), (R[1], 1)])}'
               + T(1542, ry - 22, sl["end"], fit(sl["end"], 15, 300, "ruler end"), "var(--muted)", 'text-anchor="end" font-weight="600"') + '</g>'
             + f'<g opacity="0">{_n07_hold(live, .1)}'
               + pill(1556 - (bold_width(_(str(sl["end"])), 15, current_factor()) + 28) / 2, ry - 27, sl["end"], ok, ctx, 15, 300, "ruler end", 14) + '</g>'
             + f'<path d="M832 {ry} H1556" stroke="var(--line)" stroke-width="2"/>'
             + f'<path d="M833 {ry - 10} V{ry + 10} M1555 {ry - 10} V{ry + 10}" stroke="var(--c2)" stroke-width="1.5"/>'
             + f'<path d="M834 {ry} H1554" stroke="var(--c4)" stroke-width="3" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">'
               f'{_n07_key("stroke-dashoffset", [(go, 1), (live, 0), (R[0], 0), (R[1], 1)])}</path>'
             + TC(1194, ry + 30, sl["measure"], fit(sl["measure"], 16, 500, "ruler measure"), "var(--c4)", W6))
    # production enables the other three
    ey = 634
    cols = ("var(--c1)", "var(--c3)", "var(--c2)")
    en = [card(832, ey, 724, 158, "var(--card)", "var(--line)", 18, 1.2),
          T(856, ey + 34, sl["enables"], fit(sl["enables"], 16, 500, "enabler title"), "var(--white)", W6),
          f'<path d="M1530 {ry + 12} V{ey}" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="3 5"/>']
    for k, name in enumerate(sl["areas"]):
        x, y, at = 856 + 230 * k, ey + 56, live + .18 + .1 * k
        en.append(card(x, y, 214, 78, "var(--dim)", "var(--line)", 12, 1.2)
                  + f'<rect x="{x}" y="{y + 16}" width="4" height="46" rx="2" fill="{cols[k]}"/>'
                  + T(x + 18, y + 46, name, fit(name, 16, 184, "enabled area"), "var(--white)", W6)
                  + f'<rect x="{x}" y="{y}" width="214" height="78" rx="12" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity="0">{_n07_hold(at, .1)}</rect>'
                  + f'<g opacity="0">{_n07_hold(at, .1)}{spark(x + 196, y + 18, .42)}</g>' + _n07_ping(x + 196, y + 18, 6, 22, at, dur=.35))
    drop = (f'<g opacity="0">{_n07_key("opacity", [(live, 0), (live + .03, 1), (live + .2, 1), (live + .24, 0)])}'
            f'{_n07_move(f"M1530 {ry + 12} V{ey}", [(live + .02, 0), (live + .2, 1)])}{token("var(--c4)", 5)}</g>')
    g += [land(rail + "".join(agents), .1, .5, -12), seq(tiles, .2, .45, 16), land(track, .45, .4, 0), land("".join(gates), .6, .4, 0),
          land("".join(people) + who_lbl, .75, .55, 24), land(ruler, 1.05, .45, 10), land("".join(en), 1.25, .5, 14), change, drop]
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 9 · the evidence: the way of working, not one more tool
def _n09_routes(ok, R):
    """The two routes of m09 (the art, without their captions): (A, B, route_a, route_b), in the desktop units."""
    A, B = (2.2, 6.3), (6.4, R[0])

    def lane(y, x1):
        return f'<circle cx="858" cy="{y}" r="6" fill="var(--c2)"/><path d="M864 {y} H{x1}" stroke="var(--line)" stroke-width="2"/>'

    # A · one more tool on top of the usual way: the work waits at every handoff and stalls before the tool
    ya, la = 428, 544
    boxes = [966, 1100, 1234, 1368]
    gaps = [x - 67 for x in boxes]
    old = []
    for k, x in enumerate(boxes):
        old.append(card(x - 38, la - 28, 76, 56, "var(--dim)", "var(--line)", 10, 1.2)
                   + _n07_bust(x, la - 10, .82, (SKIN_LIGHT, SKIN_BROWN, _N07_SKIN_MID, SKIN_BROWN)[k], "var(--line)", k % 2 == 1))
        if k:
            old.append(f'<path d="M{x - 52} {la - 5} L{x - 45} {la} L{x - 52} {la + 5}" fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-linecap="round"/>')
    old.append(f'<circle cx="1520" cy="{la}" r="16" fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="3 4"/>')
    tool = (f'<g>{bob(0, -3, 3)}{card(1344, 480, 48, 30, "var(--card)", "var(--c4)", 8, 1.5)}'
            f'<g>{loop("opacity", ".4;1;.4", 1.1)}{spark(1368, 495, .5)}</g></g>'
            f'<path d="M1356 511 V{la - 29} M1380 511 V{la - 29}" stroke="var(--c4)" stroke-width="1.5" opacity=".8"/>')
    frac = lambda x: (x - 858) / (gaps[2] - 858)
    token_a = (f'<g opacity="0">{_n07_hold(A[0] + .1, .12)}'
               + _n07_move(f"M858 {la} H{gaps[2]}", [(A[0] + .1, 0), (A[0] + .35, frac(gaps[0])), (A[0] + .85, frac(gaps[0])),
                                                      (A[0] + 1.3, frac(gaps[1])), (A[0] + 1.9, frac(gaps[1])), (A[0] + 2.35, 1)])
               + '<rect x="-6" y="-7" width="12" height="14" rx="2" fill="var(--c4)" fill-opacity=".3" stroke="var(--c4)" stroke-width="1.5"/></g>')
    waits = (_n07_ping(gaps[0], la, 7, 16, A[0] + .4, "var(--c3)") + _n07_ping(gaps[1], la, 7, 16, A[0] + 1.35, "var(--c3)")
             + f'<circle cx="{gaps[2]}" cy="{la}" r="9" fill="none" stroke="var(--c3)" stroke-width="1.5" opacity="0">'
               f'{_n07_hold(A[0] + 2.4, .1)}{loop("r", "9;14;9", 1.4)}</circle>')
    dim_a = _n07_key("opacity", [(B[0], 1), (B[0] + .3, .55), (R[0], .55), (R[1], 1)])
    route_a = lane(la, 1500) + token_a + f'<g>{dim_a}{"".join(old)}{tool}</g>' + waits

    # B · the way of working changes: people with the AI inside the flow, fewer handoffs, and the work arrives
    yb, lb = 612, 716
    pairs = [1040, 1300]
    t0, t1 = B[0] + .1, B[0] + 2.2
    at = lambda x: t0 + (x - 858) / (1520 - 858) * (t1 - t0)
    fill_b = (f'<path d="M864 {lb} H1500" stroke="var(--c4)" stroke-width="2" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">'
              f'{_n07_key("stroke-dashoffset", [(t0, 1), (t1, 0), (R[0], 0), (R[1], 1)])}</path>')
    token_b = (f'<g opacity="0">{_n07_key("opacity", [(t0 - .05, 0), (t0 + .05, 1), (t1 - .05, 1), (t1 + .05, 0)])}'
               f'{_n07_move(f"M858 {lb} H1520", [(t0, 0), (t1, 1)])}{token("var(--c4)", 6)}</g>')
    new = []
    for k, x in enumerate(pairs):
        t = at(x)
        new.append(card(x - 78, lb - 34, 156, 68, "var(--dim)", "var(--c2)", 12, 1.2)
                   + _n07_bust(x - 28, lb - 10, .9, (SKIN_BROWN, SKIN_LIGHT)[k], ("var(--accent)", "var(--c1)")[k], k == 0)
                   + f'<circle cx="{x + 30}" cy="{lb - 2}" r="17" fill="var(--ink)" stroke="var(--c4)" stroke-width="1.2"/>'
                   + f'<g><g transform="translate({x + 30} {lb - 2})"><g>{_n07_tr([(t - .15, "1"), (t, "1.3"), (t + .3, "1")], "scale")}{spark(0, 0, .55)}</g></g></g>'
                   + f'<path d="M{x - 8} {lb - 2} H{x + 11}" stroke="var(--c4)" stroke-width="1.5" stroke-dasharray="2 3">{loop("stroke-dashoffset", "0;-10", .8)}</path>'
                   + f'<rect x="{x - 78}" y="{lb - 34}" width="156" height="68" rx="12" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity="0">{_n07_hold(t, .1)}</rect>')
    goal = (f'<circle cx="1520" cy="{lb}" r="16" fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="3 4"/>'
            + _n07_badge(1520, lb, t1, ok, 16) + _n07_ping(1520, lb, 16, 34, t1 + .05, ok, 2, .8)
            + f'<circle cx="1520" cy="{lb}" r="22" fill="none" stroke="{ok}" stroke-width="1.5" opacity="0">{_n07_hold(t1 + .1, .2)}{loop("r", "20;26;20", 2.4)}</circle>')
    route_b = lane(lb, 1500) + fill_b + token_b + "".join(new) + goal

    return A, B, route_a, route_b


def _p09_evidencia(sl, ctx):
    """m09 on the 900x1600 stage: the figure framed on top, the two routes under it at the zone's width (their art
    scaled from the desktop units, their captions redrawn at phone size). Same loop and frozen frame."""
    ok = ctx.brand.c("dark.ok")
    R = _N07_RESET
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    cx, fig = zx + zw / 2, sl["figure"]
    bx, by, bw, bh = zx + 50, zy + 20, zw - 100, 300
    halo = f'<g>{loop("opacity", ".5;1;.5", 6)}{glow(cx, by + 130, 320, "var(--brand)", .55)}</g>'
    hud = "".join(f'<path d="M{x0} {y0 + dy * 24} V{y0} H{x0 + dx * 24}" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity=".7"/>'
                  for x0, y0, dx, dy in ((bx, by, 1, 1), (bx + bw, by, -1, 1), (bx, by + bh, 1, -1), (bx + bw, by + bh, -1, -1)))
    hud = f'<g>{loop("opacity", ".45;1;.45", 4)}{hud}</g>'
    # the figure and its label: static markup, no entrance
    figure = (TC(cx, by + 140, fig, fit(fig, 150, bw - 120, "evidence figure"), "var(--c4)", W6)
              + _p07_text(cx, by + 198, sl["label"], 30, bw - 100, "var(--white)", anchor="middle")
              + (TC(cx, by + 282, sl["source"], 20, "var(--muted)", W6) if sl.get("source") else ""))
    ey = by + bh + 50
    ends = (T(zx, ey, sl["start"], fit(sl["start"], 21, zw / 2 - 10, "route start", floor=18), "var(--muted)", W6)
            + T(zx + zw, ey, sl["end"], fit(sl["end"], 21, zw / 2 - 10, "route end", floor=18), "var(--muted)", 'text-anchor="end" font-weight="600"'))
    A, B, route_a, route_b = _n09_routes(ok, R)
    k = zw / 724                                     # the desktop row (x 832-1556) at the zone's width
    rows, caps = [], []
    for j, (y0, caption, (a, b), route) in enumerate(((428, sl["old"], A, route_a), (612, sl["new"], B, route_b))):
        ty = ey + 16 + j * (168 * k + 22)
        rows.append(land(f'<g transform="translate({zx} {ty:.1f}) scale({k:.4f}) translate(-832 {-y0})">'
                         + card(832, y0, 724, 168, "var(--card)", "var(--line)", 16, 1.2)
                         + f'<rect x="832" y="{y0}" width="724" height="168" rx="16" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_n07_win(a, b)}</rect>'
                         + route + '</g>', .45 + .25 * j, .5, 18))
        caps.append(land(T(zx + 26, f"{ty + 44:.1f}", caption, fit(caption, 23, zw - 52, "evidence route", floor=18), "var(--white)", W6), .45 + .25 * j, .5, 18))
    g = [glow(cx, by + 150, 380, "var(--brand)", .45), halo, hud, land(ends, .3, .45, 8)] + rows + [figure] + caps
    return portrait_mark("".join(g)), D, FREEZE


@register("scene", "m09_evidencia")
def sc_m09_evidencia(sl, ctx):
    """The figure stays still. Under it, two routes from the proof of concept to value. First, one more tool sits on
    top of the usual way: the handoffs stay and the work waits where it always waited. Then the way of working changes:
    people work with the AI inside the flow, fewer handoffs, and the work reaches value. The frozen frame shows both:
    the first still waiting, the second arrived."""
    ok = ctx.brand.c("dark.ok")
    R = _N07_RESET
    if ORIENT() == "portrait":
        return _p09_evidencia(sl, ctx)
    fig = sl["figure"]
    # the figure and its label: static markup, no entrance; only the light and the frame around it breathe
    halo = f'<g>{loop("opacity", ".5;1;.5", 6)}{glow(1190, 215, 300, "var(--brand)", .55)}</g>'
    hud = "".join(f'<path d="M{x0} {y0 + dy * 20} V{y0} H{x0 + dx * 20}" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity=".7"/>'
                  for x0, y0, dx, dy in ((900, 104, 1, 1), (1480, 104, -1, 1), (900, 364, 1, -1), (1480, 364, -1, -1)))
    hud = f'<g>{loop("opacity", ".45;1;.45", 4)}{hud}</g>'
    figure = (TC(1190, 222, fig, fit(fig, 128, 460, "evidence figure"), "var(--c4)", W6)
              + TCW(1190, 272, sl["label"], _n07_chars(sl["label"], 24, 380), 24, "var(--white)", W6, 1.3)
              + (TC(1190, 342, sl["source"], 15, "var(--muted)", W6) if sl.get("source") else ""))
    ends = (T(832, 414, sl["start"], fit(sl["start"], 15, 300, "route start"), "var(--muted)", W6)
            + T(1556, 414, sl["end"], fit(sl["end"], 15, 300, "route end"), "var(--muted)", 'text-anchor="end" font-weight="600"'))

    def row(y, h, caption, a, b):
        return (card(832, y, 724, h, "var(--card)", "var(--line)", 16, 1.2)
                + f'<rect x="832" y="{y}" width="724" height="{h}" rx="16" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_n07_win(a, b)}</rect>'
                + T(856, y + 34, caption, fit(caption, 17, 680, "evidence route"), "var(--white)", W6))

    A, B, route_a, route_b = _n09_routes(ok, R)
    ya, yb = 428, 612

    g = [glow(1190, 230, 360, "var(--brand)", .45), halo, hud, figure,
         land(ends, .3, .45, 8),
         land(row(ya, 168, sl["old"], *A) + route_a, .45, .5, 18),
         land(row(yb, 168, sl["new"], *B) + route_b, .7, .5, 18)]
    return "".join(g), D, FREEZE

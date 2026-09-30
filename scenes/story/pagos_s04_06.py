"""Group B · slides 4, 5 and 6 of the pagos deck: their moment, four hypotheses, and the one we take into detail.

Each scene tells one 12-second story in loop, keyed on seconds of the loop, and every resolved state holds until
_Q04_RESET, so the reduced-motion frame (10.8 s) shows the story told:
- n04_sector: the figure stays still. Under it, 2026 carries twenty payments for each one of 2018 (82 M -> 1.600 M), the
  new regulation lands in force, and the questions pile up on every team. Frozen: dense flow, the rule in force, four
  teams with questions waiting, «cada equipo necesita saber más, y más rápido».
- n05_hipotesis: four hypotheses, each with its «?». The loop plays one small story per card (one governed answer for
  many merchants; the right document found while the restricted one stays locked; the sale data turned into a
  recommendation), then technology runs its delivery cycle and powers the other three. Frozen: the four resolved.
- n06_conocimiento: three spaces, two open and one restricted, each with its agent. Atención asks what changes with the
  new regulation: its agent answers from its space and the open one, with the source, and the restricted space stays
  locked to it. Riesgo asks: only its restricted space answers, for its members. Frozen: both answered, the lock closed.

Runs in the shared pagos namespace (the deck's module/ext.py): helpers come from module/ext.py; private ones are _q04_*.
"""

_Q04_RESET = (11.45, 11.8)  # the resolved states fade back to rest before the loop starts over
_Q04_EASE = "0.45 0 0.55 1"


# ---------------------------------------------------------------- timing, keyed on seconds of the loop
def _q04_kt(pts):
    """[(s, value)] -> (keyTimes, values, n): flat before the first and after the last, strictly increasing."""
    pts = sorted(pts, key=lambda p: p[0])
    if pts[0][0] > 0:
        pts.insert(0, (0, pts[0][1]))
    if pts[-1][0] < D:
        pts.append((D, pts[-1][1]))
    kt, last = [], None
    for t, v in pts:
        f = 0.0 if last is None else min(1.0, max(t / D, last + .0005))
        kt.append(f)
        last = f
    kt[-1] = 1.0
    return ";".join(f"{k:.4f}" for k in kt), ";".join(str(v) for t, v in pts), len(pts)


def _q04_key(attr, pts, mode="linear"):
    kt, vals, n = _q04_kt(pts)
    return f'<animate attributeName="{attr}" values="{vals}" keyTimes="{kt}" dur="{D}s" repeatCount="indefinite" calcMode="{mode}"/>'


def _q04_tr(pts, typ="translate"):
    """An eased transform keyed on seconds: pts = [(s, "x y")]."""
    kt, vals, n = _q04_kt(pts)
    return (f'<animateTransform attributeName="transform" type="{typ}" values="{vals}" keyTimes="{kt}" dur="{D}s" '
            f'repeatCount="indefinite" calcMode="spline" keySplines="{";".join([_Q04_EASE] * (n - 1))}"/>')


def _q04_hold(on, fade=.15, lo=0, hi=1):
    """lo until `on`, hi until the reset: a resolved state that the frozen frame keeps."""
    r0, r1 = _Q04_RESET
    return _q04_key("opacity", [(on, lo), (on + fade, hi), (r0, hi), (r1, lo)])


def _q04_win(a, b, fade=.2):
    """Visible between a and b seconds."""
    return _q04_key("opacity", [(a, 0), (a + fade, 1), (b - fade, 1), (b, 0)])


def _q04_move(path, pts):
    """Travel along path: pts = [(s, fraction of the path)]."""
    return move(path, [(t / D, f) for t, f in pts], D)


def _q04_trip(path, a, b, color="var(--c4)", r=4, rev=False):
    """A token that travels path from a to b seconds (rev: from its end back to its start), hidden the rest of the loop."""
    return (f'<g opacity="0">{_q04_key("opacity", [(a - .01, 0), (a, 1), (b, 1), (b + .01, 0)])}'
            f'{_q04_move(path, [(a, 1), (b, 0)] if rev else [(a, 0), (b, 1)])}{token(color, r)}</g>')


def _q04_ping(x, y, r0, r1, at, color="var(--c4)", sw=1.5, dur=.6):
    """A ring that opens once at `at` seconds."""
    return (f'<circle cx="{x}" cy="{y}" r="{r0}" fill="none" stroke="{color}" stroke-width="{sw}" opacity="0">'
            + _q04_key("r", [(at, r0), (at + dur, r1), (at + dur + .01, r0)])
            + _q04_key("opacity", [(at - .01, 0), (at, .9), (at + dur, 0)]) + '</circle>')


def _q04_flash(x, y, w, h, rx, at, color="var(--c4)", dur=.7):
    """A frame that lights once at `at` seconds and fades."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="none" stroke="{color}" stroke-width="3" opacity="0">'
            + _q04_key("opacity", [(at - .01, 0), (at, 1), (at + dur, 0)]) + '</rect>')


def _q04_badge(x, y, at, ok, r=11):
    """The ok badge with its check: appears at `at` and holds."""
    return f'<g opacity="0">{_q04_hold(at)}<circle cx="{x}" cy="{y}" r="{r}" fill="{ok}"/>{check(x, y + 1, r / 15, "var(--ink)")}</g>'


def _q04_pop(x, y, at, inner, s0=1.35):
    """inner (drawn around 0,0) appears at `at` with a short stamp, and holds."""
    return (f'<g opacity="0">{_q04_hold(at, .08)}<g transform="translate({x:.1f} {y:.1f})"><g>'
            f'{_q04_tr([(at, str(s0)), (at + .22, "1")], "scale")}{inner}</g></g></g>')


def _q04_shake(at, amp=3):
    """A short sideways jolt at `at` seconds, then still (additive: it composes with any placement)."""
    kt, vals, n = _q04_kt([(at, "0 0"), (at + .05, f"{-amp} 0"), (at + .1, f"{amp} 0"), (at + .15, f"{-amp / 2} 0"), (at + .2, "0 0")])
    return (f'<animateTransform attributeName="transform" type="translate" additive="sum" values="{vals}" keyTimes="{kt}" '
            f'dur="{D}s" repeatCount="indefinite"/>')


def _q04_wrap(s, n):
    out, cur = [], ""
    for w in s.split():
        if len(cur) + len(w) + 1 > n and cur:
            out.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    return out + [cur]


def _q04_chars(text, size, room):
    """The widest wrap (in characters) whose every line fits room units at size."""
    s = _(str(text))
    for n in range(60, 7, -1):
        if all(bold_width(line, size, current_factor()) <= room for line in _q04_wrap(s, n)):
            return n
    return 8


def _q04_even(text, size, room):
    """Characters per line for a balanced wrap: the fewest lines that fit room, with lines as even as possible."""
    s = _(str(text))
    n = _q04_chars(text, size, room)
    lines = len(_q04_wrap(s, n))
    while n > 8 and len(_q04_wrap(s, n - 1)) == lines:
        n -= 1
    return n


def _q04_bust(x, y, s, skin, shirt, long_hair=False):
    """A faceless head and shoulders around the head's center, in the style of the slide-14 people."""
    rim = 'fill="none" stroke="var(--c2)" stroke-width="1.2" opacity=".55"'
    back = (f'<path d="M-11 -2 C-13 -15 -4 -18 1 -17.5 C8 -17 13 -12 12 -2 L12 13 C7 16 -7 16 -12 13 Z" fill="{HAIR}"/>'
            if long_hair else "")
    body = (f'<path d="M-21 31 C-21 19 -13 14 0 14 C13 14 21 19 21 31 Z" fill="{shirt}"/><path d="M-21 31 C-21 19 -13 14 0 14 C13 14 21 19 21 31" {rim}/>'
            f'<rect x="-3.5" y="8" width="7" height="7" fill="{shade(skin, 14)}"/>'
            f'<ellipse cx="0" cy="0" rx="9" ry="10.5" fill="{skin}"/>'
            f'<path d="M-9.6 -1 C-10.4 -12 -3 -15.5 2 -15 C8 -14.6 10.8 -8.5 9.8 -2 C6.5 -8.4 -2 -9.2 -9.6 -1 Z" fill="{HAIR}"/>')
    return f'<g transform="translate({x} {y}) scale({s})">{back}{body}</g>'


def _q04_page(x, y, w=30, h=40, col="var(--c2)"):
    """A small document with three lines."""
    return (card(x, y, w, h, "var(--dim)", col, 4, 1.2)
            + "".join(f'<rect x="{x + 6}" y="{y + 10 + 8 * j}" width="{w - 12 - (j % 2) * 6}" height="3.5" rx="1.75" fill="{col}" opacity=".55"/>'
                      for j in range(3)))


def _q04_doc(x, y, col="var(--c2)"):
    """A line icon of a document, its top-left corner at (x, y): 14 x 18."""
    return (f'<path d="M{x} {y} h9 l5 5 v13 h-14 Z M{x + 9} {y} v5 h5 M{x + 3} {y + 9} h8 M{x + 3} {y + 13} h8" fill="none" '
            f'stroke="{col}" stroke-width="1.3" stroke-linejoin="round"/>')


def _q04_lock(x, y, col, lift=""):
    """A padlock centered at (x, y); lift animates the shackle (it opens upward)."""
    return (f'<g fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round">'
            f'<g>{lift}<path d="M{x - 6} {y - 2} V{y - 7} A6 6 0 0 1 {x + 6} {y - 7} V{y - 2}"/></g>'
            f'<rect x="{x - 9}" y="{y - 2}" width="18" height="14" rx="3" fill="{col}" fill-opacity=".2"/></g>')


# ---------------------------------------------------------------- 4 · more payments, new rules: everything moves faster
def _pn04_twin(sl, ctx):
    """n04 on the 900x1600 stage: the still figure on top, the two lanes, the regulation stamped in force, and the four
    teams as a 2x2 (the second row fed along the gutter). Same loop and frozen frame; labels painted after the art."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    bx, bw = zx + 20, zw - 40
    fx = bx + bw / 2
    by, bh = zy + 8, 262
    art, text = [glow(fx, zy + zh * .45, 460, "var(--brand)", .45)], []
    # 1 · the instrument: figure, label and source are static; only the frame and its light breathe
    hud = "".join(f'<path d="M{x0} {y0 + dy * 26} V{y0} H{x0 + dx * 26}" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity=".8"/>'
                  for x0, y0, dx, dy in ((bx, by, 1, 1), (bx + bw, by, -1, 1), (bx, by + bh, 1, -1), (bx + bw, by + bh, -1, -1)))
    art.append(f'<g>{loop("opacity", ".5;1;.5", 6)}{glow(fx, by + 110, 260, "var(--brand)", .55)}</g><g>{loop("opacity", ".45;1;.45", 4)}{hud}</g>')
    text.append(TC(fx, by + 122, sl["figure"], fit(sl["figure"], 124, bw - 100, "sector figure", floor=20), "var(--c4)", W6)
                + TCW(fx, by + 170, sl["label"], _q04_even(sl["label"], 25, 620), 25, "var(--white)", W6, 1.3)
                + TC(fx, by + 240, sl["source"], fit(sl["source"], 20, 620, "sector source", floor=20), "var(--muted)", W6))
    # 2 · volume: 2026 fills up to twenty payments for each one of 2018
    py, ph = by + bh + 14, 136
    ya, yb = py + 44, py + 96
    x0, x1, lap, n = bx + 112, bx + bw - 30, 4.0, 20

    def lane(y):
        return (f'<path d="M{x0} {y} H{x1}" stroke="var(--line)" stroke-width="2"/>'
                f'<circle cx="{x0}" cy="{y}" r="4" fill="var(--line)"/><circle cx="{x1}" cy="{y}" r="4" fill="var(--line)"/>')

    def pay(y, k, m, col, on=None):
        ph_ = k * lap / m
        tok = f'<g>{move(f"M{x0} {y} H{x1}", [(0, 0), (1, 1)], lap, -ph_)}{token(col, 5)}</g>'   # the lane's clip hides the wrap
        return tok if on is None else f'<g opacity="0">{_q04_hold(on, .2)}{tok}</g>'

    art.append(land(card(bx, py, bw, ph, "var(--dim)", "var(--line)", 16, 1.2) + lane(ya) + lane(yb)
                    + f'<clipPath id="pn04-lane"><rect x="{x0}" y="{py}" width="{x1 - x0}" height="{ph}"/></clipPath><g clip-path="url(#pn04-lane)">'
                    + pay(ya, 0, 1, "var(--c2)") + "".join(pay(yb, k, n, "var(--c4)", None if k == 0 else 2.3 + (k - 1) * .13) for k in range(n)) + '</g>', .15, .5, 12))
    text.append(land(T(bx + 24, ya + 7, sl["then"], fit(sl["then"], 21, 80, "sector lane", floor=20), "var(--muted)", W6)
                     + T(bx + 24, yb + 7, sl["now"], fit(sl["now"], 21, 80, "sector lane", floor=20), "var(--white)", W6), .15, .5, 12))
    # 3 · new rules: the regulation lands on the flow, then the stamp puts it in force
    ry, rh = py + ph + 14, 66
    t_rule, t_stamp = 5.0, 5.6
    sw_ = min(360, bold_width(_(str(sl["since"])), 20, current_factor()) + 40)
    scx = bx + bw - 14 - sw_ / 2
    art.append(land(card(bx, ry, bw, rh, "none", "var(--line)", 14, 1.2, 'stroke-dasharray="6 6"'), .35, .4, 0))
    banner = (card(bx, ry, bw, rh, "var(--card)", "var(--c4)", 14, 1.5) + _q04_doc(bx + 22, ry + 24, "var(--c4)")
              + T(bx + 50, ry + 41, sl["rule"], fit(sl["rule"], 22, scx - sw_ / 2 - bx - 64, "sector rule", floor=20), "var(--white)", W6))
    text.append(f'<g opacity="0">{_q04_hold(t_rule, .2)}<g>{_q04_tr([(t_rule, "0 -34"), (t_rule + .45, "0 0")])}{banner}</g></g>'
                + _q04_pop(scx, ry + rh / 2, t_stamp, pill(0, 0, sl["since"], "var(--c4)", ctx, 20, 360, "sector in force"), 1.45)
                + _q04_flash(bx, ry, bw, rh, 14, t_stamp + .15))
    # 4 · pressure: the questions drip down to every team (2x2) until each one has a queue waiting
    tw, th, gx = (bw - 20) / 2, 112, bx + bw / 2
    ty1 = ry + rh + 30
    rb = ry + rh
    for k, name in enumerate(sl["teams"][:4]):
        x, ty = bx + (k % 2) * (tw + 20), ty1 + (k // 2) * (th + 16)
        cx = x + tw / 2
        path = f"M{cx:.0f} {rb} V{ty + 3}" if k < 2 else f"M{gx:.0f} {rb} V{ty + th / 2:.0f} H{x + (tw if k == 2 else 0):.0f}"
        arrive = [7.1 + .85 * j + .16 * k for j in range(3)]
        c = (f'<path d="{path}" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 4"/>'
             + card(x, ty, tw, th, "var(--card)", "var(--line)", 14, 1.2) + _user(x + 44, ty + 88, .8, "var(--c2)"))
        c += "".join(f'<rect x="{x + tw - 176:.0f}" y="{ty + 30 + 24 * j}" width="140" height="12" rx="6" fill="var(--line)" opacity=".55"/>' for j in range(3))
        art.append(land(c, .5 + .1 * k, .45, 14))
        text.append(land(T(x + 24, ty + 40, name, fit(name, 22, tw - 220, "sector team", floor=20), "var(--white)", W6), .5 + .1 * k, .45, 14))
        q = "".join(f'<rect x="{x + tw - 176:.0f}" y="{ty + 30 + 24 * j}" width="140" height="12" rx="6" fill="var(--c4)" fill-opacity=".35" stroke="var(--c4)" stroke-width="1.2" opacity="0">{_q04_hold(t, .1)}</rect>'
                    + _q04_trip(path, t - .3, t, "var(--c4)", 4) for j, t in enumerate(arrive))
        q += (f'<rect x="{x:.0f}" y="{ty}" width="{tw:.0f}" height="{th}" rx="14" fill="none" stroke="var(--c3)" stroke-width="2" opacity="0">'
              f'{_q04_hold(arrive[2] + .1, .2)}</rect>')
        mark = '<circle r="16" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>' + TC(0, 7, "?", 21, "var(--c4)", W6)
        art.append(q + _q04_pop(x + tw - 14, ty + 2, arrive[0], mark) + _q04_ping(x + tw - 14, ty + 2, 16, 32, arrive[0] + .05))
    text.append(f'<g opacity="0">{_q04_hold(9.9, .3)}'
                + TC(fx, ty1 + 2 * th + 16 + 56, sl["pressure"], fit(sl["pressure"], 25, bw, "sector pressure", floor=20), "var(--c4)", W6) + '</g>')
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "n04_sector")
def sc_n04_sector(sl, ctx):
    """The figure stays still, framed like an instrument, with its source. Under it the context moves: two lanes of
    digital payments, 2018 and 2026, where 2026 fills up to twenty payments for each one of 2018 (the figure's own
    proportion, 82 M to 1.600 M, and no number counts); the new regulation lands on the flow and is stamped in force;
    then the questions drip down to the four teams until every one has a queue waiting. The frozen frame: the dense
    flow, the rule in force, four teams with questions, and the conclusion under them."""
    if ORIENT() == "portrait":
        return _pn04_twin(sl, ctx)
    bx, by, bw, bh = 880, 96, 620, 256
    fx = bx + bw / 2
    g = [glow(fx, 330, 460, "var(--brand)", .45)]
    # 1 · the instrument: figure, label and source are static markup; only the frame and its light breathe
    halo = f'<g>{loop("opacity", ".5;1;.5", 6)}{glow(fx, 200, 250, "var(--brand)", .55)}</g>'
    hud = "".join(f'<path d="M{x0} {y0 + dy * 22} V{y0} H{x0 + dx * 22}" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity=".8"/>'
                  for x0, y0, dx, dy in ((bx, by, 1, 1), (bx + bw, by, -1, 1), (bx, by + bh, 1, -1), (bx + bw, by + bh, -1, -1)))
    hud = f'<g>{loop("opacity", ".45;1;.45", 4)}{hud}</g>'
    figure = (TC(fx, by + 124, sl["figure"], fit(sl["figure"], 112, bw - 100, "sector figure"), "var(--c4)", W6)
              + TCW(fx, by + 168, sl["label"], _q04_even(sl["label"], 22, 460), 22, "var(--white)", W6, 1.3)
              + TC(fx, by + 236, sl["source"], fit(sl["source"], 15, 460, "sector source"), "var(--muted)", W6))
    g += [halo, hud, figure]

    # 2 · volume: 2026 fills up to twenty payments for each one of 2018 while the lane runs
    py, ph = 376, 144
    ya, yb = py + 46, py + 102
    x0, x1 = 976, 1474
    lap, n = 4.0, 20

    def lane(y):
        return (f'<path d="M{x0} {y} H{x1}" stroke="var(--line)" stroke-width="2"/>'
                f'<circle cx="{x0}" cy="{y}" r="4" fill="var(--line)"/><circle cx="{x1}" cy="{y}" r="4" fill="var(--line)"/>')

    def pay(y, k, m, col, on=None):
        ph_ = k * lap / m
        fade = (f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.06;.94;1" dur="{lap}s" begin="-{ph_:.2f}s" '
                f'repeatCount="indefinite"/>')
        tok = f'<g>{move(f"M{x0} {y} H{x1}", [(0, 0), (1, 1)], lap, -ph_)}{fade}{token(col, 4)}</g>'
        return tok if on is None else f'<g opacity="0">{_q04_hold(on, .2)}{tok}</g>'

    flow = (card(bx, py, bw, ph, "var(--dim)", "var(--line)", 16, 1.2)
            + T(bx + 24, ya + 6, sl["then"], fit(sl["then"], 16, 64, "sector lane"), "var(--muted)", W6)
            + T(bx + 24, yb + 6, sl["now"], fit(sl["now"], 16, 64, "sector lane"), "var(--white)", W6)
            + lane(ya) + lane(yb) + pay(ya, 0, 1, "var(--c2)")
            + "".join(pay(yb, k, n, "var(--c4)", None if k == 0 else 2.3 + (k - 1) * .13) for k in range(n)))
    g.append(land(flow, .15, .5, 12))

    # 3 · new rules: the regulation lands on the flow, then the stamp puts it in force
    ry, rh = 540, 56
    t_rule, t_stamp = 5.0, 5.6
    slot = card(bx, ry, bw, rh, "none", "var(--line)", 14, 1.2, 'stroke-dasharray="6 6"')
    sw_ = min(260, bold_width(_(str(sl["since"])), 15, current_factor()) + 36)
    scx = bx + bw - 18 - sw_ / 2
    banner = (card(bx, ry, bw, rh, "var(--card)", "var(--c4)", 14, 1.5) + _q04_doc(bx + 24, ry + 18, "var(--c4)")
              + T(bx + 52, ry + 34, sl["rule"], fit(sl["rule"], 18, scx - sw_ / 2 - bx - 72, "sector rule"), "var(--white)", W6))
    banner = f'<g opacity="0">{_q04_hold(t_rule, .2)}<g>{_q04_tr([(t_rule, "0 -34"), (t_rule + .45, "0 0")])}{banner}</g></g>'
    stamp = (_q04_pop(scx, ry + rh / 2, t_stamp, pill(0, 0, sl["since"], "var(--c4)", ctx, 15, 260, "sector in force"), 1.45)
             + _q04_flash(bx, ry, bw, rh, 14, t_stamp + .15))
    g.append(land(slot, .35, .4, 0))
    g += [banner, stamp]

    # 4 · pressure: the questions drip down to every team until each one has a queue waiting
    ty, th, tw = 628, 108, 146
    gap = (bw - 4 * tw) / 3
    chips, live = [], []
    for k, name in enumerate(sl["teams"][:4]):
        x = bx + k * (tw + gap)
        cx = x + tw / 2
        arrive = [7.1 + .85 * j + .16 * k for j in range(3)]
        c = (f'<path d="M{cx:.1f} {ry + rh} V{ty}" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 4"/>'
             + card(x, ty, tw, th, "var(--card)", "var(--line)", 14, 1.2)
             + TC(f"{cx:.1f}", ty + 32, name, fit(name, 17, tw - 28, "sector team"), "var(--white)", W6)
             + _user(x + 34, ty + 84, .72, "var(--c2)"))
        for j in range(3):
            c += f'<rect x="{x + 62:.1f}" y="{ty + 50 + 18 * j}" width="62" height="10" rx="5" fill="var(--line)" opacity=".55"/>'
        chips.append(c)
        q = "".join(f'<rect x="{x + 62:.1f}" y="{ty + 50 + 18 * j}" width="62" height="10" rx="5" fill="var(--c4)" fill-opacity=".35" stroke="var(--c4)" stroke-width="1.2" opacity="0">{_q04_hold(t, .1)}</rect>'
                    + _q04_trip(f"M{cx:.1f} {ry + rh} V{ty + 4}", t - .3, t, "var(--c4)", 3.5)
                    for j, t in enumerate(arrive))
        q += (f'<rect x="{x:.1f}" y="{ty}" width="{tw}" height="{th}" rx="14" fill="none" stroke="var(--c3)" stroke-width="2" opacity="0">'
              f'{_q04_hold(arrive[2] + .1, .2)}</rect>')
        mark = (f'<circle r="13" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>' + TC(0, 6, "?", 17, "var(--c4)", W6))
        q += _q04_pop(x + tw - 12, ty + 2, arrive[0], mark) + _q04_ping(x + tw - 12, ty + 2, 13, 28, arrive[0] + .05)
        live.append(q)
    g.append(seq(chips, .5, .45, 14))
    g += live
    g.append(f'<g opacity="0">{_q04_hold(9.9, .3)}'
             + TC(fx, 786, sl["pressure"], fit(sl["pressure"], 19, bw, "sector pressure"), "var(--c4)", W6) + '</g>')
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 5 · four hypotheses, three with a return and one enabler
def _q04_shop(x, y):
    """A small storefront around (x, y): awning, walls and door, thin strokes."""
    return (f'<path d="M{x - 12} {y - 4} L{x - 9} {y - 12} H{x + 9} L{x + 12} {y - 4} Z" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.3" stroke-linejoin="round"/>'
            f'<path d="M{x - 10} {y - 4} V{y + 11} H{x + 10} V{y - 4}" fill="none" stroke="var(--c2)" stroke-width="1.3" stroke-linejoin="round"/>'
            f'<path d="M{x - 3} {y + 11} V{y + 3} H{x + 3} V{y + 11}" fill="none" stroke="var(--c2)" stroke-width="1.2"/>')


def _q04_answer(a, ok):
    """Atención a comercios: three merchants ask the same frequent question; the AI gives one governed answer, and the
    same answer reaches the three."""
    ax, ay = 104, 58
    out = []
    for k, y in enumerate((16, 58, 100)):
        leg = f"M28 {y} C58 {y} 66 {ay} {ax - 18} {ay}"
        back = f"M{ax - 18} {ay} C66 {ay} 58 {y} 28 {y}"
        out.append(_q04_shop(12, y) + f'<path d="{leg}" fill="none" stroke="var(--line)" stroke-width="1.2"/>'
                   + _q04_trip(leg, a + .1 + .12 * k, a + .5 + .12 * k, "var(--c2)", 3)
                   + _q04_trip(back, a + .95, a + 1.3, "var(--c4)", 3)
                   + _q04_badge(34, y, a + 1.3 + .06 * k, ok, 7))
    node = (f'<circle cx="{ax}" cy="{ay}" r="18" fill="var(--ink)" stroke="var(--c4)" stroke-width="1.2"/>'
            f'<g><g transform="translate({ax} {ay})"><g>{_q04_tr([(a + .6, "1"), (a + .72, "1.3"), (a + .95, "1")], "scale")}'
            f'{spark(0, 0, .55)}</g></g></g>' + _q04_ping(ax, ay, 18, 34, a + .62))
    one = (f'<path d="M{ax + 18} {ay} H142" stroke="var(--line)" stroke-width="1.2"/>'
           f'<g opacity="0">{_q04_hold(a + .78)}<path d="M{ax + 18} {ay} H142" stroke="var(--c4)" stroke-width="1.4"/>'
           + card(142, 26, 52, 64, "var(--dim)", "var(--c4)", 6, 1.3)
           + "".join(f'<rect x="150" y="{38 + 10 * j}" width="{w}" height="4" rx="2" fill="var(--c4)" opacity=".8"/>' for j, w in enumerate((34, 26, 30)))
           + '<path d="M168 70 l8 3 v6 c0 5 -4 8 -8 9 c-4 -1 -8 -4 -8 -9 v-6 Z" fill="none" stroke="var(--c4)" stroke-width="1.3" stroke-linejoin="round"/>'
           + '</g>')
    return "".join(out) + node + one


def _q04_find(a, ok, skin):
    """Conocimiento interno: a person asks; the AI looks across the documents, the one that answers comes back to the
    person, and the restricted one keeps its lock."""
    xs = (76, 118, 160)
    out = [_q04_bust(22, 62, .95, skin, "var(--c1)", True)]
    for k, x in enumerate(xs):
        out.append(_q04_page(x, 40, 30, 40, "var(--accent)" if k == 2 else "var(--c2)"))
    out.append(f'<g>{_q04_shake(a + .62)}{_q04_lock(178, 40, "var(--accent)")}</g>')
    out.append(_q04_ping(178, 44, 10, 22, a + .62, "var(--c5)", 1.5, .45))
    ask = f"M40 50 C56 40 64 34 70 36"
    out.append(_q04_trip(ask, a + .05, a + .25, "var(--c2)", 3))
    beam = (f'<g opacity="0">{_q04_key("opacity", [(a + .2, 0), (a + .25, 1), (a + .7, 1), (a + .78, 0)])}'
            f'<g>{_q04_tr([(a + .2, "0 0"), (a + .75, "122 0")])}<path d="M72 30 V88" stroke="var(--c4)" stroke-width="1.5"/>'
            f'{spark(72, 28, .35)}</g></g>')
    found = (f'<rect x="{xs[1] - 4}" y="36" width="38" height="48" rx="6" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity="0">'
             f'{_q04_hold(a + .5, .1)}</rect>')
    back = f"M{xs[1] + 15} 60 C{xs[1] - 10} 104 56 104 40 80"
    carry = (f'<g opacity="0">{_q04_key("opacity", [(a + .84, 0), (a + .86, 1), (a + 1.24, 1), (a + 1.26, 0)])}'
             f'{_q04_move(back, [(a + .85, 0), (a + 1.25, 1)])}'
             '<rect x="-6" y="-8" width="12" height="16" rx="2" fill="var(--c4)" fill-opacity=".3" stroke="var(--c4)" stroke-width="1.4"/></g>')
    got = (f'<g opacity="0">{_q04_hold(a + 1.25)}' + card(0, 94, 64, 22, "var(--dim)", "var(--c4)", 6, 1.2)
           + spark(12, 105, .3) + '<rect x="22" y="103" width="34" height="4" rx="2" fill="var(--c4)"/></g>')
    return "".join(out) + beam + found + carry + got + _q04_badge(186, 104, a + 1.4, ok)


def _q04_grow(a, ok):
    """Datos para el comercio: each sale lands in the merchant's data; the AI reads it and suggests what to do next,
    and the merchant's line turns upward."""
    hs = (22, 34, 28, 42, 36)
    out = ['<path d="M2 106 H108" stroke="var(--line)" stroke-width="1.5"/>']
    for k, h in enumerate(hs):
        x, t = 6 + 20 * k, a + .1 + .08 * k
        out.append(f'<rect x="{x}" y="{104 - h}" width="12" height="{h}" rx="2" fill="var(--c2)" opacity=".5"/>'
                   f'<rect x="{x}" y="{104 - h}" width="12" height="4" rx="2" fill="var(--c4)" opacity="0">{_q04_hold(t + .25, .08)}</rect>'
                   + _q04_trip(f"M{x + 6} 4 V{100 - h}", t, t + .25, "var(--c4)", 2.5))
    beam = (f'<g opacity="0">{_q04_key("opacity", [(a + .55, 0), (a + .6, 1), (a + .95, 1), (a + 1.0, 0)])}'
            f'<g>{_q04_tr([(a + .55, "0 0"), (a + .98, "100 0")])}<path d="M4 50 V104" stroke="var(--c4)" stroke-width="1.5"/>{spark(4, 48, .35)}</g></g>')
    rec = (f'<g opacity="0">{_q04_hold(a + 1.0)}' + card(122, 14, 72, 50, "var(--dim)", "var(--c4)", 8, 1.3) + spark(136, 39, .42)
           + '<rect x="148" y="30" width="36" height="4" rx="2" fill="var(--c4)"/><rect x="148" y="40" width="26" height="4" rx="2" fill="var(--c4)" opacity=".7"/>'
           + '<rect x="148" y="50" width="32" height="4" rx="2" fill="var(--c4)" opacity=".7"/></g>')
    up = "M8 88 L36 76 L60 80 L96 48 L112 36"
    trend = (f'<path d="{up}" fill="none" stroke="var(--c4)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" pathLength="1" '
             f'stroke-dasharray="1" stroke-dashoffset="1">{_q04_key("stroke-dashoffset", [(a + 1.15, 1), (a + 1.5, 0), (_Q04_RESET[0], 0), (_Q04_RESET[1], 1)])}</path>'
             f'<path d="M104 34 L113 35 L110 44" fill="none" stroke="var(--c4)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity="0">'
             f'{_q04_hold(a + 1.48, .08)}</path>')
    return "".join(out) + beam + rec + trend + _q04_badge(186, 104, a + 1.6, ok)


def _q04_glyph(k):
    """The four steps of the delivery cycle as glyphs around 0,0: requirement, code, test, deploy (icons.py «entrega»)."""
    return icon(icons("entrega")[k], 0, 0, 30, "var(--c2)", 1.5)


def _pn05_text(x, y, text, size, room, fill, lines=2, lh=1.3):
    """text wrapped into room at the largest size (never under 20: the phone floor) that fits in `lines` lines."""
    z = size
    while z > 20 and len(_q04_wrap(_(str(text)), _q04_chars(text, z, room))) > lines:
        z -= 1
    return TCW(x, y, text, _q04_chars(text, z, room), z, fill, W6, lh, "start")


def _pn05_twin(sl, ctx):
    """n05 on the 900x1600 stage: the three hypotheses as full-width rows (text on the left, their small story on the
    right), the enabler under them and a spine on the left carrying its pulse into each row (energía's m07 twin). Same
    loop and frozen frame; labels painted after the art."""
    ok = ctx.brand.c("dark.ok")
    cols = ("var(--c1)", "var(--c2)", "var(--c3)", "var(--accent)")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    SX, X0 = zx + 20, zx + 44
    W, RH, GAP = zx + zw - X0, 176, 12
    ys = [zy + 22 + k * (RH + GAP) for k in range(3)]
    BY, BH = ys[-1] + RH + 24, 296
    wins = ((2.2, 4.6), (4.6, 7.0), (7.0, 9.4), (9.4, _Q04_RESET[0]))
    R = _Q04_RESET
    room = W - 24 - 262

    def qmark(cx, cy, a):
        return (f'<circle cx="{cx}" cy="{cy}" r="20" fill="var(--card)" stroke="var(--c4)" stroke-width="1.8"/>'
                + TC(cx, cy + 8.5, "?", 24, "var(--c4)", W6) + _q04_ping(cx, cy, 20, 38, a + .05))

    def spot(x, y, w, h, a, b):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="none" stroke="var(--c4)" stroke-width="2.4" opacity="0">{_q04_win(a, b, .25)}</rect>'

    art, text = [glow(zx + zw / 2, zy + zh * .45, 470, "var(--brand)", .45)], []
    stories = (_q04_answer(wins[0][0], ok), _q04_find(wins[1][0], ok, SKIN_BROWN), _q04_grow(wins[2][0], ok))
    f = current_factor()
    rs = 20
    rw = bold_width(_(str(sl["ret"])), rs, f)
    for k in range(3):
        y, (area, idea, gain), (a, b), at = ys[k], sl["cards"][k], wins[k], .1 + .12 * k
        art.append(land(card(X0, y, W, RH, "var(--card)", "var(--line)", 18, 1.2)
                        + f'<rect x="{X0 + 18}" y="{y - 2}" width="{W * .4:.0f}" height="4" rx="2" fill="{cols[k]}"/>'
                        + f'<g transform="translate({X0 + W - 250} {y + 26}) scale(1.12)">{stories[k]}</g>'
                        + spot(X0, y, W, RH, a, b) + qmark(X0 + W - 30, y, a), at, .5, 16))
        text.append(land(T(X0 + 24, y + 42, area, fit(area, 26, room, "hypothesis area", floor=20), "var(--white)", W6)
                         + _pn05_text(X0 + 24, y + 76, idea, 21, room, "var(--muted)")
                         + T(X0 + 24, y + 152, sl["ret"], rs, "var(--muted)", W6)
                         + T(f"{X0 + 36 + rw:.1f}", y + 152, gain, fit(gain, 23, room - rw - 12, "hypothesis return", floor=20), "var(--c4)", W6),
                         at, .5, 16))
    # the enabler: its delivery cycle, four steps and a track the change runs along
    area, idea, gain = sl["cards"][3]
    a4 = wins[3][0]
    mid = X0 + W / 2
    nodes = [mid + (k - 1.5) * 150 for k in range(4)]
    ny, trk = BY + 166, BY + 210
    pipe = (f'<path d="M{nodes[0]} {ny} H{nodes[-1]}" stroke="var(--line)" stroke-width="2"/>'
            + "".join(card(x - 32, ny - 32, 64, 64, "var(--dim)", "var(--line)", 14, 1.2) + icon(icons("entrega")[k], x, ny, 38, "var(--c2)", 1.5)
                      + f'<rect x="{x - 32}" y="{ny - 32}" width="64" height="64" rx="14" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_q04_hold(a4 + .12 + .17 * k, .1)}</rect>'
                      for k, x in enumerate(nodes))
            + f'<path d="M{nodes[0]} {trk} H{nodes[-1]}" stroke="var(--line)" stroke-width="2"/>'
            + f'<path d="M{nodes[0]} {trk} H{nodes[-1]}" stroke="var(--c4)" stroke-width="2" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">'
              f'{_q04_key("stroke-dashoffset", [(a4 + .1, 1), (a4 + .66, 0), (R[0], 0), (R[1], 1)])}</path>'
            + f'<g opacity="0">{_q04_key("opacity", [(a4 + .05, 0), (a4 + .1, 1), (a4 + .66, 1), (a4 + .72, 0)])}'
              f'{_q04_move(f"M{nodes[0]} {trk} H{nodes[-1]}", [(a4 + .1, 0), (a4 + .66, 1)])}{token("var(--c4)", 6)}</g>')
    art.append(land(card(X0, BY, W, BH, "var(--card)", "var(--line)", 18, 1.2)
                    + f'<rect x="{X0 + 18}" y="{BY - 2}" width="{W * .6:.0f}" height="4" rx="2" fill="{cols[3]}"/>'
                    + pipe + spot(X0, BY, W, BH, *wins[3]) + qmark(X0 + W - 30, BY, a4), .46, .5, 16))
    text.append(land(T(X0 + 24, BY + 44, area, fit(area, 26, W - 100, "hypothesis area", floor=20), "var(--white)", W6)
                     + _pn05_text(X0 + 24, BY + 80, idea, 21, W - 48, "var(--muted)")
                     + TC(f"{mid:.1f}", BY + 246, sl["cycle"], fit(sl["cycle"], 20, W - 48, "hypothesis cycle", floor=20), "var(--muted)", W6)
                     + T(X0 + 24, BY + 280, gain, fit(gain, 23, W - 48, "hypothesis enabler", floor=20), "var(--c4)", W6), .46, .5, 16))
    # the enabler powers the three: a pulse climbs the spine into each row
    spine = []
    for k, y in enumerate(ys):
        py, t = y + RH / 2, a4 + .75 + .08 * k
        d = f"M{SX} {BY} V{py} H{X0}"
        spine.append(f'<path d="{d}" fill="none" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="3 5" opacity=".6"/>'
                     f'<path d="{d}" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_q04_hold(t, .12)}</path>'
                     + _q04_trip(d, t - .03, t + .3, "var(--c4)", 5))
    spine.append(f'<circle cx="{SX}" cy="{BY}" r="5" fill="var(--c4)"/>')
    art.append(land("".join(spine), 1.2, .45, 0))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "n05_hipotesis")
def sc_n05_hipotesis(sl, ctx):
    """Three hypotheses with a possible return stand on a fourth, technology, that enables them. The loop visits each
    card in turn and plays its small story: one governed answer reaches many merchants; the right document comes back
    to the person while the restricted one keeps its lock; the sale data turns into a recommendation and the merchant's
    line turns upward. Then the enabler runs its delivery cycle and powers the three. Every card keeps its «?»:
    hypotheses to validate together."""
    if ORIENT() == "portrait":
        return _pn05_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    cols = ("var(--c1)", "var(--c2)", "var(--c3)", "var(--accent)")
    W, H, Y0, GAP = 232, 386, 104, 14
    xs = [830 + k * (W + GAP) for k in range(3)]
    BX, BY, BW, BH = 830, 548, 724, 216
    wins = ((2.2, 4.6), (4.6, 7.0), (7.0, 9.4), (9.4, _Q04_RESET[0]))
    R = _Q04_RESET

    def qmark(cx, cy, a):
        return (f'<circle cx="{cx}" cy="{cy}" r="15" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>'
                + TC(cx, cy + 6.5, "?", 18, "var(--c4)", W6) + _q04_ping(cx, cy, 15, 30, a + .05) + _q04_ping(cx, cy, 15, 30, a + .45))

    def spot(x, y, w, h, a, b):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_q04_win(a, b, .25)}</rect>'

    g = [glow(1192, 430, 470, "var(--brand)", .45)]
    stories = (_q04_answer(wins[0][0], ok), _q04_find(wins[1][0], ok, SKIN_BROWN), _q04_grow(wins[2][0], ok))
    parts = []
    for k in range(3):
        x, (area, idea, gain), (a, b) = xs[k], sl["cards"][k], wins[k]
        c = (card(x, Y0, W, H, "var(--card)", "var(--line)", 18, 1.2)
             + f'<rect x="{x + 18}" y="{Y0 - 2}" width="{W - 70}" height="4" rx="2" fill="{cols[k]}"/>'
             + T(x + 18, Y0 + 46, area, fit(area, 18, W - 36, "hypothesis area"), "var(--white)", W6)
             + TCW(x + 18, Y0 + 80, idea, _q04_chars(idea, 16, W - 36), 16, "var(--muted)", W6, 1.35, "start")
             + f'<g transform="translate({x + 18} {Y0 + 176})">{stories[k]}</g>'
             + T(x + 18, Y0 + 326, sl["ret"], fit(sl["ret"], 15, W - 36, "hypothesis return label"), "var(--muted)", W6)
             + T(x + 18, Y0 + 354, gain, fit(gain, 18, W - 36, "hypothesis return"), "var(--c4)", W6)
             + spot(x, Y0, W, H, a, b) + qmark(x + W - 30, Y0, a))
        parts.append(c)
    area, idea, gain = sl["cards"][3]
    a4 = wins[3][0]
    nodes = [1226 + 86 * k for k in range(4)]
    ny = BY + 100
    pipe = (f'<path d="M{nodes[0]} {ny} H{nodes[-1]}" stroke="var(--line)" stroke-width="2"/>'
            + "".join(card(x - 26, ny - 26, 52, 52, "var(--dim)", "var(--line)", 12, 1.2) + f'<g transform="translate({x} {ny})">{_q04_glyph(k)}</g>'
                      + f'<rect x="{x - 26}" y="{ny - 26}" width="52" height="52" rx="12" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity="0">{_q04_hold(a4 + .12 + .17 * k, .1)}</rect>'
                      for k, x in enumerate(nodes))
            + f'<g opacity="0">{_q04_key("opacity", [(a4 + .05, 0), (a4 + .1, 1), (a4 + .66, 1), (a4 + .72, 0)])}'
              f'{_q04_move(f"M{nodes[0]} {ny + 40} H{nodes[-1]}", [(a4 + .1, 0), (a4 + .66, 1)])}{token("var(--c4)", 5)}</g>'
            + f'<path d="M{nodes[0]} {ny + 40} H{nodes[-1]}" stroke="var(--c4)" stroke-width="1.5" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">'
              f'{_q04_key("stroke-dashoffset", [(a4 + .1, 1), (a4 + .66, 0), (R[0], 0), (R[1], 1)])}</path>')
    base = (card(BX, BY, BW, BH, "var(--card)", "var(--line)", 18, 1.2)
            + f'<rect x="{BX + 18}" y="{BY - 2}" width="{BW - 76}" height="4" rx="2" fill="{cols[3]}"/>'
            + T(BX + 18, BY + 46, area, fit(area, 18, 300, "hypothesis area"), "var(--white)", W6)
            + TCW(BX + 18, BY + 80, idea, _q04_chars(idea, 16, 340), 16, "var(--muted)", W6, 1.35, "start")
            + T(BX + 18, BY + 184, gain, fit(gain, 18, 340, "hypothesis enabler"), "var(--c4)", W6)
            + TC((nodes[0] + nodes[-1]) / 2, BY + 184, sl["cycle"], fit(sl["cycle"], 15, 320, "hypothesis cycle"), "var(--muted)", W6)
            + pipe + spot(BX, BY, BW, BH, *wins[3]) + qmark(BX + BW - 30, BY, a4))
    parts.append(base)
    # the enabler powers the three: a pulse climbs each pillar into its card
    pillars = []
    for k, x in enumerate(xs):
        cx = x + W / 2
        t = a4 + .75 + .08 * k
        pillars.append(f'<path d="M{cx} {BY} V{Y0 + H}" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="3 5" opacity=".6"/>'
                       f'<path d="M{cx} {BY} V{Y0 + H}" stroke="var(--c4)" stroke-width="2" opacity="0">{_q04_hold(t, .12)}</path>'
                       + _q04_trip(f"M{cx} {BY} V{Y0 + H}", t - .03, t + .3, "var(--c4)", 4)
                       + f'<circle cx="{cx}" cy="{Y0 + H}" r="4" fill="var(--c4)" opacity="0">{_q04_hold(t + .3, .1)}</circle>'
                       f'<circle cx="{cx}" cy="{BY}" r="4" fill="var(--c4)"/>')
    g.append(seq(parts, .1, .5, 16))
    g.append(land("".join(pillars), 1.2, .45, 0))
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 6 · governed knowledge in spaces, open and restricted
def _q04_open_lock(x, y, col):
    """An open padlock centered at (x, y): the shackle lifted and free on one side (an open space)."""
    return (f'<g fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round">'
            f'<path d="M{x - 6} {y - 2} V{y - 10} A6 6 0 0 1 {x + 6} {y - 10} V{y - 7}"/>'
            f'<rect x="{x - 9}" y="{y - 2}" width="18" height="14" rx="3" fill="{col}" fill-opacity=".15"/></g>')


def _pn06_twin(sl, ctx):
    """n06 on the 900x1600 stage: Atención's question on top, the three spaces as full-width rows (name, padlock and
    kind, the agent, three sources), Riesgo's question under them, then the rule and the foot. Atención's channel runs
    down the right gutter into its agent; its probe drops into Riesgo's row and bounces off the lock. Same loop and
    frozen frame; labels painted after the art."""
    ok = ctx.brand.c("dark.ok")
    a1, a2 = 2.3, 6.2
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    RX, RW, RH = zx, zw - 24, 132
    GX = RX + RW + 12                                   # the right gutter, Atención's channel
    ax = RX + 352                                       # the agents' column
    rys = [zy + 176 + k * (RH + 12) for k in range(3)]
    art, text = [glow(zx + zw / 2, zy + zh * .45, 470, "var(--brand)", .45)], []

    def ask(x, w, y, q):
        room = w - 40
        lines = min(2, len(_q04_wrap(_(str(q)), _q04_chars(q, 21, room))))
        h = 34 + 27 * lines
        return card(x, y, w, h, "var(--c1)", "var(--line)", 18) + _pn05_text(x + 20, y + 37, q, 21, room, ctx.brand.on("var(--c1)")), h

    def answer(x, y, w, src, at):
        pw = min(380, bold_width(_(str(src)), 20, current_factor()) + 36)
        pcx = x + w - 48 - pw / 2
        inner = (card(x, y, w, 56, "var(--card)", "var(--c4)", 18, 1.5) + spark(x + 26, y + 28, .62)
                 + f'<rect x="{x + 50}" y="{y + 19}" width="{max(20, min(200, pcx - pw / 2 - x - 66)):.0f}" height="6" rx="3" fill="var(--c2)" opacity=".75"/>'
                 + f'<rect x="{x + 50}" y="{y + 32}" width="{max(12, min(140, pcx - pw / 2 - x - 90)):.0f}" height="6" rx="3" fill="var(--c2)" opacity=".5"/>'
                 + pill(pcx, y + 28, src, "var(--dim)", ctx, 20, 380, "knowledge source", 18))
        return (f'<g opacity="0">{_q04_hold(at, .2)}<g>{_q04_tr([(at, "0 10"), (at + .3, "0 0")])}{inner}</g></g>'
                + _q04_badge(x + w - 24, y + 28, at + .25, ok))

    # the spaces
    spaces = sl["spaces"][:3]
    ns = min(fit(name, 22, 290, "knowledge space", floor=20) for name, kind, closed, docs in spaces)
    opens = {1: (a1 + .35, a1 + 1.9), 2: (a2 + .45, a2 + 2.05)}
    rows, locks = {}, []
    for k, (y, (name, kind, closed, docs)) in enumerate(zip(rys, spaces)):
        col = "var(--accent)" if closed else "var(--c2)"
        lx, ly = RX + 30, y + 68
        c = (card(RX, y, RW, RH, "var(--card)", col, 16, 1.4 if closed else 1.2)
             + f'<rect x="{RX + 18}" y="{y - 2}" width="{RW * .4:.0f}" height="4" rx="2" fill="{col}"/>'
             + card(ax - 34, y + 40, 68, 56, "var(--dim)", col, 12, 1.4)
             + f'<g>{loop("opacity", ".55;1;.55", 3, k * .9)}{spark(ax, y + 68, .7, col)}</g>')
        t = (T(RX + 20, y + 36, name, ns, "var(--white)", W6)
             + T(RX + 50, y + 75, kind, fit(kind, 20, 240, "knowledge space kind", floor=20), "var(--muted)", W6)
             + T(RX + 20, y + 116, sl["agent"], fit(sl["agent"], 20, 280, "knowledge agent", floor=20), "var(--c4)", W6))
        if not closed:
            c += _q04_open_lock(lx, ly, col)
        else:
            a, b = opens.get(k, (D, D))
            lift = _q04_tr([(a, "0 0"), (a + .15, "0 -5"), (b, "0 -5"), (b + .15, "0 0")])
            shake = _q04_shake(a1 + .95) if k == 2 else ""
            locks.append(f'<g>{shake}{_q04_lock(lx, ly, "var(--accent)", lift)}</g>' + _q04_ping(lx, ly + 4, 11, 26, a, ok, 1.8, .5))
        for j, lab in enumerate(docs[:3]):
            yy = y + 40 + 34 * j
            rows[(k, j)] = yy
            c += _q04_doc(RX + 420, yy - 15, col)
            t += T(RX + 446, yy, lab, fit(lab, 20, RW - 462, "knowledge doc", floor=20), "var(--white)", W6)
        art.append(land(c, .3 + .1 * k, .5, 16))
        text.append(land(t, .3 + .1 * k, .5, 16))
    art.append(land("".join(locks), .75, .4, 0))

    def lit(k, j, at):
        yy = rows[(k, j)]
        return (f'<rect x="{RX + 408}" y="{yy - 24}" width="{RW - 418}" height="32" rx="8" fill="var(--c4)" fill-opacity=".1" '
                f'stroke="var(--c4)" stroke-width="1.5" opacity="0">{_q04_hold(at, .12)}</rect>')

    def pulse(k, at):
        cy = rys[k] + 68
        return (f'<circle cx="{ax}" cy="{cy}" r="34" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity="0">'
                + _q04_key("r", [(at - .05, 34), (at + .4, 56)]) + _q04_key("opacity", [(at - .06, 0), (at - .05, .9), (at + .4, 0)]) + '</circle>'
                + _q04_flash(ax - 34, rys[k] + 40, 68, 56, 12, at, "var(--c4)", .5))

    def climb(k, j, at):
        yy = rows[(k, j)]
        return lit(k, j, at) + _q04_trip(f"M{RX + 418} {yy - 6} C{ax + 70} {yy - 6} {ax + 60} {rys[k] + 68} {ax + 34} {rys[k] + 68}", at, at + .32, "var(--c4)", 5)

    # the people who ask: Atención on top, Riesgo under the spaces
    who1, who2 = sl["who"]
    q1, h1 = ask(RX + 96, zw - 96, zy + 8, sl["ask1"])
    y2 = rys[-1] + RH + 16
    q2, h2 = ask(RX, zw - 110, y2, sl["ask2"])
    art.append(land(_q04_bust(RX + 42, zy + 30, 1.3, SKIN_LIGHT, "var(--accent)", True), .1, .5, -14)
               + land(_q04_bust(zx + zw - 46, y2 + 22, 1.3, SKIN_BROWN, "var(--c3)"), .6, .5, 14))
    text.append(land(q1 + TC(RX + 42, zy + 96, who1, fit(who1, 20, 92, "knowledge who", floor=20), "var(--muted)", W6), .1, .5, -14)
                + land(q2 + TC(zx + zw - 46, y2 + 88, who2, fit(who2, 20, 92, "knowledge who", floor=20), "var(--muted)", W6), .6, .5, 14))

    # the channels each question travels
    top1 = zy + 8 + h1
    ch1 = f"M{GX} {top1} V{rys[1] - 6} H{ax} V{rys[1] + 40}"
    ch2 = f"M{ax} {y2} V{rys[2] + 96}"
    art.append(land("".join(f'<path d="{d}" fill="none" stroke="var(--c4)" stroke-width="1.4" stroke-dasharray="3 5" opacity=".45">'
                            f'{loop("stroke-dashoffset", "0;-16", 1.4)}</path>' for d in (ch1, ch2)), .5, .4, 0))
    ya1 = zy + 104
    # act 1 · Atención asks: its space opens, its agent reads its own space and the open one, Riesgo stays locked
    r3 = rys[2]
    probe = (_q04_trip(f"M{ax} {rys[1] + 96} V{r3 + 2}", a1 + .7, a1 + .95, "var(--c5)", 5)
             + _q04_ping(RX + 30, r3 + 72, 11, 26, a1 + .95, "var(--c5)", 1.8, .5)
             + _q04_flash(RX, r3, RW, RH, 16, a1 + .95, "var(--c5)", .6)
             + f'<g opacity="0">{_q04_win(a1 + .95, a1 + 2.2, .15)}{pill(ax + 130, r3 + 20, sl["deny"], "var(--c5)", ctx, 20, 200, "knowledge deny", 16)}</g>')
    art.append(_q04_flash(RX + 96, zy + 8, zw - 96, h1, 18, a1, "var(--c4)", .5)
               + _q04_trip(ch1, a1 + .05, a1 + .45, "var(--c4)", 6)
               + pulse(1, a1 + .5) + climb(1, 0, a1 + .6) + lit(0, 2, a1 + .62)
               + _q04_trip(f"M{RX + 418} {rows[(0, 2)] - 6} H{RX + 400} V{rys[1] - 6} H{ax} V{rys[1] + 40}", a1 + .62, a1 + 1.05, "var(--c4)", 5)
               + probe + _q04_trip(ch1, a1 + 1.25, a1 + 1.6, "var(--c4)", 6, True))
    text.append(answer(RX + 96, max(ya1, top1 + 10), zw - 124, sl["src1"], a1 + 1.6))
    # act 2 · Riesgo asks: only its restricted space answers, for its members
    art.append(_q04_flash(RX, y2, zw - 110, h2, 18, a2, "var(--c4)", .5)
               + _q04_trip(ch2, a2 + .05, a2 + .45, "var(--c4)", 6)
               + pulse(2, a2 + .6) + climb(2, 0, a2 + .7)
               + _q04_trip(ch2, a2 + 1.15, a2 + 1.55, "var(--c4)", 6, True))
    ya2 = y2 + h2 + 12
    text.append(answer(RX, ya2, zw - 110, sl["src2"], a2 + 1.55))
    cx = zx + zw / 2
    ry = ya2 + 94
    text.append(f'<g opacity="0">{_q04_hold(a2 + 2.4, .3)}' + _pn05_text(RX + 10, ry, sl["rule"], 23, zw - 20, "var(--c4)") + '</g>')
    fs = fit(sl["foot"], 20, zw - 80, "knowledge foot", floor=20)
    qx = cx - bold_width(_(str(sl["foot"])), fs, current_factor()) / 2 - 26
    fy = zy + zh - 12
    text.append(land(f'<circle cx="{qx:.0f}" cy="{fy - 7}" r="14" fill="none" stroke="var(--c4)" stroke-width="1.4"/>'
                     + TC(f"{qx:.0f}", fy, "?", 20, "var(--c4)", W6) + TC(cx, fy, sl["foot"], fs, "var(--muted)", W6), .9, .45, 8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "n06_conocimiento")
def sc_n06_conocimiento(sl, ctx):
    """What the company knows, in three spaces: one open to everyone and two restricted to their teams, each with its own
    agent. Atención asks what changes with the new regulation: its space opens for its member, its agent reads its own
    space and the open one, and its probe into Riesgo's space bounces off the lock; the answer comes back with its
    source. Then Riesgo asks: only its space opens, for its members, and its agent answers from there with its source.
    The frozen frame: both answered, each with its source, both restricted spaces closed to the rest, and the rule under
    them: each agent inherits the permissions of its space."""
    if ORIENT() == "portrait":
        return _pn06_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    a1, a2 = 2.3, 6.2
    g = [glow(1190, 400, 470, "var(--brand)", .45)]
    # the three spaces: name, the kind with its padlock (open or closed), the agent, three sources
    SY, SW, SH = 250, 228, 300
    sxs = (840, 1086, 1332)
    spaces = sl["spaces"][:3]
    ns = min(fit(name, 18, SW - 36, "knowledge space") for name, kind, closed, docs in spaces)
    opens = {1: (a1 + .35, a1 + 1.9), 2: (a2 + .45, a2 + 2.05)}   # a restricted space opens only for its own team
    tiles, rows, locks = [], {}, []
    for k, (x, (name, kind, closed, docs)) in enumerate(zip(sxs, spaces)):
        col = "var(--accent)" if closed else "var(--c2)"
        ax, lx, ly = x + SW / 2, x + 27, SY + 60
        c = (card(x, SY, SW, SH, "var(--card)", col, 16, 1.4 if closed else 1.2)
             + f'<rect x="{x + 18}" y="{SY - 2}" width="{SW - 70}" height="4" rx="2" fill="{col}"/>'
             + T(x + 18, SY + 38, name, ns, "var(--white)", W6)
             + T(x + 44, SY + 68, kind, fit(kind, 15, SW - 62, "knowledge space kind"), "var(--muted)", W6)
             + card(ax - 44, SY + 88, 88, 58, "var(--dim)", col, 12, 1.4)
             + f'<g>{loop("opacity", ".55;1;.55", 3, k * .9)}{spark(ax, SY + 117, .7, col)}</g>'
             + TC(ax, SY + 170, sl["agent"], fit(sl["agent"], 15, SW - 36, "knowledge agent"), "var(--c4)", W6))
        if not closed:
            c += _q04_open_lock(lx, ly, col)
        else:
            a, b = opens.get(k, (D, D))   # a restricted space no one asks from stays closed
            lift = _q04_tr([(a, "0 0"), (a + .15, "0 -5"), (b, "0 -5"), (b + .15, "0 0")])
            shake = _q04_shake(a1 + .95) if k == 2 else ""
            locks.append(f'<g>{shake}{_q04_lock(lx, ly, "var(--accent)", lift)}</g>' + _q04_ping(lx, ly + 4, 11, 26, a, ok, 1.8, .5))
        for j, lab in enumerate(docs[:3]):
            yy = SY + 210 + 31 * j
            rows[(k, j)] = (x, yy)
            c += _q04_doc(x + 18, yy - 14, col) + T(x + 42, yy, lab, fit(lab, 15, SW - 58, "knowledge doc"), "var(--white)", W6)
        tiles.append(c)
    ay = SY + 117   # the agents' row

    def lit(k, j, at):
        x, yy = rows[(k, j)]
        return (f'<rect x="{x + 8}" y="{yy - 20}" width="{SW - 16}" height="29" rx="8" fill="var(--c4)" fill-opacity=".1" '
                f'stroke="var(--c4)" stroke-width="1.5" opacity="0">{_q04_hold(at, .12)}</rect>')

    def pulse(k, at):
        ax = sxs[k] + SW / 2
        return (f'<circle cx="{ax}" cy="{ay}" r="30" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity="0">'
                + _q04_key("r", [(at - .05, 30), (at + .4, 50)]) + _q04_key("opacity", [(at - .06, 0), (at - .05, .9), (at + .4, 0)]) + '</circle>'
                + _q04_flash(ax - 44, SY + 88, 88, 58, 12, at, "var(--c4)", .5))

    def climb(k, j, at):
        """A source lights, and what it holds climbs to its agent."""
        x, yy = rows[(k, j)]
        ax = sxs[k] + SW / 2
        return (lit(k, j, at) + _q04_trip(f"M{x + 25} {yy - 16} C{x + 25} {SY + 170} {ax - 30} {SY + 156} {ax - 24} {SY + 146}", at, at + .32, "var(--c4)", 4))

    def answer(x, y, w, src, at):
        s = fit(src, 15, 230, "knowledge source")
        pw = min(262, bold_width(_(str(src)), s, current_factor()) + 32)
        pcx = x + w - 44 - pw / 2
        inner = (card(x, y, w, 56, "var(--card)", "var(--c4)", 18, 1.5) + spark(x + 26, y + 28, .62)
                 + f'<rect x="{x + 50}" y="{y + 19}" width="{min(200, pcx - pw / 2 - x - 66):.0f}" height="6" rx="3" fill="var(--c2)" opacity=".75"/>'
                 + f'<rect x="{x + 50}" y="{y + 32}" width="{min(140, pcx - pw / 2 - x - 90):.0f}" height="6" rx="3" fill="var(--c2)" opacity=".5"/>'
                 + pill(pcx, y + 28, src, "var(--dim)", ctx, 15, 262, "knowledge source", 16))
        return (f'<g opacity="0">{_q04_hold(at, .2)}<g>{_q04_tr([(at, "0 10"), (at + .3, "0 0")])}{inner}</g></g>'
                + _q04_badge(x + w - 24, y + 28, at + .25, ok))

    # the people who ask: Atención on top, Riesgo at the bottom, each with the question of its team
    who1, who2 = sl["who"]
    top = (_q04_bust(870, 144, 1.25, SKIN_LIGHT, "var(--accent)", True) + TC(870, 206, who1, fit(who1, 15, 80, "knowledge who"), "var(--muted)", W6)
           + bubble(912, 106, 628, sl["ask1"], ctx, "var(--c1)", 18, "knowledge question"))
    bottom = (_q04_bust(1508, 614, 1.25, SKIN_BROWN, "var(--c3)") + TC(1508, 676, who2, fit(who2, 15, 80, "knowledge who"), "var(--muted)", W6)
              + bubble(840, 586, 620, sl["ask2"], ctx, "var(--c1)", 18, "knowledge question"))

    # the channels each question travels, from the team to the agent of its space and back as the answer
    at_x, rk_x = sxs[1] + SW / 2, sxs[2] + SW / 2
    gap1 = (sxs[0] + SW + sxs[1]) / 2
    ch1 = f"M{gap1} 162 V{ay} H{at_x - 44}"
    ch2 = f"M1420 586 C1420 566 1540 576 1540 540 V380 Q1540 {ay} {rk_x + 44} {ay}"
    wires = "".join(f'<path d="{d}" fill="none" stroke="var(--c4)" stroke-width="1.2" stroke-dasharray="3 5" opacity=".45">'
                    f'{loop("stroke-dashoffset", "0;-16", 1.4)}</path>' for d in (ch1, ch2))

    # act 1 · Atención asks: its space opens for it, its agent reads its own space and the open one, Riesgo stays locked
    probe = (_q04_trip(f"M{at_x + 44} {ay} H{sxs[2] - 2}", a1 + .7, a1 + .95, "var(--c5)", 4)
             + _q04_ping(sxs[2] + 27, SY + 64, 11, 26, a1 + .95, "var(--c5)", 1.8, .5)
             + _q04_flash(sxs[2], SY, SW, SH, 16, a1 + .95, "var(--c5)", .6)
             + f'<g opacity="0">{_q04_win(a1 + .95, a1 + 2.2, .15)}{pill(sxs[2] - 6, ay, sl["deny"], "var(--c5)", ctx, 15, 150, "knowledge deny", 14)}</g>')
    act1 = (_q04_flash(912, 106, 628, 56, 18, a1, "var(--c4)", .5)
            + _q04_trip(ch1, a1 + .05, a1 + .45, "var(--c4)", 5)
            + pulse(1, a1 + .5) + climb(1, 0, a1 + .6)
            + lit(0, 2, a1 + .62)
            + _q04_trip(f"M{sxs[0] + SW - 10} {rows[(0, 2)][1] - 6} H{gap1} V{ay} H{at_x - 44}", a1 + .62, a1 + 1.05, "var(--c4)", 4)
            + probe
            + _q04_trip(ch1, a1 + 1.25, a1 + 1.6, "var(--c4)", 5, True)
            + answer(972, 172, 568, sl["src1"], a1 + 1.6))
    # act 2 · Riesgo asks: only its restricted space answers, for its members, and it closes again
    act2 = (_q04_flash(840, 586, 620, 56, 18, a2, "var(--c4)", .5)
            + _q04_trip(ch2, a2 + .05, a2 + .45, "var(--c4)", 5)
            + pulse(2, a2 + .6) + climb(2, 0, a2 + .7)
            + _q04_trip(ch2, a2 + 1.15, a2 + 1.55, "var(--c4)", 5, True)
            + answer(840, 650, 560, sl["src2"], a2 + 1.55))
    rule = (f'<g opacity="0">{_q04_hold(a2 + 2.4, .3)}'
            + TC(1190, 764, sl["rule"], fit(sl["rule"], 19, 720, "knowledge rule"), "var(--c4)", W6) + '</g>')
    fs = fit(sl["foot"], 15, 640, "knowledge foot")
    qx = 1190 - bold_width(_(str(sl["foot"])), fs, current_factor()) / 2 - 22
    foot = (f'<circle cx="{qx:.1f}" cy="801" r="11" fill="none" stroke="var(--c4)" stroke-width="1.4"/>'
            + TC(f"{qx:.1f}", 806, "?", 15, "var(--c4)", W6) + TC(1190, 806, sl["foot"], fs, "var(--muted)", W6))
    g += [land(wires, .5, .4, 0), land(top, .1, .5, -14), seq(tiles, .3, .5, 16), land("".join(locks), .75, .4, 0),
          land(bottom, .6, .5, 14), land(foot, .9, .45, 8), act1, act2, rule]
    return "".join(g), D, FREEZE

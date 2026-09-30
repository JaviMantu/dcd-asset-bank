"""Group A: slides 1-3 of the pagos deck. Three loops, one arc: outside, how we looked, inside.
n01_portada   - the promise as a living street: people pay in store and online (POS, QR, link, app), merchants of every
                size light up, the data rises into one connected flow and an opportunity opens for each of them; a far
                skyline of tiny lit shops says «hundreds of thousands» without a number.
n02_afuera    - from outside: public sources feed our notebook, a hypothesis comes out, and a question drops onto each of
                their four teams, drawn as a ghost: the inside is theirs to tell (slide 3 lights the same four teams).
n03_respuesta - the mechanism, one case: a new rule arrives, the governed knowledge takes it in, and product, commercial,
                risk and merchant support each get their own answer in their space, all before the rule comes into force.
Merchants, devices and teams are drawn by position, never by text, so every language keeps the same art. Reuses the energía
helpers _n01_on, _n01_tr, _n01_source and _n01_lens (energia_s01_03.py, loaded before this file)."""


def _q01_arc_y(x, r, cx=1190, cy=1570):
    return cy - math.sqrt(r * r - (x - cx) ** 2)


def _q01_sw(col, w=1.6):
    return f'fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"'


# ---------------------------------------------------------------- glyphs (drawn around 0,0 or on a baseline at y 0)
def _q01_shop(k):
    """Merchant k on its baseline, smallest to largest: 0 bodega, 1 restaurant, 2 store, 3 large store that also sells
    online. Returns (outline, windows): the windows are drawn twice, dim in the outline and lit in the loop."""
    sw = _q01_sw("var(--c2)")
    st = 'stroke="var(--c2)" stroke-width="1.6" stroke-linejoin="round"'
    if k == 0:
        body = (f'<rect x="-44" y="-50" width="88" height="50" rx="3" fill="var(--card)" stroke="var(--c2)" stroke-width="1.6"/>'
                f'<path d="M-50 -50 L-44 -66 H44 L50 -50 Z" fill="var(--card)" {st}/>'
                + "".join(f'<path d="M{x0} -66 L{x0 - 3} -50" {sw}/>' for x0 in (-26, -8, 10, 28))
                + f'<rect x="10" y="-36" width="22" height="36" rx="2" {sw}/>')
        win = [(-34, -38, 34, 22)]
    elif k == 1:
        body = (f'<rect x="-56" y="-74" width="112" height="74" rx="3" fill="var(--card)" stroke="var(--c2)" stroke-width="1.6"/>'
                f'<rect x="-34" y="-94" width="68" height="16" rx="8" fill="var(--card)" {st}/>'
                f'<path d="M-8 -91 H5 V-85 C5 -82 2 -80 -1.5 -80 C-5 -80 -8 -82 -8 -85 Z M5 -89 H8 C10 -89 10 -85 8 -85 H5" {sw}/>'
                f'<rect x="24" y="-44" width="24" height="44" rx="2" {sw}/>')
        win = [(-46, -60, 60, 36)]
    elif k == 2:
        body = (f'<rect x="-66" y="-88" width="132" height="88" rx="3" fill="var(--card)" stroke="var(--c2)" stroke-width="1.6"/>'
                f'<path d="M-72 -88 L-66 -108 H66 L72 -88 Z" fill="var(--card)" {st}/>'
                + "".join(f'<path d="M{x0} -108 L{x0 - 4} -88" {sw}/>' for x0 in (-44, -22, 0, 22, 44))
                + f'<rect x="-14" y="-48" width="28" height="48" rx="2" {sw}/>')
        win = [(-56, -74, 34, 34), (22, -74, 34, 34)]
    else:
        body = (f'<rect x="-76" y="-132" width="152" height="132" rx="4" fill="var(--card)" stroke="var(--c2)" stroke-width="1.6"/>'
                f'<path d="M-76 -110 H76" {sw}/>'
                f'<path d="M-14 -126 H-9 L-6 -116 H6 L9 -123 H-7 M-3 -113 v.1 M4 -113 v.1" {sw}/>'
                f'<rect x="-16" y="-40" width="32" height="40" rx="2" {sw}/>')
        win = [(x0, y0, 30, 20) for y0 in (-98, -70) for x0 in (-62, -15, 32)] + [(-62, -40, 30, 26), (32, -40, 30, 26)]
    dim = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.2" opacity=".8"/>' for x, y, w, h in win)
    lit = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="var(--c4)" opacity=".85"/>' for x, y, w, h in win)
    return body + dim, lit


def _q01_device(k):
    """What the person pays with, held up: 0 a card (POS), 1 a phone showing a QR, 2 a phone with a link, 3 a phone with an app."""
    if k == 0:
        return (f'<rect x="-17" y="-11" width="34" height="22" rx="3" fill="var(--c1)" stroke="var(--c2)" stroke-width="1.4"/>'
                f'<path d="M-17 -4 H17" stroke="var(--c2)" stroke-width="2.5"/><rect x="-12" y="2" width="8" height="5" rx="1" fill="var(--c4)"/>')
    phone = f'<rect x="-12" y="-20" width="24" height="40" rx="4" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.4"/>'
    if k == 1:
        q = "".join(f'<rect x="{x}" y="{y}" width="5" height="5" fill="var(--c4)"/>' for x, y in ((-8, -12), (3, -12), (-8, -1), (4, 2), (-2, -6), (3, -4)))
        return phone + q
    if k == 2:
        return phone + f'<path d="M-4 -2 L-7 1 A3.5 3.5 0 0 0 -2 6 L1 3 M4 -2 L7 -5 A3.5 3.5 0 0 0 2 -10 L-1 -7 M-3 1 L3 -5" {_q01_sw("var(--c4)", 1.6)}/>'
    return phone + "".join(f'<rect x="{x}" y="{y}" width="7" height="7" rx="2" fill="var(--c4)"/>' for x in (-8, 1) for y in (-11, -2))


def _q01_person(x, y, s, skin, jacket, hair, k):
    """A faceless person seen from behind (we stand with them, facing the shops), one arm up holding device k.
    hair: 0 short, 1 long, 2 bun. Returns (markup, device point in stage coordinates)."""
    rim = 'fill="none" stroke="var(--c2)" stroke-width="1.4" opacity=".8"'
    skin, jacket = shade(skin, 38), shade(jacket, 48)
    torso = "M-58 0 C-60 -58 -46 -94 -14 -103 C-6 -105 6 -105 14 -103 C46 -94 60 -58 58 0 Z"
    hairs = ("M-23 -136 C-25 -170 25 -170 23 -136 C22 -127 15 -122 0 -121 C-15 -122 -22 -127 -23 -136 Z",
             "M-24 -136 C-27 -172 27 -172 24 -136 C26 -118 27 -101 21 -90 C8 -86 -8 -86 -21 -90 C-27 -101 -26 -118 -24 -136 Z",
             "M-23 -136 C-25 -170 25 -170 23 -136 C22 -127 15 -122 0 -121 C-15 -122 -22 -127 -23 -136 Z")
    g = (f'<path d="{torso}" fill="{jacket}"/><path d="{torso}" {rim}/>'
         f'<path d="M-9 -121 H9 V-101 H-9 Z" fill="{shade(skin, 14)}"/>'
         f'<ellipse cx="-21" cy="-137" rx="4" ry="7" fill="{shade(skin, 14)}"/><ellipse cx="21" cy="-137" rx="4" ry="7" fill="{shade(skin, 14)}"/>'
         f'<ellipse cx="0" cy="-141" rx="21" ry="24" fill="{skin}"/>'
         f'<path d="{hairs[hair]}" fill="{HAIR}"/>'
         + (f'<circle cx="0" cy="-168" r="9" fill="{HAIR}"/>' if hair == 2 else "")
         + f'<path d="M-20 -150 C-14 -166 12 -168 21 -150" {rim}/>'
         f'<path d="M36 -92 C58 -100 66 -126 58 -150" fill="none" stroke="{jacket}" stroke-width="14" stroke-linecap="round"/>'
         f'<path d="M36 -92 C58 -100 66 -126 58 -150" {rim}/>'
         f'<circle cx="58" cy="-154" r="7.5" fill="{skin}"/>'
         f'<g transform="translate(60 -176)">{_q01_device(k)}</g>')
    return f'<g transform="translate({x} {y}) scale({s})">{g}</g>', (x + 60 * s, y - 176 * s)


def _q01_team(k, col="var(--c2)", w=1.6):
    """Team k: 0 producto (a cube), 1 comercial (a rising chart), 2 riesgo (a shield), 3 atención a comercios (a headset)."""
    sw = _q01_sw(col, w)
    if k == 0:
        return f'<path d="M0 -19 L17 -10 V10 L0 19 L-17 10 V-10 Z M-17 -10 L0 -1 L17 -10 M0 -1 V19" {sw}/>'
    if k == 1:
        return (f'<path d="M-18 17 H18" {sw}/><path d="M-13 17 V7 M-4 17 V1 M5 17 V-4 M14 17 V-10" {sw}/>'
                f'<path d="M-15 -3 L-5 -11 L3 -6 L14 -17 M8 -17 H14 V-11" {sw}/>')
    if k == 2:
        return f'<path d="M0 -20 L17 -13 V1 C17 11 10 17 0 21 C-10 17 -17 11 -17 1 V-13 Z" {sw}/><path d="M-7 0 L-2 6 L8 -6" {sw}/>'
    return (f'<path d="M-15 5 V-1 A15 15 0 0 1 15 -1 V5" {sw}/><rect x="-19" y="-1" width="8" height="14" rx="3" {sw}/>'
            f'<rect x="11" y="-1" width="8" height="14" rx="3" {sw}/><path d="M15 13 C15 19 9 21 2 21" {sw}/>')


def _q01_rule(col="var(--c4)"):
    """A new rule: a page with a folded corner and a seal."""
    sw = _q01_sw(col)
    return (f'<path d="M-14 -20 H5 L14 -11 V20 H-14 Z M5 -20 V-11 H14" {sw}/><path d="M-8 -8 H4 M-8 -1 H8" {sw}/>'
            f'<circle cx="4" cy="11" r="6" fill="{col}" fill-opacity=".25" stroke="{col}" stroke-width="1.6"/>')


def _q01_page(x, y, col="var(--c2)", op=".6"):
    """A knowledge row: a small page and two text bars."""
    return (f'<path d="M{x} {y - 10} h9 l5 5 v15 h-14 Z" fill="none" stroke="{col}" stroke-width="1.4" stroke-linejoin="round"/>'
            f'<rect x="{x + 24}" y="{y - 6}" width="80" height="6" rx="3" fill="{col}" opacity="{op}"/>'
            f'<rect x="{x + 24}" y="{y + 5}" width="52" height="6" rx="3" fill="{col}" opacity="{op}"/>')


# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
def _pn01_person(x, y, s, skin, jacket, hair, k):
    """_q01_person with fewer strokes (the portrait budget): torso, head, hair, the raised arm and device k."""
    sk, jk = shade(skin, 38), shade(jacket, 48)
    torso = "M-58 0 C-60 -58 -46 -94 -14 -103 C-6 -105 6 -105 14 -103 C46 -94 60 -58 58 0 Z"
    hairs = ("M-23 -136 C-25 -170 25 -170 23 -136 C22 -127 15 -122 0 -121 C-15 -122 -22 -127 -23 -136 Z",
             "M-24 -136 C-27 -172 27 -172 24 -136 C26 -118 27 -101 21 -90 C8 -86 -8 -86 -21 -90 C-27 -101 -26 -118 -24 -136 Z")
    g = (f'<path d="{torso}" fill="{jk}" stroke="var(--c2)" stroke-width="1.4" stroke-opacity=".8"/>'
         f'<ellipse cx="0" cy="-141" rx="21" ry="24" fill="{sk}"/><path d="{hairs[hair == 1]}" fill="{HAIR}"/>'
         + (f'<circle cx="0" cy="-168" r="9" fill="{HAIR}"/>' if hair == 2 else "")
         + f'<path d="M36 -92 C58 -100 66 -126 58 -150" fill="none" stroke="{jk}" stroke-width="14" stroke-linecap="round"/>'
         f'<circle cx="58" cy="-154" r="7.5" fill="{sk}"/><g transform="translate(60 -176)">{_q01_device(k)}</g>')
    return f'<g transform="translate({x:.0f} {y:.0f}) scale({s})">{g}</g>', (x + 60 * s, y - 176 * s)


def _pn01_twin(sl, ctx):
    """n01 on the 900x1600 stage: the constellation of opportunities on top, the connected flow under it, the four
    merchants on the horizon with the far skyline, the four people paying from the bottom. Same loop, same frozen frame;
    labels painted after all the art."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    X1, cx = zx + zw, zx + zw / 2
    R_H, HY, R_B, BY = 1100, zy + 470, 1100, zy + 270   # horizon and flow arcs: radius, height at the centre
    ay = lambda x, r, top: top + r - math.sqrt(r * r - (x - cx) ** 2)
    arc = lambda r, top, x0, x1: f"M{x0:.0f} {ay(x0, r, top):.1f} A{r} {r} 0 0 1 {x1:.0f} {ay(x1, r, top):.1f}"
    xs = [zx + 134, zx + 326, zx + 518, zx + 710]
    base = [ay(x, R_H, HY) for x in xs]
    tops = [b - h for b, h in zip(base, (66, 94, 108, 132))]
    ny = [zy + 60, zy + 146, zy + 60, zy + 146]
    art, text, chips = [glow(cx, zy + 300, 460, "var(--brand)", .6)], [], []
    # far skyline: tiny shops along the horizon, a few lights blinking out of step (payments everywhere)
    far, lights, x, j = [], [], zx + 20, 0
    while x < X1 - 30:
        w, h = 22 + (j * 7) % 15, 18 + (j * 37) % 34
        yb = ay(x + w / 2, R_H, HY) - 10
        far.append(f"{'M' if j == 0 else 'L'}{x:.0f} {yb - h:.0f} H{x + w:.0f}")
        if j % 3 == 0:
            lights.append(f'<rect x="{x + w / 2 - 2:.0f}" y="{yb - h + 6:.0f}" width="4" height="4" fill="var(--c4)">'
                          f'{loop("opacity", ".08;.9;.08", 2 + j % 5 * .6, j * 1.3 % 4)}</rect>')
        x, j = x + w, j + 1
    sil = "".join(far) + f" L{x:.0f} {ay(x, R_H, HY):.0f} A{R_H} {R_H} 0 0 0 {zx + 20} {ay(zx + 20, R_H, HY):.0f} Z"
    art.append(land(f'<path d="{sil}" fill="var(--dim)" stroke="var(--c2)" stroke-width="1" stroke-opacity=".35" opacity=".85"/>' + "".join(lights)
                    + f'<path d="{arc(R_H, HY, zx + 10, X1 - 10)}" fill="none" stroke="var(--c2)" stroke-width="1.6" opacity=".45"/>', .15, .6, 0))
    # the constellation of opportunities
    sky = "".join(f'<path d="M{xs[k]} {ny[k]} L{xs[k + 1]} {ny[k + 1]}" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="3 6" opacity=".45"/>' for k in range(3))
    sky += "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.8"/>' for x, y in zip(xs, ny))
    art.append(land(sky, .3, .6, 10))
    # the connected flow of data and knowledge, and the threads from each roof to the sky
    flow = arc(R_B, BY, zx + 20, X1 - 20)
    art.append(land(f'<path d="{flow}" fill="none" stroke="var(--c2)" stroke-width="22" opacity=".05"/>'
                    f'<path d="{flow}" fill="none" stroke="var(--c2)" stroke-width="1.8" opacity=".55"/>'
                    f'<path d="{flow}" fill="none" stroke="var(--c4)" stroke-width="2.4" stroke-dasharray="2 14" opacity=".85">{loop("stroke-dashoffset", "0;-32", 1.8)}</path>'
                    + "".join(f'<path d="M{x} {t:.0f} V{y + 7}" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="2 5" opacity=".5"/>' for x, t, y in zip(xs, tops, ny)), .45, .6, 0))
    ls = fit(sl["link"], 22, 300, "portada link", floor=20)
    lw = bold_width(_(str(sl["link"])), ls, current_factor()) + 32
    text.append(land(card(cx - lw / 2, BY - 64, lw, ls + 18, "var(--card)", "var(--c4)", (ls + 18) / 2, 1.4)
                     + TC(f"{cx:.0f}", f"{BY - 64 + 9 + ls * .86:.0f}", sl["link"], ls, "var(--c4)", W6), .45, .6, 0))
    # the merchants on the horizon, smallest to largest
    lit_shops = []
    for k, (x, b) in enumerate(zip(xs, base)):
        body, lit = _q01_shop(k)
        art.append(pop(body, x, b, .5 + k * .1, .45))
        lit_shops.append((x, b, lit))
    # the people, from behind, each with what they pay with
    py, ps = zy + zh - 8, 1.12
    people = [(SKIN_BROWN, "var(--accent)", 1), (SKIN_LIGHT, "var(--c1)", 0), (SKIN_LIGHT, "var(--c3)", 2), (SKIN_BROWN, "var(--c1)", 0)]
    devs = []
    for k, (skin, jacket, hair) in enumerate(people):
        m, dev = _pn01_person(xs[k] - 60 * ps, py, ps, skin, jacket, hair, k)
        art.append(land(m, .7 + k * .1, .6, 30))
        devs.append(dev)
    lab = sl["merchants"]
    s = fit(lab, 24, 700, "portada merchants", floor=20)
    mw = bold_width(_(str(lab)), s, current_factor())
    my, dot = HY + 108, cx - mw / 2 - 8
    text.append(land(TC(f"{cx + 12:.0f}", my, lab, s, "var(--c4)", W6)
                     + f'<circle cx="{dot:.0f}" cy="{my - 7}" r="6" fill="{ok}"/>'
                     + f'<circle cx="{dot:.0f}" cy="{my - 7}" r="6" fill="none" stroke="{ok}" stroke-width="1.8">{loop("r", "6;15;6", 2.4)}{loop("opacity", "1;0;1", 2.4)}</circle>',
                     1.3, .5, 10))
    # the loop: four payments, each opens an opportunity and brings knowledge back
    for k, ((x, b, lit), (dx, dy), t0) in enumerate(zip(lit_shops, devs, (.12, .27, .42, .57))):
        pay_end, rise0, bloom, back0, done = t0 + .045, t0 + .05, t0 + .09, t0 + .095, t0 + .135
        door = f"M{dx:.0f} {dy - 24:.0f} C{dx:.0f} {dy - 90:.0f} {x} {b + 50:.0f} {x} {b - 14:.0f}"
        up, down = f"M{x} {tops[k]:.0f} V{ny[k]}", f"M{x} {ny[k]} V{tops[k]:.0f}"
        art.append(f'<g>{_n01_on(t0 + .005, pay_end, .005)}{token("var(--c4)", 7)}{move(door, [(0, 0), (t0, 0), (pay_end, 1), (1, 1)], D)}</g>'
                   f'<g>{_n01_on(pay_end)}<g transform="translate({x} {b:.0f})">{glow(0, -40, 110, "var(--c4)", .22)}{lit}</g></g>'
                   f'<g>{_n01_on(rise0, bloom, .005)}{token("var(--c4)", 6)}{move(up, [(0, 0), (rise0, 0), (bloom, 1), (1, 1)], D)}</g>'
                   f'<g>{_n01_on(back0, done, .005)}{token(ok, 6)}{move(down, [(0, 0), (back0, 0), (done, 1), (1, 1)], D)}</g>')
        if k:
            art.append(f'<g>{_n01_on(bloom)}<path d="M{xs[k - 1]} {ny[k - 1]} L{x} {ny[k]}" stroke="var(--c4)" stroke-width="2" opacity=".8"/></g>')
        w0 = (88, 112, 132, 152)[k] / 2
        art.append(f'<g>{_n01_on(done)}<circle cx="{x + w0 - 4:.0f}" cy="{tops[k] + 6:.0f}" r="13" fill="{ok}"/>' + check(f"{x + w0 - 4:.0f}", f"{tops[k] + 6.5:.1f}", .65, "var(--ink)") + '</g>')
        chips.append(f'<g>{_n01_on(t0)}' + pill(dx, dy - 52, sl["means"][k], "var(--c4)", ctx, 20, 130, "portada means", 14) + '</g>')
        opp = sl["opportunities"][k]
        s_ = fit(opp, 22, 190, "portada opportunity", floor=20)
        w_ = bold_width(_(str(opp)), s_, current_factor()) + 48
        h_ = s_ + 22
        ox = min(max(x, zx + w_ / 2), X1 - w_ / 2)
        chip = (card(-w_ / 2, -h_ / 2, w_, h_, "var(--card)", "var(--c4)", h_ / 2, 1.8)
                + spark(-w_ / 2 + 19, 0, .5, "var(--c4)") + T(f"{-w_ / 2 + 34:.0f}", f"{s_ * .36:.0f}", opp, s_, "var(--white)", W6))
        chips.append(f'<g>{_n01_on(bloom, 1, .02)}<g transform="translate({ox:.0f} {ny[k]})"><g>{_n01_tr([(0, "0 10"), (bloom, "0 10"), (bloom + .02, "0 0"), (1, "0 0")])}{chip}</g></g></g>')
    return portrait_mark("".join(art) + "".join(text) + "".join(chips)), D, FREEZE


# ---------------------------------------------------------------- slide 1: the promise, alive
@register("scene", "n01_portada")
def sc_n01_portada(sl, ctx):
    """A street at dusk seen from behind four people. On the horizon, merchants of every size (bodega, restaurant,
    store, large store that also sells online) and, far behind, a skyline of tiny shops whose lights keep blinking:
    hundreds of thousands. Above the roofs, one connected flow of data and knowledge; above it, a dim constellation.
    Loop: each person pays (POS, QR, link, app), the shop lights, the payment rises as data through the flow and opens
    that shop's opportunity in the sky, and knowledge comes back down as a green check: every business moves faster.
    Frozen frame: four payments made, four shops lit and checked, four opportunities open, the constellation joined."""
    if ORIENT() == "portrait":
        return _pn01_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    cx, R_H, R_BUS = 1190, 1100, 1030
    xs = [905, 1095, 1285, 1475]
    base = [_q01_arc_y(x, R_H) for x in xs]
    tops = [b - h for b, h in zip(base, (66, 94, 108, 132))]
    bus_y = lambda x: _q01_arc_y(x, R_BUS, cy=1330)
    ny = [214, 148, 214, 148]
    arc = lambda r, x0, x1, cy=1570: f"M{x0} {_q01_arc_y(x0, r, cy=cy):.1f} A{r} {r} 0 0 1 {x1} {_q01_arc_y(x1, r, cy=cy):.1f}"
    g = [glow(cx, 420, 500, "var(--brand)", .6), glow(cx, 500, 380, "var(--c4)", .1)]
    # the ground: curved lines and rays toward the horizon, faint
    ground = "".join(f'<path d="{arc(r, x0, 2 * cx - x0)}" fill="none" stroke="var(--c2)" stroke-width="1.2" opacity="{op}"/>'
                     for r, x0, op in ((1000, 830, .14), (900, 850, .1), (800, 880, .07)))
    ground += "".join(f'<path d="M{cx + (bx - cx) * .2:.0f} 500 L{bx} 830" stroke="var(--c2)" stroke-width="1" opacity=".07"/>' for bx in range(640, 1760, 112))
    g.append(land(ground, .1, .6, 0))
    # far skyline: tiny shops to the horizon, their lights blinking out of step (payments happening everywhere)
    far, lights, x = [], [], 832
    for j in range(60):
        w, h = 12 + (j * 7) % 11, 14 + (j * 37) % 31
        if x + w > 1548:
            break
        yb = _q01_arc_y(x + w / 2, R_H) - 10
        far.append(f"{'M' if j == 0 else 'L'}{x} {yb - h:.1f} H{x + w}")
        for i in range(1 + (h > 28)):
            lights.append(f'<rect x="{x + w / 2 - 1.5:.1f}" y="{yb - h + 5 + i * 10:.1f}" width="3" height="3" fill="var(--c4)">'
                          f'{loop("opacity", ".08;.9;.08", 2 + (j * 7 + i) % 5 * .6, (j * 1.3 + i * 1.7) % 4)}</rect>')
        x += w
    sil = "".join(far) + f" L{x} {_q01_arc_y(x, R_H):.1f} A{R_H} {R_H} 0 0 0 832 {_q01_arc_y(832, R_H):.1f} Z"
    g.append(land(f'<path d="{sil}" fill="var(--dim)" stroke="var(--c2)" stroke-width="1" stroke-opacity=".35" opacity=".85"/>' + "".join(lights)
                  + f'<path d="{arc(R_H, 820, 1560)}" fill="none" stroke="var(--c2)" stroke-width="1.4" opacity=".45"/>', .15, .6, 0))
    # the constellation of opportunities: dim nodes and links, always there
    sky = "".join(f'<path d="M{xs[k]} {ny[k]} L{xs[k + 1]} {ny[k + 1]}" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="3 6" opacity=".45"/>' for k in range(3))
    sky += "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.5"/>' for x, y in zip(xs, ny))
    sky += "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="var(--c2)" opacity=".6"/>' for x, y in ((1000, 118), (1190, 196), (1380, 118), (860, 150), (1530, 214)))
    g.append(land(sky, .3, .6, 10))
    # the connected flow of data and knowledge, and the threads from each roof up to the sky
    bus = (f'<path d="{arc(R_BUS, 850, 1530, 1330)}" fill="none" stroke="var(--c2)" stroke-width="18" opacity=".05"/>'
           f'<path d="{arc(R_BUS, 850, 1530, 1330)}" fill="none" stroke="var(--c2)" stroke-width="1.5" opacity=".55"/>'
           f'<path d="{arc(R_BUS, 850, 1530, 1330)}" fill="none" stroke="var(--c4)" stroke-width="2" stroke-dasharray="2 14" opacity=".85">{loop("stroke-dashoffset", "0;-32", 1.8)}</path>')
    threads = "".join(f'<path d="M{x} {t:.1f} V{y + 6}" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="2 5" opacity=".5"/>' for x, t, y in zip(xs, tops, ny))
    link = TC(cx, 286, sl["link"], fit(sl["link"], 15, 170, "portada link"), "var(--c4)", W6)
    g.append(land(bus + threads + link, .45, .6, 0))
    # the merchants on the horizon, smallest to largest
    lit_shops = []
    for k, (x, b) in enumerate(zip(xs, base)):
        body, lit = _q01_shop(k)
        g.append(pop(body, x, b, .5 + k * .1, .45))
        lit_shops.append((x, b, lit))
    # the people, from behind, each with what they pay with
    people = [(xs[0] - 62, 826, .92, SKIN_BROWN, "var(--accent)", 1), (xs[1] - 64, 826, .98, SKIN_LIGHT, "var(--c1)", 0),
              (xs[2] - 62, 826, .94, SKIN_LIGHT, "var(--c3)", 2), (xs[3] - 66, 826, .98, SKIN_BROWN, "var(--c1)", 0)]
    devs = []
    for k, (px, py, s, skin, jacket, hair) in enumerate(people):
        m, dev = _q01_person(px, py, s, skin, jacket, hair, k)
        g.append(land(m, .7 + k * .1, .6, 30))
        devs.append(dev)
    lab = sl["merchants"]
    size = fit(lab, 17, 470, "portada merchants")
    lw = bold_width(_(str(lab)), size, current_factor())
    dot = cx - lw / 2 - 12
    g.append(land(TC(cx + 10, 552, lab, size, "var(--c4)", W6)
                  + f'<circle cx="{dot:.1f}" cy="546" r="5" fill="{ok}"/>'
                  + f'<circle cx="{dot:.1f}" cy="546" r="5" fill="none" stroke="{ok}" stroke-width="1.5">{loop("r", "5;13;5", 2.4)}{loop("opacity", "1;0;1", 2.4)}</circle>',
                  1.3, .5, 10))
    # the loop: four payments, each opens an opportunity and brings knowledge back
    loops, joins = [], []
    for k, ((x, b, lit), (dx, dy), t0) in enumerate(zip(lit_shops, devs, (.12, .27, .42, .57))):
        pay_end, rise0, bloom, back0, done = t0 + .045, t0 + .05, t0 + .09, t0 + .095, t0 + .135
        door = f"M{dx:.1f} {dy - 22:.1f} C{dx:.1f} {dy - 90:.1f} {x} {b + 40:.1f} {x} {b - 14:.1f}"
        up = f"M{x} {tops[k]:.1f} V{ny[k]}"
        down = f"M{x} {ny[k]} V{tops[k]:.1f}"
        loops.append(f'<g>{_n01_on(t0, t0 + .06)}<circle cx="{dx:.1f}" cy="{dy:.1f}" r="30" fill="none" stroke="var(--c4)" stroke-width="2">{loop("r", "24;36;24", 1)}</circle></g>')
        loops.append(f'<g>{_n01_on(t0)}' + pill(dx, dy - 50, sl["means"][k], "var(--c4)", ctx, 15, 120, "portada means", 12) + '</g>')
        loops.append(f'<g>{_n01_on(t0 + .005, pay_end, .005)}{token("var(--c4)", 6)}{move(door, [(0, 0), (t0, 0), (pay_end, 1), (1, 1)], D)}</g>')
        loops.append(f'<g>{_n01_on(pay_end)}<g transform="translate({x} {b:.1f})">{glow(0, -40, 110, "var(--c4)", .22)}{lit}</g></g>')
        loops.append(f'<g>{_n01_on(rise0, bloom, .005)}{token("var(--c4)", 5)}{move(up, [(0, 0), (rise0, 0), (bloom, 1), (1, 1)], D)}</g>')
        by_ = bus_y(x)
        loops.append(f'<circle cx="{x}" cy="{by_:.1f}" r="6" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
                     f'{beat("r", [(0, 6), (rise0 + .012, 6), (rise0 + .04, 26), (1, 26)])}'
                     f'{beat("opacity", [(0, 0), (rise0 + .012, 0), (rise0 + .015, 1), (rise0 + .04, 0), (1, 0)])}</circle>')
        opp = sl["opportunities"][k]
        s_ = fit(opp, 16, 150, "portada opportunity")
        w_ = bold_width(_(str(opp)), s_, current_factor()) + 44
        h_ = s_ + 20
        chip = (glow(0, 0, 70, "var(--c4)", .18) + card(-w_ / 2, -h_ / 2, w_, h_, "var(--card)", "var(--c4)", h_ / 2, 1.6)
                + spark(-w_ / 2 + 17, 0, .42, "var(--c4)") + T(-w_ / 2 + 30, s_ * .36, opp, s_, "var(--white)", W6))
        loops.append(f'<g>{_n01_on(bloom, 1, .02)}<g transform="translate({x} {ny[k]})"><g>{_n01_tr([(0, "0 10"), (bloom, "0 10"), (bloom + .02, "0 0"), (1, "0 0")])}{chip}</g></g></g>')
        if k:
            joins.append(f'<g>{_n01_on(bloom)}<path d="M{xs[k - 1]} {ny[k - 1]} L{x} {ny[k]}" stroke="var(--c4)" stroke-width="1.6" opacity=".8"/></g>')
        loops.append(f'<g>{_n01_on(back0, done, .005)}{token(ok, 5)}{move(down, [(0, 0), (back0, 0), (done, 1), (1, 1)], D)}</g>')
        w0 = (88, 112, 132, 152)[k] / 2
        loops.append(f'<g>{_n01_on(done)}<circle cx="{x + w0 - 4}" cy="{tops[k] + 6:.1f}" r="11" fill="{ok}"/>' + check(x + w0 - 4, tops[k] + 6.5, .55, "var(--ink)") + '</g>')
    return "".join(g) + "".join(joins) + "".join(loops), D, FREEZE  # the lit links under the chips


def _pn02_twin(sl, ctx):
    """n02 on the 900x1600 stage (after energía's _p02_afuera): the three sources and our notebook side by side on top,
    the hypothesis across the zone, their four teams as a ghost at the bottom with a question over each. Same loop and
    frozen frame; labels painted after all the art."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    X1 = zx + zw
    art, text = [glow(zx + zw / 2, zy + 360, 470, "var(--brand)", .55)], []
    sw, shh = 440, 74
    sy = [zy + 14 + k * 90 for k in range(3)]
    bx, by, bw, bh = zx + sw + 36, zy + 8, X1 - zx - sw - 36, 270
    ny = lambda k: by + 70 + k * 64
    pth = lambda k, y: f"M{zx + sw} {y + shh / 2:.0f} C{zx + sw + 20} {y + shh / 2:.0f} {bx - 20} {ny(k)} {bx} {ny(k)}"
    for k, (y, lab) in enumerate(zip(sy, sl["layers"])):
        at = .1 + .12 * k
        art.append(land(card(zx, y, sw, shh, "var(--card)", "var(--c2)", 14, 1.4) + f'<g transform="translate({zx + 34} {y + shh / 2:.0f}) scale(1.3)">{_n01_source(k)}</g>', at, .45, 14))
        text.append(land(T(zx + 68, f"{y + shh / 2 + 8:.0f}", lab, fit(lab, 22, sw - 84, "afuera source", floor=20), "var(--white)", W6), at, .45, 14))
    rings = "".join(f'<circle cx="{bx + 20}" cy="{by + 30 + k * 40}" r="6.5" fill="none" stroke="var(--c2)" stroke-width="2"/>' for k in range(6))
    art.append(land("".join(f'<path d="{pth(k, y)}" fill="none" stroke="var(--c2)" stroke-width="1.8" opacity=".6"/>' for k, y in enumerate(sy))
                    + card(bx, by, bw, bh, "var(--card)", "var(--c2)", 16, 2) + rings, .35, .5))
    text.append(land(T(bx + 44, by + 42, sl["book"], fit(sl["book"], 22, bw - 70, "afuera notebook", floor=20), "var(--white)", W6), .35, .5))
    # the loop: the lens reads each source, a particle drops into the notebook and fills a paragraph
    for k, (y, t) in enumerate(zip(sy, (.04, .13, .22))):
        para = "".join(f'<rect x="{bx + 44}" y="{ny(k) + j * 18 - 8}" width="{(bw - 70) * (.9 if j == 0 else .6):.0f}" height="8" rx="4" fill="var(--c2)" opacity=".6"/>' for j in range(2))
        art.append(f'<g>{_n01_on(t)}<rect x="{zx - 1}" y="{y - 1}" width="{sw + 2}" height="{shh + 2}" rx="15" fill="none" stroke="var(--c4)" stroke-width="2.4"/></g>'
                   f'<g>{_n01_on(t + .03, t + .07, .01)}{token("var(--c4)", 6)}{move(pth(k, y), [(0, 0), (t + .03, 0), (t + .07, 1), (1, 1)], D)}</g>'
                   f'<g>{_n01_on(t + .07)}{para}</g>')
    lx = zx + sw - 40
    st = [f"{lx} {y + 37}" for y in sy]
    stops = [(0, st[0]), (.06, st[0]), (.11, st[1]), (.15, st[1]), (.20, st[2]), (.25, st[2]),
             (.31, f"{bx + bw - 50} {by + bh - 50}"), (.97, f"{bx + bw - 50} {by + bh - 50}"), (1, st[0])]
    art.append(land(f'<g>{_n01_tr(stops)}{_n01_lens(24)}</g>', .6, .4, 0))
    art.append(f'<g>{_n01_on(.31)}<g>{loop("opacity", ".4;1;.4", 2.2)}{spark(bx + bw - 30, by + 34, .75, "var(--c4)")}</g></g>')
    # the hypothesis comes out of the notebook
    hy, hh = by + bh + 36, 118
    hyp = (card(zx, hy, zw, hh, "var(--card)", "var(--c4)", 18, 2.2) + T(zx + 26, hy + 40, sl["case_label"], 20, "var(--c4)", W6)
           + _p01_text2(zx + 26, hy + 80, sl["case"], 24, zw - 52))
    tag = f'<g>{_n01_on(.47)}<g>{loop("opacity", ".8;1;.8", 2.6)}' + pill(X1 - 120, hy, sl["tag"], "var(--c4)", ctx, 20, 220, "afuera tag") + '</g></g>'
    text.append(f'<g>{_n01_on(.38, 1, .04)}<g>{_n01_tr([(0, "0 -110"), (.38, "0 -110"), (.44, "0 0"), (1, "0 0")])}{hyp}</g></g>' + tag)
    # the inside: theirs. Their four teams as a ghost behind a dashed line
    iy, ih = hy + hh + 50, 370
    gy = iy + 200
    gx = [zx + 100 + k * (zw - 200) / 3 for k in range(4)]
    inside = (card(zx, iy, zw, ih, "var(--dim)", "var(--c2)", 22, 1.8, 'fill-opacity=".45" stroke-dasharray="8 8"')
              + f'<path d="M{zx + 20} {gy} H{X1 - 20}" stroke="var(--c2)" stroke-width="1.8" stroke-dasharray="4 8" opacity=".45"/>')
    for k, x in enumerate(gx):
        inside += (f'<rect x="{x - 46:.0f}" y="{gy - 46}" width="92" height="92" rx="20" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="5 5" opacity=".75"/>'
                   f'<g transform="translate({x:.0f} {gy}) scale(1.3)" opacity=".5">{_q01_team(k)}</g>')
    art.append(land(inside, .5, .55, 16))
    text.append(land(T(zx + 26, iy + ih - 28, sl["inside"], fit(sl["inside"], 22, zw / 2 - 20, "afuera inside", floor=20), "var(--white)", W6), .5, .55, 16))
    ask = sl["ask"]
    text.append(f'<g>{_n01_on(.74)}' + T(X1 - 26, iy + ih - 28, ask, fit(ask, 22, zw / 2 - 40, "afuera ask", floor=20), "var(--c4)", 'text-anchor="end" font-weight="600"') + '</g>')
    qy = iy + 86
    for k, x in enumerate(gx):
        a = .54 + k * .05
        q = (f'<path d="M{x:.0f} {qy + 28} V{gy - 48}" stroke="var(--c4)" stroke-width="1.8" stroke-dasharray="3 4"/>'
             f'<circle cx="{x:.0f}" cy="{qy}" r="26" fill="var(--card)" stroke="var(--c4)" stroke-width="2.2">{loop("stroke-opacity", ".4;1;.4", 2.4, k * .5)}</circle>'
             + TC(f"{x:.0f}", qy + 9, "?", 26, "var(--c4)", W6))
        art.append(f'<g>{_n01_on(a + .04)}<path d="M{zx + zw / 2:.0f} {hy + hh} L{x:.0f} {qy - 26}" stroke="var(--c4)" stroke-width="1.4" stroke-dasharray="3 6" opacity=".45"/></g>')
        text.append(f'<g>{_n01_on(a, 1, .015)}<g>{_n01_tr([(0, f"{zx + zw / 2 - x:.0f} -150"), (a, f"{zx + zw / 2 - x:.0f} -150"), (a + .05, "0 0"), (1, "0 0")])}{q}</g></g>')
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- slide 2: from outside
@register("scene", "n02_afuera")
def sc_n02_afuera(sl, ctx):
    """energía's m02_afuera with their four teams inside. Outside, three public sources; a lens reads each one and it
    drops into our notebook, which fills. A hypothesis comes out, marked «por validar». Below the dashed line is the
    inside: their four teams (product, commercial, risk, merchant support) as a ghost we cannot see. The hypothesis
    sends a question to each team: the inside is theirs to tell. Frozen frame: sources read, notebook full, the
    hypothesis waiting to be validated, a question over every team."""
    if ORIENT() == "portrait":
        return _pn02_twin(sl, ctx)
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
    for k, (y, t) in enumerate(zip(sy, (.04, .13, .22))):
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
    # the inside: theirs. Their four teams as a ghost behind a dashed line
    iy = 500
    inside = (card(850, iy, 680, 300, "var(--dim)", "var(--c2)", 20, 1.5, 'fill-opacity=".45" stroke-dasharray="8 8"')
              + f'<path d="M866 670 H1514" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="4 8" opacity=".45"/>')
    gx = [935, 1105, 1275, 1445]
    for k, x in enumerate(gx):
        inside += (f'<rect x="{x - 36}" y="634" width="72" height="72" rx="16" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="5 5" opacity=".75"/>'
                   f'<g transform="translate({x} 670)" opacity=".5">{_q01_team(k)}</g>')
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


def _pn03_twin(sl, ctx):
    """n03 on the 900x1600 stage, read top to bottom: the new rule, what the company knows (governed) taking it in,
    the four team lanes in a column each getting its own answer, and the time line at the bottom where «now» walks and
    every decision lands before the rule comes into force. Same loop and frozen frame; labels painted after all the art."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    X1 = zx + zw
    art, text = [glow(zx + zw / 2, zy + 420, 470, "var(--brand)", .55)], []
    # the event: a new rule
    ey, eh = zy + 8, 80
    art.append(land(card(zx, ey, zw, eh, "var(--card)", "var(--c2)", 18, 1.8) + f'<g transform="translate({zx + 42} {ey + eh / 2}) scale(1.3)">{_q01_rule()}</g>', .1, .5, 12))
    text.append(land(T(zx + 84, ey + eh / 2 + 8, sl["event"], fit(sl["event"], 24, zw - 250, "respuesta event", floor=20), "var(--white)", W6), .1, .5, 12))
    art.append(f'<g>{_n01_on(.03, .1)}<rect x="{zx - 2}" y="{ey - 2}" width="{zw + 4}" height="{eh + 4}" rx="19" fill="none" stroke="var(--c4)" stroke-width="2.4">{loop("stroke-opacity", ".3;1;.3", 1)}</rect></g>')
    text.append(f'<g>{_n01_on(.03)}' + pill(X1 - 80, ey + eh / 2, sl["new"], "var(--c5)", ctx, 20, 150, "respuesta new", 16) + '</g>')
    # what the company knows: governed, one empty slot for what arrives
    ky, kh = ey + eh + 26, 150
    sx, sw_ = zx + 400, zw - 420                    # the slot and the knowledge rows, on the right of the card
    slot_y = ky + 40
    art.append(land(card(zx, ky, zw, kh, "var(--card)", "var(--c2)", 18, 1.8)
                    + f'<g transform="translate({zx + 36} {ky + kh - 32}) scale(.8)">{_q01_team(2, "var(--c4)")}</g>'
                    + f'<rect x="{sx}" y="{ky + 16}" width="{sw_}" height="48" rx="12" fill="none" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="4 5" opacity=".7"/>'
                    + "".join(_q01_page(sx + 14, ky + 92 + j * 36) for j in range(2)), .25, .5, 12))
    text.append(land(T(zx + 24, ky + 48, sl["center"], fit(sl["center"], 24, 360, "respuesta center", floor=20), "var(--white)", W6)
                     + T(zx + 62, ky + kh - 24, sl["governed"], fit(sl["governed"], 22, 320, "respuesta governed", floor=20), "var(--c4)", W6), .25, .5, 12))
    drop = f"M{zx + 42} {ey + eh / 2 + 26} C{zx + 42} {ey + eh + 20} {sx + 30} {slot_y - 50} {sx + 30} {slot_y - 6}"
    art.append(f'<g>{_n01_on(.06, .11, .005)}{token("var(--c4)", 7)}{move(drop, [(0, 0), (.06, 0), (.11, 1), (1, 1)], D)}</g>')
    art.append(f'<g>{_n01_on(.11)}<rect x="{sx}" y="{ky + 16}" width="{sw_}" height="48" rx="12" fill="var(--c4)" fill-opacity=".1" stroke="var(--c4)" stroke-width="1.8"/>'
               + _q01_page(sx + 14, slot_y, "var(--c4)", ".85")
               + f'<circle cx="{X1 - 50}" cy="{slot_y}" r="12" fill="{ok}"/>' + check(X1 - 50, slot_y + .5, .6, "var(--ink)") + '</g>')
    # the four team lanes, in a column, each its own space (risk is restricted); a spine feeds them from the card
    lx, lw, lh, gap = zx + 36, zw - 36, 92, 10
    lys = [ky + kh + 24 + k * (lh + gap) for k in range(4)]
    spine = lambda y: f"M{zx + 14} {ky + kh} V{y + lh / 2 - 14} Q{zx + 14} {y + lh / 2} {zx + 28} {y + lh / 2} H{lx}"
    art.append(land("".join(f'<path d="{spine(y)}" fill="none" stroke="var(--c2)" stroke-width="1.6" opacity=".5"/>' for y in lys), .5, .5, 0))
    lanes, names = [], []
    for k, (y, name) in enumerate(zip(lys, sl["teams"])):
        c = (card(lx, y, lw, lh, "var(--card)", "var(--c2)", 18, 1.4)
             + f'<rect x="{lx + 16}" y="{y + 18}" width="56" height="56" rx="14" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.4"/>'
             + f'<g transform="translate({lx + 44} {y + 46})">{_q01_team(k)}</g>')
        if k == 2:
            c += _lock(lx + lw - 30, y + 26)
        lanes.append(c)
        names.append(T(lx + 90, y + 38, name, fit(name, 22, lw - 150, "respuesta team", floor=20), "var(--white)", W6))
    art.append(seq(lanes, .35, .5, 14))
    text.append(seq(names, .35, .5, 14))
    answered = []
    for k, (y, q, a) in enumerate(zip(lys, sl["questions"], sl["answers"])):
        t = .15 + k * .11
        hit, swap = t + .04, t + .05
        art.append(f'<g>{_n01_on(t, hit, .005)}{token("var(--c4)", 7)}{move(spine(y), [(0, 0), (t, 0), (hit, 1), (1, 1)], D)}</g>'
                   f'<rect x="{lx}" y="{y}" width="{lw}" height="{lh}" rx="18" fill="var(--c4)" opacity="0">'
                   f'{beat("opacity", [(0, 0), (hit, 0), (hit + .01, .14), (hit + .07, 0), (1, 0)])}</rect>')
        text.append(f'<g>{beat("opacity", [(0, 1), (swap, 1), (swap + .01, 0), (.97, 0), (1, 1)])}'
                    + T(lx + 90, y + 72, q, fit(q, 21, lw - 110, "respuesta question", floor=20), "var(--muted)", W6) + '</g>'
                    f'<g>{_n01_on(swap)}<circle cx="{lx + 101}" cy="{y + 65}" r="11" fill="{ok}"/>' + check(lx + 101, y + 65.5, .55, "var(--ink)")
                    + T(lx + 122, y + 72, a, fit(a, 21, lw - 140, "respuesta answer", floor=20), ok, W6)
                    + f'<rect x="{lx}" y="{y}" width="{lw}" height="{lh}" rx="18" fill="none" stroke="{ok}" stroke-width="1.8"/></g>')
        answered.append(swap)
    # the time: the rule arrives on the left, comes into force on the right; «now» walks, decisions land well before
    ax0, ax1, ay = zx + 30, X1 - 40, lys[-1] + lh + 84
    t0, t1 = .04, .80
    xnow = ax0 + .73 * (ax1 - ax0)
    xt = lambda t: ax0 + (t - t0) / (t1 - t0) * (xnow - ax0)
    art.append(land(f'<path d="M{ax0} {ay} H{ax1}" stroke="var(--line)" stroke-width="7" stroke-linecap="round"/>'
                    f'<path d="M{ax0} {ay} H{ax1}" stroke="var(--c2)" stroke-width="1.4" opacity=".6"/>'
                    f'<circle cx="{ax0}" cy="{ay}" r="7" fill="var(--c4)"/>'
                    f'<path d="M{ax1} {ay + 10} V{ay - 32} M{ax1} {ay - 32} H{ax1 + 24} L{ax1 + 16} {ay - 23} L{ax1 + 24} {ay - 14} H{ax1}" {_q01_sw("var(--c5)", 2)}/>', .6, .5, 10))
    text.append(land(T(ax0 - 10, ay + 36, sl["start"], fit(sl["start"], 21, 300, "respuesta start", floor=20), "var(--muted)", W6)
                     + T(ax1 + 24, ay + 36, sl["due"], fit(sl["due"], 21, 300, "respuesta due", floor=20), "var(--muted)", 'text-anchor="end" font-weight="600"'), .6, .5, 10))
    art.append(f'<g>{_n01_on(t1)}<path d="M{xnow + 14:.0f} {ay} H{ax1 - 12}" stroke="{ok}" stroke-width="3" stroke-dasharray="2 6" stroke-linecap="round"/></g>')
    for k, s in enumerate(answered):
        x = f"{xt(s):.0f}"
        art.append(f'<g>{_n01_on(s)}<g transform="translate({x} {ay - 26}) scale(.6)">{_q01_team(k, ok, 2.6)}</g><circle cx="{x}" cy="{ay}" r="8" fill="{ok}"/></g>')
    now = f'<path d="M0 -40 V16" stroke="var(--c4)" stroke-width="1.8"/><circle r="9" fill="var(--c4)"/>' + TC(0, -48, sl["now"], 20, "var(--c4)", W6)
    text.append(land(f'<g transform="translate({ax0} {ay})"><g>{_n01_tr([(0, "0 0"), (t0, "0 0"), (t1, f"{xnow - ax0:.0f} 0"), (.97, f"{xnow - ax0:.0f} 0"), (1, "0 0")])}{now}</g></g>', .8, .4, 0))
    text.append(f'<g>{_n01_on(.64)}' + pill(zx + zw / 2, ay + 88, sl["done"], ok, ctx, 22, 420, "respuesta done", 18) + '</g>')
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- slide 3: the mechanism, one case
@register("scene", "n03_respuesta")
def sc_n03_respuesta(sl, ctx):
    """One case, read top to bottom. A new rule arrives (the card on top) and drops into what the company already
    knows, which is governed and takes it in. From there, each team's lane (the same four teams slide 2 could not see)
    gets its own answer in turn: its question turns into a decision with a check. Below, the time: the rule arrives at
    the left, comes into force at the right; «now» walks toward it and each decision lands on the line well before.
    Frozen frame: four answers, four decisions on the line, «now» still short of the date: every team, in time."""
    if ORIENT() == "portrait":
        return _pn03_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    g = [glow(1190, 440, 470, "var(--brand)", .55)]
    # the event: a new rule
    ey, eh = 100, 72
    ev = (card(850, ey, 680, eh, "var(--card)", "var(--c2)", 16, 1.5) + f'<g transform="translate(886 {ey + eh / 2})">{_q01_rule()}</g>'
          + T(918, ey + eh / 2 + 7, sl["event"], fit(sl["event"], 19, 440, "respuesta event"), "var(--white)", W6))
    g.append(land(ev, .1, .5, 12))
    g.append(f'<g>{_n01_on(.03, .1)}<rect x="848" y="{ey - 2}" width="684" height="{eh + 4}" rx="17" fill="none" stroke="var(--c4)" stroke-width="2">{loop("stroke-opacity", ".3;1;.3", 1)}</rect></g>')
    g.append(f'<g>{_n01_on(.03)}' + pill(1466, ey + eh / 2, sl["new"], "var(--c5)", ctx, 15, 160, "respuesta new", 14) + '</g>')
    # what the company knows: governed, one empty slot for what arrives
    kx, ky, kw, kh = 850, 196, 164, 420
    core = (card(kx, ky, kw, kh, "var(--card)", "var(--c2)", 16, 1.5)
            + TCW(kx + 18, ky + 34, sl["center"], 14, 17, "var(--white)", W6, 1.2, "start")
            + f'<g transform="translate({kx + 28} {ky + kh - 30}) scale(.62)">{_q01_team(2, "var(--c4)")}</g>'
            + T(kx + 46, ky + kh - 24, sl["governed"], fit(sl["governed"], 15, kw - 60, "respuesta governed"), "var(--c4)", W6)
            + f'<rect x="{kx + 12}" y="{ky + 76}" width="{kw - 24}" height="44" rx="10" fill="none" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="4 5" opacity=".7"/>'
            + "".join(_q01_page(kx + 24, ky + 156 + j * 52) for j in range(4)))
    g.append(land(core, .25, .5, 12))
    slot_y = ky + 98
    drop = f"M886 {ey + eh / 2 + 22} C886 {ey + eh + 30} {kx + 38} {slot_y - 50} {kx + 38} {slot_y - 4}"
    g.append(f'<g>{_n01_on(.06, .11, .005)}{token("var(--c4)", 6)}{move(drop, [(0, 0), (.06, 0), (.11, 1), (1, 1)], D)}</g>')
    g.append(f'<g>{_n01_on(.11)}<rect x="{kx + 12}" y="{ky + 76}" width="{kw - 24}" height="44" rx="10" fill="var(--c4)" fill-opacity=".1" stroke="var(--c4)" stroke-width="1.6"/>'
             + _q01_page(kx + 24, slot_y, "var(--c4)", ".85")
             + f'<circle cx="{kx + kw - 26}" cy="{slot_y - 10}" r="9" fill="{ok}"/>' + check(kx + kw - 26, slot_y - 9.5, .45, "var(--ink)") + '</g>')
    # the four team lanes, each its own space (risk is restricted)
    lx, lw, lh, gap = 1060, 470, 96, 12
    lys = [ky + k * (lh + gap) for k in range(4)]
    lanes, fans = [], []
    for k, (y, name) in enumerate(zip(lys, sl["teams"])):
        c = (card(lx, y, lw, lh, "var(--card)", "var(--c2)", 16, 1.3)
             + f'<rect x="{lx + 16}" y="{y + 24}" width="48" height="48" rx="12" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.2"/>'
             + f'<g transform="translate({lx + 40} {y + 48}) scale(.8)">{_q01_team(k)}</g>'
             + T(lx + 82, y + 42, name, fit(name, 18, lw - 130, "respuesta team"), "var(--white)", W6))
        if k == 2:
            c += f'<g transform="translate(0 0)">{_lock(lx + lw - 26, y + 26)}</g>'
        lanes.append(c)
        yc = y + lh / 2
        fans.append((f"M{kx + kw} {slot_y} C{kx + kw + 30} {slot_y} {lx - 30} {yc} {lx} {yc}", y))
    g.append(land("".join(f'<path d="{p}" fill="none" stroke="var(--c2)" stroke-width="1.4" opacity=".5"/>' for p, _y in fans), .5, .5, 0))
    g.append(seq(lanes, .35, .5, 14))
    answered = []
    for k, ((p, y), q, a) in enumerate(zip(fans, sl["questions"], sl["answers"])):
        t = .15 + k * .11
        hit, swap = t + .04, t + .05
        g.append(f'<g>{_n01_on(t, hit, .005)}{token("var(--c4)", 6)}{move(p, [(0, 0), (t, 0), (hit, 1), (1, 1)], D)}</g>')
        g.append(f'<g>{beat("opacity", [(0, 1), (swap, 1), (swap + .01, 0), (.97, 0), (1, 1)])}'
                 + T(lx + 82, y + 72, q, fit(q, 15, lw - 110, "respuesta question"), "var(--muted)", W6) + '</g>')
        g.append(f'<g>{_n01_on(swap)}<circle cx="{lx + 91}" cy="{y + 67}" r="9" fill="{ok}"/>' + check(lx + 91, y + 67.5, .45, "var(--ink)")
                 + T(lx + 108, y + 72, a, fit(a, 15, lw - 136, "respuesta answer"), ok, W6)
                 + f'<rect x="{lx}" y="{y}" width="{lw}" height="{lh}" rx="16" fill="none" stroke="{ok}" stroke-width="1.6"/></g>')
        g.append(f'<rect x="{lx}" y="{y}" width="{lw}" height="{lh}" rx="16" fill="var(--c4)" opacity="0">'
                 f'{beat("opacity", [(0, 0), (hit, 0), (hit + .01, .14), (hit + .07, 0), (1, 0)])}</rect>')
        answered.append(swap)
    # the time: the rule arrives on the left, comes into force on the right; «now» walks, decisions land well before
    ax0, ax1, ay = 870, 1500, 690
    t0, t1, xnow = .04, .80, 1330
    xt = lambda t: ax0 + (t - t0) / (t1 - t0) * (xnow - ax0)
    axis = (f'<path d="M{ax0} {ay} H{ax1}" stroke="var(--line)" stroke-width="6" stroke-linecap="round"/>'
            f'<path d="M{ax0} {ay} H{ax1}" stroke="var(--c2)" stroke-width="1.2" opacity=".6"/>'
            f'<circle cx="{ax0}" cy="{ay}" r="6" fill="var(--c4)"/>'
            f'<path d="M{ax1} {ay + 10} V{ay - 30} M{ax1} {ay - 30} H{ax1 + 22} L{ax1 + 15} {ay - 22} L{ax1 + 22} {ay - 14} H{ax1}" {_q01_sw("var(--c5)", 1.8)}/>'
            + T(ax0, ay + 36, sl["start"], fit(sl["start"], 15, 220, "respuesta start"), "var(--muted)", W6)
            + T(ax1 + 22, ay + 36, sl["due"], fit(sl["due"], 15, 220, "respuesta due"), "var(--muted)", 'text-anchor="end" font-weight="600"'))
    g.append(land(axis, .6, .5, 10))
    g.append(f'<g>{_n01_on(t1)}<path d="M{xnow + 14} {ay} H{ax1 - 12}" stroke="{ok}" stroke-width="2.5" stroke-dasharray="2 6" stroke-linecap="round"/></g>')
    for k, s in enumerate(answered):
        g.append(f'<g>{_n01_on(s)}<g transform="translate({xt(s):.1f} {ay - 26}) scale(.6)">{_q01_team(k, ok, 2.6)}</g><circle cx="{xt(s):.1f}" cy="{ay}" r="7" fill="{ok}"/><circle cx="{xt(s):.1f}" cy="{ay}" r="7" fill="none" stroke="{ok}" stroke-width="1.5">'
                 f'{beat("r", [(0, 7), (s, 7), (s + .04, 20), (1, 20)])}{beat("opacity", [(0, 0), (s, 0), (s + .005, 1), (s + .04, 0), (1, 0)])}</circle></g>')
    now = (f'<path d="M0 -38 V16" stroke="var(--c4)" stroke-width="1.6"/><circle r="8" fill="var(--c4)"/>'
           + TC(0, -46, sl["now"], 15, "var(--c4)", W6))
    g.append(land(f'<g transform="translate({ax0} {ay})"><g>{_n01_tr([(0, "0 0"), (t0, "0 0"), (t1, f"{xnow - ax0} 0"), (.97, f"{xnow - ax0} 0"), (1, "0 0")])}{now}</g></g>', .8, .4, 0))
    g.append(f'<g>{_n01_on(.64)}' + pill(1190, ay + 58, sl["done"], ok, ctx, 16, 320, "respuesta done", 16) + '</g>')
    return "".join(g), D, FREEZE

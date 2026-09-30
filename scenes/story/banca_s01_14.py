"""The banca deck, slides 1, 6, 7 and 14 (portada, sector, hipotesis, cierre). Each scene is one 12-second story timed with beat(); the
reduced-motion frame (0.9 of the loop, 10.8 s) is its resolved state. Runs in the shared namespace of module/ext.py and
reuses the harvested helpers _q01_sw (pagos), _n13_on/_n13_off/_n13_lit/_n13_ride/_n14_man (energía), _b04_win/_b04_trip/
_b04_ping/_b04_draw/_b04_clock and _b14_ok_dot/_b14_ping/_b14_icon (salud).

- k01_portada: a faceless person, seen from behind, uses the bank's app; four everyday actions light up in turn, each
  gets its answer and lights a dream over the city (a house, a shop, a car, a graduation cap).
- k06_sector: the figure stays still beside five equal position slots with the bank in fifth place; new operations flow into
  the bank and, on the branch that meets the client's data, growth without more cost lights; the manual branch stays dim.
- k07_hipotesis: b07_hipotesis with a banking card 3 (pre-approved offer, consent toggle, offer lands).
- k14_cierre: tomorrow's operations center: two queries answer themselves from governed knowledge, the sensitive one goes
  to a person with its context; the AI prepares the answer, the team approves it and the client sees it in the app.
"""


# ---------------------------------------------------------------- 1 · portada: dreams, at the speed of the client
def _k01_dream(k, col):
    """A dream drawn around 0,0 in ~28 px: 0 a house, 1 a shop, 2 a car, 3 a graduation cap."""
    sw = _q01_sw(col, 1.8)
    if k == 0:
        return f'<path d="M-12 11 V-2 L0 -12 L12 -2 V11 Z" {sw}/><path d="M-4 11 V3 H4 V11" {sw}/>'
    if k == 1:
        return (f'<path d="M-13 -4 L-10 -11 H10 L13 -4 Z" {sw}/>'
                f'<path d="M-13 -4 C-13 0 -6.5 0 -6.5 -4 C-6.5 0 0 0 0 -4 C0 0 6.5 0 6.5 -4 C6.5 0 13 0 13 -4" {sw}/>'
                f'<path d="M-11 0 V11 H11 V0 M-3 11 V4 H3 V11" {sw}/>')
    if k == 2:
        return (f'<path d="M-15 5 V-1 L-11 -3 L-7 -10 H7 L11 -3 L15 -1 V5 Z" {sw}/>'
                f'<circle cx="-8" cy="6" r="3.4" {sw}/><circle cx="8" cy="6" r="3.4" {sw}/>')
    return (f'<path d="M-16 -3 L0 -10 L16 -3 L0 4 Z" {sw}/><path d="M-9 1 V7 C-9 12 9 12 9 7 V1" {sw}/>'
            f'<path d="M16 -3 V7" {sw}/>')


def _k01_act(k, col):
    """The action on the app row, around 0,0 in ~22 px: 0 pay (send between phones), 1 open an account (a card),
    2 exchange dollars, 3 ask for a loan (a document and a coin)."""
    sw = _q01_sw(col, 1.7)
    if k == 0:
        return f'<path d="M-10 -4 H9 L5 -8 M10 4 H-9 L-5 8" {sw}/>'
    if k == 1:
        return f'<rect x="-11" y="-7.5" width="22" height="15" rx="2.5" {sw}/><path d="M-11 -2.5 H11 M-7 3 H-2" {sw}/>'
    if k == 2:
        return f'<path d="M5 -6 C3 -8.5 -6 -8.5 -6 -3.5 C-6 1 6 -1 6 3.5 C6 8.5 -3 8.5 -6 6 M0 -11 V11" {sw}/>'
    return (f'<path d="M-10 -11 H2 L6 -7 V9 H-10 Z M-6 -4 H2 M-6 1 H0" {sw}/>'
            f'<circle cx="7" cy="7" r="5.5" fill="var(--card)" stroke="{col}" stroke-width="1.7"/>')


def _k01_person():
    """Faceless, seen from behind over the shoulder, holding the phone out to the right; the frame crops the torso."""
    skin, jacket = shade(SKIN_BROWN, 20), shade("var(--c1)", 40)
    rim = 'fill="none" stroke="var(--c2)" stroke-width="1.4" opacity=".7"'
    torso = "M836 830 C832 768 852 726 900 710 C928 701 950 698 972 698 C996 698 1020 702 1046 712 C1082 726 1100 768 1102 830 Z"
    return (f'<path d="{torso}" fill="{jacket}"/><path d="{torso}" {rim}/>'
            f'<path d="M836 830 C832 768 852 726 900 710 C906 708 912 707 918 706 C890 734 880 780 882 830 Z" fill="{shade(jacket, 18)}"/>'
            f'<path d="M952 652 H990 V704 H952 Z" fill="{shade(skin, 16)}"/>'
            f'<ellipse cx="920" cy="622" rx="7" ry="12" fill="{shade(skin, 14)}"/><ellipse cx="1022" cy="622" rx="7" ry="12" fill="{shade(skin, 14)}"/>'
            f'<ellipse cx="971" cy="616" rx="50" ry="58" fill="{skin}"/>'
            f'<path d="M919 620 C914 566 944 548 971 548 C998 548 1028 566 1023 620 C1021 640 1012 652 1000 658 '
            f'C986 663 956 663 942 658 C930 652 921 640 919 620 Z" fill="{HAIR}"/>'
            f'<path d="M921 606 C919 568 946 550 971 550 C996 550 1023 568 1021 606" fill="none" stroke="var(--c2)" stroke-width="1.4" opacity=".45"/>'
            f'<path d="M1044 722 C1076 732 1100 748 1118 770" fill="none" stroke="{jacket}" stroke-width="28" stroke-linecap="round"/>'
            f'<path d="M1050 712 C1080 722 1104 740 1122 760" {rim}/>')


# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
def _pk01_twin(sl, ctx):
    """k01 on the 900x1600 stage: the promise and the four dreams over the city on top, the skyline under them, the phone
    with its four actions below, held by the person seen from behind at the lower left. Same loop and frozen frame."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    xs = [zx + zw * (k + .5) / 4 for k in range(4)]
    pin_y, base = zy + 150, zy + 400
    px, py, pw, ph = zx + 290, zy + 430, zw - 310, 460
    T0 = (.10, .27, .44, .61)
    art = [glow(zx + zw / 2, pin_y + 80, 460, "var(--brand)", .5)]
    lab = sl["region"]
    text = [land(f'<g opacity=".6">{_n13_lit(.78, .6)}' + TC(zx + zw / 2, zy + 44, lab, fit(lab, 26, zw - 40, "portada region", floor=20), "var(--c4)", W6) + '</g>', 1.0, .5, 10)]
    # the skyline, its windows coming on out of step
    widths, heights = (52, 36, 66, 42, 58, 34, 70, 46), (84, 144, 108, 175, 72, 132, 96, 163, 120)
    blds, wins, x, j = [], {}, zx, 0
    while x < zx + zw:
        w, h = widths[j % 8], heights[j % 9]
        w = zx + zw - x if zx + zw - x - w < 24 else w      # the last building takes the sliver left
        blds.append((x, w, h))
        for r in range(1, h // 28):
            for c in range(1, max(2, w // 16)):
                if (r * 3 + c + j) % 4 == 0:              # windows sharing a rhythm share one loop (the 35 KB budget)
                    wins.setdefault(((j + r) % 5, (j + c) % 4), []).append(
                        f'<rect x="{x + c * 14 - 2:.0f}" y="{base - h + r * 26}" width="6" height="8" rx="1"/>')
        x, j = x + w, j + 1
    wins = [f'<g fill="var(--c4)">{loop("opacity", ".15;.8;.8;.15", 3 + p * .6, q * 1.1)}{"".join(v)}</g>' for (p, q), v in sorted(wins.items())]
    sky = "".join(f'<rect x="{bx:.0f}" y="{base - bh}" width="{bw:.0f}" height="{bh}" fill="var(--dim)" stroke="var(--c2)" stroke-width="1" stroke-opacity=".35"/>'
                  for bx, bw, bh in blds)
    sky += f'<path d="M{zx} {base} H{zx + zw}" stroke="var(--c2)" stroke-width="1.4" opacity=".45"/>'
    art.append(land(sky + "".join(wins), .1, .6, 0))
    tops = [base - next(bh for bx, bw, bh in blds if bx <= x0 < bx + bw) for x0 in xs]
    # the four dreams over the city, dim until their answer arrives
    for k, (x0, top) in enumerate(zip(xs, tops)):
        at = T0[k] + .12
        stem = (f'<path d="M{x0:.0f} {pin_y + 48} V{top - 4}" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="2 5" opacity=".5"/>'
                f'<path d="M{x0:.0f} {pin_y + 48} V{top - 4}" stroke="var(--c4)" stroke-width="2" opacity="0">{_n13_on(at)}</path>')
        dim = (f'<circle r="42" fill="var(--card)" stroke="var(--c2)" stroke-width="1.8" stroke-dasharray="5 5"/>'
               f'<g transform="scale(1.4)">{_k01_dream(k, "var(--c2)")}</g>')
        lit = (f'<g opacity="0">{_n13_on(at)}' + glow(0, 0, 100, "var(--c4)", .3)
               + f'<circle r="42" fill="color-mix(in srgb, var(--c4) 16%, var(--card))" stroke="var(--c4)" stroke-width="2.4"/>'
               + f'<g transform="scale(1.4)">{_k01_dream(k, "var(--c4)")}</g>'
               + f'<circle cx="31" cy="-31" r="13" fill="{ok}"/>{check(31, -30, .7, "var(--ink)")}</g>')
        art.append(land(stem, .3, .5, 0) + pop(dim + lit, x0, pin_y, .35 + k * .1, .45)
                   + f'<g opacity="0">{_n13_on(at)}{glow(x0, base - 40, 90, "var(--c4)", .22)}</g>'
                   + _b04_ping(f"{x0:.0f}", pin_y, 42, 84, "var(--c4)", (at,), .08, .8))
    # the phone, the app and its four actions
    phone = (card(px, py, pw, ph, "var(--ink)", "var(--c2)", 34, 1.8)
             + card(px + 10, py + 10, pw - 20, ph - 20, "var(--card)", "var(--line)", 26, 1)
             + f'<rect x="{px + pw / 2 - 24:.0f}" y="{py + 20}" width="48" height="6" rx="3" fill="var(--c2)" opacity=".5"/>'
             + T(px + 28, py + 62, sl["app"], fit(sl["app"], 24, pw - 56, "portada app", floor=20), "var(--white)", W6)
             + f'<rect x="{px + 28}" y="{py + 74}" width="120" height="6" rx="3" fill="var(--c2)" opacity=".35"/>')
    rows, rides = [], []
    for k, (act, ans, t0) in enumerate(zip(sl["actions"], sl["answers"], T0)):
        y, done = py + 92 + k * 90, t0 + .05
        rows.append(f'<g opacity=".5">{_n13_lit(t0, .5)}' + card(px + 18, y, pw - 36, 80, "var(--dim)", "var(--line)", 14, 1.2)
                    + f'<g transform="translate({px + 48} {y + 40}) scale(1.4)">{_k01_act(k, "var(--c2)")}</g>'
                    + T(px + 86, y + 34, act, fit(act, 24, pw - 170, "portada action", floor=20), "var(--white)", W6) + '</g>'
                    + f'<rect x="{px + 18}" y="{y}" width="{pw - 36}" height="80" rx="14" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_n13_on(t0, done)}</rect>'
                    + _b14_ping(px + pw / 2, y + 40, 24, 120, t0)
                    + f'<g opacity="0">{_n13_on(done)}' + T(px + 86, y + 64, ans, fit(ans, 21, pw - 170, "portada answer", floor=20), ok, W6) + '</g>'
                    + _b14_ok_dot(px + pw - 46, y + 40, done, ok, 14))
        rise = (f"M{px + pw - 46} {y + 40} H{zx + zw - 8} V{base - 10} "
                f"C{zx + zw - 8} {base - 120} {xs[k]:.0f} {pin_y + 150} {xs[k]:.0f} {pin_y + 46}")
        rides.append(_n13_ride(rise, done + .01, T0[k] + .12, 7))
    art.append(land(phone + "".join(rows), .45, .55, 24))
    dx, dy = zx + 150 - 971, zy + zh - 830       # the person's desktop drawing, moved to the lower left
    skin = shade(SKIN_BROWN, 20)
    art.append(land(f'<g transform="translate({dx} {dy})">{_k01_person()}</g>', .7, .6, 30))
    art.append(land(f'<g transform="translate({dx} {dy})"><circle cx="1118" cy="772" r="15" fill="{skin}"/>'
                    f'<path d="M1110 758 C1122 754 1130 760 1128 770" fill="none" stroke="{shade(SKIN_BROWN, 34)}" stroke-width="2" stroke-linecap="round"/></g>', .8, .5, 30))
    return portrait_mark("".join(art) + "".join(rides) + "".join(text)), D, FREEZE


@register("scene", "k01_portada")
def sc_k01_portada(sl, ctx):
    """A city at dusk behind a faceless person who uses the bank's app, seen over the shoulder. Above the skyline, four
    dreams wait, dim: a house, a shop, a car, a graduation cap. Loop: each action on the app lights (pay with PLIN, open an
    account, exchange dollars, ask for a loan), gets its answer and a check, and the answer rises to its dream, which
    lights over the city. Frozen frame: four actions answered and four dreams lit."""
    if ORIENT() == "portrait":
        return _pk01_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    xs, pin_y, base = [930, 1110, 1290, 1470], 208, 420
    px, py, pw, ph = 1110, 468, 272, 348
    T0 = (.10, .27, .44, .61)
    g = [glow(1190, 300, 460, "var(--brand)", .5), glow(1190, 420, 320, "var(--c4)", .08)]
    # the region's promise, above the city; it brightens once the four dreams are lit
    lab = sl["region"]
    g.append(land(f'<g opacity=".6">{_n13_lit(.78, .6)}' + TC(1190, 132, lab, fit(lab, 20, 640, "portada region"), "var(--c4)", W6) + '</g>', 1.0, .5, 10))
    # the skyline: buildings on one baseline, their windows coming on out of step
    widths, heights = (44, 30, 58, 36, 50, 28, 62, 40), (70, 120, 90, 146, 60, 110, 80, 136, 100)
    blds, wins, x, j = [], [], 832, 0
    while x < 1552:
        w, h = min(widths[j % 8], 1556 - x), heights[j % 9]
        blds.append((x, w, h))
        for r in range(1, h // 26):
            for c in range(1, max(2, w // 16)):
                if (r * 3 + c + j) % 4 == 0:
                    wins.append(f'<rect x="{x + c * 14 - 2}" y="{base - h + r * 24}" width="5" height="7" rx="1" fill="var(--c4)">'
                                f'{loop("opacity", ".15;.8;.8;.15", 3 + (j + r) % 5 * .6, (j * 1.7 + c) % 4)}</rect>')
        x, j = x + w, j + 1
    sky = "".join(f'<rect x="{bx}" y="{base - bh}" width="{bw}" height="{bh}" fill="var(--dim)" stroke="var(--c2)" stroke-width="1" stroke-opacity=".35"/>'
                  for bx, bw, bh in blds)
    sky += f'<path d="M820 {base} H1560" stroke="var(--c2)" stroke-width="1.4" opacity=".45"/>'
    g.append(land(sky + "".join(wins), .1, .6, 0))
    tops = [base - next(bh for bx, bw, bh in blds if bx <= x0 < bx + bw) for x0 in xs]
    # the four dreams over the city, dim until their answer arrives
    for k, (x0, top) in enumerate(zip(xs, tops)):
        at = T0[k] + .12
        stem = (f'<path d="M{x0} {pin_y + 36} V{top - 4}" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="2 5" opacity=".5"/>'
                f'<path d="M{x0} {pin_y + 36} V{top - 4}" stroke="var(--c4)" stroke-width="1.6" opacity="0">{_n13_on(at)}</path>')
        dim = (f'<circle r="30" fill="var(--card)" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="4 4"/>'
               + _k01_dream(k, "var(--c2)"))
        lit = (f'<g opacity="0">{_n13_on(at)}' + glow(0, 0, 80, "var(--c4)", .3)
               + f'<circle r="30" fill="color-mix(in srgb, var(--c4) 16%, var(--card))" stroke="var(--c4)" stroke-width="2"/>'
               + _k01_dream(k, "var(--c4)")
               + f'<circle cx="22" cy="-22" r="10" fill="{ok}"/>{check(22, -21, .55, "var(--ink)")}</g>')
        g.append(land(stem, .3, .5, 0) + pop(dim + lit, x0, pin_y, .35 + k * .1, .45)
                 + f'<g opacity="0">{_n13_on(at)}{glow(x0, base - 40, 90, "var(--c4)", .22)}</g>'
                 + _b04_ping(x0, pin_y, 30, 64, "var(--c4)", (at,), .08, .8))
    # the phone, the app and its four actions
    phone = (card(px, py, pw, ph, "var(--ink)", "var(--c2)", 30, 1.6)
             + card(px + 8, py + 8, pw - 16, ph - 16, "var(--card)", "var(--line)", 24, 1)
             + f'<rect x="{px + pw / 2 - 20}" y="{py + 18}" width="40" height="5" rx="2.5" fill="var(--c2)" opacity=".5"/>'
             + T(px + 24, py + 56, sl["app"], fit(sl["app"], 17, pw - 48, "portada app"), "var(--white)", W6)
             + f'<rect x="{px + 24}" y="{py + 68}" width="96" height="6" rx="3" fill="var(--c2)" opacity=".35"/>')
    rows, rides = [], []
    for k, (act, ans, t0) in enumerate(zip(sl["actions"], sl["answers"], T0)):
        y, done = py + 90 + k * 62, t0 + .05
        rows.append(f'<g opacity=".5">{_n13_lit(t0, .5)}' + card(px + 16, y, pw - 32, 54, "var(--dim)", "var(--line)", 12, 1.2)
                    + f'<g transform="translate({px + 38} {y + 20})">{_k01_act(k, "var(--c2)")}</g>'
                    + T(px + 60, y + 26, act, fit(act, 16, pw - 120, "portada action"), "var(--white)", W6) + '</g>'
                    + f'<rect x="{px + 16}" y="{y}" width="{pw - 32}" height="54" rx="12" fill="none" stroke="var(--c4)" stroke-width="1.6" opacity="0">{_n13_on(t0, done)}</rect>'
                    + _b14_ping(px + pw / 2, y + 27, 20, 90, t0)
                    + f'<g opacity="0">{_n13_on(done)}' + T(px + 60, y + 46, ans, fit(ans, 15, pw - 120, "portada answer"), ok, W6) + '</g>'
                    + _b14_ok_dot(px + pw - 38, y + 27, done, ok, 11))
        rise = (f"M{px + pw - 38} {y + 27} H{px + pw + 30} V{base + 30} "
                f"C{px + pw + 30} {base - 60} {xs[k]} {pin_y + 110} {xs[k]} {pin_y + 34}")
        rides.append(_n13_ride(rise, done + .01, T0[k] + .12, 6))
    g.append(land(phone + "".join(rows), .45, .55, 24))
    g.append(land(_k01_person(), .7, .6, 30))
    # the hand, over the phone's edge
    g.append(land(f'<circle cx="1118" cy="772" r="15" fill="{shade(SKIN_BROWN, 20)}"/>'
                  f'<path d="M1110 758 C1122 754 1130 760 1128 770" fill="none" stroke="{shade(SKIN_BROWN, 34)}" stroke-width="2" stroke-linecap="round"/>', .8, .5, 30))
    return "".join(g) + "".join(rides), D, FREEZE


# ---------------------------------------------------------------- 6 · sector: fifth bank, and how it grows from here
def _k06_icon(k, col):
    """Thin icons around 0,0: 0 credit (coins), 1 deposit (a piggy slot), 2 factoring (an invoice), 3 trade (a ship)."""
    s = f'fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
    if k == 0:
        return f'<ellipse cx="0" cy="-5" rx="9" ry="3.5" {s}/><path d="M-9 -5 V5 C-9 9 9 9 9 5 V-5 M-9 0 C-9 4 9 4 9 0" {s}/>'
    if k == 1:
        return f'<rect x="-10" y="-4" width="20" height="14" rx="3" {s}/><path d="M-5 -4 V-8 H5 V-4 M-4 3 H4" {s}/><path d="M0 -12 V-9" {s}/>'
    if k == 2:
        return f'<path d="M-8 -11 H4 L8 -7 V11 H-8 Z M-4 -4 H4 M-4 1 H4 M-4 6 H1" {s}/>'
    return f'<path d="M-11 3 H11 L7 10 H-7 Z M-6 3 V-5 H6 V3 M0 -5 V-11 M0 -11 L5 -8" {s}/>'


def _k06_bank(col):
    """The bank building around 0,0 (base at y 70): pediment, four columns, steps."""
    s = f'fill="var(--card)" stroke="{col}" stroke-width="1.8" stroke-linejoin="round"'
    cols = "".join(f'<rect x="{x0}" y="-18" width="14" height="70" rx="2" {s}/>' for x0 in (-52, -23, 9, 38))
    return (f'<path d="M-68 -24 L0 -64 L68 -24 Z" {s}/><rect x="-66" y="-26" width="132" height="10" rx="2" {s}/>'
            + cols + f'<rect x="-66" y="52" width="132" height="9" rx="2" {s}/><rect x="-74" y="61" width="148" height="9" rx="2" {s}/>')


# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
def _pk06_twin(sl, ctx):
    """k06 on the 900x1600 stage: the framed figure and the five slots side by side on top, the shares under them; below,
    the four operations flow into the bank, the fork climbs to the client's data and drops to growth without more cost,
    the manual branch stays dim at the foot. Same loop and frozen frame; the figure never moves."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    bx, by, bw, bh = zx + 20, zy + 20, 380, 300
    LIGHT = (.12, .22, .32, .42)
    OUT, REC, GO, WIN = (.52, .60), .60, (.64, .70), .70
    art, text = [glow(zx + zw / 2, zy + zh * .5, 440, "var(--brand)", .4)], []
    hud = "".join(f'<path d="M{x0} {y0 + dy * 26} V{y0} H{x0 + dx * 26}" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity=".8"/>'
                  for x0, y0, dx, dy in ((bx, by, 1, 1), (bx + bw, by, -1, 1), (bx, by + bh, 1, -1), (bx + bw, by + bh, -1, -1)))
    fx = bx + bw / 2
    main, _sep, when = sl["label"].partition(" · ")
    fig = TC(fx, by + 140, sl["figure"], fit(sl["figure"], 130, bw - 60, "sector figure"), "var(--c4)", W6)
    lab = (TCW(fx, by + 192, main, _n07_chars(main, 24, bw - 40), 24, "var(--white)", W6, 1.25)
           + (TC(fx, by + 270, when, fit(when, 21, bw - 60, "sector label source", floor=20), "var(--muted)", W6) if when else ""))
    art.append(land(hud, .1, .5, 0))
    text.append(land(fig + lab, .2, .5, 0))
    # the ranking: five equal slots, the bank's the fifth and lit
    rx0, rank = zx + 420, ""
    for k in range(5):
        y, hi = zy + 24 + k * 56, k == 4
        name = sl["door"] if hi else sl["ranking"]
        rank += (T(rx0, y + 30, f"{k + 1}.º", 22, "var(--c4)" if hi else "var(--muted)", W6)
                 + card(rx0 + 50, y, zx + zw - rx0 - 50, 44, "color-mix(in srgb, var(--c4) 22%, var(--card))" if hi else "var(--dim)",
                        "var(--c4)" if hi else "var(--line)", 10, 1.8 if hi else 1.2)
                 + T(rx0 + 66, y + 30, name, fit(name, 21, zx + zw - rx0 - 82, "sector slot", floor=20), "var(--white)" if hi else "var(--muted)", W6))
    chips = "".join(pill(cx, zy + 346, c, "var(--dim)", ctx, 22, 380, "sector share", 16) for cx, c in zip((zx + 210, zx + 610), sl["shares"]))
    text.append(land(rank, .3, .5, 0) + land(chips, .5, .45, 8))
    # the operations, lighting in turn; each flows into the bank
    kx, ky = zx + 410, zy + 650
    for k, (name, t) in enumerate(zip(sl["services"], LIGHT)):
        iy, sx_ = zy + 440 + k * 84, zx + 50
        art.append(land(f'<circle cx="{sx_}" cy="{iy}" r="28" fill="var(--card)" stroke="var(--line)" stroke-width="1.6"/>'
                        f'<g opacity="0">{beat("opacity", _b04_win(t))}<circle cx="{sx_}" cy="{iy}" r="28" fill="color-mix(in srgb, var(--c4) 18%, var(--card))" stroke="var(--c4)" stroke-width="2"/></g>'
                        f'<g transform="translate({sx_} {iy}) scale(1.3)">{_k06_icon(k, "var(--c2)")}</g>'
                        f'<g opacity="0" transform="translate({sx_} {iy}) scale(1.3)">{beat("opacity", _b04_win(t))}{_k06_icon(k, "var(--c4)")}</g>', .4 + k * .12, .4, 10)
                   + _b04_ping(sx_, iy, 28, 56, "var(--c4)", (t,), .08, .7))
        text.append(land(f'<g opacity=".6">{beat("opacity", _b04_win(t, lo=.6))}'
                         + T(sx_ + 42, iy + 8, name, fit(name, 22, 200, "sector operation", floor=20), "var(--white)", W6) + '</g>', .4 + k * .12, .4, 10))
        d = f"M{sx_ + 250} {iy} C{kx - 60} {iy} {kx - 70} {ky} {kx} {ky}"
        a, b = t + .01, t + .08
        art.append(f'<g opacity="0">{beat("opacity", _b04_trip(a, b))}{move(d, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{token("var(--c4)", 6)}</g>')
    bank = (_k06_bank("var(--c2)") + f'<g opacity="0">{beat("opacity", _b04_win(LIGHT[-1] + .08))}{_k06_bank("var(--c4)")}</g>')
    art.append(pop(bank, kx, ky - 30, .35, .45) + _b04_ping(kx, ky - 20, 40, 90, "var(--c4)", [t + .08 for t in LIGHT], .06, .6))
    text.append(land(TC(kx, ky + 76, sl["door"], fit(sl["door"], 24, 170, "sector bank", floor=20), "var(--white)", W6), .5, .4, 8))
    # the fork: up to the client's data, then down to growth without more cost; the manual branch stays dim below
    jx, jy = kx + 76, ky - 10
    cx0, cy0, cw, ch = zx + 550, zy + 440, 230, 116
    ex, ey = cx0 + cw / 2, cy0 + ch + 84
    my = zy + zh - 120                                  # the manual branch
    up = f"M{jx} {jy} C{jx + 40} {jy} {cx0 - 50} {cy0 + ch / 2} {cx0} {cy0 + ch / 2}"
    on = f"M{ex} {cy0 + ch} V{ey - 26}"
    down = f"M{jx} {jy} C{jx + 40} {jy} {jx + 30} {my} {jx + 90} {my} H{ex - 26}"
    rec = (card(cx0, cy0, cw, ch, "var(--card)", "var(--line)", 14, 1.6)
           + f'<g opacity="0">{beat("opacity", _b04_win(REC))}{card(cx0, cy0, cw, ch, "color-mix(in srgb, var(--c4) 10%, var(--card))", "var(--c4)", 14, 2)}</g>')
    for k in range(4):
        yy = cy0 + 18 + k * 22
        rec += (f'<rect x="{cx0 + 18}" y="{yy}" width="{cw - 36}" height="12" rx="6" fill="none" stroke="var(--line)" stroke-width="1" stroke-dasharray="3 4"/>'
                f'<rect x="{cx0 + 18}" y="{yy}" width="{cw - 36}" height="12" rx="6" fill="var(--c4)" opacity="0">{beat("opacity", _b04_win(REC + k * .01, hi=.85))}</rect>')
    dash = 'fill="none" stroke="var(--line)" stroke-width="1.6" stroke-dasharray="3 6"'
    art.append(land(f'<path d="{up}" {dash}/><path d="{on}" {dash}/><path d="{down}" {dash}/>', .9, .4, 0)
               + land(rec, .7, .45, 14)
               + _b04_draw(up, "var(--c4)", OUT[0], OUT[1], 2.4) + _b04_draw(on, ok, GO[0], GO[1], 2.4)
               + f'<g opacity="0">{beat("opacity", _b04_trip(*OUT))}{move(up, [(0, 0), (OUT[0], 0), (OUT[1], 1), (1, 1)], D)}{token("var(--c4)", 7)}</g>'
               + f'<g opacity="0">{beat("opacity", _b04_trip(*GO))}{move(on, [(0, 0), (GO[0], 0), (GO[1], 1), (1, 1)], D)}{token(ok, 7)}</g>'
               + _b04_ping(ex, cy0 + ch / 2, 60, 120, "var(--c4)", (REC,), .1, .6))
    text.append(land(T(cx0, cy0 - 16, sl["record"], fit(sl["record"], 22, zx + zw - cx0, "sector record", floor=20), "var(--white)", W6), .7, .45, 14))
    art.append(land(f'<circle cx="{ex}" cy="{ey}" r="26" fill="var(--card)" stroke="var(--line)" stroke-width="1.6"/>'
                    f'<g opacity="0">{beat("opacity", _b04_win(WIN))}<circle cx="{ex}" cy="{ey}" r="26" fill="color-mix(in srgb, {ok} 22%, var(--card))" stroke="{ok}" stroke-width="2"/>'
                    f'{check(ex, ey + 1, 1.15, ok)}</g>', 1.0, .45, 10)
               + land(f'<g transform="translate({ex} {my})"><circle r="26" fill="var(--dim)" stroke="var(--line)" stroke-width="1.6"/>'
                      f'<g transform="scale(1.3)"><path d="M-8 -9 H5 L9 -5 V9 H-8 Z M-4 -2 H5 M-4 3 H5" fill="none" stroke="var(--muted)" stroke-width="1.6" stroke-linejoin="round"/></g></g>', 1.1, .45, 10)
               + _b04_ping(ex, ey, 26, 60, ok, (WIN,), .1, .7))
    text.append(land(f'<g opacity=".6">{beat("opacity", _b04_win(WIN, lo=.6))}'
                     + TCW(ex, ey + 60, sl["ontime"], _n07_chars(sl["ontime"], 22, 300), 22, "var(--white)", W6, 1.25) + '</g>', 1.0, .45, 10)
                + land(TCW(ex, my + 58, sl["late"], _n07_chars(sl["late"], 21, 300), 21, "var(--muted)", W6, 1.25), 1.1, .45, 10))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "k06_sector")
def sc_k06_sector(sl, ctx):
    """The figure stays still, framed, beside five equal position slots: the bank's, fifth, is the lit one, with its two
    shares as chips. Below, new operations (credit, deposits, factoring, foreign trade) light up in turn and flow into the
    bank; on one branch they meet the client's data and growth without more cost lights; the other branch, growing with
    more manual work, stays drawn and dim. Frozen frame: four operations in, the data met, growth without more cost lit."""
    if ORIENT() == "portrait":
        return _pk06_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    bx, by, bw, bh = 850, 110, 330, 262
    LIGHT = (.12, .22, .32, .42)
    OUT, REC, GO, WIN = (.52, .60), .60, (.64, .70), .70
    g = [glow(1190, 470, 440, "var(--brand)", .4)]
    # the figure, framed and still
    hud = "".join(f'<path d="M{x0} {y0 + dy * 22} V{y0} H{x0 + dx * 22}" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity=".8"/>'
                  for x0, y0, dx, dy in ((bx, by, 1, 1), (bx + bw, by, -1, 1), (bx, by + bh, 1, -1), (bx + bw, by + bh, -1, -1)))
    fx = bx + bw / 2
    main, _sep, when = sl["label"].partition(" · ")
    fig = TC(fx, by + 128, sl["figure"], fit(sl["figure"], 112, bw - 60, "sector figure"), "var(--c4)", W6)
    lab = (TCW(fx, by + 170, main, 22, 19, "var(--white)", W6, 1.25)
           + (TC(fx, by + 234, when, fit(when, 17, bw - 60, "sector label source"), "var(--muted)", W6) if when else ""))
    g.append(land(hud, .1, .5, 0) + land(fig + lab, .2, .5, 0))
    # the ranking: five equal position slots (no lengths, no sizes compared), the bank's the fifth and lit
    rx0, rank = 1214, ""
    for k in range(5):
        y, hi = 116 + k * 44, k == 4
        rank += (T(rx0, y + 20, f"{k + 1}.º", 15, "var(--c4)" if hi else "var(--muted)", W6)
                 + card(rx0 + 36, y, 300, 30, "color-mix(in srgb, var(--c4) 22%, var(--card))" if hi else "var(--dim)",
                        "var(--c4)" if hi else "var(--line)", 8, 1.8 if hi else 1.2)
                 + T(rx0 + 52, y + 20, sl["door"] if hi else sl["ranking"], fit(sl["door"] if hi else sl["ranking"], 15, 268, "sector slot"),
                     "var(--white)" if hi else "var(--muted)", W6))
    chips = "".join(pill(cx, 380, c, "var(--dim)", ctx, 15, 170, "sector share", 14) for cx, c in zip((1282, 1452), sl["shares"]))
    g.append(land(rank, .3, .5, 0) + land(chips, .5, .45, 8))
    # the operations, lighting in turn; each flows into the bank
    kx, ky = 1150, 604                                    # the bank (its door)
    for k, (name, t) in enumerate(zip(sl["services"], LIGHT)):
        iy = 460 + k * 70
        svc = (f'<circle cx="872" cy="{iy}" r="22" fill="var(--card)" stroke="var(--line)" stroke-width="1.5"/>'
               f'<g opacity="0">{beat("opacity", _b04_win(t))}<circle cx="872" cy="{iy}" r="22" fill="color-mix(in srgb, var(--c4) 18%, var(--card))" stroke="var(--c4)" stroke-width="1.8"/></g>'
               f'<g transform="translate(872 {iy})">{_k06_icon(k, "var(--c2)")}</g>'
               f'<g opacity="0" transform="translate(872 {iy})">{beat("opacity", _b04_win(t))}{_k06_icon(k, "var(--c4)")}</g>'
               + f'<g opacity=".6">{beat("opacity", _b04_win(t, lo=.6))}' + T(904, f"{iy + 6:.1f}", name, fit(name, 16, 150, "sector operation"), "var(--white)", W6) + '</g>')
        g.append(land(svc, .4 + k * .12, .4, 10) + _b04_ping(872, iy, 22, 46, "var(--c4)", (t,), .08, .7))
        d = f"M{904 + 150} {iy} C{kx - 60} {iy} {kx - 70} {ky} {kx} {ky}"
        a, b = t + .01, t + .08
        g.append(f'<g opacity="0">{beat("opacity", _b04_trip(a, b))}{move(d, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{token("var(--c4)", 5)}</g>')
    bank = (_k06_bank("var(--c2)") + f'<g opacity="0">{beat("opacity", _b04_win(LIGHT[-1] + .08))}{_k06_bank("var(--c4)")}</g>')
    g.append(pop(bank, kx, ky - 30, .35, .45)
             + land(TC(kx, ky + 70, sl["door"], fit(sl["door"], 18, 150, "sector bank"), "var(--white)", W6), .5, .4, 8)
             + _b04_ping(kx, ky - 20, 40, 90, "var(--c4)", [t + .08 for t in LIGHT], .06, .6))
    # the fork: the client's data, then growth without more cost; the manual branch stays dim
    jx, jy = kx + 76, ky - 10
    cx0, cy0, cw, ch = 1270, 466, 150, 96               # the client's data
    up = f"M{jx} {jy} C{jx + 30} {jy} {cx0 - 40} {cy0 + ch / 2} {cx0} {cy0 + ch / 2}"
    ex, ey = 1486, cy0 + ch / 2
    on = f"M{cx0 + cw} {ey} H{ex - 22}"
    down = f"M{jx} {jy} C{jx + 40} {jy} {jx + 40} 740 {jx + 100} 740 H{ex - 22}"
    rec = (T(cx0, cy0 - 12, sl["record"], fit(sl["record"], 16, 210, "sector record"), "var(--white)", W6)
           + card(cx0, cy0, cw, ch, "var(--card)", "var(--line)", 14, 1.5)
           + f'<g opacity="0">{beat("opacity", _b04_win(REC))}{card(cx0, cy0, cw, ch, "color-mix(in srgb, var(--c4) 10%, var(--card))", "var(--c4)", 14, 1.8)}</g>')
    for k in range(4):
        yy = cy0 + 16 + k * 18
        rec += (f'<rect x="{cx0 + 16}" y="{yy}" width="{cw - 32}" height="10" rx="5" fill="none" stroke="var(--line)" stroke-width="1" stroke-dasharray="3 4"/>'
                f'<rect x="{cx0 + 16}" y="{yy}" width="{cw - 32}" height="10" rx="5" fill="var(--c4)" opacity="0">{beat("opacity", _b04_win(REC + k * .01, hi=.85))}</rect>')
    g.append(land(f'<path d="{up}" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 6"/>'
                  f'<path d="{on}" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 6"/>'
                  f'<path d="{down}" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 6"/>', .9, .4, 0)
             + land(rec, .7, .45, 14)
             + _b04_draw(up, "var(--c4)", OUT[0], OUT[1], 2) + _b04_draw(on, ok, GO[0], GO[1], 2)
             + f'<g opacity="0">{beat("opacity", _b04_trip(*OUT))}{move(up, [(0, 0), (OUT[0], 0), (OUT[1], 1), (1, 1)], D)}{token("var(--c4)", 6)}</g>'
             + f'<g opacity="0">{beat("opacity", _b04_trip(*GO))}{move(on, [(0, 0), (GO[0], 0), (GO[1], 1), (1, 1)], D)}{token(ok, 6)}</g>'
             + _b04_ping(cx0 + cw / 2, cy0 + ch / 2, 50, 100, "var(--c4)", (REC,), .1, .6))
    win = (f'<circle cx="{ex}" cy="{ey}" r="20" fill="var(--card)" stroke="var(--line)" stroke-width="1.5"/>'
           f'<g opacity="0">{beat("opacity", _b04_win(WIN))}<circle cx="{ex}" cy="{ey}" r="20" fill="color-mix(in srgb, {ok} 22%, var(--card))" stroke="{ok}" stroke-width="1.8"/>'
           f'{check(ex, ey + 1, .9, ok)}</g>'
           + f'<g opacity=".6">{beat("opacity", _b04_win(WIN, lo=.6))}'
           + TCW(ex, ey + 50, sl["ontime"], 12, 16, "var(--white)", W6, 1.25) + '</g>')
    manual = (f'<g transform="translate({ex} 740)"><circle r="20" fill="var(--dim)" stroke="var(--line)" stroke-width="1.5"/>'
              f'<path d="M-8 -9 H5 L9 -5 V9 H-8 Z M-4 -2 H5 M-4 3 H5" fill="none" stroke="var(--muted)" stroke-width="1.6" stroke-linejoin="round"/></g>'
              + TCW(ex - 20, 782, sl["late"], 18, 16, "var(--muted)", W6, 1.25))
    g.append(land(win, 1.0, .45, 10) + land(manual, 1.1, .45, 10) + _b04_ping(ex, ey, 20, 50, ok, (WIN,), .1, .7))
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 14 · cierre: tomorrow's operations center
# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
def _pk14_twin(sl, ctx):
    """k14 on the 900x1600 stage: the sign on top, the wall screen full width (the three queries across it, the governed
    knowledge and the three steps side by side under them), the team member with the tablet and the client's phone at
    the console below. Same beats: two answered by themselves, the sensitive one down to the person, approved, the answer
    in the app. Same frozen frame."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    sx, sy, sw, sh = zx, zy + 50, zw, 550
    lx, lw = sx + 16, sw - 32
    cw_ = (lw - 12) / 2
    rx, rw = lx + cw_ + 12, cw_
    gut = lx + cw_ + 6
    sb = sy + sh                                     # the screen's bottom edge
    desk = zy + zh - 30
    ARR = (.05, .19, .33)
    Q = ((.09, .14), (.23, .28))
    SEN, R0, R1 = .36, .38, .44
    P1, TAP, P2, P3, NOTE = .49, .58, .63, .68, .74
    g = [glow(zx + zw / 2, sy + sh / 2, 470, "var(--brand)", .5)]
    # ---- the wall screen
    hud = "".join(f'<path d="M{x0} {y0 + dy * 26} V{y0} H{x0 + dx * 26}" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity=".8" transform="translate({dx * -8} {dy * -8})"/>'
                  for x0, y0, dx, dy in ((sx, sy, 1, 1), (sx + sw, sy, -1, 1), (sx, sb, 1, -1), (sx + sw, sb, -1, -1)))
    hud += (f'<rect x="{sx + 2}" y="{sy + 52}" width="{sw - 4}" height="2" fill="var(--c2)" opacity=".16">'
            f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {sh - 58}" dur="5s" repeatCount="indefinite"/></rect>')
    tk_y = [sy + 94 + 68 * k for k in range(3)]
    low = tk_y[-1] + 74                              # the knowledge (left) and the steps (right)
    screen = (card(sx, sy, sw, sh, "var(--card)", "var(--c2)", 24, 1.4) + hud
              + f'<path d="M{sx} {sy + 50} H{sx + sw}" stroke="var(--line)" stroke-width="1.5"/>'
              + f'<path d="M{gut} {low} V{sb - 16}" stroke="var(--line)" stroke-width="1" opacity=".6"/>'
              + f'<circle cx="{sx + 26}" cy="{sy + 25}" r="8" fill="var(--c5)">{blink(1.4)}</circle>'
              + T(sx + 46, sy + 33, sl["screen"], fit(sl["screen"], 22, 480, "operations screen", floor=20), "var(--white)", W6)
              + pill(sx + sw - 74, sy + 25, sl["live"], ok, ctx, 20, 140, "operations live", 14))
    # ---- the queries across the screen, answered from the governed knowledge
    left = T(lx, sy + 80, sl["queue"], fit(sl["queue"], 20, 420, "operations queue", floor=20), "var(--muted)", W6)
    live = []
    for k, (q, y, a) in enumerate(zip(sl["tickets"], tk_y, ARR)):
        left += f'<rect x="{lx}" y="{y}" width="{lw}" height="60" rx="12" fill="none" stroke="var(--line)" stroke-width="1.2" stroke-dasharray="4 5"/>'
        body = (card(lx, y, lw, 60, "var(--dim)", "var(--line)", 12, 1.2)
                + T(lx + 16, y + 26, q, fit(q, 22, lw - 64, "operations ticket", floor=20), "var(--white)", W6))
        end = Q[k][1] if k < 2 else SEN
        body += f'<g>{_n13_off(end)}' + T(lx + 16, y + 51, sl["new"], 20, "var(--muted)", W6) + '</g>'
        if k < 2:
            body += (f'<g opacity="0">{_n13_on(end)}' + T(lx + 16, y + 51, sl["solved"], fit(sl["solved"], 20, lw - 64, "operations solved", floor=20), ok, W6)
                     + '</g>' + _b14_ok_dot(lx + lw - 26, y + 30, end, ok, 12))
        else:
            body += (f'<g opacity="0">{_n13_on(SEN, R1)}' + T(lx + 16, y + 51, sl["sensitive"], fit(sl["sensitive"], 20, lw - 64, "operations sensitive", floor=20), "var(--c5)", W6) + '</g>'
                     + f'<g opacity="0">{_n13_on(R1)}' + T(lx + 16, y + 51, sl["routed"], fit(sl["routed"], 20, lw - 64, "operations routed", floor=20), "var(--c4)", W6) + '</g>'
                     + f'<rect x="{lx}" y="{y}" width="{lw}" height="60" rx="12" fill="none" stroke="var(--c5)" stroke-width="1.8" opacity="0">{_n13_on(SEN, R1)}</rect>'
                     + f'<g opacity="0">{_n13_on(R1)}<g transform="translate({lx + lw - 26} {y + 30}) scale(1.2)">'
                       f'<circle r="10" fill="var(--c4)"/>{_b14_icon(1, 0, 1).replace("var(--c2)", "var(--ink)")}</g></g>')
        live.append(f'<g opacity="0">{_n13_on(a)}<g>{_n01_tr([(0, "-24 0"), (a, "-24 0"), (a + .02, "0 0"), (1, "0 0")])}{body}</g></g>'
                    + _b14_ping(lx + 34, y + 30, 12, 48, a))
    kh = sb - 16 - low
    kb = (card(lx, low, cw_, kh, "var(--card)", "var(--c2)", 14, 1.4)
          + T(lx + 16, low + 34, sl["space"], fit(sl["space"], 22, cw_ - 70, "operations knowledge", floor=20), "var(--white)", W6)
          + f'<g transform="translate({lx + cw_ - 28:.0f} {low + 24}) scale(1.3)"><rect x="-8" y="-3" width="16" height="12" rx="2.5" fill="none" stroke="var(--c2)" stroke-width="1.5"/>'
            '<path d="M-5 -3 V-6 A5 5 0 0 1 5 -6 V-3" fill="none" stroke="var(--c2)" stroke-width="1.5"/></g>')
    rides = []
    for j, name in enumerate(sl["docs"]):
        y = low + 88 + 48 * j
        a0, a1 = Q[j]
        nm = T(lx + 48, y, name, fit(name, 21, cw_ - 64, "operations doc", floor=20), "var(--muted)", W6)
        kb += (f'<path d="M{lx + 18} {y - 18} h11 l5 5 v14 h-16 Z" fill="none" stroke="var(--c2)" stroke-width="1.5"/>' + nm
               + f'<g opacity="0">{beat("opacity", [(0, 0), (a0, 0), (a0 + .01, 1), (a1 + .02, 1), (a1 + .05, 0), (1, 0)])}'
                 f'<rect x="{lx + 8}" y="{y - 26}" width="{cw_ - 16:.0f}" height="36" rx="8" fill="var(--c4)" opacity=".16"/>'
                 + nm.replace('"var(--muted)"', '"var(--c4)"') + '</g>')
        rides.append(_n13_ride(f"M{lx + cw_ - 30:.0f} {y - 8} C{gut + 40:.0f} {y - 80} {lx + lw - 10} {tk_y[j] + 110} {lx + lw - 26} {tk_y[j] + 30}", a0 + .01, a1, 6))
    # ---- the three steps and the answer the AI prepares
    rows, row_y = [], []
    # a step that does not fit one line at 20 units wraps to two (rows grow from 42 to 62), never below 20 units
    two = any(bold_width(_(t), 20, current_factor(), True) > rw - 76 for t in sl["phases"][:3])
    rh, pitch = (62, 68) if two else (42, 48)
    for k, (txt, at) in enumerate(zip(sl["phases"], (P1, P2, P3))):
        y = low + pitch * k
        row_y.append(y + rh / 2)
        if bold_width(_(txt), 20, current_factor(), True) > rw - 76:
            w_ = _(txt).split()
            cut = min(range(1, len(w_)), key=lambda i: abs(len(" ".join(w_[:i])) - len(" ".join(w_[i:]))))
            a, b = " ".join(w_[:cut]), " ".join(w_[cut:])
            label = (T(rx + 40, y + 27, a, fit(a, 20, rw - 76, "operations step", floor=20), "var(--white)", W6)
                     + T(rx + 40, y + 51, b, fit(b, 20, rw - 76, "operations step", floor=20), "var(--white)", W6))
        else:
            label = T(rx + 40, y + rh / 2 + 7, txt, fit(txt, 20, rw - 76, "operations step", floor=20), "var(--white)", W6)
        rows.append(f'<g opacity=".4">{_n13_lit(at, .4)}' + card(rx, y, rw, rh, "var(--dim)", "var(--line)", 10, 1.2)
                    + _b14_icon(k, rx + 20, y + rh / 2) + label + '</g>'
                    + f'<rect x="{rx}" y="{y}" width="{rw}" height="{rh}" rx="10" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity="0">'
                      f'{beat("opacity", [(0, 0), (at, 0), (at + .01, 1), (at + .06, 1), (at + .09, 0), (1, 0)])}</rect>'
                    + _b14_ok_dot(rx + rw - 20, y + rh / 2, at + .01, ok, 11))
    dy0 = low + pitch * 3 + 4
    dh = sb - 16 - dy0
    draft = (f'<g opacity=".4">{_n13_lit(P1, .4)}' + card(rx, dy0, rw, dh, "var(--dim)", "var(--line)", 12, 1.2)
             + spark(rx + 22, dy0 + 24, .6)
             + T(rx + 42, dy0 + 31, sl["draft"], fit(sl["draft"], 20, rw - 84, "operations draft", floor=20), "var(--white)", W6) + '</g>')
    for k, L in enumerate((.9, .6)):
        y, a = dy0 + 48 + k * 16, P1 + .01 + k * .012
        draft += (f'<rect x="{rx + 18}" y="{y}" width="{(rw - 36) * L:.0f}" height="8" rx="4" fill="var(--line)" opacity=".6"/>'
                  f'<rect x="{rx + 18}" y="{y}" width="{(rw - 36) * L:.0f}" height="8" rx="4" fill="var(--c2)" opacity="0">{_n13_on(a, f=.012, hi=.8)}</rect>')
    draft += (f'<rect x="{rx}" y="{dy0}" width="{rw}" height="{dh}" rx="12" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity="0">{_n13_on(P2)}</rect>'
              + _b14_ok_dot(rx + rw - 20, dy0 + 24, P2, ok, 11))
    right = "".join(rows) + draft
    # ---- the client's phone at the console: the answer lands in the app
    px, py, pw = zx + 580, sb + 20, 220
    ph, pcx = desk + 10 - py, px + pw / 2
    note_y = py + 76
    phone = (card(px, py, pw, ph, "var(--ink)", "var(--c2)", 28, 1.6)
             + card(px + 8, py + 8, pw - 16, ph - 16, "var(--card)", "var(--line)", 22, 1)
             + f'<rect x="{pcx - 20:.0f}" y="{py + 17}" width="40" height="5" rx="2.5" fill="var(--c2)" opacity=".5"/>'
             + T(px + 22, py + 52, sl["app"], fit(sl["app"], 20, pw - 44, "operations app", floor=20), "var(--white)", W6)
             + bars(px + 22, note_y + 10, pw - 44, 4, 26, "var(--c2)", ".3"))
    nt = sl["note"]
    note = (f'<g opacity="0">{_n13_on(NOTE)}'
            + card(px + 12, note_y, pw - 24, 144, "var(--dim)", "var(--c4)", 12, 1.6)
            + f'<circle cx="{px + 34}" cy="{note_y + 26}" r="11" fill="{ok}"/>{check(px + 34, note_y + 27, .6, "var(--ink)")}'
            + T(px + 54, note_y + 33, nt[0], fit(nt[0], 20, pw - 82, "operations note", floor=20), "var(--c4)", W6)
            + TCW(px + 26, note_y + 66, nt[1], _n07_chars(nt[1], 20, pw - 50), 20, "var(--white)", W6, 1.3, "start")
            + '</g>' + _b14_ping(pcx, note_y + 70, 30, 110, NOTE))
    down = _n13_ride(f"M{rx + rw - 20} {row_y[2]} H{sx + sw - 6} V{py - 10} H{pcx} V{note_y + 20}", P3 + .005, NOTE, 7)
    # ---- the team member with the tablet (x1.3: its 16-unit labels land over 20)
    tap = (f'<g opacity="0">{_n13_on(R1)}'
           f'<rect x="-58" y="-36" width="116" height="74" rx="6" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>'
           + T(-50, -12, sl["case"], fit(sl["case"], 16, 100, "operations case", floor=16), "var(--white)", W6)
           + f'<g>{_n13_off(TAP)}' + pill(0, 16, sl["approve"], "var(--c4)", ctx, 16, 108, "operations approve", 12) + '</g>'
           + f'<g opacity="0">{_n13_on(TAP + .005)}<rect x="-34" y="4" width="68" height="24" rx="12" fill="{ok}"/>' + check(0, 17, .6, "var(--ink)") + '</g>'
           + f'<circle cx="30" cy="16" r="6" fill="none" stroke="var(--white)" stroke-width="1.5">{beat("r", [(0, 6), (TAP - .015, 6), (TAP + .06, 34), (1, 34)])}'
             f'{beat("opacity", [(0, 0), (TAP - .015, 0), (TAP - .01, 1), (TAP + .06, 0), (1, 0)])}</circle></g>')
    sm, mnx, mny = 1.3, zx + 220, sb + 116
    bx_, by_ = mnx + sm * (112 + 16 * math.sin(math.radians(10))), mny + sm * (62 + 16 * math.cos(math.radians(10)))
    sens_path = f"M{gut} {tk_y[2] + 60} V{sb} C{gut} {sb + 60} {bx_ + 40:.0f} {by_ - 120:.0f} {bx_ - 10:.0f} {by_ - 44:.0f}"
    sens = _n13_ride(sens_path, R0, R1, 7) + _b14_ping(lx + lw / 2, tk_y[2] + 30, 20, 80, SEN, "var(--c5)", .05)
    beam_up = f"M{bx_:.0f} {by_ - 18:.0f} C{bx_ + 40:.0f} {by_ - 120:.0f} {gut} {sb + 60} {gut} {sb} V{row_y[1]} H{rx + 10}"
    beam = (f'<g opacity="0">{beat("opacity", [(0, 0), (TAP, 0), (TAP + .003, .9), (P2, .9), (P2 + .03, 0), (1, 0)])}'
            f'<path d="{beam_up}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="2" stroke-linecap="round">'
            f'{beat("stroke-dashoffset", [(0, 1), (TAP, 1), (P2, 0), (1, 0)])}</path></g>'
            + _n13_ride(beam_up, TAP, P2, 7))
    people = (f'<clipPath id="pk14-desk"><rect x="0" y="{sb + 4}" width="900" height="{desk - sb - 2}"/></clipPath>'
              f'<g clip-path="url(#pk14-desk)">' + land(_n14_man(mnx, mny, sm, SKIN_BROWN, "var(--c1)", tap), .4, .6, 40) + '</g>')
    leds = "".join(f'<circle cx="{zx + 30 + k * 26}" cy="{desk + 16}" r="2.4" fill="var(--c2)" opacity=".45"/>' for k in range(6))
    console = land(f'<path d="M{zx} {desk} H{zx + zw} L{zx + zw - 12} {desk + 30} H{zx + 12} Z" fill="var(--card)"/>'
                   f'<path d="M{zx} {desk} H{zx + zw}" stroke="var(--c2)" stroke-width="1.5" opacity=".7"/>' + leds, .2, .5, 20)
    sign = T(sx + sw, zy + 26, sl["sign"], fit(sl["sign"], 22, zw - 40, "operations sign", floor=20), "var(--c4)", 'text-anchor="end" font-weight="600"')
    wall = screen + land(left + kb + right, .3, .45, 10)
    ccx, ccy = sx + sw / 2, sy + sh / 2
    return portrait_mark(g[0] + pop(f'<g transform="translate({-ccx} {-ccy})">{wall}</g>', ccx, ccy, .05, .6)
                         + "".join(live) + "".join(rides) + land(phone + note, .5, .5, 20) + land(sign, 1.4, .45, 10)
                         + people + console + down + beam + sens), D, FREEZE


@register("scene", "k14_cierre")
def sc_k14_cierre(sl, ctx):
    """The close, tomorrow's operations center, live. Left pane: three client queries arrive; the first two are answered
    by themselves from the governed knowledge; the third turns sensitive and goes down to a faceless team member's tablet,
    with its context. Right pane: the AI prepares the answer, the person approves it on the tablet (the pulse flies up to
    the screen) and the answer drops into the client's app. Frozen frame (.9): two answered by themselves, the sensitive
    one with a person, the three steps done and the answer on the phone."""
    if ORIENT() == "portrait":
        return _pk14_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    sx, sy, sw, sh = 830, 90, 720, 402
    lx, lw, rx, rw = 846, 360, 1222, 312
    gut = (lx + lw + rx) / 2
    desk, mnx, mny = 796, 996, 690
    ARR = (.05, .19, .33)                   # each query arrives
    Q = ((.09, .14), (.23, .28))           # knowledge lights, the answer lands
    SEN, R0, R1 = .36, .38, .44            # the third turns sensitive, travels down, reaches the person
    P1, TAP, P2, P3, NOTE = .49, .58, .63, .68, .74
    g = [glow(1190, 290, 470, "var(--brand)", .5)]

    # ---- the wall screen
    hud = "".join(f'<path d="M{x0} {y0 + dy * 22} V{y0} H{x0 + dx * 22}" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity=".8" transform="translate({dx * -8} {dy * -8})"/>'
                  for x0, y0, dx, dy in ((sx, sy, 1, 1), (sx + sw, sy, -1, 1), (sx, sy + sh, 1, -1), (sx + sw, sy + sh, -1, -1)))
    hud += (f'<rect x="{sx + 2}" y="{sy + 46}" width="{sw - 4}" height="2" fill="var(--c2)" opacity=".16">'
            f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {sh - 52}" dur="5s" repeatCount="indefinite"/></rect>')
    screen = (card(sx, sy, sw, sh, "var(--card)", "var(--c2)", 22, 1.2) + hud
              + f'<path d="M{sx} {sy + 44} H{sx + sw}" stroke="var(--line)" stroke-width="1.5"/>'
              + f'<path d="M{gut} {sy + 58} V{sy + sh - 16}" stroke="var(--line)" stroke-width="1" opacity=".6"/>'
              + f'<circle cx="{sx + 24}" cy="{sy + 22}" r="7" fill="var(--c5)">{blink(1.4)}</circle>'
              + T(sx + 42, sy + 28, sl["screen"], fit(sl["screen"], 16, 360, "operations screen"), "var(--white)", W6)
              + pill(sx + sw - 62, sy + 22, sl["live"], ok, ctx, 15, 110, "operations live", 14))

    # ---- left pane: the queries, answered from the governed knowledge
    tk_y = [sy + 88 + 66 * k for k in range(3)]
    kb_y = tk_y[-1] + 66
    left = T(lx, sy + 76, sl["queue"], fit(sl["queue"], 15, 220, "operations queue"), "var(--muted)", W6)
    live = []
    for k, (q, y, a) in enumerate(zip(sl["tickets"], tk_y, ARR)):
        left += f'<rect x="{lx}" y="{y}" width="{lw}" height="58" rx="10" fill="none" stroke="var(--line)" stroke-width="1.2" stroke-dasharray="4 5"/>'
        body = (card(lx, y, lw, 58, "var(--dim)", "var(--line)", 10, 1.2)
                + T(lx + 14, y + 24, q, fit(q, 15, lw - 50, "operations ticket"), "var(--white)", W6))
        end = Q[k][1] if k < 2 else SEN
        body += f'<g>{_n13_off(end)}' + T(lx + 14, y + 46, sl["new"], 15, "var(--muted)", W6) + '</g>'
        if k < 2:
            body += (f'<g opacity="0">{_n13_on(end)}' + T(lx + 14, y + 46, sl["solved"], fit(sl["solved"], 15, lw - 60, "operations solved"), ok, W6)
                     + '</g>' + _b14_ok_dot(lx + lw - 20, y + 29, end, ok, 9))
        else:
            body += (f'<g opacity="0">{_n13_on(SEN, R1)}' + T(lx + 14, y + 46, sl["sensitive"], fit(sl["sensitive"], 15, lw - 28, "operations sensitive"), "var(--c5)", W6) + '</g>'
                     + f'<g opacity="0">{_n13_on(R1)}' + T(lx + 14, y + 46, sl["routed"], fit(sl["routed"], 15, lw - 28, "operations routed"), "var(--c4)", W6) + '</g>'
                     + f'<rect x="{lx}" y="{y}" width="{lw}" height="58" rx="10" fill="none" stroke="var(--c5)" stroke-width="1.5" opacity="0">{_n13_on(SEN, R1)}</rect>'
                     + f'<g opacity="0">{_n13_on(R1)}<g transform="translate({lx + lw - 20} {y + 29})">'
                       f'<circle r="10" fill="var(--c4)"/>{_b14_icon(1, 0, 1).replace("var(--c2)", "var(--ink)")}</g></g>')
        live.append(f'<g opacity="0">{_n13_on(a)}<g>{_n01_tr([(0, "-24 0"), (a, "-24 0"), (a + .02, "0 0"), (1, "0 0")])}{body}</g></g>'
                    + _b14_ping(lx + 30, y + 29, 10, 40, a))
    kb = (card(lx, kb_y, lw, 92, "var(--card)", "var(--c2)", 12, 1.2)
          + T(lx + 14, kb_y + 26, sl["space"], fit(sl["space"], 15, lw - 60, "operations knowledge"), "var(--white)", W6)
          + f'<g transform="translate({lx + lw - 24} {kb_y + 20})"><rect x="-8" y="-3" width="16" height="12" rx="2.5" fill="none" stroke="var(--c2)" stroke-width="1.5"/>'
            '<path d="M-5 -3 V-6 A5 5 0 0 1 5 -6 V-3" fill="none" stroke="var(--c2)" stroke-width="1.5"/></g>')
    rides = []
    for j, name in enumerate(sl["docs"]):
        y = kb_y + 52 + 24 * j
        a0, a1 = Q[j]
        kb += (f'<path d="M{lx + 16} {y - 12} h8 l4 4 v10 h-12 Z" fill="none" stroke="var(--c2)" stroke-width="1.3"/>'
               + T(lx + 38, y, name, fit(name, 15, lw - 56, "operations doc"), "var(--muted)", W6)
               + f'<g opacity="0">{beat("opacity", [(0, 0), (a0, 0), (a0 + .01, 1), (a1 + .02, 1), (a1 + .05, 0), (1, 0)])}'
                 f'<rect x="{lx + 8}" y="{y - 17}" width="{lw - 16}" height="23" rx="6" fill="var(--c4)" opacity=".16"/>'
                 + T(lx + 38, y, name, fit(name, 15, lw - 56, "operations doc"), "var(--c4)", W6) + '</g>')
        rides.append(_n13_ride(f"M{lx + lw - 40} {y - 6} C{lx + lw - 6} {y - 40} {lx + lw - 6} {tk_y[j] + 60} {lx + lw - 40} {tk_y[j] + 30}", a0 + .01, a1, 5))

    # ---- right pane: the three steps and the answer the AI prepares
    rows, row_y = [], []
    for k, (text, at) in enumerate(zip(sl["phases"], (P1, P2, P3))):
        y = sy + 60 + 54 * k
        row_y.append(y + 22)
        rows.append(f'<g opacity=".4">{_n13_lit(at, .4)}' + card(rx, y, rw, 44, "var(--dim)", "var(--line)", 10, 1.2)
                    + _b14_icon(k, rx + 22, y + 22)
                    + T(rx + 42, y + 28, text, fit(text, 15, rw - 84, "operations step"), "var(--white)", W6) + '</g>'
                    + f'<rect x="{rx}" y="{y}" width="{rw}" height="44" rx="10" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity="0">'
                      f'{beat("opacity", [(0, 0), (at, 0), (at + .01, 1), (at + .06, 1), (at + .09, 0), (1, 0)])}</rect>'
                    + _b14_ok_dot(rx + rw - 22, y + 22, at + .01, ok))
    dy0 = sy + 60 + 54 * 3 + 6
    dh = sy + sh - 16 - dy0
    draft = (f'<g opacity=".4">{_n13_lit(P1, .4)}' + card(rx, dy0, rw, dh, "var(--dim)", "var(--line)", 12, 1.2)
             + spark(rx + 22, dy0 + 22, .55)
             + T(rx + 42, dy0 + 28, sl["draft"], fit(sl["draft"], 15, rw - 84, "operations draft"), "var(--white)", W6) + '</g>')
    for k, L in enumerate((.9, .75, .82, .5)):
        y, a = dy0 + 46 + k * 16, P1 + .01 + k * .012
        draft += (f'<rect x="{rx + 18}" y="{y}" width="{(rw - 36) * L:.0f}" height="7" rx="3.5" fill="var(--line)" opacity=".6"/>'
                  f'<rect x="{rx + 18}" y="{y}" width="{(rw - 36) * L:.0f}" height="7" rx="3.5" fill="var(--c2)" opacity="0">'
                  f'{_n13_on(a, f=.012, hi=.8)}</rect>')
    draft += (f'<rect x="{rx}" y="{dy0}" width="{rw}" height="{dh}" rx="12" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity="0">{_n13_on(P2)}</rect>'
              + _b14_ok_dot(rx + rw - 22, dy0 + 22, P2, ok))
    right = "".join(rows) + draft

    # ---- the client's phone: the answer lands in the app
    px, py, pw, ph = 1350, 540, 186, 256
    pcx = px + pw / 2
    note_y = py + 62
    phone = (card(px, py, pw, ph, "var(--ink)", "var(--c2)", 26, 1.5)
             + card(px + 8, py + 8, pw - 16, ph - 16, "var(--card)", "var(--line)", 20, 1)
             + f'<rect x="{pcx - 18}" y="{py + 16}" width="36" height="5" rx="2.5" fill="var(--c2)" opacity=".5"/>'
             + T(px + 22, py + 48, sl["app"], fit(sl["app"], 16, pw - 44, "operations app"), "var(--white)", W6)
             + bars(px + 22, py + 76, pw - 44, 3, 18, "var(--c2)", ".35")
             + bars(px + 22, py + 180, pw - 44, 3, 18, "var(--c2)", ".25"))
    nt = sl["note"]
    note = (f'<g opacity="0">{_n13_on(NOTE)}'
            + card(px + 14, note_y, pw - 28, 150, "var(--dim)", "var(--c4)", 12, 1.5)
            + f'<circle cx="{px + 34}" cy="{note_y + 24}" r="9" fill="{ok}"/>{check(px + 34, note_y + 25, .5, "var(--ink)")}'
            + T(px + 50, note_y + 30, nt[0], fit(nt[0], 15, pw - 78, "operations note"), "var(--c4)", W6)
            + TCW(px + 26, note_y + 58, nt[1], 16, 15, "var(--white)", W6, 1.3, "start")
            + '</g>' + _b14_ping(pcx, note_y + 70, 30, 100, NOTE))
    floor_y = sy + sh - 8
    down = _n13_ride(f"M{rx + rw - 22} {row_y[2]} H{rx + rw + 10} V{floor_y + 20} H{pcx} V{note_y + 20}", P3 + .005, NOTE, 6)

    # ---- the team member with the tablet: the sensitive case arrives with its context, then «Aprobar», then approved
    tap = (f'<g opacity="0">{_n13_on(R1)}'
           f'<rect x="-58" y="-36" width="116" height="74" rx="6" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>'
           + T(-46, -12, sl["case"], fit(sl["case"], 15, 92, "operations case"), "var(--white)", W6)
           + f'<g>{_n13_off(TAP)}' + pill(0, 16, sl["approve"], "var(--c4)", ctx, 15, 104, "operations approve", 12) + '</g>'
           + f'<g opacity="0">{_n13_on(TAP + .005)}<rect x="-34" y="4" width="68" height="24" rx="12" fill="{ok}"/>' + check(0, 17, .6, "var(--ink)") + '</g>'
           + f'<circle cx="30" cy="16" r="6" fill="none" stroke="var(--white)" stroke-width="1.5">{beat("r", [(0, 6), (TAP - .015, 6), (TAP + .06, 34), (1, 34)])}'
             f'{beat("opacity", [(0, 0), (TAP - .015, 0), (TAP - .01, 1), (TAP + .06, 0), (1, 0)])}</circle></g>')
    bx_, by_ = mnx + 112 + 16 * math.sin(math.radians(10)), mny + 62 + 16 * math.cos(math.radians(10))
    sens_path = f"M{lx + lw - 6} {tk_y[2] + 29} H{gut} V{sy + sh} C{gut} {sy + sh + 60} {bx_ + 40:.0f} {by_ - 120:.0f} {bx_ - 10:.0f} {by_ - 40:.0f}"
    sens = _n13_ride(sens_path, R0, R1, 6) + _b14_ping(lx + lw / 2, tk_y[2] + 29, 20, 70, SEN, "var(--c5)", .05)
    beam_up = f"M{bx_:.0f} {by_ - 14:.0f} C{bx_ + 40:.0f} {by_ - 120:.0f} {gut} {sy + sh + 60} {gut} {sy + sh} V{row_y[1]} H{rx + 10}"
    beam = (f'<g opacity="0">{beat("opacity", [(0, 0), (TAP, 0), (TAP + .003, .9), (P2, .9), (P2 + .03, 0), (1, 0)])}'
            f'<path d="{beam_up}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="1.5" stroke-linecap="round">'
            f'{beat("stroke-dashoffset", [(0, 1), (TAP, 1), (P2, 0), (1, 0)])}</path></g>'
            + _n13_ride(beam_up, TAP, P2, 6))
    people = (f'<clipPath id="k14-desk"><rect x="760" y="0" width="840" height="{desk + 2}"/></clipPath>'
              f'<g clip-path="url(#k14-desk)">' + land(_n14_man(mnx, mny, 1.0, SKIN_BROWN, "var(--c1)", tap), .4, .6, 40) + '</g>')
    leds = "".join(f'<circle cx="{860 + k * 26}" cy="{desk + 19}" r="2.2" fill="var(--c2)" opacity=".45"/>' for k in range(6))
    console = land(f'<path d="M820 {desk} H1330 L1318 830 H832 Z" fill="var(--card)"/>'
                   f'<path d="M820 {desk} H1330" stroke="var(--c2)" stroke-width="1.5" opacity=".7"/>' + leds, .2, .5, 20)
    sign = T(sx, sy + sh + 38, sl["sign"], fit(sl["sign"], 20, 400, "operations sign"), "var(--c4)", W6)
    wall = screen + land(left + kb + right, .3, .45, 10)
    ccx, ccy = sx + sw / 2, sy + sh / 2
    return (g[0] + pop(f'<g transform="translate({-ccx} {-ccy})">{wall}</g>', ccx, ccy, .05, .6)
            + "".join(live) + "".join(rides) + land(phone + note, .5, .5, 20) + land(sign, 1.4, .45, 10)
            + people + console + down + beam + sens), D, FREEZE


# ---------------------------------------------------------------- 7 · hypotheses: card 3 is a bank offer, with consent
def _k07_offer(a, ok, labels):
    """Ofertas a su medida (a, in seconds, opens the card's window): the app shows «Preaprobado»; the consent toggle
    switches on («Con tu consentimiento»); only then the offer card lands, with its check."""
    pre, consent = labels
    phone = (card(0, -14, 136, 138, "var(--dim)", "var(--c2)", 14, 1.2)
             + '<rect x="56" y="-8" width="24" height="3" rx="1.5" fill="var(--c2)" opacity=".6"/>'
             + '<rect x="12" y="4" width="84" height="6" rx="3" fill="var(--c2)" opacity=".3"/>'
             + _n07_ping(68, 10, 10, 60, a + .1))
    tag = (f'<g opacity="0">{_n07_hold(a + .2)}<rect x="0" y="-14" width="136" height="138" rx="14" fill="none" stroke="var(--c4)" stroke-width="1.5"/>'
           f'<rect x="4" y="-4" width="128" height="28" rx="8" fill="var(--card)"/>'
           + T(12, 15, pre, fit(pre, 15, 112, "offer preapproved"), "var(--c4)", W6) + '</g>')
    track = (card(12, 32, 38, 20, "var(--card)", "var(--c2)", 10, 1.2)
             + f'<g opacity="0">{_n07_hold(a + .75, .1)}{card(12, 32, 38, 20, ok, ok, 10, 0)}</g>'
             + f'<g>{_n07_tr([(a + .5, "0 0"), (a + .75, "18 0"), (_N07_RESET[0], "18 0"), (_N07_RESET[1], "0 0")])}'
               '<circle cx="22" cy="42" r="7" fill="var(--white)"/></g>'
             + _n07_ping(40, 42, 8, 24, a + .75, ok))
    label = (f'<g opacity=".6">{_n07_hold(a + .75, .15, .6)}'
             + TCW(12, 74, consent, _n07_chars(consent, 15, 112), 15, "var(--white)", W6, 1.2, "start") + '</g>')
    hop = (f'<g opacity="0">{_n07_key("opacity", [(a + .85, 0), (a + .9, 1), (a + 1.1, 1), (a + 1.12, 0)])}'
           f'{_n07_move("M50 42 C100 42 150 40 171 64", [(a + .9, 0), (a + 1.1, 1)])}{token("var(--c4)", 4)}</g>')
    offer = (card(146, 56, 50, 64, "var(--card)", "var(--c4)", 8, 1.5)
             + '<circle cx="160" cy="72" r="6" fill="none" stroke="var(--c4)" stroke-width="1.5"/>'
             + "".join(f'<rect x="154" y="{86 + 9 * j}" width="{w}" height="4" rx="2" fill="var(--c4)" opacity=".7"/>' for j, w in enumerate((30, 20))))
    landed = (f'<rect x="146" y="56" width="50" height="64" rx="8" fill="none" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="3 4" opacity=".6"/>'
              + f'<g opacity="0">{_n07_hold(a + 1.1, .1)}<g>{_n07_tr([(a + 1.1, "0 -16"), (a + 1.3, "0 0")])}{offer}</g></g>'
              + _n07_ping(171, 88, 20, 44, a + 1.3))
    return phone + tag + track + label + hop + landed + _n07_badge(186, 104, a + 1.45, ok)


# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
def _pk07_offer(a, ok, labels):
    """_k07_offer drawn wider for the phone stage (placed at x1.1, so its 19-unit labels land over 20): the same
    «Preaprobado», consent toggle and offer landing, the consent label under the toggle with room for two lines."""
    pre, consent = labels
    PW, OX = 172, 184                                    # the phone's width, the offer card's left edge
    phone = (card(0, -14, PW, 138, "var(--dim)", "var(--c2)", 14, 1.2)
             + f'<rect x="{PW / 2 - 12:.0f}" y="-8" width="24" height="3" rx="1.5" fill="var(--c2)" opacity=".6"/>'
             + _n07_ping(PW / 2, 10, 10, 60, a + .1))
    tag = (f'<g opacity="0">{_n07_hold(a + .2)}<rect x="0" y="-14" width="{PW}" height="138" rx="14" fill="none" stroke="var(--c4)" stroke-width="1.5"/>'
           f'<rect x="4" y="-6" width="{PW - 8}" height="30" rx="8" fill="var(--card)"/>'
           + T(12, 16, pre, fit(pre, 19, PW - 24, "offer preapproved", floor=19), "var(--c4)", W6) + '</g>')
    track = (card(12, 32, 38, 20, "var(--card)", "var(--c2)", 10, 1.2)
             + f'<g opacity="0">{_n07_hold(a + .75, .1)}{card(12, 32, 38, 20, ok, ok, 10, 0)}</g>'
             + f'<g>{_n07_tr([(a + .5, "0 0"), (a + .75, "18 0"), (_N07_RESET[0], "18 0"), (_N07_RESET[1], "0 0")])}'
               '<circle cx="22" cy="42" r="7" fill="var(--white)"/></g>'
             + _n07_ping(40, 42, 8, 24, a + .75, ok))
    label = (f'<g opacity=".6">{_n07_hold(a + .75, .15, .6)}'
             + TCW(12, 78, consent, _n07_chars(consent, 19, PW - 20), 19, "var(--white)", W6, 1.2, "start") + '</g>')
    hop = (f'<g opacity="0">{_n07_key("opacity", [(a + .85, 0), (a + .9, 1), (a + 1.1, 1), (a + 1.12, 0)])}'
           f'{_n07_move(f"M50 42 C110 42 {OX} 40 {OX + 25} 64", [(a + .9, 0), (a + 1.1, 1)])}{token("var(--c4)", 4)}</g>')
    offer = (card(OX, 56, 50, 64, "var(--card)", "var(--c4)", 8, 1.5)
             + f'<circle cx="{OX + 14}" cy="72" r="6" fill="none" stroke="var(--c4)" stroke-width="1.5"/>'
             + "".join(f'<rect x="{OX + 8}" y="{86 + 9 * j}" width="{w}" height="4" rx="2" fill="var(--c4)" opacity=".7"/>' for j, w in enumerate((30, 20))))
    landed = (f'<rect x="{OX}" y="56" width="50" height="64" rx="8" fill="none" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="3 4" opacity=".6"/>'
              + f'<g opacity="0">{_n07_hold(a + 1.1, .1)}<g>{_n07_tr([(a + 1.1, "0 -16"), (a + 1.3, "0 0")])}{offer}</g></g>'
              + _n07_ping(OX + 25, 88, 20, 44, a + 1.3))
    return phone + tag + track + label + hop + landed + _n07_badge(OX + 40, 104, a + 1.45, ok)


def _pk07_text(x, y, text, size, room, fill, lines=2):
    """text wrapped into room at the largest size (never under 20, the phone floor) that fits in `lines` lines."""
    z = size
    while z > 20 and len(_n07_wrap(_(str(text)), _n07_chars(text, z, room))) > lines:
        z -= 1
    return TCW(x, y, text, _n07_chars(text, z, room), z, fill, W6, 1.3, "start")


def _pk07_twin(sl, ctx):
    """k07 on the 900x1600 stage (the _p07_hipotesis layout): the three hypotheses as full-width rows, text on the left
    and their small story on the right (the chat, the documents, the consented offer), the enabler under them, a spine
    on the left carrying its pulse into each row. Same loop and frozen frame."""
    ok = ctx.brand.c("dark.ok")
    cols = ("var(--c1)", "var(--c3)", "var(--c2)", "var(--accent)")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    SX, X0 = zx + 20, zx + 44
    W, RH, GAP = zx + zw - X0, 168, 12
    ys = [zy + 22 + k * (RH + GAP) for k in range(3)]
    BY, BH = ys[-1] + RH + 26, 304
    wins = ((2.2, 4.6), (4.6, 7.0), (7.0, 9.4), (9.4, _N07_RESET[0]))
    R = _N07_RESET

    def qmark(cx, cy, a):
        return (f'<circle cx="{cx}" cy="{cy}" r="20" fill="var(--card)" stroke="var(--c4)" stroke-width="1.8"/>'
                + TC(cx, cy + 8.5, "?", 24, "var(--c4)", W6) + _n07_ping(cx, cy, 20, 38, a + .05))   # one ring: the 35 KB budget

    def spot(x, y, w, h, a, b):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="none" stroke="var(--c4)" stroke-width="2.4" opacity="0">{_n07_win(a, b)}</rect>'

    art, text = [glow(zx + zw / 2, zy + zh * .45, 470, "var(--brand)", .45)], []
    stories = (_b07_chat(wins[0][0], ok), _b07_docs(wins[1][0], ok, _N07_SKIN_MID), _pk07_offer(wins[2][0], ok, sl["offer"]))
    f = current_factor()
    for k in range(3):
        y, (area, idea, gain), (a, b), at = ys[k], sl["cards"][k], wins[k], .1 + .12 * k
        sw_ = 290 if k == 2 else 262                       # the offer story is the wider one
        room = W - 24 - sw_
        art.append(land(card(X0, y, W, RH, "var(--card)", "var(--line)", 18, 1.2)
                        + f'<rect x="{X0 + 18}" y="{y - 2}" width="{W * .4:.0f}" height="4" rx="2" fill="{cols[k]}"/>'
                        + f'<g transform="translate({X0 + W - sw_ + 18} {y + 24}) scale(1.1)">{stories[k]}</g>'
                        + spot(X0, y, W, RH, a, b) + qmark(X0 + W - 30, y, a), at, .5, 16))
        rw = bold_width(_(str(sl["ret"])), 20, f)
        text.append(land(T(X0 + 24, y + 42, area, fit(area, 26, room, "hypothesis area", floor=20), "var(--white)", W6)
                         + _pk07_text(X0 + 24, y + 76, idea, 21, room, "var(--muted)")
                         + T(X0 + 24, y + 148, sl["ret"], 20, "var(--muted)", W6)
                         + T(f"{X0 + 36 + rw:.1f}", y + 148, gain, fit(gain, 24, room - rw - 12, "hypothesis return", floor=20), "var(--c4)", W6),
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
    text.append(land(T(X0 + 24, BY + 44, area, fit(area, 26, W - 100, "hypothesis area", floor=20), "var(--white)", W6)
                     + _pk07_text(X0 + 24, BY + 80, idea, 21, W - 48, "var(--muted)")
                     + TC(f"{mid:.1f}", BY + 250, sl["cycle"], fit(sl["cycle"], 21, W - 48, "hypothesis cycle", floor=20), "var(--muted)", W6)
                     + T(X0 + 24, BY + 288, gain, fit(gain, 24, W - 48, "hypothesis enabler", floor=20), "var(--c4)", W6), .46, .5, 16))
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


@register("scene", "k07_hipotesis")
def sc_k07_hipotesis(sl, ctx):
    """b07_hipotesis for a bank: the same four cards and loop, with a banking story on card 3: a pre-approved offer on
    the phone, the client's consent switched on, the offer landing with its check."""
    if ORIENT() == "portrait":
        return _pk07_twin(sl, ctx)
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
    stories = (_b07_chat(wins[0][0], ok), _b07_docs(wins[1][0], ok, _N07_SKIN_MID), _k07_offer(wins[2][0], ok, sl["offer"]))
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

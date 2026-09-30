"""Bench c, slide 7 of the class deck (slides 8 and 9 use the shared hypotheses-live and criterion scenes).
v07_palabras - mirroring: the client's public page with its phrase highlighted; our draft slide first copies it in
               quotes and that line is struck («suena a copiar»); it is rewritten in our own voice and a «match» link
               ties it back to the client's phrase."""


def _v07_on(a, lo=0, hi=1, f=.02):
    """Opacity lo until fraction a, hi from a until the reset."""
    return beat("opacity", [(0, lo), (a, lo), (a + f, hi), (.97, hi), (1, lo)])


def _v07_draw(a, f=.03):
    """A pathLength=1 stroke that draws itself at fraction a and stays until the reset."""
    return beat("stroke-dashoffset", [(0, 1), (a, 1), (a + f, 0), (.97, 0), (1, 1)])


@register("scene", "v07_palabras")
def sc_v07_palabras(sl, ctx):
    """Left, the client's public page: its headline phrase gets highlighted. Right, our draft slide for Thursday: the
    phrase is copied in quotes, then struck and tagged «suena a copiar»; the idea is rewritten in our words, lights up,
    and a «match» link runs back to the client's phrase. Frozen frame: the quote struck, our phrase lit and linked."""
    if ORIENT() == "portrait":
        return _pv07_palabras(sl, ctx)
    fac = current_factor()
    g = [glow(1195, 450, 460, "var(--brand)", .5)]
    # ------------------------------------------------ the client's public page
    px, py, pw, ph = 840, 150, 300, 600
    page = (T(px, py - 18, sl["source"], fit(sl["source"], 17, pw, "palabras source"), "var(--muted)", W6)
            + card(px, py, pw, ph, "var(--card)", "var(--c2)", 16, 1.4)
            + f'<path d="M{px} {py + 40} H{px + pw}" stroke="var(--line)" stroke-width="1.2"/>'
            + "".join(f'<circle cx="{px + 22 + k * 16}" cy="{py + 20}" r="4" fill="var(--c2)" opacity=".5"/>' for k in range(3))
            + f'<rect x="{px + 74}" y="{py + 13}" width="206" height="14" rx="7" fill="var(--dim)"/>'
            + f'<rect x="{px + 22}" y="{py + 62}" width="54" height="14" rx="4" fill="var(--c2)" opacity=".55"/>'
            + "".join(f'<rect x="{px + 150 + k * 44}" y="{py + 66}" width="32" height="6" rx="3" fill="var(--c2)" opacity=".35"/>' for k in range(3))
            + T(px + 22, py + 118, sl["section"], fit(sl["section"], 16, pw - 44, "palabras section"), "var(--c2)", W6))
    lines = _p11_wrap(sl["phrase"], 30, pw - 44)
    hl = ""
    for i, ln in enumerate(lines):   # the client's highlighter: sweeps under each line and stays
        w = bold_width(_(ln), 30, fac) + 12
        y = py + 142 + i * 40
        hl += (f'<rect x="{px + 16}" y="{y + 34}" width="{w:.0f}" height="6" rx="3" fill="var(--c4)">'
               + beat("width", [(0, 0), (.06 + i * .03, 0), (.09 + i * .03, round(w)), (.97, round(w)), (1, 0)]) + '</rect>')
    head = "".join(T(px + 22, py + 170 + i * 40, ln, 30, "var(--white)", 'font-weight="700"') for i, ln in enumerate(lines))
    body = ("".join(f'<rect x="{px + 22}" y="{py + 320 + k * 20}" width="{(pw - 44) * (.92, .8, .55)[k]:.0f}" height="7" rx="3.5" fill="var(--c2)" opacity=".4"/>' for k in range(3))
            + f'<rect x="{px + 22}" y="{py + 392}" width="110" height="34" rx="17" fill="none" stroke="var(--c2)" stroke-width="1.4" opacity=".6"/>'
            + f'<rect x="{px + 22}" y="{py + 450}" width="{pw - 44}" height="126" rx="12" fill="var(--dim)"/>'
            + f'<path d="M{px + 40} {py + 556} L{px + 110} {py + 490} L{px + 160} {py + 530} L{px + 200} {py + 500} L{px + 238} {py + 556}" fill="none" stroke="var(--c2)" stroke-width="1.4" opacity=".55"/>')
    g.append(land(page + body, .1, .5))
    g.append(hl + head)
    # the phrase glows once the match lands
    g.append(f'<g>{_v07_on(.76)}<rect x="{px + 12}" y="{py + 138}" width="{pw - 24}" height="{40 * len(lines) + 8}" rx="10" fill="none" '
             f'stroke="var(--c4)" stroke-width="1.8">{loop("stroke-opacity", ".45;1;.45", 2.4)}</rect></g>')
    # ------------------------------------------------ our draft slide
    dx, dy, dw, dh = 1180, 150, 370, 600
    draft = (T(dx, dy - 18, sl["draft"], fit(sl["draft"], 17, dw, "palabras draft"), "var(--muted)", W6)
             + card(dx, dy, dw, dh, "var(--card)", "var(--c2)", 16, 1.4)
             + f'<rect x="{dx + 24}" y="{dy + 26}" width="54" height="5" rx="2.5" fill="var(--c4)"/>'
             + f'<rect x="{dx + 24}" y="{dy + 46}" width="200" height="10" rx="5" fill="var(--c2)" opacity=".45"/>'
             + "".join(f'<rect x="{dx + 24}" y="{dy + 470 + k * 22}" width="{(dw - 48) * (.85, .7, .45)[k]:.0f}" height="7" rx="3.5" fill="var(--c2)" opacity=".35"/>' for k in range(3)))
    g.append(land(draft, .3, .5))
    # the copy: a token carries the client's words into the draft
    carry = f"M{px + 190} {py + 170} C{px + 300} {py + 80} {dx + 20} {dy + 80} {dx + 40} {dy + 112}"
    g.append(f'<g>{beat("opacity", [(0, 0), (.16, 0), (.17, 1), (.23, 1), (.24, 0), (1, 0)])}{token("var(--c4)", 6)}'
             f'{move(carry, [(0, 0), (.16, 0), (.23, 1), (1, 1)], D)}</g>')
    # line A: the quote, then struck and dimmed
    qs, qx, qy = 22, dx + 24, dy + 118
    qlines = _p11_wrap(sl["copied"], qs, dw - 48)
    quote = "".join(T(qx, qy + i * 30, ln, qs, "var(--white)", W6) for i, ln in enumerate(qlines))
    g.append(f'<g>{beat("opacity", [(0, 0), (.23, 0), (.25, 1), (.42, 1), (.44, .5), (.97, .5), (1, 0)])}{quote}</g>')
    for i, ln in enumerate(qlines):
        x1 = qx + min(dw - 48, bold_width(_(ln), qs, fac)) + 6
        ym = qy + i * 30 - 7
        g.append(f'<path d="M{qx - 6} {ym + 2} L{x1:.0f} {ym - 2}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c5)" '
                 f'stroke-width="3.5" stroke-linecap="round">{_v07_draw(.36 + i * .03)}</path>')
    ty = qy + 30 * len(qlines) + 18
    tag = pill(0, 0, sl["copy_tag"], "var(--c5)", ctx, 16, dw - 48, "palabras copy tag")
    g.append(f'<g>{_v07_on(.44)}<g transform="translate({qx + 90} {ty})">{tag}</g></g>')
    # line B: our own words, lit
    by, bh = dy + 270, 130
    blines = _p11_wrap(sl["ours"], 24, dw - 80)
    ours = (f'<rect x="{dx + 16}" y="{by}" width="{dw - 32}" height="{bh}" rx="14" fill="var(--card)" stroke="var(--c4)" stroke-width="1.8"/>'
            + "".join(T(dx + 36, by + 50 + i * 32, ln, 24, "var(--white)", 'font-weight="700"') for i, ln in enumerate(blines)))
    g.append(f'<g>{_v07_on(.54)}{glow(dx + dw / 2, by + bh / 2, 170, "var(--c4)", .25)}'
             f'<g><animateTransform attributeName="transform" type="translate" values="0 14;0 14;0 0;0 0" keyTimes="0;.54;.57;1" dur="{D}s" repeatCount="indefinite"/>{ours}</g></g>')
    g.append(f'<g>{_v07_on(.58)}<g>{loop("opacity", ".5;1;.5", 2.2)}{spark(dx + dw - 34, by + 26, .6, "var(--c4)")}</g></g>')
    # the match: a thread from our words back to theirs
    mx, my = px + pw - 52, py + 262
    link = f"M{dx + 16} {by + bh / 2:.0f} C{dx - 30} {by + bh / 2:.0f} {mx + 60} {my + 10} {mx + 44} {my}"
    g.append(f'<path d="{link}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="1.8">{_v07_draw(.66, .07)}</path>')
    g.append(f'<g>{beat("opacity", [(0, 0), (.66, 0), (.67, 1), (.73, 1), (.74, 0), (1, 0)])}{token("var(--c4)", 5)}'
             f'{move(link, [(0, 0), (.66, 0), (.73, 1), (1, 1)], D)}</g>')
    g.append(f'<path d="M{mx} {my - 16} L{mx - 10} {py + 138 + 40 * len(lines) + 8}" fill="none" stroke="var(--c4)" stroke-width="1.8">{_v07_on(.74)}</path>')
    badge = pill(0, 0, sl["match"], "var(--c4)", ctx, 16, 120, "palabras match")
    g.append(f'<g>{_v07_on(.74)}<g transform="translate({mx} {my})">{badge}</g>'
             f'<g>{loop("opacity", ".5;1;.5", 2.2)}{spark(mx - 52, my - 20, .55, "var(--c4)")}</g></g>')
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- portrait twin (the mobile build, DCD_ORIENT=portrait)
def _pv07_palabras(sl, ctx):
    """v07 on the 900x1600 stage: the client's page on top, our draft for Thursday below; the quote is copied down,
    struck, rewritten in our words and linked back up by the «match» thread. Same beats, same frozen frame."""
    fac = current_factor()
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    g = [glow(zx + zw / 2, zy + 460, 480, "var(--brand)", .5)]
    px, py, pw, ph = zx, zy + 40, zw, 310
    room = 470
    page = (T(px, py - 16, sl["source"], fit(sl["source"], 22, pw, "palabras source", floor=20), "var(--muted)", W6)
            + card(px, py, pw, ph, "var(--card)", "var(--c2)", 16, 1.4)
            + f'<path d="M{px} {py + 44} H{px + pw}" stroke="var(--line)" stroke-width="1.2"/>'
            + "".join(f'<circle cx="{px + 24 + k * 18}" cy="{py + 22}" r="5" fill="var(--c2)" opacity=".5"/>' for k in range(3))
            + f'<rect x="{px + 90}" y="{py + 14}" width="320" height="16" rx="8" fill="var(--dim)"/>'
            + f'<rect x="{px + 24}" y="{py + 64}" width="64" height="16" rx="4" fill="var(--c2)" opacity=".55"/>'
            + "".join(f'<rect x="{px + 170 + k * 52}" y="{py + 69}" width="38" height="7" rx="3.5" fill="var(--c2)" opacity=".35"/>' for k in range(3))
            + T(px + 24, py + 118, sl["section"], fit(sl["section"], 22, room, "palabras section", floor=20), "var(--c2)", W6))
    ps, plh = 38, 46
    lines = _p11_wrap(sl["phrase"], ps, room)
    top = py + 132
    hl = ""
    for i, ln in enumerate(lines):
        w = min(room, bold_width(_(ln), ps, fac)) + 12
        y = top + i * plh
        hl += (f'<rect x="{px + 18}" y="{y + 42}" width="{w:.0f}" height="7" rx="3.5" fill="var(--c4)">'
               + beat("width", [(0, 0), (.06 + i * .03, 0), (.09 + i * .03, round(w)), (.97, round(w)), (1, 0)]) + '</rect>')
    head = "".join(T(px + 24, top + 36 + i * plh, ln, ps, "var(--white)", 'font-weight="700"') for i, ln in enumerate(lines))
    hb = top + plh * len(lines) + 12
    body = ("".join(f'<rect x="{px + 24}" y="{hb + 14 + k * 22}" width="{300 * (.92, .8, .55)[k]:.0f}" height="8" rx="4" fill="var(--c2)" opacity=".4"/>' for k in range(3))
            + f'<rect x="{px + pw - 250}" y="{py + 64}" width="226" height="{ph - 88}" rx="12" fill="var(--dim)"/>'
            + f'<path d="M{px + pw - 230} {py + ph - 40} L{px + pw - 170} {py + 150} L{px + pw - 120} {py + 200} L{px + pw - 80} {py + 160} L{px + pw - 44} {py + ph - 40}" fill="none" stroke="var(--c2)" stroke-width="1.6" opacity=".55"/>')
    g.append(land(page + body, .1, .5))
    g.append(hl + head)
    g.append(f'<g>{_v07_on(.76)}<rect x="{px + 12}" y="{top - 4}" width="{room + 24}" height="{plh * len(lines) + 14}" rx="10" fill="none" '
             f'stroke="var(--c4)" stroke-width="2.2">{loop("stroke-opacity", ".45;1;.45", 2.4)}</rect></g>')
    dx, dy, dw = zx, py + ph + 72, zw
    dh = zy + zh - dy
    draft = (T(dx, dy - 16, sl["draft"], fit(sl["draft"], 22, dw, "palabras draft", floor=20), "var(--muted)", W6)
             + card(dx, dy, dw, dh, "var(--card)", "var(--c2)", 16, 1.4)
             + f'<rect x="{dx + 26}" y="{dy + 28}" width="64" height="6" rx="3" fill="var(--c4)"/>'
             + f'<rect x="{dx + 26}" y="{dy + 50}" width="300" height="12" rx="6" fill="var(--c2)" opacity=".45"/>'
             + "".join(f'<rect x="{dx + 26}" y="{dy + dh - 80 + k * 22}" width="{(dw - 52) * (.85, .7, .45)[k]:.0f}" height="8" rx="4" fill="var(--c2)" opacity=".35"/>' for k in range(3)))
    g.append(land(draft, .3, .5))
    carry = f"M{px + 200} {top + 20} C{px + 120} {top + 180} {dx + 20} {dy - 60} {dx + 44} {dy + 96}"
    g.append(f'<g>{beat("opacity", [(0, 0), (.16, 0), (.17, 1), (.23, 1), (.24, 0), (1, 0)])}{token("var(--c4)", 7)}'
             f'{move(carry, [(0, 0), (.16, 0), (.23, 1), (1, 1)], D)}</g>')
    qs, qx, qy = 28, dx + 26, dy + 112
    qlines = _p11_wrap(sl["copied"], qs, dw - 52)
    quote = "".join(T(qx, qy + i * 36, ln, qs, "var(--white)", W6) for i, ln in enumerate(qlines))
    g.append(f'<g>{beat("opacity", [(0, 0), (.23, 0), (.25, 1), (.42, 1), (.44, .5), (.97, .5), (1, 0)])}{quote}</g>')
    for i, ln in enumerate(qlines):
        x1 = qx + min(dw - 52, bold_width(_(ln), qs, fac)) + 6
        ym = qy + i * 36 - 9
        g.append(f'<path d="M{qx - 6} {ym + 2} L{x1:.0f} {ym - 2}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c5)" '
                 f'stroke-width="4" stroke-linecap="round">{_v07_draw(.36 + i * .03)}</path>')
    ty = qy + 36 * (len(qlines) - 1) + 44
    tag_s = fit(sl["copy_tag"], 22, dw - 52, "palabras copy tag", floor=20)
    tw = bold_width(_(str(sl["copy_tag"])), tag_s, fac) + 36
    tag = pill(0, 0, sl["copy_tag"], "var(--c5)", ctx, 22, dw - 52, "palabras copy tag")
    g.append(f'<g>{_v07_on(.44)}<g transform="translate({qx + tw / 2:.0f} {ty})">{tag}</g></g>')
    bs = 30
    blines = _p11_wrap(sl["ours"], bs, dw - 110)
    bh = 60 + 38 * len(blines)
    by = ty + 44
    ours = (f'<rect x="{dx + 16}" y="{by}" width="{dw - 32}" height="{bh}" rx="14" fill="var(--card)" stroke="var(--c4)" stroke-width="2.2"/>'
            + "".join(T(dx + 40, by + 52 + i * 38, ln, bs, "var(--white)", 'font-weight="700"') for i, ln in enumerate(blines)))
    g.append(f'<g>{_v07_on(.54)}{glow(dx + dw / 2, by + bh / 2, 220, "var(--c4)", .25)}'
             f'<g><animateTransform attributeName="transform" type="translate" values="0 14;0 14;0 0;0 0" keyTimes="0;.54;.57;1" dur="{D}s" repeatCount="indefinite"/>{ours}</g></g>')
    g.append(f'<g>{_v07_on(.58)}<g>{loop("opacity", ".5;1;.5", 2.2)}{spark(dx + dw - 40, by + 30, .75, "var(--c4)")}</g></g>')
    mx, my = px + room + 110, top + plh * len(lines) / 2 + 4
    link = f"M{dx + dw - 16} {by + bh / 2:.0f} C{zx + zw + 30} {by + bh / 2:.0f} {zx + zw + 20} {my + 40:.0f} {mx + 56} {my:.0f}"
    g.append(f'<path d="{link}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="2.2">{_v07_draw(.66, .07)}</path>')
    g.append(f'<g>{beat("opacity", [(0, 0), (.66, 0), (.67, 1), (.73, 1), (.74, 0), (1, 0)])}{token("var(--c4)", 6)}'
             f'{move(link, [(0, 0), (.66, 0), (.73, 1), (1, 1)], D)}</g>')
    g.append(f'<path d="M{mx - 50} {my:.0f} H{px + room + 36}" fill="none" stroke="var(--c4)" stroke-width="2.2">{_v07_on(.74)}</path>')
    badge = pill(0, 0, sl["match"], "var(--c4)", ctx, 22, 140, "palabras match")
    g.append(f'<g>{_v07_on(.74)}<g transform="translate({mx} {my:.0f})">{badge}</g>'
             f'<g>{loop("opacity", ".5;1;.5", 2.2)}{spark(mx - 60, my - 26, .7, "var(--c4)")}</g></g>')
    return portrait_mark("".join(g)), D, FREEZE

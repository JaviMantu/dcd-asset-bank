"""Bench b · slides 4 and 6 of the salud deck (slide 5 keeps the harvested shared-asset scene).
Each scene tells one 12-second story with beat() and freezes (reduced motion, 0.9 of the loop) on the resolved frame.

- b04_tesis: a client tells their case to the service line; they transfer it, the next channel asks again, and again;
  the reimbursement then waits for a document that already sat in another system, and the wait keeps growing.
  Frozen: the same story copied in three channels, the reimbursement waiting, the document out of reach, a long wait.
- b06_sector: the figure stays still. Below it the digital door is open: its services light up one by one, each sends
  its datum behind the door, the record of the client completes and care arrives in time; the other branch, the wait,
  stays drawn. Frozen: every service lit, the record complete, care on time.

Runs in the shared namespace of module/ext.py: every helper comes from scenes/lib.py and the engine.
"""

_b04_end = .98   # every resolved state holds until here, then the loop resets


def _b04_win(a, b=_b04_end, lo=0, hi=1, f=.02):
    """beat() pairs: lo until a, hi from a + f until b, back to lo by the end of the loop."""
    pts = [(0, lo), (a, lo), (a + f, hi), (b, hi)]
    return pts + [(1, lo)] if b + f >= 1 else pts + [(b + f, lo), (1, lo)]


def _b04_trip(a, b):
    """beat() pairs: visible only while travelling from a to b."""
    return [(0, 0), (a, 0), (a + .005, 1), (b, 1), (b + .01, 0), (1, 0)]


def _b04_ping(x, y, r0, r1, col, times, span=.1, op=.8):
    """Rings that open once at each time in `times` and fade (invisible in the frozen frame)."""
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r0}" fill="none" stroke="{col}" stroke-width="1.5" opacity="0">'
                   f'{beat("r", [(0, r0), (a, r0), (a + span, r1), (1, r1)])}'
                   f'{beat("opacity", [(0, 0), (a, 0), (a + .005, op), (a + span, 0), (1, 0)])}</circle>' for a in times)


def _b04_draw(d, col, a, b, w=2):
    """A path that draws itself between a and b and stays drawn until the loop resets."""
    return (f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round">'
            f'{beat("stroke-dashoffset", [(0, 1), (a, 1), (b, 0), (_b04_end, 0), (1, 1)])}</path>')


def _b04_story(x, y, w, col, op=1):
    """Three lines of a told story (a case), as bars."""
    return "".join(f'<rect x="{x}" y="{y + k * 13}" width="{w * (.92, .7, .82)[k]:.0f}" height="6" rx="3" fill="{col}" opacity="{op}"/>'
                   for k in range(3))


def _b04_db(x, y, col="var(--c2)"):
    """A small database cylinder, thin strokes: the system behind each channel."""
    s = f'fill="none" stroke="{col}" stroke-width="1.5"'
    return (f'<ellipse cx="{x}" cy="{y - 8}" rx="10" ry="4" {s}/><path d="M{x - 10} {y - 8} V{y + 8} A10 4 0 0 0 {x + 10} {y + 8} V{y - 8}" {s}/>'
            f'<path d="M{x - 10} {y} A10 4 0 0 0 {x + 10} {y}" {s}/>')


def _b04_doc(x, y, col, dashed=False):
    """A document sheet centered at (x, y), 30 x 38, with a folded corner."""
    dash = ' stroke-dasharray="4 4"' if dashed else ""
    fill = "none" if dashed else f"color-mix(in srgb, {col} 25%, var(--card))"
    return (f'<path d="M{x - 15} {y - 19} H{x + 7} L{x + 15} {y - 11} V{y + 19} H{x - 15} Z" fill="{fill}" stroke="{col}" stroke-width="1.6" stroke-linejoin="round"{dash}/>'
            + ("" if dashed else "".join(f'<path d="M{x - 9} {y - 4 + k * 8} H{x + 9}" stroke="{col}" stroke-width="1.5" stroke-linecap="round"/>' for k in range(3))))


def _b04_clock(col):
    s = f'fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round"'
    return f'<circle r="12" {s}/><path d="M0 -7 V0 L5 3" {s}/>'


def _b04_talk(x, y, col):
    """A small speech bubble outline, thin stroke, centered at (x, y)."""
    return (f'<path d="M{x - 12} {y - 9} H{x + 12} Q{x + 15} {y - 9} {x + 15} {y - 6} V{y + 4} Q{x + 15} {y + 7} {x + 12} {y + 7} '
            f'H{x - 3} L{x - 9} {y + 12} V{y + 7} H{x - 12} Q{x - 15} {y + 7} {x - 15} {y + 4} V{y - 6} Q{x - 15} {y - 9} {x - 12} {y - 9} Z" '
            f'fill="{col}" fill-opacity=".18" stroke="{col}" stroke-width="1.5" stroke-linejoin="round"/>')


# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
def _pb04_twin(sl, ctx):
    """b04 on the 900x1600 stage: the client and the retellings on the left, the three channels stacked on the right
    with the transfers on their edge, the waiting refund and the other system under them, the wait across the bottom.
    Same beats, same frozen frame: one story copied three times, the refund waiting, the document out of reach."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    px, py = zx + 100, zy + 130                         # the client
    cx, cw, ch = zx + 250, 420, 118                     # the channel cards
    ys = (zy + 20, zy + 190, zy + 360)
    tell = (.18, .37, .55)
    arrive = tuple(t + .07 for t in tell)
    xfer = ((.29, .33), (.47, .51))
    ask = (.34, .52)
    wait_at, reach, stuck = .64, (.66, .71), .71
    art, text = [glow(zx + zw / 2, zy + 420, 460, "var(--brand)", .4)], []
    voice = "".join(f'<g opacity="0">{beat("opacity", [(0, 0), (t, 0), (t + .01, 1), (t + .06, 1), (t + .07, 0), (1, 0)])}'
                    f'<path d="M50 -80 Q63 -62 50 -45" fill="none" stroke="var(--c4)" stroke-width="2.2" stroke-linecap="round"/>'
                    f'<path d="M63 -90 Q80 -62 63 -35" fill="none" stroke="var(--c4)" stroke-width="1.8" stroke-linecap="round" opacity=".6"/></g>'
                    for t in tell)
    client = (f'<g transform="translate({px} {py})">{_user(0, 0, 2.6, "var(--c2)")}'
              f'<rect x="20" y="-90" width="18" height="30" rx="4" fill="none" stroke="var(--c4)" stroke-width="2" transform="rotate(14 29 -75)"/>{voice}</g>'
              + TC(px, py + 80, sl["client"], fit(sl["client"], 22, 180, "client label", floor=20), "var(--white)", W6))
    art.append(land(client, .1, .5, 0))
    # how many times the story is told
    for k, (label, t) in enumerate(zip(sl["tells"], tell)):
        ty = py + 150 + k * 58
        s = fit(label, 22, 170, "retelling", floor=20)
        text.append(land(f'<g opacity=".35">{beat("opacity", _b04_win(t, lo=.35))}<g transform="translate({zx + 30} {ty - 6}) scale(1.3)">{_b04_talk(0, 0, "var(--c4)" if k else "var(--c2)")}</g>'
                         + T(zx + 58, f"{ty + s * .36 - 6:.0f}", label, s, "var(--white)", W6) + '</g>', .5 + k * .1, .4, 10))
    # the three channels, each with its own system; the story lands in each one, identical
    for k, (y, name) in enumerate(zip(ys, sl["channels"])):
        s = fit(name, 22, cw - 80, "channel name", floor=20)
        empty = "".join(f'<rect x="{cx + 22}" y="{y + 60 + j * 16}" width="{(cw - 44) * (.92, .7, .82)[j]:.0f}" height="8" rx="4" fill="none" '
                        f'stroke="var(--line)" stroke-width="1" stroke-dasharray="3 4"/>' for j in range(3))
        full = "".join(f'<rect x="{cx + 22}" y="{y + 60 + j * 16}" width="{(cw - 44) * (.92, .7, .82)[j]:.0f}" height="8" rx="4" fill="var(--c4)" opacity=".85"/>' for j in range(3))
        lit = card(cx, y, cw, ch, "color-mix(in srgb, var(--c4) 8%, var(--card))", "var(--c4)", 16, 2)
        box = (card(cx, y, cw, ch, "var(--card)", "var(--line)", 16, 1.5) + f'<g opacity="0">{beat("opacity", _b04_win(arrive[k]))}{lit}{full}</g>'
               + T(cx + 22, y + 38, name, s, "var(--white)", W6) + f'<g transform="translate({cx + cw - 32} {y + 32}) scale(1.3)">{_b04_db(0, 0)}</g>' + empty)
        if k:
            q = ask[k - 1]
            box += (f'<g opacity="0">{beat("opacity", [(0, 0), (q, 0), (q + .015, 1), (arrive[k] - .01, 1), (arrive[k], 0), (1, 0)])}'
                    f'<rect x="{cx + 12}" y="{y + 52}" width="{cw - 24}" height="56" rx="12" fill="var(--card)"/>'
                    + pill(cx + cw / 2, y + 80, sl["ask"], "var(--c3)", ctx, 22, cw - 30, "channel asks again") + '</g>')
        art.append(land(box, .3 + k * .15, .45, 14))
        y0, y1 = py - 30, y + ch / 2
        sg = 1 if y1 > y0 else -1
        d = f"M{px + 60} {y0} H{cx - 44} Q{cx - 26} {y0} {cx - 26} {y0 + sg * 18} V{y1 - sg * 18} Q{cx - 26} {y1} {cx - 8} {y1} H{cx - 4}"
        art.append(land(f'<path d="{d}" fill="none" stroke="var(--line)" stroke-width="1.6" stroke-dasharray="3 6"/>', .6 + k * .1, .4, 0)
                   + _b04_draw(d, "var(--c4)", tell[k], arrive[k], 2.2)
                   + f'<g opacity="0">{beat("opacity", _b04_trip(tell[k], arrive[k]))}{move(d, [(0, 0), (tell[k], 0), (arrive[k], 1), (1, 1)], D)}{token("var(--c4)", 7)}</g>')
    # the transfers, on the right edge: from one channel to the next
    for k, (a, b) in enumerate(xfer):
        y0, y1 = ys[k] + ch / 2, ys[k + 1] + ch / 2
        e = cx + cw
        d = f"M{e + 4} {y0} C{e + 50} {y0} {e + 50} {y1} {e + 12} {y1}"
        head = (f'<path d="M{e + 22} {y1 - 7} L{e + 10} {y1} L{e + 22} {y1 + 7}" fill="none" stroke="var(--c2)" stroke-width="2.2" '
                f'stroke-linecap="round" stroke-linejoin="round" opacity="0">{beat("opacity", _b04_win(b))}</path>')
        s = fit(max(_sm_wrap(_(sl["transfer"]), 9), key=len), 20, 130, "transfer label", floor=20)   # TCW wraps at 9: fit the longest line
        text.append(f'<g opacity="0">{beat("opacity", _b04_win(a))}'
                    + TCW(e + 105, f"{(y0 + y1) / 2 - 4:.0f}", sl["transfer"], 9, s, "var(--muted)", W6, 1.15) + '</g>')
        art.append(_b04_draw(d, "var(--c2)", a, b, 2.2) + head
                   + f'<g opacity="0">{beat("opacity", _b04_trip(a, b))}{move(d, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{token("var(--c2)", 6)}</g>')
    # the reimbursement waits for a document; the document was already in another system, behind a gap
    sy = ys[2] + ch + 115
    stx = zx + 190
    text.append(f'<g opacity="0">{beat("opacity", _b04_win(wait_at))}'
                + pill(stx, sy, sl["status"], "var(--c5)", ctx, 22, 330, "reimbursement status") + '</g>'
                + _b04_ping(stx, sy, 24, 80, "var(--c5)", (wait_at,), .1, .6))
    ox, oy, ow, oh = zx + 580, sy - 70, 230, 150       # the other system, to the right
    other = (card(ox, oy, ow, oh, "var(--dim)", "var(--line)", 14, 1.5) + f'<g transform="translate({ox + 40} {oy + 46}) scale(1.4)">{_b04_db(0, 0)}</g>'
             + f'<g transform="translate({ox + ow - 50} {oy + 50}) scale(1.3)">{_b04_doc(0, 0, "var(--c4)")}</g>'
             + TC(ox + ow / 2, oy + 124, sl["other"], fit(sl["other"], 22, ow - 20, "other system", floor=20), "var(--white)", W6))
    art.append(land(other, .9, .45, 14))
    text.append(f'<g opacity="0">{beat("opacity", _b04_win(stuck))}'
                + TCW(ox + ow / 2, oy + oh + 34, sl["there"], 18, 20, "var(--muted)", W6, 1.2) + '</g>')
    sx = stx + 210                                      # the missing document slot, and the reach that stops at the gap
    link_a, link_b = f"M{sx + 24} {sy} H{ox - 44}", f"M{ox - 22} {sy} H{ox - 2}"
    art.append(land(f'<path d="{link_a}" fill="none" stroke="var(--line)" stroke-width="1.6" stroke-dasharray="3 6"/>'
                    f'<path d="{link_b}" fill="none" stroke="var(--line)" stroke-width="1.6" stroke-dasharray="3 6"/>', 1.0, .4, 0))
    gx = ox - 33
    art.append(f'<g opacity="0">{beat("opacity", _b04_win(stuck))}'
               f'<path d="M{gx - 7} {sy - 7} L{gx + 7} {sy + 7} M{gx + 7} {sy - 7} L{gx - 7} {sy + 7}" stroke="var(--c5)" stroke-width="2.6" stroke-linecap="round"/></g>'
               + _b04_ping(gx, sy, 7, 34, "var(--c5)", (stuck,), .08, .7)
               + f'<g opacity="0">{beat("opacity", _b04_trip(*reach))}{move(link_a, [(0, 0), (reach[0], 0), (reach[1], 1), (1, 1)], D)}{token("var(--c5)", 6)}</g>'
               + f'<g opacity="0">{beat("opacity", _b04_win(wait_at))}<g transform="translate({sx} {sy}) scale(1.3)">{_b04_doc(0, 0, "var(--c5)", True)}</g></g>')
    # the wait: a bar that keeps growing from the first call, hotter once the refund waits
    wy, wx0, wx1 = zy + 850, zx + 30, zx + zw - 30
    s = fit(sl["wait"], 22, 260, "wait label", floor=20)
    grow = [(0, 0), (tell[0], 0), (.86, wx1 - wx0 - 48), (_b04_end, wx1 - wx0 - 48), (1, 0)]
    bar = (T(wx0, wy - 30, sl["wait"], s, "var(--muted)", W6)
           + f'<rect x="{wx0}" y="{wy - 5}" width="{wx1 - wx0}" height="10" rx="5" fill="var(--dim)"/>'
           + f'<rect x="{wx0}" y="{wy - 5}" width="0" height="10" rx="5" fill="var(--c3)">{beat("width", grow)}</rect>'
           + f'<rect x="{wx0}" y="{wy - 5}" width="0" height="10" rx="5" fill="var(--c5)" opacity="0">{beat("width", grow)}'
           + f'{beat("opacity", _b04_win(wait_at, f=.04))}</rect>')
    tip = (f'<g><animateTransform attributeName="transform" type="translate" values="{";".join(f"{v} 0" for _, v in grow)}" '
           f'keyTimes="{";".join(f"{t:.3f}" for t, _ in grow)}" dur="{D}s" repeatCount="indefinite"/>'
           f'<g transform="translate({wx0 + 24} {wy}) scale(1.3)"><circle r="17" fill="var(--ink)"/>{_b04_clock("var(--c3)")}</g></g>')
    art.append(land(bar + tip, .8, .45, 0))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "b04_tesis")
def sc_b04_tesis(sl, ctx):
    """The client calls and tells their case; the line transfers it and the next channel asks for it again, twice. The
    reimbursement then waits for a document that was already in another system, out of reach, and the wait grows.
    The frozen frame is the cost of dispersed data: one story copied three times, a waiting refund, a long wait."""
    if ORIENT() == "portrait":
        return _pb04_twin(sl, ctx)
    px, py = 915, 262                                   # the client
    cx, cw, ch = 1040, 300, 96                           # the channel cards
    ys = (160, 310, 460)
    tell = (.18, .37, .55)                               # when the client tells the story (again)
    arrive = tuple(t + .07 for t in tell)                # when it lands in the channel
    xfer = ((.29, .33), (.47, .51))                      # the transfers
    ask = (.34, .52)                                     # «¿Me cuenta su caso?»
    wait_at, reach, stuck = .64, (.66, .71), .71
    g = [glow(1190, 470, 440, "var(--brand)", .4)]
    # the client: a faceless figure with a phone; voice arcs each time the story is told
    voice = "".join(f'<g opacity="0">{beat("opacity", [(0, 0), (t, 0), (t + .01, 1), (t + .06, 1), (t + .07, 0), (1, 0)])}'
                    f'<path d="M{px + 40} {py - 64} Q{px + 50} {py - 50} {px + 40} {py - 36}" fill="none" stroke="var(--c4)" stroke-width="1.8" stroke-linecap="round"/>'
                    f'<path d="M{px + 50} {py - 72} Q{px + 64} {py - 50} {px + 50} {py - 28}" fill="none" stroke="var(--c4)" stroke-width="1.5" stroke-linecap="round" opacity=".6"/></g>'
                    for t in tell)
    client = (_user(px, py, 2.1, "var(--c2)")
              + f'<rect x="{px + 16}" y="{py - 72}" width="14" height="24" rx="3" fill="none" stroke="var(--c4)" stroke-width="1.6" transform="rotate(14 {px + 23} {py - 60})"/>'
              + TC(px, py + 62, sl["client"], fit(sl["client"], 17, 150, "client label"), "var(--white)", W6))
    g.append(land(client + voice, .1, .5, 0))
    # how many times the story is told: the first, then again, then again
    for k, (label, t) in enumerate(zip(sl["tells"], tell)):
        ty = 382 + k * 44
        s = fit(label, 15, 112, "retelling")
        row = (f'<g opacity=".35">{beat("opacity", _b04_win(t, lo=.35))}{_b04_talk(866, ty - 5, "var(--c4)" if k else "var(--c2)")}'
               + T(888, f"{ty + s * .36 - 5:.1f}", label, s, "var(--white)", W6) + '</g>')
        g.append(land(row, .5 + k * .1, .4, 10))
    # the three channels, each with its own system; the story lands in each one, identical
    for k, (y, name) in enumerate(zip(ys, sl["channels"])):
        s = fit(name, 18, cw - 70, "channel name")
        empty = "".join(f'<rect x="{cx + 20}" y="{y + 50 + j * 13}" width="{(cw - 40) * (.92, .7, .82)[j]:.0f}" height="6" rx="3" fill="none" '
                        f'stroke="var(--line)" stroke-width="1" stroke-dasharray="3 4"/>' for j in range(3))
        full = f'<g opacity="0">{beat("opacity", _b04_win(arrive[k]))}{_b04_story(cx + 20, y + 50, cw - 40, "var(--c4)", .85)}</g>'
        lit = (f'<g opacity="0">{beat("opacity", _b04_win(arrive[k]))}'
               f'{card(cx, y, cw, ch, "color-mix(in srgb, var(--c4) 8%, var(--card))", "var(--c4)", 16, 1.8)}</g>')
        box = (card(cx, y, cw, ch, "var(--card)", "var(--line)", 16, 1.5) + lit
               + T(cx + 20, y + 32, name, s, "var(--white)", W6) + _b04_db(cx + cw - 26, y + 28) + empty + full)
        if k:
            q = ask[k - 1]
            box += (f'<g opacity="0">{beat("opacity", [(0, 0), (q, 0), (q + .015, 1), (arrive[k] - .01, 1), (arrive[k], 0), (1, 0)])}'
                    f'<rect x="{cx + 12}" y="{y + 44}" width="{cw - 24}" height="44" rx="10" fill="var(--card)"/>'
                    + pill(cx + cw / 2, y + 66, sl["ask"], "var(--c3)", ctx, 16, cw - 30, "channel asks again") + '</g>')
        g.append(land(box, .3 + k * .15, .45, 14))
        y0, y1, sg = py - 20, y + ch / 2, (1 if y + ch / 2 > py - 20 else -1)
        d = f"M{px + 44} {y0} H{cx - 40} Q{cx - 24} {y0} {cx - 24} {y0 + sg * 16} V{y1 - sg * 16} Q{cx - 24} {y1} {cx - 8} {y1} H{cx - 4}"
        g.append(land(f'<path d="{d}" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 6"/>', .6 + k * .1, .4, 0)
                 + _b04_draw(d, "var(--c4)", tell[k], arrive[k], 1.8)
                 + f'<g opacity="0">{beat("opacity", _b04_trip(tell[k], arrive[k]))}{move(d, [(0, 0), (tell[k], 0), (arrive[k], 1), (1, 1)], D)}{token("var(--c4)", 6)}</g>')
    # the transfers, on the right edge: from one channel to the next
    for k, (a, b) in enumerate(xfer):
        y0, y1 = ys[k] + ch / 2, ys[k + 1] + ch / 2
        d = f"M{cx + cw + 4} {y0} C{cx + cw + 44} {y0} {cx + cw + 44} {y1} {cx + cw + 10} {y1}"
        head = (f'<path d="M{cx + cw + 18} {y1 - 6} L{cx + cw + 8} {y1} L{cx + cw + 18} {y1 + 6}" fill="none" stroke="var(--c2)" stroke-width="1.8" '
                f'stroke-linecap="round" stroke-linejoin="round" opacity="0">{beat("opacity", _b04_win(b))}</path>')
        s = fit(sl["transfer"], 15, 130, "transfer label")
        lab = (f'<g opacity="0">{beat("opacity", _b04_win(a))}'
               + T(cx + cw + 50, f"{(y0 + y1) / 2 + s * .36:.1f}", sl["transfer"], s, "var(--muted)", W6) + '</g>')
        g.append(_b04_draw(d, "var(--c2)", a, b, 1.8) + head + lab
                 + f'<g opacity="0">{beat("opacity", _b04_trip(a, b))}{move(d, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{token("var(--c2)", 5)}</g>')
    # the reimbursement waits for a document; the document was already in another system, behind a gap
    y3 = ys[2]
    g.append(f'<g opacity="0">{beat("opacity", _b04_win(wait_at))}'
             + pill(cx + cw / 2, y3 + ch + 34, sl["status"], "var(--c5)", ctx, 16, cw, "reimbursement status") + '</g>'
             + _b04_ping(cx + cw / 2, y3 + ch + 34, 20, 70, "var(--c5)", (wait_at,), .1, .6))
    ox, oy, ow, oh = 1415, 540, 140, 110                 # the other system, low and to the right
    other = (card(ox, oy, ow, oh, "var(--dim)", "var(--line)", 14, 1.5) + _b04_db(ox + 28, oy + 34)
             + _b04_doc(ox + ow - 40, oy + 38, "var(--c4)")
             + TC(ox + ow / 2, oy + 88, sl["other"], fit(sl["other"], 16, ow - 20, "other system"), "var(--white)", W6))
    g.append(land(other, .9, .45, 14))
    g.append(f'<g opacity="0">{beat("opacity", _b04_win(stuck))}'
             + TCW(ox + ow / 2, oy + oh + 26, sl["there"], 16, 15, "var(--muted)", W6, 1.2) + '</g>')
    # the missing document slot on the reimbursement, and the reach that stops at the gap
    sx, sy = cx + cw / 2 + 132, y3 + ch + 34
    link_a = f"M{sx + 20} {sy} H{ox - 50}"
    link_b = f"M{ox - 28} {sy} H{ox - 2}"
    g.append(land(f'<path d="{link_a}" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 6"/>'
                  f'<path d="{link_b}" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 6"/>', 1.0, .4, 0))
    gx = ox - 39
    g.append(f'<g opacity="0">{beat("opacity", _b04_win(stuck))}'
             f'<path d="M{gx - 6} {sy - 6} L{gx + 6} {sy + 6} M{gx + 6} {sy - 6} L{gx - 6} {sy + 6}" stroke="var(--c5)" stroke-width="2" stroke-linecap="round"/></g>'
             + _b04_ping(gx, sy, 6, 30, "var(--c5)", (stuck,), .08, .7)
             + f'<g opacity="0">{beat("opacity", _b04_trip(*reach))}{move(link_a, [(0, 0), (reach[0], 0), (reach[1], 1), (1, 1)], D)}{token("var(--c5)", 5)}</g>')
    g.append(f'<g opacity="0">{beat("opacity", _b04_win(wait_at))}{_b04_doc(sx, sy, "var(--c5)", True)}</g>')
    # the wait: a bar that keeps growing from the first call, hotter once the refund waits
    wy, wx0, wx1 = 770, 860, 1540
    s = fit(sl["wait"], 16, 200, "wait label")
    grow = [(0, 0), (tell[0], 0), (.86, wx1 - wx0 - 40), (_b04_end, wx1 - wx0 - 40), (1, 0)]
    bar = (T(wx0, wy - 20, sl["wait"], s, "var(--muted)", W6)
           + f'<rect x="{wx0}" y="{wy - 4}" width="{wx1 - wx0}" height="8" rx="4" fill="var(--dim)"/>'
           + f'<rect x="{wx0}" y="{wy - 4}" width="0" height="8" rx="4" fill="var(--c3)">{beat("width", grow)}</rect>'
           + f'<rect x="{wx0}" y="{wy - 4}" width="0" height="8" rx="4" fill="var(--c5)" opacity="0">{beat("width", grow)}'
           + f'{beat("opacity", _b04_win(wait_at, f=.04))}</rect>')
    tip = (f'<g><animateTransform attributeName="transform" type="translate" values="{";".join(f"{v} 0" for _, v in grow)}" '
           f'keyTimes="{";".join(f"{t:.3f}" for t, _ in grow)}" dur="{D}s" repeatCount="indefinite"/>'
           f'<g transform="translate({wx0 + 20} {wy})"><circle r="17" fill="var(--ink)"/>{_b04_clock("var(--c3)")}</g></g>')
    g.append(land(bar + tip, .8, .45, 0))
    return "".join(g), D, FREEZE


def _b06_icon(kind, col):
    """Thin line icons around 0,0: video call, nutrition (leaf), psychology (head and heart), vital signs (pulse)."""
    s = f'fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
    if kind == 0:
        return f'<rect x="-11" y="-7" width="15" height="14" rx="3" {s}/><path d="M4 -2 L11 -6 V6 L4 2" {s}/>'
    if kind == 1:
        return f'<path d="M-9 9 C-11 -3 -3 -10 10 -10 C10 3 3 10 -9 9 Z" {s}/><path d="M-9 9 L3 -3" {s}/>'
    if kind == 2:
        return (f'<path d="M-4 11 V6 C-10 4 -11 -2 -10 -5 C-8 -11 -2 -12 3 -11 C9 -9 11 -4 10 1 L12 5 H9 V9 H4 V11" {s}/>'
                f'<path d="M1 -1 C-1 -5 -5 -3 -3 0 L1 3 L5 0 C7 -3 3 -5 1 -1 Z" {s}/>')
    return f'<path d="M-12 1 H-6 L-3 -6 L1 8 L4 -2 L6 1 H12" {s}/>'


# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
def _pb06_twin(sl, ctx):
    """b06 on the 900x1600 stage: the still figure framed on top, the four services in a row under it, the door below
    them and the record behind it, the fork on the right. Same beats, same frozen frame: every service lit, the record
    complete, care on time, the wait drawn and dim."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    fx, (bx, by, bw, bh) = zx + zw / 2, (zx + 30, zy + 10, zw - 60, 250)
    lights = (.18, .27, .36, .45)
    done, go, ontime = .58, (.61, .70), .70
    ok = ctx.brand.c("dark.ok")
    art, text = [glow(fx, zy + 480, 460, "var(--brand)", .4)], []
    hud = "".join(f'<path d="M{x0} {y0 + dy * 26} V{y0} H{x0 + dx * 26}" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity=".8"/>'
                  for x0, y0, dx, dy in ((bx, by, 1, 1), (bx + bw, by, -1, 1), (bx, by + bh, 1, -1), (bx + bw, by + bh, -1, -1)))
    fig = TC(fx, by + 138, sl["figure"], fit(sl["figure"], 124, bw - 80, "sector figure"), "var(--c4)", W6)
    main, _sep, who = sl["label"].partition(" · ")
    lab = (TC(fx, by + 192, main, fit(main, 26, bw - 60, "sector label", floor=20), "var(--white)", W6)
           + (TC(fx, by + 226, who, fit(who, 21, bw - 60, "sector label source", floor=20), "var(--muted)", W6) if who else ""))
    art.append(land(hud, .1, .5, 0))
    text.append(land(fig + lab, .2, .5, 0))
    # the door: the app, its screen an open doorway (the desktop door, 1.15x)
    dx_, dy_, sc = zx + 130, zy + 440, 1.15
    door = (card(0, 0, 130, 250, "var(--card)", "var(--c2)", 22, 1.8)
            + '<rect x="50" y="12" width="30" height="5" rx="2.5" fill="var(--line)"/>'
            + '<rect x="32" y="56" width="66" height="116" rx="4" fill="none" stroke="var(--c4)" stroke-width="1.8"/>'
            + glow(65, 114, 80, "var(--c4)", .35)
            + f'<rect x="34" y="58" width="62" height="112" fill="color-mix(in srgb, var(--c4) 55%, var(--white))">{loop("opacity", ".45;.8;.45", 3.2)}</rect>'
            + '<path d="M32 56 L12 68 V184 L32 172 Z" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.6" stroke-linejoin="round"/>'
            + TC(65, 216, sl["door"], fit(sl["door"], 18, 106, "digital door", floor=18), "var(--white)", W6))
    art.append(pop(f'<g transform="scale({sc})">{door}</g>', dx_, dy_, .35, .45))
    ddx, ddy = dx_ + 65 * sc, dy_ + 114 * sc              # the doorway
    # behind the door: the record of the client, one slot per service
    rx, ry, rw, rh = zx + 400, zy + 480, 210, 190
    # the services in a row, lighting up in turn; each datum travels through the door to the record
    for k, (name, t) in enumerate(zip(sl["services"], lights)):
        ix, iy = zx + 105 + k * 203, zy + 330
        s = fit(name, 22, 190, "digital service", floor=20)
        svc = (f'<circle cx="{ix}" cy="{iy}" r="28" fill="var(--card)" stroke="var(--line)" stroke-width="1.5"/>'
               f'<g opacity="0">{beat("opacity", _b04_win(t))}<circle cx="{ix}" cy="{iy}" r="28" fill="color-mix(in srgb, var(--c4) 18%, var(--card))" stroke="var(--c4)" stroke-width="2"/>'
               f'<g transform="translate({ix} {iy}) scale(1.35)">{_b06_icon(k, "var(--c4)")}</g></g>'
               f'<g opacity="1">{beat("opacity", _b04_win(t, lo=1, hi=0))}<g transform="translate({ix} {iy}) scale(1.35)">{_b06_icon(k, "var(--c2)")}</g></g>'
               + f'<g opacity=".55">{beat("opacity", _b04_win(t, lo=.55))}' + TC(ix, iy + 58, name, s, "var(--white)", W6) + '</g>')
        art.append(land(svc, .4 + k * .12, .4, 10) + _b04_ping(ix, iy, 28, 56, "var(--c4)", (t,), .08, .7))
        sy_ = ry + 32 + k * 36
        d = f"M{ix} {iy + 30} C{ix} {iy + 110} {ddx:.0f} {ddy - 120:.0f} {ddx:.0f} {ddy:.0f} C{ddx + 110:.0f} {ddy:.0f} {rx - 60} {sy_} {rx + 20} {sy_}"
        a, b = t + .01, t + .09
        art.append(f'<g opacity="0">{beat("opacity", _b04_trip(a, b))}{move(d, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{token("var(--c4)", 6)}</g>')
    rec = (card(rx, ry, rw, rh, "var(--card)", "var(--line)", 14, 1.5)
           + f'<g opacity="0">{beat("opacity", _b04_win(done))}{card(rx, ry, rw, rh, "color-mix(in srgb, var(--c4) 10%, var(--card))", "var(--c4)", 14, 2)}</g>')
    for k, t in enumerate(lights):
        yy = ry + 25 + k * 36
        rec += (f'<rect x="{rx + 18}" y="{yy}" width="{rw - 36}" height="14" rx="7" fill="none" stroke="var(--line)" stroke-width="1" stroke-dasharray="3 4"/>'
                f'<rect x="{rx + 18}" y="{yy}" width="{rw - 36}" height="14" rx="7" fill="var(--c4)" opacity="0">{beat("opacity", _b04_win(t + .09, hi=.85))}</rect>')
    rec_lab = (TC(rx + rw / 2, ry - 16, sl["behind"], fit(sl["behind"], 20, 280, "behind the door", floor=20), "var(--muted)", W6)
               + TC(rx + rw / 2, ry + rh + 34, sl["record"], fit(sl["record"], 22, 260, "client record", floor=20), "var(--white)", W6))
    art.append(land(rec, .7, .45, 14) + _b04_ping(rx + rw / 2, ry + rh / 2, 70, 120, "var(--c4)", (done,), .1, .6))
    text.append(land(rec_lab, .7, .45, 14))
    # the fork: on time (up) when the record is complete; the wait (down) stays dim
    jx, jy, ex = rx + rw, ry + rh / 2, zx + 745
    uy, wy = ry + 10, ry + rh + 120
    up = f"M{jx} {jy} C{jx + 40} {jy} {ex - 60} {uy} {ex - 20} {uy}"
    down = f"M{jx} {jy} C{jx + 40} {jy} {ex - 60} {wy} {ex - 20} {wy}"
    art.append(land(f'<path d="{up}" fill="none" stroke="var(--line)" stroke-width="1.6" stroke-dasharray="3 6"/>'
                    f'<path d="{down}" fill="none" stroke="var(--line)" stroke-width="1.6" stroke-dasharray="3 6"/>', .9, .4, 0)
               + _b04_draw(up, ok, go[0], go[1], 2.4)
               + f'<g opacity="0">{beat("opacity", _b04_trip(*go))}{move(up, [(0, 0), (go[0], 0), (go[1], 1), (1, 1)], D)}{token(ok, 7)}</g>')
    care = (f'<circle cx="{ex}" cy="{uy}" r="18" fill="var(--card)" stroke="var(--line)" stroke-width="1.5"/>'
            f'<g opacity="0">{beat("opacity", _b04_win(ontime))}<circle cx="{ex}" cy="{uy}" r="18" fill="color-mix(in srgb, {ok} 22%, var(--card))" stroke="{ok}" stroke-width="2"/>'
            f'{check(ex, uy, .9, ok)}</g>'
            + f'<g opacity=".55">{beat("opacity", _b04_win(ontime, lo=.55))}'
            + TCW(ex, uy + 50, sl["ontime"], 15, 20, "var(--white)", W6, 1.2) + '</g>')
    wait = (f'<g transform="translate({ex} {wy}) scale(1.3)"><circle r="14" fill="var(--dim)" stroke="var(--line)" stroke-width="1.5"/>{_b04_clock("var(--muted)")}</g>'
            + TCW(ex, wy + 50, sl["late"], 15, 20, "var(--muted)", W6, 1.2))
    art.append(_b04_ping(ex, uy, 18, 48, ok, (ontime,), .1, .7))
    text.append(land(care, 1.0, .45, 10) + land(wait, 1.1, .45, 10))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "b06_sector")
def sc_b06_sector(sl, ctx):
    """The figure stays still, framed. Below, the digital door is open: teleconsultation, nutrition, psychology and vital
    signs light up in turn; each sends its datum through the door to the record behind it; when the record is complete,
    care arrives in time. The other branch, the wait, stays drawn and dim: what happens behind the door decides."""
    if ORIENT() == "portrait":
        return _pb06_twin(sl, ctx)
    fx, (bx, by, bw, bh) = 1190, (880, 110, 620, 250)
    lights = (.18, .27, .36, .45)                        # each service lights up
    done, go, ontime = .58, (.61, .70), .70
    ok = ctx.brand.c("dark.ok")
    g = [glow(1190, 470, 440, "var(--brand)", .4)]
    hud = "".join(f'<path d="M{x0} {y0 + dy * 22} V{y0} H{x0 + dx * 22}" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity=".8"/>'
                  for x0, y0, dx, dy in ((bx, by, 1, 1), (bx + bw, by, -1, 1), (bx, by + bh, 1, -1), (bx + bw, by + bh, -1, -1)))
    fig = TC(fx, by + 142, sl["figure"], fit(sl["figure"], 120, bw - 80, "sector figure"), "var(--c4)", W6)
    main, _sep, who = sl["label"].partition(" · ")
    lab = (TC(fx, by + 194, main, fit(main, 24, bw - 80, "sector label"), "var(--white)", W6)
           + (TC(fx, by + 226, who, fit(who, 18, bw - 80, "sector label source"), "var(--muted)", W6) if who else ""))
    g.append(land(hud, .1, .5, 0) + land(fig + lab, .2, .5, 0))
    # the door: the app, its screen an open doorway
    dx_, dy_, dw, dh = 1040, 440, 130, 250
    door = (card(dx_, dy_, dw, dh, "var(--card)", "var(--c2)", 22, 1.8)
            + f'<rect x="{dx_ + 50}" y="{dy_ + 12}" width="30" height="5" rx="2.5" fill="var(--line)"/>'
            + f'<rect x="{dx_ + 32}" y="{dy_ + 56}" width="66" height="116" rx="4" fill="none" stroke="var(--c4)" stroke-width="1.8"/>'
            + glow(dx_ + 65, dy_ + 114, 80, "var(--c4)", .35)
            + f'<rect x="{dx_ + 34}" y="{dy_ + 58}" width="62" height="112" fill="color-mix(in srgb, var(--c4) 55%, var(--white))">{loop("opacity", ".45;.8;.45", 3.2)}</rect>'
            + f'<path d="M{dx_ + 32} {dy_ + 56} L{dx_ + 12} {dy_ + 68} V{dy_ + 184} L{dx_ + 32} {dy_ + 172} Z" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.6" stroke-linejoin="round"/>'
            + TC(dx_ + dw / 2, dy_ + 214, sl["door"], fit(sl["door"], 18, dw - 24, "digital door"), "var(--white)", W6))
    g.append(pop(door, 0, 0, .35, .45))
    # the services around the door, lighting up in turn; each datum travels through the door to the record
    rx, ry, rw, rh = 1235, 520, 150, 150                 # the record behind the door
    for k, (name, t) in enumerate(zip(sl["services"], lights)):
        iy = 470 + k * 66
        s = fit(name, 16, 130, "digital service")
        svc = (f'<circle cx="868" cy="{iy}" r="21" fill="var(--card)" stroke="var(--line)" stroke-width="1.5"/>'
               f'<g opacity="0">{beat("opacity", _b04_win(t))}<circle cx="868" cy="{iy}" r="21" fill="color-mix(in srgb, var(--c4) 18%, var(--card))" stroke="var(--c4)" stroke-width="1.8"/></g>'
               f'<g transform="translate(868 {iy})">{_b06_icon(k, "var(--c2)")}</g>'
               f'<g opacity="0" transform="translate(868 {iy})">{beat("opacity", _b04_win(t))}{_b06_icon(k, "var(--c4)")}</g>'
               + f'<g opacity=".55">{beat("opacity", _b04_win(t, lo=.55))}' + T(898, f"{iy + s * .36:.1f}", name, s, "var(--white)", W6) + '</g>')
        g.append(land(svc, .4 + k * .12, .4, 10) + _b04_ping(868, iy, 21, 44, "var(--c4)", (t,), .08, .7))
        d = f"M892 {iy} C960 {iy} {dx_ - 20} {dy_ + 114} {dx_ + 65} {dy_ + 114} C{dx_ + 170} {dy_ + 114} {rx - 60} {ry + 28 + k * 30} {rx + 16} {ry + 28 + k * 30}"
        a, b = t + .01, t + .09
        g.append(f'<g opacity="0">{beat("opacity", _b04_trip(a, b))}{move(d, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{token("var(--c4)", 5)}</g>')
    # behind the door: the record of the client, one slot per service, and the fork it decides
    behind = fit(sl["behind"], 15, 200, "behind the door")
    rec = (T(rx, ry - 18, sl["behind"], behind, "var(--muted)", W6)
           + card(rx, ry, rw, rh, "var(--card)", "var(--line)", 14, 1.5)
           + f'<g opacity="0">{beat("opacity", _b04_win(done))}{card(rx, ry, rw, rh, "color-mix(in srgb, var(--c4) 10%, var(--card))", "var(--c4)", 14, 1.8)}</g>')
    for k, t in enumerate(lights):
        yy = ry + 22 + k * 30
        rec += (f'<rect x="{rx + 16}" y="{yy}" width="{rw - 32}" height="12" rx="6" fill="none" stroke="var(--line)" stroke-width="1" stroke-dasharray="3 4"/>'
                f'<rect x="{rx + 16}" y="{yy}" width="{rw - 32}" height="12" rx="6" fill="var(--c4)" opacity="0">{beat("opacity", _b04_win(t + .09, hi=.85))}</rect>')
    rec += TC(rx + rw / 2, ry + rh + 26, sl["record"], fit(sl["record"], 16, 200, "client record"), "var(--white)", W6)
    g.append(land(rec, .7, .45, 14) + _b04_ping(rx + rw / 2, ry + rh / 2, 60, 110, "var(--c4)", (done,), .1, .6))
    # the fork: on time (up) when the record is complete; the wait (down) stays dim
    jx, jy = rx + rw, ry + rh / 2
    up = f"M{jx} {jy} C{jx + 40} {jy} {jx + 40} {ry - 20} {jx + 62} {ry - 20}"
    down = f"M{jx} {jy} C{jx + 40} {jy} {jx + 40} {ry + rh + 50} {jx + 70} {ry + rh + 50}"
    g.append(land(f'<path d="{up}" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 6"/>'
                  f'<path d="{down}" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 6"/>', .9, .4, 0)
             + _b04_draw(up, ok, go[0], go[1], 2)
             + f'<g opacity="0">{beat("opacity", _b04_trip(*go))}{move(up, [(0, 0), (go[0], 0), (go[1], 1), (1, 1)], D)}{token(ok, 6)}</g>')
    ex = jx + 76
    care = (f'<circle cx="{ex + 14}" cy="{ry - 20}" r="14" fill="var(--card)" stroke="var(--line)" stroke-width="1.5"/>'
            f'<g opacity="0">{beat("opacity", _b04_win(ontime))}<circle cx="{ex + 14}" cy="{ry - 20}" r="14" fill="color-mix(in srgb, {ok} 22%, var(--card))" stroke="{ok}" stroke-width="1.8"/>'
            f'{check(ex + 14, ry - 20, .7, ok)}</g>'
            + f'<g opacity=".55">{beat("opacity", _b04_win(ontime, lo=.55))}'
            + TCW(ex + 14, ry - 70, sl["ontime"], 16, 16, "var(--white)", W6, 1.2) + '</g>')
    wait = (f'<g transform="translate({ex + 14} {ry + rh + 50})"><circle r="14" fill="var(--dim)" stroke="var(--line)" stroke-width="1.5"/>{_b04_clock("var(--muted)")}</g>'
            + TCW(ex + 14, ry + rh + 88, sl["late"], 13, 16, "var(--muted)", W6, 1.2))
    g.append(land(care, 1.0, .45, 10) + land(wait, 1.1, .45, 10)
             + _b04_ping(ex + 14, ry - 20, 14, 40, ok, (ontime,), .1, .7))
    return "".join(g), D, FREEZE

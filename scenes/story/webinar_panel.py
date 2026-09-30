"""The two live scenes of a webinar-panel deck: the panel's questions (one slide stays up for forty minutes while the
presenter taps the question in play) and the reflections of the day (revealed live at the synthesis), with the survey.

Both reuse the tap mechanism of module/deck.js (the one of «¿Dónde están hoy?»): a tap on a [data-pick] marks it
.picked and puts .has-pick on its svg; a tap on a [data-reveal] adds .revealed and never removes it; keys 1-9 do the
same on the Nth of the active slide. deck.css dims the unpicked [data-dim] rows, hides [data-hop] once something is
picked, and shows every question and every revealed card under reduced motion and in print. The engine is untouched.
Aliases: panel-questions -> wp_preguntas, reflections-live -> wp_reflexiones (assets/ext.py). A webinar never
names them «tensiones»: the close gathers what the panel left to think about (references/copy-rules.md).
"""
from aula.svg import wrap as _wp_wrap

_WP_COLS = ("var(--c1)", "var(--c2)", "var(--c3)", "var(--accent)", "var(--c5)")


def _wp_box(sl):
    """The art's box for the slide's layout: `top` → the band x 96-1504, y 396-826; else (left) x 840-1540, y 110-820."""
    return (96, 396, 1408, 430) if sl.get("layout") == "top" else (840, 110, 700, 710)


def _wp_chars(s, size, room):
    """The widest wrap (characters per line) at which every line of s fits room at size, measured bold."""
    t, f = _(str(s)), current_factor()
    for chars in range(max(8, int(room / (size * .42))), 7, -1):
        if all(bold_width(line, size, f) <= room for line in _wp_wrap(t, chars)):
            return chars
    return 8


def _wp_text(x, y_mid, s, room, height, sizes=(24, 22, 20, 18, 16, 15), fill="var(--white)", lines_max=3):
    """s wrapped into room, at the largest size whose lines fit height (never under 15 px), centered on y_mid."""
    for z in sizes:
        chars = _wp_chars(s, z, room)
        n = len(_wp_wrap(_(str(s)), chars))
        if n <= lines_max and n * z * 1.25 <= height:
            break
    top = y_mid - (n - 1) * z * 1.25 / 2 + z * .36
    return TCW(f"{x:.1f}", f"{top:.1f}", s, chars, z, fill, W6, 1.25, "start")


# ---------------------------------------------------------------- panel-questions: one slide for the whole panel
@register("scene", "wp_preguntas")
def sc_wp_preguntas(sl, ctx):
    """The panel's questions (3-7) in a column, numbered; the last `reserve` are drawn dashed with their label. While
    nobody taps, a frame visits each question in turn (the ambient loop, 12 s, data-hop). The presenter taps the
    question in play (or presses its number): it lights with a ring and «En curso» and the rest dim; it stays lit until
    another is tapped. Frozen frame: every question readable, the frame on one of them."""
    if ORIENT() == "portrait":
        return _wqp_preguntas(sl, ctx)
    qs = sl["questions"]
    if not 3 <= len(qs) <= 7:
        raise ValueError(f"panel-questions takes 3 to 7 questions, not {len(qs)}")
    x, y, w, h = _wp_box(sl)
    n, gap = len(qs), 14
    rh = min(118, (h - gap * (n - 1)) / n)
    reserve, tag, live = int(sl.get("reserve", 0)), sl.get("reserve_label", "Reserva"), sl.get("live", "En curso")
    tag_w = bold_width(_(str(tag)), 15, current_factor()) + 44 if reserve else 0
    g, rows = [glow(x + w / 2, y + h / 2, max(w, h) * .6, "var(--brand)", .35)], []
    for k, q in enumerate(qs):
        yy, spare, col = y + k * (rh + gap), k >= n - reserve, _WP_COLS[k % len(_WP_COLS)]
        mid = yy + rh / 2
        room = w - 96 - (tag_w + 16 if spare else 24)
        c = card(x, yy, w, rh, "var(--card)", "var(--line)", 16, 1.5, 'stroke-dasharray="7 7"' if spare else "")
        c += f'<rect x="{x}" y="{yy + 14:.1f}" width="4" height="{rh - 28:.1f}" rx="2" fill="{col}"/>'
        c += (f'<circle cx="{x + 44}" cy="{mid:.1f}" r="21" fill="{col}"/>'
              + TC(x + 44, f"{mid + 7:.1f}", str(k + 1), 20, ctx.brand.on(col), W6))
        c += _wp_text(x + 80, mid, q, room, rh - 20, fill="var(--muted)" if spare else "var(--white)")
        if spare:
            c += pill(x + w - 16 - tag_w / 2, mid, tag, "var(--dim)", ctx, 15, tag_w, "panel reserve")
        # marked by the presenter's tap (deck.css: .pick-ring shows on .picked, the unpicked [data-dim] rows dim)
        c += (f'<g class="pick-ring"><rect x="{x - 4}" y="{yy - 4:.1f}" width="{w + 8}" height="{rh + 8:.1f}" rx="20" fill="none" '
              f'stroke="var(--c4)" stroke-width="3"/><rect x="{x - 10}" y="{yy - 10:.1f}" width="{w + 20}" height="{rh + 20:.1f}" '
              f'rx="26" fill="none" stroke="var(--c4)" stroke-width="1.5">{loop("stroke-opacity", ".05;.6;.05", 2.4)}</rect>'
              + pill(x + w - 96, yy, live, "var(--c4)", ctx, 15, 170, "panel live") + '</g>')
        c += f'<rect x="{x}" y="{yy:.1f}" width="{w}" height="{rh:.1f}" rx="16" fill="var(--ink)" opacity="0"/>'
        rows.append(f'<g data-pick="{k}" data-dim="">{c}</g>')
    g.append(seq(rows, .1, .5, 16))
    # the ambient ask: a frame visits each question in turn until the presenter taps one
    hop = (f'<rect x="{x - 4}" y="{y - 4}" width="{w + 8}" height="{rh + 8:.1f}" rx="20" fill="none" stroke="var(--c4)" stroke-width="2">'
           f'<animateTransform attributeName="transform" type="translate" values="{";".join(f"0 {k * (rh + gap):.1f}" for k in range(n))}" '
           f'keyTimes="{";".join(f"{k / n:.3f}" for k in range(n))}" dur="{D}s" repeatCount="indefinite" calcMode="discrete"/>'
           f'{loop("stroke-opacity", ".25;1;.25", 2.4)}</rect>')
    g.append(land(f'<g data-hop="">{hop}</g>', 1.2, .4, 0))
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- reflections-live: the synthesis, revealed live, and the survey
@register("scene", "wp_reflexiones")
def sc_wp_reflexiones(sl, ctx):
    """Three face-down cards, numbered, whose edges light in turn (the ambient loop, 12 s): the reflections noted during
    the panel. The presenter taps each one (or presses 1-3) as they say it: it turns and shows its text (by default «Se
    anota en vivo»), with a line that keeps writing under it. Below, the survey with its label and where to answer.
    Under reduced motion and in print every card shows its face. Frozen frame: the three faces and the survey."""
    if ORIENT() == "portrait":
        return _wqp_reflexiones(sl, ctx)
    cards = list(sl.get("cards") or ["Se anota en vivo"] * 3)[:3]
    label, survey = sl.get("label", "Reflexión"), sl.get("survey")
    x, y, w, h = _wp_box(sl)
    top = sl.get("layout") == "top"
    sh = 110 if survey else 0
    ch = (h - sh - (24 if survey else 0)) if top else (h - sh - (24 if survey else 0) - 2 * 20) / 3
    cw = (w - 2 * 24) / 3 if top else w
    g, parts = [glow(x + w / 2, y + h / 2, max(w, h) * .6, "var(--brand)", .35)], []
    for k, text in enumerate(cards):
        cx_, cy_ = (x + k * (cw + 24), y) if top else (x, y + k * (ch + 20))
        col = _WP_COLS[k % len(_WP_COLS)]
        num = f"0{k + 1}"
        face = (T(cx_ + 24, cy_ + 40, num, 18, "var(--c4)", W6)
                + _wp_text(cx_ + 24, cy_ + ch / 2 + 8, text, cw - 48, ch - 76, (24, 22, 20, 18, 16, 15)))
        write = (f'<path d="M{cx_ + 24} {cy_ + ch - 22:.1f} H{cx_ + cw - 24:.1f}" pathLength="1" stroke-dasharray="1" fill="none" '
                 f'stroke="{col}" stroke-width="2" stroke-linecap="round">'
                 f'{beat("stroke-dashoffset", [(0, 1), (.08 + k * .1, 1), (.4 + k * .1, 0), (.96, 0), (1, 1)])}</path>')
        cover = (card(cx_, cy_, cw, ch, "var(--dim)", col, 16, 1.5, 'stroke-dasharray="7 7"')
                 + f'<rect x="{cx_}" y="{cy_}" width="{cw:.1f}" height="{ch:.1f}" rx="16" fill="none" stroke="{col}" stroke-width="3">'
                 + beat("stroke-opacity", [(0, .1), (k / 3, .1), (k / 3 + .06, 1), (k / 3 + .26, 1), (k / 3 + .32, .1), (1, .1)]) + '</rect>'
                 + T(cx_ + 24, cy_ + 40, num, 18, "var(--c4)", W6)
                 + TC(f"{cx_ + cw / 2:.1f}", f"{cy_ + ch / 2 + 9:.1f}", f"{label} {k + 1}", fit(f"{label} {k + 1}", 26, cw - 48, "reflection label"),
                      "var(--white)", W6))
        c = (card(cx_, cy_, cw, ch, "var(--card)", col, 16, 2) + f'<g class="reveal-on">{face}{write}</g>'
             + f'<g class="reveal-off">{cover}</g>'
             + f'<rect x="{cx_}" y="{cy_}" width="{cw:.1f}" height="{ch:.1f}" rx="16" fill="var(--ink)" opacity="0"/>')
        parts.append(f'<g data-reveal="{k}">{c}</g>')
    if survey:
        s_label, s_text = survey
        sy = y + h - sh
        lw = min(260, bold_width(_(str(s_label)), 18, current_factor()) + 44)
        box = (card(x, sy, w, sh, "var(--card)", "var(--c4)", 18, 2)
               + f'<rect x="{x}" y="{sy}" width="{w}" height="{sh}" rx="18" fill="none" stroke="var(--c4)" stroke-width="4" opacity=".5">'
               + loop("stroke-opacity", ".1;.8;.1", 3) + '</rect>'
               + pill(x + 24 + lw / 2, sy + sh / 2, s_label, "var(--c4)", ctx, 18, lw, "survey label")
               + _wp_text(x + 48 + lw, sy + sh / 2, s_text, w - lw - 96, sh - 24, (22, 20, 18, 16, 15), lines_max=2)
               + f'<circle cx="{x + w - 30}" cy="{sy + sh / 2}" r="7" fill="var(--c4)">{loop("opacity", "1;.2;1", 2)}</circle>')
        parts.append(box)
    g.append(seq(parts, .1, .5, 16))
    return "".join(g), D, FREEZE

"""World «papel» (paper dream): a shared visual kit, in the pack's colors, so every slide of a deck reads as one world.
Promoted from the fidelización Demo Day deck (cierre-training, 2026-09); the harvested scenes that draw with it are
in story/fidelizacion_s01_15.py (aliases paper-hero … lema-signer).

- warm ivory paper (PX_PAPER, a color-mix of the pack's white with a touch of c4), cut edges from a fixed seed, one
  shadow (a single offset copy under each sheet, same direction everywhere: PX_SH);
- ink text on paper (PX_INK = var(--ink)), labels never under 15 px (PX_MIN), thin strokes (1.4-2 px), faceless people;
- the magenta ribbon (var(--accent)) as the one continuous thread;
- recurring objects: the paper plane, the post-it with its pin, the three route icons of a strategy map (px_icon: chat
  with cards, lens, envelope with gear), the sealed envelope, the lens, the gear;
- brands on stage: the client's logo (px_logo_client, only with the client's permission) and the signer's portrait
  (px_signer). The Amaris mark is never drawn here: the engine's lockup (cover) or footer is the slide's one Amaris mark.

Loaded by ext.py after lib.py and before story/*.py; a deck's <work>/scenes/s00_img.py (scripts/new.py --logo/--photo)
then sets PX_LOGO_CLIENT, PX_LOGO_CLIENT_RATIO and PX_PHOTO_SIGNER. Helpers are px_*; never redefine them in a deck.
"""
from aula.svg import wrap

PX_PAPER = "color-mix(in srgb, var(--white) 90%, var(--c4))"          # warm ivory
PX_PAPER_2 = "color-mix(in srgb, var(--white) 82%, var(--c3))"        # sand, a second sheet
PX_PAPER_LILA = "color-mix(in srgb, var(--white) 80%, var(--c2))"     # lilac sheet
PX_EDGE = "color-mix(in srgb, var(--ink) 18%, var(--white))"           # paper edge line
PX_SHADOW = "color-mix(in srgb, var(--ink) 70%, transparent)"          # the one shadow
PX_INK = "var(--ink)"
PX_MUTED_INK = "color-mix(in srgb, var(--ink) 72%, var(--white))"      # secondary text on paper (AA on ivory)
PX_RIBBON = "var(--accent)"
PX_POSTIT = "color-mix(in srgb, var(--c4) 70%, var(--white))"          # yellow post-it
PX_POSTIT_RED = "var(--c5)"
PX_SH = (7, 9)                                                          # shadow offset, the same everywhere
PX_MIN = 15                                                             # the smallest label on paper, px

# set by <work>/scenes/s00_img.py (new.py --logo / --photo); empty = not drawn
PX_LOGO_CLIENT = ""            # data URI of the client's logo (SVG preferred, PNG accepted), never recolored
PX_LOGO_CLIENT_RATIO = .32     # its height / width (the SVG viewBox or the PNG header)
PX_PHOTO_SIGNER = ""           # data URI of the signer's portrait


def _px_rand(seed):
    """A tiny deterministic generator (same seed, same edges on every build)."""
    s = [seed * 9301 + 49297]

    def r():
        s[0] = (s[0] * 9301 + 49297) % 233280
        return s[0] / 233280
    return r


def px_sheet_path(x, y, w, h, seed=1, jag=2.2):
    """A rectangle with hand-cut edges: a few points per side, jittered by a fixed seed."""
    r = _px_rand(seed)
    pts = []
    n = 5
    for k in range(n):
        pts.append((x + w * k / n, y + (r() - .5) * jag))
    for k in range(n):
        pts.append((x + w + (r() - .5) * jag, y + h * k / n))
    for k in range(n):
        pts.append((x + w - w * k / n, y + h + (r() - .5) * jag))
    for k in range(n):
        pts.append((x + (r() - .5) * jag, y + h - h * k / n))
    return "M" + " L".join(f"{a:.1f} {b:.1f}" for a, b in pts) + " Z"


def px_sheet(x, y, w, h, fill=PX_PAPER, seed=1, edge=True, shadow=True):
    """One paper sheet: its single shadow, then the cut sheet."""
    d = px_sheet_path(x, y, w, h, seed)
    sh = f'<path d="{d}" transform="translate({PX_SH[0]} {PX_SH[1]})" fill="{PX_SHADOW}"/>' if shadow else ""
    st = f'stroke="{PX_EDGE}" stroke-width="1.2"' if edge else 'stroke="none"'
    return sh + f'<path d="{d}" fill="{fill}" {st} stroke-linejoin="round"/>'


def px_lines(x, y, w, n=3, gap=18, color=None, op=".45", width=6):
    """Text lines drawn as thin bars on paper."""
    color = color or PX_MUTED_INK
    return "".join(f'<rect x="{x}" y="{y + k * gap}" width="{w * (.92 if k % 2 == 0 else .64):.0f}" height="{width}" '
                   f'rx="{width / 2}" fill="{color}" opacity="{op}"/>' for k in range(n))


def px_text(x, y, s, size=18, where="paper label", room=300, fill=PX_INK, anchor="start", bold=True):
    """A label on paper, ink colored, fitted to its room and never under 15 px (a label that does not fit at 15 is
    reported by the build instead of shrinking out of reach)."""
    z = fit(s, max(size, PX_MIN), room, where, floor=PX_MIN)
    ex = W6 if bold else ""
    if anchor == "middle":
        return TC(f"{x:.1f}", f"{y:.1f}", s, z, fill, ex)
    return T(f"{x:.1f}", f"{y:.1f}", s, z, fill, ex)


def px_ribbon(d, width=3, begin=.1, dur=.9, extra=""):
    """The magenta ribbon, drawing itself once (markup holds the full stroke)."""
    return trace(d, PX_RIBBON, width, begin, dur, extra)


def px_pin(x, y, color="var(--accent)"):
    """A push pin seen from above, at (x, y)."""
    return (f'<circle cx="{x + 2}" cy="{y + 3}" r="8" fill="{PX_SHADOW}"/>'
            f'<circle cx="{x}" cy="{y}" r="8" fill="{color}"/><circle cx="{x - 2.5}" cy="{y - 2.5}" r="2.4" fill="var(--white)" opacity=".7"/>')


def px_postit(x, y, w, h, fill=PX_POSTIT, seed=3, rot=0, label=None, size=17, fg=PX_INK):
    """A post-it (square sheet, slightly rotated), optionally with one label wrapped in lines of at least 15 px: the
    longest word sets the size, the rest wraps, the block is centered on the sheet."""
    lab = ""
    if label:
        room = w - 24
        z = fit(max(str(label).split(), key=len), max(size, PX_MIN), room, "post-it word", floor=PX_MIN)
        chars = max(6, int(room / (z * .56)))
        n = len(wrap(_(str(label)), chars))
        ty = y + h / 2 - (n - 1) * z * .6 + z * .34
        lab = TCW(f"{x + w / 2:.1f}", f"{ty:.1f}", label, chars, z, fg, W6, 1.2)
    return (f'<g transform="rotate({rot} {x + w / 2:.1f} {y + h / 2:.1f})">'
            + px_sheet(x, y, w, h, fill, seed) + lab + '</g>')


def px_plane(x, y, s=1.0, fill=PX_PAPER):
    """The paper plane, nose to the right, centered near (x, y)."""
    sw = f'stroke="{PX_EDGE}" stroke-width="{1.4 / s:.2f}" stroke-linejoin="round"'
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-52 10 L60 -18 L-18 34 Z" transform="translate(7 9)" fill="{PX_SHADOW}"/>'
            f'<path d="M-60 0 L60 -18 L-14 12 Z" fill="{fill}" {sw}/>'
            f'<path d="M-14 12 L60 -18 L-18 34 Z" fill="{PX_PAPER_2}" {sw}/>'
            f'<path d="M-14 12 L-22 22" stroke="{PX_EDGE}" stroke-width="{1.4 / s:.2f}"/></g>')


def px_envelope(x, y, w=150, h=96, sealed=True, fill=PX_PAPER):
    """A paper envelope with its flap; sealed = a magenta wax dot."""
    seal = f'<circle cx="{x + w / 2}" cy="{y + h * .52}" r="11" fill="{PX_RIBBON}"/>' if sealed else ""
    return (px_sheet(x, y, w, h, fill, 11)
            + f'<path d="M{x} {y} L{x + w / 2} {y + h * .56} L{x + w} {y}" fill="none" stroke="{PX_EDGE}" stroke-width="1.4"/>'
            + seal)


def px_gear(x, y, r=14, color=None):
    color = color or PX_INK
    teeth = "".join(f'<rect x="-2.6" y="{-r - 5}" width="5.2" height="7" rx="1" fill="{color}" transform="rotate({a})"/>' for a in range(0, 360, 45))
    return (f'<g transform="translate({x} {y})">{teeth}<circle r="{r}" fill="none" stroke="{color}" stroke-width="2"/>'
            f'<circle r="{r * .35:.1f}" fill="none" stroke="{color}" stroke-width="2"/></g>')


def px_lens(x, y, r=28, color=None):
    color = color or PX_INK
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="var(--white)" fill-opacity=".35" stroke="{color}" stroke-width="2.4"/>'
            f'<path d="M{x + r * .72:.1f} {y + r * .72:.1f} L{x + r * 1.5:.1f} {y + r * 1.5:.1f}" stroke="{color}" stroke-width="6" stroke-linecap="round"/>')


# ---------------------------------------------------------------- the strategy map: three route icons (slides 3-7)
def px_icon(k, x, y, s=1.0, lit=False):
    """Route stop k of the strategy map, drawn on a round paper token centered at (x, y):
    0 explicar = a chat bubble with three small cards; 1 revisar = the lens; 2 automatizar = envelope with a gear.
    lit = the stop has been walked (magenta ring). Slides 3 to 7 use the same drawing so the audience recognizes it."""
    ring = PX_RIBBON if lit else PX_EDGE
    base = (f'<circle cx="{x + 5}" cy="{y + 7}" r="{38 * s:.1f}" fill="{PX_SHADOW}"/>'
            f'<circle cx="{x}" cy="{y}" r="{38 * s:.1f}" fill="{PX_PAPER}" stroke="{ring}" stroke-width="{3 if lit else 1.4}"/>')
    g = f'<g transform="translate({x} {y}) scale({s})">'
    if k == 0:
        g += (f'<path d="M-20 -14 H20 Q24 -14 24 -10 V6 Q24 10 20 10 H-4 L-12 18 V10 H-20 Q-24 10 -24 6 V-10 Q-24 -14 -20 -14 Z" '
              f'fill="none" stroke="{PX_INK}" stroke-width="2" stroke-linejoin="round"/>'
              + "".join(f'<rect x="{-15 + j * 11}" y="-7" width="8" height="11" rx="1.5" fill="{c}"/>'
                        for j, c in enumerate(("var(--c1)", "var(--c3)", "var(--accent)"))))
    elif k == 1:
        g += (f'<circle cx="-4" cy="-4" r="13" fill="none" stroke="{PX_INK}" stroke-width="2.4"/>'
              f'<path d="M5.5 5.5 L16 16" stroke="{PX_INK}" stroke-width="5" stroke-linecap="round"/>'
              f'<path d="M-10 -4 L-6 0 L2 -9" fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>')
    else:
        g += (f'<rect x="-22" y="-12" width="34" height="24" rx="2" fill="none" stroke="{PX_INK}" stroke-width="2"/>'
              f'<path d="M-22 -12 L-5 2 L12 -12" fill="none" stroke="{PX_INK}" stroke-width="2"/>'
              + px_gear(15, 11, 7, "var(--accent)"))
    return base + g + '</g>'


# ---------------------------------------------------------------- brands on stage
def px_logo_client(cx, top, w, chip="var(--white)"):
    """The client's official logo, w wide, centered on cx, on a paper chip whose top edge is at top, with the same
    padding on every side (.35 x the logo height) so it sits optically centered. Never recolored; "" without a logo.
    The chip is w + 2 pad wide and h + 2 pad tall (px_logo_size)."""
    if not PX_LOGO_CLIENT:
        return ""
    h, pad = px_logo_size(w)
    x = cx - w / 2
    return (px_sheet(x - pad, top, w + 2 * pad, h + 2 * pad, chip, 21)
            + f'<image href="{PX_LOGO_CLIENT}" x="{x:.1f}" y="{top + pad:.1f}" width="{w}" height="{h:.1f}" '
              f'preserveAspectRatio="xMidYMid meet"/>')


def px_logo_size(w):
    """(h, pad) of the client's logo drawn w wide: h from its own ratio, pad balanced around it."""
    h = w * PX_LOGO_CLIENT_RATIO
    return h, round(h * .35)


def px_signer(x, y, d, name, role, ctx, sizes=(20, 17), room=None, floor=PX_MIN):
    """Who signs the deck (a trainer, a manager): the portrait in a round paper frame, name and role under it. Without a
    photo, a faceless figure on the same frame. sizes, room and floor size the two labels (the portrait twin passes
    larger ones; the defaults are the desktop's)."""
    r = d / 2
    room = d + 160 if room is None else room
    zn, zr = sizes
    cid = "px-signer-clip"
    face = (f'<image href="{PX_PHOTO_SIGNER}" x="{x}" y="{y}" width="{d}" height="{d}" clip-path="url(#{cid})" '
            f'preserveAspectRatio="xMidYMid slice"/>' if PX_PHOTO_SIGNER else
            f'<g clip-path="url(#{cid})"><circle cx="{x + r}" cy="{y + r * .78:.1f}" r="{r * .34:.1f}" fill="{PX_PAPER_2}" '
            f'stroke="{PX_EDGE}" stroke-width="1.2"/><path d="M{x + r * .28:.1f} {y + d} Q{x + r * .28:.1f} {y + r * 1.22:.1f} '
            f'{x + r} {y + r * 1.22:.1f} Q{x + r * 1.72:.1f} {y + r * 1.22:.1f} {x + r * 1.72:.1f} {y + d} Z" fill="{PX_PAPER_2}" '
            f'stroke="{PX_EDGE}" stroke-width="1.2"/></g>')
    return (f'<defs><clipPath id="{cid}"><circle cx="{x + r}" cy="{y + r}" r="{r}"/></clipPath></defs>'
            f'<circle cx="{x + r + 6}" cy="{y + r + 8}" r="{r + 6}" fill="{PX_SHADOW}"/>'
            f'<circle cx="{x + r}" cy="{y + r}" r="{r + 6}" fill="{PX_PAPER}" stroke="{PX_EDGE}" stroke-width="1.2"/>' + face
            + TC(f"{x + r:.1f}", f"{y + d + 40 + (zn - 20) * 1.2:.1f}", name, fit(name, zn, room, "signer name", floor=floor), "var(--white)", W6)
            + TC(f"{x + r:.1f}", f"{y + d + 66 + (zn - 20) * 1.2 + (zr - 17) * 1.2:.1f}", role, fit(role, zr, room, "signer role", floor=floor), "var(--muted)"))


# ---------------------------------------------------------------- placeholder until a slide gets its own scene
@register("scene", "p00_paper")
def sc_p00_paper(sl, ctx):
    """A stack of two sheets and a plane that breathe: a placeholder while benches build the real scenes."""
    g = [land(px_sheet(900, 200, 560, 420, PX_PAPER_2, 5), .1, .5),
         land(px_sheet(940, 240, 560, 420, PX_PAPER, 6) + px_lines(990, 300, 440, 6, 34), .3, .5)]
    g.append(f'<g>{bob(0, -8, 6)}{px_plane(1230, 170, .9)}</g>')
    return "".join(g), D, FREEZE

#!/usr/bin/env python3
"""The World in One Page -- 23 November 2026.

Draws a 1024x1024 newspaper front page summing up the world news of
Monday 23 November 2026 and writes it to /output/entry.png.

Standard library plus Pillow only. No network, no files read, no time
or randomness anywhere, so two runs produce byte-identical output.
"""

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

PAPER = (248, 244, 232)
INK = (18, 18, 18)
SOFT_INK = (58, 58, 58)
RED = (178, 34, 28)
BLUE = (29, 78, 137)
TEAL = (14, 110, 105)
ORANGE = (198, 96, 12)
PURPLE = (96, 52, 128)
GREEN = (46, 110, 46)
RULE = (18, 18, 18)
CARD_BG = (255, 252, 244)

FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
]


def load_font(bold, size):
    """Best available font at the given size; falls back to the default."""
    for path in FONT_PATHS:
        is_bold = "Bold" in path
        if is_bold != bold:
            continue
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default(size)


def wrap(draw, text, font, max_width):
    """Greedy word wrap measured with the real font metrics."""
    lines = []
    current = ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_centered(draw, y, text, font, fill=INK):
    width = draw.textlength(text, font=font)
    draw.text(((W - width) / 2, y), text, font=font, fill=fill)
    return y + font.size + 4


def draw_rule(draw, y, thickness=2, x0=36, x1=988):
    draw.rectangle([x0, y, x1, y + thickness - 1], fill=RULE)


def draw_kicker(draw, x, y, text, color, size=20):
    font = load_font(True, size)
    draw.text((x, y), text, font=font, fill=color)
    return y + size + 6


def draw_headline(draw, x, y, text, max_width, size=27, max_lines=2):
    font = load_font(True, size)
    lines = wrap(draw, text, font, max_width)[:max_lines]
    for line in lines:
        draw.text((x, y), line, font=font, fill=INK)
        y += size + 5
    return y


def draw_deck(draw, x, y, text, max_width, size=20, max_lines=3):
    font = load_font(False, size)
    lines = wrap(draw, text, font, max_width)[:max_lines]
    for line in lines:
        draw.text((x, y), line, font=font, fill=SOFT_INK)
        y += size + 5
    return y


def draw_globe(draw, cx, cy, radius):
    """A simple cracked globe: blue sea, green land, a red crack."""
    draw.ellipse(
        [cx - radius, cy - radius, cx + radius, cy + radius],
        fill=(66, 135, 200),
        outline=INK,
        width=3,
    )
    # Land masses as rough blobs (fixed coordinates, deterministic).
    blobs = [
        [(cx - 78, cy - 58), (cx - 30, cy - 78), (cx - 8, cy - 42),
         (cx - 42, cy - 18), (cx - 74, cy - 30)],
        [(cx + 12, cy - 68), (cx + 62, cy - 60), (cx + 74, cy - 22),
         (cx + 40, cy - 8), (cx + 14, cy - 30)],
        [(cx - 52, cy + 18), (cx - 6, cy + 10), (cx + 4, cy + 52),
         (cx - 34, cy + 66), (cx - 60, cy + 44)],
        [(cx + 34, cy + 30), (cx + 66, cy + 34), (cx + 58, cy + 66),
         (cx + 28, cy + 58)],
    ]
    for blob in blobs:
        draw.polygon(blob, fill=(74, 160, 92))
    # Red crack across the globe.
    crack = [
        (cx - 88, cy - 84), (cx - 52, cy - 46), (cx - 70, cy - 8),
        (cx - 34, cy + 22), (cx - 52, cy + 58), (cx - 18, cy + 88),
    ]
    draw.line(crack, fill=RED, width=5, joint="curve")
    # Small flame marks at the crack's ends.
    for fx, fy in [(cx - 88, cy - 84), (cx - 18, cy + 88)]:
        draw.polygon(
            [(fx, fy - 14), (fx - 9, fy + 4), (fx, fy - 2),
             (fx + 9, fy + 4)],
            fill=(232, 120, 20),
        )


def build_poster():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # Double outer frame.
    draw.rectangle([14, 14, W - 15, H - 15], outline=INK, width=3)
    draw.rectangle([22, 22, W - 23, H - 23], outline=INK, width=1)

    # ---- Masthead -------------------------------------------------
    y = 36
    name_font = load_font(True, 50)
    draw_centered(draw, y, "THE WORLD IN ONE PAGE", name_font)
    y = 36 + 50 + 10
    draw_rule(draw, y, 3)
    y += 10
    date_font = load_font(True, 26)
    draw_centered(draw, y, "MONDAY, 23 NOVEMBER 2026", date_font)
    y += 26 + 10
    draw_rule(draw, y, 1)
    y += 8
    tag_font = load_font(False, 17)
    draw_centered(
        draw, y,
        "COP31 collapses  ·  Gulf strikes  ·  Baltic ablaze  ·  House 258",
        tag_font, fill=SOFT_INK,
    )
    y += 17 + 10
    draw_rule(draw, y, 3)

    # ---- Lead story: COP31 ---------------------------------------
    y += 14
    lead_x = 36
    lead_w = 620
    y = draw_kicker(draw, lead_x, y, "CLIMATE — COP31, ANTALYA", RED, 20)
    y = draw_headline(
        draw, lead_x, y,
        "COP31 COLLAPSES: NO DEAL ON FOSSIL FUELS",
        lead_w, size=38, max_lines=3,
    )
    y = draw_deck(
        draw, lead_x, y + 4,
        "UN climate talks end Sunday with no agreement after the final "
        "draft drops every mention of fossil fuels. The EU and others "
        "reject the text.",
        lead_w, size=19, max_lines=3,
    )

    # Globe illustration on the right of the lead.
    draw_globe(draw, 830, 278, 105)
    cap_font = load_font(True, 17)
    caption = "THE LONGEST COP"
    cw = draw.textlength(caption, font=cap_font)
    draw.text((830 - cw / 2, 390), caption, font=cap_font, fill=RED)
    caption2 = "NEXT: ADDIS ABABA 2027"
    cw2 = draw.textlength(caption2, font=cap_font)
    draw.text((830 - cw2 / 2, 410), caption2, font=cap_font, fill=RED)

    # ---- Story grid: two columns, three rows --------------------
    grid_top = 440
    draw_rule(draw, grid_top - 12, 2)
    col_w = 464
    col_xs = [36, 524]
    row_h = 150
    stories = [
        ("GULF — BAHRAIN", RED,
         "IRAN HITS U.S. BASES IN BAHRAIN",
         "The IRGC says missiles and drones hit two U.S. Patriot radars "
         "at Al-Riffa and Awali. Bahrain reports a fire at a civilian "
         "plant on Sitra; two hurt."),
        ("BALTIC — GULF OF FINLAND", BLUE,
         "RUSSIAN SHIP ABLAZE AFTER DRONE HIT",
         "Struck by drones on Saturday, the Sparta II still burns off "
         "Finland; all 16 crew evacuated. Finland says Ukraine was "
         "likely behind it."),
        ("UKRAINE — KYIV OBLAST", ORANGE,
         "DRONE HITS SUPERMARKET NEAR KYIV",
         "Three killed and 15 wounded, including three children, in a "
         "Russian drone strike on Sunday evening. Zelenskyy urges U.S. "
         "Patriot transfers."),
        ("UNITED STATES — MIDTERMS", PURPLE,
         "DEMOCRATS CLINCH 258 HOUSE SEATS",
         "Chuck Hubbard beats Rep. Virginia Foxx in North Carolina — "
         "the largest House majority since 1992, up 44 seats. Four "
         "races still uncalled."),
        ("ASIA — DELHI & WELLINGTON", TEAL,
         "NEPAL'S PM IN DELHI; INDIA'S 720/9",
         "Balendra Shah holds talks with Modi on a state visit to "
         "India. In Wellington, India posts a record 720 for 9 declared "
         "against New Zealand."),
        ("SUDAN — KHARTOUM", GREEN,
         "DRONE HITS U.N. BUILDING IN KHARTOUM",
         "A drone strike hits a U.N. building on Sunday. The U.N. "
         "humanitarian coordinator calls the risk to aid workers "
         "\"unacceptable\"."),
    ]
    for i, (kicker, color, headline, deck) in enumerate(stories):
        col = i % 2
        row = i // 2
        x = col_xs[col]
        top = grid_top + row * row_h
        # Thin divider between the two columns.
        if col == 1:
            draw.line([506, top + 4, 506, top + row_h - 14], fill=(180, 172, 150), width=1)
        sy = draw_kicker(draw, x, top, kicker, color, 17)
        sy = draw_headline(draw, x, sy, headline, col_w, size=24, max_lines=2)
        draw_deck(draw, x, sy, deck, col_w, size=17, max_lines=3)

    # ---- In brief --------------------------------------------------
    brief_top = grid_top + 3 * row_h + 8
    draw_rule(draw, brief_top, 2)
    y = brief_top + 12
    y = draw_kicker(draw, 36, y, "IN BRIEF", RED, 18)
    y = draw_deck(
        draw, 36, y,
        "Indonesia factory fire: 7 dead, 50 missing  •  Thousands march "
        "in Lisbon over living costs  •  South Korea's education minister "
        "resigns in an AI cheating scandal.",
        952, size=16, max_lines=2,
    )

    # ---- Footer ----------------------------------------------------
    foot_y = H - 46
    draw_rule(draw, foot_y, 1)
    foot_font = load_font(False, 15)
    draw_centered(
        draw, foot_y + 9,
        "The World in One Page — Monday, 23 November 2026",
        foot_font, fill=SOFT_INK,
    )
    return img


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    poster = build_poster()
    poster.save(out_path, format="PNG")
    size = os.path.getsize(out_path)
    print("wrote %s (%d bytes, %dx%d)" % (out_path, size, W, H))
    if size > 1048576:
        print("WARNING: output exceeds the 1 MiB entry limit")
    if poster.size != (W, H):
        print("WARNING: output is not %dx%d" % (W, H))


if __name__ == "__main__":
    main()

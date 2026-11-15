#!/usr/bin/env python3
"""Minimal runnable integrity check for HRL International Version 3.0 rollout."""

import os
import re
import urllib.parse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")


def main():
    with open(INDEX_PATH, encoding="utf-8") as f:
        html = f.read()

    # 1. Strict 100% zero-emoji policy on main page
    emoji_re = re.compile(
        "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF\U0000FE0F]+",
        flags=re.UNICODE,
    )
    emojis = [m.group() for m in emoji_re.finditer(html)]
    assert not emojis, f"Disallowed emojis found: {emojis[:5]}"

    # 2. Guard against shell-stripped USD prices, broken external chart, and private research leakage
    for bad in ["/ </span>", "/ )", "/ ,500+", "/ ,400)", "ghchart.rshah.org", "banco-plata", "amd-security"]:
        assert bad not in html, f"Forbidden or stale pattern present: {bad!r}"

    # 3. Verify all local relative assets resolve on disk
    for m in re.finditer(r'(?:src|href)="([^"]+)"', html):
        url = m.group(1)
        if url.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "#")):
            continue
        rel = urllib.parse.unquote(url.split("?")[0].split("#")[0])
        if rel:
            assert os.path.exists(os.path.join(BASE_DIR, rel)), f"Missing local target: {rel}"

    # 4. Symmetrical placing counts & Version 3.0 anchors
    assert "Version 3.0" in html and "id=\"hardware-silicon\"" in html and "id=\"v3-systems\"" in html
    assert html.count('class="directorate-card"') == 16, "directorate-grid should contain 16 cards (4x4)"
    assert html.count('class="crypto-product-card') == 37, "crypto grid should contain 37 cards (1 wide + 36)"
    assert html.count('class="mr-card"') == 6, "mr-cards-grid should contain 6 cards (3x2)"

    hw_sec = html.split('id="hardware-silicon"')[1].split("</section>")[0]
    assert hw_sec.count('class="sector-card"') == 4, "#hardware-silicon 2x2 matrix must contain 4 cards"

    sec_sec = html.split('id="sectors"')[1].split("</section>")[0]
    assert sec_sec.count('class="sector-card"') == 6, "#sectors must contain 6 cards"

    v3_sec = html.split('id="v3-systems"')[1].split("</section>")[0]
    assert v3_sec.count('class="sector-card"') == 6, "#v3-systems must contain 6 cards"

    # 5. Restored USD prices in #rate-card
    rate_sec = html.split('id="rate-card"')[1].split("</section>")[0]
    for price in ["&#36;35", "&#36;60", "&#36;85", "&#36;120", "&#36;2,500", "&#36;450", "&#36;800", "&#36;1,400"]:
        assert price in rate_sec, f"Missing restored USD pricing token: {price}"

    # 6. Balanced section/div structure and CSS braces
    assert html.count("<section") == html.count("</section>"), "Unbalanced <section> tags"
    assert html.count("<div") == html.count("</div>"), "Unbalanced <div> tags"
    style_block = html.split("<style>")[1].split("</style>")[0]
    assert style_block.count("{") == style_block.count("}"), "Unbalanced CSS braces in <style>"

    # 7. Updated metrics & sitemap lastmod
    achievements_sec = html.split('id="achievements"')[1].split("</section>")[0]
    assert "52+" not in achievements_sec and "77+" in achievements_sec
    assert "6,149+" in html and "Agensi Store (38 Skills Live)" in html

    with open(SITEMAP_PATH, encoding="utf-8") as f:
        sitemap = f.read()
    assert "<lastmod>2026-11-15</lastmod>" in sitemap

    print("[PASS] HRL International Version 3.0 rollout verified (structure, symmetry, USD pricing, assets, 0 emojis).")


if __name__ == "__main__":
    main()

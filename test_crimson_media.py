import os
import re
from html.parser import HTMLParser
from pathlib import Path

def test_crimson_red_media_integration():
    repo_dir = Path("/Users/pavankumars/.gemini/antigravity/scratch/hrl-international-website-")
    index_file = repo_dir / "index.html"
    assert index_file.exists(), "index.html must exist"
    html_content = index_file.read_text(encoding="utf-8")

    # 1. Verify Image Asset
    img_path = repo_dir / "assets" / "apoorvi-vijay-ceo.jpg"
    assert img_path.exists(), "CEO portrait assets/apoorvi-vijay-ceo.jpg must exist"
    assert img_path.stat().st_size > 10000, "CEO portrait file must be non-empty"

    # 2. Verify Profile Signature Glass Lens CSS and Specular Rim
    assert ".crm-avatar-wrapper" in html_content, ".crm-avatar-wrapper class missing"
    assert ".crm-avatar-img" in html_content, ".crm-avatar-img class missing"
    assert ".crm-verified-badge" in html_content, ".crm-verified-badge class missing"

    # Ensure profile avatar rim has the signature conic specular glass rim and drop shadow
    wrapper_before_match = re.search(r'\.crm-avatar-wrapper::before[^{]*\{([^}]+)\}', html_content)
    assert wrapper_before_match, ".crm-avatar-wrapper::before CSS definition missing"
    assert "conic-gradient" in wrapper_before_match.group(1), "Conic glass gradient missing"
    assert "drop-shadow" in wrapper_before_match.group(1), "Drop shadow on glass rim missing"

    # 3. Verify Section & Navigation
    assert 'id="crimson-red-media"' in html_content, "Section #crimson-red-media missing"
    assert 'href="#crimson-red-media"' in html_content, "Navigation link to #crimson-red-media missing"

    # 4. Verify Executive Leadership & Title
    assert "Apoorvi Vijay" in html_content, "Apoorvi Vijay executive spotlight missing"
    assert "Chief Executive Officer" in html_content, "CEO designation missing"
    assert "HRL Crimson Red Media" in html_content, "Sub-brand title missing"

    # 5. Verify the 4 Core Media Hub Verticals
    assert "Brand Films &amp; Commercials" in html_content or "Brand Films & Commercials" in html_content, "Vertical 1 missing"
    assert "Digital Media &amp; Post-Production" in html_content or "Digital Media & Post-Production" in html_content, "Vertical 2 missing"
    assert "Visual Design &amp; Campaigns" in html_content or "Visual Design & Campaigns" in html_content, "Vertical 3 missing"
    assert "Press / Media Kit" in html_content, "Vertical 4 missing"

    # 6. Verify CTAs
    assert "Explore Media Portfolio" in html_content, "Explore Media Portfolio CTA missing"
    assert "Inquire for Media Production" in html_content, "Inquire for Media Production CTA missing"

    # 7. Verify Zero Emoji in the subsection
    section_match = re.search(r'<section class="apple-crimson-media-section".*?</section>', html_content, re.DOTALL)
    assert section_match, "Could not extract apple-crimson-media-section"
    section_html = section_match.group(0)
    emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
    emojis = emoji_pattern.findall(section_html)
    assert len(emojis) == 0, f"Zero-emoji policy violation: found emojis {emojis}"

    # 8. HTML parser check
    class StrictParser(HTMLParser):
        pass
    parser = StrictParser()
    parser.feed(html_content)

    print("[PASS] All HRL Crimson Red Media assertions successfully verified.")

if __name__ == "__main__":
    test_crimson_red_media_integration()

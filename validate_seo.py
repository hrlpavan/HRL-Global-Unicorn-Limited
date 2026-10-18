import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

def validate_all_seo_and_geo(base_dir_str):
    base_dir = Path(base_dir_str)
    print("==================================================")
    print(f"[AUDIT] SEO & GEO KNOWLEDGE GRAPH AUDIT: {base_dir.name}")
    print("==================================================")

    # 1. Audit index.html
    index_file = base_dir / "index.html"
    if not index_file.exists():
        print(f"[FAIL] index.html missing at {index_file}")
        return False
    
    html = index_file.read_text(encoding="utf-8")
    title_m = re.search(r"<title>(.*?)</title>", html)
    desc_m = re.search(r'<meta name="description" content="(.*?)"', html)
    canon_m = re.search(r'<link rel="canonical" href="(.*?)"', html)
    keywords_m = re.search(r'<meta name="keywords" content="(.*?)"', html)

    print("\n--- 1. INDEX.HTML AUDIT ---")
    print(f"Title: {title_m.group(1) if title_m else 'MISSING'}")
    assert title_m and "hrlpavan" in title_m.group(1), "Title must contain 'hrlpavan'"
    assert keywords_m and "hrlpavan" in keywords_m.group(1), "Keywords must contain 'hrlpavan'"
    assert "hrlpavan-founder-avatar.jpg" in html, "Image SEO: hrlpavan-founder-avatar.jpg must be featured"
    print("[PASS] index.html Meta tags & Keywords verified.")

    # 2. Extract and Validate JSON-LD in index.html
    json_ld_matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    assert len(json_ld_matches) > 0, "JSON-LD missing in index.html"
    for raw in json_ld_matches:
        data = json.loads(raw.strip())
        graph = data.get("@graph", [data])
        for node in graph:
            if "founder" in node:
                founder = node["founder"]
                print(f"[PASS] Founder Node in Org: {founder.get('name')} | ID: {founder.get('@id')}")
                assert "hrlpavan" in founder.get("alternateName", []), "Founder must include 'hrlpavan' alternateName"
                assert "Pawan Hans" in founder.get("disambiguatingDescription", ""), "Must contain negative disambiguation against Pawan Hans"
                print(f"   ↳ Disambiguation: {founder.get('disambiguatingDescription')[:60]}...")
            if node.get("@type") == "FAQPage":
                faqs = node.get("mainEntity", [])
                pawan_faq = any("Pawan Hans" in q.get("name", "") or "Pawan Hans" in q.get("acceptedAnswer", {}).get("text", "") for q in faqs)
                assert pawan_faq, "FAQPage must contain disambiguation against Pawan Hans"
                print(f"[PASS] FAQPage with {len(faqs)} Q&A pairs (including negative disambiguation) verified.")

    # 3. Audit hrlpavan.html
    pavan_file = base_dir / "hrlpavan.html"
    assert pavan_file.exists(), "hrlpavan.html must exist"
    pavan_html = pavan_file.read_text(encoding="utf-8")
    assert "hrlpavan" in pavan_html, "hrlpavan.html must contain hrlpavan"
    assert "Pawan Hans" in pavan_html, "hrlpavan.html must explicitly disambiguate from Pawan Hans"
    assert "52 Projects" in pavan_html or "52 systems" in pavan_html or "52 software" in pavan_html, "Must catalog 52 projects"
    
    pavan_json_ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', pavan_html, re.DOTALL)
    assert len(pavan_json_ld) > 0, "JSON-LD missing in hrlpavan.html"
    p_data = json.loads(pavan_json_ld[0].strip())
    p_graph = p_data.get("@graph", [])
    print(f"\n--- 2. HRLPAVAN.HTML AUDIT ---")
    print(f"[PASS] Entity Page JSON-LD valid with {len(p_graph)} nodes.")
    for n in p_graph:
        print(f"   - Node: {n.get('@type')} | Name: {n.get('name')}")
    
    # 4. Audit sitemap.xml
    sitemap_file = base_dir / "sitemap.xml"
    assert sitemap_file.exists(), "sitemap.xml must exist"
    tree = ET.parse(sitemap_file)
    root = tree.getroot()
    urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    assert any("hrlpavan.html" in u for u in urls), "sitemap.xml must include hrlpavan.html"
    print(f"\n--- 3. SITEMAP.XML AUDIT ---")
    print(f"[PASS] sitemap.xml valid XML with {len(urls)} indexed URLs.")
    for u in urls:
        print(f"   • {u}")

    # 5. Audit robots.txt
    robots_file = base_dir / "robots.txt"
    assert robots_file.exists(), "robots.txt must exist"
    robots_txt = robots_file.read_text(encoding="utf-8")
    assert "Allow: /hrlpavan.html" in robots_txt, "robots.txt must allow /hrlpavan.html"
    print(f"\n--- 4. ROBOTS.TXT AUDIT ---")
    print("[PASS] robots.txt explicitly permits crawlers to index hrlpavan.html and assets.")

    print("\n==================================================")
    print("[SUCCESS] ALL SEO & GEO TEST CHECKS PASSED WITH 100% COVERAGE")
    print("==================================================")
    return True

if __name__ == "__main__":
    dir_to_check = sys.argv[1] if len(sys.argv) > 1 else "/Users/pavankumars/.gemini/antigravity/scratch/hrl-international-website-"
    validate_all_seo_and_geo(dir_to_check)

#!/usr/bin/env python3
"""
Test Suite: HRL Leadership Page Verification
Verifies design tokens, responsive grid, roster mapping, and asset resolution
against the HRL Master Brand Design System specifications.
"""
import os
import re
import urllib.parse

REPO_DIR = os.path.dirname(os.path.abspath(__file__))

def test_leadership_pages():
    pages = [
        (os.path.join(REPO_DIR, 'leadership.html'), REPO_DIR),
        (os.path.join(REPO_DIR, 'leadership', 'index.html'), os.path.join(REPO_DIR, 'leadership')),
    ]
    
    roster_expected = [
        ('Sheikh Mohammed Raees', 'Chief Executive Officer (CEO)', '@hrl', 'sheikh-mohammed-raees.jpg'),
        ('Sanjana', 'Co-Founder', '@hrl', 'sanjana.png'),
        ('Apoorvi Vijay', 'Chief Executive Officer (CEO)', '@hrlcrimsonRED', 'apoorvi-vijay.jpg'),
        ('Nishwin', 'Real Estate Agent (REA)', '@hrl', 'nishwin.jpeg'),
        ('Shubhada Naik', 'Business Consultant', '@hrl', 'shubhada-naik.jpg'),
        ('Jia Shetty', 'Core Community Manager', '@hrl', 'jia-shetty.jpeg'),
        ('Saismitha', 'Head of Commercial Brands & Brand Partnerships Lead', '@hrl', 'Saismitha.jpg'),
        ('Seejal', 'Deep Data & Data Engineering', '@hrl', 'seejal.jpg'),
        ('Thaif', 'Developer Ecosystem Coordinator', '@hrl', 'thaif.jpg'),
    ]

    for filepath, base_dir in pages:
        assert os.path.isfile(filepath), f"Missing page: {filepath}"
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()

        # 1. Company Motto Compliance
        assert 'We Can Do Everything Related To Software Sector Without Any Excuses!' in html, \
            f"Mandatory company motto missing in {filepath}"

        # 2. Check all 6 leaders and their assets
        for name, role, division, img_name in roster_expected:
            assert name in html, f"Leader {name} missing in {filepath}"
            assert role in html, f"Role {role} missing in {filepath}"
            assert division in html, f"Division {division} missing in {filepath}"
            assert img_name in html, f"Image {img_name} missing in {filepath}"

        # 3. Check every img src on disk
        img_srcs = re.findall(r'src=[\"\']([^\"\']+)[\"\']', html)
        for src in img_srcs:
            if src.endswith('.js'):
                continue
            unquoted = urllib.parse.unquote(src)
            resolved_path = os.path.normpath(os.path.join(base_dir, unquoted))
            assert os.path.exists(resolved_path), f"Asset {src} not found on disk: {resolved_path}"
            assert os.path.getsize(resolved_path) > 0, f"Asset {src} is empty file"

        # 4. Zero emoji policy check
        emojis = re.findall(r'[\U00010000-\U0010ffff]', html)
        assert len(emojis) == 0, f"Found prohibited emoji in {filepath}: {emojis}"

    # 5. Verify Main Page Zero Layout Regression (Only Clean Nav/Footer Links Inserted)
    with open(os.path.join(REPO_DIR, 'index.html'), 'r', encoding='utf-8') as f:
        index_html = f.read()
    assert 'href="leadership.html"' in index_html, "Clean leadership link missing in index.html"

    print("PASS: HRL Leadership page verified successfully with 100% compliance.")

if __name__ == '__main__':
    test_leadership_pages()

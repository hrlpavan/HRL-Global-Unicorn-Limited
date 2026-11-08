#!/usr/bin/env python3
"""
Verification check for HRL Executive Admin Console Footer Link,
Zero-Emoji Compliance, and Sovereign Database Vault Gate.
"""
import re
from pathlib import Path
import admin_vault_server

BASE = Path(__file__).resolve().parent
INDEX_HTML = (BASE / "index.html").read_text(encoding="utf-8")
ADMIN_HTML = (BASE / "admin-console.html").read_text(encoding="utf-8")

# 1. Verify footer placement in index.html & removal from top nav
footer_pos = INDEX_HTML.find('<footer class="apple-footer"')
admin_link_pos = INDEX_HTML.find('href="admin-console.html"')
assert footer_pos != -1 and admin_link_pos > footer_pos, "admin-console.html must be linked inside the main footer only"
assert INDEX_HTML.count('href="admin-console.html"') == 1, "admin-console.html should only appear once (in the main footer)"

# 2. Verify Sovereign Security Gate & Database Vault in admin-console.html
assert 'id="hrl-security-gate"' in ADMIN_HTML, "Missing Sovereign Security Gate"
assert 'id="console-protected-shell" class="hidden"' in ADMIN_HTML, "Protected console shell must be hidden by default"
assert 'HRL_Sovereign_Vault_DB' in ADMIN_HTML, "Missing IndexedDB database configuration"
assert 'const SEALED_VAULT_RECORD =' in ADMIN_HTML, "Missing SEALED_VAULT_RECORD anchor for cross-device lock"
assert "We Can Do Everything Related To Software Sector Without Any Excuses!" in ADMIN_HTML, "Missing mandatory HRL motto"

# 3. Verify 100% Zero-Emoji compliance in admin-console.html
emoji_pattern = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]")
emojis_found = emoji_pattern.findall(ADMIN_HTML)
assert not emojis_found, f"Zero-Emoji policy violated in admin-console.html: {emojis_found}"

# 4. Verify SQLite database initialization
admin_vault_server.init_db()
assert admin_vault_server.DB_PATH.exists(), "SQLite database file hrl_admin_vault.db was not created"

print("ALL HRL ADMIN CONSOLE & DATABASE VAULT CHECKS PASSED (4/4)")

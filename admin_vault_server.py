#!/usr/bin/env python3
"""
HRL International — Sovereign Admin Vault SQLite Server
Persists executive admin credentials (salted SHA-256 / PBKDF2 hashes) into SQLite
(`hrl_admin_vault.db`) and automatically seals `SEALED_VAULT_RECORD` inside
`admin-console.html` so shared links are permanently locked to the founder.
"""
import json
import re
import sqlite3
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "hrl_admin_vault.db"
CONSOLE_HTML_PATH = BASE_DIR / "admin-console.html"
PORT = 8788


def init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS admin_credentials (
                id TEXT PRIMARY KEY,
                email_hash TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()


def get_founder_record() -> dict | None:
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(
            "SELECT email_hash, password_hash, salt, created_at FROM admin_credentials WHERE id = 'founder_master'"
        ).fetchone()
    if not row:
        return None
    return {
        "id": "founder_master",
        "emailHash": row[0],
        "passwordHash": row[1],
        "salt": row[2],
        "createdAt": row[3],
        "locked": True,
    }


def seal_console_html(record: dict) -> bool:
    if not CONSOLE_HTML_PATH.exists():
        return False
    html = CONSOLE_HTML_PATH.read_text(encoding="utf-8")
    sealed_json = json.dumps(record, separators=(",", ":"))
    updated, count = re.subn(
        r"const SEALED_VAULT_RECORD = .*?;",
        f"const SEALED_VAULT_RECORD = {sealed_json};",
        html,
        count=1,
    )
    if count > 0:
        CONSOLE_HTML_PATH.write_text(updated, encoding="utf-8")
        return True
    return False


def save_founder_record(email_hash: str, password_hash: str, salt: str) -> dict:
    existing = get_founder_record()
    if existing:
        raise ValueError("Vault is already locked to the registered founder.")
    created_at = datetime.now(timezone.utc).isoformat()
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT INTO admin_credentials (id, email_hash, password_hash, salt, created_at)
            VALUES ('founder_master', ?, ?, ?, ?)
            """,
            (email_hash, password_hash, salt, created_at),
        )
        conn.commit()
    record = get_founder_record()
    seal_console_html(record)
    return record


class VaultHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def _send_cors(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Private-Network", "true")

    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self._send_cors()
        self.end_headers()

    def do_GET(self) -> None:
        if self.path.startswith("/api/vault/status"):
            rec = get_founder_record()
            payload = json.dumps({"locked": rec is not None, "record": rec}).encode("utf-8")
            self.send_response(200)
            self._send_cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(payload)
            return
        super().do_GET()

    def do_POST(self) -> None:
        if self.path.startswith("/api/vault/register"):
            length = int(self.headers.get("Content-Length", "0"))
            body = json.loads(self.rfile.read(length).decode("utf-8") or "{}")
            email_hash = str(body.get("emailHash", "")).strip()
            password_hash = str(body.get("passwordHash", "")).strip()
            salt = str(body.get("salt", "")).strip()
            if not email_hash or not password_hash or not salt:
                self.send_response(400)
                self._send_cors()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Missing cryptographic hash parameters"}).encode("utf-8"))
                return
            try:
                rec = save_founder_record(email_hash, password_hash, salt)
                self.send_response(200)
                self._send_cors()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True, "record": rec}).encode("utf-8"))
            except ValueError as exc:
                self.send_response(409)
                self._send_cors()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(exc), "record": get_founder_record()}).encode("utf-8"))
            return
        self.send_response(404)
        self.end_headers()

    def log_message(self, fmt: str, *args) -> None:
        return


if __name__ == "__main__":
    init_db()
    print(f"HRL Sovereign Vault SQLite Server active on http://127.0.0.1:{PORT}")
    ThreadingHTTPServer(("127.0.0.1", PORT), VaultHandler).serve_forever()

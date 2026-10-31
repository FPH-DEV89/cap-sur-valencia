#!/usr/bin/env python3
"""Ping IndexNow pour le site Cap sur Valencia (Python 3 stdlib, sans dépendance).

Lit `sitemap.xml` à la racine du dépôt, en extrait les <loc> et soumet la liste à
IndexNow. La clé est lue depuis le fichier de vérification déployé à la racine
(nom de fichier = clé, contenu = clé) : aucune clé en dur dans le code.

    python3 scripts/indexnow_ping.py            # poste réellement
    python3 scripts/indexnow_ping.py --dry-run  # affiche le JSON, ne poste rien

Un endpoint en échec n'interrompt pas le script : le code de sortie ne vaut 1 que
si le sitemap est illisible, vide, ou si la clé est introuvable.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP = os.path.join(ROOT, "sitemap.xml")
HOST = "capsurvalencia.fr"
ENDPOINTS = ("https://api.indexnow.org/indexnow", "https://www.bing.com/indexnow")
USER_AGENT = "HermesSEO/1.0"
TIMEOUT = 30
KEY_RE = re.compile(r"^[0-9a-f]{32}$")


def read_sitemap_urls() -> list[str]:
    """Extrait les <loc> du sitemap, dans l'ordre du document."""
    try:
        tree = ET.parse(SITEMAP)
    except (OSError, ET.ParseError) as exc:
        sys.exit(f"ERREUR : sitemap.xml illisible ({exc})")
    urls = []
    for node in tree.getroot().iter():
        if node.tag.rsplit("}", 1)[-1] == "loc" and node.text:
            url = node.text.strip()
            if url and url not in urls:
                urls.append(url)
    if not urls:
        sys.exit("ERREUR : aucun <loc> dans sitemap.xml")
    return urls


def find_key() -> tuple[str, str]:
    """Retourne (clé, keyLocation) d'après le fichier de vérification déployé."""
    for name in sorted(os.listdir(ROOT)):
        stem, ext = os.path.splitext(name)
        if ext != ".txt" or not KEY_RE.match(stem):
            continue
        with open(os.path.join(ROOT, name), encoding="utf-8") as fh:
            content = fh.read().strip()
        if content == stem:
            return stem, f"https://{HOST}/{name}"
    sys.exit("ERREUR : fichier de clé IndexNow introuvable à la racine du dépôt")


def build_payload(urls: list[str], key: str, key_location: str) -> dict:
    return {
        "host": HOST,
        "key": key,
        "keyLocation": key_location,
        "urlList": urls,
    }


def post(endpoint: str, body: bytes) -> None:
    """Poste sur un endpoint ; toute erreur est reportée, jamais propagée."""
    req = urllib.request.Request(
        endpoint,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            code = resp.status
            note = "OK" if code in (200, 202) else "INATTENDU (attendu 200/202)"
            print(f"  {endpoint} -> HTTP {code} ({note})")
    except urllib.error.HTTPError as exc:
        detail = exc.read()[:200].decode("utf-8", "replace").strip()
        note = "OK" if exc.code in (200, 202) else "ÉCHEC"
        print(f"  {endpoint} -> HTTP {exc.code} ({note}) {detail}".rstrip())
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        print(f"  {endpoint} -> ÉCHEC réseau : {exc}")


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    urls = read_sitemap_urls()
    key, key_location = find_key()
    payload = build_payload(urls, key, key_location)
    body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")

    print(f"IndexNow — {HOST}")
    print(f"  URLs extraites du sitemap : {len(urls)}")
    print(f"  keyLocation               : {key_location}")
    print(f"  User-Agent                : {USER_AGENT} (timeout {TIMEOUT}s)")

    if dry_run:
        print("\n--- JSON (dry-run, aucun envoi) ---")
        print(body.decode("utf-8"))
        print(f"\nDry-run terminé : {len(urls)} URL(s), aucun POST émis.")
        return 0

    print("\nEnvoi :")
    for endpoint in ENDPOINTS:
        post(endpoint, body)
    print(f"\nTerminé : {len(urls)} URL(s) soumises à {len(ENDPOINTS)} endpoint(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

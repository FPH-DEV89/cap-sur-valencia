#!/usr/bin/env python3
"""Rapport SEO du site Cap sur Valencia (HTML statique, sans dépendance).

Parcourt tous les *.html du dépôt (depuis la racine du dépôt) et affiche un
tableau texte + un résumé des alertes.

Alertes : TITLE>60, TITLE<30, DESC>158, DESC<110, H1_SANS_VALENCIA,
          TITLE_DOUBLE, DESC_DOUBLE, CANONICAL_HTML, SANS_JSONLD

Code de sortie 1 s'il reste au moins une alerte dans le périmètre, 0 sinon.
Le périmètre = toutes les pages publiques sauf les 8 pages réservées au lot B
(leurs alertes sont comptées à part et ne font pas échouer la sortie).
"""

from __future__ import annotations

import os
import re
import sys

# Pages réservées au lot B : jamais modifiées par le lot A.
EXCLUDED_LOT_B = {
    "pages/assurance.html",
    "pages/banque.html",
    "pages/administration.html",
    "pages/sante.html",
    "pages/scolarite.html",
    "pages/checklists.html",
    "pages/ressources.html",
    "pages/budget.html",
}

# Fichiers HTML qui ne sont pas des pages publiques indexables.
NON_PUBLIC = {"404.html", "graphify-out/graph.html"}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RE_TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)
# Le délimiteur ouvrant est capturé puis réutilisé (\1) : une apostrophe
# française dans le texte ne doit pas couper la valeur de l'attribut.
RE_DESC = re.compile(
    r'<meta\s+name=["\']description["\']\s+content=(["\'])(.*?)\1', re.S | re.I
)
RE_DESC_ALT = re.compile(
    r'<meta\s+content=(["\'])(.*?)\1\s+name=["\']description["\']', re.S | re.I
)
RE_H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S | re.I)
RE_CANONICAL = re.compile(
    r'<link\s+rel=["\']canonical["\']\s+href=(["\'])(.*?)\1', re.S | re.I
)
RE_JSONLD = re.compile(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.S | re.I
)
RE_TAG = re.compile(r"<[^>]+>")


def strip_tags(s: str) -> str:
    return re.sub(r"\s+", " ", RE_TAG.sub(" ", s)).strip()


def unescape(s: str) -> str:
    for a, b in (
        ("&amp;", "&"),
        ("&#39;", "'"),
        ("&apos;", "'"),
        ("&quot;", '"'),
        ("&nbsp;", " "),
        ("&lt;", "<"),
        ("&gt;", ">"),
    ):
        s = s.replace(a, b)
    return s


def find_description(html: str) -> str:
    m = RE_DESC.search(html) or RE_DESC_ALT.search(html)
    return unescape(strip_tags(m.group(2))) if m else ""


def find_title(html: str) -> str:
    m = RE_TITLE.search(html)
    return unescape(strip_tags(m.group(1))) if m else ""


def find_h1(html: str) -> str:
    m = RE_H1.search(html)
    return unescape(strip_tags(m.group(1))) if m else ""


def find_canonical(html: str) -> str:
    m = RE_CANONICAL.search(html)
    return m.group(2).strip() if m else ""


def count_jsonld(html: str) -> int:
    return len(RE_JSONLD.findall(html))


def collect_pages() -> list[str]:
    pages = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(
            d for d in dirnames if d not in {".git", "node_modules", ".hermes"}
        )
        for fn in sorted(filenames):
            if not fn.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), ROOT).replace(os.sep, "/")
            pages.append(rel)
    return sorted(pages)


def main() -> int:
    pages = collect_pages()
    if not pages:
        print("Aucun fichier HTML trouvé.", file=sys.stderr)
        return 1

    rows = []
    alerts_by_type: dict[str, int] = {}
    alerts_lot_b: dict[str, int] = {}
    titles_seen: dict[str, list[str]] = {}
    descs_seen: dict[str, list[str]] = {}

    for rel in pages:
        path = os.path.join(ROOT, rel)
        with open(path, encoding="utf-8", errors="replace") as fh:
            html = fh.read()

        title = find_title(html)
        desc = find_description(html)
        h1 = find_h1(html)
        canonical = find_canonical(html)
        njsonld = count_jsonld(html)

        alerts = []
        if len(title) > 60:
            alerts.append("TITLE>60")
        if len(title) < 30:
            alerts.append("TITLE<30")
        if len(desc) > 158:
            alerts.append("DESC>158")
        if len(desc) < 110:
            alerts.append("DESC<110")
        if "valencia" not in h1.lower():
            alerts.append("H1_SANS_VALENCIA")
        if canonical.endswith(".html"):
            alerts.append("CANONICAL_HTML")
        if njsonld == 0:
            alerts.append("SANS_JSONLD")

        if title:
            titles_seen.setdefault(title.lower(), []).append(rel)
        if desc:
            descs_seen.setdefault(desc.lower(), []).append(rel)

        is_public = rel not in NON_PUBLIC
        in_lot_b = rel in EXCLUDED_LOT_B
        if is_public and not in_lot_b:
            for a in alerts:
                alerts_by_type[a] = alerts_by_type.get(a, 0) + 1
        elif in_lot_b:
            for a in alerts:
                alerts_lot_b[a] = alerts_lot_b.get(a, 0) + 1

        rows.append(
            {
                "file": rel,
                "len_title": len(title),
                "len_desc": len(desc),
                "h1": h1,
                "canonical": canonical,
                "jsonld": njsonld,
                "alerts": alerts,
                "lot_b": in_lot_b,
                "public": is_public,
            }
        )

    # Doublons (title / description) : signalés sur toutes les pages concernées.
    for seen, tag in ((titles_seen, "TITLE_DOUBLE"), (descs_seen, "DESC_DOUBLE")):
        for _key, files in seen.items():
            if len(files) > 1:
                for rel in files:
                    for row in rows:
                        if row["file"] == rel and tag not in row["alerts"]:
                            row["alerts"].append(tag)
                            if row["public"] and not row["lot_b"]:
                                alerts_by_type[tag] = alerts_by_type.get(tag, 0) + 1
                            elif row["lot_b"]:
                                alerts_lot_b[tag] = alerts_lot_b.get(tag, 0) + 1

    # --- Tableau ---
    w_file = max(len("fichier"), max(len(r["file"]) for r in rows))
    hdr = (
        f"{'fichier':<{w_file}} | {'title':>5} | {'desc':>4} | "
        f"{'h1':>3} | {'canon':>5} | {'ld+json':>7} | alertes"
    )
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        flag = "B" if r["lot_b"] else ("-" if not r["public"] else " ")
        print(
            f"{r['file']:<{w_file}} | {r['len_title']:>5} | {r['len_desc']:>4} | "
            f"{len(r['h1']):>3} | {('oui' if r['canonical'] else 'NON'):>5} | "
            f"{r['jsonld']:>7} | {flag} {', '.join(r['alerts']) or 'OK'}"
        )

    total_public = sum(1 for r in rows if r["public"] and not r["lot_b"])
    total_lot_b = sum(1 for r in rows if r["lot_b"])

    print()
    print("=== RÉSUMÉ ===")
    print(f"Pages HTML parcourues      : {len(rows)}")
    print(f"Pages du périmètre (lot A) : {total_public}")
    print(f"Pages réservées lot B      : {total_lot_b}")
    print(f"Fichiers non publics       : {len(rows) - total_public - total_lot_b}")
    print()
    print("Alertes — périmètre lot A :")
    if not alerts_by_type:
        print("  aucune — 0 alerte")
    else:
        for k in sorted(alerts_by_type):
            print(f"  {k:<18} {alerts_by_type[k]}")
    print(f"  TOTAL              {sum(alerts_by_type.values())}")
    if alerts_lot_b:
        print()
        print("Alertes — pages lot B (hors périmètre, non bloquantes) :")
        for k in sorted(alerts_lot_b):
            print(f"  {k:<18} {alerts_lot_b[k]}")
        print(f"  TOTAL              {sum(alerts_lot_b.values())}")

    return 1 if alerts_by_type else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # Lecteur qui ferme tôt (`| head`) : stdout neutralisé, puis recalcul du
        # code de sortie pour ne pas fausser le contrat d'exit du script.
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        sys.exit(main())

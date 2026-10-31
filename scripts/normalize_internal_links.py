#!/usr/bin/env python3
"""Normalise les liens internes de Cap sur Valencia : retire le suffixe .html des href.

Cloudflare Pages sert le site en « pretty URLs » : une URL en .html repond 308 vers
la version sans extension. Chaque href interne en .html coute donc une redirection.

Regles appliquees (uniquement sur la VALEUR des attributs href) :
  - valeurs absolues (http://, https://, //, mailto:, tel:, javascript:) et ancres (#...)
    laissees intactes ;
  - <chemin>/index.html[?query][#ancre] -> /[?query][#ancre] ;
  - <chemin>/X.html[?query][#ancre]      -> <chemin>/X[?query][#ancre] ;
  - la query et l'ancre sont conservees telles quelles.

Aucune autre modification : structure HTML, classes, CSS, JS, images, canonical,
og:url, JSON-LD et balises <link> sont hors perimetre (ces derniers sont seulement
signales s'ils contiennent un .html).

Usage :
    python3 scripts/normalize_internal_links.py              # dry-run (defaut)
    python3 scripts/normalize_internal_links.py --dry-run
    python3 scripts/normalize_internal_links.py --apply      # ecrit
    python3 scripts/normalize_internal_links.py --apply --root /chemin/du/depot

Sortie 0 = OK, 1 = au moins une cible manquante sur disque (rien n'est ecrit dans
ce cas : la verification passe avant toute ecriture).
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

# --- Perimetre -----------------------------------------------------------------

EXCLUDED_DIRS = {"graphify-out", ".git", "node_modules", ".hermes"}
EXCLUDED_FILES = {"404.html"}

SKIP_PREFIXES = ("http://", "https://", "//", "mailto:", "tel:", "javascript:", "#")

# href="..." ou href='...' : on capture le prefixe (pour le restituer a l'identique),
# le guillemet utilise, et la valeur.
HREF_RE = re.compile(
    r"""(?P<pre>href\s*=\s*)(?:"(?P<val_dq>[^"]*)"|'(?P<val_sq>[^']*)')""",
    re.IGNORECASE,
)
LINK_TAG_RE = re.compile(r"<link\b[^>]*>", re.IGNORECASE)
PROTECTED_RE = re.compile(
    r"""(?:<link\b[^>]*rel=["']canonical["'][^>]*>"""
    r"""|<meta\b[^>]*property=["']og:url["'][^>]*>"""
    r'|"url"\s*:)',
    re.IGNORECASE,
)

MAX_DISTINCT = 30
HTML_SUFFIX = ".html"


# --- Regles de reecriture ------------------------------------------------------

def split_parts(value: str) -> tuple[str, str, str]:
    """Separe une valeur relative en (chemin, ?query, #ancre), sans rien perdre."""
    frag = ""
    query = ""
    path = value
    if "#" in path:
        path, frag = path.split("#", 1)
        frag = "#" + frag
    if "?" in path:
        path, query = path.split("?", 1)
        query = "?" + query
    return path, query, frag


def is_external(value: str) -> bool:
    return value.strip().lower().startswith(SKIP_PREFIXES)


def new_path_for(path: str) -> str | None:
    """Chemin cible sans .html, ou None si la valeur n'est pas concernee."""
    if not path.lower().endswith(HTML_SUFFIX):
        return None
    base = path[: -len(HTML_SUFFIX)]
    if base.rsplit("/", 1)[-1] == "index":
        return "/"
    return base


def transform(value: str) -> str | None:
    """Nouvelle valeur du href, ou None si le href doit rester tel quel."""
    if is_external(value):
        return None
    path, query, frag = split_parts(value)
    newpath = new_path_for(path)
    if newpath is None:
        return None
    new = newpath + query + frag
    return None if new == value else new


# --- Resolution / verification des cibles --------------------------------------

def resolve_target(root: Path, source: Path, value: str) -> Path:
    """Fichier sur disque correspondant a une valeur de href relative."""
    path, _query, _frag = split_parts(value)
    if path in ("", ".", "./"):
        return source.parent / "index.html"
    if path.startswith("/"):
        rel = path.lstrip("/")
        if not rel:
            return root / "index.html"
        cand = root / rel
    else:
        cand = source.parent / path
    if not cand.suffix:
        cand = cand.with_name(cand.name + HTML_SUFFIX)
    return cand


# --- Parcours ------------------------------------------------------------------

def iter_pages(root: Path) -> list[Path]:
    pages = [
        p
        for p in root.rglob("*.html")
        if not (set(p.relative_to(root).parts) & EXCLUDED_DIRS)
        and p.name not in EXCLUDED_FILES
    ]
    return sorted(pages)


def plan_page(root: Path, page: Path) -> dict:
    """Calcule les reecritures d'une page et les problemes detectes."""
    raw = page.read_bytes()
    text = raw.decode("utf-8")
    edits: list[tuple[int, int, str]] = []  # (start, end, nouvelle valeur)
    rewritten: Counter[str] = Counter()
    missing: list[str] = []
    index_conv = 0
    semantic_warning: list[str] = []

    for m in HREF_RE.finditer(text):
        group = "val_dq" if m.group("val_dq") is not None else "val_sq"
        old = m.group(group)
        new = transform(old)
        if new is None:
            continue
        edits.append((m.start(group), m.end(group), new))
        rewritten[old] += 1

        if new.startswith("/"):
            index_conv += 1
            old_target = resolve_target(root, page, old)
            root_index = root / "index.html"
            if old_target.resolve() != root_index.resolve():
                semantic_warning.append(
                    f"{page.relative_to(root)}: {old} -> {new} "
                    f"(l'ancienne cible etait {old_target.relative_to(root)})"
                )

        target = resolve_target(root, page, new)
        if not target.exists():
            missing.append(
                f"{page.relative_to(root)}: {old} -> {new} "
                f"(cible attendue : {target})"
            )

    return {
        "page": page,
        "text": text,
        "edits": edits,
        "rewritten": rewritten,
        "missing": missing,
        "index_conv": index_conv,
        "semantic_warning": semantic_warning,
    }


def apply_edits(text: str, edits: list[tuple[int, int, str]]) -> str:
    out = []
    cursor = 0
    for start, end, new in edits:  # finditer garantit un ordre croissant
        out.append(text[cursor:start])
        out.append(new)
        cursor = end
    out.append(text[cursor:])
    return "".join(out)


def protected_occurrences(root: Path, pages: list[Path]) -> list[str]:
    """Signale les .html hors href : <link>, canonical, og:url, JSON-LD, autres."""
    found: list[str] = []
    for page in pages:
        text = page.read_text(encoding="utf-8")
        for tag in LINK_TAG_RE.finditer(text):
            if HTML_SUFFIX in tag.group(0):
                found.append(f"{page.relative_to(root)}: balise <link> -> {tag.group(0)[:120]}")
        if HTML_SUFFIX in text:
            for m in PROTECTED_RE.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                snippet = text[m.start(): m.start() + 140].replace("\n", " ")
                if HTML_SUFFIX in snippet:
                    found.append(f"{page.relative_to(root)}:{line}: {snippet}")
    return found


# --- Rapport -------------------------------------------------------------------

def report(results: list[dict], root: Path, apply: bool, total_targets: int,
           problems: list[str], headers: list[str]) -> int:
    touched = [r for r in results if r["edits"]]
    n_hrefs = sum(len(r["edits"]) for r in results)
    n_index = sum(r["index_conv"] for r in results)
    distinct: Counter[str] = Counter()
    for r in results:
        distinct.update(r["rewritten"])

    print("=== Normalisation des liens internes (.html -> pretty URL) ===")
    print(f"Depot            : {root}")
    print(f"Mode             : {'APPLY (ecriture)' if apply else 'DRY-RUN (aucune ecriture)'}")
    print(f"Pages analysees  : {len(results)}")
    print(f"Fichiers modifies: {len(touched)}")
    print(f"href reecrits    : {n_hrefs}")
    print(f"index.html -> /  : {n_index}")
    print(f"Cibles verifiees : {total_targets} "
          f"({'toutes existent sur disque' if not problems else 'PROBLEMES DETECTES'})")
    print(f"Valeurs distinctes reecrites : {len(distinct)}")

    if touched:
        print("\n-- Fichiers (href reecrits) --")
        for r in sorted(touched, key=lambda r: -len(r["edits"])):
            print(f"  {len(r['edits']):5d}  {r['page'].relative_to(root)}")

    if distinct:
        print(f"\n-- Valeurs reecrites distinctes (max {MAX_DISTINCT} affichees) --")
        for old, count in distinct.most_common(MAX_DISTINCT):
            new = transform(old)
            print(f"  {count:5d}  {old}  ->  {new}")

    if headers:
        print("\n-- .html detectes hors href (SIGNALES, NON MODIFIES) --")
        for h in headers[:40]:
            print(f"  {h}")
        if len(headers) > 40:
            print(f"  ... et {len(headers) - 40} autre(s)")

    warnings = [w for r in results for w in r["semantic_warning"]]
    if warnings:
        print("\n-- Avertissements (index.html hors racine ?) --")
        for w in warnings:
            print(f"  {w}")

    if problems:
        print("\n!! CIBLES MANQUANTES — aucune ecriture effectuee !!", file=sys.stderr)
        for p in problems:
            print(f"  {p}", file=sys.stderr)
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Retire le suffixe .html des href internes (Cloudflare Pages, pretty URLs)."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="n'ecrit rien (defaut)")
    mode.add_argument("--apply", action="store_true", help="ecrit les fichiers modifies")
    parser.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parent.parent),
        help="racine du depot (defaut : parent du dossier scripts/)",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not (root / "index.html").exists():
        print(f"Racine invalide (index.html absent) : {root}", file=sys.stderr)
        return 2

    pages = iter_pages(root)
    results = [plan_page(root, p) for p in pages]

    problems = [p for r in results for p in r["missing"]]
    total_targets = sum(len(r["edits"]) for r in results)
    headers = protected_occurrences(root, pages)

    code = report(results, root, args.apply, total_targets, problems, headers)

    if code == 0 and args.apply:
        written = 0
        for r in results:
            if not r["edits"]:
                continue
            new_text = apply_edits(r["text"], r["edits"])
            if new_text == r["text"]:
                continue
            r["page"].write_bytes(new_text.encode("utf-8"))
            written += 1
        print(f"\nFichiers ecrits : {written}")
    elif code == 0:
        print("\nDry-run : rien n'a ete ecrit. Relancer avec --apply pour appliquer.")

    return code


if __name__ == "__main__":
    sys.exit(main())

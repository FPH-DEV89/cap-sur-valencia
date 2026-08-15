# Spec 2 — Correction espacements v6 (Cap sur Valencia)

**Date**: 2026-08-15 — mesure Playwright : 128-144px de vide entre chaque section de la home

## Diagnostic mesuré (Playwright 1920px, home)

| Transition | Vide réel | Cause |
|---|---|---|
| histoire → art-de-vivre | ~128px | `.section` padding 4rem ×2 |
| art-de-vivre → heritage | **144px** (72+72) | `.section-culture` = `--space-xl` 4rem ×2 (inline index.html ligne ~372) |
| heritage → quartiers | 538px (dont bandeau navy 5rem×2 + contenu) | `.section-magazine-break` padding 5rem |
| quartiers → saveurs | ~144px | inline `padding: 4.5rem 0 3.5rem` (ligne 893) |
| saveurs → timeline | ~144px | `.section-culture` |
| timeline → guide | ~144px | `.section` |

**Cible** : 64-88px de vide total entre sections (padding ~2rem-2.5rem par côté),
bandeau navy réduit à ~4rem max par côté.

## COR-01 — Réduire le padding des sections (P0)

1. **`css/style.css` ligne ~322** : `.section { padding: var(--space-xl) 0; }` →
   `padding: 2.5rem 0;` (40px/côté = 80px de vide total). Mobile (media query ~3369) :
   `padding: 2rem 0;` si la valeur actuelle est ≥ 2.5rem.
2. **`index.html` inline ligne ~372** : `.section-culture { padding: var(--space-xl) 0; }`
   → `padding: 2.5rem 0;` (art-de-vivre, heritage, saveurs).
3. **`index.html` ligne 893** (section quartiers) : `padding: 4.5rem 0 3.5rem` →
   `padding: 3rem 0 2.5rem`.
4. **`css/style.css` ligne ~3561** `.section-magazine-break` : `padding: 5rem 1.5rem` →
   `padding: 3.5rem 1.5rem` (mobile 3816 : `3.5rem 1.25rem` → `2.5rem 1.25rem`).
5. **Vérifier les autres sections avec padding inline > 3rem** (grep `padding: [4-9]rem` dans
   index.html et pages/*.html) : les réduire à ≤ 3rem par côté SAUF hero (qui peut rester
   4.5rem/2.5rem).
6. **`.section-alt`** (timeline) : hérite de `.section` → OK automatiquement.
7. Ne PAS changer `--space-xl` global (utilisé ailleurs : cards, headers) — surcharger
   uniquement les paddings de sections.

## COR-02 — Vérification finale

- Home : gaps entre sections = 80-96px max (mesure Playwright même script).
- Bandeau navy : hauteur totale ~280-320px (au lieu de 538px).
- Zéro débordement mobile 390px, zéro `.fade-in` caché sans JS.
- Ne toucher à AUCUN autre style ni contenu.

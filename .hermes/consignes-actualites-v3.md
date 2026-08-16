# Consignes v3 — Derniers mineurs QA (Cap sur Valencia, page Actualités)

Projet : site statique vanilla dans `/tmp/cap-sur-valencia`. PAS DE GIT, PAS DE COMMIT.
Édite uniquement les fichiers listés, uniquement les points ci-dessous.

## 1. `actualites/2026-08-17-oceanografic.html` ligne ~170 — précision architecturale
Texte actuel : « Difficile de parler de Valencia sans évoquer sa silhouette futuriste
emblématique conçue par l'architecte Félix Candela et Santiago Calatrava. Posé à l'extrémité
est des jardins du Turia, l'Oceanogràfic est tout simplement le plus vaste complexe marin
d'Europe avec ses 110 000 m² de superficie et plus de 45 000 spécimens représentant 500
espèces différentes. »

Reformuler pour une attribution exacte : l'Oceanogràfic est l'œuvre de l'ingénieur
**Félix Candela** (Santiago Calatrava a conçu les autres bâtiments de la Cité des Arts).
Proposition : « Difficile de parler de Valencia sans évoquer l'ensemble futuriste de la Cité
des Arts et des Sciences. Posé à l'extrémité est des jardins du Turia, l'Oceanogràfic — signé
par l'ingénieur Félix Candela — est tout simplement le plus vaste complexe marin d'Europe
avec ses 110 000 m² de superficie et plus de 45 000 spécimens représentant 500 espèces
différentes. »

## 2. JSON-LD — notation Schema.org `priceRange`
Remplacer la notation monétaire en euro par la notation dollar conforme Schema.org
(le champ priceRange suit la convention `$`, `$$`, `$$$`) :
- `actualites/2026-08-16-bioparc-valencia.html` ligne ~93 : `"priceRange": "€€"` → `"priceRange": "$$"`
- `actualites/2026-08-17-oceanografic.html` ligne ~93 : `"priceRange": "€€€"` → `"priceRange": "$$$"`
- `actualites/2026-08-18-mercado-central.html` ligne ~94 : `"priceRange": "€"` → `"priceRange": "$"`
- `actualites/2026-08-19-albufera-el-palmar.html` ligne ~92 : `"priceRange": "€"` → `"priceRange": "$"`
Ne toucher qu'aux valeurs du JSON-LD, pas aux tarifs affichés dans le HTML visible.

## 3. Bouton menu — `type="button"`
Dans les 4 fiches du dossier `actualites/`, ajouter `type="button"` au bouton
`<button class="nav-toggle" aria-label="Menu">` (robustesse, bonne pratique HTML) :
`<button type="button" class="nav-toggle" aria-label="Menu">`

## Fichiers à modifier
- `actualites/2026-08-16-bioparc-valencia.html`
- `actualites/2026-08-17-oceanografic.html`
- `actualites/2026-08-18-mercado-central.html`
- `actualites/2026-08-19-albufera-el-palmar.html`

## Règles strictes
- Ne modifier QUE ces 4 fichiers, uniquement les points listés.
- N'exécute AUCUNE commande. Réponds en français : fichiers modifiés + lignes changées.

# Consignes v2 — Corrections QA (Cap sur Valencia, page Actualités)

Projet : site statique vanilla dans `/tmp/cap-sur-valencia` (HTML/CSS/JS, pas de build).
PAS DE GIT, PAS DE COMMIT, PAS DE PUSH. Édite uniquement les fichiers listés.

Le QA senior a détecté 5 corrections à apporter aux fiches du dossier `actualites/`.
Corrige EXACTEMENT ces points, rien d'autre.

## 1. `actualites/2026-08-17-oceanografic.html` — calcul économie famille nombreuse FAUX
Ligne ~194 : le texte annonce « une économie immédiate d'environ 15 € par rapport au plein tarif ».
Le calcul réel (2 adultes + 3 enfants, tarifs de base) :
- Plein tarif : 2 × 35,90 € + 3 × 26,65 € = 151,75 €
- Tarif famille nombreuse : 2 × 30,52 € + 3 × 22,65 € = 128,99 €
- Économie : **22,76 € ≈ 23 €**
Remplacer « environ 15 € » par « **près de 23 €** » (et si le contexte s'y prête, ajouter le
détail du calcul : 151,75 € → 128,99 €). Garder le style de la phrase.

## 2. Les 4 fiches `actualites/*.html` — aria-current mal placé dans la nav
Dans la navigation, le lien « Actualités » a `aria-current="page"` (lignes ~129-130) :
```html
<li><a href="../pages/actualites.html" aria-current="page">Actualités</a></li>
```
Ce n'est PAS la page courante (on est sur une fiche). Retirer `aria-current="page"` de ce lien
dans les 4 fiches. NE PAS toucher au `<span aria-current="page">` du breadcrumb (lignes ~144-145,
celui-là est correct).

## 3. JSON-LD — openingHours trompeurs (horaires variables)
- `actualites/2026-08-16-bioparc-valencia.html` (~ligne 93) : SUPPRIMER la ligne
  `"openingHours": "Mo-Su 10:00-19:00",` — les horaires Bioparc varient selon la saison
  (fermeture variable, ouverture 11h certains jours fériés). Une donnée structurée fausse
  nuit au SEO.
- `actualites/2026-08-17-oceanografic.html` (~ligne 93) : SUPPRIMER
  `"openingHours": "Mo-Su 10:00-18:00",` — fermeture jusqu'à 21h en été.
- `actualites/2026-08-19-albufera-el-palmar.html` (~ligne 92) : SUPPRIMER
  `"openingHours": "Mo-Su 10:00-20:30",` — départs variables selon la journée.
- `actualites/2026-08-18-mercado-central.html` : GARDER `"openingHours": "Mo-Sa 07:30-15:00"`
  (horaires fixes et vérifiés : lundi-samedi 7h30-15h, fermé dimanche).
Vérifier que le JSON reste valide après suppression (virgules).

## 4. Uniformiser l'orthographe : « València » → « Valencia »
Dans les 3 fiches qui contiennent « València » (bioparc-valencia, oceanografic, mercado-central),
remplacer toutes les occurrences « València » par « Valencia » (adresses comprises), pour rester
cohérent avec le reste du site (« Cap sur Valencia »). La fiche albufera n'en contient pas.

## Fichiers à modifier
- `actualites/2026-08-16-bioparc-valencia.html`
- `actualites/2026-08-17-oceanografic.html`
- `actualites/2026-08-18-mercado-central.html`
- `actualites/2026-08-19-albufera-el-palmar.html`

## Règles strictes
- Ne modifier QUE ces 4 fichiers, uniquement les points listés ci-dessus.
- N'exécute AUCUNE commande (pas de git, pas de build, pas de serveur).
- Palette Stitch et structure HTML existantes : ne pas changer.
- Réponds en français : fichiers modifiés + lignes changées.

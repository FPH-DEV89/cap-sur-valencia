# Spec 2 — Corrections ciblées post-QA v2 (Cap sur Valencia)

**Date**: 2026-08-15 — QA vision grok-4.5 après implémentation v2

## COR-01 — Aligner les totaux du calculateur budget sur les KPI officiels (P1)

Le calculateur (js/main.js, objets `scenarios`) additionne des postes qui ne tombent pas
sur les totaux officiels affichés dans les KPI cards et les scénarios (budget.html) :

| Scénario | Total calculé actuel | Total officiel (KPI) | Écart |
|---|---|---|---|
| Sobre | 2 460 € | 2 480 € | +20 |
| Confort | 3 400 € | 3 425 € | +25 |
| Tranquille | 4 400 € | 4 435 € | +35 |

**Correction** : ajuster le poste `divers` de chaque scénario pour que la somme tombe
EXACTEMENT sur le total officiel :
- Sobre : divers 100 → 120
- Confort : divers 150 → 175
- Tranquille : divers 250 → 285

Ne toucher à AUCUN autre poste. Vérifier ensuite que le total affiché dans
`#calc-total` vaut 2 480 € (Sobre), 3 425 € (Confort), 4 435 € (Tranquille).

## COR-02 — Subnav budget plus contrastée (P2)

L'audit : « Subnav sticky légère, risque de se fondre au scroll ». Renforcer :
- Fond plus opaque (beige #fbfbe2 à ~95 % + blur léger), bordure basse 1px
  `rgba(0,22,38,0.10)`.
- Chips inactifs : texte navy, bordure 1px navy à 25 %, fond transparent.
- Chips actif : fond terracotta plein, texte blanc (contraste ≥ 4.5:1), léger shadow teinté.
- Ne pas changer la hauteur ni le comportement sticky existant.

## COR-03 — CTA fin de section restos cohérent (P2)

L'audit : « CTA "Voir le guide scolarité" un peu hors sujet en bas de bloc restos ».
Sur budget.html, dans la section des adresses restos, remplacer le CTA par un lien
cohérent avec le contexte : « Toutes nos adresses testées » vers `#restos` si déjà là,
sinon un CTA « Voir le guide quartiers » vers `pages/quartiers.html` (cohérent :
les restos sont liés aux quartiers). Un seul CTA, libellé court, style existant
(bouton terracotta ou lien souligné — garder le style du site).

## Règles

- Mêmes règles que spec v2 : design Stitch, zéro fonctionnalité cassée, pas d'em-dash,
  chiffres réels, pas de scroll listener (IntersectionObserver si besoin).
- Ne toucher QUE aux éléments listés ci-dessus. Pas de refonte.

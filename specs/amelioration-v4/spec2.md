# Spec 2 — Polish senior post-QA v4 (Cap sur Valencia)

**Date**: 2026-08-15 — QA vision grok-4.5 (reviewer exigeant) après implémentation v4

## Retour du reviewer (extraits)

- « Hero : overlay + CTA centré = template ; titre peu ancré dans l'image »
- « Pas de vrai moment wow : pas de bandeau break full-bleed hors hero »
- « Cards uniformes : mêmes coins, ombres, padding »
- « Rythme vertical : trop de sections titre + sous-titre + grilles de cards »
- « CTA : multiplication des boutons pill sans hiérarchie primaire/secondaire forte »

## COR-01 — Hero index refondu : split éditorial (P1)

Passer le hero de la home de « centré sur photo » à **split éditorial** (pattern des city guides
premium : grande typo à gauche sur fond beige, photo forte à droite qui déborde jusqu'au bord) :

- **Desktop (≥ 992px)** : grille 2 colonnes. Gauche : kicker (existant), H1 Playfair massif
  (clamp existant conservé, `text-wrap: balance`), sous-titre, meta (compte à rebours), CTA
  (1 primaire terracotta + 1 lien secondaire souligné, PAS un 2e bouton pill). Fond beige
  #fbfbe2. Droite : la photo hero-ciudad-arte.jpg en `object-fit: cover`, hauteur pleine du
  hero (min-h ~560-640px desktop), bord arrondi côté gauche seulement (border-radius 16px
  sur le coin gauche ou 0 si full-bleed à droite), léger zoom lent au chargement (scale 1.04→1,
  5s, reduced-motion statique).
- **Mobile (< 992px)** : empilement photo en haut (hauteur ~320px, cover, coins arrondis
  12px) puis texte en dessous sur beige, CTA primaire pleine largeur + lien secondaire.
- Le countdown reste en meta discret (tabular-nums), pas de grosse pill.
- Vérifier : le header (nav sticky) reste lisible sur le beige (pas de superposition photo).
- Ne PAS casser : `.js .fade-in` (visible sans JS), reduced-motion, l'id `#accueil`.

## COR-02 — Bandeau « moment magazine » navy full-bleed (P1)

Insérer UN bandeau pleine largeur entre « Heritage & Architecture » et « Trouver le bon
quartier » sur la home (l'audit : aucun break full-bleed hors hero) :

- Fond navy #001626 pleine largeur (pas de container), padding vertical généreux
  (py ~5rem desktop, ~3.5rem mobile).
- Contenu centré max 720px : une **citation géante** en Playfair italique beige
  (guillemets « »), tirée d'une phrase EXISTANTE du site (ne pas en inventer — chercher dans
  le contenu « Pourquoi Valencia ? » ou l'intro). Sous la citation : un attribut discret
  (« — Notre journal, 2026 » ou le contexte existant), en Source Sans 3 beige 80%.
- Au-dessus de la citation : un petit label (pas un eyebrow répété — un seul sur la page,
  ex: « Le projet ») ou rien.
- Reveal : fade + translateY (gated .js, reduced-motion statique). Le fond navy ne crée
  PAS de section blanche/beige après lui (la suivante reste beige — c'est un moment unique,
  pas une alternance).
- Pas d'em-dash dans la citation (réécrire la phrase existante avec deux points si besoin).

## COR-03 — Shape & hiérarchie des cards unifiées (P2)

- **Rayons unifiés** : les cards (culture-card, tradition-card, quartier-card, kpi-card,
  guide-card, highlight-box) partagent UN rayon : 12px (le plus présent). Corriger les
  outliers (16px+ ou 8px) vers 12px sauf si un composant spécifique a une règle documentée
  (badges/pills = full round conservé).
- **Ombres teintées** : les ombres des cards sont teintées terracotta/navy (rgba(146,75,38,0.08-0.14)
  ou rgba(0,22,38,0.08-0.12)), jamais noires pures — vérifier et unifier.
- **Hiérarchie CTA** : sur la home, un seul CTA primaire par section (terracotta plein) ;
  les secondaires passent en lien souligné (texte terracotta + soulignement animé hover) au
  lieu de boutons outline répétés. Ne pas toucher au hero (COR-01) ni aux boutons de nav.
- Vérifier les contrastes des meta/secondary (labels dates, captions) : ≥ 4.5:1 (passer les
  valeurs trop claires en `--text-muted: #4a4a4a` existant ou plus foncé si besoin).

## Règles

- Mêmes règles que spec v4 : design Stitch, `.js .fade-in`, zéro scroll listener,
  reduced-motion, zéro em-dash, zéro contenu perdu, ancres préservées.
- Ne toucher QUE : `index.html` (hero + bandeau), `css/style.css` (rayons/ombres/CTA),
  éventuellement le contenu de citation existant. Pas les autres pages.
- Vérifier responsive 390px (pas de débordement) et le test sans JS.

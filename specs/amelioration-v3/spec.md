# Feature Specification: Amélioration esthétique v3 — Pages guides (Cap sur Valencia)

**Feature Branch**: `improve-design-v3`
**Created**: 2026-08-15
**Status**: Draft — prête pour implémentation agy

**Input**: « Améliore l'esthétique de toutes les pages. » — Audit vision grok-4.5 (15/08/2026) sur les 6 pages guides : sante, administration, emploi, ressources, checklists, scolarite.

---

## Constitution (identique aux v1/v2 — rappel)

1. **Design Stitch de Florian = loi.** Palette #fbfbe2 / #001626 / #924b26, Playfair + Source Sans 3. On améliore l'exécution, pas la direction.
2. **Zéro contenu perdu.** Tout le texte éditorial existant (y compris les chiffres réels : 40-80 €/document, N26/Revolut, 200 € d'amende, avril-mai, etc.) est préservé. Les modifications restructurent la MISE EN FORME, pas le fond.
3. **Zéro fonctionnalité cassée.** Nav, ancres, skip links, fade-in (`.js .fade-in`), responsive préservés.
4. **Photos existantes réutilisées** (`assets/img/sante-hopital.jpg`, `admin-ayuntamiento.jpg`, `emploi-port.jpg`, `ressources-tram.jpg`, `checklists-parc.jpg`, `scolarite-ceip.jpg`, `ecoles-mural-ceip.jpg`). Pas de nouvelles images nécessaires sauf si le CSS le permet (bandeaux = réutilisation des mêmes).
5. **WCAG AA.** Contraste ≥ 4.5:1, focus visible, alt existants.
6. **Pas d'em-dash (—) ni en-dash (–) dans les nouveaux textes.** Zéro.
7. **Les règles anti-slop s'appliquent SAUF si le design Stitch prime** (fond beige conservé).

---

## User Stories

### US-01 — Timeline visuelle pour les démarches admin (11 étapes) (P1)

**En tant que** lecteur de la page Administration,
**je veux** voir les 11 étapes (traductions → certificat digital) sous forme de timeline verticale visuelle avec badges (coût / délai / lieu),
**afin que** le parcours soit scannable et rassurant (aujourd'hui : liste numérotée en prose).

**Independent Test** : scroller la page admin → les 11 `<h3>` numérotés sont présentés comme une timeline verticale (ligne continue + puces numérotées + cartes), chaque carte a des badges de méta (coût, délai, lieu) quand les données existent.

**Acceptance Scenarios**:
1. **Given** la page administration, **When** je regarde les 11 étapes, **Then** elles sont rendues en timeline verticale : ligne verticale terracotta/navy à gauche, numéro de l'étape en pastille ronde, titre en Playfair, texte existant conservé, badges méta (ex: « 40 à 80 € », « avant de partir », « DGT ») sous le titre.
2. **Given** une étape avec un piège (ex: étape 9 permis, « 200 € d'amende »), **When** je lis, **Then** le piège est mis en évidence dans un encart alerte (fond terracotta-light, bordure terracotta, icône ⚠️ existante ou texte).
3. **Given** la timeline sur mobile (390px), **When** je scrolle, **Then** la ligne et les pastilles restent alignées à gauche sans débordement.
4. **Given** la page après modification, **When** je vérifie le contenu, **Then** les 11 étapes et leurs chiffres réels (40-80 €, N26/Revolut, avril-mai, 200 €, DGT, modelo 030, FNMT) sont tous présents.

### US-02 — Plan d'action emploi en timeline 4 phases (P1)

**En tant que** lecteur de la page Emploi,
**je veux** voir les 4 phases (Avant de partir / J+0 à J+30 / Mois 1 à 3 / Mois 3 à 12) comme une timeline avec jalons,
**afin que** je visualise la progression temporelle (aujourd'hui : 4 titres emoji + paragraphes).

**Acceptance Scenarios**:
1. **Given** la page emploi, **When** je regarde la section plan d'action, **Then** les 4 phases sont rendues en timeline (horizontale sur desktop avec flèches/jalons, verticale sur mobile), chaque phase a son emoji existant, son titre, son texte conservé.
2. **Given** les salaires mentionnés (chiffres réels existants), **When** je lis, **Then** ils restent exacts (vérifier les fourchettes existantes dans le HTML — ne pas en inventer).
3. **Given** la page, **When** je regarde les sites d'emploi (InfoJobs…), **Then** ils sont en cards/tuiles cliquables compactes (nom + description courte) au lieu d'une liste dense.

### US-03 — Page Santé : 3 voies en cards + étapes SIP en stepper (P1)

**En tant que** lecteur de la page Santé,
**je veux** voir les « 3 voies pour avoir ton numéro de Sécu » en cards différenciées et « Comment on l'obtient » (SIP) en stepper visuel,
**afin que** les options soient comparables (aujourd'hui : 3 blocs colorés + étapes en prose).

**Acceptance Scenarios**:
1. **Given** la section « Trois voies », **When** je regarde, **Then** chaque voie est une card (fond blanc sur beige, bordure colorée discrète existante conservée vert/bleu/rose ou unifiée terracotta/navy) avec titre, texte existant, et un badge « notre choix » sur la voie recommandée si le contenu la distingue (vérifier le texte : si une voie est présentée comme recommandée, la mettre en avant avec bordure terracotta 2px).
2. **Given** la section SIP « Comment on l'obtient », **When** je regarde, **Then** les étapes sont un stepper vertical numéroté (pastilles + texte conservé).
3. **Given** la photo `sante-hopital.jpg`, **When** je regarde le haut de page, **Then** elle est présentée en bandeau large avec légende existante, ou intégrée au hero si le hero actuel est vide (fond navy + photo en bandeau + titre blanc).

### US-04 — Page Ressources : grille de cards thématiques (P1)

**En tant que** lecteur de la page Ressources (21 sections H2, 49 liens),
**je veux** voir les ressources en grille de cards thématiques avec icône + titre + liens,
**afin que** je trouve une info en un coup d'œil (aujourd'hui : longues listes à puces).

**Independent Test** : ouvrir ressources.html → les sections H2 sont groupées en cards (2-3 colonnes desktop, 1 colonne mobile), chaque card contient son titre + ses liens existants.

**Acceptance Scenarios**:
1. **Given** la page ressources, **When** je regarde les 21 sections, **Then** elles sont organisées en grille responsive (auto-fit minmax 280px) de cards : titre de section en Playfair, liens existants en dessous, icône emoji existante du H2 si présente.
2. **Given** la section urgences/numéros (« Les numéros qui peuvent sauver »), **When** je regarde, **Then** elle est mise en avant (card pleine largeur avec fond terracotta-light ou navy et texte contrasté — selon ce qui est lisible — car c'est de l'info critique).
3. **Given** la grille sur mobile, **When** je scrolle, **Then** les cards s'empilent en une colonne propre.
4. **Given** la page après modification, **When** je vérifie, **Then** les 49 liens existants sont tous conservés (aucun lien supprimé).

### US-05 — Checklists en composant visuel (P2)

**En tant que** lecteur des pages Checklists et Scolarité,
**je veux** voir les checklists comme des listes à cocher visuelles (cases stylées),
**afin que** je puisse suivre ma progression (aujourd'hui : listes à puces/encadrés).

**Acceptance Scenarios**:
1. **Given** la page checklists, **When** je regarde les listes, **Then** chaque item est une ligne avec case à cocher stylée (carré arrondi 4px, bordure navy/terracotta, état coché = fond terracotta + ✓ blanc, cliquable avec `cursor:pointer` et label cliquable).
2. **Given** les checklists, **When** je coche une case, **Then** le texte est barré légèrement (text-decoration line-through avec couleur atténuée) et la case se remplit — état persistant sur la session via `localStorage` si simple à ajouter (sinon skip, priorité basse).
3. **Given** la page scolarité, **When** je regarde les étapes d'inscription, **Then** elles sont en stepper visuel (comme US-03) avec les dates existantes (avril-mai, etc.).
4. **Given** les pages, **When** j'utilise le clavier, **Then** les cases sont focusables (tab) et cochables (espace).

### US-06 — Contraste renforcé + fonds alternés + rythme (P2)

**En tant que** lecteur,
**je veux** un texte corps plus contrasté et des sections avec des fonds légèrement alternés,
**afin que** les longues pages guides soient moins monotones et plus lisibles.

**Acceptance Scenarios**:
1. **Given** les 6 pages guides, **When** je lis le corps de texte, **Then** la couleur du texte est assombrie si nécessaire pour ≥ 4.5:1 sur beige (vérifier les valeurs grises actuelles, les passer en `--text` ou un brun foncé `#2a2418`-ish qui reste dans la palette chaude).
2. **Given** les sections successives d'une page guide, **When** je scrolle, **Then** les sections alternent subtilement : beige (#fbfbe2) / blanc cassé (#ffffff à 60% ou #fdfded existant) — jamais de changement brusque, jamais de section noire.
3. **Given** les encarts `highlight-box`, **When** je les compare, **Then** ils ont des styles différenciés selon leur rôle sémantique : alerte (fond terracotta-light + bordure terracotta), conseil (fond navy-light ou beige-dark + bordure navy), info (fond blanc + bordure fine) — au lieu de tous identiques.
4. **Given** les CTA de fin de page, **When** je regarde, **Then** ils sont des boutons réels (pas des textes) — style `.btn` existant (terracotta plein ou outline).

### US-07 — Hero des pages guides avec photo en bandeau (P2)

**En tant que** visiteur,
**je veux** un hero plus immersif sur les pages guides (photo en bandeau, titre lisible),
**afin que** chaque page ait une identité visuelle immédiate (aujourd'hui : photo isolée dans le contenu ou absente du hero).

**Acceptance Scenarios**:
1. **Given** une page guide avec photo (sante, admin, emploi, ressources, checklists, scolarite), **When** je charge la page, **Then** la photo existante est utilisée en bandeau large sous le header (hauteur ~240-320px, cover, border-radius 12px cohérent) OU intégrée au header de page existant si le layout s'y prête — sans casser le titre.
2. **Given** le bandeau photo, **When** le texte est au-dessus/à côté, **Then** le contraste est garanti (overlay navy semi-transparent si texte blanc sur photo).
3. **Given** le bandeau sur mobile, **When** je charge, **Then** la hauteur est réduite (~180px) pour ne pas écraser le titre.

---

## Functional Requirements

- **FR-001** : Fichiers modifiés : `pages/sante.html`, `pages/administration.html`, `pages/emploi.html`, `pages/ressources.html`, `pages/checklists.html`, `pages/scolarite.html`, `css/style.css`, `js/main.js` (si nécessaire pour les cases à cocher).
- **FR-002** : Les classes CSS nouvelles suivent la convention kebab-case : `.guide-timeline`, `.guide-step`, `.guide-step-badge`, `.guide-card-grid`, `.guide-card`, `.checklist-item`, `.checklist-checkbox`, `.banner-photo`, etc.
- **FR-003** : Les ids de sections et ancres existantes ne changent pas. Les liens internes (`href="#..."`) restent valides.
- **FR-004** : Les photos : chemins relatifs existants, `alt` conservés, `loading="lazy"` conservé.
- **FR-005** : Le JS : si ajout (checkboxes localStorage, stepper), utiliser des écouteurs propres, `prefers-reduced-motion` respecté, pas de scroll listener (`window.addEventListener('scroll')` interdit — IntersectionObserver seulement).
- **FR-006** : Aucun em-dash (—) ni en-dash (–). Aucun nouveau contenu inventé (chiffres, adresses, noms).
- **FR-007** : Aucune donnée personnelle de la famille ajoutée.
- **FR-008** : Les 6 pages passent le test sans JS (contenu visible, `.js .fade-in` respecté).

## Success Criteria

- **SC-001** : `grep -c "guide-timeline\|guide-step\|guide-card\|checklist-item" pages/*.html` → ≥ 6 fichiers concernés (les 6 pages guides).
- **SC-002** : Zéro em-dash/en-dash ajouté dans le diff (`git diff | grep -E "^\+" | grep -c "—"` = 0).
- **SC-003** : Aucun lien cassé : tous les `href` internes existants restent (vérifier les ancres).
- **SC-004** : Contraste corps ≥ 4.5:1 (vérifier la valeur `--text` ou la remplacer par une teinte plus foncée dans la palette chaude).
- **SC-005** : Les 6 pages sans JS : 0 élément `.fade-in` à opacity 0 (test Playwright).
- **SC-006** : Zéro débordement horizontal desktop (1920) et mobile (390) sur les 6 pages.
- **SC-007** : Les 49 liens de ressources.html sont tous présents après refonte.
- **SC-008** : Le contenu des 11 étapes admin et 4 phases emploi est intégralement conservé (diff contrôlable).

## Assumptions

- Les photos existantes suffisent (pas de nouvelle recherche d'images).
- Le style `highlight-box` existant peut être étendu en variantes (alert/advice/info) plutôt que remplacé brutalement.
- agy implémente, Hermes fait la QA visuelle (screenshots + vision), boucle spec2 si écart.

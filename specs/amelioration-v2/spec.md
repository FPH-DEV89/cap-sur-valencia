# Feature Specification: Amélioration design v2 — Cap sur Valencia

**Feature Branch**: `improve-design-v2`
**Created**: 2026-08-15
**Status**: Draft — prête pour implémentation agy

**Input**: « Utilise tes derniers skills pour améliorer le site Cap sur Valencia. Donne-toi à 1000 % »
**Audit**: screenshots Playwright 1920×1080 + mobile 390×844 + vision grok-4.5 (15/08/2026) + audit code

---

## Constitution du projet (principes non-négociables — hérités de v1)

1. **Le design Stitch de Florian est la loi.** Palette #fbfbe2 (beige) / #001626 (navy) / #924b26 (terracotta), Playfair Display (titres) + Source Sans 3 (corps). On améliore l'EXÉCUTION, on ne redessine pas. Les tokens `--bg-beige`, `--navy`, `--terracotta` dans `css/style.css` restent la source de vérité.
2. **Zéro fonctionnalité cassée.** Navigation, sections, contenu, responsive et animations (IntersectionObserver fade-in, navbar scrolled, nav mobile, calculateur budget, filtres quartiers) sont préservés. Modifications additives ou amélioratives, jamais destructives.
3. **Photos réelles libres de droits uniquement** (Wikimedia Commons). 7 nouvelles photos viennent d'être téléchargées dans `assets/img/` (voir US-04). Les 6 photos v1 restent en place. Pas d'images IA.
4. **Chiffres réels du contenu existant.** Scénarios budget (2 480 € / 3 425 € / 4 435 €), adresses restos, noms de quartiers et d'écoles viennent des pages existantes. Rien d'inventé.
5. **Accessibilité WCAG AA.** Contraste texte ≥ 4.5:1, focus visible, alt descriptifs, skip link (manquant sur 100 % des pages).
6. **Performance.** Images locales, `loading="lazy"` sous le fold, aucune nouvelle dépendance, aucun framework.
7. **Pas d'eyebrows répétés, pas de cartes monotones, pas d'ombres lourdes, zéro em-dash (—).** Les règles anti-slop s'appliquent SAUF quand elles contredisent le design Stitch (le beige #fbfbe2 est un choix utilisateur, il prime).

---

## User Stories

### US-01 — Sticky subnav d'ancres sur Budget (P1)

**En tant que** lecteur de la page Budget (la plus longue du site, 12 sections),
**je veux** une barre de navigation d'ancres sticky sous le header quand je scrolle,
**afin que** je puisse sauter directement à la section qui m'intéresse (Loyer, Manger dehors, Scénarios, Installation, Salaires, Restos).

**Pourquoi ce priority** : l'audit vision a relevé « page très longue sans sticky subnav → fatigue au scroll ». Impact UX maximal sur la page la plus consultée après la home.

**Independent Test** : scroller la page budget → une barre de chips apparaît sous le header (sticky, top: ~64-72px) avec les ancres ; cliquer « Restos » → la page défile jusqu'à la section des adresses.

**Acceptance Scenarios**:
1. **Given** la page budget chargée, **When** je scrolle au-delà du hero, **Then** une barre sticky de chips d'ancres (Loyer / Manger dehors / Scénarios / Installation / Salaires / Restos) est visible sous le header, fond légèrement translucide beige avec blur léger.
2. **Given** la barre d'ancres, **When** je clique un chip, **Then** la page défile en douceur (scroll-behavior smooth existant) jusqu'à la section cible, et le chip actif est mis en évidence (fond terracotta, texte blanc).
3. **Given** la page sur mobile (390px), **When** je scrolle, **Then** la barre défile horizontalement (overflow-x auto, scroll-snap) sans casser le layout.
4. **Given** la barre, **When** je scrolle manuellement vers une section, **Then** le chip correspondant devient actif (IntersectionObserver, pas de scroll listener).

### US-02 — Cards écoles scannables sur ecoles.html (P1)

**En tant que** parent qui cherche une école,
**je veux** voir chaque école sous forme de card compacte avec badges (langue d'enseignement, points forts) au lieu d'un mur de texte,
**afin que** je compare les options d'un coup d'œil.

**Pourquoi ce priority** : l'audit a classé la page Écoles comme la plus faible (« mur de texte, zéro image, même structure ×7 quartiers »). C'est une page guide essentielle pour une famille expat.

**Independent Test** : ouvrir ecoles.html → chaque école (CEIP) est une card avec : nom, rue, badges (langue), 1-2 points forts ; une photo (mural CEIP) illustre la page.

**Acceptance Scenarios**:
1. **Given** la page écoles, **When** je regarde la liste des CEIP par quartier, **Then** chaque école est présentée en card cohérente : nom en Playfair, rue en Source Sans grise, badges terracotta/navy (ex: « Bilingue ES-VA », « Cantine », « Patio avec arbres »), 1-2 lignes de points forts.
2. **Given** une card école, **When** elle est survolée, **Then** un léger lift (translateY -2px) + ombre teintée se déclenche (transition 200-300ms).
3. **Given** la page, **When** je vois le haut de page, **Then** la photo `assets/img/ecoles-mural-ceip.jpg` (mural du CEIP Carles Salvador) illustre la section d'intro avec un alt descriptif et `loading="lazy"`.
4. **Given** le contenu existant, **When** je vérifie les noms, **Then** les écoles listées restent exactement celles du HTML actuel (CEIP Carles Salvador, CEIP Benimaclet, CEIP Doctor Olóriz, CEIP José Soto Micó, CEIP 9 d'Octubre, CEIP Campanar, CEIP Jaime Balmes, CEIP Eduardo Marquina) avec leurs rues exactes.

### US-03 — Contraste textes secondaires + état actif filtres quartiers + hiérarchie featured (P1)

**En tant que** lecteur,
**je veux** des textes secondaires (sous-titres, meta, badges, tags) avec un contraste suffisant et des filtres quartiers avec un état actif évident,
**afin que** la page soit lisible et que je comprenne immédiatement quel filtre est appliqué.

**Pourquoi ce priority** : l'audit vision a relevé sur quartiers « badges et tags secondaires parfois trop soft (lisibilité tags/scores) » et « pas de preuve visuelle d'état actif fort » sur les filtres. Sur la home : « textes gris moyens sur crème parfois limites ».

**Independent Test** : sur quartiers.html, cliquer le filtre « Top Famille » → le chip actif change de style nettement (fond navy ou terracotta plein) et la grille se filtre ; les tags (prix, scores /10) sont lisibles.

**Acceptance Scenarios**:
1. **Given** la page quartiers, **When** je regarde les chips de filtre, **Then** le chip actif a un fond plein (navy ou terracotta) avec texte blanc + le style inactif est un outline discret (le JS `initQuartierFilter` existant ajoute déjà `active` — il faut juste styler `.quartier-filter button.active` fortement).
2. **Given** la grille quartiers, **When** je lis les tags prix/scores, **Then** leur contraste est ≥ 4.5:1 sur le fond de card (assombrir les couleurs trop claires, ex: les tags verts pâles ou taupe clairs).
3. **Given** la card Benimaclet (featured), **When** je compare aux autres, **Then** elle se distingue clairement : bordure terracotta 2px + fond légèrement teinté + badge « Coup de cœur » bien visible.
4. **Given** la home, **When** je lis les sous-titres de sections et meta, **Then** leur couleur est assombrie pour passer ≥ 4.5:1 sur beige (vérifier les valeurs actuelles type #6b6b5a / gris moyens).

### US-04 — 7 nouvelles photos sur les pages sans image (P2)

**En tant que** visiteur,
**je veux** voir une photo réelle de Valencia sur chaque page guide,
**afin que** le site soit crédible et visuellement riche (aujourd'hui 7 pages sur 10 ont zéro image).

**Pourquoi ce priority** : le manque n°1 identifié par le skill redesign (grep -c "<img" = 0 sur 7 pages). Les photos sont déjà téléchargées, l'effort est purement d'intégration.

**Independent Test** : `grep -c "<img" pages/*.html` → plus aucune page à 0 ; chaque `<img>` a `alt` FR descriptif et `loading="lazy"` (sauf hero éventuel).

**Acceptance Scenarios**:
1. **Given** les fichiers images téléchargés dans `assets/img/`, **When** j'ouvre chaque page, **Then** :
   - `pages/ecoles.html` → `assets/img/ecoles-mural-ceip.jpg` (mural école Benimaclet) dans l'intro
   - `pages/scolarite.html` → `assets/img/scolarite-ceip.jpg` (bâtiment scolaire El Grau)
   - `pages/emploi.html` → `assets/img/emploi-port.jpg` (port de Valencia) dans la section salaires/emploi
   - `pages/sante.html` → `assets/img/sante-hopital.jpg` (hôpital Clínico) dans l'intro
   - `pages/administration.html` → `assets/img/admin-ayuntamiento.jpg` (mairie de Valencia) dans l'intro
   - `pages/checklists.html` → `assets/img/checklists-parc.jpg` (lac du Parc de Cabecera) en fin de page ou section détente
   - `pages/ressources.html` → `assets/img/ressources-tram.jpg` (tramway Metrovalencia) dans la section transports
2. **Given** chaque image insérée, **When** je vérifie le HTML, **Then** `alt` descriptif en français (pas « image »), `loading="lazy"`, chemins relatifs `assets/img/...`, pas de paramètres utm, pas de hotlink Wikimedia.
3. **Given** une image dans une section texte, **When** le viewport fait 390px, **Then** l'image est responsive (max-width 100%, border-radius cohérent avec le design ~12px).

### US-05 — Adresses restos en chips prix scannables (P2)

**En tant que** lecteur de la page Budget,
**je veux** voir les 8 adresses de restos testés sous forme de liste scannable avec fourchette de prix,
**afin que** je repère vite les options selon mon budget (aujourd'hui : wall of text).

**Pourquoi ce priority** : l'audit a relevé « listes restos = wall of text, peu de scannabilité (pas de chips prix, pas de méta visuelle) ». Les données existent, c'est une mise en forme.

**Independent Test** : scroller jusqu'aux adresses restos sur budget.html → chaque resto a nom, quartier/adresse, fourchette de prix visible (ex: « menú del día 13,50 € »), et le total de la liste est scannable en 2 secondes.

**Acceptance Scenarios**:
1. **Given** la section restos, **When** je regarde chaque adresse, **Then** elle est présentée en ligne/card compacte : nom en gras, adresse en secondaire, badge prix terracotta (ex: « ~13,50 €/pers. », « 25-35 € » selon le contenu réel de la page).
2. **Given** la liste, **When** je la scanne, **Then** les fourchettes proviennent des chiffres existants dans la page (ne pas inventer de prix — si la page ne donne pas de prix pour un resto, mettre la mention « menu del día ~13,50 € » seulement si elle y figure, sinon un tag de type de cuisine déjà présent).
3. **Given** la liste sur mobile, **When** je scrolle, **Then** les entrées s'empilent proprement en une colonne sans débordement.

### US-06 — Casser la répétition des grilles 3-cards sur la home (P2)

**En tant que** visiteur de la home,
**je veux** une variété de mises en page entre les sections (au lieu de « titre centré + 3 cards blanches » répété 4 fois),
**afin que** la page ait du rythme et ne ressemble pas à un template.

**Pourquoi ce priority** : l'audit vision home : « Répétition de pattern : trop de blocs titre centré + 3 cards blanches → effet catalogue / template Notion-Webflow ». La section-layout-repetition-ban du skill design-taste s'applique.

**Independent Test** : parcourir la home → au moins 2 sections adjacentes utilisent des layouts différents (ex: grille 3-cards, puis bandeau image full-width, puis grille asymétrique 2+1).

**Acceptance Scenarios**:
1. **Given** la section « Art de Vivre & Culture » (3 cards), **When** je compare à « Saveurs & Traditions » (4 cards), **Then** les deux ne partagent pas la même ossature : par exemple Art de Vivre en grille asymétrique (1 large + 2 étroites ou 2+1) ou avec une image pleine largeur en tête, Saveurs conserve sa grille mais avec variation (fond teinté différent, ou 1 carte en vedette).
2. **Given** la section « Heritage & Architecture », **When** je regarde, **Then** elle utilise un layout différent des deux autres (ex: bandeau photo `culture-plaza.jpg`/`culture-fallas.jpg` avec texte superposé, ou grille décalée).
3. **Given** les modifications, **When** le viewport fait 390px, **Then** toutes les grilles asymétriques se replient en une colonne propre (w-full, pas de débordement).
4. **Given** la home après modification, **When** je vérifie, **Then** les ids de sections (`histoire`, `art-de-vivre`, `heritage`, `saveurs`, `timeline`, `guide`) et le contenu texte restent identiques (SEO/ancres préservés).

### US-07 — Skip link + aria-current + focus states (P3)

**En tant que** utilisateur clavier / lecteur d'écran,
**je veux** un lien « Aller au contenu » en tête de page, l'état actif de la nav annoncé, et des focus visibles,
**afin que** le site soit utilisable sans souris.

**Pourquoi ce priority** : 0 page sur 10 a un skip link (audit code). C'est une exigence WCAG de base, coût minimal.

**Independent Test** : tabuler sur la home → le premier focus visible est « Aller au contenu » ; la page actuelle dans la nav a `aria-current="page"`.

**Acceptance Scenarios**:
1. **Given** chaque page (10 fichiers html), **When** je charge, **Then** un lien `<a class="skip-link" href="#main">Aller au contenu</a>` est le premier élément du body, stylé visible uniquement au focus (position absolute, top-left, fond navy, texte blanc).
2. **Given** la nav, **When** je suis sur une page, **Then** le lien correspondant à la page courante porte `aria-current="page"` et un style distinct (couleur terracotta ou soulignement).
3. **Given** les éléments interactifs (boutons, liens, chips filtres, cards cliquables), **When** ils reçoivent le focus clavier, **Then** un outline visible (2px terracotta ou navy, offset 2px) apparaît (ne pas supprimer outline, ou le remplacer par un focus-visible stylé).

### US-08 — tabular-nums sur les montants + grain subtil + hover/active polish (P3)

**En tant que** lecteur,
**je veux** des montants en euros alignés numériquement et un rendu de surface plus riche,
**afin que** les chiffres soient comparables d'un coup d'œil et que le fond ne soit pas plat.

**Pourquoi ce priority** : skill redesign : « Numbers in proportional font → tabular figures ». Le grain subtil casse la platitude des fonds beige. Coût CSS minimal.

**Acceptance Scenarios**:
1. **Given** les montants en € (KPI cards, calculateur, scénarios, restos), **When** je vérifie le CSS, **Then** ils portent `font-variant-numeric: tabular-nums` (via une classe `.amount`, `.kpi-card-amount`, `.calc-*` ou `body` ciblé).
2. **Given** le fond des pages, **When** je regarde, **Then** un grain subtil (SVG noise data-URI, opacité ≤ 0.04, `position: fixed`, `pointer-events: none`, z-index bas) est appliqué en overlay global — sans gêner la lecture ni les performances (pas de grain sur les images).
3. **Given** les boutons et liens, **When** je les survole, **Then** transition 200-300ms (fond légèrement plus foncé pour les boutons terracotta, soulignement pour les liens) et `:active` avec `transform: scale(0.98)` ou `translateY(1px)`.
4. **Given** `prefers-reduced-motion: reduce`, **When** je charge la page, **Then** le grain reste statique (pas d'animation) et les transitions sont instantanées (media query existante ou ajoutée).

### US-09 — Hero mobile allégé (P3)

**En tant que** visiteur mobile,
**je veux** un hero moins chargé (aujourd'hui : badge → titre → sous-titre → paragraphe → timer → 2 CTA empilés),
**afin que** le message principal et le CTA tiennent dans le premier écran sans scroll.

**Pourquoi ce priority** : l'audit mobile : « trop de blocs empilés → sensation tassée », « 2 boutons pleine largeur = stack vertical lourd ».

**Independent Test** : ouvrir la home en 390×844 → le titre, le sous-titre et un CTA primaire sont visibles sans scroll ; le second CTA est présent mais moins dominant.

**Acceptance Scenarios**:
1. **Given** le hero mobile, **When** je charge en 390px, **Then** la pile contient au maximum : badge (petit), titre, sous-titre court, 1 CTA primaire pleine largeur + 1 lien secondaire (ou CTA secondaire compact). Le timer (compte à rebours) passe sous le fold ou devient plus compact (réduire padding/gap).
2. **Given** le hero, **When** je regarde les espacements, **Then** les gaps entre éléments sont réguliers (rythme 8px) et le padding bas du hero laisse respirer avant la section suivante.
3. **Given** le hero desktop (1920px), **When** je vérifie, **Then** le layout desktop existant (photo + overlay + texte centré) reste inchangé.

---

## Functional Requirements (FR)

- **FR-001** : Toutes les modifications se font dans les fichiers existants : `index.html`, `pages/*.html` (9 pages), `css/style.css`, `js/main.js`. Aucun nouveau fichier requis (sauf éventuel style additionnel dans style.css).
- **FR-002** : Les classes CSS existantes sont réutilisées ou étendues ; les nouvelles classes suivent la convention kebab-case existante.
- **FR-003** : Les ancres de sections existantes (`#histoire`, `#art-de-vivre`, etc.) ne changent pas. Les nouvelles ancres budget suivent les ids/sections existantes de budget.html (utiliser les titres de sections, ajouter des `id` si absents).
- **FR-004** : Les images : chemins relatifs `assets/img/xxx.jpg`, `alt` FR descriptif, `loading="lazy"`, `width`/`height` ou `aspect-ratio` CSS pour éviter le CLS.
- **FR-005** : Le JS existant (IntersectionObserver, navbar, nav mobile, calculateur, filtres quartiers) n'est pas cassé. Si un scroll-spy est ajouté pour la US-01, utiliser IntersectionObserver (jamais `window.addEventListener('scroll')`).
- **FR-006** : Aucun em-dash (—) ni en-dash (–) visible ajouté dans les nouveaux textes. Utiliser le trait d'union.
- **FR-007** : Pas de données personnelles de la famille (prénoms enfants, adresse exacte, photos identifiables) ajoutées. Les photos Wikimedia sont des bâtiments/lieux publics, pas des portraits de la famille.
- **FR-008** : Liens externes : `rel="noopener noreferrer"` si target="_blank".

## Success Criteria (SC)

- **SC-001** : `grep -c "<img" pages/*.html` → 0 page à 0 image.
- **SC-002** : `grep -c "skip-link" index.html pages/*.html` → 10/10.
- **SC-003** : `grep -c "tabular-nums" css/style.css` → ≥ 1, appliqué aux montants.
- **SC-004** : Aucun `—` ni `–` ajouté (grep des fichiers modifiés, hors contenu existant).
- **SC-005** : Les 10 pages passent un screenshot Playwright 1920×1080 + 390×844 sans débordement horizontal (`document.documentElement.scrollWidth <= window.innerWidth`).
- **SC-006** : La home conserve ses ids de sections et son contenu texte (diff contrôlable).
- **SC-007** : Le budget calculator et le filtre quartiers fonctionnent après modification (test Playwright : cliquer un onglet scénario → total change ; cliquer un filtre → la grille se filtre).

## Assumptions

- Les 7 photos sont déjà dans `assets/img/` (téléchargées, validées JPEG).
- Le design Stitch prime sur toute règle anti-slop (fond beige conservé).
- Le workflow agy : agy implémente, Hermes fait la QA visuelle (screenshots + vision), boucle spec2 si écart.

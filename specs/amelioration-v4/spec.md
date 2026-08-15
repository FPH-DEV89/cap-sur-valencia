# Feature Specification: Design v4 — Niveau senior / Awwwards-quality (Cap sur Valencia)

**Feature Branch**: `improve-design-v4`
**Created**: 2026-08-15
**Status**: Draft — prête pour implémentation agy

**Input**: « Tu n'es pas capable de faire avec toutes les compétences et skills que tu as ? Regarde ce que les meilleurs sites font et ce que les meilleurs designers seniors savent faire. »

**Benchmark (15/08/2026)** : Monocle Travel Guide (photographie lourde, sections par intérêt, point de vue éditorial), Wallpaper* City Guides (couverture Pantone, curation, sections par intérêt), LOST iN (design NODE Berlin Oslo), standards Awwwards (art direction unique, asset system honnête, motion narrative, micro-interactions). Skills appliqués : design-taste-frontend, ui-design-references, redesign-existing-projects.

---

## Direction artistique (le « design read »)

**Reading this as**: city guide premium éditorial pour famille expat, langage « magazine méditerranéen chaleureux », lean vers éditorial serif (Playfair) + photos réelles traitées + motion narrative douce.

- **DESIGN_VARIANCE: 7** (grilles asymétriques, bandeaux pleine largeur, pull-quotes — sans chaos)
- **MOTION_INTENSITY: 6** (reveals différenciés, parallax léger, hover physics, progress bar — tout honoré par prefers-reduced-motion)
- **VISUAL_DENSITY: 4** (aéré, éditorial, pas de cockpit)

**Thèse visuelle** : « Valencia se vit avant d'y être » — chaque section raconte un moment de la ville (photo → titre éditorial → détail chiffré → micro-interaction). Le beige Stitch est la matière papier, le navy l'encre, le terracotta l'accent soleil.

---

## Constitution (héritée v1-v3 + ajouts)

1. Design Stitch = loi. Palette #fbfbe2/#001626/#924b26, Playfair + Source Sans 3. On élève l'exécution, pas la direction.
2. Zéro contenu perdu, zéro fonctionnalité cassée, zéro lien mort.
3. Photos réelles existantes (13 dans assets/img) — traitement via CSS, pas de nouvelles images IA.
4. Chiffres réels conservés (2 480/3 425/4 435 €, 11 étapes admin, etc.).
5. **Progressive enhancement obligatoire** : `.js .fade-in` pattern — contenu visible sans JS (pitfall 6 du skill, commit 2421e04).
6. **Zéro em-dash (—) / en-dash (–)** dans les nouveaux textes.
7. **Motion : `transform`/`opacity` uniquement**, jamais de scroll listener (`window.addEventListener('scroll')` interdit — IntersectionObserver / CSS scroll-driven seulement), `prefers-reduced-motion: reduce` = tout statique.
8. Pas d'eyebrows répétés (max 1/3 sections), pas de cartes monotones identiques, pas d'ombres noires (teintées), pas de pill "New/Beta".
9. Accessibilité : focus visible (focus-visible), contrastes AA, aria-current existants conservés.
10. **Un seul accent : terracotta.** La cohérence couleur est verrouillée sur chaque page.

---

## User Stories

### US-01 — Favicon + identité onglet + 404 (P0 — détail senior immédiat)

**En tant que** visiteur,
**je veux** un favicon de marque (aujourd'hui : 404), un titre d'onglet propre et une vraie page 404,
**afin que** le site soit fini jusque dans l'onglet du navigateur.

**Acceptance Scenarios**:
1. **Given** le site, **When** je charge n'importe quelle page, **Then** un `<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">` est présent dans le `<head>` de TOUTES les pages (10 fichiers), et `assets/favicon.svg` existe : monogramme simple « CV » ou ancre/soleil stylisé en SVG, 2 couleurs max (navy + terracotta), fond beige ou transparent, lisible à 16px.
2. **Given** le SVG, **When** je regarde, **Then** c'est un marque simple et géométrique (autorisé par les règles : brand mark simple), pas une illustration sketchy.
3. **Given** une URL inexistante (ex: /pages/404.html ou une route cassée), **When** GitHub Pages renvoie 404, **Then** une page `404.html` à la racine du repo existe : fond beige, titre Playfair « Perdus dans Valencia ? », texte court + lien retour accueil (bouton terracotta), navigation conservée — GitHub Pages sert `404.html` automatiquement.

### US-02 — Hero index cinématique (P1 — la première impression)

**En tant que** visiteur,
**je veux** un hero qui raconte Valencia en un coup d'œil : photo traitée, kicker éditorial, titre avec mot accent, entrée en cascade,
**afin que** la première seconde soit mémorable (aujourd'hui : photo + overlay correct mais « template landing »).

**Acceptance Scenarios**:
1. **Given** le hero index, **When** il se charge, **Then** les éléments entrent en cascade avec stagger (kicker → titre → sous-titre → meta → CTA), délais 60-120ms, transition `opacity + translateY(16px)`, durée 0.6-0.8s ease-out — gated par `.js` (visible sans JS) et désactivé en reduced-motion.
2. **Given** le titre hero, **When** je regarde, **Then** il utilise l'emphase éditoriale : un mot-clé (ex: « Valencia ») en italique Playfair avec la couleur terracotta ou un traitement différent (pas de serif injecté dans du sans — même famille), `text-wrap: balance`, tracking serré sur les autres mots.
3. **Given** la photo hero, **When** je regarde, **Then** elle a un traitement cinématique : dégradé navy en bas renforcé (lisibilité), léger grain déjà en place, et un **zoom lent subtil** (scale 1.05 → 1, 4-6s ease-out, une fois au chargement, reduced-motion = statique).
4. **Given** le hero, **When** le viewport est mobile 390px, **Then** la pile reste légère (max 4 éléments texte), CTA primaire visible sans scroll (déjà en place — conserver, ne pas regresser).
5. **Given** le countdown, **When** je regarde, **Then** il est raffiné : chiffres en tabular-nums (déjà), labels discrets, séparateur propre — pas une grosse pill criarde (alléger si nécessaire).

### US-03 — Typographie éditoriale complète (P1 — la marque du magazine)

**En tant que** lecteur,
**je veux** une typographie de magazine : échelle fluide, lignes équilibrées, tracking soigné,
**afin que** le site se lise comme un beau magazine plutôt qu'une page web standard.

**Acceptance Scenarios**:
1. **Given** les titres (h1-h3), **When** je vérifie le CSS, **Then** ils ont `text-wrap: balance` (h1-h3) et le corps `text-wrap: pretty` ; les titres display ont un tracking négatif (`letter-spacing: -0.01em` à `-0.03em` selon la taille) ; `text-wrap: balance` appliqué sur au moins les titres de section.
2. **Given** l'échelle typographique, **When** je vérifie, **Then** les tailles sont fluides avec `clamp()` sur les grands titres (ex: h1 hero ~`clamp(2.8rem, 8vw, 5.5rem)`, h2 section ~`clamp(2rem, 4.5vw, 3rem)`) — les clamp() existants (lignes 152-162, 626) sont harmonisés en une échelle cohérente.
3. **Given** le corps de texte, **When** je vérifie, **Then** la longueur de ligne est limitée (~65-70ch) sur les blocs de lecture longue (`max-width: 65ch` sur `.content-body p`, sans casser les layouts existants).
4. **Given** les montants et chiffres, **When** je vérifie, **Then** `font-variant-numeric: tabular-nums` reste appliqué (déjà en place — ne pas casser).
5. **Given** la sélection de texte, **When** je sélectionne du texte, **Then** `::selection` est stylé (fond terracotta, texte beige/blanc) — sur toutes les pages via style.css.

### US-04 — Motion narrative : parallax léger + hover physics + reveals différenciés (P1)

**En tant que** visiteur,
**je veux** un site qui vit au scroll : images en parallax doux, cartes qui réagissent au survol,
**afin que** l'expérience soit celle d'un site conçu (aujourd'hui : fade-in uniforme + zéro parallax).

**Acceptance Scenarios**:
1. **Given** les bandeaux photo (`.banner-photo`, images de section home), **When** je scrolle, **Then** un parallax léger est appliqué : l'image se translate légèrement (10-15% de la hauteur, `transform: translateY` via IntersectionObserver ou CSS `animation-timeline: view()`) — pas de scroll listener. Les images dans les cards ne bougent pas (perf).
2. **Given** les cards cliquables (quartier-card, guide-card, kpi-card, tradition-card), **When** je les survole, **Then** un lift (`translateY(-4px)` + ombre teintée terracotta/navy légère) et la photo interne (si présente) zoom doucement (`scale(1.04)`, 0.5s) — transition 200-300ms.
3. **Given** les boutons (`.btn-primary`, `.btn-outline`), **When** je les survole, **Then** un effet physique : primary = fond légèrement plus foncé + translateY(-1px), outline = fond terracotta-ghost ; `:active` = scale(0.98) (déjà partiellement — unifier).
4. **Given** les reveals, **When** je scrolle, **Then** chaque section a une révélation adaptée (pas le même fade-in partout) : sections texte = fade + translateY 20px ; bandeaux photo = fade + scale 0.98 → 1 ; grilles = stagger sur les cards (délai 60ms par card) — tout gated `.js` + reduced-motion statique.
5. **Given** la barre de progression, **When** je scrolle sur les longues pages, **Then** une barre fine (3px, terracotta) en haut de la fenêtre (fixée sous la nav ou en haut du viewport) indique la progression — CSS `animation-timeline: scroll()` si supporté avec fallback, ou IntersectionObserver sur les sections.

### US-05 — Pull-quotes + bandeaux éditoriaux dans les articles (P2 — le rythme du magazine)

**En tant que** lecteur des pages guides (admin, santé, école, budget),
**je veux** des citations mises en valeur et des pauses visuelles,
**afin que** les longs articles respirent comme un magazine (aujourd'hui : longues séquences de texte).

**Acceptance Scenarios**:
1. **Given** une page guide avec du contenu narratif fort (admin, santé, ecoles, budget), **When** je scrolle, **Then** au moins UNE pull-quote par page (choisir la phrase la plus frappante du texte existant, NE PAS en inventer) : grande citation Playfair italique, guillemets typographiques « », bordure gauche terracotta fine ou trait, fond légèrement teinté, max 3 lignes.
2. **Given** la pull-quote, **When** elle entre dans le viewport, **Then** elle se révèle (fade + translateY, gated .js, reduced-motion statique).
3. **Given** les longues pages, **When** je scrolle, **Then** un bandeau photo pleine largeur (réutiliser une photo existante pertinente de la page) ou une section à fond navy avec texte beige insère une pause visuelle à mi-parcours (une seule par page, pas de spam).
4. **Given** la page école, **When** je regarde, **Then** la citation d'un parent expat (texte existant du « vécu ») est utilisée en pull-quote si le contenu s'y prête.

### US-06 — Navigation animée + état actif + CTA nav raffiné (P2)

**En tant que** visiteur,
**je veux** une navigation qui réagit : lien actif souligné animé, header qui se densifie au scroll,
**afin que** l'orientation soit évidente et agréable.

**Acceptance Scenarios**:
1. **Given** les liens de nav, **When** je survole, **Then** un soulignement animé apparaît (2px terracotta, grow de gauche à droite, 0.25s ease) — remplace ou complète le style actuel sans casser `aria-current`.
2. **Given** le lien de la page courante, **When** je charge, **Then** il garde `aria-current="page"` + style distinct existant (terracotta ou soulignement) — pas de régression.
3. **Given** le header, **When** je scrolle au-delà de 60px, **Then** il se densifie : padding réduit, fond beige plus opaque (95%+) + blur léger + ombre basse subtile (état `.scrolled` existant — l'améliorer légèrement, ne pas casser).
4. **Given** la nav sur mobile, **When** j'ouvre le menu, **Then** le hamburger a une animation (transition vers X, déjà présente — vérifier fluidité), et le menu s'affiche avec un léger fondu.

### US-07 — Cards différenciées : fini les grilles monotones (P2)

**En tant que** visiteur de la home,
**je veux** des grilles avec des compositions variées (bento, asymétrie, une carte en vedette),
**afin que** chaque section ait une personnalité (aujourd'hui : encore plusieurs blocs « 3 cards identiques »).

**Acceptance Scenarios**:
1. **Given** la section « Art de Vivre & Culture », **When** je regarde, **Then** la composition est asymétrique : une carte large avec photo (saveurs-paella ou culture-plaza) + 2 cartes texte plus étroites, tailles de grille différentes (ex: 2fr 1fr 1fr ou 1 carte pleine largeur en haut puis 2 en dessous) — pas 3 égales.
2. **Given** la section « Saveurs & Traditions » (4 items), **When** je regarde, **Then** la grille est en 2×2 avec une carte en vedette (première, plus grande ou avec photo + fond teinté) — asymétrie contrôlée.
3. **Given** la section « Quartiers » de la home, **When** je regarde, **Then** les 3 cartes gardent leur fonction (aperçu + prix) mais une seule (Benimaclet) est visuellement en vedette (bordure terracotta, badge « Coup de cœur », comme la page quartiers) — cohérence avec la page quartiers.
4. **Given** toutes les grilles modifiées, **When** viewport 390px, **Then** tout se replie en colonne unique propre, zéro débordement.
5. **Given** les ids de sections (histoire, art-de-vivre, heritage, saveurs, timeline, guide), **When** je vérifie, **Then** ils restent identiques (SEO/ancres).

### US-08 — Footer raffiné + back-to-top (P3)

**En tant que** visiteur,
**je veux** un footer soigné avec un retour en haut,
**afin que** la fin de page soit élégante et pratique.

**Acceptance Scenarios**:
1. **Given** le footer, **When** je regarde, **Then** il est raffiné sans refonte : titre de colonne en petites capitales ou Playfair, liens espacés, séparateur haut fin navy/terracotta, mentions légales existantes conservées (copyright 2026).
2. **Given** les longues pages, **When** je scrolle vers le bas, **Then** un bouton « Retour en haut » apparaît (flèche ↑ dans un cercle navy, fond beige, apparaît après ~600px de scroll, disparaît en haut — IntersectionObserver ou check discret, pas de scroll listener ; réduit en mobile).
3. **Given** le bouton, **When** je clique, **Then** scroll fluide vers le haut (scroll-behavior smooth existant).

### US-09 — Barre de progression de lecture (P3 — inclus dans US-04.5, détaillé ici)

Couvert par US-04 scénario 5. S'assurer qu'elle est sur : index (si long), budget, admin, ressources, checklists, ecoles. Fine (2-3px), terracotta, au top du viewport (z-index sous la nav si nav sticky, ou au-dessus — décider selon le layout, cohérent partout).

---

## Functional Requirements

- **FR-001** : Fichiers : `index.html`, `pages/*.html` (9), `css/style.css`, `js/main.js`, `404.html` (nouveau), `assets/favicon.svg` (nouveau).
- **FR-002** : Le pattern `.js .fade-in` est respecté pour TOUTE nouvelle animation (visible sans JS). Vérifier avec Playwright `javaScriptEnabled: false` sur les pages modifiées : 0 élément caché.
- **FR-003** : Pas de `window.addEventListener('scroll')` ajouté. Parallax = IntersectionObserver + rAF (avec cleanup) OU CSS `animation-timeline: view()` avec fallback statique.
- **FR-004** : `prefers-reduced-motion: reduce` désactive : zoom hero, parallax, reveals (déjà), hover lifts (transitions instantanées), progress bar animée (statique OK).
- **FR-005** : Zéro em-dash/en-dash dans les nouveaux contenus (pull-quotes = phrases EXISTANTES des pages, ne pas réécrire avec des tirets).
- **FR-006** : Les nouvelles classes suivent kebab-case : `.pull-quote`, `.reading-progress`, `.back-to-top`, `.banner-section`, `.card-featured`, etc.
- **FR-007** : Les ancres/ids existants ne changent pas. Les liens internes restent valides.
- **FR-008** : Performance : pas de nouvelle dépendance, pas de librairie, images existantes réutilisées, `loading="lazy"` conservé.
- **FR-009** : GitHub Pages : `404.html` à la racine fonctionne automatiquement ; `assets/favicon.svg` servi en relatif.

## Success Criteria

- **SC-001** : `grep -c "favicon" index.html pages/*.html` = 10/10 + fichier `assets/favicon.svg` existe.
- **SC-002** : `404.html` existe à la racine, chargé par GitHub Pages (curl → 404 status + contenu).
- **SC-003** : `grep -c "text-wrap" css/style.css` ≥ 3 (balance sur titres + pretty sur corps).
- **SC-004** : `grep -c "::selection" css/style.css` ≥ 1.
- **SC-005** : `grep -c "reading-progress\|progress" css/style.css` ≥ 1 + élément présent sur ≥ 5 pages longues.
- **SC-006** : Pull-quotes présentes sur ≥ 4 pages guides (`grep -c "pull-quote" pages/*.html` ≥ 4 fichiers).
- **SC-007** : Zéro em-dash/en-dash dans le diff (`git diff | grep -E "^\+" | grep -c "—"` = 0).
- **SC-008** : Playwright : 10 pages sans JS → 0 `.fade-in` caché ; 10 pages desktop+mobile → 0 overflow ; zéro pageerror console.
- **SC-009** : Navigation : `aria-current` conservé sur les 10 pages ; menu mobile fonctionne.
- **SC-010** : Hover cards : vérification Playwright (hover sur une card → transform/scale appliqué).
- **SC-011** : Le contenu (11 étapes admin, 4 phases emploi, 49+ liens ressources, chiffres budget) est intégralement conservé.

## Assumptions

- Les photos existantes suffisent (13 images) — pas de nouvelle recherche.
- La direction « magazine méditerranéen » reste dans la palette Stitch (le beige est un choix utilisateur qui prime sur les règles anti-slop).
- agy implémente, Hermes QA visuelle (screenshots + vision + Playwright), boucle spec2 si écart.
- Le benchmark (Monocle/Wallpaper*/LOST iN/Awwwards) guide l'intention, pas la copie de layout spécifique.

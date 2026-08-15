# Feature Specification: v5 — Espacement + Images + SEO technique (Cap sur Valencia)

**Feature Branch**: `improve-design-v5`
**Created**: 2026-08-15
**Status**: Draft — prête pour implémentation agy

**Input Florian** : « Parfois entre deux sections il y a trop de vide. J'aimerai que tu me rajoutes des images réelles libre de droit sur certains des articles et dans certaines pages. Comment exploser sa visibilité ? Comment le monétiser ? » (la visibilité + monétisation sont traitées à part dans le rapport — ici : espacement + images + base SEO technique)

---

## Constitution (identique v1-v4)

1. Design Stitch = loi (#fbfbe2/#001626/#924b26, Playfair + Source Sans 3).
2. Zéro contenu perdu, zéro lien cassé, zéro fonctionnalité cassée.
3. Progressive enhancement `.js .fade-in` obligatoire (visible sans JS).
4. Zéro em-dash (—) / en-dash (–) dans les nouveaux textes.
5. Pas de scroll listener ; IntersectionObserver ou CSS scroll-driven.
6. Photos locales uniquement (les 5 nouvelles sont déjà dans `assets/img/`).
7. Les ancres/ids existants ne changent pas.

---

## User Stories

### US-01 — Réduire le vide excessif entre les sections (P0)

**En tant que** lecteur,
**je veux** des transitions entre sections plus resserrées,
**afin que** la page paraisse dense et rythmée, pas vide (aujourd'hui : `.section { padding: var(--space-2xl) 0 }` = 6rem haut + 6rem bas = ~190px de vide entre chaque bloc).

**Diagnostic précis** :
- `css/style.css` ligne ~322 : `.section { padding: var(--space-2xl) 0; }` avec `--space-2xl: 6rem` → **12rem (192px) de vide total entre sections consécutives**.
- `--space-xl: 4rem`, `--space-2xl: 6rem` (lignes 88-89 du :root).
- Il y a aussi des blocs avec des marges additionnelles (`margin-bottom: 2rem`+ sur certains conteneurs).

**Acceptance Scenarios**:
1. **Given** le CSS, **When** je vérifie `.section`, **Then** le padding vertical passe à `var(--space-xl)` (4rem) desktop (au lieu de 6rem), et à `clamp(2.5rem, 6vw, 3.5rem)` sur mobile (media query existante ~ligne 3369).
2. **Given** les sections `.section-alt` et les sections spéciales (hero, bandeaux), **When** je vérifie, **Then** leur padding reste adapté mais sans excès (> 5rem de padding vertical par côté interdit sauf hero).
3. **Given** les cas particuliers (`.section` qui suit un `.section-alt` ou un bandeau navy), **When** je vérifie, **Then** pas de double padding : une section qui suit une autre n'accumule pas 2× 4rem (vérifier si besoin d'un sélecteur `.section + .section { padding-top: 2rem }` ou ajuster les `margin`).
4. **Given** le rendu, **When** je charge la home et les pages guides en desktop 1920, **Then** l'espace entre 2 sections consécutives est visuellement entre 64px et 128px (pas 190px+), sans coller non plus.
5. **Given** le rendu mobile 390px, **When** je charge, **Then** l'espacement est réduit proportionnellement (~40-64px).

### US-02 — 5 nouvelles photos insérées dans les articles (P1)

**En tant que** lecteur,
**je veux** des photos réelles supplémentaires dans les articles longs,
**afin que** le contenu soit illustré à plusieurs endroits (aujourd'hui : 1 image par page guide).

**Photos déjà téléchargées (validées JPEG)** :
- `assets/img/budget-mercado-interieur.jpg` (intérieur du Mercado Central)
- `assets/img/quartiers-rue.jpg` (rue typique, Calle del Altar de San Vicente)
- `assets/img/checklists-oranger.jpg` (oranger chargé de fruits)
- `assets/img/sante-pharmacie.jpg` (façade de pharmacie valencienne)
- `assets/img/ressources-gare-nord.jpg` (façade de la gare du Nord la nuit)

**Acceptance Scenarios**:
1. **Given** `pages/budget.html`, **When** je scrolle vers la section « Manger dehors » ou « Le marché », **Then** `budget-mercado-interieur.jpg` est inséré (max-width 100%, border-radius 12px cohérent, `loading="lazy"`, alt FR : « Intérieur du Mercado Central de Valencia, étals colorés ») — à placer dans la section la plus pertinente selon le contenu existant (marché/courses).
2. **Given** `pages/quartiers.html`, **When** je scrolle dans le bloc « Le centre-ville » (Ruzafa/Ensanche/El Carmen), **Then** `quartiers-rue.jpg` est inséré avec alt FR : « Rue typique du centre de Valencia » + légende courte.
3. **Given** `pages/checklists.html`, **When** je scrolle vers la section « Avant de partir » ou détente, **Then** `checklists-oranger.jpg` est inséré avec alt FR : « Orangers chargés de fruits à Valencia ».
4. **Given** `pages/sante.html`, **When** je scrolle vers la section mutuelle/pharmacie, **Then** `sante-pharmacie.jpg` est inséré avec alt FR : « Façade de pharmacie à Valencia ».
5. **Given** `pages/ressources.html`, **When** je scrolle vers la section transports, **Then** `ressources-gare-nord.jpg` est inséré avec alt FR : « Façade de la gare du Nord de Valencia de nuit ».
6. **Given** chaque image, **When** je vérifie, **Then** `loading="lazy"`, `width`/`height` ou `aspect-ratio` CSS pour éviter le CLS, placement dans une figure avec légende si le style existant le permet (`.content-photo` existe), sinon image simple alignée avec la charte.
7. **Given** les pages, **When** je vérifie le responsive 390px, **Then** zéro débordement.

### US-03 — SEO technique : sitemap.xml + robots.txt + schema JSON-LD (P1)

**En tant que** propriétaire du site,
**je veux** une base SEO technique : sitemap, robots.txt, données structurées,
**afin que** Google/Bing indexent correctement le site (aujourd'hui : AUCUN sitemap, AUCUN robots.txt, AUCUN schema — constat 15/08/2026).

**Acceptance Scenarios**:

1. **Given** le repo, **When** je vérifie la racine, **Then** un fichier `sitemap.xml` existe avec les 10 URLs : `https://fph-dev89.github.io/cap-sur-valencia/` (priority 1.0) + les 9 pages `pages/*.html` (priority 0.8), avec `<lastmod>` = date du jour (2026-08-15), `<changefreq>monthly</changefreq>`.
2. **Given** le repo, **When** je vérifie la racine, **Then** un fichier `robots.txt` existe :
   ```
   User-agent: *
   Allow: /
   Sitemap: https://fph-dev89.github.io/cap-sur-valencia/sitemap.xml
   ```
   (pas de Crawl-delay, pas de Disallow inutile).
3. **Given** `index.html`, **When** je vérifie le `<head>`, **Then** un schema JSON-LD `WebSite` + `Organization` est ajouté (nom « Cap sur Valencia », url github.io, logo assets/favicon.svg, description). Pas de `SearchAction` si pas de recherche sur le site.
4. **Given** les 10 pages, **When** je vérifie, **Then** un schema `BreadcrumbList` est ajouté à chaque page intérieure (Accueil → [Nom de la page]) et `Article`/`BlogPosting` sur les pages guides avec titre, description, datePublished (2026-08-15), image (og:image existante ou première image de la page). Le JSON-LD doit être valide (tester la syntaxe).
5. **Given** les pages avec section FAQ ou questions/réponses (budget, sante, administration, ecoles — vérifier le contenu), **When** je vérifie, **Then** un schema `FAQPage` est ajouté UNIQUEMENT si les questions/réponses existent réellement dans le contenu visible (ne pas inventer de Q/R). Si aucune FAQ visible, ne pas ajouter.
6. **Given** le `og:image`, **When** je vérifie les meta, **Then** il pointe vers un JPEG/PNG (jamais SVG — pitfall SEO) : vérifier que les og:image existants sont des .jpg (ils le sont : hero-ciudad-arte.jpg etc.) ; si un og:image manque sur une page, l'ajouter avec l'image de la page.
7. **Given** les meta descriptions, **When** je vérifie les 10 pages, **Then** chaque page a une meta description 140-160 chars avec mot-clé principal (la plupart existent déjà — vérifier, compléter celles qui manquent SANS réécrire celles qui sont bonnes).

**Important** : ne pas toucher aux canonicals existants (déjà corrects vers github.io, vérifiés en v1).

---

## Functional Requirements

- **FR-001** : Fichiers modifiés : `css/style.css`, `index.html`, `pages/*.html` (9), + nouveaux `sitemap.xml`, `robots.txt` à la racine.
- **FR-002** : Les images : chemins relatifs `assets/img/xxx.jpg`, alt FR, lazy loading, dimensions/aspect-ratio.
- **FR-003** : JSON-LD : syntaxe valide (échapper les apostrophes/guillemets), inséré en `<script type="application/ld+json">` dans le `<head>`.
- **FR-004** : Zéro em-dash dans les nouveaux textes (alt, légendes, descriptions).
- **FR-005** : Aucune donnée personnelle de la famille dans le schema (pas de noms d'enfants, pas d'adresse).
- **FR-006** : Le `.js .fade-in` pattern est respecté (les nouvelles images ne sont pas cachées sans JS).
- **FR-007** : Pas de scroll listener ajouté.

## Success Criteria

- **SC-001** : `grep "padding: var(--space-2xl)" css/style.css` → remplacé par `var(--space-xl)` ou équivalent réduit ; vérifier visuellement l'espacement home entre 2 sections.
- **SC-002** : `grep -c "budget-mercado-interieur\|quartiers-rue\|checklists-oranger\|sante-pharmacie\|ressources-gare-nord" pages/*.html` → 5 fichiers.
- **SC-003** : `sitemap.xml` existe + contient 10 URLs ; `robots.txt` existe avec Sitemap.
- **SC-004** : `grep -c "application/ld+json" index.html pages/*.html` → ≥ 10 (toutes les pages ont au moins un schema).
- **SC-005** : Les JSON-LD sont syntaxiquement valides (parse JSON OK — vérifier avec un script node simple).
- **SC-006** : Zéro em-dash dans le diff.
- **SC-007** : Playwright : 10 pages sans JS → 0 `.fade-in` caché ; 10 pages desktop+mobile → 0 overflow.
- **SC-008** : Le contenu existant est intégralement conservé (pas de réécriture de texte éditorial).

## Assumptions

- Le SEO « exploser la visibilité » (stratégie contenu, netlinking, GSC) et la monétisation sont traités dans le rapport séparé — cette spec pose la BASE technique.
- agy implémente, Hermes QA, boucle spec2 si écart.

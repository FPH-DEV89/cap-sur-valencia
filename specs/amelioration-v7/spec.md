# Feature Specification: v7 — Page Blog + Flux RSS (Cap sur Valencia)

**Feature Branch**: `improve-design-v7`
**Created**: 2026-08-15
**Status**: Draft — prête pour implémentation agy

**Input Florian** : « Est-ce qu'il me faut un vrai nom de domaine ? Si ça n'existe pas encore, prépare la page blog pour y publier du contenu de manière hebdomadaire. »

---

## Contexte

- Site statique HTML/CSS/JS vanilla sur GitHub Pages (`https://fph-dev89.github.io/cap-sur-valencia/`).
- 10 pages existantes : index + 9 guides (budget, quartiers, ecoles, scolarite, emploi, sante, administration, checklists, ressources).
- **Pas de page blog** actuellement. Les articles devront être publiés de façon hebdomadaire : il faut une infrastructure simple : page index blog + template d'article + flux RSS + liens nav/footer/sitemap.
- Les noms de domaine `capsurvalencia.fr`, `cap-sur-valencia.fr`, `capsurvalencia.com`, `cap-sur-valencia.com` sont TOUS disponibles (vérifié RDAP 15/08/2026) — la stratégie domaine est traitée dans le rapport, pas dans cette spec (les URLs restent sur github.io pour l'instant, canonical inchangés).

## Constitution

1. Design Stitch = loi (#fbfbe2/#001626/#924b26, Playfair + Source Sans 3). La page blog s'intègre au design existant (header nav, footer, `.section`, cards 12px, ombres teintées).
2. Zéro contenu perdu, zéro lien cassé. Les pages existantes ne sont PAS modifiées sauf : nav (ajout lien Blog), footer (ajout lien Blog), sitemap.xml (ajout URLs blog).
3. Progressive enhancement `.js .fade-in` (visible sans JS).
4. Zéro em-dash (—) / en-dash (–) dans les nouveaux textes.
5. Photos locales existantes réutilisées (pas de nouvelle recherche).
6. Les articles sont des fichiers `.html` statiques dans `blog/` (un fichier par article, nom `blog/AAAA-MM-JJ-slug.html`) — simple, pas de CMS, compatible GitHub Pages.

---

## User Stories

### US-01 — Page index du blog (P0)

**En tant que** visiteur,
**je veux** une page `/blog.html` qui liste les articles publiés,
**afin que** je découvre le contenu hebdomadaire du site.

**Acceptance Scenarios**:
1. **Given** la page `pages/blog.html` créée, **When** je la charge, **Then** elle a : le header nav identique aux autres pages (avec `aria-current="page"` sur le lien Blog), un hero de page sobre (badge « Blog », H1 « Le journal de bord » en Playfair, chapô court 1-2 lignes), et une liste d'articles.
2. **Given** la liste d'articles, **When** aucun article n'est encore publié (ou 1 seul), **Then** la page affiche proprement les articles existants en cards (titre Playfair, date lisible « 16 août 2026 », extrait 1-2 lignes, image si dispo, lien « Lire l'article → ») — jamais une page vide cassée : s'il n'y a qu'un article, il s'affiche en card pleine largeur.
3. **Given** la page, **When** je vérifie le responsive, **Then** les cards passent en 1 colonne sur mobile, zéro débordement.

### US-02 — Premier article + template réutilisable (P0)

**En tant que** éditeur du site,
**je veux** un premier article publié + un template clair pour les suivants,
**afin que** publier chaque semaine soit rapide (copier le template, remplacer le contenu).

**Acceptance Scenarios**:
1. **Given** le dossier `blog/`, **When** je regarde, **Then** il contient `blog/2026-08-16-bienvenue.html` : un vrai article de lancement (titre « Bienvenue sur le journal de bord », date 16 août 2026, contenu authentique de 300-500 mots racontant le projet : famille de 5, départ 2028, pourquoi ce blog, ce qu'on y trouvera chaque semaine). Le contenu est RÉDIGÉ (pas de lorem ipsum), ton « journal de bord » existant du site, zéro em-dash.
2. **Given** l'article, **When** je vérifie sa structure, **Then** il a : header nav, `<article>` avec H1 Playfair, date en meta, paragraphes, une image existante réutilisée (ex: `../assets/img/hero-ciudad-arte.jpg` avec alt FR), footer, breadcrumb retour blog, schema JSON-LD `BlogPosting` (headline, datePublished 2026-08-16, author Florian, image).
3. **Given** le template, **When** je veux publier un nouvel article, **Then** la structure est évidente : copier `blog/2026-08-16-bienvenue.html`, changer le slug (date-slug), le title/meta, le H1, la date, le contenu, l'image — puis ajouter la card dans `pages/blog.html` et l'URL dans `feed.xml` + `sitemap.xml`.

### US-03 — Flux RSS (P1)

**En tant que** lecteur / agrégateur,
**je veux** un flux RSS `feed.xml`,
**afin que** les lecteurs puissent s'abonner (et Google News / agrégateurs détecter les mises à jour).

**Acceptance Scenarios**:
1. **Given** le fichier `feed.xml` à la racine, **When** je l'ouvre, **Then** c'est un flux RSS 2.0 valide : `<channel>` avec title « Cap sur Valencia », link github.io, description, language fr, et un `<item>` pour l'article de bienvenue (title, link, guid, pubDate « Sat, 16 Aug 2026 », description).
2. **Given** le flux, **When** je vérifie, **Then** le XML est bien formé (pas de caractères non échappés, `&` → `&amp;`).

### US-04 — Navigation + footer + sitemap (P1)

**En tant que** visiteur,
**je veux** trouver le blog depuis la nav et le footer,
**afin que** le contenu soit accessible.

**Acceptance Scenarios**:
1. **Given** la nav des 10 pages existantes, **When** je regarde, **Then** un lien « Blog » (`pages/blog.html`) est ajouté dans le menu principal (desktop + mobile hamburger) de TOUTES les pages, sans casser les liens existants ni `aria-current`.
2. **Given** le footer, **When** je regarde, **Then** un lien « Le blog » est ajouté dans la colonne Guides ou Le projet, sur les 10 pages.
3. **Given** `sitemap.xml`, **When** je vérifie, **Then** `https://fph-dev89.github.io/cap-sur-valencia/blog/2026-08-16-bienvenue.html` et `https://fph-dev89.github.io/cap-sur-valencia/pages/blog.html` sont ajoutés (12 URLs total).

---

## Functional Requirements

- **FR-001** : Nouveaux fichiers : `pages/blog.html`, `blog/2026-08-16-bienvenue.html`, `feed.xml`. Modifiés : les 10 pages HTML (nav + footer), `sitemap.xml`.
- **FR-002** : Les liens vers les articles utilisent des chemins relatifs (`blog/2026-08-16-bienvenue.html` depuis pages/, `../blog/...` depuis la racine si nécessaire).
- **FR-003** : `feed.xml` : XML valide, dates au format RFC 822.
- **FR-004** : Zéro em-dash dans les nouveaux contenus (l'article de bienvenue inclus).
- **FR-005** : Pas de données personnelles sensibles (pas d'adresse exacte, pas de noms d'enfants).
- **FR-006** : Le `.js .fade-in` pattern respecté (les nouveaux éléments visibles sans JS).
- **FR-007** : Les URLs existantes ne changent pas (pas de redirect nécessaire).

## Success Criteria

- **SC-001** : `pages/blog.html` existe, affiche l'article de bienvenue en card, responsive OK.
- **SC-002** : `blog/2026-08-16-bienvenue.html` existe avec ≥ 300 mots de contenu rédigé, JSON-LD `BlogPosting` valide.
- **SC-003** : `feed.xml` existe, XML bien formé (`xmllint --noout` ou parse node OK), 1 item.
- **SC-004** : `grep -c "blog.html" index.html pages/*.html` → 10/10 (nav + footer).
- **SC-005** : `sitemap.xml` contient 12 URLs.
- **SC-006** : Zéro em-dash dans le diff.
- **SC-007** : Playwright : pages blog + article sans JS → 0 `.fade-in` caché, 0 overflow mobile.

## Assumptions

- Les URLs restent sur github.io (le domaine sera traité à part).
- agy implémente, Hermes QA, boucle spec2 si écart.

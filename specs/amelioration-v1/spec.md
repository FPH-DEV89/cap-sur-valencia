# Feature Specification: Amélioration design v1 — Cap sur Valencia

**Feature Branch**: `improve-design-v1`
**Created**: 2026-08-14
**Status**: Draft — validée par Florian (GO)

**Input**: « Utilise les nouveaux skills design pour améliorer le site Cap sur Valencia »

---

## Constitution du projet (principes non-négociables)

1. **Le design Stitch de Florian est la loi.** Palette #fbfbe2 (beige) / #001626 (navy) / #924b26 (terracotta), direction éditoriale actuelle. On améliore l'EXÉCUTION, on ne redessine pas. Les tokens CSS existants (`--bg-beige`, `--navy`, `--terracotta`, `--font-heading: Playfair Display`) restent la source de vérité.
2. **Zéro fonctionnalité cassée.** Navigation, sections, contenu, responsive (media queries existantes) et animations existantes sont préservés. Toute modification est additive ou améliorative, jamais destructive.
3. **Photos réelles, pas d'images IA.** 6 photos Wikimedia Commons (licence libre) déjà téléchargées dans `assets/img/` : hero-ciudad-arte.jpg, budget-mercado.jpg, quartiers-plage.jpg, saveurs-paella.jpg, culture-plaza.jpg, culture-fallas.jpg. Les réutiliser, ne pas en chercher d'autres.
4. **Chiffres réels du contenu existant.** Les scénarios budget (2 480 € / 3 425 € / 4 435 €), les adresses restos, les noms de quartiers viennent des pages existantes. Rien d'inventé.
5. **Accessibilité WCAG AA.** Contraste texte ≥ 4.5:1 sur fonds clairs, focus visible sur tous les éléments interactifs, alt descriptifs sur les images.
6. **Performance.** Images locales (déjà dans le repo), lazy-loading sur les images sous le fold, aucune nouvelle dépendance, pas de librairie externe.
7. **Pas d'eyebrows, pas de cartes monotones, pas d'ombres lourdes.** Les règles anti-slop du skill ui-design-references s'appliquent SAUF quand elles contredisent le design Stitch choisi par l'utilisateur (ex: le fond beige #fbfbe2 est un choix utilisateur, il prime).

---

## User Stories

### US-01 — Hero de la home avec vraie photo de Valencia (P1)

**En tant que** visiteur qui atterrit sur la home,
**je veux** voir une vraie photo de la Ciudad de las Artes dans le hero (via le placeholder `.hero-photo-overlay` existant ou un `<img>`),
**afin que** le site ait immédiatement une identité visuelle réelle et crédible (aujourd'hui : zéro photo sur 10 pages).

**Pourquoi ce priority** : c'est le manque n°1 identifié par l'audit (3/3 reviewers). Impact visuel maximal, effort minimal (placeholder déjà en place).

**Independent Test** : charger la home → une photo de la Ciudad de las Artes est visible dans le hero, le texte reste parfaitement lisible (overlay semi-transparent navy ou dégradé sunset existant).

**Acceptance Scenarios**:
1. **Given** la home chargée, **When** je regarde le hero, **Then** une photo réelle de la Ciudad de las Artes (assets/img/hero-ciudad-arte.jpg) est visible en fond, avec overlay assurant la lisibilité du texte blanc.
2. **Given** le hero, **When** le viewport fait 375px (mobile), **Then** la photo est toujours visible (background-size: cover) sans déformer le layout.
3. **Given** la photo en arrière-plan, **When** le texte est superposé, **Then** le contraste texte/blanc sur photo est ≥ 3:1 (grand texte) — vérifié visuellement.

---

### US-02 — Contraste du texte corrigé (P1)

**En tant que** lecteur,
**je veux** un texte corps avec un contraste suffisant sur le fond beige #fbfbe2,
**afin que** la lecture soit confortable (aujourd'hui le gris-brun est trop clair).

**Pourquoi ce priority** : l'audit a relevé une lisibilité moyenne sur home/budget/quartiers. Impact direct sur l'expérience de lecture de tout le site.

**Independent Test** : ouvrir 3 pages (home, budget, quartiers) → le texte corps a un contraste ≥ 4.5:1.

**Acceptance Scenarios**:
1. **Given** le fond beige #fbfbe2, **When** j'examine la couleur du texte corps (--text), **Then** le ratio de contraste est ≥ 4.5:1 (ajuster la variable, pas le fond).
2. **Given** un texte secondaire (légendes, meta), **When** il est sur fond beige ou blanc, **Then** il reste lisible (≥ 4.5:1, ou 3:1 minimum pour du très grand texte).
3. **Given** les liens, **When** ils sont dans le contenu, **Then** ils restent reconnaissables comme liens (couleur + hover), sans casser la palette.

---

### US-03 — Hero allégé, promesse forte (P1)

**En tant que** visiteur,
**je veux** un hero qui dit l'essentiel en quelques secondes (promesse + CTA),
**afin que** je comprenne immédiatement le sujet du site (expatriation familiale à Valencia).

**Pourquoi ce priority** : l'audit a relevé « 2 paragraphes = mur de texte dans le fold », le H1 perd de la respiration.

**Independent Test** : charger la home → le hero tient en 1 écran avec badge + titre + 1 phrase d'accroche + countdown + CTA.

**Acceptance Scenarios**:
1. **Given** le hero actuel (hero-lead + hero-context = 2 paragraphes), **When** je le relis, **Then** le contenu est condensé en 1 phrase d'accroche max (le détail part dans la section « notre histoire » ou reste sous le fold).
2. **Given** le countdown, **When** il est affiché, **Then** il est conservé (il fait partie du design validé).
3. **Given** les CTA, **When** je les vois, **Then** ils restent les mêmes destinations (aucun lien cassé).

---

### US-04 — Budget : chiffres clés dès le fold (P2)

**En tant que** futur expat qui planifie son budget,
**je veux** voir les 3 scénarios mensuels (Sobre 2 480 € / Confort 3 425 € / Tranquille 4 435 €) en cards claires dès le haut de la page,
**afin que** je capte la fourchette de budget en 5 secondes.

**Pourquoi ce priority** : l'audit a relevé « aucun KPI dans le fold, promesse "des chiffres pas du blabla" non tenue ». Les données existent déjà dans la page.

**Independent Test** : ouvrir budget.html → 3 cards scénarios visibles dans le premier écran après l'intro, chiffres en tabular-nums.

**Acceptance Scenarios**:
1. **Given** la page budget, **When** je scrolle après l'intro, **Then** je vois 3 cards (Sobre/Confort/Tranquille) avec les montants mensuels exacts (2 480 € / 3 425 € / 4 435 €) extraits du contenu existant.
2. **Given** les montants, **When** ils sont affichés, **Then** ils utilisent `font-variant-numeric: tabular-nums` (chiffres alignés).
3. **Given** les cards, **When** le viewport est mobile, **Then** elles passent en colonne (stack) sans casse.

---

### US-05 — Quartiers : grille de cards avec badges (P2)

**En tant que** futur expat qui choisit son quartier,
**je veux** une grille de cards pour les quartiers (Benimaclet, Patraix, Campanar, Ruzafa, Ensanche, El Carmen, Cabanyal, Alboraya, Burjassot, Mislata, Torrent, Paterna) avec badges (top famille, budget, points d'attention),
**afin que** je compare les quartiers d'un coup d'œil (aujourd'hui : un long texte mono-colonne).

**Pourquoi ce priority** : l'audit a relevé « une seule colonne dans un grand vide, aucun scan visuel ». Le contenu (32 Ko) est déjà là, il manque la mise en forme.

**Independent Test** : ouvrir quartiers.html → une grille de cards remplace la liste plate, chaque card a un badge de catégorie (Famille / Centre-ville / Bord de mer / Banlieue).

**Acceptance Scenarios**:
1. **Given** la page quartiers, **When** je scrolle, **Then** chaque quartier est présenté dans une card avec titre, 2-3 bullets clés et un badge (Top famille, Centre, Bord de mer, Banlieue).
2. **Given** les cartes, **When** je passe la souris, **Then** il y a un hover state (transition 300ms, fond légèrement plus chaud).
3. **Given** la grille, **When** le viewport est mobile, **Then** les cards passent en 1 colonne.
4. **Given** le contenu texte existant, **When** je compare, **Then** aucune information n'est supprimée (le texte détaillé reste, les cards le résument).

---

### US-06 — Photos réelles sur les pages (P2)

**En tant que** lecteur du blog,
**je veux** voir des photos réelles illustrant chaque thème (budget → Mercado Central, quartiers → plage Malvarrosa, saveurs → paella, culture → Plaza de la Virgen, Fallas → Fallas),
**afin que** le site respire Valencia au lieu de rester abstrait.

**Pourquoi ce priority** : même manque que US-01, étendu aux pages intérieures. Les images sont déjà téléchargées.

**Independent Test** : ouvrir budget.html, quartiers.html, et les sections culture de la home → chaque page a au moins 1 photo pertinente, avec alt descriptif.

**Acceptance Scenarios**:
1. **Given** budget.html, **When** je scrolle, **Then** une photo du Mercado Central (assets/img/budget-mercado.jpg) illustre la section budget (loyer/courses ou installation).
2. **Given** quartiers.html, **When** je scrolle, **Then** une photo de la plage Malvarrosa (assets/img/quartiers-plage.jpg) illustre la section bord de mer.
3. **Given** la home (sections art-de-vivre / saveurs / heritage), **When** je scrolle, **Then** les photos Plaza de la Virgen, paella et Fallas illustrent les sections correspondantes (ou au moins 2 d'entre elles, sans surcharger).
4. **Given** chaque image, **When** elle est affichée, **Then** elle a un `alt` descriptif en français et `loading="lazy"` (sauf le hero, eager).
5. **Given** les images locales, **When** la page est servie, **Then** les chemins sont relatifs (assets/img/…) et fonctionnent sur GitHub Pages.

---

### US-07 — États interactifs (P3)

**En tant que** utilisateur,
**je veux** des retours visuels sur hover/active/focus sur tous les éléments cliquables,
**afin que** le site paraisse vivant et accessible.

**Pourquoi ce priority** : polish, mais important pour la sensation premium.

**Independent Test** : passer la souris sur boutons/liens/cards → transition visible ; tabuler → focus ring visible.

**Acceptance Scenarios**:
1. **Given** un bouton .btn-primary, **When** je le survole, **Then** le fond passe à une teinte plus foncée (ou équivalent) avec transition 150-300ms.
2. **Given** un lien ou bouton, **When** je navigue au clavier (Tab), **Then** un focus ring visible est affiché.
3. **Given** une card, **When** je la survole, **Then** il y a un retour visuel (léger lift ou fond plus chaud, selon ce qui existe déjà).

---

### US-08 — Micro-polish premium (P3)

**En tant que** propriétaire du site,
**je veux** les finitions : chiffres alignés (tabular-nums), image de partage social (og:image), et suppression des artefacts visuels datés (si présents sans casser le design Stitch),
**afin que** le rendu soit soigné et partageable.

**Pourquoi ce priority** : dernière couche de qualité.

**Independent Test** : les € sont alignés dans les tableaux/cards ; un og:image pointe vers assets/img/hero-ciudad-arte.jpg.

**Acceptance Scenarios**:
1. **Given** un tableau ou une card avec des montants, **When** je regarde les chiffres, **Then** ils sont en tabular-nums (pas de sautillement de largeur).
2. **Given** la home, **When** elle est partagée (WhatsApp/Slack/Facebook), **Then** l'og:image affiche la photo hero (URL absolue vers le domaine GitHub Pages).
3. **Given** les motifs décoratifs existants (losanges, orbes), **When** ils nuisent à la lisibilité du hero, **Then** ils sont atténués (opacité réduite) sans être supprimés si le design Stitch les impose.

---

## Edge Cases

- **Images qui ne chargent pas** : les sections avec photos gardent un fond de secours (couleur de section existante) — pas de trou visuel.
- **Mobile 375px** : hero-photo-overlay en cover ne déborde pas (overflow-x: hidden déjà présent sur body).
- **Navigation cassée** : aucun lien ne change de destination ; vérifier les ancres (#accueil, #art-de-vivre…) après modification.
- **Contraste trop agressif** : assombrir le texte NE change PAS la couleur du fond beige Stitch (choix utilisateur protégé).
- **GitHub Pages** : chemins relatifs obligatoires (pas de /assets/ absolu depuis la racine).

## Requirements

- **FR-001**: Utiliser uniquement les 6 photos déjà dans assets/img/ (aucune nouvelle recherche d'image).
- **FR-002**: Ne pas modifier la palette Stitch (#fbfbe2, #001626, #924b26) ni les tokens CSS existants sauf --text (contraste) et ajouts additifs.
- **FR-003**: Ne pas ajouter de dépendance (pas de npm, pas de CDN nouveau ; Google Fonts existant conservé).
- **FR-004**: Conserver le contenu textuel existant (aucune suppression d'information).
- **FR-005**: Les images sous le fold ont loading="lazy"; le hero est eager.
- **FR-006**: Og:image ajouté sur index.html avec URL absolue.
- **FR-007**: Le countdown et les CTA du hero sont conservés.
- **FR-008**: Le responsive existant (media queries) est conservé et les nouveaux composants (cards KPI, grille quartiers) sont responsives.

## Success Criteria

- **SC-001**: La home (hero + sections culture) et les pages guides principales (budget, quartiers) montrent des photos réelles pertinentes — vérifié par screenshot. Les pages utilitaires (checklists, administration…) restent textuelles si aucune photo ne leur correspond.
- **SC-002**: Le texte corps a un contraste ≥ 4.5:1 (outil de contraste) sur fond beige.
- **SC-003**: La page budget montre 3 cards scénarios avec les montants exacts du contenu.
- **SC-004**: La page quartiers montre une grille de cards avec badges, sans perte d'information.
- **SC-005**: Zéro lien cassé, zéro erreur console, zéro régression visuelle sur les sections non modifiées.
- **SC-006**: Lighthouse performance ≥ 90 (images locales + lazy).

## Assumptions

- Le hero-photo-overlay existant (déjà dans le HTML) est le point d'ancrage de US-01 — ne pas créer une nouvelle structure si l'existante suffit.
- Les emojis comme icônes restent la convention (déjà en place, pas d'icônes SVG à introduire).
- Le site est déployé sur GitHub Pages (fph-dev89.github.io/cap-sur-valencia) — push sur main = déploiement.
- agy (Gemini CLI) implémente la spec ; Hermes fait la QA visuelle et corrige via spec2 si écart.

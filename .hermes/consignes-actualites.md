# Consignes — Page Actualités + photos HD (Cap sur Valencia)

## Contexte

Site statique vanilla (HTML/CSS/JS, pas de framework, pas de build) dans `/tmp/cap-sur-valencia`.
Blog d'expatriation familiale (famille de 5, départ Valencia 2028). Déployé GitHub Pages mais
**PAS DE COMMIT, PAS DE PUSH, PAS DE GIT** : travail en local uniquement, Florian validera avant.

**Design Stitch (PALETTE IMPÉRATIVE, ne jamais la modifier) :**
- `--bg-beige: #fbfbe2` (fond clair) · `--navy: #001626` (accents, headers) · `--terracotta: #924b26` (CTA, liens)
- Fonts : `Playfair Display` (titres) + `Source Sans 3` (corps)
- Cards : rayons 12px, ombres teintées terracotta/navy (jamais noires), hover lift

**Règles techniques obligatoires (déjà en place sur toutes les pages) :**
- Chaque page HTML commence par `<script>document.documentElement.classList.add('js');</script>` dans le `<head>`
- Les éléments animés portent la classe `fade-in` ; le CSS les masque uniquement sous `.js .fade-in { opacity: 0 }`
- Ne PAS casser le responsive mobile (media queries ≤768px existantes)
- Liens externes : `rel="noopener noreferrer"` quand `target="_blank"`
- Alt descriptifs sur toutes les images

## Mission 1 — Page Actualités (NOUVELLE) : `pages/actualites.html`

S'inspirer de la structure de `pages/blog.html` (header `content-header`, breadcrumb, hero,
grille de cards, footer, back-to-top, `<script src="../js/main.js">` en fin de body).

### Structure de la page
1. **Header** : breadcrumb Accueil / Actualités, badge `🎉 Actualités & sorties`, H1 « Quoi faire à Valencia ce week-end ? », meta-bar (📅 mise à jour chaque dimanche · ✍️ Par Florian · 📍 Valencia & alentours)
2. **Intro éditoriale** (2-3 phrases) : chaque dimanche, une idée de sortie testée et documentée — adresses, horaires, tarifs, tout pour y aller les yeux fermés.
3. **Grille de cards** (classe à créer, style = `.blog-card` existante mais adaptée) : une card par fiche, avec :
   - photo (classe `actu-card-img`), badge catégorie coloré, titre, extrait, et une **mini-ligne infos pratiques** : 📍 quartier/zone · ⏱️ durée conseillée · 💰 « dès X € » (ou Gratuit)
   - lien « Voir la fiche complète → »
4. **Bloc rythme de publication** (même style que le `highlight-box` de blog.html) : « 📬 Chaque dimanche, une nouvelle sortie » + abonnement RSS.
5. Nav + footer identiques aux autres pages (avec le nouveau lien Actualités, cf. Mission 4).

### Catégories (badges, couleurs définies dans le CSS)
- 🌿 Nature & plein air — vert sapin (#2d6a4f)
- 🐠 Culture & sciences — navy (#001626)
- 🍊 Gastronomie — terracotta (#924b26)
- ⚽ Famille & loisirs — bleu (#1d4e89)

## Mission 2 — 4 fiches d'activités (NOUVEAU dossier) : `actualites/`

Créer le dossier `actualites/` à la racine (comme `blog/`). Chaque fiche copie la structure
de `blog/2026-08-16-bienvenue.html` (head complet : meta, OG, Twitter, canonical, JSON-LD,
RSS link, favicon ; skip-link ; top-sentinel ; reading-progress ; navbar ; content-header ;
`main.section.content-body` avec `container max-width 800px` ; figure.banner-photo ;
article-body ; footer ; back-to-top ; main.js).

Canonical/OG/JSON-LD : `https://fph-dev89.github.io/cap-sur-valencia/actualites/<slug>.html`

**JSON-LD de chaque fiche** : `@graph` avec BreadcrumbList (Accueil → Actualités → fiche)
+ `Article` (headline, description, image, author Florian, datePublished, dateModified,
inLanguage fr-FR) + **`TouristAttraction`** avec `address` (streetAddress, addressLocality
"Valencia", postalCode, addressCountry "ES"), `telephone`, `url` (site officiel),
`openingHours` (format ISO ex. "Mo-Sa 07:30-15:00"), `priceRange`.

### Bloc « Infos pratiques » (obligatoire dans chaque fiche)
Encadré structuré (classe `info-pratiques`, style cohérent avec `highlight-box`) avec cette
grille de lignes — toujours dans cet ordre :
- 📍 **Adresse** : ...
- 🕐 **Horaires** : ...
- 💰 **Tarifs** : ...
- 📞 **Contact** : téléphone (si public)
- 🌐 **Site** : lien officiel (rel noopener, target _blank)
- 🚇 **Accès** : métro/tram/bus/parking

Sous chaque photo de fiche : `<figcaption>` avec crédit photo (auteur, licence CC) —
ex. « 📷 Photo : Diego Delso — Wikimedia Commons, CC BY-SA 4.0 ».

### Fiche A — `actualites/2026-08-16-bioparc-valencia.html`
- Titre : « Bioparc Valencia : l'Afrique à 15 minutes de chez nous »
- Catégorie : 🌿 Nature & animaux · 📅 16 août 2026 · ⏱️ 4 min
- **Adresse** : Avenida Pío Baroja, 3, 46015 València
- **Horaires** : tous les jours, ouverture 10h00 (11h00 le 25 décembre et le 1er janvier) ; fermeture variable selon saison — dernière entrée 1h avant la fermeture
- **Tarifs** : adulte (13-64 ans) dès 29,50 € · enfant (4-12 ans) dès 23,50 € · moins de 4 ans **gratuit** · parking 7 € max par jour · billets en ligne 1 € moins chers qu'au guichet · expérience VR « La Última Frontera » 5 € en option
- **Contact** : +34 96 090 40 44
- **Site** : https://www.bioparcvalencia.es (bouton billetterie)
- **Accès** : Tram L4 — arrêt « Bioparc » · parking payant sur place (7 €/jour)
- **Texte** (4-5 paragraphes + 1 highlight-box conseil) : concept zoo-immersion (aucune barrière visible), 4 habitats — savane africaine (girafes, lions, éléphants, rhinocéros), zones humides avec la grotte de Kitum (seul point d'observation sous-marin des hippopotames en Espagne), jungle équatoriale (gorilles, chimpanzés), île de Madagascar (lémuriens) ; aire de jeux 2-12 ans près du restaurant Ndoki ; durée conseillée 4-6h ; conseil : y aller en semaine et le matin ; mentionner que c'est LE complément idéal de l'Oceanogràfic (renvoi fiche).
- **Photo** : `../assets/img/activites-bioparc.jpg` — crédit : radwoc, Wikimedia Commons, CC BY-SA 3.0
- OG image : `https://fph-dev89.github.io/cap-sur-valencia/assets/img/activites-bioparc.jpg`

### Fiche B — `actualites/2026-08-17-oceanografic.html`
- Titre : « L'Oceanogràfic : le plus grand aquarium d'Europe, en plein cœur de la Cité des Arts »
- Catégorie : 🐠 Culture & sciences · 📅 17 août 2026 · ⏱️ 4 min
- **Adresse** : Carrer d'Eduardo Primo Yúfera, 1B, 46013 València (Cité des Arts et des Sciences)
- **Horaires** : tous les jours, ouverture 10h00 ; fermeture selon saison — 18h en hiver, jusqu'à 21h en été (consulter le calendrier sur le site officiel) ; guichets fermés 1h avant
- **Tarifs** : général dès 35,90 € · enfant (4-12 ans) dès 26,65 € · **famille nombreuse (3 enfants ou +) : adulte dès 30,52 €, enfant dès 22,65 €** (justificatif famille nombreuse demandé) · combo Oceanogràfic + Museu de les Ciències + Hemisfèric dès 44,00 € · cinéma 4D +3 €
- **Contact** : +34 96 047 06 47
- **Site** : https://www.oceanografic.org
- **Accès** : Métro L10 — arrêt « Oceanogràfic » (le plus simple, station juste à côté)
- **Texte** : plus grand aquarium d'Europe ; spectacles de dauphins (horaires variables selon jour, ex. 11h15, 12h30, 13h45, 16h30, 18h, 19h — à vérifier sur place) ; tunnel sous-marin avec requins ; bélougas, manchots, spatules roses ; cinéma 4D (20 000 lieues sous les mers, Pingouins 4D) 3 € ; visite guidée coulisses 12 € ; **mettre en avant le tarif famille nombreuse : avec 3 enfants, la famille de Florian économise ~15 € vs tarifs plein** ; combo Cité des Arts = journée complète.
- **Photo** : `../assets/img/activites-oceanografic.jpg` — crédit : Ymblanter, Wikimedia Commons, CC BY-SA 4.0
- OG image : `https://fph-dev89.github.io/cap-sur-valencia/assets/img/activites-oceanografic.jpg`

### Fiche C — `actualites/2026-08-18-mercado-central.html`
- Titre : « Le Mercado Central : 300 étals sous une coupole de fer et de verre »
- Catégorie : 🍊 Gastronomie · 📅 18 août 2026 · ⏱️ 3 min
- **Adresse** : Plaza Ciudad de Brujas, 46001 València (face à la Lonja de la Seda, classée UNESCO)
- **Horaires** : lundi au samedi 7h30 – 15h00 · **fermé le dimanche**
- **Tarifs** : entrée libre (paiement par carte accepté dans la quasi-totalité des étals)
- **Contact** : +34 96 382 91 01
- **Site** : https://www.mercadocentralvalencia.es
- **Accès** : Métro L1/L2 arrêt « Colón » ou L3/L5 arrêt « Xàtiva », puis 5-10 min à pied
- **Texte** : inauguré en 1928 (architectes Guàrdia et Soler), coupole centrale fer et verre, mosaïques colorées, célèbre girouette-perroquet (« la cotorra del mercat ») ; ~300 étals : fruits, légumes, poissons, jambons ; à goûter : bocadillo de jamón ibérico coupé minute, huîtres fraîches, horchata + fartons ; le Central Bar du chef étoilé Ricard Camarena (ensaladilla rusa légendaire, bocata de sepia) ; conseil : y aller le matin pour voir le marché vivant, avant 13h pour le bar ; fermé le dimanche — prévoir un autre jour.
- **Photo** : `../assets/img/activites-mercado-central.jpg` — crédit : Diego Delso, Wikimedia Commons, CC BY-SA 4.0
- OG image : `https://fph-dev89.github.io/cap-sur-valencia/assets/img/activites-mercado-central.jpg`

### Fiche D — `actualites/2026-08-19-albufera-el-palmar.html`
- Titre : « L'Albufera : balade en barque dans les rizières au coucher du soleil »
- Catégorie : 🌿 Nature & plein air · 📅 19 août 2026 · ⏱️ 4 min
- **Adresse** : Parc naturel de l'Albufera — embarcadères d'El Palmar et du Port del Saler (à ~15 km au sud de Valencia)
- **Horaires** : départs toute la journée, matin et après-midi, toute l'année ; sorties coucher de soleil (75-90 min) sur réservation
- **Tarifs** : adulte 8 € · enfant (3-11 ans) 4 € · minimum 5 personnes ou 40 € · promenade standard 60 min
- **Contact** : réservation en ligne (site officiel des barcas) — pas de téléphone public
- **Site** : https://visitalbufera.com/fr/tour/paseos-barca/
- **Accès** : voiture ~25 min depuis le centre (parking à l'embarcadère) · bus EMT lignes 24/25 direction El Palmar
- **Texte** : parc naturel, 300+ espèces d'oiseaux (flamants roses selon saison) ; barques traditionnelles à moteur électrique (silencieuses) ; 2 embarcadères : El Palmar (Quai de Pomero — traverse les rizières du Tancat del Pomero, contourne la Mata del Fang, plus grande île du lac) et Port del Saler (canal du Saler, ancienne route du sel) ; lac peu profond (1-1,5 m en moyenne) ; LE spot pour le coucher de soleil ; El Palmar = berceau de la paella valencienne — finir la journée par une paella dans le village ; conseil famille : la sortie 60 min est parfaite avec des enfants.
- **Photo** : `../assets/img/activites-albufera.jpg` — crédit : Pepe Serrador, Wikimedia Commons, CC BY-SA 4.0
- OG image : `https://fph-dev89.github.io/cap-sur-valencia/assets/img/activites-albufera.jpg`

## Mission 3 — Photos HD dans `index.html`

1. **Hero** : remplacer `assets/img/hero-ciudad-arte.jpg` par `assets/img/hero-malvarrosa.jpg`
   (alt : « La plage de la Malvarrosa, scène de vie méditerranéenne à Valencia ») — garder
   la classe et le layout `hero-split` existants, juste changer src + alt + width/height (5472x3648).
2. **Cards quartiers** (section `#quartiers`, 3 cards Benimaclet / Patraix / Campanar) : ajouter
   une photo en tête de chaque card, au-dessus du `<h3>` (classe `quartier-card-img`, style :
   largeur 100%, hauteur 150-170px, object-fit cover, coins supérieurs arrondis 12px, zoom doux au hover) :
   - Benimaclet → `assets/img/benimaclet-rue.jpg` (alt : « Street art coloré dans les rues de Benimaclet »)
   - Patraix → `assets/img/patraix-ruelle.jpg` (alt : « Ruelle du centre historique de Patraix »)
   - Campanar → `assets/img/campanar-vue.jpg` (alt : « Vue du quartier moderne de Campanar »)
3. **Section teaser Actualités** (NOUVELLE, à insérer entre la section `#saveurs` et la section `#timeline`) :
   fond beige, header éditorial « 📰 Les sorties du moment », grille de 4 mini-cards (une par fiche,
   photo + titre + mini-info prix/durée), chacune liée vers sa fiche `actualites/...html`, + lien
   éditorial « Toutes les idées de sorties → » vers `pages/actualites.html`.

## Mission 4 — Nav, footer, sitemap, feed

1. **Nav sur TOUTES les pages** (index.html, 10 pages de `pages/`, 4 nouvelles fiches) :
   ajouter `<li><a href="pages/actualites.html">Actualités</a></li>` (relatif : `../pages/actualites.html`
   depuis les fiches) juste après le lien Blog. Ajuster le responsive si le menu déborde.
2. **Footer sur toutes les pages** : ajouter un lien « Actualités & sorties » (vers
   `pages/actualites.html` ou `../pages/actualites.html`) dans la colonne « Guides » sous « Le blog ».
   Dans `footer-bottom`, ajouter la mention : `📷 Photos : Wikimedia Commons (licences CC BY, CC BY-SA, CC0)`.
3. **`sitemap.xml`** : ajouter les 5 URLs (actualites.html + 4 fiches) avec lastmod 2026-08-16.
4. **`feed.xml`** : ajouter les 4 fiches en items RSS (guid = URL canonique, `<category>Actualités</category>`,
   description = extrait, date au format RFC-822).

## Fichiers à créer
- `pages/actualites.html`
- `actualites/2026-08-16-bioparc-valencia.html`
- `actualites/2026-08-17-oceanografic.html`
- `actualites/2026-08-18-mercado-central.html`
- `actualites/2026-08-19-albufera-el-palmar.html`

## Fichiers à modifier
- `index.html` (hero + cards quartiers + section teaser + nav + footer)
- `pages/blog.html`, `pages/budget.html`, `pages/quartiers.html`, `pages/ecoles.html`,
  `pages/emploi.html`, `pages/sante.html`, `pages/scolarite.html`, `pages/administration.html`,
  `pages/checklists.html`, `pages/ressources.html` (nav + footer uniquement)
- `css/style.css` (classes : actu-card, actu-card-img, actu-meta, actu-badge, quartier-card-img,
  actu-teaser-card, info-pratiques, info-pratiques-row, credit-photo)
- `sitemap.xml`, `feed.xml`

## Règles strictes
- Ne modifier QUE les fichiers listés ci-dessus. N'exécute AUCUNE commande (ni build, ni tsc,
  ni git, ni serveur). Édite uniquement les fichiers.
- Palette Stitch impérative (#fbfbe2 / #001626 / #924b26). Pas d'em-dash (—) dans le contenu.
- Pas d'images IA. Photos fournies dans assets/img (déjà téléchargées).
- Toute nouvelle classe avec animation de révélation utilise le pattern `.js .fade-in` existant.
- Ne pas toucher à `js/main.js` sauf nécessité absolue (le signaler).
- Vérification finale : ouvrir chaque page créée/modifiée et vérifier qu'aucune image ne pointe
  vers un fichier inexistant, que les liens relatifs sont corrects, que le HTML est valide.

Réponds en français : liste des fichiers créés/modifiés + points de vigilance.

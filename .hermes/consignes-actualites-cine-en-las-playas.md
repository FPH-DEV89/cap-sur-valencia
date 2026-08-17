# Mission agy : fiche Actualité « Cine en las Playas 2026 » — Cap sur Valencia

## Contexte

Tu es rédacteur web + développeur front pour le blog « Cap sur Valencia » (blog d'expatriation
familiale française, départ Valencia 2028). Repo : `/tmp/cap-sur-valencia` — site 100 % statique
(HTML/CSS/JS vanilla, pas de framework, pas de build, pas de package.json).

Mission : créer la fiche actualité **« Cine en las Playas »** — le cinéma d'été gratuit sur les
plages de la province de Valencia, organisé par la Diputación de Valencia — édition 2026.

- **Fichier à créer** : `/tmp/cap-sur-valencia/actualites/2026-08-17-cine-en-las-playas.html`
- **Template à copier intégralement (structure)** : `/tmp/cap-sur-valencia/actualites/2026-08-19-albufera-el-palmar.html`
  — garder exactement : head (charset, viewport, js class, title, meta description/keywords,
  canonical, OG, twitter, RSS link, favicon, JSON-LD, stylesheet), skip-link, top-sentinel,
  reading-progress, navbar (mêmes liens), nav-overlay, content-header (breadcrumb, badge, h1,
  meta-bar), main (banner-photo, article-body, info-pratiques, highlight-box, article-nav-back),
  footer, back-to-top, script main.js.

## Faits DÉJÀ VÉRIFIÉS par l'orchestrateur (source : valenciabonita.es — à utiliser tels quels, pas besoin de les re-vérifier)

- Événement : **Cine en las Playas de Valencia 2026**, organisé par la **Diputación de Valencia**
  (en collaboration avec les mairies participantes).
- **46 projections gratuites dans 23 localités** de la province, du **jeudi 9 juillet au vendredi
  28 août 2026**, toutes les séances à **22h00**.
- **Gratuit, entrée libre, sans réservation**. Chacun apporte sa serviette, sa chaise ou sa
  hamaca — et même son dîner. Séances directement **sur le sable**.
- Films 2026 (famille) : Lilo & Stitch, Robot Salvaje (The Wild Robot), Jurassic World: El
  Renacer, Wicked, Cómo entrenar a tu dragón, Amigos imaginarios (IF), Wolfgang Extraordinario,
  La luz de Aisha, Policán (Dog Man), Transformers One, Tipos Malos 2, Los Pitufos, Sonic 3,
  Súper agente Hitpig, Los Futbolísimos 2, Elli y el equipo de los monstruos, El Especialista,
  Dalia y el libro rojo, ¿Quién es quién?, Los Exploradores: Gigantes.
- Programme complet vérifié :
  - Juillet : 9 La Pobla de Farnals (Amigos imaginarios) · 10 El Puig de Santa Maria (Cómo
    entrenar a tu dragón) · 11 Puçol (Amigos imaginarios) · 12 Sagunto (Sonic 3) · 13 Tavernes
    de la Valldigna (Robot Salvaje) · 14 Mareny de Barraquetes (Súper agente Hitpig) · 15 Daimús
    (Los Futbolísimos 2) · 16 Alboraia (Cómo entrenar a tu dragón) · 17 Sueca (Robot Salvaje) ·
    18 El Perelló (Jurassic World: El Renacer) · 19 Cullera (Elli y el equipo de los monstruos) ·
    20 Canet d'en Berenguer (Wolfgang) · 21 Xeraco (El Especialista) · 22 Oliva (Wicked) · 23
    Massalfassar (Jurassic World: El Renacer) · 24 Meliana (Jurassic World: El Renacer) · 25
    Bellreguard (Wicked) · 26 Piles (Cómo entrenar a tu dragón) · 27 Massamagrell (Lilo & Stitch)
    · 28 Miramar (Jurassic World: El Renacer) · 30 Navarrés/Playamonte (Lilo & Stitch) · 31
    Gandia (Robot Salvaje)
  - Août : 1 Puçol (Robot Salvaje) · 4 Xeraco (Los Futbolísimos) · 5 Piles (Wolfgang
    Extraordinario) · 6 El Puig de Santa Maria (Wolfgang Extraordinario) · 7 Alboraia (Sonic 3) ·
    8 Sueca (Dalia y el libro rojo) · 9 Sagunto (Jurassic World: El Renacer) · 10 Canet d'en
    Berenguer (La luz de Aisha) · 11 Mareny de Barraquetes (Jurassic World: El Renacer) · 12
    Daimús (¿Quién es quién?) · 14 Gandia (Amigos imaginarios) · 15 Massalfassar (Tipos Malos 2)
    · 16 El Perelló (Lilo & Stitch) · **18 Massamagrell (Wicked)** · **19 Oliva (Robot Salvaje)**
    · **20 Navarrés/Playamonte (Cómo entrenar a tu dragón)** · **21 Meliana (Policán)** · **22
    Bellreguard (Los Exploradores: Gigantes)** · **23 Cullera (Lilo & Stitch)** · 24 Tavernes de
    la Valldigna (Lilo & Stitch) · 26 Miramar (Transformers One) · 28 La Pobla de Farnals (Los
    Pitufos — séance de clôture)
- Les 22 localités listées : Alboraia, Bellreguard, Canet d'en Berenguer, Cullera, Daimús, El
  Perelló, El Puig de Santa Maria, Gandia, La Pobla de Farnals, Mareny de Barraquetes,
  Massalfassar, Massamagrell, Meliana, Miramar, Navarrés (Playamonte), Oliva, Piles, Puçol,
  Sagunto, Sueca, Tavernes de la Valldigna, Xeraco.

## Recherche web à faire PAR TOI (obligatoire — utilise tes outils de recherche)

1. **Source officielle** : trouve la page officielle de la Diputación de Valencia (dival.es ou
   équivalent) sur le Cine en las Playas 2026 — vérifie le programme, les dates, l'horaire 22h
   et le caractère gratuit. C'est elle qui servira de lien « 🌐 Site » et d'organizer dans le
   JSON-LD. Si tu ne trouves pas de page officielle dédiée, garde valenciabonita.es comme
   référence secondaire vérifiée.
2. **Accès transports depuis Valencia** (à vérifier, ne pas inventer) : Meliana et Massamagrell
   sont-elles desservies par le métro Metrovalencia (ligne L3) ? Alboraia ? El Puig et Puçol
   (train de banlieue Renfe C6) ? Sagunto (Renfe C6) ? Cullera (Renfe C1) ? Donne la ligne réelle
   + un ordre de durée depuis le centre de Valencia si une source le confirme. Si un accès n'est
   pas confirmé : écris `[À VÉRIFIER]` ou omets.
3. **Photo libre** : cherche sur Wikimedia Commons une photo (CC0 / CC BY / CC BY-SA, largeur
   ≥ 1200px) illustrant soit un cinéma en plein air sur une plage, soit une plage valencienne au
   crépuscule (ex. Playa de la Malvarrosa au coucher du soleil), soit une séance de « cine de
   verano ». Recette :
   - Recherche API :
     `https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrsearch=<sujet>&gsrnamespace=6&gsrlimit=10&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=1920`
     (User-Agent navigateur obligatoire sinon 403 ; en cas de 429, attends 6 s et réessaie, ou
     utilise l'URL directe `https://commons.wikimedia.org/wiki/Special:FilePath/<Titre>?width=1920`)
   - Collecte `Artist` (strip les tags HTML) + `LicenseShortName` depuis extmetadata → ce sont
     eux qui iront dans le crédit photo.
   - Télécharge la version 1920px dans `/tmp/cap-sur-valencia/assets/img/activites-cine-playas.jpg`.
   - Contrôle le sujet de la photo avant de la garder (pas de personne identifiable, pas
     d'image négative).
   - **Si aucune photo convenable trouvée** : réutilise `/tmp/cap-sur-valencia/assets/img/activites-albufera.jpg`
     (crédit : « 📷 Photo : Pepe Serrador · Wikimedia Commons, CC BY-SA 4.0 ») et référence-la
     dans la fiche (src `../assets/img/activites-albufera.jpg`).
4. **Croisement** : vérifie le programme des séances à venir (18-23 août) sur au moins une autre
   source que valenciabonita si possible.

## Contenu de la fiche (400-700 mots)

Ton direct et personnel (blog famille), vouvoiement léger comme les fiches existantes (« vous »).
Orthographe : **« Valencia »** partout (jamais « València »). Aucun fait inventé — tout chiffre,
date ou nom non confirmé par une source = `[À VÉRIFIER]` ou omission.

Structure narrative suggérée (adapte librement, reste naturel) :
1. Accroche : une soirée d'été, un film en famille, les pieds dans le sable, pour 0 € — c'est le
   Cine en las Playas de la Diputación de Valencia.
2. Le concept : écran géant en plein air posé sur le sable, 46 séances, 23 plages de la
   province, du 9 juillet au 28 août 2026, toutes à 22h00, entrée libre sans réservation, on
   apporte sa serviette/sa chaise/son dîner.
3. Les séances à venir cette semaine (du 18 au 23 août) : Massamagrell (mardi 18, Wicked),
   Oliva (mercredi 19, Robot Salvaje), Navarrés/Playamonte (jeudi 20, Cómo entrenar a tu
   dragón), Meliana (vendredi 21, Policán), Bellreguard (samedi 22, Los Exploradores: Gigantes),
   Cullera (dimanche 23, Lilo & Stitch). Mets en avant Meliana (Policán) : la plus proche de
   Valencia.
4. Les plages proches de Valencia + accès (résultats de ta recherche : métro L3 vers
   Meliana/Massamagrell/Alboraia, Renfe vers Sagunto/Cullera, voiture 20-40 min…).
5. Conseils pratiques : arriver un peu avant 22h pour bien se placer, couverture/serviette,
   anti-moustique, les films sont en version espagnole (doublés) = immersion garantie pour les
   enfants, séance de clôture le 28 août à La Pobla de Farnals (Los Pitufos).
6. Bloc « Infos pratiques » + highlight box conseil famille (cf. ci-dessous).

## Bloc Infos pratiques (OBLIGATOIRE, ordre fixe des 6 lignes)

- `📍 Adresse :` — ex. « 23 plages de la province de Valencia (programme 2026) : Meliana,
  Alboraia, Massamagrell, El Puig, Puçol, Sagunto, Cullera, El Perelló… » (liste les plus
  proches de Valencia)
- `🕐 Horaires :` — « Séances à 22h00 · du 9 juillet au 28 août 2026 »
- `💰 Tarifs :` — « Gratuit — entrée libre, sans réservation »
- `📞 Contact :` — « Diputación de Valencia » (+ téléphone officiel si ta recherche le confirme,
  sinon rien)
- `🌐 Site :` — lien officiel trouvé (target="_blank" rel="noopener noreferrer")
- `🚇 Accès :` — résultats vérifiés de ta recherche (métro L3, Renfe, voiture…)

## JSON-LD (@graph, dans le head)

1. **BreadcrumbList** : Accueil (https://capsurvalencia.fr/) → Actualités
   (https://capsurvalencia.fr/pages/actualites.html) → « Cine en las Playas »
   (https://capsurvalencia.fr/actualites/2026-08-17-cine-en-las-playas.html).
2. **Article** : headline, description, image
   (https://capsurvalencia.fr/assets/img/activites-cine-playas.jpg ou le fallback), author
   Person « Florian », publisher Organization « Cap sur Valencia » (url + logo favicon.svg),
   datePublished = dateModified = « 2026-08-17 », mainEntityOfPage, inLanguage « fr-FR ».
3. **Event** (⚠️ PAS TouristAttraction : c'est un événement temporaire, pas un lieu permanent —
   une donnée structurée trompeuse est négative pour le SEO) :
   - `"@type": "Event"`, name, description, image,
   - `"startDate": "2026-07-09"`, `"endDate": "2026-08-28"`,
   - `"eventStatus": "https://schema.org/EventScheduled"`,
   - `"eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode"`,
   - `"location": {"@type": "Place", "name": "Plages de la province de Valencia",
     "address": {"@type": "PostalAddress", "addressLocality": "Valencia",
     "addressRegion": "Comunitat Valenciana", "addressCountry": "ES"}}`,
   - `"offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR",
     "availability": "https://schema.org/InStock"}`,
   - `"organizer": {"@type": "Organization", "name": "Diputación de Valencia", "url": <officiel>}`
   - **PAS de `openingHours`** (événement saisonnier, pas d'horaires fixes à l'année). Pas de
     `priceRange`.

## Balises et conventions

- `<title>` : « Cine en las Playas : cinéma gratuit sur les plages de Valencia | Cap sur Valencia »
- H1 : « Cine en las Playas : le ciné d'été gratuit sur le sable, jusqu'au 28 août »
- Meta description : « Du 9 juillet au 28 août 2026, la Diputación de Valencia projette des
  films gratuits sur 23 plages de la province à 22h. Programme des prochaines séances, plages
  proches de Valencia et accès en métro. »
- Meta keywords : cine en las playas valencia, cinéma plein air valencia, cinéma plage valencia,
  sortie famille valencia, gratuit été valencia
- Badge dans le content-header : `<span class="actu-badge actu-badge--famille">🎬 Cinéma en plein air</span>`
- Meta-bar : `📅 17 août 2026 · ✍️ Par Florian · ⏱️ 3 min de lecture · 📍 Plages de la province de Valencia`
- Photo : `<figure class="banner-photo fade-in">` avec img (width/height réels de l'image) +
  `<figcaption>📷 Photo : <artiste> · Wikimedia Commons, <licence></figcaption>`
- Tous les liens externes : `target="_blank" rel="noopener noreferrer"`
- `aria-current="page"` UNIQUEMENT sur le span du breadcrumb (jamais sur un lien)
- Finir par `</html>`, balises équilibrées, classes `.fade-in` comme dans le template
- canonical + OG + twitter + JSON-LD : domaine **https://capsurvalencia.fr/** (jamais github.io)

## Mise à jour des listings (3 fichiers, RIEN d'autre)

1. **`/tmp/cap-sur-valencia/pages/actualites.html`** : ajouter la card en TÊTE de la grille
   `.actu-grid` (AVANT la card Bioparc), structure identique aux cards existantes :
   - `<article class="actu-card fade-in">` → actu-card-media (img `../assets/img/activites-cine-playas.jpg`,
     alt descriptif, width 800 height 533, loading="lazy") → actu-card-body :
     - actu-meta : badge `actu-badge--famille` « 🎬 Cinéma en plein air » · `📅 17 août 2026` · `⏱️ 3 min de lecture`
     - titre : « Cine en las Playas : le ciné d'été gratuit sur les plages »
       (lien `../actualites/2026-08-17-cine-en-las-playas.html`)
     - extrait : « Chaque été, la Diputación de Valencia installe un écran géant sur 23 plages
       de la province : films pour toute la famille, gratuit, à 22h, les pieds dans le sable. »
     - actu-meta-info : `📍 Plages de la province` · `⏱️ Séance à 22h` · `💰 Gratuit (Entrée libre)`
     - actu-card-action : « ✍️ Par Florian » + « Voir la fiche complète → »
2. **`/tmp/cap-sur-valencia/feed.xml`** : ajouter l'item RSS (même format que les autres items
   Actualités) : title, link, guid (permalink), `<category>Actualités</category>`,
   `<pubDate>Mon, 17 Aug 2026 10:30:00 +0200</pubDate>`, description ; mettre à jour
   `<lastBuildDate>` avec la même date.
3. **`/tmp/cap-sur-valencia/sitemap.xml`** : ajouter l'URL
   `https://capsurvalencia.fr/actualites/2026-08-17-cine-en-las-playas.html` avec
   `<lastmod>2026-08-17</lastmod>`, changefreq monthly, priority 0.8 (même format que les 4
   autres fiches actualités).

## Règles strictes

- Ne modifier QUE : le nouveau fichier fiche, pages/actualites.html, feed.xml, sitemap.xml et
  (si nouvelle photo) assets/img/activites-cine-playas.jpg. AUCUN autre fichier. Ne touche pas
  au CSS, ni à index.html, ni aux autres fiches.
- N'exécute AUCUNE commande (ni build, ni git, ni serveur, ni test). Édite uniquement les fichiers.
- Zéro invention : toute URL, date, horaire, tarif ou téléphone non confirmé → `[À VÉRIFIER]` ou omission.
- Orthographe « Valencia » partout.
- Les fiches existantes utilisent un ton « vous » — reste cohérent.

## Rapport final obligatoire (en français)

1. Liste des URLs sources consultées (avec ce que tu en as tiré — précise la source officielle
   Diputación si trouvée).
2. Photo choisie : fichier, artiste exact, licence exacte, page Commons.
3. Les chiffres utilisés et leur source.
4. Les points restés `[À VÉRIFIER]`, s'il y en a.

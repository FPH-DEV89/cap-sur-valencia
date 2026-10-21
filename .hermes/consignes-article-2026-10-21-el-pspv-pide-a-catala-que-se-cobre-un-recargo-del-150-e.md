# Consignes de rédaction d'article de blog Cap sur Valencia

## Contexte
- Blog d'expatriation familiale (famille de 5 avec 3 enfants, départ Valencia prévu en 2028).
- Longueur de l'article : 900 à 1400 mots.
- Ton direct, à la 1re personne du pluriel (« nous »), chaleureux, pragmatique et structuré.
- Orthographe stricte : TOUJOURS écrire « Valencia » (jamais « València »).
- Chiffres exacts et sourcés, hook réel dès l'introduction.
- ZÉRO cliché : les termes « perle cachée », « incontournable », « joyau méconnu » sont formellement INTERDITS.
- Encadré budget chiffré obligatoire (tableau ou encadré récapitulatif avec coûts concrets en euros).
- Conclusion obligatoire sous l'intertitre H2 : « Notre avis honnête ».
- Anonymat & Confidentialité absolue : AUCUNE information personnelle identifiable (adresse exacte du futur logement interdite, prénoms des enfants interdits, photos de famille interdites).

## Sujet & Sources
- Sujet : El PSPV pide a Catalá que se cobre un recargo del 150% en el IBI a las viviendas turísticas
- Date de publication : 2026-10-21
- URL source de veille : https://valenciaplaza.com/valenciaplaza/valencia/el-pspv-pide-a-catala-que-se-cobre-un-recargo-del-150-en-el-ibi-a-las-viviendas-turisticas
- Extrait / Données de veille : Une initiative municipale propose d'appliquer une majoration pouvant aller jusqu'à 150 % sur la taxe foncière (IBI) des locations touristiques et logements vacants à Valence. Cette pression fiscale vise à désengorger le marché immobilier et à réorienter les biens vers la location résidentielle classique. C'est un signal positif pour les futurs expatriés en recherche d'un bail longue durée pour se loger en famille.

Effectue une recherche web réelle auprès des sources officielles (gva.es, valencia.es, ministères espagnols) et de la presse locale (Levante-EMV, Las Provincias, Valencia Plaza).
⚠️ Interdiction absolue d'inventer une URL, un chiffre, une adresse, un tarif ou un fait — si incertain écris [À VÉRIFIER].

## Fichiers à modifier / créer (NE TOUCHER À AUCUN AUTRE FICHIER) :
1. **Article de blog** :
   - Copier `/tmp/cap-sur-valencia/blog/2026-08-16-bienvenue.html` vers `/tmp/cap-sur-valencia/blog/2026-10-21-el-pspv-pide-a-catala-que-se-cobre-un-recargo-del-150-e.html`.
   - Mettre à jour l'en-tête HTML : `<title>`, `<meta description>`, `<link rel="canonical" href="https://capsurvalencia.fr/blog/2026-10-21-el-pspv-pide-a-catala-que-se-cobre-un-recargo-del-150-e">`, OpenGraph (`og:title`, `og:description`, `og:url`), Twitter cards, H1, date `2026-10-21`.
   - Intégrer le Schema.org JSON-LD complet dans `@graph` (BreadcrumbList + Article / BlogPosting avec headline, datePublished, dateModified, author Florian, publisher).
   - Intégrer une image Wikimedia Commons de qualité CC/CC0 ≥1200px (ou réutiliser une photo pertinente de `assets/img/`) enregistrée dans `assets/img/` avec son crédit sous l'image (auteur + licence) dans un `<figcaption>` ou paragraphe de crédit.
   - Rédiger le contenu complet (900-1400 mots) avec encadré budget, bloc « Infos pratiques » et conclusion « Notre avis honnête ».
   - S'assurer que le HTML se termine bien par `</html>`.

2. **Mettre à jour les listings** :
   - `/tmp/cap-sur-valencia/pages/blog.html` : insérer la nouvelle card en tête de la grille `<div class="blog-grid">` (avec badge catégorie, image, extrait percutant, mini-ligne 📍 durée 💰 « dès X € »).
   - `/tmp/cap-sur-valencia/feed.xml` : insérer le nouvel `<item>` RSS 2.0 en tête sous le premier `<atom:link>`.
   - `/tmp/cap-sur-valencia/sitemap.xml` : insérer la nouvelle URL `<url><loc>https://capsurvalencia.fr/blog/2026-10-21-el-pspv-pide-a-catala-que-se-cobre-un-recargo-del-150-e</loc><lastmod>2026-10-21</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>`.

## Contraintes d'exécution
- Ne modifier QUE ces fichiers.
- N'exécuter AUCUNE commande de build ou git (ni git commit, ni git push, ni deploy).

## Rapport final obligatoire
À la fin de ta réponse, fournis la liste exhaustive des URLs sources consultées avec le détail factuel de ce que tu en as tiré.

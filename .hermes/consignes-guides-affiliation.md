# Mission agy : 2 pages guides monétisation — « Assurance santé » + « Banque en Espagne »

## Contexte

Tu es rédacteur web + développeur front pour le blog « Cap sur Valencia » (blog d'expatriation
familiale française, départ Valencia 2028, famille de 5). Repo : `/tmp/cap-sur-valencia` — site
100 % statique (HTML/CSS/JS vanilla, pas de framework, pas de build, pas de package.json).
Design Stitch : fond beige `#fbfbe2`, navy `#001626`, terracotta `#924b26`, fonts Playfair
Display (titres) + Source Sans 3 (corps).

Mission : créer **2 nouvelles pages guide** dans `/tmp/cap-sur-valencia/pages/` :

1. **`assurance.html`** — « Assurance santé en Espagne : ce qu'il faut savoir avant de partir »
2. **`banque.html`** — « Ouvrir un compte en banque en Espagne (2026) »

Ces pages sont les **pages monétisation** du site (liens d'affiliation SafetyWing + Revolut).
Elles doivent rester 100 % crédibles et utiles — le ton du blog est un journal de bord honnête
(« on », « nous », expériences vécues), JAMAIS une promo sèche.

## Template à copier

Copie la STRUCTURE de `/tmp/cap-sur-valencia/pages/sante.html` intégralement : head (charset,
viewport, js class, title, meta description/keywords, canonical, OG, twitter, RSS link, favicon,
JSON-LD @graph, stylesheet), skip-link, reading-progress, navbar (mêmes liens que sante.html),
content-header (breadcrumb, badge, h1, meta-bar), main (sections avec ids, guide-paths-grid,
guide-path-card, highlight-box, pull-quote, guide-stepper), footer, back-to-top, script main.js.
Adapte les sections au contenu (voir plus bas). Les classes CSS existantes de style.css doivent
suffire — n'invente PAS de nouvelles classes sans vérifier qu'elles existent dans css/style.css.

## Faits DÉJÀ VÉRIFIÉS par l'orchestrateur (à utiliser TELS QUELS, pas besoin de re-vérifier)

### SafetyWing Nomad Insurance (2026, source : guide pricing earthsims mars 2026 + safetywing.com)
- Tarif de base : **dès 56,28 $ US / 4 semaines** (tranche 10-39 ans) — soit ~52 € / 4 semaines.
- Tranches d'âge : 40-49 ans = 92,40 $/4 sem · 50-59 = 145,04 $ · 60-69 = 196,84 $ · 70+ = non couvert.
- **Enfants de moins de 10 ans : GRATUITS** sur la police d'un parent assuré (1 parent = 1 enfant
  gratuit, 2 parents = 2 enfants gratuits). Enfants 10-17 ans : tarif plein 56,28 $/4 sem.
- **Franchise : 0 $** · limite médicale **250 000 $** · évacuation médicale **100 000 $** ·
  dentaire d'urgence 1 000 $ · couverture monde entier · résiliable à tout moment (cycle 4 semaines).
- Exemple famille (2 parents ~35 ans + enfant 4 ans + enfant 12 ans) : 168,84 $/4 semaines
  (~2 195 $/an) — vs 3 000-5 000 $/an chez World Nomads.
- Offre « Complete » (vraie santé internationale, routine incluse) : dès 177,50 $/mois —
  pour expats installés 6+ mois. À mentionner comme option, ne pas détailler.
- ⚠️ HONNÊTETÉ REQUISE : SafetyWing est une assurance **voyage / médicale d'urgence** — ce n'est
  PAS un remplacement de la Sécurité sociale espagnole pour un résident. Le site a déjà une page
  `sante.html` (Sécu espagnole + carte SIP) : l'article doit présenter SafetyWing comme la
  couverture de la **période de transition** (avant l'affiliation à la Sécu espagnole / avant la
  carte SIP) + complément voyage. Ne jamais écrire que ça remplace la Sécu espagnole.

### Revolut parrainage (2026, source : selectra.fr mis à jour 07/08/2026)
- **Jusqu'à 80 € / filleul** versé au parrain (campagnes variables 10-80 €). Le filleul ne reçoit
  rien — c'est le parrain qui encaisse.
- Lien **nominatif** généré dans l'app (Profil > Inviter des amis) — pas de code public.
- Conditions filleul : nouveau client, ouverture via le lien, **commander une carte physique**,
  effectuer **3 paiements d'au moins 5 €** chacun.
- **Maximum 5 filleuls par campagne** · prime versée sous ~10 jours ouvrés.

## Recherche web à faire PAR TOI (obligatoire — vérifie les chiffres avant de les écrire)

### Page banque (l'essentiel de ta recherche)
- Faut-il un compte espagnol quand on s'installe à Valencia ? (IBAN espagnol pour salaire, loyer,
  factures ; NIE ; padrón) — sources fiables (gouvernement espagnol, banques, blogs expat sérieux).
- Banques traditionnelles espagnoles accessibles aux expats : **CaixaBank, Santander, Sabadell,
  ING España, Openbank** (en ligne) — frais, ouverture à distance ou sur rendez-vous, exigence NIE.
- **Revolut en Espagne** : compte espagnol possible, IBAN ES pour les résidents ; comptes multi-
  devises ; vérifie ce point précis (source officielle Revolut help) — si incertain, reste général.
- **N26 en Espagne** : existe, à citer sans lien (programme de parrainage mort en 2026, ne pas
  promettre de prime).
- **BoursoBank** (option secondaire pour les lecteurs FR qui gardent un compte français) : frais
  zéro, mais conditions (dépôt 300 €, revenus 1 000 €/mois) — à confirmer avant d'écrire.
- Vérifier TOUTES les URL que tu cites (web_extract) — une URL morte ou un chiffre faux = page rejetée.

### Page assurance
- Genki (alternative) : tarif approximatif ~35-48 €/mois (déjà vérifié — à confirmer si tu le cites).
- Assurance privée espagnole pour résidents (Sanitas, Adeslas) : mention brève, pas de détail.
- La période d'affiliation à la Sécu espagnole (convention UE / modèle S1) : 1-2 phrases, renvoyer
  vers `sante.html` — ne pas faire de recherche lourde, la page sante.html couvre déjà le sujet.

## Règles éditoriales STRICTES (non négociables — le QA les vérifie)

1. **Orthographe « Valencia »** partout (jamais « València »).
2. **JSON-LD @graph** : BreadcrumbList + Article + Person (auteur) + Organization + ImageObject —
   reprends la structure exacte de sante.html, URLs canoniques en `https://capsurvalencia.fr/pages/assurance`
   et `https://capsurvalencia.fr/pages/banque` (SANS .html — les clean URLs de Cloudflare).
3. **Canonical + og:url** : `https://capsurvalencia.fr/pages/assurance` / `.../pages/banque` (sans .html).
4. **1 photo Wikimedia Commons par page** (≥1200px, licence CC/CC0) : assurance → hôpital/clinique
   de Valencia ou scène médicale ; banque → rue commerçante / bâtiment emblématique de Valencia.
   **Crédit sous chaque image** (artiste + licence). Recette API si besoin :
   `https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=<sujet>&gsrlimit=5&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=1280&format=json`
   (⚠️ rate-limit 429 : espace les requêtes de 2-3 s).
5. **Ton journal de bord** : « nous », « on », expériences de préparation du départ (2028). Phrases
   courtes, jamais de jargon bancaire/assurance gratuit (expliquer chaque terme : NIE, padrón, IBAN,
   franchise, carte SIP).
6. **Pull-quotes** : 1 par page, phrase frappante ISSUE de ton propre texte (pas inventée séparément).
7. **Disclaimer affiliation** (RGPD, OBLIGATOIRE) : en haut (sous le hero, petite ligne) ET en bas :
   « Cet article contient des liens affiliés : si vous passez par eux, nous pouvons recevoir une
   commission, sans coût supplémentaire pour vous. »
8. **Placeholders liens affiliés** (les comptes ne sont pas encore ouverts) :
   - Page assurance : CTA principal avec `href="[LIEN_SAFETYWING_AFFILIE]"` (texte : « Voir les tarifs
     SafetyWing » ou similaire). NE METS PAS de vraie URL d'affiliation.
   - Page banque : section Revolut avec `href="[LIEN_REVOLUT_PARRAINAGE]"` (texte : « Profiter de
     l'offre Revolut »). Idem pour BoursoBank si cité : `[LIEN_BOURSOBANK_PARRAINAGE]`.
   - Ces placeholders seront remplacés par les vraies URLs quand les comptes seront ouverts.
9. **Zéro donnée personnelle de la famille** : pas de prénoms des enfants, pas d'adresse, pas de
   photos identifiables de la famille.
10. **Aucun chiffre non vérifié** : chaque prix/durée/condition cité doit venir de ta recherche
    avec la source notée dans un commentaire HTML `<!-- source: URL -->` en fin de fichier.
11. **Ne crée QUE ces 2 fichiers** : `/tmp/cap-sur-valencia/pages/assurance.html` et
    `/tmp/cap-sur-valencia/pages/banque.html`. Ne modifie AUCUN autre fichier (ni nav, ni footer,
    ni sitemap, ni style.css — Hermes s'en charge). N'exécute AUCUNE commande git/build.
12. **N'utilise PAS de classes CSS qui n'existent pas** dans css/style.css — vérifie avant.

## Structure recommandée

### assurance.html — « Assurance santé en Espagne : ce qu'il faut savoir avant de partir »
1. Hero (titre + intro courte) : la question que tout le monde se pose avant l'expatriation.
2. Partie 1 : le système espagnol en 30 secondes (Sécu espagnole, convention UE, carte SIP —
   renvoi vers `sante.html`, pas de doublon).
3. Partie 2 : la période de transition — le trou de couverture (entre l'arrivée et l'affiliation :
   plusieurs semaines/mois) → c'est LE moment où une assurance voyage/médicale privée a du sens.
4. Partie 3 : SafetyWing en détail — tableau des prix par tranche d'âge (chiffres vérifiés),
   enfants < 10 ans gratuits (argument famille), franchise 0 $, 250 000 $, évacuation, monde entier,
   résiliation à tout moment. Highlight-box « pour notre famille » : 168,84 $/4 semaines.
   ⚠️ Encadré honnêteté (highlight-box-alert) : « SafetyWing = assurance voyage/médicale d'urgence,
   pas un remplacement de la Sécu espagnole ».
5. Partie 4 : alternatives (Genki ~35-48 €/mois, assurance privée espagnole Sanitas/Adeslas pour
   résidents — mention brève).
6. CTA final + disclaimer affiliation (haut ET bas).
7. FAQ (3-4 questions) + JSON-LD FAQPage (comme budget.html si le pattern existe).

### banque.html — « Ouvrir un compte en banque en Espagne (2026) »
1. Hero : l'argent au quotidien quand on s'expatrie — ce qui change (IBAN, NIE, taux de change).
2. Partie 1 : faut-il vraiment une banque espagnole ? (loyer, salaire, factures, démarches →
   l'IBAN espagnol facilite tout ; mais on peut démarrer avec une néobanque).
3. Partie 2 : les banques espagnoles classiques (CaixaBank, Santander, Sabadell, ING España,
   Openbank) — tableau comparatif court (frais, ouverture à distance, NIE requis).
4. Partie 3 : Revolut (et les néobanques) — multi-devises, IBAN local pour résidents, pourquoi
   c'est pratique en transition ; **section parrainage honnête** : « jusqu'à 80 € offerts à celui
   qui parraine (c'est nous 😉) » + conditions (carte physique, 3 paiements de 5 €) +
   `[LIEN_REVOLUT_PARRAINAGE]`.
5. Partie 4 : garder un compte français ? BoursoBank (mention + placeholder), transferts
   (Wise/Revolut) — 1-2 phrases.
6. Récap « notre plan » : néobanque pour le quotidien + banque espagnole classique après le NIE
   (étape par étape, guide-stepper comme sante.html).
7. CTA + disclaimer affiliation (haut ET bas).
8. FAQ (3-4 questions) + JSON-LD FAQPage si le pattern existe.

## Livrable attendu (rapport final en français)
- Liste des 2 fichiers créés (chemins exacts)
- Pour chaque page : titre H1, nb de sections, sources vérifiées (URLs), photo utilisée (fichier + crédit)
- Les chiffres clés cités (prix SafetyWing, conditions Revolut) avec leur source
- Confirmation : aucun autre fichier modifié, aucune commande exécutée

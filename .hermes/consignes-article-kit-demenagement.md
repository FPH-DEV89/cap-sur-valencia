# Cap sur Valencia — Article « Le kit du déménagement en avion » (18/08/2026)

Tu crées UN article complet dans le repo /tmp/cap-sur-valencia : `pages/kit-demenagement-avion.html` (slug : kit-demenagement-avion).

## Contexte

Blog francophone sur l'expatriation à Valencia (Espagne), site statique HTML/CSS/JS (Cloudflare Pages). L'article est un « guide d'achat » monétisé par affiliation Amazon — le PREMIER du site. Le compte Amazon Associates vient d'être activé (ID `capsurvalenci-21`). L'article doit convertir (lecteur qui achète via nos liens) tout en restant 100 % honnête et utile.

## Angle éditorial

- **Titre H1** : « Déménager à Valencia : le kit du voyage en avion (testé en famille) »
- **Promesse** : tout ce qu'une famille de 5 doit prévoir pour le trajet France → Valencia, sans se faire avoir (bagages low-cost, autonomie, confort, sécurité).
- **Fil rouge (intro)** : le support tablette voiture acheté pour les vacances = « le meilleur investissement avant de partir » (témoignage vécu, une phrase d'expérience réelle — pas de promo sèche).
- **Cible** : familles françaises qui envisagent l'expatriation ou un long séjour à Valencia.

## Fichier à créer

- `pages/kit-demenagement-avion.html` — NE modifier AUCUN autre fichier, ne pas exécuter git.
- Template : copie la structure de `pages/assurance.html` (header + nav identiques, mêmes classes CSS : guide-paths-grid, highlight-box, pull-quote, bloc checklist, footer avec 📬 contact@capsurvalencia.fr).
- Toutes les URLs propres (canonical, og:url, JSON-LD) SANS `.html` ; les liens INTERNES gardent `.html`.
- JSON-LD `@graph` : BreadcrumbList + Article (datePublished 2026-08-22) + FAQPage (3-4 questions : « Quelle valise pour Ryanair ? », « Peut-on prendre une power bank en avion ? », « Faut-il un adaptateur de prise en Espagne ? », « Comment peser ses bagages ? »).

## Structure (7 sections H2 — ordre strict)

1. **H2 « Pourquoi ce kit ? »** — intro : on prépare le grand départ vers Valencia avec 3 enfants ; la leçon apprise (support tablette voiture = meilleur investissement voyage) ; annonce : les vrais produits qu'on a validés, avec prix et notes vérifiés ce jour.
2. **H2 « La règle d'or : le bagage cabine low-cost »** — Ryanair/Easyjet/Vueling = porte d'entrée de Valencia, dimensions strictes (55×40×20 ou 45×36×20 selon compagnie) ; micro-conseil : serrure TSA. → **CARTES PRODUIT pour les produits 1 et 2**, lien inline pour le 3 (option premium).
3. **H2 « Le confort de voyage (la catégorie qu'on sous-estime) »** — le calme dans l'avion, les enfants qui dorment. → **CARTE PRODUIT pour le produit 5** (casque), liens inline pour 4 et 6.
4. **H2 « L'autonomie électrique (la vraie peur de l'expat) »** — apps de traduction + GPS + photos = batterie qui fond ; power bank autorisée en avion (règle : < 100 Wh, en cabine, jamais en soute). → **CARTE PRODUIT pour le produit 7**, lien inline pour 8.
5. **H2 « L'organisation (le déménagement, pas les vacances) »** — gagner de la place, ne rien perdre, les documents (passeports, NIE) en sécurité. → liens inline pour 9, 10, 11.
6. **H2 « Et dans la voiture ? (le scénario road trip) »** — le trajet en voiture pour ceux qui préfèrent ; le témoignage du support tablette (rappel du fil rouge). → liens inline pour 12, 13.
7. **H2 « La checklist récap »** — liste des 13 produits avec prix individuel + **total kit ≈ 300 €** (ou ~420 € avec la valise premium) ; rappel : **pas besoin d'adaptateur de prise en Espagne** (mêmes prises type C/E qu'en France) ; CTA final : « Et vous, vous partez en avion ou en voiture ? » + lien vers la page Ressources (pages/ressources.html).

## Les 13 produits — DONNÉES VÉRIFIÉES le 18/08/2026 (à utiliser TELLES QUELLES, NE PAS réinventer prix/notes/avis)

**Format de lien affilié OBLIGATOIRE** : `https://www.amazon.fr/dp/<ASIN>?tag=capsurvalenci-21` (tag exact, rien d'autre).

1. **Sac à dos cabine KLOSTAIN 30L** (45×36×20, compatible Easyjet/Ryanair) — ASIN `B0D59RWBTX` — 28,87 € — 4,7/5 (3 298 avis)
2. **Valise cabine Amazon Basics 55×40×20** (approuvée Ryanair, coque rigide) — ASIN `B07G4SRQC8` — 39,90 € — 4,5/5 (53 226 avis)
3. **Valise Samsonite S'Cure Spinner 75** (option premium soute) — ASIN `B007WQJSGM` — 149,00 € — 4,5/5 (20 082 avis) — à présenter comme « le modèle premium si vous partez avec plus de bagages »
4. **Coussin cervical mémoire de forme Far win** — ASIN `B0DJNM8412` — ~11 € — 4,5/5 (2 161 avis)
5. **Casque Soundcore Q20i (réduction de bruit ANC)** — ASIN `B0C3HCD34R` — 33,99 € — 4,6/5 (71 580 avis) — argument : le silence dans l'avion, indispensable avec enfants
6. **Masque de sommeil 3D occultant Gritin** — ASIN `B0CRYX3FCZ` — 8,69 € — 4,8/5 (13 855 avis)
7. **Power bank INIU 10000 mAh 45 W** — ASIN `B0DC93Z911` — 22,55 € — 4,6/5 (32 190 avis) — mentionner « autorisée en avion »
8. **Power bank INIU 20000 mAh 22,5 W** (version famille) — ASIN `B0FX9HMGWS` — 34,99 € — 4,4/5 (28 560 avis)
9. **Cubes de rangement Amazon Essentials (lot de 4, double fermeture éclair)** — ASIN `B014VBGKFW` — 12,99 € — 4,6/5 (~40 700 avis)
10. **Balance à bagages Blendura 50 kg** — ASIN `B0CVXHDMRZ` — 7,99 € — 4,5/5 (13 127 avis)
11. **Pochette tour de cou anti-RFID WACCET** (passeports, NIE) — ASIN `B07PJ41RBF` — 12,99 € — 4,5/5 (1 125 avis)
12. **Support tablette voiture Lamicall (appuie-tête, rotation 360°)** — ASIN `B0DMR9KJNS` — 18,99 € (1 pc) / 36,99 € (lot de 2) — 4,7/5 (831 avis) — **LE produit du témoignage** (« celui qu'on a acheté pour les vacances »)
13. **Sac de voyage pliable 120 L YOUNGOA** (compartiment chaussures) — ASIN `B0DCFQFBJH` — 39,99 € — 4,5/5 (452 avis) — pour le retour et les cartons

**Prix total à afficher** : kit de base (sans Samsonite) ≈ **300 €** ; avec la Samsonite premium ≈ **420 €**.

## Règles de placement des liens

- **MAX 4 cartes produit avec bouton** (produits 1, 2, 5, 7 — les best-sellers), le reste en **liens inline naturels** dans le texte (1 phrase d'usage réel par produit, pas de specs barbants).
- Chaque lien affilié : `rel="sponsored noopener noreferrer"`.
- **Disclaimer affiliation RGPD en haut ET en bas** (obligatoire) : « Cet article contient des liens affiliés Amazon : si vous passez par eux, nous pouvons recevoir une commission, sans coût supplémentaire pour vous. »
- Encadré « Transparence » (highlight-box) avec le total estimé du kit + explication : commission ~3-5 % reversée, prix identiques pour le lecteur.
- **JAMAIS d'adaptateur de prise** (l'Espagne utilise les mêmes prises qu'en France — piège d'affilié amateur, on l'explique dans la checklist).

## Contenu — règles éditoriales

- Orthographe « Valencia » (jamais « València »), zéro faute, ton chaleureux et direct (blog familial).
- Zéro donnée personnelle (aucun prénom d'enfant, aucune adresse, aucune photo de famille).
- Honnêteté NON négociable : chaque produit = 1 phrase d'usage réel (« on l'utilise pour X »), pas de superlativés de pub ; si un produit est une alternative (« ou »), le dire.
- Photo hero : 1 photo Wikimedia Commons réelle (valises/bagages en voyage ou famille à l'aéroport), ≥1200px, crédit photo (auteur + licence CC) sous l'image.
- Commentaire HTML en fin de fichier : `<!-- Sources : prix/notes vérifiés sur Amazon.fr le 18/08/2026 (ASIN fournis dans la spec) -->`.

## QA interne avant de terminer

- Relis : les 13 ASIN présents exactement dans les liens `?tag=capsurvalenci-21`, cohérence des prix (28,87 / 39,90 / 149 / ~11 / 33,99 / 8,69 / 22,55 / 34,99 / 12,99 / 7,99 / 12,99 / 18,99-36,99 / 39,99), total ≈ 300 € ou ≈ 420 €, pas de doublon de `</p>`, JSON-LD parseable, crédit photo présent, disclaimer haut ET bas, zéro « València », zéro donnée perso, 7 sections H2 dans l'ordre.

# Consignes — Fiche Actualité : Cours de paella en famille à Valencia

Tu crées UNE fiche actualité complète dans le repo /tmp/cap-sur-valencia, en suivant EXACTEMENT la structure et le style de `actualites/2026-08-16-bioparc-valencia.html` (même squelette : header, hero, sections, bloc Infos pratiques, JSON-LD, footer).

## Fichier à créer
- `actualites/2026-08-20-cours-de-paella.html` — slug : cours-de-paella
- Ne modifier AUCUN autre fichier. Ne pas exécuter de commande git.

## Contenu (structure type d'une fiche actualité)
1. **Header + nav** identiques aux autres fiches (mêmes liens relatifs, `aria-current="page"` sur le breadcrumb).
2. **Hero** : titre « Apprendre à cuisiner la paella à Valencia en famille », accroche, photo (voir Photos).
3. **Sections** (4-6) avec `h2` :
   - La paella, une tradition valencienne (histoire : née dans les rizières de l'Albufera, plat du dimanche, cuite au feu de bois de sarment, la socarrat)
   - Le déroulement d'un cours typique (visite du Mercado Central incluse dans les meilleures formules, marché, ingrédients : riz bomba, safran/colorant, poulet-lapin ou fruits de mer ; cuisson sur paellera, dégustation avec sangria ou vin)
   - Cours de paella en famille : ce qu'il faut savoir (⚠️ vérifier les limites d'âge : plusieurs ateliers exigent 12 ans ou plus, certains acceptent les enfants — présenter honnêtement les deux cas, ne pas affirmer « adapté aux enfants » sans preuve)
   - Budget : fourchettes réelles (voir Chiffres vérifiés)
   - Alternatives si les enfants sont trop jeunes (dîner paella en famille dans un restaurant d'El Palmar, barque Albufera — lien interne vers `2026-08-19-albufera-el-palmar.html`)
4. **Bloc « Infos pratiques »** obligatoire, ordre fixe : 📍 Adresse (Mercado Central de Valencia, Plaça de la Ciutat de Bruixes, 2, 46003 Valencia si le cours commence au marché ; sinon indiquer le point de rendez-vous type) · 🕐 Horaires (sessions typiques : matin ~10h-14h ou soir ~17h-21h, variable selon l'atelier — ne pas inventer d'horaires fixes) · 💰 Tarifs (voir Chiffres vérifiés) · 📞 Contact (Mercado Central : +34 96 382 91 01, uniquement si pertinent) · 🌐 Site (ex. paella-cooking-class-valencia.es, visitvalencia.com) · 🚇 Accès (métro Xàtiva L3/L5/L9 ou Colón L3/L5/L7, tram)
5. **Bouton affilié** avant le bloc Infos pratiques :
   `<p style="text-align: center; margin: 2rem 0;"><a href="[LIEN_PAELLA]" class="btn btn-primary" target="_blank" rel="sponsored noopener noreferrer">👨‍🍳 Réserver un cours de paella (dès ~69 €) →</a></p>`
   + encart transparence (pattern exact des autres fiches, highlight-box-advice) avec la mention « Pourquoi ce prix ? » : les prix officiels varient de ~65 à ~100 € selon la formule (marché + dégustation, maison de chef, etc.) ; le lien GetYourGuide mène aux formules notées 5,0/5.
6. **JSON-LD `@graph`** : BreadcrumbList + Article + TouristAttraction (name, address, telephone, url, priceRange `$$$` en notation Schema.org) — reprends le pattern de bioparc-valencia.html. URLs SANS `.html`.
7. **Photos** : 1 photo Wikimedia Commons réelle (paella sur paellera ou Mercado Central), ≥1200px, crédit photo sous l'image (auteur + licence CC) — vérifie que la licence est CC/CC0.
8. **Footer** identique aux autres fiches (avec 📬 contact@capsurvalencia.fr).

## Chiffres vérifiés (à utiliser tels quels, NE PAS inventer d'autres chiffres)
- GetYourGuide : « Real Paella Cooking Class – Market Visit & Sangría Workshop » — note 5,0/5 (373 avis), dès ~75 $ ≈ **~69 €**
- VisitValencia (mai 2026) : « Paella Cooking Class, Wine Tasting & Central Market » — **65 €**, note 5,0/5 (~2 000 avis)
- Cours à domicile avec chef local (TripAdvisor) : à partir de **~100 € par adulte** (prix variable selon le groupe)
- Le billet Oceanogràfic = lien interne vers la fiche existante, ne pas répéter ses tarifs.

## Règles
- Orthographe « Valencia » (jamais « València »), zéro faute.
- Zéro donnée personnelle (aucun prénom d'enfant, aucune adresse perso, aucune photo de famille).
- Encadré « Transparence » avec lien affilié obligatoire (pattern des autres fiches).
- Si une information n'est pas vérifiable (horaires exacts d'un atelier précis, limite d'âge), formuler avec prudence (« la plupart des ateliers », « certaines formules ») — JAMAIS d'affirmation absolue non sourcée.
- Ne pas inventer de numéro de téléphone ni d'URL d'atelier spécifique non vérifié.

## QA interne avant de terminer
- Relis le fichier : cohérence des chiffres (65 / ~69 / ~100 €), pas de doublon de `</p>`, JSON-LD parseable, crédit photo présent, bouton avec `[LIEN_PAELLA]` en placeholder + encart transparence.

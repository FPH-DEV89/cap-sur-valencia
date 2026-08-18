# Consignes — Fiche Actualité : Visite guidée du centre historique de Valencia

Tu crées UNE fiche actualité complète dans le repo /tmp/cap-sur-valencia, en suivant EXACTEMENT la structure et le style de `actualites/2026-08-20-cours-de-paella.html` (même squelette : header, hero, sections, bloc Infos pratiques, JSON-LD, bouton affilié + encart transparence, footer).

## Fichier à créer
- `actualites/2026-08-21-visite-centre-historique.html` — slug : visite-centre-historique
- Ne modifier AUCUN autre fichier. Ne pas exécuter de commande git.

## Contenu (structure type d'une fiche actualité)
1. **Header + nav** identiques aux autres fiches (mêmes liens relatifs, `aria-current="page"` sur le breadcrumb).
2. **Hero** : titre « Le centre historique de Valencia en famille : Cathédrale, Saint-Graal et tours », accroche, photo Wikimedia (voir Photos).
3. **Sections (5-6) avec `h2`** :
   - **Un concentré d'histoire à taille humaine** : le centre historique (Ciutat Vella) = l'un des plus grands d'Europe, ~2000 ans d'histoire (romains, musulmans, couronne d'Aragon) ; tout se visite à pied, quartiers El Carmen, La Seu, Mercat, Ruzafa en périphérie.
   - **La Cathédrale et le Saint-Graal** : cathédrale Santa Maria (mélange gothique/baroque), le calice vénéré comme le Saint-Graal (coupe en agate du Ier siècle, apportée à Valencia au XIIIe siècle — histoire qui fascine les enfants), tarif 8 € avec guide audio inclus, tour du Miguelet (El Micalet) +2 € : 207 marches, 51 m, vue sur le Mercado Central, la Lonja et les Jardins du Túria.
   - **La Lonja de la Seda, joyau UNESCO** : bourse de la soie (XVe siècle), 24 colonnes hélicoïdales, salle d'or ; 2 €, GRATUITE le dimanche et jours fériés ; fermée le lundi.
   - **Les tours médiévales** : Torres de Serranos et Torres de Quart (2 € chacune), vestiges des remparts, vues sur la vieille ville ; les boulets de canon de 1812 encore visibles sur les Torres de Quart (histoire vivante pour les enfants) ; souvent gratuites avec la Valencia Tourist Card.
   - **Le centre historique en famille : conseils pratiques** : visiter le matin (dès 10h, affluence l'après-midi), rythme doux avec enfants (1 attraction par demi-journée), le dimanche = jour des musées gratuits (Lonja, Torres, L'Almoina), pause au Mercado Central (lien interne vers `2026-08-18-mercado-central.html`) ou aux Jardins du Túria, option visite guidée coupe-file pour ne pas faire la queue.
   - **Budget** : circuit DIY ~12-14 €/adulte (Cathédrale 8 € + Miguelet 2 € + 2 tours 2 € chacune) ; visite guidée organisée dès ~19 € (voir Chiffres vérifiés).
4. **Bloc « Infos pratiques »** obligatoire, ordre fixe :
   - 📍 Adresse : Cathédrale Santa Maria, Plaça de l'Almoina, s/n, 46003 Valencia (point de départ du circuit)
   - 🕐 Horaires : Cathédrale lun-sam ~10h30-18h30, dim ~14h-18h30 (variables selon saison — formuler avec prudence) · Lonja mar-sam 10h-19h, dim 10h-14h, fermée lundi
   - 💰 Tarifs : Cathédrale 8 € (guide audio inclus) · Tour Miguelet +2 € · Lonja 2 € (gratuit dimanche) · Torres de Serranos et Quart 2 € chacune · Visite guidée dès ~19 €
   - 📞 Contact : +34 96 391 81 27 (Cathédrale) — à vérifier, si non vérifiable ne pas l'inventer
   - 🌐 Site : catedraldevalencia.es · visitvalencia.com
   - 🚇 Accès : métro L3/L5/L9 arrêt « Xàtiva » ou L3/L5/L7 « Colón » (5-10 min à pied) · bus EMT centre
5. **Bouton affilié** avant le bloc Infos pratiques :
   `<p style="text-align: center; margin: 2rem 0;"><a href="[LIEN_VISITE_CENTRE]" class="btn btn-primary" target="_blank" rel="sponsored noopener noreferrer">🏛️ Réserver une visite guidée du centre historique (dès ~19 €) →</a></p>`
   + encart transparence (pattern exact des autres fiches, highlight-box-advice) avec « Pourquoi ce prix ? » : le circuit DIY coûte ~12-14 €/adulte en entrées séparées ; la visite guidée GetYourGuide (dès ~19 €) ajoute un guide francophone/anglophone et l'accès coupe-file à la Cathédrale — le bon compromis pour ne rien rater sans gérer la logistique.
6. **JSON-LD `@graph`** : BreadcrumbList + Article + TouristAttraction (name « Centre historique de Valencia », address, telephone si vérifié, url, priceRange `$$`) — pattern de cours-de-paella.html. URLs SANS `.html`.
7. **Photos** : 1-2 photos Wikimedia Commons réelles (Cathédrale de Valencia ou Torres de Serranos ou Lonja), ≥1200px, crédit photo sous chaque image (auteur + licence CC) — licence CC/CC0 obligatoire.
8. **Footer** identique aux autres fiches (avec 📬 contact@capsurvalencia.fr).

## Chiffres vérifiés (à utiliser tels quels, NE PAS inventer d'autres chiffres)
- Cathédrale : 8 € adulte (guide audio inclus), tarif réduit ~6,50 € ; Miguelet +2 € (207 marches, 51 m)
- Lonja de la Seda : 2 € (1 € réduit), GRATUITE dimanche et jours fériés, fermée lundi, UNESCO
- Torres de Serranos : 2 € · Torres de Quart : 2 € (impacts de boulets de 1812)
- Visite guidée GetYourGuide « Essentials and World Heritage Sites Walking Tour » : 2 h, note 4,6/5 (818 avis), dès ~19 € (~~23 $~~ 19 $)
- Option premium : « Old Town Tour with Wine & Tapas » ~80 € (5,0/5, ~3 000 avis) — à mentionner comme option adulte
- Saint-Graal : coupe en agate du Ier siècle, à Valencia depuis le XIIIe siècle

## Règles
- Orthographe « Valencia » (jamais « València »), zéro faute.
- Zéro donnée personnelle (aucun prénom d'enfant, aucune adresse perso, aucune photo de famille).
- Encadré « Transparence » avec lien affilié obligatoire (pattern des autres fiches).
- Si une information n'est pas vérifiable (horaires exacts, téléphone), formuler avec prudence (« environ », « généralement ») ou ne pas l'inclure — JAMAIS d'affirmation absolue non sourcée.
- Ne pas inventer de numéro de téléphone ni d'URL non vérifié.
- Le téléphone de la Cathédrale : si tu ne peux pas le vérifier, mets « +34 96 391 81 27 » uniquement si tu le confirmes par recherche, sinon laisse la ligne Contact avec le site web seulement.

## QA interne avant de terminer
- Relis : cohérence des chiffres (8 / 2 / ~19 €), pas de doublon de `</p>`, JSON-LD parseable, crédit photo présent, bouton avec `[LIEN_VISITE_CENTRE]` en placeholder + encart transparence, zéro « València ».

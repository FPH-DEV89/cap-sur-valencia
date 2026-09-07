# Ajout du tracker Umami sur toutes les pages HTML

## Objectif
Ajouter le script de tracking Umami dans le <head> de TOUTES les pages HTML du site Cap sur Valencia (statique) pour compter les visiteurs.

## Fichiers à modifier
TOUS les fichiers `.html` du repo, y compris :
- `index.html` et `404.html` (racine)
- `pages/*.html` (toutes les pages guides)
- `blog/*.html` (tous les articles)
- `actualites/*.html` (toutes les fiches)

Ne pas toucher aux fichiers `.css`, `.js`, `.xml`, `.svg`, images.

## Modification exacte (identique sur chaque fichier)
Insérer la ligne suivante juste avant la balise `</head>` de chaque page (après les balises meta existantes, au même endroit que les autres scripts de head) :

`<script defer src="https://stats.fph-solutions.com/script.js" data-website-id="38bad159-7e24-4082-88cd-d35034fc9eb8"></script>`

## Contraintes
- Ajouter UNIQUEMENT cette ligne. Ne modifier rien d'autre dans les fichiers.
- Si une page contient déjà cette ligne, la laisser telle quelle (idempotent).
- Vérifier l'équilibre des balises : ne pas casser la structure HTML.
- N'exécute AUCUNE commande, ne lance aucun serveur, ne fais aucun commit.

# Spec2 — Correction orthographe fiche Cine en las Playas

## Contexte

Fiche créée à l'instant : `/tmp/cap-sur-valencia/actualites/2026-08-17-cine-en-las-playas.html`.
Le QA de l'orchestrateur a relevé UNE seule erreur à corriger.

## Erreur vérifiée (corrige UNIQUEMENT ça)

**Règle du site : orthographe uniforme « Valencia » (jamais « València »).**

Le fichier contient 3 occurrences de « València-Nord » (lignes 227, 228 et 229), dans les
puces transports :

- ligne 227 : `(~15-20 min depuis València-Nord ou Cabanyal)`
- ligne 228 : `(~30 min depuis València-Nord)`
- ligne 229 : `(~35-40 min depuis València-Nord, puis navette de bus locale vers les plages)`

## Correction attendue

Remplacer les 3 occurrences « València-Nord » par « **Valencia-Nord** » (même phrase, même
formatage HTML, rien d'autre ne change).

## Contraintes

- Ne modifier QUE `/tmp/cap-sur-valencia/actualites/2026-08-17-cine-en-las-playas.html`.
- N'exécute AUCUNE commande (ni build, ni git, ni serveur).
- Ne touche à aucun autre fichier.

## Vérification finale obligatoire

Après correction, vérifie toi-même qu'il ne reste AUCUNE occurrence de « València » dans le
fichier (grep mental : cherche « València »), et que « Valencia » apparaît bien au moins 5 fois.
Rapporte en français : les lignes modifiées.

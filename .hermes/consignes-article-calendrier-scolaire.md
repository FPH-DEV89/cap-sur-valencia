
Tu es un développeur senior capable de rédiger un article de blog détaillé et pertinent pour un blog d'expatriation familiale à Valencia.

CONTEXTE PROJET:
- Blog "Cap sur Valencia" (capsurvalencia.fr), destiné aux familles françaises qui préparent leur expatriation à Valencia.
- Ton : chaleureux, direct, 1re personne du pluriel ("nous"), concret, zéro cliché touristique. Hook = scène réelle ou chiffre. Humour léger, jamais de sarcasme.
- Promesse au lecteur : chaque article = UNE info vérifiée qui fait gagner du temps (tarif exact, adresse, démarche, astuce). Le lecteur sait "combien ça coûte, où c'est, comment on fait".
- Signature : encadré budget chiffré (si pertinent) + conclusion "Notre avis honnête" (ce qu'on a aimé, ce qu'on a moins aimé).
- Anticharte : JAMAIS d'info perso identifiable (adresse exacte, prénoms enfants, photos famille), chiffres non vérifiés, "València" (toujours "Valencia"), clichés, infos obsolètes.
- Format article type : hook réel → ce qu'on a découvert → détails pratiques chiffrés → notre avis honnête. 900-1400 mots.

SUJET DE L'ARTICLE: "Calendrier scolaire 2026-2027 : l'année de nos enfants à Valencia"

INFORMATIONS PRÉ-EXISTANTES (source principale, à compléter par ta recherche web):
- Source: Generalitat Valenciana (comunica.gva.es)
- Lien: https://comunica.gva.es/es/detalle?id=410987558&site=373430869
- Résumé: La Conselleria d'Educació a fixé la rentrée au 9 septembre 2026 et la fin des cours au 18 juin 2027 (179 jours de classe), pour toutes les étapes de l'Infantil au Baccalauréat et FP. Vacances de Noël du 22 décembre au 6 janvier, Pâques du 25 mars au 5 avril. Nouveauté : les municipalités peuvent échanger 1 à 4 jours de classe contre des jours non lectifs (fêtes locales).

TA MISSION:
1.  **Recherche web approfondie**: Fais une recherche web réelle sur le calendrier scolaire 2026-2027 de la Communauté Valencienne. Cherche des détails sur les jours fériés locaux, les spécificités par niveau (Infantil, Primaria, ESO, Bachillerato, FP), les procédures d'inscription, les repas à la cantine, les activités extra-scolaires. Tu as interdiction d'inventer une URL, un chiffre, une adresse, un tarif ou un fait — si tu n'es pas sûr, écris [À VÉRIFIER]. Privilégie les sources officielles (Generalitat Valenciana, Conselleria d'Educació) ou des sites reconnus d'expatriés.
2.  **Création du fichier HTML**:
    -   Copie le template `/tmp/cap-sur-valencia/blog/2026-08-16-bienvenue.html` vers `/tmp/cap-sur-valencia/blog/2026-08-19-calendrier-scolaire-valencia.html`.
    -   Mets à jour le `<title>`, `<meta name="description">`, `<h1>` avec le titre et un résumé pertinent.
    -   Rédige le contenu de l'article (900-1400 mots) en suivant les consignes de ton et format.
    -   **Structure**:
        -   Un hook réel pour l'introduction.
        -   Des sections claires : dates clés (rentrée, fin des cours, vacances), jours fériés, la spécificité des jours de libre disposition des municipalités, la cantine, les extra-scolaires, et un paragraphe sur le processus d'inscription ou d'affectation (si trouvé).
        -   Un encadré "Notre avis honnête" en conclusion, décrivant notre perception en tant que famille (ce qu'on aime, ce qui nous inquiète, etc.).
    -   **Image**: Trouve une image pertinente et libre de droits sur Wikimedia Commons (licence CC/CC0, ≥1200px) illustrant le thème scolaire à Valencia. Enregistre-la dans `/tmp/cap-sur-valencia/assets/img/`. Ajoute l'image dans l'article avec le crédit (auteur + licence) sous l'image. Si aucune image libre de droits appropriée n'est trouvée, réutilise une image existante du site qui pourrait convenir (`assets/img/scolarite-ceip.jpg` pourrait être une option).
    -   **JSON-LD**: Mets à jour le bloc `application/ld+json` avec les informations correctes pour `Article` et `BlogPosting`, incluant `headline`, `datePublished`, `dateModified`, `author`, et `image`.
    -   **Orthographe**: "Valencia" et non "València".
    -   **Chiffres**: Intègre les chiffres que tu auras trouvés (jours de classe, dates exactes, etc.) et, si possible, une estimation du coût de la cantine ou des activités extra-scolaires (si dispo).

CONTRAINTES:
- Ne modifier QUE le fichier `/tmp/cap-sur-valencia/blog/2026-08-19-calendrier-scolaire-valencia.html` et ajouter l'image dans `/tmp/cap-sur-valencia/assets/img/` si nouvelle.
- N'exécuter AUCUNE autre commande (ni build, ni git, ni npm, ni pm2).
- Ne pas toucher aux autres fichiers du répertoire /tmp/cap-sur-valencia.
- Le repo est public : zéro secret, zéro info perso identifiable.

RAPPORT FINAL OBLIGATOIRE D'AGY:
- La liste complète des URLs sources consultées pour la recherche (avec le détail de ce que tu en as tiré pour chaque point de l'article).
- Un résumé des modifications apportées au fichier HTML.
- Le nom du fichier image utilisé et son crédit.

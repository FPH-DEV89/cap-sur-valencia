# Graph Report - .  (2026-08-12)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 133 nodes · 224 edges · 25 communities (9 shown, 16 thin omitted)
- Extraction: 85% EXTRACTED · 12% INFERRED · 3% AMBIGUOUS · INFERRED: 27 edges (avg confidence: 0.69)
- Token cost: 985 input · 1,675 output

## Graph Freshness
- Built from commit: `55368371`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Homepage Content & Guides
- Legacy Design Tokens
- Design Direction & Fonts
- Expat Administrative Procedures
- Client-Side Interactions
- Card & Surface Styles
- Hero & Footer Components
- Budget & Filter Widgets
- Relocation Timeline & Checklist
- Dark Red Color Token
- Sand Noise Texture
- Light Blue Color Token
- Slate Surface Token
- Sun Gold Light Token
- Art de Vivre Section
- Heritage & Architecture Section
- Charcoal Light Token
- JetBrains Mono Font
- MegaPrompt Med Light Token
- Spain Red Dark Token
- Sun Light Token
- Pre-Departure Advice
- Arrival & First Weeks
- Neighborhood Cards Grid

## God Nodes (most connected - your core abstractions)
1. `Guide Checklists d'expatriation` - 24 edges
2. `Guide Ressources & Contacts` - 21 edges
3. `Mega-Prompt — Refonte Maxpatrie v4` - 20 edges
4. `Design Brief v3 — Soleil Méditerranéen` - 19 edges
5. `Page d'accueil Maxpatrie (index.html)` - 15 edges
6. `Guide Administration` - 15 edges
7. `Guide Santé & Sécurité Sociale` - 15 edges
8. `Guide Budget & Coût de la Vie` - 14 edges
9. `Guide Emploi & Carrière` - 14 edges
10. `Guide Écoles par quartier` - 13 edges

## Surprising Connections (you probably didn't know these)
- `CSS token MegaPrompt --med-blue` --semantically_similar_to--> `CSS token --med-blue`  [AMBIGUOUS] [semantically similar]
  MEGA_PROMPT.md → DESIGN_BRIEF.md
- `CSS token MegaPrompt --sun-gold` --semantically_similar_to--> `CSS token --sun-gold`  [AMBIGUOUS] [semantically similar]
  MEGA_PROMPT.md → DESIGN_BRIEF.md
- `CSS token MegaPrompt --spain-red` --semantically_similar_to--> `CSS token --esp-red`  [AMBIGUOUS] [semantically similar]
  MEGA_PROMPT.md → DESIGN_BRIEF.md
- `Police Lora (MegaPrompt)` --semantically_similar_to--> `Police Source Serif 4`  [AMBIGUOUS] [semantically similar]
  MEGA_PROMPT.md → DESIGN_BRIEF.md
- `CSS token MegaPrompt --surface` --semantically_similar_to--> `Legacy token --surface (remplacé)`  [AMBIGUOUS] [semantically similar]
  MEGA_PROMPT.md → DESIGN_BRIEF.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Template commun navbar + content-header + content-body + footer** — index_page, pages_administration_page, pages_budget_page, pages_checklists_page, pages_ecoles_page, pages_emploi_page, pages_quartiers_page, pages_ressources_page, pages_sante_page, pages_scolarite_page [EXTRACTED 0.85]
- **Palette El Sol Mediterráneo** — design_brief_sol_mediterraneo, design_brief_sun_gold, design_brief_sun_gold_deep, design_brief_sun_gold_light, design_brief_med_blue, design_brief_med_blue_deep, design_brief_med_blue_light, design_brief_esp_red, design_brief_esp_red_dark, design_brief_warm_white, design_brief_warm_white_alt, design_brief_charcoal, design_brief_charcoal_light, design_brief_slate_deep, design_brief_slate_surface, design_brief_olive, design_brief_olive_light [EXTRACTED 0.95]
- **Parcours administratif d'installation à Valencia** — pages_administration_nie, pages_administration_empadronamiento, pages_administration_labora, pages_administration_modelo_030, pages_administration_certificado_digital, pages_sante_carte_sip, pages_sante_ceam, pages_sante_convenio_especial [INFERRED 0.75]

## Communities (25 total, 16 thin omitted)

### Community 0 - "Homepage Content & Guides"
Cohesion: 0.19
Nodes (29): Système d'emojis stratégiques, Plan de migration palette, CSS token --olive, CSS token --olive-light, Compte à rebours départ (data-target), Bloc épargne 40 000 €, Page d'accueil Maxpatrie (index.html), AI Slop Test (+21 more)

### Community 1 - "Legacy Design Tokens"
Cohesion: 0.12
Nodes (19): Legacy token --accent (remplacé), Pattern CSS Azulejo Classique, Composant Boutons, CSS token --charcoal-light, CSS token --esp-red, Legacy token --golden (supprimé), Composant Liens, CSS token --med-blue (+11 more)

### Community 2 - "Design Direction & Fonts"
Cohesion: 0.14
Nodes (17): style.css (fichier God File legacy), CSS token --charcoal, Architecture de contraste, Ancienne police Crimson Text, Ancienne police DM Serif Display, Design Brief v3 — Soleil Méditerranéen, Google Fonts (fonts.googleapis.com), Police Playfair Display (+9 more)

### Community 3 - "Expat Administrative Procedures"
Cohesion: 0.29
Nodes (14): Certificat digital FNMT, Les 11 démarches dans l'ordre, DGT — permis de conduire (dgt.es), Démarche Empadronamiento, LABORA — service public emploi valencien, Modelo 030 (résidence fiscale), Démarche NIE, Portail valencia.es (+6 more)

### Community 4 - "Client-Side Interactions"
Cohesion: 0.18
Nodes (8): animateCounter(), counterObserver, navbar, navLinks, navOverlay, navToggle, observer, observerOptions

### Community 5 - "Card & Surface Styles"
Cohesion: 0.18
Nodes (11): Composant Cartes (alternance), Legacy token --cream (supprimé), Legacy token --sand (supprimé), Composant Sections Alternées, Dégradé Sunset Glow (cartes), Legacy token --surface (remplacé), Legacy token --surface-alt (remplacé), CSS token --warm-white (+3 more)

### Community 6 - "Hero & Footer Components"
Cohesion: 0.29
Nodes (8): Composant Footer, Composant Hero (refonte), CSS token --slate-deep, Dégradé Sunset Hero Overlay, Pattern CSS Vague Méditerranéenne, Hero Valencia (#accueil), Texture drapeau Espagne en CSS (hero), Texture drapeau Valencia en CSS (footer)

### Community 7 - "Budget & Filter Widgets"
Cohesion: 0.40
Nodes (5): Calculateur budget (IDs calc-*), Filtre quartiers (data-filter), Rôle QA Tester, Calculateur budget page Budget, Filtre quartiers page Quartiers

## Ambiguous Edges - Review These
- `CSS token --esp-red` → `CSS token MegaPrompt --spain-red`  [AMBIGUOUS]
  MEGA_PROMPT.md · relation: semantically_similar_to
- `CSS token --med-blue` → `CSS token MegaPrompt --med-blue`  [AMBIGUOUS]
  MEGA_PROMPT.md · relation: semantically_similar_to
- `CSS token --sun-gold` → `CSS token MegaPrompt --sun-gold`  [AMBIGUOUS]
  MEGA_PROMPT.md · relation: semantically_similar_to
- `Police Source Serif 4` → `Police Lora (MegaPrompt)`  [AMBIGUOUS]
  MEGA_PROMPT.md · relation: semantically_similar_to
- `Legacy token --surface (remplacé)` → `CSS token MegaPrompt --surface`  [AMBIGUOUS]
  MEGA_PROMPT.md · relation: semantically_similar_to
- `Dégradé Sunset Hero Overlay` → `Texture drapeau Espagne en CSS (hero)`  [AMBIGUOUS]
  MEGA_PROMPT.md · relation: conceptually_related_to

## Knowledge Gaps
- **53 isolated node(s):** `navbar`, `navLinks`, `navOverlay`, `navToggle`, `observer` (+48 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `CSS token --esp-red` and `CSS token MegaPrompt --spain-red`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `CSS token --med-blue` and `CSS token MegaPrompt --med-blue`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `CSS token --sun-gold` and `CSS token MegaPrompt --sun-gold`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Police Source Serif 4` and `Police Lora (MegaPrompt)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Legacy token --surface (remplacé)` and `CSS token MegaPrompt --surface`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Dégradé Sunset Hero Overlay` and `Texture drapeau Espagne en CSS (hero)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Design Brief v3 — Soleil Méditerranéen` connect `Design Direction & Fonts` to `Homepage Content & Guides`, `Legacy Design Tokens`, `Card & Surface Styles`, `Hero & Footer Components`?**
  _High betweenness centrality (0.230) - this node is a cross-community bridge._
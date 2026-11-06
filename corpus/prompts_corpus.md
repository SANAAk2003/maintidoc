# Prompts utilisés pour constituer le corpus

Projet MaintiDoc - Sanaa KASTASS - Site fictif : Atlas Mall, Casablanca.
Vérification des noms fictifs "Escalys" et "Rolway" : recherche web effectuée le 05\11\2026, aucune entreprise d'escaliers mécaniques correspondante trouvée.

## Fiche de référence (collée au début de chaque prompt)

Site fictif : Atlas Mall, Casablanca.

Équipements :
- ESC-A-01 : escalier mécanique modèle EA-200, constructeur fictif "Escalys", entrée principale.
- ESC-B-01 : escalier mécanique modèle RB-300, constructeur fictif "Rolway", étage supérieur.

Voyant orange "MAINTENANCE" (ambigu volontairement) :
- ESC-A-01 : défaut de vitesse de la main courante (code A-12).
- ESC-B-01 : inspection périodique due (code B-07).

Codes d'alarme ESC-A-01 : A-03 arrêt d'urgence activé ; A-07 peigne d'entrée obstrué ; A-12 vitesse de main courante hors tolérance ; A-15 surchauffe du moteur.
Codes d'alarme ESC-B-01 : B-02 arrêt d'urgence activé ; B-05 marche manquante détectée ; B-07 inspection périodique due ; B-11 surchauffe du moteur.

Procédure de contrôle des freins : v1 (2023-06) inspection tous les 6 mois ; v2 (2025-03) inspection tous les 3 mois (contradiction volontaire pour les tests).

Critère d'acceptation du contrôle des freins (valeurs fictives) : v1 (2023-06) distance d'arrêt maximale 1,2 m ; v2 (2025-03) distance d'arrêt maximale 1,0 m.
Groupes d'accès : techniciens_escaliers, responsables.
Convention : identifiants d'équipement en MAJUSCULES avec tirets (ESC-A-01). Documents en français, pages numérotées, figures numérotées "Figure X.Y". Aucune donnée personnelle réelle.

## Journal des prompts

(Chaque prompt est ajouté ci-dessous au format P01, P02... avec : outil, date, objectif, prompt, documents produits, problèmes constatés.)


### P01
- Outil : PO1
- Date : 06\11\2026
- Objectif : manuel d'utilisation et de maintenance de ESC-A-01
- Prompt : fiche de référence (voir plus haut) + la tâche suivante : "Rédige le Manuel d'utilisation et de maintenance de l'escalier mécanique ESC-A-01 (modèle EA-200, Escalys), environ 12 pages numérotées en français. Structure : 1) présentation, 2) consignes de sécurité, 3) description du panneau de commande avec le voyant orange MAINTENANCE (Figure 3.1), 4) tableau des codes d'alarme (page 8), 5) maintenance préventive, 6) contrôle des freins (version v2, 2025-03). Écris Page X au début de chaque page. Décris chaque figure en une phrase. N'invente aucun code absent de la fiche."
- Document produit : manuel_esc_a (manuel_esc_a.pdf)
- Problèmes constatés :
  - Sommaire faux : section 5 annoncée pages 9 et 10, réellement page 10 -> corrigé
  - Version et date du document absentes -> ajoutées (v1.0, 2026-11)
  - Formulation contradictoire du voyant en 3.4 -> reformulée
  - Section 3.5 donnait le sens du voyant de l'ESC-B-01, cas ambigu trop facile -> supprimée
  - A-12 sans arrêt de l'escalier -> ajout de l'arrêt si l'écart persiste
  - Mentions "Page X" du texte différentes des pages réelles du PDF -> mentions supprimées, numérotation en pied de page
  - Figures décrites par l'IA mais non fournies -> générées en PNG avec Claude (script Python), vérifiées par l'étudiante
  - Mise en page finale du PDF (12 pages, pagination alignée sur le pied de page) réalisée avec Claude à partir du texte corrigé par l'étudiante
# Prompts utilisés pour constituer le corpus

Projet MaintiDoc - Sanaa KASTASS - Site fictif : Atlas Mall, Casablanca.
Vérification des noms fictifs "Escalys" et "Rolway" : recherche web effectuée le 05\11\2026, aucune entreprise d'escaliers mécaniques correspondante trouvée.

## Fiche de référence (collée au début de chaque prompt)

Site fictif : Atlas Mall, Casablanca.

Équipements :
- ESC-A-01 : escalier mécanique modèle EA-200, constructeur fictif "Escalys", entrée principale.
- ESC-B-01 : escalier mécanique modèle RB-300, constructeur fictif "Rolway", étage supérieur.

Voyant orange "MAINTENANCE" (ambigu volontairement) :
- ESC-A-01 : défaut de vitesse de la main courante (code A-12).
- ESC-B-01 : inspection périodique due (code B-07).

Codes d'alarme ESC-A-01 : A-03 arrêt d'urgence activé ; A-07 peigne d'entrée obstrué ; A-12 vitesse de main courante hors tolérance ; A-15 surchauffe du moteur.
Codes d'alarme ESC-B-01 : B-02 arrêt d'urgence activé ; B-05 marche manquante détectée ; B-07 inspection périodique due ; B-11 surchauffe du moteur.

Procédure de contrôle des freins : v1 (2023-06) inspection tous les 6 mois ; v2 (2025-03) inspection tous les 3 mois (contradiction volontaire pour les tests).

Critère d'acceptation du contrôle des freins (valeurs fictives) : v1 (2023-06) distance d'arrêt maximale 1,2 m ; v2 (2025-03) distance d'arrêt maximale 1,0 m.
Groupes d'accès : techniciens_escaliers, responsables.
Convention : identifiants d'équipement en MAJUSCULES avec tirets (ESC-A-01). Documents en français, pages numérotées, figures numérotées "Figure X.Y". Aucune donnée personnelle réelle.

## Journal des prompts

(Chaque prompt est ajouté ci-dessous au format P01, P02... avec : outil, date, objectif, prompt, documents produits, problèmes constatés.)

# Prompts utilisés pour constituer le corpus

Projet MaintiDoc - Sanaa KASTASS - Site fictif : Atlas Mall, Casablanca.
Vérification des noms fictifs "Escalys" et "Rolway" : recherche web effectuée le 05\11\2026, aucune entreprise d'escaliers mécaniques correspondante trouvée.

## Fiche de référence (collée au début de chaque prompt)

Site fictif : Atlas Mall, Casablanca.

Équipements :
- ESC-A-01 : escalier mécanique modèle EA-200, constructeur fictif "Escalys", entrée principale.
- ESC-B-01 : escalier mécanique modèle RB-300, constructeur fictif "Rolway", étage supérieur.

Voyant orange "MAINTENANCE" (ambigu volontairement) :
- ESC-A-01 : défaut de vitesse de la main courante (code A-12).
- ESC-B-01 : inspection périodique due (code B-07).

Codes d'alarme ESC-A-01 : A-03 arrêt d'urgence activé ; A-07 peigne d'entrée obstrué ; A-12 vitesse de main courante hors tolérance ; A-15 surchauffe du moteur.
Codes d'alarme ESC-B-01 : B-02 arrêt d'urgence activé ; B-05 marche manquante détectée ; B-07 inspection périodique due ; B-11 surchauffe du moteur.

Procédure de contrôle des freins : v1 (2023-06) inspection tous les 6 mois ; v2 (2025-03) inspection tous les 3 mois (contradiction volontaire pour les tests).

Critère d'acceptation du contrôle des freins (valeurs fictives) : v1 (2023-06) distance d'arrêt maximale 1,2 m ; v2 (2025-03) distance d'arrêt maximale 1,0 m.
Groupes d'accès : techniciens_escaliers, responsables.
Convention : identifiants d'équipement en MAJUSCULES avec tirets (ESC-A-01). Documents en français, pages numérotées, figures numérotées "Figure X.Y". Aucune donnée personnelle réelle.

## Journal des prompts

(Chaque prompt est ajouté ci-dessous au format P01, P02... avec : outil, date, objectif, prompt, documents produits, problèmes constatés.)

# Prompts utilisés pour constituer le corpus

Projet MaintiDoc - Sanaa KASTASS - Site fictif : Atlas Mall, Casablanca.
Vérification des noms fictifs "Escalys" et "Rolway" : recherche web effectuée le 05\11\2026, aucune entreprise d'escaliers mécaniques correspondante trouvée.

## Fiche de référence (collée au début de chaque prompt)

Site fictif : Atlas Mall, Casablanca.

Équipements :
- ESC-A-01 : escalier mécanique modèle EA-200, constructeur fictif "Escalys", entrée principale.
- ESC-B-01 : escalier mécanique modèle RB-300, constructeur fictif "Rolway", étage supérieur.

Voyant orange "MAINTENANCE" (ambigu volontairement) :
- ESC-A-01 : défaut de vitesse de la main courante (code A-12).
- ESC-B-01 : inspection périodique due (code B-07).

Codes d'alarme ESC-A-01 : A-03 arrêt d'urgence activé ; A-07 peigne d'entrée obstrué ; A-12 vitesse de main courante hors tolérance ; A-15 surchauffe du moteur.
Codes d'alarme ESC-B-01 : B-02 arrêt d'urgence activé ; B-05 marche manquante détectée ; B-07 inspection périodique due ; B-11 surchauffe du moteur.

Procédure de contrôle des freins : v1 (2023-06) inspection tous les 6 mois ; v2 (2025-03) inspection tous les 3 mois (contradiction volontaire pour les tests).

Critère d'acceptation du contrôle des freins (valeurs fictives) : v1 (2023-06) distance d'arrêt maximale 1,2 m ; v2 (2025-03) distance d'arrêt maximale 1,0 m.
Groupes d'accès : techniciens_escaliers, responsables.
Convention : identifiants d'équipement en MAJUSCULES avec tirets (ESC-A-01). Documents en français, pages numérotées, figures numérotées "Figure X.Y". Aucune donnée personnelle réelle.

## Journal des prompts

(Chaque prompt est ajouté ci-dessous au format P01, P02... avec : outil, date, objectif, prompt, documents produits, problèmes constatés.)

# Prompts utilisés pour constituer le corpus

Projet MaintiDoc - Sanaa KASTASS - Site fictif : Atlas Mall, Casablanca.
Vérification des noms fictifs "Escalys" et "Rolway" : recherche web effectuée le 05\11\2026, aucune entreprise d'escaliers mécaniques correspondante trouvée.

## Fiche de référence (collée au début de chaque prompt)

Site fictif : Atlas Mall, Casablanca.

Équipements :
- ESC-A-01 : escalier mécanique modèle EA-200, constructeur fictif "Escalys", entrée principale.
- ESC-B-01 : escalier mécanique modèle RB-300, constructeur fictif "Rolway", étage supérieur.

Voyant orange "MAINTENANCE" (ambigu volontairement) :
- ESC-A-01 : défaut de vitesse de la main courante (code A-12).
- ESC-B-01 : inspection périodique due (code B-07).

Codes d'alarme ESC-A-01 : A-03 arrêt d'urgence activé ; A-07 peigne d'entrée obstrué ; A-12 vitesse de main courante hors tolérance ; A-15 surchauffe du moteur.
Codes d'alarme ESC-B-01 : B-02 arrêt d'urgence activé ; B-05 marche manquante détectée ; B-07 inspection périodique due ; B-11 surchauffe du moteur.

Procédure de contrôle des freins : v1 (2023-06) inspection tous les 6 mois ; v2 (2025-03) inspection tous les 3 mois (contradiction volontaire pour les tests).

Critère d'acceptation du contrôle des freins (valeurs fictives) : v1 (2023-06) distance d'arrêt maximale 1,2 m ; v2 (2025-03) distance d'arrêt maximale 1,0 m.
Groupes d'accès : techniciens_escaliers, responsables.
Convention : identifiants d'équipement en MAJUSCULES avec tirets (ESC-A-01). Documents en français, pages numérotées, figures numérotées "Figure X.Y". Aucune donnée personnelle réelle.

## Journal des prompts

(Chaque prompt est ajouté ci-dessous au format P01, P02... avec : outil, date, objectif, prompt, documents produits, problèmes constatés.)


## P04 à P10 - Traitement et Cas d'usage du Corpus (06/11/2026)
- Intégration des blocs de test pour l'évaluation des réponses de l'assistant.
- Validation de la conformité des sources documentaires et des contraintes d'abstention.

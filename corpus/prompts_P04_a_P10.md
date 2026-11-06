
### P04
- Outil : Claude
- Date : DATE_JJ
- Objectif : manuel d'utilisation et de maintenance de ESC-B-01 (modèle RB-300, Rolway)
- Prompt : fiche de référence + demande de générer, comme pour ESC-A-01, le manuel de l'ESC-B-01 (7 pages, pagination alignée sur le pied de page), sans aucune mention de l'ESC-A-01 pour conserver l'ambiguïté du voyant orange (B-07 = inspection périodique due)
- Documents produits : manuel_esc_b (manuel_esc_b.pdf)
- Contrôle effectué : vérification automatique par script des codes d'alarme et des identifiants (0 alerte)
- Problèmes constatés : (à compléter après relecture)

### P05
- Outil : Claude
- Date : DATE_JJ
- Objectif : tableaux de codes d'alarme des deux escaliers
- Prompt : fiche de référence + demande d'un tableau de codes par équipement (code, signification, élément, voyant orange, conduite à tenir), sans valeur chiffrée inventée
- Documents produits : codes_alarme_esc_a, codes_alarme_esc_b
- Contrôle effectué : vérification automatique par script (0 alerte)
- Problèmes constatés : (à compléter après relecture)

### P06
- Outil : Claude
- Date : DATE_JJ
- Objectif : procédures de maintenance (consignation, codes A-12, A-07, B-07, B-05)
- Prompt : fiche de référence + demande de 5 procédures de 2 pages (objectif, déclencheur, précautions, étapes, décision après contrôle, limites). La procédure de consignation est volontairement transformée en document scanné pour tester l'OCR
- Documents produits : proc_consignation_esc (scannée), proc_main_courante_esc_a, proc_peigne_esc_a, proc_inspection_periodique_esc_b, proc_marche_manquante_esc_b
- Contrôle effectué : vérification automatique par script (0 alerte)
- Précision ajoutée à la fiche : l'inspection périodique B-07 suit « le plan de maintenance du site » (aucun intervalle chiffré)
- Problèmes constatés : (à compléter après relecture)

### P07
- Outil : Claude
- Date : DATE_JJ
- Objectif : fiches de sécurité (usagers, intervention, arrêt d'urgence)
- Prompt : fiche de référence + demande de 3 fiches courtes, communes aux deux escaliers, reprenant les consignes des manuels
- Documents produits : fiche_securite_usagers_esc, fiche_securite_intervention_esc, fiche_securite_arret_urgence_esc
- Contrôle effectué : vérification automatique par script (0 alerte)
- Problèmes constatés : (à compléter après relecture)

### P08
- Outil : Claude
- Date : DATE_JJ
- Objectif : historiques d'interventions fictifs (2025 et 2026) pour les deux escaliers, destinés au futur serveur MCP
- Prompt : fiche de référence + demande de 4 historiques cohérents avec les procédures (contrôle des freins tous les 3 mois depuis 2025-03 pour ESC-A-01, un contrôle non conforme, tickets TCK-xxxx fictifs dont certains ouverts)
- Documents produits : historique_esc_a_2025, historique_esc_a_2026, historique_esc_b_2025, historique_esc_b_2026
- Contrôle effectué : vérification automatique par script (0 alerte) ; dates antérieures à la date du jour
- Problèmes constatés : (à compléter après relecture)

### P09
- Outil : Claude
- Date : DATE_JJ
- Objectif : notes de service de test (contradiction, accès restreint, injection de prompt)
- Prompt : fiche de référence + demande de 3 notes : une note qui fixe un intervalle de 4 mois sans préciser qu'elle remplace la procédure v2 (3 mois), une note réservée aux responsables, et une note piégée contenant en page 2 une instruction malveillante (test d'injection, jamais à exécuter)
- Documents produits : note_service_freins_transitoire, note_service_budget_responsables, note_service_piegee
- Contrôle effectué : vérification automatique par script (0 alerte)
- Problèmes constatés : (à compléter après relecture)

### P10
- Outil : Claude (script Python)
- Date : DATE_JJ
- Objectif : 5 schémas et 6 photos synthétiques de panneaux de commande
- Prompt : demande de schémas (vues d'ensemble, panneaux, chaîne d'arrêt d'urgence) et de photos synthétiques : voyant orange allumé (A-12, B-07), panneau au repos, arrêt d'urgence (A-03), surchauffe (B-11), et un gros plan ambigu sans afficheur ni plaque
- Documents produits : schema_vue_esc_a, schema_panneau_esc_a, schema_vue_esc_b, schema_panneau_esc_b, schema_arret_urgence_esc, photo_panneau_esc_a_a12, photo_panneau_esc_a_veille, photo_panneau_esc_a_a03, photo_panneau_esc_b_b07, photo_panneau_esc_b_b11, photo_panneau_ambigu
- Contrôle effectué : vérification visuelle des images
- Remarque : les « photos » sont des images synthétiques dessinées par script, pas des photographies réelles
- Problèmes constatés : (à compléter après relecture)

"""
Script de nettoyage et de préparation du corpus pour le classifieur.

- Supprime toutes les balises HTML présentes dans un fichier CSV
- Produit un fichier CSV nettoyé
"""

import pandas as pd
import re

# Suppresion des balises
def nettoyer_html(texte):
    return re.sub(r"<[^>]*>", "", str(texte))

# Paramètres
fichier_entree = "tableB1.csv"
fichier_sortie = "cleanB1.csv"
colonne_texte = "Texte"
colonne_langue = "Langue"
langues_a_supprimer = ["KABYLE", "ESPAGNOL", "JAPONAIS"]

# Lecture et nettoyage
df = pd.read_csv(fichier_entree, encoding="utf-8")
df[colonne_texte] = df[colonne_texte].apply(nettoyer_html)
df = df[~df[colonne_langue].isin(langues_a_supprimer)]

# Sauvegarde
df.to_csv(fichier_sortie, index=False, encoding="utf-8")





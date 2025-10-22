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
fichier_entree = "tableA1.csv"
fichier_sortie = "cleanA1.csv"
index_colonne = 1 

df = pd.read_csv(fichier_entree, header=None, encoding="utf-8")
df[index_colonne] = df[index_colonne].apply(nettoyer_html)
df.to_csv(fichier_sortie, index=False, header=False, encoding="utf-8")





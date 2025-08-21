"""
Module utilitaire pour gérer les êtres vivants (Animal et Plante) 
dans l'application Tkinter.

Ce module fournit :
- La fonction `senourrir` pour afficher le comportement alimentaire de chaque être vivant.
- La fonction `sauvegarde_etrevivant_fichier` pour enregistrer 
les êtres vivants dans un fichier texte.
- La fonction `sauvegarde_noms_interface` pour afficher les noms des êtres vivants 
dans l'interface graphique Tkinter,
  avec un affichage en colonnes (5 noms par colonne) et un header.
"""
import tkinter as tk
from typing import List
from models import EtreVivant, Animal, Plante
from style_config import TAGS_STYLE, FONT_LABEL, FONT_PRIMARY


def senourrir(etre_vivants: List[EtreVivant]) -> None:
    """Afficher le comportement de déplacement de chaque animal (polymorphisme)."""
    for etre_vivant in etre_vivants:
        print(etre_vivant.se_nourrir())

def sauvegarde_etrevivant_fichier(etre_vivants: List[EtreVivant], filename: str) -> None:
    """Sauvegarde les êtres vivants dans un fichier texte trié par nom."""
    sorted_etre_vivant = sorted(etre_vivants, key=lambda a: a.nom.lower())
    with open(filename, "w", encoding="utf-8") as fichier:
        for etre_vivant in sorted_etre_vivant:
            if isinstance(etre_vivant, Animal) and etre_vivant.age > 10:
                fichier.write(
                    f"(Animal) ->\n"
                    f"Nom :{etre_vivant.nom}\n"
                    f"Âge :{etre_vivant.age}\n"
                    f"Espèces :{etre_vivant.especes}\n"
                    f"Nourriture : {etre_vivant.nourriture}\n\n"
                    )
            elif isinstance(etre_vivant, Plante) and etre_vivant.age > 10:
                fichier.write(
                    f"(Plante) ->\n"
                    f"Nom :{etre_vivant.nom}\n"
                    f"Âge :{etre_vivant.age}\n"
                    f"Type de feuille : {etre_vivant.type_feuille}\n"
                    f"Couleur de fleur: {etre_vivant.couleur_fleur}\n\n"
                    )

def sauvegarde_noms_interface(etre_vivants: List[EtreVivant], frame: tk.Frame) -> None:
    """ Sauvegarde les noms dans l'interface.
    Afficher les noms dans des colonnes avec 5 noms par colonne, header à row=8.
    """
    sorted_nom = sorted(etre_vivants, key=lambda a: a.nom.lower())

    # Supprimer les anciens labels si on reclique plusieurs fois
    for widget in frame.grid_slaves():
        if getattr(widget, "is_name_label", False) or getattr(widget, "is_header_label", False):
            widget.destroy()

    header_row = 8
    max_rows_per_col = 5  # 5 noms par colonne

    # Ajouter le header
    header = tk.Label(frame, text="Noms des Êtres Vivants", **FONT_LABEL, **TAGS_STYLE)
    header.is_header_label = True
    header.grid(row=header_row, column=0, columnspan=5, pady=(30, 5), sticky="NSEW")

    # Commencer la liste des noms juste après le header
    start_row = header_row + 1
    for idx, etre_vivant  in enumerate(sorted_nom):
        if isinstance(etre_vivant, Animal):
            text = f"Animal : {etre_vivant.nom}"
        else:
            text = f"Plante : {etre_vivant.nom}"
        col = idx // max_rows_per_col # nouvelle colonne toutes les 5 lignes
        row = start_row + (idx % max_rows_per_col)  # ligne à l’intérieur de la colonne
        label = tk.Label(frame, text=text, **TAGS_STYLE, font=FONT_PRIMARY, padx=10, pady=5, 
                         borderwidth=0, relief="solid")
        label.is_name_label = True
        label.grid(row=row, column=col, padx=5, pady=5, sticky="w")

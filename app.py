"""
Module d'interface graphique pour la création et la gestion
des êtres vivants (Animal et Plante) avec Tkinter.
Fournit les fonctions pour créer, afficher et gérer les
champs de saisie, bouton et label dans la fenêtre principale.
"""
import tkinter as tk
from tkinter import messagebox
from models import Animal, Plante
from utils import senourrir, sauvegarde_etrevivant_fichier, sauvegarde_noms_interface
from style_config import (
    TAGS_STYLE, FONT_LABEL,
    INPUT_FIELD, PRIMARY_COLOUR, 
    BUTTON_EXIT, BUTTON_DISPLAY, 
    BUTTON_CREAT, SECONDARY_COLOUR
)

# ===================
# DONNÉES D'EXEMPLE
# ===================
etre_vivants = [
    Animal("Lion", 15, "Mammifère", "Carnivore"),
    Animal("Perroquet", 10, "Oiseau", "Herbivore"),
    Plante("Lotus", 8, "Large", "Argentée"),
    Plante("Aloe", 15, "Épineuse", "Jaune"),
]

# Exécuter la fonction se_nourrir() sur les êtres vivants
senourrir(etre_vivants)

# Créer le fichier etres_vivants.txt pour sauvegarder les informations
sauvegarde_etrevivant_fichier(etre_vivants, "etres_vivants.txt")

# ====================
# INTERFACE TKINTER
# ====================
root = tk.Tk()
root.title("Créateur d'êtres vivants")
root.geometry("750x750")
root.configure(bg=SECONDARY_COLOUR)
root.resizable(False, False)

# Conteneur principal (Frame)
frame = tk.Frame(root, padx=20, pady=40, bg=PRIMARY_COLOUR)
frame.pack(fill="both", expand=True, pady=20, padx=20)

# Rendre les colonnes de la grille de largeur égale
# → weight=1 : elles s'agrandissent également si la fenêtre change
# → uniform="form" : garantit que les colonnes 0, 1 et 2 auront la même largeur
for col in range(3):
    frame.grid_columnconfigure(col, weight=1, uniform="form")

# Radiobuttons - Variable de type (Animal ou Plante), par défaut "Animal"
entry_type = tk.StringVar(value="Animal")

# Définition des champs de saisie pour chaque type
field_definitions = {
    "Animal": ["Nom", "Âge", "Espèces", "Nourriture de l'animal"],
    "Plante": ["Nom", "Âge", "Type de feuille", "Couleur de fleur"]
}

entries = {}  # dictionnaire pour stocker labels et champs de saisie

# Créer tous les champs mais ne les afficher qu'en fonction du type sélectionné
for field in set(field_definitions["Animal"] + field_definitions["Plante"]):
    label_field = tk.Label(frame, text=field + " :", **TAGS_STYLE, **FONT_LABEL)
    entry_field = tk.Entry(frame, **INPUT_FIELD)
    entries[field] = {"label": label_field, "entry": entry_field}

def update_fields():
    """Afficher uniquement les champs pertinents selon le type choisi (Animal ou Plante)."""
    # Masquer tous les champs
    for show_field in entries.values():
        show_field["label"].grid_forget()
        show_field["entry"].grid_forget()

    # Afficher uniquement les champs correspondant au type sélectionné
    fields = field_definitions[entry_type.get()]
    for idx, field_input in enumerate(fields):
        entries[field_input]["label"].grid(row=idx+1, column=0, sticky="E", padx=(0,8), pady=4)
        entries[field_input]["entry"].grid(row=idx+1, column=1, sticky="WE", pady=4)

def creer_etre_vivant():
    """Créer un nouvel être vivant (Animal ou Plante) et l’ajouter à la liste."""
    get_fields = field_definitions[entry_type.get()]
    values = {}
    # Vérification : tous les champs obligatoires doivent être remplis
    for get_field in get_fields:
        values[get_field] = entries[get_field]["entry"].get().strip()
        if not values[get_field]:
            messagebox.showerror("Erreur", f"Le champ {get_field.upper()} est obligatoire.")
            return
    # Vérification : l’âge doit être un entier
    try:
        age = int(values["Âge"])
        if age <= 0:
            messagebox.showerror("Erreur", "L'âge doit être supérieur à 0.")    
    except ValueError:
        messagebox.showerror("Erreur", "L'âge doit être un nombre entier.")
        return
    # Création de l'objet correspondant (Animal ou Plante)
    if entry_type.get() == "Animal":
        etre_vivant = Animal(values["Nom"], age, values["Espèces"], values["Nourriture de l'animal"])
    else:
        etre_vivant = Plante(values["Nom"], age, values["Type de feuille"], values["Couleur de fleur"])
    # Ajout dans la liste et sauvegarde dans le fichier
    etre_vivants.append(etre_vivant)
    sauvegarde_etrevivant_fichier(etre_vivants, "etres_vivants.txt")
    # Message de succès
    messagebox.showinfo("Succès", f"Génial ! Vous avez créé avec succès le être vivant {entry_type.get().upper()}.")

    # Réinitialiser les champs
    clear_entries()

    # Si les noms sont affichés, rafraîchir l’affichage
    if not SHOWING_INFO:
        sauvegarde_noms_interface(etre_vivants, frame)

def clear_entries():
    """Effacer les champs de saisie après la création d’un être vivant."""
    for input_field in entries.values():
        input_field["entry"].delete(0, tk.END)
    entry_type.set("Animal")
    update_fields()

# ======================
# CLEAR NAMES INTERFACE
# ======================
def clear_noms_interface():
    """Détruit tous les labels de noms ajoutés par sauvegarde_noms_interface."""
    for widget in frame.grid_slaves():
        if getattr(widget, "is_name_label", False) or getattr(widget, "is_header_label", False):
            widget.destroy()

# ====================
# WIDGETS
# ====================

# Radiobuttons pour choisir Animal ou Plante
tk.Label(frame, text="Êtres vivants :",
         **TAGS_STYLE, **FONT_LABEL).grid(row=0, column=0, sticky="E", padx=(0,8))
tk.Radiobutton(frame, text="Animal", variable=entry_type,
        value="Animal", command=update_fields,
        **TAGS_STYLE, **FONT_LABEL, cursor="hand2").grid(row=0, column=1, sticky="NSEW")
tk.Radiobutton(frame, text="Plante", variable=entry_type, value="Plante",
        command=update_fields,
        **TAGS_STYLE, **FONT_LABEL, cursor="hand2").grid(row=0, column=2, sticky="W")

# Variable globale de contrôle pour l’affichage des infos
SHOWING_INFO = True

def toggle_info():
    """Alterner entre afficher les noms des êtres vivants et afficher le message d’information."""
    global SHOWING_INFO # indiquer à Python que l'on utilise la variable globale
    if SHOWING_INFO:
        # Premier clic → cacher l’info, afficher les noms
        info_label.grid_remove()
        sauvegarde_noms_interface(etre_vivants, frame)
        toggle_button.config(text="Masquer les noms")
    else:
        # Deuxième clic → cacher les noms, réafficher le message
        clear_noms_interface()
        info_label.grid()
        toggle_button.config(text="Afficher les noms")
    SHOWING_INFO = not SHOWING_INFO

# Boutons principaux
tk.Button(frame, text="Créer Êtres Vivants", command=creer_etre_vivant,
          **BUTTON_CREAT).grid(row=6, column=0, sticky="EW", padx=5, pady=(40,0))
tk.Button(frame, text="QUITTER", command=root.destroy,
          **BUTTON_EXIT).grid(row=6, column=2, sticky="EW", padx=5, pady=(40,0))

# Bouton pour afficher/masquer les noms
toggle_button = tk.Button(frame, text="Afficher Les Noms", command=toggle_info, **BUTTON_DISPLAY)
toggle_button.grid(row=6, column=1, sticky="EW", padx=5, pady=(40,0))

# Label d’information (affiché par défaut)
info_label = tk.Label(frame,
    text='Cliquez sur le bouton "Afficher les noms" pour voir \n le nom de chaque être vivant.', **TAGS_STYLE, **FONT_LABEL)
info_label.grid(row=7, column=0, sticky="EW", columnspan=3, pady=(20, 0))

# Initialiser les champs
update_fields()

# Boucle principale Tkinter
root.mainloop()

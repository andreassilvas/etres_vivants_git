"""
Module définissant la classe abstraite EtreVivant.

Ce module fournit :
- La classe abstraite `EtreVivant` avec des propriétés de base (`nom`, `age`).
- Des setters et getters pour ces propriétés.
- Une méthode abstraite `se_nourrir` que toutes les sous-classes doivent implémenter.

Les sous-classes (par exemple `Animal` et `Plante`) doivent hériter de `EtreVivant` 
et définir le comportement spécifique de `se_nourrir`.
"""
from abc import ABC, abstractmethod

class EtreVivant(ABC):
    """
    Classe représentant un être vivant.

    Attributs :
        _nom (str) : Nom de l'être vivant.
        _age (int) : Âge de l'être vivant.
        
        convention pour dire « interne à la classe », 
        donc à ne pas modifier directement à l’extérieur.
    """
    def __init__(self, nom: str, age: int):
        self._nom = nom
        self._age = age

    @property
    def nom(self) -> str:
        """Retourne le nom de l'être vivant."""
        return self._nom

    @nom.setter
    def nom(self, value: str):
        """Modifie le nom de l'être vivant.
        
        Args:
            value (str): Nouveau nom à attribuer.
        """
        self._nom = value

    @property
    def age(self) -> int:
        """Retourne l'âge de l'être vivant."""
        return self._age

    @age.setter
    def age(self, value: int):
        """Modifie l'âge de l'être vivant.
        
        Args:
            value (int): Nouvel âge à attribuer.
        """
        self._age = value
    @abstractmethod
    def se_nourrir(self) -> str:
        """Méthode abstraite qui doit retourner une description
        de la manière dont l'être vivant se nourrit.

        Returns:
            str: Description du mode d'alimentation.
        """
    def __str__(self):
        return f"{self.nom}, âge: {self.age}"


class Animal(EtreVivant):
    """
    Classe représentant une Animal.
    """
    def __init__(self, nom: str, age: int, especes: str, nourriture: str):
        super().__init__(nom, age)
        self.especes = especes
        self.nourriture = nourriture
    def se_nourrir(self):
        return f"{self.nom}, Cet animal suit un régime {self.nourriture}."
    def emettre_son(self):
        """Produit un son spécifique selon le genre de l'animal."""
        sons = {
            "Insecte géant": "Bzzz...!",
            "Amphibien": "Croa croa!",
            "Créature marine": "Glouuu glou!"
        }
        print(sons.get(self.especes, "Ce genre reste silencieux."))

    def __str__(self):
        return f"{super().__str__()}, Espèces: {self.especes}, Se nourrir: {self.nourriture}"


class Plante(EtreVivant):
    """
    Classe représentant une plante.
    """
    def __init__(self, nom: str, age: int, type_feuille: str, couleur_fleur: str):
        super().__init__(nom, age)
        self.type_feuille = type_feuille
        self.couleur_fleur = couleur_fleur
    def se_nourrir(self) -> str:
        return f"{self.nom}, Cette plante produit son énergie grâce à la lumière et à l'eau."
    def besoin_eau(self):
        """Indique les besoins en arrosage selon le type de feuille."""
        if self.type_feuille.lower() == "épineuse":
            print("Arrosage rare, adapté aux milieux arides.")
        elif self.type_feuille.lower() == "large":
            print("Besoins élevés en eau, surtout en période chaude.")
        else:
            print("Besoins en eau variables, à observer selon la saison.")
              
    def __str__(self) -> str:
        return f"{super().__str__()}, Type de feuille: {self.type_feuille}, Couleur de fleur: {self.couleur_fleur}"
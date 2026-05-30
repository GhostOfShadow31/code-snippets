"""
Structure de donnée : Noeud
"""

class Node:
    """
    Représente un noeud (Node), un élément d'une liste chainée (LinkedList)
    """

    def __init__(self, value):
        """
        Initialise un noeud
        """

        self.value = value
        self.next = None
    
    def __str__(self):
        """
        Représentation textuelle d'un noeud
        """

        return f"{self.value}"
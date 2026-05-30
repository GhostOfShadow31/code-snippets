""""
Structure de données : Linked List
"""

from node import Node

class LinkedList:
    """
    Représente une liste chainée (LinkedList) composée de noeud (Node).
    """

    def __init__(self):
        """
        Initialise une liste chainée.
        """

        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, item):
        """
        Ajoute un noeud à la fin de la liste chainée.
        
        Parameters:
            item: noeud à ajouter
        """

        element = Node(item)

        if self.head is None: # LinkedList vide
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            self.tail = element
        
        self.length += 1
    
    def prepend(self, item):
        """
        Ajoute un noeud au début de la liste chainée.
        
        Parameters:
            item: noeud à ajouter
        """

        element = Node(item)

        if self.head is None: # LinkedList vide
            self.head = element
            self.tail = element
        else:
            element.next = self.head
            self.head = element
        
        self.length += 1

    def insert(self, index, item):
        """
        Insert un item à un indec donnée dans la liste chainée.
        
        Parameters:
            index: index d'insertion
            item: noeud à ajouter
        
        Raises:
            IndexError: si l'index est invalide
        """

        absolute_index = index if index >= 0 else self.length + index

        if absolute_index > self.length: # Index hors de portée
            raise IndexError("Index hors de portée")
        
        if absolute_index == 0: # Ajout au début de la liste chainée
            self.prepend(item)
            return
        
        if absolute_index == self.length: # Ajout à la fin de la liste chainée
            self.append(item)
            return

        element = Node(item)
        iterator = self.head
        compteur = 0

        while compteur < absolute_index - 1:
            iterator = iterator.next
            compteur += 1
        
        # Insertion
        element.next = iterator.next
        iterator.next = element
        
        self.length += 1
    
    def remove(self, item):
        """
        Supprimer un noeud de la liste chainée.
        
        Parameters:
            item: noeud à retirer
        """

        if self.length == 0:
            return

        # Supression du head
        if self.head.value == item:
            self.head = self.head.next
            self.length -= 1

            if self.head is None:
                self.tail = None
            
            return
    

        prev = self.head
        current = self.head.next

        while current is not None:
            if current.value == item:
                prev.next = current.next

                # Mise à jour du tail si besoin
                if current == self.tail:
                    self.tail = prev
                
                self.length -= 1
                return
            
            prev = current
            current = current.next

    def pop(self, index=-1):
        """
        Supprimer et retourne un noeud à l'indice donné
        
        Parameters:
            index: l'index du noeud à supprimer
        
        Raises:
            IndexError: si l'index est hors de portée
        """
        absolute_index = index if index >= 0 else self.length + index

        if absolute_index < 0 or absolute_index >= self.length: # Index hors de portée
            raise IndexError("Index hors de portée")

        # Suppression du head
        if absolute_index == 0:
            value = self.head.value
            self.head = self.head.next

            if self.head is None:
                self.tail = None
            
            self.length -= 1
            return value
        
        prev = self.head
        
        for _ in range(absolute_index - 1):
            prev = prev.next
        
        current = prev.next
        value = current.value
        
        prev.next = current.next

        # Mise à jour du tail si besoin
        if current == self.tail:
            self.tail = prev
        
        self.length -= 1
        return value

    def find(self, item):
        """
        Trouve un item dans la liste chainée ou renvoie None
        
        Parameters:
            item: l'item à trouver
        """
        iterator = self.head

        while iterator is not None:
            if iterator.value == item:
                return iterator
            
            iterator = iterator.next
        
        return None
    
    def contains(self, item):
        """
        Vérifie si un item est contenu dans la liste chainée

        Parameters:
            item: l'item à vérifier
        
        Returns:
            bool: True si contenue, False sinon
        """
        return self.find(item) is not None

    
    def is_empty(self):
        """
        Vérifie si la liste chainée est vide.

        Returns:
            bool: True si vide, False sinon
        """

        return self.length == 0

    def clear(self):
        """
        Vide la liste chainée
        """

        self.head = None
        self.tail = None
        self.length = 0
    
    def size(self):
        """
        Retourne la taille de la liste chainée
        """

        return self.length
    
    def __len__(self):
        """
        Permet de faire len(LinkedList).
        """

        return self.length
    
    def __str__(self):
        """
        Représentation textuelle d'une liste chainée.
        """

        return f"({self.head}, {self.tail})"
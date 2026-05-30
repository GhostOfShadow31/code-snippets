"""
Structure de données : File (FIFO)
"""

class Queue:
    """
    Représente une file (Queue) utilisant le principe FIFO
    (First In First Out).
    
    Le premier élément ajouté est le premier retiré.
    """

    def __init__(self):
        """
        Initialise une file vide.
        """

        self.items = []
        self.length = 0
    
    def enqueue(self, item):
        """
        Ajoute un élément à la fin de la file.
        
        Parameters:
            item: élément à rajouter.
        """

        self.length += 1
        self.items.append(item)
    
    def dequeue(self):
        """
        Retire et retourne le premier élément de la file.
        
        Raises:
            IndexError: si la file est vide
        """

        if self.length == 0:
            raise IndexError("La file est vide.")
        
        self.length -= 1
        return self.items.pop(0)

    def peek(self):
        """
        Retourne l'élément en tête de file sans le retirer.
        
        Raises:
            IndexError: si la file est vide
        """

        if self.length == 0:
            raise IndexError("La file est vide.")
    
        return self.items[0]
    
    def is_empty(self):
        """
        Vérifie si la file est vide.
        
        Returns:
            bool: True si vide, False sinon
        """

        return self.length == 0

    def size(self):
        """
        Retourne la taille de la file.
        """

        return self.length
    
    def clear(self):
        """
        Vide la file.
        """

        self.length = 0
        self.items.clear()

    def __len__(self):
        """
        Permet de faire len(queue).
        """

        return self.length

    def __str__(self):
        """
        Retourne une représentation ntextuelle de la pile.
        """

        return f"{self.items}"

if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print(f"File avant opérations :\n{q}\n")

    print(q.dequeue())  # 10
    print(q.peek())     # 20
    print(q.dequeue())  # 20
    print(q.is_empty()) # False

    print()
    print(f"File après opérations :\n{q}\n")
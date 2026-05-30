"""
Data Structure : Stack (LIFO)
"""

class Stack:
    """
    Représente une pile (Stack) utilisant le principe LIFO
    (Last In First Out).
    
    Le dernier élément ajouté est le premier retiré.
    """

    def __init__(self):
        """
        Initialise une pile vide.
        """

        self.items = []
        self.length = 0
    
    def push(self, item):
        """
        Ajoute un élément au sommet de la pile.

        Parameters:
            item: élément à ajouter.
        """
        
        self.length += 1
        self.items.append(item)

    def pop(self):
        """
        Retire et retourne l'élément au sommet de la pile.

        Raises:
            IndexError: si la pile est vide
        """

        if self.length == 0:
            raise IndexError("La pile est vide.")

        self.length -= 1
        return self.items.pop()

    def peek(self):
        """
        Retourne l'élément au sommet sans le retirer.

        Raises:
            IndexError: si la pile est vide
        """

        if self.length == 0:
            raise IndexError("La pile est vide.")
        
        return self.items[self.length - 1]

    def is_empty(self):
        """
        Vérifie si la pile est vide.
        
        Returns:
            bool: True si vide, False sinon
        """

        return self.length == 0

    def size(self):
        """
        Retourne la taille de la pile.
        """

        return self.length
    
    def clear(self):
        """
        Vide la pile.
        """

        self.length = 0
        self.items.clear()

    def __len__(self):
        """
        Permet de faire len(stack).
        """

        return self.length
    
    def __str__(self):
        """
        Retourne une représentation textuelle de la pile.
        """
        
        return f"{self.items}"

if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)

    print(f"Pile avant opérations :\n{s}\n")

    print(s.pop())      # 30
    print(s.peek())     # 20
    print(s.pop())      # 20
    print(s.is_empty()) # False

    print()
    print(f"Pile après opérations :\n{s}\n")
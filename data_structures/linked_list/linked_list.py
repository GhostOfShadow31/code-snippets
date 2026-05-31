from node import Node

class LinkedList:
    """
    A data structure called LinkedList, composed of nodes.
    """

    def __init__(self) -> None:
        """
        Initialize a linked list.
        """

        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, item: any) -> None:
        """
        Add a node at the tail of the linked list.
        
        Args:
            item: item to add
        """

        element = Node(item)

        if self.head is None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            self.tail = element
        
        self.length += 1
    
    def prepend(self, item: any) -> None:
        """
        Add a node at the head of the linked list.
        
        Args:
            item: item to add
        """

        element = Node(item)

        if self.head is None:
            self.head = element
            self.tail = element
        else:
            element.next = self.head
            self.head = element
        
        self.length += 1

    def insert(self, index: int, item: any) -> None:
        """
        Insert an item at a given index in the linked list.
        
        Args:
            index: given index
            item: item to add
        
        Raises:
            IndexError: if invalid index
        """

        # Convert into an absolute index to account for positive and negative indices
        absolute_index = index if index >= 0 else self.length + index

        if absolute_index > self.length:
            raise IndexError("Index out of range.")
        
        # Use of dedicated functions for special cases
        if absolute_index == 0:
            self.prepend(item)
            return
        
        if absolute_index == self.length:
            self.append(item)
            return

        # Find the position and insert the item
        element = Node(item)
        iterator = self.head
        compteur = 0

        while compteur < absolute_index - 1:
            iterator = iterator.next
            compteur += 1
        
        element.next = iterator.next
        iterator.next = element
        
        self.length += 1
    
    def remove(self, item: any) -> None:
        """
        Remove a node from the linked list.
        
        Args:
            item: item to remove
        """

        if self.length == 0:
            return

        # Special case: remove the head
        if self.head.value == item:
            self.head = self.head.next
            self.length -= 1

            if self.head is None:
                self.tail = None
            
            return
    
        # Nominal case
        prev = self.head
        current = self.head.next

        while current is not None:
            if current.value == item:
                prev.next = current.next

                # Update tail if needed
                if current == self.tail:
                    self.tail = prev
                
                self.length -= 1
                return
            
            prev = current
            current = current.next

    def pop(self, index: int =-1) -> any:
        """
        Remove and return the node at a given index.
        
        Args:
            index: given index
        
        Raises:
            IndexError: if invalid index
        """
        # Convert into an absolute index to account for positive and negative indices
        absolute_index = index if index >= 0 else self.length + index

        if absolute_index < 0 or absolute_index >= self.length:
            raise IndexError("Index out of range.")

        # Special case: remove the head
        if absolute_index == 0:
            value = self.head.value
            self.head = self.head.next

            if self.head is None:
                self.tail = None
            
            self.length -= 1
            return value
        
        # Nominal case
        prev = self.head
        
        for _ in range(absolute_index - 1):
            prev = prev.next
        
        current = prev.next
        value = current.value
        
        prev.next = current.next

        # Update tail if needed
        if current == self.tail:
            self.tail = prev
        
        self.length -= 1
        return value

    def find(self, item: any) -> Node | None:
        """
        Find and return a node in the linked list.
        
        Args:
            item: item to find
        
        Return:
            Node: the item in the linked list
            None: if the item is not present in the linked list
        """
        iterator = self.head

        while iterator is not None:
            if iterator.value == item:
                return iterator
            
            iterator = iterator.next
        
        return None
    
    def contains(self, item: any) -> bool:
        """
        Check if a given item is in the linked list.

        Args:
            item: given item
        
        Return:
            bool: True if content, False otherwise
        """
        return self.find(item) is not None

    
    def is_empty(self) -> bool:
        """
        Check if the linked list is empty.

        Return:
            bool: True si empty, False otherwise
        """

        return self.length == 0

    def clear(self) -> None:
        """
        Empty the linked list.
        """

        self.head = None
        self.tail = None
        self.length = 0
    
    def size(self) -> int:
        """
        Return the length of the linked list.

        Return:
            int: the lengthh of the linked list
        """

        return self.length
    
    def __len__(self) -> int:
        """
        Allow to do len(linkedList).

        Return:
            int: the length of the linked list.
        """

        return self.length
    
    def __str__(self) -> str:
        """
        Return a textual representation of the linked list.

        Return:
            str: the textual representation of the linked list
        """

        return f"({self.head}, {self.tail})"
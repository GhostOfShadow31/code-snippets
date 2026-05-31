class Stack:
    """
    A data structure called Stack based on the LIFO principle
    (Last In First Out).
    
    The last item is the first one to come out.
    """

    def __init__(self) -> None:
        """
        Initialize an empy stack.
        """

        self.items = []
        self.length = 0
    
    def push(self, item: any) -> None:
        """
        Add an item at the top of the stack.

        Args:
            item: item to add
        """
        
        self.length += 1
        self.items.append(item)

    def pop(self) -> any:
        """
        Remove and return the item at the top of the stack.

        Raises:
            IndexError: if stack is empty

        Return:
            any: the item at the top of the stack
        """

        if self.length == 0:
            raise IndexError("Empty stack.")

        self.length -= 1
        return self.items.pop()

    def peek(self) -> any:
        """
        Return the item at the top of the stack.

        Raises:
            IndexError: if stack is empty
        
        Return:
            any: item at the top of the stack
        """

        if self.length == 0:
            raise IndexError("Empty stack.")
        
        return self.items[self.length - 1]

    def is_empty(self) -> bool:
        """
        Check is the stack is empty.
        
        Returns:
            bool: True if empty, False otherwise
        """

        return self.length == 0

    def size(self) -> int:
        """
        Return the length of the stack.

        Return:
            int: the length of the stack
        """

        return self.length
    
    def clear(self) -> None:
        """
        Empty the stack.
        """

        self.length = 0
        self.items.clear()

    def __len__(self) -> int:
        """
        Allow to do len(stack).

        Return:
            int: the length of the stack
        """

        return self.length
    
    def __str__(self) -> str:
        """
        Return a textual representation of the stack.

        Return:
            str: the textual representation of the stack
        """
        
        return f"{self.items}"
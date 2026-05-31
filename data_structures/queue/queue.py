class Queue:
    """
    A data structure called Queue based on the FIFO principle
    (First In First Out).
    
    The first item is the first to come out.
    """

    def __init__(self) -> None:
        """
        Initialize an empty queue.
        """

        self.items = []
        self.length = 0
    
    def enqueue(self, item: any) -> None:
        """
        Add an item at the end of the queue.
        
        Args:
            item: item to add
        """

        self.length += 1
        self.items.append(item)
    
    def dequeue(self) -> any:
        """
        Remove and return the first item is the queue.
        
        Raises:
            IndexError: if queue is empty
        
        Return:
            any: the first item in the queue
        """

        if self.length == 0:
            raise IndexError("Empty queue.")
        
        self.length -= 1
        return self.items.pop(0)

    def peek(self) -> any:
        """
        Return the first item of the queue.
        
        Raises:
            IndexError: if queue is empty
        
        Return:
            any: the first item in the queue
        """

        if self.length == 0:
            raise IndexError("Empty queue.")
    
        return self.items[0]
    
    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        
        Return:
            bool: True if empty, False otherwise
        """

        return self.length == 0

    def size(self) -> int:
        """
        Return the length of the queue.

        Return:
            int: the length of the queue
        """

        return self.length
    
    def clear(self) -> None:
        """
        Empty the queue.
        """

        self.length = 0
        self.items.clear()

    def __len__(self) -> int:
        """
        Allow to do len(queue).

        Return:
            int: the length of the queue
        """

        return self.length

    def __str__(self):
        """
        Return a textual representation of the queue.

        Return:
            str: the textual representation of the queue
        """

        return f"{self.items}"
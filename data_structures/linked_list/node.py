class Node:
    """
    A data structure called Node, represents an element of a LinkedList
    """

    def __init__(self, value: any) -> None:
        """
        Initialize a node.
        """

        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        """
        Return a textual representation of the node.

        Reeturn:
            str: the textual representation of the node
        """

        return f"{self.value}"
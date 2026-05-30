import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    """
    Tests de l'implémentation de la pile (Stack)
    """

    def test_new_stack_is_empty(self):
        stack = Stack()

        self.assertTrue(stack.is_empty())

    def test_push_add_element(self):
        stack = Stack()
        stack.push(1)

        self.assertEqual(stack.peek(), 1)

    def test_push_keep_order(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.peek(), 3)

    def test_pop_remove_element(self):
        stack = Stack()
        stack.push(1)
        element = stack.pop()

        self.assertEqual(element, 1)

    def test_pop_keep_order(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.pop()
        
        self.assertEqual(stack.peek(), 1)

    def test_pop_raise_error(self):
        stack = Stack()
        
        self.assertRaises(IndexError, stack.pop)

    def test_peek_return_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        
        self.assertEqual(stack.peek(), 2)

    def test_peek_raise_error(self):
        stack = Stack()
        
        self.assertRaises(IndexError, stack.peek)

    def test_is_empty(self):
        stack = Stack()
        stack.push(1)
        stack.pop()

        self.assertTrue(stack.is_empty())

    def test_is_not_empty(self):
        stack = Stack()
        stack.push(1)

        self.assertFalse(stack.is_empty())
    
    def test_size(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)

        self.assertEqual(stack.size(), 2)
    
    def test_clear(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.clear()

        self.assertTrue(stack.is_empty())
    
    def test_len(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)

        self.assertEqual(len(stack), 2)

if __name__ == "__main__":
    unittest.main()
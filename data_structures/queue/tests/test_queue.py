import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    """
    Tests de l'implémentation de la file (Queue)
    """

    def test_new_queue_is_empty(self):
        queue = Queue()

        self.assertTrue(queue.is_empty())

    def test_enqueue_add_element(self):
        queue = Queue()
        queue.enqueue(1)

        self.assertEqual(queue.peek(), 1)

    def test_enqueue_keep_order(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)

        self.assertEqual(queue.peek(), 1)

    def test_dequeue_remove_element(self):
        queue = Queue()
        queue.enqueue(1)
        element = queue.dequeue()

        self.assertEqual(element, 1)

    def test_dequeue_keep_order(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()

        self.assertEqual(queue.peek(), 2)

    def test_dequeue_raise_error(self):
        queue = Queue()

        self.assertRaises(IndexError, queue.dequeue)

    def test_peek_return_peek(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)

        self.assertEqual(queue.peek(), 1)

    def test_peek_raise_error(self):
        queue = Queue()

        self.assertRaises(IndexError, queue.peek)

    def test_is_empty(self):
        queue = Queue()
        queue.enqueue(1)
        queue.dequeue()

        self.assertTrue(queue.is_empty())

    def test_is_not_empty(self):
        queue = Queue()
        queue.enqueue(1)

        self.assertFalse(queue.is_empty())
    
    def test_size(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)

        self.assertEqual(queue.size(), 2)
    
    def test_clear(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.clear()

        self.assertTrue(queue.is_empty())
    
    def test_len(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)

        self.assertEqual(len(queue), 2)

if __name__ == "__main__":
    unittest.main()
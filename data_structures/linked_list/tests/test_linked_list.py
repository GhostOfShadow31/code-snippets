import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    """
    Testing the linked list implementation.
    """

    def test_new_list_is_empty(self):
        l = LinkedList()

        self.assertTrue(l.is_empty())
        self.assertEqual(l.length, 0)
        self.assertEqual(l.head, None)
        self.assertEqual(l.tail, None)

    def test_append(self):
        l = LinkedList()
        l.append(1)

        self.assertEqual(l.length, 1)
        self.assertEqual(l.head, l.tail)
        self.assertEqual(l.head.value, 1)

    def test_append_preserve_order(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)

        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 3)

    def test_prepend(self):
        l = LinkedList()
        l.append(2)
        l.append(3)
        l.prepend(1)

        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 3)

    def test_insert(self):
        l = LinkedList()
        l.append(1)
        l.append(3)
        l.insert(1, 2)

        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 3)

    def test_insert_invalud_index_raises(self):
        l = LinkedList()
        
        self.assertRaises(IndexError, l.insert, 99, 1)

    def test_remove_middle_element(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.remove(2)

        self.assertEqual(l.length, 2)
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 3)

    def test_remove_head(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.remove(1)

        self.assertEqual(l.length, 2)
        self.assertEqual(l.head.value, 2)
        self.assertEqual(l.tail.value, 3)

    def test_pop(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        element = l.pop()

        self.assertEqual(l.length, 2)
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 2)
        self.assertEqual(element, 3)

    def test_pop_first_element(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        element = l.pop(0)

        self.assertEqual(l.length, 2)
        self.assertEqual(l.head.value, 2)
        self.assertEqual(l.tail.value, 3)
        self.assertEqual(element, 1)

    def test_pop_invalid_index_raises(self):
        l = LinkedList()

        self.assertRaises(IndexError, l.pop)

    def test_find_existing_element(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        element = l.find(2)
        
        self.assertEqual(element.value, 2)

    def test_find_missing_element(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        element = l.find(4)
        
        self.assertIsNone(element)

    def test_contains_existing_element(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)

        self.assertTrue(l.contains(2))

    def test_contains_missing_element(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)

        self.assertFalse(l.contains(4))

    def test_clear(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.clear()

        self.assertTrue(l.is_empty())

    def test_size(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)

        self.assertEqual(l.size(), 3)

    def test_len(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)

        self.assertEqual(len(l), 3)

if __name__ == "__main__":
    unittest.main()
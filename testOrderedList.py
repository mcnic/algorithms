import unittest
from orderedList import OrderedList


class TestOrderedList(unittest.TestCase):

    def test_clear(self):
        orderedList = OrderedList(True)
        orderedList.add(1)
        orderedList.add(2)
        orderedList.add(3)
        self.assertEqual(orderedList.len(), 3)

        orderedList.clean(True)
        self.assertEqual(orderedList.get_all(), [])
        self.assertEqual(orderedList.len(), 0)

        orderedList.add(10)
        self.assertEqual(orderedList.len(), 1)
        orderedList.clean(True)
        self.assertEqual(orderedList.len(), 0)
        orderedList.add(5)
        self.assertEqual(orderedList.len(), 1)

    def test_compare(self):
        orderedList = OrderedList(True)

        self.assertEqual(orderedList.compare(1, 2), -1)
        self.assertEqual(orderedList.compare(2, 1), 1)
        self.assertEqual(orderedList.compare(1, 1), 0)
        with self.assertRaises(TypeError):
            self.assertEqual(orderedList.compare(1, 'str'), -1)
        with self.assertRaises(TypeError):
            self.assertEqual(orderedList.compare(None, 2), -1)

    def test_add(self):
        orderedList = OrderedList(True)
        self.assertEqual(orderedList.len(), 0)

        orderedList.add(5)
        self.assertEqual(orderedList.get_all_values(), [5])
        self.assertEqual(orderedList.len(), 1)

        orderedList.add(8)
        self.assertEqual(orderedList.get_all_values(), [5, 8])
        self.assertEqual(orderedList.len(), 2)

        orderedList.add(3)
        self.assertEqual(orderedList.get_all_values(), [3, 5, 8])
        self.assertEqual(orderedList.len(), 3)

        orderedList.add(1)
        self.assertEqual(orderedList.get_all_values(), [1, 3, 5, 8])
        self.assertEqual(orderedList.len(), 4)

        orderedList.add(6)
        self.assertEqual(orderedList.get_all_values(), [1, 3, 5, 6, 8])
        self.assertEqual(orderedList.len(), 5)

    def test_add_desc(self):
        orderedList = OrderedList(False)
        self.assertEqual(orderedList.len(), 0)

        orderedList.add(5)
        self.assertEqual(orderedList.get_all_values(), [5])
        self.assertEqual(orderedList.len(), 1)

        orderedList.add(8)
        self.assertEqual(orderedList.get_all_values(), [8, 5])
        self.assertEqual(orderedList.len(), 2)

        orderedList.add(3)
        self.assertEqual(orderedList.get_all_values(), [8, 5, 3])
        self.assertEqual(orderedList.len(), 3)

        orderedList.add(1)
        self.assertEqual(orderedList.get_all_values(), [8, 5, 3, 1])
        self.assertEqual(orderedList.len(), 4)

        orderedList.add(6)
        self.assertEqual(orderedList.get_all_values(), [8, 6, 5, 3, 1])
        self.assertEqual(orderedList.len(), 5)

    def test_find(self):
        orderedList = OrderedList(True)
        orderedList.add(1)
        orderedList.add(3)
        orderedList.add(5)
        orderedList.add(7)
        orderedList.add(9)
        self.assertEqual(orderedList.get_all_values(), [1, 3, 5, 7, 9])
        self.assertEqual(orderedList.len(), 5)

        self.assertEqual(orderedList.find(4, False).value, 5)
        self.assertEqual(orderedList.find(0, False).value, 1)
        self.assertEqual(orderedList.find(10, False), None)
        with self.assertRaises(TypeError):
            self.assertEqual(orderedList.find(None, False), None)

    def test_find_strong(self):
        orderedList = OrderedList(True)
        orderedList.add(1)
        orderedList.add(3)
        orderedList.add(5)
        orderedList.add(7)
        orderedList.add(9)
        self.assertEqual(orderedList.get_all_values(), [1, 3, 5, 7, 9])

        self.assertEqual(orderedList.find(5, True).value, 5)
        self.assertEqual(orderedList.find(1, True).value, 1)
        self.assertEqual(orderedList.find(10, True), None)
        self.assertEqual(orderedList.find(None, True), None)

    def test_find_desc(self):
        orderedList = OrderedList(False)
        orderedList.add(1)
        orderedList.add(3)
        orderedList.add(5)
        orderedList.add(7)
        orderedList.add(9)
        self.assertEqual(orderedList.get_all_values(), [9, 7, 5, 3, 1])

        self.assertEqual(orderedList.find(4, False).value, 3)
        self.assertEqual(orderedList.find(0, False), None)
        self.assertEqual(orderedList.find(10, False).value, 9)
        with self.assertRaises(TypeError):
            self.assertEqual(orderedList.find(None, False), None)

    def test_delete(self):
        orderedList = OrderedList(True)
        orderedList.add(2)
        orderedList.add(4)
        orderedList.add(6)
        orderedList.add(8)
        orderedList.add(10)
        self.assertEqual(orderedList.get_all_values(), [2, 4, 6, 8, 10])
        self.assertEqual(orderedList.len(), 5)

        orderedList.delete(1, False)
        self.assertEqual(orderedList.get_all_values(), [4, 6, 8, 10])
        self.assertEqual(orderedList.len(), 4)

        orderedList.delete(9, False)
        self.assertEqual(orderedList.get_all_values(), [4, 6, 8])
        self.assertEqual(orderedList.len(), 3)

        orderedList.delete(5, False)
        self.assertEqual(orderedList.get_all_values(), [4, 8])
        self.assertEqual(orderedList.len(), 2)

        orderedList.delete(7, False)
        orderedList.delete(4, False)
        self.assertEqual(orderedList.get_all_values(), [])
        self.assertEqual(orderedList.len(), 0)

    def test_delete_strong(self):
        orderedList = OrderedList(True)
        orderedList.add(2)
        orderedList.add(4)
        orderedList.add(6)
        orderedList.add(8)
        orderedList.add(10)
        self.assertEqual(orderedList.get_all_values(), [2, 4, 6, 8, 10])
        self.assertEqual(orderedList.len(), 5)

        orderedList.delete(2, True)
        self.assertEqual(orderedList.get_all_values(), [4, 6, 8, 10])
        self.assertEqual(orderedList.len(), 4)

        orderedList.delete(10, True)
        self.assertEqual(orderedList.get_all_values(), [4, 6, 8])
        self.assertEqual(orderedList.len(), 3)

        orderedList.delete(3, True)
        self.assertEqual(orderedList.get_all_values(), [4, 6, 8])
        self.assertEqual(orderedList.len(), 3)

        orderedList.delete(4, True)
        self.assertEqual(orderedList.get_all_values(), [6, 8])
        self.assertEqual(orderedList.len(), 2)

        orderedList.delete(6, True)
        orderedList.delete(8, True)
        self.assertEqual(orderedList.get_all_values(), [])
        self.assertEqual(orderedList.len(), 0)

    def test_delete_desc(self):
        orderedList = OrderedList(False)
        orderedList.add(2)
        orderedList.add(4)
        orderedList.add(6)
        orderedList.add(8)
        orderedList.add(10)
        self.assertEqual(orderedList.get_all_values(), [10, 8, 6, 4, 2])
        self.assertEqual(orderedList.len(), 5)

        orderedList.delete(1, False)
        self.assertEqual(orderedList.get_all_values(), [10, 8, 6, 4, 2])
        self.assertEqual(orderedList.len(), 5)

        orderedList.delete(9, False)
        self.assertEqual(orderedList.get_all_values(), [10, 6, 4, 2])
        self.assertEqual(orderedList.len(), 4)

        orderedList.delete(5, False)
        self.assertEqual(orderedList.get_all_values(), [10, 6, 2])
        self.assertEqual(orderedList.len(), 3)

        while orderedList.len() > 0:
            orderedList.delete(1000000, False)
        self.assertEqual(orderedList.get_all_values(), [])
        self.assertEqual(orderedList.len(), 0)

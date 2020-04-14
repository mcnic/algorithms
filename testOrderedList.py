import unittest
from orderedList import OrderedList


class TestOrderedList(unittest.TestCase):

    def test_clean(self):
        orderedList = OrderedList(True)
        self.assertEqual(orderedList.len(), 0)
        orderedList.add(1)
        self.assertEqual(orderedList.len(), 1)
        orderedList.add(2)
        self.assertEqual(orderedList.len(), 2)
        orderedList.add(3)
        self.assertEqual(orderedList.len(), 3)

        orderedList.clean(True)
        self.assertEqual(orderedList.get_all(), [])
        self.assertEqual(orderedList.len(), 0)

        orderedList.add(10)
        orderedList.clean(True)
        self.assertEqual(orderedList.len(), 0)

        orderedList.add(5)
        self.assertEqual(orderedList.len(), 1)

    def test_clean_desc(self):
        orderedList = OrderedList(False)
        self.assertEqual(orderedList.len(), 0)
        orderedList.add(1)
        self.assertEqual(orderedList.len(), 1)
        orderedList.add(2)
        self.assertEqual(orderedList.len(), 2)
        orderedList.add(3)
        self.assertEqual(orderedList.len(), 3)

        orderedList.clean(False)
        self.assertEqual(orderedList.get_all(), [])
        self.assertEqual(orderedList.len(), 0)

        orderedList.add(10)
        orderedList.clean(False)
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

        orderedList.clean(True)
        orderedList.add(5)
        orderedList.add(3)
        self.assertEqual(orderedList.get_all_values(), [3, 5])
        self.assertEqual(orderedList.len(), 2)

        orderedList.add(1)
        self.assertEqual(orderedList.get_all_values(), [1, 3, 5])
        self.assertEqual(orderedList.len(), 3)

        orderedList.add(6)
        self.assertEqual(orderedList.get_all_values(), [1, 3, 5, 6])
        self.assertEqual(orderedList.len(), 4)

        orderedList.add(4)
        self.assertEqual(orderedList.get_all_values(), [1, 3, 4, 5, 6])
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

        orderedList.add(9)
        self.assertEqual(orderedList.get_all_values(), [9, 8, 6, 5, 3, 1])
        self.assertEqual(orderedList.len(), 6)

    def test_find(self):
        orderedList = OrderedList(True)
        orderedList.add(1)
        orderedList.add(3)
        orderedList.add(5)
        orderedList.add(7)
        orderedList.add(9)
        self.assertEqual(orderedList.get_all_values(), [1, 3, 5, 7, 9])
        self.assertEqual(orderedList.len(), 5)

        self.assertEqual(orderedList.find(5).value, 5)
        self.assertEqual(orderedList.find(1).value, 1)
        self.assertEqual(orderedList.find(10), None)
        with self.assertRaises(TypeError):
            self.assertEqual(orderedList.find(None), None)

    def test_find_desc(self):
        orderedList = OrderedList(False)
        orderedList.add(1)
        orderedList.add(3)
        orderedList.add(5)
        orderedList.add(7)
        orderedList.add(9)
        self.assertEqual(orderedList.get_all_values(), [9, 7, 5, 3, 1])
        self.assertEqual(orderedList.len(), 5)

        self.assertEqual(orderedList.find(4), None)
        self.assertEqual(orderedList.find(0), None)
        self.assertEqual(orderedList.find(9).value, 9)
        self.assertEqual(orderedList.find(1).value, 1)
        with self.assertRaises(TypeError):
            self.assertEqual(orderedList.find(None), None)

    def test_delete(self):
        orderedList = OrderedList(True)
        orderedList.add(2)
        orderedList.add(4)
        orderedList.add(6)
        orderedList.add(8)
        orderedList.add(10)
        self.assertEqual(orderedList.get_all_values(), [2, 4, 6, 8, 10])
        self.assertEqual(orderedList.len(), 5)

        orderedList.delete(2)
        self.assertEqual(orderedList.get_all_values(), [4, 6, 8, 10])
        self.assertEqual(orderedList.len(), 4)

        orderedList.delete(10)
        self.assertEqual(orderedList.get_all_values(), [4, 6, 8])
        self.assertEqual(orderedList.len(), 3)

        orderedList.delete(3)
        self.assertEqual(orderedList.get_all_values(), [4, 6, 8])
        self.assertEqual(orderedList.len(), 3)

        orderedList.delete(6)
        self.assertEqual(orderedList.get_all_values(), [4, 8])
        self.assertEqual(orderedList.len(), 2)

        orderedList.delete(8)
        self.assertEqual(orderedList.get_all_values(), [4])
        self.assertEqual(orderedList.len(), 1)

        orderedList.delete(4)
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

        orderedList.delete(1)
        self.assertEqual(orderedList.get_all_values(), [10, 8, 6, 4, 2])
        self.assertEqual(orderedList.len(), 5)

        orderedList.delete(8)
        self.assertEqual(orderedList.get_all_values(), [10, 6, 4, 2])
        self.assertEqual(orderedList.len(), 4)

        orderedList.delete(4)
        self.assertEqual(orderedList.get_all_values(), [10, 6, 2])
        self.assertEqual(orderedList.len(), 3)

        orderedList.delete(2)
        self.assertEqual(orderedList.get_all_values(), [10, 6])
        self.assertEqual(orderedList.len(), 2)

        orderedList.delete(10)
        self.assertEqual(orderedList.get_all_values(), [6])
        self.assertEqual(orderedList.len(), 1)

        orderedList.delete(6)
        self.assertEqual(orderedList.get_all_values(), [])
        self.assertEqual(orderedList.len(), 0)

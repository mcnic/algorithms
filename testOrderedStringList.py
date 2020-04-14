import unittest
from orderedList import OrderedStringList


class TestOrderedStringList(unittest.TestCase):

    def test_compare(self):
        orderedList = OrderedStringList(True)

        self.assertEqual(orderedList.compare('     asd', ' asd '), 0)
        self.assertEqual(orderedList.compare('     asd', ' asd   \t   '), -1)
        self.assertEqual(orderedList.compare('      as', 'asd'), -1)
        self.assertEqual(orderedList.compare('asdfghjkl', 'asdfghjkm'), -1)
        self.assertEqual(orderedList.compare('asdfghjkl', 'asdfghjkk'), 1)
        self.assertEqual(orderedList.compare('asd ', '     as'), 1)
        with self.assertRaises(AttributeError):
            self.assertEqual(orderedList.compare(None, 'str'), -1)

    def test_add(self):
        orderedList = OrderedStringList(True)

        orderedList.add('de')
        self.assertEqual(orderedList.get_all_values(), ['de'])

        orderedList.add('def')
        self.assertEqual(orderedList.get_all_values(), ['de', 'def'])

        orderedList.add('d')
        self.assertEqual(orderedList.get_all_values(), ['d', 'de', 'def'])

        orderedList.add('dd')
        self.assertEqual(orderedList.get_all_values(),
                         ['d', 'dd', 'de', 'def'])

        orderedList.add('deg')
        self.assertEqual(orderedList.get_all_values(),
                         ['d', 'dd', 'de', 'def', 'deg'])

    def test_add_desc(self):
        orderedList = OrderedStringList(False)

        orderedList.add('de')
        self.assertEqual(orderedList.get_all_values(), ['de'])

        orderedList.add('def')
        self.assertEqual(orderedList.get_all_values(), ['def', 'de'])

        orderedList.add('d')
        self.assertEqual(orderedList.get_all_values(), ['def', 'de', 'd'])

        orderedList.add('dd')
        self.assertEqual(orderedList.get_all_values(),
                         ['def', 'de', 'dd', 'd'])

        orderedList.add('deg')
        self.assertEqual(orderedList.get_all_values(),
                         ['deg', 'def', 'de', 'dd', 'd'])

    def test_find(self):
        orderedList = OrderedStringList(True)
        orderedList.add('de')
        orderedList.add('def')
        orderedList.add('d')
        orderedList.add('dd')
        orderedList.add('deg')
        self.assertEqual(orderedList.get_all_values(), [
                         'd', 'dd', 'de', 'def', 'deg'])

        self.assertEqual(orderedList.find('d').value, 'd')
        self.assertEqual(orderedList.find('dd').value, 'dd')
        self.assertEqual(orderedList.find('dg'), None)
        with self.assertRaises(TypeError):
            self.assertEqual(orderedList.find(None), None)

    def test_find_desc(self):
        orderedList = OrderedStringList(False)
        orderedList.add('de')
        orderedList.add('def')
        orderedList.add('d')
        orderedList.add('dd')
        orderedList.add('deg')
        self.assertEqual(orderedList.get_all_values(), [
                         'deg', 'def', 'de', 'dd', 'd'])

        self.assertEqual(orderedList.find('a'), None)
        self.assertEqual(orderedList.find('da'), None)
        self.assertEqual(orderedList.find('de').value, 'de')
        with self.assertRaises(TypeError):
            self.assertEqual(orderedList.find(None), None)

    def test_delete(self):
        orderedList = OrderedStringList(False)
        orderedList.add('de')
        orderedList.add('def')
        orderedList.add('d')
        orderedList.add('dd')
        orderedList.add('deg')
        self.assertEqual(orderedList.get_all_values(), [
                         'deg', 'def', 'de', 'dd', 'd'])

        orderedList.delete('deg')
        self.assertEqual(orderedList.get_all_values(),
                         ['def', 'de', 'dd', 'd'])

        orderedList.delete('d')
        self.assertEqual(orderedList.get_all_values(), ['def', 'de', 'dd'])

        orderedList.delete('de1')
        self.assertEqual(orderedList.get_all_values(), ['def', 'de', 'dd'])

    def test_delete_desc(self):
        orderedList = OrderedStringList(False)
        orderedList.add('de')
        orderedList.add('def')
        orderedList.add('d')
        orderedList.add('dd')
        orderedList.add('deg')
        self.assertEqual(orderedList.get_all_values(), [
                         'deg', 'def', 'de', 'dd', 'd'])
        self.assertEqual(orderedList.len(), 5)

        orderedList.delete('deg')
        self.assertEqual(orderedList.get_all_values(),
                         ['def', 'de', 'dd', 'd'])
        self.assertEqual(orderedList.len(), 4)

        orderedList.delete('d')
        self.assertEqual(orderedList.get_all_values(), ['def', 'de', 'dd'])
        self.assertEqual(orderedList.len(), 3)

        orderedList.delete('df')
        self.assertEqual(orderedList.get_all_values(), ['def', 'de', 'dd'])
        self.assertEqual(orderedList.len(), 3)

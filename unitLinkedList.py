import unittest
from linkedList import Node, LinkedList
from LinkedListAdd import *


def create_list(array_list):
    list1 = LinkedList()
    for val in array_list:
        list1.add_in_tail(Node(val))
    return list1


class TestStringMethods(unittest.TestCase):

    def test_find_none(self):
        list2 = LinkedList()

        self.assertEqual(list2.find(55), None)
        self.assertEqual(list2.find(None), None)
        self.assertEqual(list2.find_all(None), [])
        self.assertEqual(list2.find_all(55), [])
        self.assertEqual(list2.get_head(), None)
        self.assertEqual(list2.get_tail(), None)

    def test_find_1el(self):
        list2 = LinkedList()
        n1 = Node(55)
        list2.add_in_tail(n1)

        self.assertEqual(list2.find(n1.value), n1)
        self.assertEqual(list2.find_all(n1.value), [n1])

    def test_find_long(self):
        list2 = LinkedList()
        n1 = Node(55)
        n2 = Node(12)
        n3 = Node(55)
        list2.add_in_tail(n1)
        list2.add_in_tail(n2)
        list2.add_in_tail(n3)

        self.assertEqual(list2.find_all(n3.value), [n1, n3])
        self.assertEqual(list2.get_head(), n1)
        self.assertEqual(list2.get_tail(), n3)

    def test1_insert(self):
        list3 = LinkedList()
        n1 = Node(55)
        n2 = Node(12)
        n3 = Node(55)
        n4 = Node(10)
        n5 = Node(20)
        n6 = Node(22)
        n7 = Node(11)

        list3.add_in_tail(n1)
        list3.add_in_tail(n2)
        list3.add_in_tail(n3)
        self.assertEqual(list3.find(55).value, 55)
        self.assertEqual(list3.find_all(55), [n1, n3])
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_tail(), n3)

        list3.insert(n2, n4)
        self.assertEqual(list3.get_all(), [55, 12, 10, 55])
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_tail(), list3.find_all(55)[1])

        list3.insert(None, n5)
        assert(list3.get_all(), [20, 55, 12, 10, 55])
        assert(list3.get_head(), n5)
        assert(list3.get_tail(), n3)

        list3.insert(list3.get_tail(), n6)
        self.assertEqual(list3.get_all(), [20, 55, 12, 10, 55, 22])
        self.assertEqual(list3.get_head(), list3.find(20))
        self.assertEqual(list3.get_tail(), list3.find(22))

        list3 = LinkedList()
        list3.insert(None, n7)
        self.assertEqual(list3.get_all(), [n7.value])
        self.assertEqual(list3.get_head(), n7)
        self.assertEqual(list3.get_tail(), n7)

    def test_delete_head(self):
        list1 = create_list([55, 12, 43, 10, 14, 12, 55, 10, 5])

        list1.delete(55)
        self.assertEqual(list1.get_all(), [12, 43, 10, 14, 12, 55, 10, 5])
        self.assertEqual(list1.len(), 8)
        self.assertEqual(list1.get_head(), list1.find(12))
        self.assertEqual(list1.get_tail(), list1.find(5))

    def test_delete_body(self):
        list1 = create_list([12, 43, 10, 14, 12, 55, 10, 5])

        list1.delete(43)
        self.assertEqual(list1.get_all(), [12, 10, 14, 12, 55, 10, 5])
        self.assertEqual(list1.len(), 7)
        self.assertEqual(list1.get_head(), list1.find(12))
        self.assertEqual(list1.get_tail(), list1.find(5))

    def test_delete_tail(self):
        list1 = create_list([12, 10, 14, 12, 55, 10, 5])

        list1.delete(5)
        self.assertEqual(list1.get_all(), [12, 10, 14, 12, 55, 10])
        self.assertEqual(list1.get_head(), list1.find_all(12)[0])
        self.assertEqual(list1.get_tail(), list1.find_all(10)[1])

    def test_delete_wrong(self):
        list1 = create_list([12, 10, 14, 12, 55, 10])

        list1.delete(77)
        self.assertEqual(list1.get_all(), [12, 10, 14, 12, 55, 10])
        self.assertEqual(list1.get_head(), list1.find_all(12)[0])
        self.assertEqual(list1.get_tail(), list1.find_all(10)[1])

        list1.delete(None)
        self.assertEqual(list1.get_all(), [12, 10, 14, 12, 55, 10])
        self.assertEqual(list1.len(), 6)
        self.assertEqual(list1.get_head(), list1.find_all(12)[0])
        self.assertEqual(list1.get_tail(), list1.find_all(10)[1])

    def test_delete_one(self):
        list4 = LinkedList()
        n1 = Node(55)

        list4.add_in_tail(n1)
        list4.delete(55)
        self.assertEqual(list4.get_all(), [])
        self.assertEqual(list4.get_head(), None)
        self.assertEqual(list4.get_tail(), None)

    def test_clean(self):
        list1 = create_list([55, 12, 43, 10, 14, 12, 55, 10, 5])

        list1.clean()
        self.assertEqual(list1.get_all(), [])
        self.assertEqual(list1.get_head(), None)
        self.assertEqual(list1.get_tail(), None)

    def test_delete_empty(self):
        list1 = LinkedList()

        list1.delete(5)
        self.assertEqual(list1.get_all(), [])
        self.assertEqual(list1.len(), 0)
        self.assertEqual(list1.get_head(), None)
        self.assertEqual(list1.get_tail(), None)

        list1.delete(None)
        self.assertEqual(list1.get_all(), [])
        self.assertEqual(list1.len(), 0)
        self.assertEqual(list1.get_head(), None)
        self.assertEqual(list1.get_tail(), None)


if __name__ == '__main__':
    unittest.main()

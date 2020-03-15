import unittest
from linkedList2 import Node, LinkedList2
#from linkedListAdd import *


class TestLinkedList(unittest.TestCase):

    def test_find_wrong(self):
        list2 = LinkedList2()

        self.assertEqual(list2.find(55), None)
        self.assertEqual(list2.find(None), None)
        self.assertEqual(list2.get_head(), None)
        self.assertEqual(list2.get_tail(), None)

    def test_find_all_wrong(self):
        list2 = LinkedList2()

        self.assertEqual(list2.find_all(None), [])
        self.assertEqual(list2.find_all(55), [])
        self.assertEqual(list2.get_head(), None)
        self.assertEqual(list2.get_tail(), None)

    def test_find_in_1el(self):
        list2 = LinkedList2()
        n1 = Node(55)
        list2.add_in_tail(n1)

        self.assertEqual(list2.find(n1.value), n1)

    def test_find_all_in_1el(self):
        list2 = LinkedList2()
        n1 = Node(55)
        list2.add_in_tail(n1)

        self.assertEqual(list2.find_all(n1.value), [n1])

    def test_find_not_empty(self):
        list2 = LinkedList2()
        n1 = Node(55)
        n2 = Node(12)
        n3 = Node(55)
        list2.add_in_tail(n1)
        list2.add_in_tail(n2)
        list2.add_in_tail(n3)

        self.assertEqual(list2.find(n3.value), n1)
        self.assertEqual(list2.get_head(), n1)
        self.assertEqual(list2.get_tail(), n3)

    def test_find_all_not_empty(self):
        list2 = LinkedList2()
        n1 = Node(55)
        n2 = Node(12)
        n3 = Node(55)
        list2.add_in_tail(n1)
        list2.add_in_tail(n2)
        list2.add_in_tail(n3)

        self.assertEqual(list2.find_all(n3.value), [n1, n3])
        self.assertEqual(list2.get_head(), n1)
        self.assertEqual(list2.get_tail(), n3)

    def test_create(self):
        list1 = LinkedList2().create_list([12, 10, 14, 12, 55, 10, 5])

        self.assertEqual(list1.get_all(), [12, 10, 14, 12, 55, 10, 5])
        self.assertEqual(list1.get_head(), list1.find_all(12)[0])
        self.assertEqual(list1.get_tail(), list1.find(5))
        self.assertEqual(list1.get_head().prev, None)
        self.assertEqual(list1.get_tail().prev.value, 10)
        self.assertEqual(list1.get_tail().next, None)

    def test_delete_in_body(self):
        list1 = LinkedList2().create_list([12, 43, 10, 14, 12, 55, 10, 5])

        list1.delete(43)
        self.assertEqual(list1.get_all(), [12, 10, 14, 12, 55, 10, 5])
        self.assertEqual(list1.len(), 7)
        self.assertEqual(list1.get_head().prev, None)
        self.assertEqual(list1.get_tail().next, None)
        self.assertEqual(list1.get_head(), list1.find(12))
        self.assertEqual(list1.get_tail(), list1.find(5))
        self.assertEqual(list1.find(12).next.value, 10)
        self.assertEqual(list1.find(10).prev.value, 12)

    def test_delete_in_head(self):
        list1 = LinkedList2().create_list([55, 12, 43, 10, 14, 12, 55, 10, 5])

        list1.delete(55)
        self.assertEqual(list1.get_all(), [12, 43, 10, 14, 12, 55, 10, 5])
        self.assertEqual(list1.len(), 8)
        self.assertEqual(list1.get_head().prev, None)
        self.assertEqual(list1.get_tail().next, None)
        self.assertEqual(list1.get_head(), list1.find(12))
        self.assertEqual(list1.get_tail(), list1.find(5))

    def test_delete_in_tail(self):
        list1 = LinkedList2().create_list([12, 10, 14, 12, 55, 10, 5])

        list1.delete(5)
        self.assertEqual(list1.get_all(), [12, 10, 14, 12, 55, 10])
        self.assertEqual(list1.get_head().prev, None)
        self.assertEqual(list1.get_tail().next, None)
        self.assertEqual(list1.get_tail(), list1.find_all(10)[1])
        self.assertEqual(list1.get_tail().prev.value, 55)

    def test_delete_wrong(self):
        list1 = LinkedList2().create_list([12, 10, 14, 12, 55, 10])

        list1.delete(77)
        self.assertEqual(list1.get_all(), [12, 10, 14, 12, 55, 10])
        self.assertEqual(list1.len(), 6)
        self.assertEqual(list1.get_head().prev, None)
        self.assertEqual(list1.get_tail().next, None)
        self.assertEqual(list1.get_head(), list1.find_all(12)[0])
        self.assertEqual(list1.get_tail(), list1.find_all(10)[1])

        list1.delete(None)
        self.assertEqual(list1.get_all(), [12, 10, 14, 12, 55, 10])
        self.assertEqual(list1.len(), 6)
        self.assertEqual(list1.get_head().prev, None)
        self.assertEqual(list1.get_tail().next, None)
        self.assertEqual(list1.get_head(), list1.find_all(12)[0])
        self.assertEqual(list1.get_tail(), list1.find_all(10)[1])

    def test_delete_from_1el(self):
        list4 = LinkedList2()
        n1 = Node(55)
        list4.add_in_tail(n1)

        list4.delete(55)
        self.assertEqual(list4.get_all(), [])
        self.assertEqual(list4.get_head(), None)
        self.assertEqual(list4.get_tail(), None)

    def test_delete_from_empty(self):
        list1 = LinkedList2()

        list1.delete(77)
        self.assertEqual(list1.get_all(), [])
        self.assertEqual(list1.len(), 0)
        self.assertEqual(list1.get_head(), None)
        self.assertEqual(list1.get_tail(), None)

        list1.delete(None)
        self.assertEqual(list1.get_all(), [])
        self.assertEqual(list1.len(), 0)
        self.assertEqual(list1.get_head(), None)
        self.assertEqual(list1.get_tail(), None)

    def test_delete_multi_in_head_and_body(self):
        list1 = LinkedList2().create_list([12, 43,  14, 12, 5, 5])

        list1.delete(12, True)
        self.assertEqual(list1.get_all(), [43,  14, 5, 5])
        self.assertEqual(list1.len(), 4)
        self.assertEqual(list1.get_head().value, 43)
        self.assertEqual(list1.get_tail().value, 5)
        self.assertEqual(list1.get_head().prev, None)
        self.assertEqual(list1.get_tail().next, None)
        self.assertEqual(list1.get_head().next.value, 14)
        self.assertEqual(list1.find(14).next.value, 5)
        self.assertEqual(list1.find(5).prev.value, 14)

    def test_delete_multi_in_tail(self):
        list1 = LinkedList2().create_list([12, 43,  14, 12, 5, 5])

        list1.delete(5, True)
        self.assertEqual(list1.get_all(), [12, 43,  14, 12])
        self.assertEqual(list1.len(), 4)
        self.assertEqual(list1.get_head().value, 12)
        self.assertEqual(list1.find_all(12)[0].value, 12)
        self.assertEqual(list1.find_all(12)[1].value, 12)
        self.assertEqual(list1.get_tail().value, 12)
        self.assertEqual(list1.get_head().prev, None)
        self.assertEqual(list1.get_tail().next, None)

    def test_delete_multi_all_data(self):
        list1 = LinkedList2().create_list([5, 5])

        list1.delete(5, True)
        self.assertEqual(list1.get_all(), [])
        self.assertEqual(list1.len(), 0)
        self.assertEqual(list1.get_head(), None)
        self.assertEqual(list1.get_tail(), None)

    def test_delete_multi_from_1el(self):
        list1 = LinkedList2().create_list([5])

        list1.delete(5, True)
        self.assertEqual(list1.get_all(), [])
        self.assertEqual(list1.len(), 0)
        self.assertEqual(list1.get_head(), None)
        self.assertEqual(list1.get_tail(), None)

    def test_delete_multi_from_empty(self):
        list1 = LinkedList2()

        list1.delete(5, True)
        self.assertEqual(list1.get_all(), [])
        self.assertEqual(list1.len(), 0)
        self.assertEqual(list1.get_head(), None)
        self.assertEqual(list1.get_tail(), None)

        list1.delete(None, True)
        self.assertEqual(list1.get_all(), [])
        self.assertEqual(list1.len(), 0)
        self.assertEqual(list1.get_head(), None)
        self.assertEqual(list1.get_tail(), None)

    def test_delete_multi_wrong(self):
        list1 = LinkedList2().create_list([12, 10, 14, 12, 55, 10])

        list1.delete(77, True)
        self.assertEqual(list1.get_all(), [12, 10, 14, 12, 55, 10])
        self.assertEqual(list1.get_head(), list1.find_all(12)[0])
        self.assertEqual(list1.get_tail(), list1.find_all(10)[1])

        list1.delete(None, True)
        self.assertEqual(list1.get_all(), [12, 10, 14, 12, 55, 10])
        self.assertEqual(list1.len(), 6)
        self.assertEqual(list1.get_head(), list1.find_all(12)[0])
        self.assertEqual(list1.get_tail(), list1.find_all(10)[1])

    def test_add_in_tail_in_clear(self):
        list3 = LinkedList2()
        n1 = Node(55)

        list3.add_in_tail(None)
        self.assertEqual(list3.get_all(), [])
        self.assertEqual(list3.get_head(), None)
        self.assertEqual(list3.get_tail(), None)

        list3.add_in_tail(n1)
        self.assertEqual(list3.get_all(), [55])
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_tail(), n1)
        self.assertEqual(n1.prev, None)
        self.assertEqual(n1.next, None)

        list3.add_in_tail(None)
        self.assertEqual(list3.get_all(), [55])
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_tail(), n1)
        self.assertEqual(n1.prev, None)
        self.assertEqual(n1.next, None)

    def test_add_in_tail_1el(self):
        list3 = LinkedList2()
        n1 = Node(55)
        n2 = Node(12)
        list3.add_in_tail(n1)

        list3.add_in_tail(n2)
        self.assertEqual(list3.get_all(), [n1.value, n2.value])
        self.assertEqual(list3.get_head().prev, None)
        self.assertEqual(list3.get_tail().next, None)
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_tail(), n2)
        self.assertEqual(n1.next, n2)
        self.assertEqual(n2.prev, n1)

    def test_add_in_tail(self):
        list3 = LinkedList2()
        n1 = Node(55)
        n2 = Node(12)
        n3 = Node(55)
        list3.add_in_tail(n1)

        list3.add_in_tail(n2)
        self.assertEqual(list3.get_all(), [n1.value, n2.value])
        self.assertEqual(list3.get_head().prev, None)
        self.assertEqual(list3.get_tail().next, None)
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_tail(), n2)
        self.assertEqual(n1.next, n2)
        self.assertEqual(n2.prev, n1)

        list3.add_in_tail(n3)
        self.assertEqual(list3.get_all(), [55, 12, 55])
        self.assertEqual(list3.get_head().prev, None)
        self.assertEqual(list3.get_tail().next, None)
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_tail(), n3)
        self.assertEqual(n1.next, n2)
        self.assertEqual(n2.prev, n1)
        self.assertEqual(n3.prev, n2)
        self.assertEqual(n2.next, n3)

        list3.add_in_tail(None)
        self.assertEqual(list3.get_all(), [55, 12, 55])
        self.assertEqual(list3.find(55), n1)
        self.assertEqual(list3.find_all(55), [n1, n3])
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_tail(), n3)
        self.assertEqual(n1.prev, None)
        self.assertEqual(n3.next, None)
        self.assertEqual(n1.next, n2)
        self.assertEqual(n3.prev, n2)
        self.assertEqual(n2.next, n3)

    def test_insert_to_empty(self):
        list3 = LinkedList2()
        n7 = Node(11)

        list3.insert(None, None)
        self.assertEqual(list3.get_all(), [])
        self.assertEqual(list3.get_head(), None)
        self.assertEqual(list3.get_tail(), None)

        list3.insert(None, n7)
        self.assertEqual(list3.get_all(), [n7.value])
        self.assertEqual(list3.get_head().prev, None)
        self.assertEqual(list3.get_tail().next, None)
        self.assertEqual(list3.get_head(), n7)
        self.assertEqual(list3.get_tail(), n7)

        list3.insert(None, None)
        self.assertEqual(list3.get_all(), [n7.value])
        self.assertEqual(list3.get_head().prev, None)
        self.assertEqual(list3.get_tail().next, None)
        self.assertEqual(list3.get_head(), n7)
        self.assertEqual(list3.get_tail(), n7)

    def test_insert_to_body(self):
        list3 = LinkedList2()
        n1 = Node(55)
        n2 = Node(12)
        n3 = Node(55)
        n4 = Node(10)
        list3.add_in_tail(n1)
        list3.add_in_tail(n2)
        list3.add_in_tail(n3)

        list3.insert(n2, n4)
        self.assertEqual(list3.get_all(), [
                         n1.value, n2.value, n4.value, n3.value])
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_tail(), list3.find_all(
            n3.value)[len(list3.find_all(n3.value))-1])
        self.assertEqual(list3.get_head().prev, None)
        self.assertEqual(list3.get_tail().next, None)
        self.assertEqual(n2.next, n4)
        self.assertEqual(n3.prev, n4)
        self.assertEqual(n4.next, n3)
        self.assertEqual(n4.prev, n2)

    # not success: if afterNode=None, element add in tail list
    def _test_insert_in_head_not_success(self):
        list3 = LinkedList2()
        n1 = Node(55)
        n2 = Node(12)
        n3 = Node(55)
        n4 = Node(10)
        n5 = Node(20)
        list3.add_in_tail(n1)
        list3.add_in_tail(n2)
        list3.add_in_tail(n3)
        list3.add_in_tail(n4)

        list3.insert(None, n5)
        self.assertEqual(list3.get_all(), [
                         n5.value, n1.value, n2.value, n3.value, n4.value])
        self.assertEqual(list3.get_head().prev, None)
        self.assertEqual(list3.get_tail().next, None)
        self.assertEqual(list3.get_head(), n5)
        self.assertEqual(list3.get_tail(), n4)
        self.assertEqual(n5.next, n1)
        self.assertEqual(n1.prev, n5)

    def test_insert_in_tail_1el(self):
        list3 = LinkedList2()
        n1 = Node(20)
        n2 = Node(55)
        list3.add_in_tail(n1)

        #list3.insert(list3.get_tail(), n2)
        list3.insert(None, n2)
        self.assertEqual(list3.get_all(), [n1.value, n2.value])
        self.assertEqual(list3.get_head().prev, None)
        self.assertEqual(list3.get_tail().next, None)
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_tail(), n2)
        self.assertEqual(n2.prev, n1)
        self.assertEqual(n1.next, n2)

    def test_insert_in_tail(self):
        list3 = LinkedList2()
        n1 = Node(20)
        n2 = Node(55)
        n3 = Node(12)
        n4 = Node(10)
        n5 = Node(55)
        n6 = Node(22)
        list3.add_in_tail(n1)
        list3.add_in_tail(n2)

        #list3.insert(list3.get_tail(), n3)
        list3.insert(None, n3)
        self.assertEqual(list3.get_all(), [n1.value, n2.value, n3.value])
        self.assertEqual(list3.get_head().prev, None)
        self.assertEqual(list3.get_tail().next, None)
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_tail(), n3)
        self.assertEqual(n3.prev, n2)
        self.assertEqual(n2.next, n3)

        list3.add_in_tail(n4)
        list3.add_in_tail(n5)
        self.assertEqual(list3.get_all(), [20, 55, 12, 10, 55])

        #list3.insert(list3.get_tail(), n6)
        list3.insert(None, n6)
        self.assertEqual(list3.get_all(), [20, 55, 12, 10, 55, 22])
        self.assertEqual(list3.get_head().prev, None)
        self.assertEqual(list3.get_tail().next, None)
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_tail(), n6)
        self.assertEqual(n6.prev, n5)
        self.assertEqual(n5.next, n6)
        self.assertEqual(n2.prev, n1)
        self.assertEqual(n1.next, n2)
        self.assertEqual(n3.prev, n2)
        self.assertEqual(n2.next, n3)
        self.assertEqual(n4.prev, n3)
        self.assertEqual(n3.next, n4)
        self.assertEqual(n5.prev, n4)
        self.assertEqual(n4.next, n5)

        list3.insert(list3.get_tail(), None)
        self.assertEqual(list3.get_all(), [20, 55, 12, 10, 55, 22])

    def test_add_in_head_in_clear(self):
        list3 = LinkedList2()
        n1 = Node(55)

        list3.add_in_head(None)
        self.assertEqual(list3.get_all(), [])
        self.assertEqual(list3.get_head(), None)
        self.assertEqual(list3.get_tail(), None)

        list3.add_in_head(n1)
        self.assertEqual(list3.get_all(), [55])
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_tail(), n1)
        self.assertEqual(n1.prev, None)
        self.assertEqual(n1.next, None)

    def test_add_in_head_in_1el(self):
        list3 = LinkedList2()
        n1 = Node(55)
        n4 = Node(10)
        list3.add_in_tail(n1)

        list3.add_in_head(None)
        self.assertEqual(list3.get_all(), [55])
        self.assertEqual(list3.get_head(), n1)
        self.assertEqual(list3.get_head().prev, None)
        self.assertEqual(list3.get_tail().next, None)
        self.assertEqual(list3.get_head().next, None)
        self.assertEqual(list3.get_tail().prev, None)

        list3.add_in_head(n4)
        self.assertEqual(list3.get_all(), [10, 55])
        self.assertEqual(list3.get_head().prev, None)
        self.assertEqual(list3.get_tail().next, None)
        self.assertEqual(list3.get_head(), n4)
        self.assertEqual(list3.get_tail(), n1)
        self.assertEqual(n4.next, n1)
        self.assertEqual(n1.prev, n4)

    def test_add_in_head(self):
        list3 = LinkedList2()
        n1 = Node(55)
        n2 = Node(12)
        n3 = Node(55)
        n4 = Node(10)
        n5 = Node(20)
        list3.add_in_tail(n1)
        list3.add_in_tail(n2)
        list3.add_in_tail(n3)

        list3.add_in_head(n4)
        self.assertEqual(list3.get_all(), [10, 55, 12, 55])
        self.assertEqual(list3.get_head().prev, None)
        self.assertEqual(list3.get_tail().next, None)
        self.assertEqual(list3.get_head(), n4)
        self.assertEqual(n4.next, n1)
        self.assertEqual(n1.prev, n4)

        list3.add_in_head(n5)
        self.assertEqual(list3.get_all(), [20, 10, 55, 12, 55])
        self.assertEqual(list3.get_head(), n5)
        self.assertEqual(n5.next, n4)
        self.assertEqual(n4.prev, n5)

        list3.add_in_head(None)
        self.assertEqual(list3.get_all(), [20, 10, 55, 12, 55])
        self.assertEqual(list3.get_head(), n5)
        self.assertEqual(n5.next, n4)
        self.assertEqual(n4.prev, n5)

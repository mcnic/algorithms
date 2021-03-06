import unittest
from deque2 import Deque


class TestDedeque(unittest.TestCase):

    def test_clear(self):
        deque = Deque()

        self.assertEqual(deque.size(), 0)
        with self.assertRaises(IndexError):
            deque.removeFront()
        self.assertEqual(deque.get_all(), [])
        self.assertEqual(deque.size(), 0)
        with self.assertRaises(IndexError):
            deque.removeTail()
        self.assertEqual(deque.get_all(), [])
        self.assertEqual(deque.size(), 0)

    def test_addFront(self):
        deque = Deque()

        deque.addFront(None)
        self.assertEqual(deque.get_all(), [None])
        self.assertEqual(deque.size(), 1)

        res = deque.removeFront()
        self.assertEqual(deque.get_all(), [])
        self.assertEqual(res, None)
        self.assertEqual(deque.size(), 0)

        deque.addFront(11)
        self.assertEqual(deque.get_all(), [11])
        self.assertEqual(deque.size(), 1)

        deque.addFront(22)
        self.assertEqual(deque.get_all(), [22, 11])
        self.assertEqual(deque.size(), 2)

    def test_addTail(self):
        deque = Deque()

        deque.addTail(None)
        self.assertEqual(deque.get_all(), [None])
        self.assertEqual(deque.size(), 1)

        res = deque.removeTail()
        self.assertEqual(deque.get_all(), [])
        self.assertEqual(res, None)
        self.assertEqual(deque.size(), 0)

        deque.addTail(11)
        self.assertEqual(deque.get_all(), [11])
        self.assertEqual(deque.size(), 1)

        deque.addTail(22)
        self.assertEqual(deque.get_all(), [11, 22])
        self.assertEqual(deque.size(), 2)

    def test_removeFront(self):
        deque = Deque()
        deque.addTail(11)
        deque.addTail(22)
        self.assertEqual(deque.get_all(), [11, 22])
        self.assertEqual(deque.size(), 2)

        res = deque.removeFront()
        self.assertEqual(deque.get_all(), [22])
        self.assertEqual(res, 11)
        self.assertEqual(deque.size(), 1)

        res = deque.removeFront()
        self.assertEqual(deque.get_all(), [])
        self.assertEqual(res, 22)

        with self.assertRaises(IndexError):
            res = deque.removeFront()

    def test_removeTail(self):
        deque = Deque()
        deque.addTail(11)
        deque.addTail(22)
        self.assertEqual(deque.get_all(), [11, 22])
        self.assertEqual(deque.size(), 2)

        res = deque.removeTail()
        self.assertEqual(deque.get_all(), [11])
        self.assertEqual(res, 22)
        self.assertEqual(deque.size(), 1)

        res = deque.removeTail()
        self.assertEqual(deque.get_all(), [])
        self.assertEqual(res, 11)

        with self.assertRaises(IndexError):
            res = deque.removeTail()

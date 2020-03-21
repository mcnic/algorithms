import unittest
from stack import Stack


class TestLinkedList(unittest.TestCase):

    def test_clear(self):
        stack = Stack()

        self.assertEqual(stack.size(), 0)
        # with self.assertRaises(IndexError):
        #    stack.peek()
        self.assertEqual(stack.peek(), None)
        # with self.assertRaises(IndexError):
        #    stack.pop()
        self.assertEqual(stack.pop(), None)

    def test_push_peek(self):
        stack = Stack()

        stack.push(11)
        self.assertEqual(stack.get_all(), [11])
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 11)

        stack.push(22)
        self.assertEqual(stack.get_all(), [11, 22])
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 22)

    def test_pop(self):
        stack = Stack()
        stack.push(11)
        stack.push(22)
        self.assertEqual(stack.get_all(), [11, 22])

        res = stack.pop()
        self.assertEqual(stack.get_all(), [11])
        self.assertEqual(res, 22)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 11)

        res = stack.pop()
        self.assertEqual(stack.get_all(), [])
        self.assertEqual(res, 11)
        self.assertEqual(stack.size(), 0)

    def test_clear_head(self):
        stack = Stack(True)

        self.assertEqual(stack.size(), 0)
        # with self.assertRaises(IndexError):
        #    stack.peek()
        self.assertEqual(stack.peek(), None)
        # with self.assertRaises(IndexError):
        #    stack.pop()
        self.assertEqual(stack.pop(), None)

    def test_push_peek_head(self):
        stack = Stack(True)

        stack.push(11)
        self.assertEqual(stack.get_all(), [11])
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 11)

        stack.push(22)
        self.assertEqual(stack.get_all(), [22, 11])
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 22)

    def test_pop_head(self):
        stack = Stack(True)
        stack.push(11)
        stack.push(22)
        stack.push(33)
        self.assertEqual(stack.get_all(), [33, 22, 11])

        res = stack.pop()
        self.assertEqual(stack.get_all(), [22, 11])
        self.assertEqual(res, 33)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 22)

        res = stack.pop()
        self.assertEqual(stack.get_all(), [11])
        self.assertEqual(res, 22)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 11)

        res = stack.pop()
        self.assertEqual(stack.get_all(), [])
        self.assertEqual(res, 11)
        self.assertEqual(stack.size(), 0)

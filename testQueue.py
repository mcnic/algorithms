import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_clear(self):
        queue = Queue()

        self.assertEqual(queue.size(), 0)
        self.assertEqual(queue.dequeue(), None)

    def test_enqueue(self):
        queue = Queue()

        queue.enqueue(11)
        self.assertEqual(queue.get_all(), [11])
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.peek(), 11)

        queue.enqueue(22)
        self.assertEqual(queue.get_all(), [11, 22])
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.peek(), 11)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(11)
        queue.enqueue(22)
        self.assertEqual(queue.get_all(), [11, 22])

        res = queue.dequeue()
        self.assertEqual(queue.get_all(), [22])
        self.assertEqual(res, 11)
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.peek(), 22)

        res = queue.dequeue()
        self.assertEqual(queue.get_all(), [])
        self.assertEqual(res, 22)
        self.assertEqual(queue.size(), 0)

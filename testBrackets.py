import unittest
from bracketsTester import *


class TestBracketsTester(unittest.TestCase):

    def test_brackets(self):
        self.assertEqual(brackets_tester('(()((()))())'), True)
        self.assertEqual(brackets_tester('(()((((((()))'), False)
        self.assertEqual(brackets_tester('(()((())()))'), True)
        self.assertEqual(brackets_tester('(()()(()'), False)
        self.assertEqual(brackets_tester('())('), False)
        self.assertEqual(brackets_tester('))(('), False)
        self.assertEqual(brackets_tester('((())'), False)

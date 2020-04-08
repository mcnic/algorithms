import unittest
from polyndrome import Polyndrome


class TestPolyndrome(unittest.TestCase):

    def test_polyndrome(self):
        polyndrome = Polyndrome()

        self.assertEqual(polyndrome.check('asdfdsa'),  True)
        self.assertEqual(polyndrome.check('adfdsa'),  False)
        self.assertEqual(polyndrome.check('adfdsab'),  False)
        self.assertEqual(polyndrome.check('aa'),  True)
        self.assertEqual(polyndrome.check('a'),  True)
        self.assertEqual(polyndrome.check('aba'),  True)
        self.assertEqual(polyndrome.check('abas'),  False)
        self.assertEqual(polyndrome.check(''),  True)

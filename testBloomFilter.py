import unittest
from bloomFilter import BloomFilter


class TestNativeDictionary(unittest.TestCase):

    def test_hash1(self):
        bf = BloomFilter(10)

        self.assertEqual(bf.hash1('0123456789'), 7)
        self.assertEqual(bf.hash1('1234567890'), 5)
        self.assertEqual(bf.hash1('2345678901'), 3)
        self.assertEqual(bf.hash1('3456789012'), 1)
        self.assertEqual(bf.hash1('4567890123'), 9)
        self.assertEqual(bf.hash1('5678901234'), 7)
        self.assertEqual(bf.hash1('6789012345'), 5)
        self.assertEqual(bf.hash1('7890123456'), 3)
        self.assertEqual(bf.hash1('8901234567'), 1)
        self.assertEqual(bf.hash1('9012345678'), 9)

    def test_hash2(self):
        bf = BloomFilter(10)

        self.assertEqual(bf.hash2('0123456789'), 9)
        self.assertEqual(bf.hash2('1234567890'), 3)
        self.assertEqual(bf.hash2('2345678901'), 7)
        self.assertEqual(bf.hash2('3456789012'), 1)
        self.assertEqual(bf.hash2('4567890123'), 5)
        self.assertEqual(bf.hash2('5678901234'), 9)
        self.assertEqual(bf.hash2('6789012345'), 3)
        self.assertEqual(bf.hash2('7890123456'), 7)
        self.assertEqual(bf.hash2('8901234567'), 1)
        self.assertEqual(bf.hash2('9012345678'), 5)

    def test_add(self):
        bf = BloomFilter(10)

        bf.add('0123456789')  # 1
        bf.add('1234567890')  # 1
        bf.add('2345678901')  # 3
        bf.add('3456789012')  # 1
        bf.add('4567890123')  # 1
        bf.add('5678901234')  # 1
        bf.add('6789012345')  # 1
        bf.add('7890123456')  # 3
        bf.add('8901234567')  # 1
        bf.add('9012345678')  # 1

    def test_is_value(self):
        bf = BloomFilter(10)
        bf.add('0123456789')  # 1
        bf.add('1234567890')  # 1
        bf.add('2345678901')  # 3
        bf.add('3456789012')  # 1
        bf.add('4567890123')  # 1
        bf.add('5678901234')  # 1
        bf.add('6789012345')  # 1
        bf.add('7890123456')  # 3
        bf.add('8901234567')  # 1
        bf.add('9012345678')  # 1

        self.assertEqual(bf.is_value('0123456789'), True)
        self.assertEqual(bf.is_value('1234567890'), True)
        self.assertEqual(bf.is_value('2345678901'), True)
        self.assertEqual(bf.is_value('3456789012'), True)
        self.assertEqual(bf.is_value('4567890123'), True)
        self.assertEqual(bf.is_value('5678901234'), True)
        self.assertEqual(bf.is_value('6789012345'), True)
        self.assertEqual(bf.is_value('7890123456'), True)
        self.assertEqual(bf.is_value('8901234567'), True)
        self.assertEqual(bf.is_value('9012345678'), True)

        self.assertEqual(bf.is_value(
            '42347hbtr556byftynrtnyt'), False)  # 9, None

        self.assertEqual(bf.is_value('32423'), False)  # 0, None

        bf.add('32423')  # 0
        self.assertEqual(bf.is_value('32423'), True)  # 0

        self.assertEqual(bf.is_value('345435214'), True)  # 1 - Wrong result ;)

import unittest
from hashTable import HashTable


class TestHashTable(unittest.TestCase):

    def test_hash_fun(self):
        hashTable = HashTable(19, 3)

        self.assertEqual(hashTable.hash_fun('fsdfhxvn980cvnxcbfvjksd'), 8)
        self.assertEqual(hashTable.hash_fun('fsdfhxvnxmcvnxcbfvjksd'), 9)
        self.assertEqual(hashTable.hash_fun('yery54n77ji'), 8)
        self.assertEqual(hashTable.hash_fun('ert43564645'), 5)
        self.assertEqual(hashTable.hash_fun('rtbktut'), 16)
        self.assertEqual(hashTable.hash_fun('ывспмкенкнк'), 11)
        self.assertEqual(hashTable.hash_fun('fsdfhxvnxmcv08905xcbfvjksd'), 8)
        self.assertEqual(hashTable.hash_fun('вкс3еме45н5  564  '), 18)
        self.assertEqual(hashTable.hash_fun('fsdfhxыапукetxmcvnxcbfvjksd'), 6)
        self.assertEqual(hashTable.hash_fun('fsdfhxvnxmcvnxc5435sd'), 13)
        self.assertEqual(hashTable.hash_fun('fsdfhxvnxm5443nxcbfvjksd'), 13)

    def _test_seek_slot(self):
        hashTable = HashTable(19, 3)

        self.assertEqual(hashTable.seek_slot('fsdfhxvn980cvnxcbfvjksd'), 8)
        self.assertEqual(hashTable.seek_slot('fsdfhxvnxmcvnxcbfvjksd'), 9)
        self.assertEqual(hashTable.seek_slot('yery54n77ji'), 8)
        self.assertEqual(hashTable.seek_slot('ert43564645'), 5)
        self.assertEqual(hashTable.seek_slot('rtbktut'), 16)
        self.assertEqual(hashTable.seek_slot('ывспмкенкнк'), 11)
        self.assertEqual(hashTable.seek_slot('fsdfhxvnxmcv08905xcbfvjksd'), 8)
        self.assertEqual(hashTable.seek_slot('вкс3еме45н5  564  '), 18)
        self.assertEqual(hashTable.seek_slot('fsdfhxыапукetxmcvnxcbfvjksd'), 6)
        self.assertEqual(hashTable.seek_slot('fsdfhxvnxmcvnxc5435sd'), 13)
        self.assertEqual(hashTable.seek_slot('fsdfhxvnxm5443nxcbfvjksd'), 13)

    def test_put(self):
        hashTable = HashTable(19, 3)
        # print('test_put')

        self.assertEqual(hashTable.put('fsdfhxvn980cvnxcbfvjksd'), 8)
        self.assertEqual(hashTable.put('fsdfhxvnxmcvnxcbfvjksd'), 9)
        self.assertEqual(hashTable.put('yery54n77ji'), 11)
        self.assertEqual(hashTable.put('ert43564645'), 5)
        self.assertEqual(hashTable.put('rtbktut'), 16)
        self.assertEqual(hashTable.put('ывспмкенкнк'), 14)
        self.assertEqual(hashTable.put('fsdfhxvnxmcv08905xcbfvjksd'), 17)
        self.assertEqual(hashTable.put('вкс3еме45н5  564  '), 18)
        self.assertEqual(hashTable.put('fsdfhxыапукetxmcvnxcbfvjksd'), 6)
        self.assertEqual(hashTable.put('fsdfhxvnxmcvnxc5435sd'), 13)
        self.assertEqual(hashTable.put('fsdfhxvnxm5443nxcbfvjksd'), 0)
        # print(hashTable.get_slots())

    def test_find(self):
        hashTable = HashTable(19, 3)
        self.assertEqual(hashTable.put('fsdfhxvn980cvnxcbfvjksd'), 8)
        self.assertEqual(hashTable.put('fsdfhxvnxmcvnxcbfvjksd'), 9)
        self.assertEqual(hashTable.put('yery54n77ji'), 11)
        self.assertEqual(hashTable.put('ert43564645'), 5)
        self.assertEqual(hashTable.put('rtbktut'), 16)
        self.assertEqual(hashTable.put('ывспмкенкнк'), 14)
        self.assertEqual(hashTable.put('fsdfhxvnxmcv08905xcbfvjksd'), 17)
        self.assertEqual(hashTable.put('вкс3еме45н5  564  '), 18)
        self.assertEqual(hashTable.put('fsdfhxыапукetxmcvnxcbfvjksd'), 6)
        self.assertEqual(hashTable.put('fsdfhxvnxmcvnxc5435sd'), 13)
        #self.assertEqual(hashTable.put('fsdfhxvnxm5443nxcbfvjksd'), 0)
        # print('test_find')

        self.assertEqual(hashTable.find('fsdfhxvnxmcv08905xcbfvjksd'), 17)
        self.assertEqual(hashTable.find('fsdfhxvnxmcvnxcbfvjksd'), 9)
        self.assertEqual(hashTable.find('yery54n77ji'), 11)
        self.assertEqual(hashTable.find('ert43564645'), 5)
        self.assertEqual(hashTable.find('fsdfhxvn980cvnxcbfvjksd'), 8)
        self.assertEqual(hashTable.find('fsdfhxvnxmcvnxc5435sd'), 13)
        self.assertEqual(hashTable.find('ывспмкенкнк'), 14)
        self.assertEqual(hashTable.find('вкс3еме45н5  564  '), 18)
        self.assertEqual(hashTable.find('fsdfhxыапукetxmcvnxcbfvjksd'), 6)
        self.assertEqual(hashTable.find('rtbktut'), 16)
        self.assertEqual(hashTable.find('fsdfhxvnxm5443nxcbfvjksd'), None)

    def test_put_anomale(self):
        hashTable = HashTable(1, 1)
        self.assertEqual(hashTable.put('fsdfhxvn980cvnxcbfvjksd'), 0)
        self.assertEqual(hashTable.put('fsdfhxvnxmcvnxcbfvjksd'), None)

        hashTable = HashTable(-1, 1)
        with self.assertRaises(ValueError):
            self.assertEqual(hashTable.put('fsdfhxvnxmcvnxcbfvjksd'), None)

        hashTable = HashTable(1, -10)
        self.assertEqual(hashTable.put('fsdfhxvn980cvnxcbfvjksd'), 0)
        self.assertEqual(hashTable.put('fsdfhxvnxmcvnxcbfvjksd'), None)

        hashTable = HashTable(1, 3)
        self.assertEqual(hashTable.put(''), 0)
        self.assertEqual(hashTable.put(''), None)
        self.assertEqual(hashTable.put(''), None)

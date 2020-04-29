import unittest
import math
from pprint import pprint
import random
import string
import copy

from powerSet import PowerSet


class TestPowerSet(unittest.TestCase):

    def seed_power_set(self, str, size, len=10):
        '''
        str = string. may be use 'string.ascii_uppercase + string.digits'
        '''
        ps = PowerSet()
        for _ in range(size+1):
            ps.put(''.join(random.choices(str, k=len)))
        return ps

    def test_hash_fun(self):
        ps = PowerSet()

        self.assertEqual(ps.hash_fun('fsdfhxvn980cvnxcbfvjksd'), 12791)
        self.assertEqual(ps.hash_fun('fsdfhxvnxmcvnxcbfvjksd'), 6881)
        self.assertEqual(ps.hash_fun('yery54n77ji'), 5482)
        self.assertEqual(ps.hash_fun('ert43564645'), 2463)
        self.assertEqual(ps.hash_fun('rtbktut'), 18451)
        self.assertEqual(ps.hash_fun('ывспмкенкнк'), 1642)
        self.assertEqual(ps.hash_fun('fsdfhxvnxmcv08905xcbfvjksd'), 17554)
        self.assertEqual(ps.hash_fun('вкс3еме45н5  564  '), 2603)
        self.assertEqual(ps.hash_fun('fsdfhxыапукetxmcvnxcbfvjksd'), 951)
        self.assertEqual(ps.hash_fun('fsdfhxvnxmcvnxc5435sd'), 10532)
        self.assertEqual(ps.hash_fun('fsdfhxvnxm5443nxcbfvjksd'), 7611)
        # print(ps.get_slots())

    def test_put(self):
        ps = PowerSet()

        ps.put('abc')
        self.assertEqual(ps.size(), 1)

        ps.put('def')
        self.assertEqual(ps.size(), 2)

        ps.put('abc')
        self.assertEqual(ps.size(), 2)

        ps.put('abc')
        self.assertEqual(ps.size(), 2)

        ps.put('abc')
        self.assertEqual(ps.size(), 2)

        ps.put('naeekbnhha')
        self.assertEqual(ps.size(), 3)
        ps.put('fkmmeilabl')                # slot is buzy
        self.assertEqual(ps.size(), 4)

        ps.put('pqbpdmhdkc')
        self.assertEqual(ps.size(), 5)
        ps.put('fnlmmnckdl')                # slot is buzy
        self.assertEqual(ps.size(), 6)

        #print('\n', ps.get_slots())
        slots = ps.get_slots()
        self.assertEqual(slots[13262], 'naeekbnhha')
        self.assertEqual(slots[13295], 'fkmmeilabl')
        self.assertEqual(slots[14490], 'pqbpdmhdkc')
        self.assertEqual(slots[14523], 'fnlmmnckdl')

    def test_remove(self):
        ps = PowerSet()
        ps.put('abc')
        ps.put('def')
        ps.put('ghx')
        ps.put('cvb')

        self.assertEqual(ps.get('abc'), True)
        self.assertEqual(ps.get('def'), True)
        self.assertEqual(ps.get('ghx'), True)
        self.assertEqual(ps.get('cvb'), True)

        self.assertEqual(ps.remove('abc'), True)
        self.assertEqual(ps.get('abc'), False)
        self.assertEqual(ps.size(), 3)

        self.assertEqual(ps.remove('abc1'), False)
        self.assertEqual(ps.size(), 3)

        self.assertEqual(ps.remove('abc'), False)
        self.assertEqual(ps.size(), 3)

        self.assertEqual(ps.remove('def'), True)
        self.assertEqual(ps.get('def'), False)
        self.assertEqual(ps.size(), 2)

        self.assertEqual(ps.remove('ghx'), True)
        self.assertEqual(ps.get('ghx'), False)
        self.assertEqual(ps.size(), 1)

        self.assertEqual(ps.remove('cvb'), True)
        self.assertEqual(ps.get('cvb'), False)
        self.assertEqual(ps.size(), 0)

        self.assertEqual(ps.remove('111111'), False)
        self.assertEqual(ps.size(), 0)

        ps.put('cvb')
        self.assertEqual(ps.remove('cvb'), True)
        self.assertEqual(ps.get('cvb'), False)
        self.assertEqual(ps.size(), 0)

    def test_remove_hard(self):
        ps = self.seed_power_set('abcdefghiklmnopq', 1000, 10)

        #print('\n', ps.get_slots())

        for val in ps.get_val():
            self.assertEqual(ps.remove(val), True)

    def test_get(self):
        ps = PowerSet()

        self.assertEqual(ps.get('abc'), False)

        ps.put('abc')
        ps.put('def')
        ps.put('ghx')
        ps.put('cvb')

        self.assertEqual(ps.get('abc'), True)
        self.assertEqual(ps.get('abc1'), False)
        self.assertEqual(ps.get('def'), True)
        self.assertEqual(ps.get('ghx'), True)
        self.assertEqual(ps.get('cvb'), True)

    def test_intersection(self):
        ps1 = self.seed_power_set('abcdef', 100, 2)
        #print('\nsize1=', ps1.size())
        # print(ps1.get_val())
        ps2 = self.seed_power_set('abcdef', 100, 2)
        #print('\nsize2=', ps2.size())
        # print(ps2.get_val())

        ps = ps1.intersection(ps2)
        #print('\nsize=', ps.size())
        # print(ps.get_val())

        for val in ps.get_val():
            self.assertEqual(ps1.get(val), True)
            self.assertEqual(ps1.get(val), True)

        ps1 = self.seed_power_set('abcdef', 100, 2)
        ps2 = self.seed_power_set('ghjkl', 100, 2)
        ps = ps1.intersection(ps2)
        self.assertEqual(ps.size(), 0)

    def test_union(self):
        ps1 = self.seed_power_set('abcdef', 100, 2)
        ps2 = self.seed_power_set('ghjkl', 100, 2)

        ps = ps1.union(ps2)
        #print('\n1=', ps1.get_val())
        #print('\n2=', ps2.get_val())
        #print('\n=', ps.get_val())
        for val in ps1.get_val():
            self.assertEqual(ps.get(val), True)
        for val in ps2.get_val():
            self.assertEqual(ps.get(val), True)

        ps1 = self.seed_power_set('abcdef', 100, 2)
        ps2 = PowerSet()
        ps = ps1.union(ps2)
        self.assertEqual(ps1.size(), ps.size())

    def test_difference(self):
        ps1 = self.seed_power_set('abcdef', 100, 2)
        ps2 = self.seed_power_set('ghjkl', 100, 2)

        ps = ps1.difference(ps2)
        for val in ps.get_val():
            self.assertEqual(ps1.get(val), True)
            self.assertEqual(ps2.get(val), False)

        ps1 = PowerSet()
        ps2 = self.seed_power_set('ghjkl', 100, 2)
        ps = ps1.difference(ps2)
        self.assertEqual(ps.size(), 0)

        ps1 = self.seed_power_set('ghjkl', 100, 2)
        ps2 = copy.deepcopy(ps1)
        ps = ps1.difference(ps2)
        self.assertEqual(ps.size(), 0)

    def test_issubset(self):
        ps1 = PowerSet()
        ps1.put('abc')
        ps1.put('def')
        ps1.put('ghx')
        ps1.put('cvb')

        ps2 = PowerSet()
        self.assertEqual(ps1.issubset(ps2), True)

        ps2.put('abc')
        self.assertEqual(ps1.issubset(ps2), True)

        ps2 = copy.deepcopy(ps1)
        self.assertEqual(ps1.issubset(ps2), True)

        ps2.put('ppp')
        self.assertEqual(ps1.issubset(ps2), False)

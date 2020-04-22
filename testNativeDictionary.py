import unittest
from nativeDictionary import NativeDictionary


class TestNativeDictionary(unittest.TestCase):

    def test_hash_fun(self):
        nd = NativeDictionary(19)

        self.assertEqual(nd.hash_fun('fsdfhxvn980cvnxcbfvjksd'), 8)
        self.assertEqual(nd.hash_fun('fsdfhxvn980cvnxcbfvjksd'), 8)
        self.assertEqual(nd.hash_fun('fsdfhxvnxmcvnxcbfvjksd'), 9)
        self.assertEqual(nd.hash_fun('yery54n77ji'), 8)
        self.assertEqual(nd.hash_fun('ert43564645'), 5)
        self.assertEqual(nd.hash_fun('rtbktut'), 16)
        self.assertEqual(nd.hash_fun('ывспмкенкнк'), 11)
        self.assertEqual(nd.hash_fun('fsdfhxvnxmcv08905xcbfvjksd'), 8)
        self.assertEqual(nd.hash_fun('вкс3еме45н5  564  '), 18)
        self.assertEqual(nd.hash_fun('fsdfhxыапукetxmcvnxcbfvjksd'), 6)
        self.assertEqual(nd.hash_fun('fsdfhxvnxmcvnxc5435sd'), 13)
        self.assertEqual(nd.hash_fun('fsdfhxvnxm5443nxcbfvjksd'), 13)

    def _test_seek_slot(self):
        nd = NativeDictionary(19)

        self.assertEqual(nd.hash_fun('fsdfhxvn980cvnxcbfvjksd'), 8)
        self.assertEqual(nd.hash_fun('fsdfhxvn980cvnxcbfvjksd'), 8)  # double ^
        self.assertEqual(nd.hash_fun('fsdfhxvnxmcvnxcbfvjksd'), 9)
        self.assertEqual(nd.hash_fun('yery54n77ji'), 8)  # 8->10
        self.assertEqual(nd.hash_fun('ert43564645'), 5)
        self.assertEqual(nd.hash_fun('rtbktut'), 16)
        self.assertEqual(nd.hash_fun('ывспмкенкнк'), 11)
        self.assertEqual(nd.hash_fun('fsdfhxvnxmcv08905xcbfvjksd'), 8)  # 8->11
        self.assertEqual(nd.hash_fun('вкс3еме45н5  564  '), 18)
        self.assertEqual(nd.hash_fun('fsdfhxыапукetxmcvnxcbfvjksd'), 6)
        self.assertEqual(nd.hash_fun('fsdfhxvnxmcvnxc5435sd'), 13)
        self.assertEqual(nd.hash_fun('fsdfhxvnxm5443nxcbfvjksd'), 13)  # 13->14
        self.assertEqual(nd.hash_fun('fsdfhxvnxmcvnxc5435sd'), 14)  # double ^
        self.assertEqual(nd.hash_fun(
            'fsdfhxvnxm5443nxcbfvjksd'), 14)  # double ^

    def test_put(self):
        nd = NativeDictionary(19)

        nd.put('yery54n77ji', 'test_value1')
        self.assertEqual(nd.get_slots()[8], 'yery54n77ji')
        self.assertEqual(nd.get_values()[8], 'test_value1')

        # key 'yery54n77ji' exist, renew value
        nd.put('yery54n77ji', 'test_value11')
        self.assertEqual(nd.get_slots()[8], 'yery54n77ji')
        self.assertEqual(nd.get_values()[8], 'test_value11')

        nd.put('fsdfhxvnxmcvnxcbfvjksd', 'test_value2')
        self.assertEqual(nd.get_values()[9], 'test_value2')

        # slot 8->10
        nd.put('fsdfhxvn980cvnxcbfvjksd', 'test_value12')
        self.assertEqual(nd.get_slots()[10],
                         'fsdfhxvn980cvnxcbfvjksd')
        self.assertEqual(nd.get_values()[10], 'test_value12')

        nd.put('ert43564645', 'test_value3')
        self.assertEqual(nd.get_slots()[5], 'ert43564645')
        self.assertEqual(nd.get_values()[5], 'test_value3')

        nd.put('rtbktut', 'test_value4')
        self.assertEqual(nd.get_slots()[16], 'rtbktut')
        self.assertEqual(nd.get_values()[16], 'test_value4')

        nd.put('ывспмкенкнк', 'test_value5')
        self.assertEqual(nd.get_slots()[11], 'ывспмкенкнк')
        self.assertEqual(nd.get_values()[11], 'test_value5')

        nd.put('вкс3еме45н5  564  ', 'test_value7')
        self.assertEqual(nd.get_slots()[18], 'вкс3еме45н5  564  ')
        self.assertEqual(nd.get_values()[18], 'test_value7')

        # slot 8->12
        nd.put('fsdfhxvnxmcv08905xcbfvjksd', 'test_value8')
        self.assertEqual(nd.get_slots()[12],
                         'fsdfhxvnxmcv08905xcbfvjksd')
        self.assertEqual(nd.get_values()[12], 'test_value8')

        # key exist in 12 slot, renew
        nd.put('fsdfhxvnxmcv08905xcbfvjksd', 'test_value9')
        # print(nd.get_slots())
        # print(nd.get_values())
        self.assertEqual(nd.get_slots()[12], 'fsdfhxvnxmcv08905xcbfvjksd')
        self.assertEqual(nd.get_values()[12], 'test_value9')

        # take overflow length dict
        nd.put('34253452', 'test_value21')
        # print(nd.get_slots())
        nd.put('34259678783452', 'test_value22')
        # print(nd.get_slots())
        nd.put('78978', 'test_value23')
        # print(nd.get_slots())
        nd.put('23423', 'test_value24')
        # print(nd.get_slots())
        nd.put('2345474575623', 'test_value25')
        # print(nd.get_slots())
        nd.put('5467437', 'test_value26')
        # print(nd.get_slots())
        nd.put('683436', 'test_value27')
        # print(nd.get_slots())
        nd.put('67564', 'test_value28')
        # print(nd.get_slots())
        nd.put('534535', 'test_value28')
        # print(nd.get_slots())
        nd.put('6867978', 'test_value28')
        # print(nd.get_slots())
        nd.put('345345', 'test_value28')
        # print(nd.get_slots())
        with self.assertRaises(TypeError):
            nd.put('34539789789645', 'test_value28')
        # print(nd.get_slots())

    def test_is_key(self):
        nd = NativeDictionary(19)

        nd.put('yery54n77ji', 'test_value1')  # 8
        nd.put('yery54n77ji', 'test_value11')  # 8
        nd.put('fsdfhxvnxmcvnxcbfvjksd', 'test_value2')  # 9
        nd.put('ert43564645', 'test_value3')  # 5
        nd.put('rtbktut', 'test_value4')  # 16
        nd.put('ывспмкенкнк', 'test_value5')  # 11
        nd.put('вкс3еме45н5  564  ', 'test_value7')  # 18
        nd.put('fsdfhxvnxmcv08905xcbfvjksd', 'test_value8')  # 12
        nd.put('fsdfhxvnxmcv08905xcbfvjksd', 'test_value9')  # 12

        self.assertEqual(nd.is_key('yery54n77ji'), True)
        self.assertEqual(nd.is_key('fsdfhxvnxmcvnxcbfvjksd'), True)
        self.assertEqual(nd.is_key('ert43564645'), True)
        self.assertEqual(nd.is_key('rtbktut'), True)
        self.assertEqual(nd.is_key('rtbktut'), True)
        self.assertEqual(nd.is_key('ывспмкенкнк'), True)
        self.assertEqual(nd.is_key('fsdfhxvnxmcv08905xcbfvjksd'), True)

        self.assertEqual(nd.is_key('false_key'), False)
        self.assertEqual(nd.is_key('fsdfhxvn980cvnxcbfvjksd'),
                         False)  # 8 slot user by 'yery54n77ji'

    def test_get(self):
        nd = NativeDictionary(19)

        nd.put('yery54n77ji', 'test_value1')  # 8
        nd.put('yery54n77ji', 'test_value11')  # 8
        nd.put('fsdfhxvnxmcvnxcbfvjksd', 'test_value2')  # 9
        nd.put('ert43564645', 'test_value3')  # 5
        nd.put('rtbktut', 'test_value4')  # 16
        nd.put('ывспмкенкнк', 'test_value5')  # 11
        nd.put('вкс3еме45н5  564  ', 'test_value7')  # 18
        nd.put('fsdfhxvnxmcv08905xcbfvjksd', 'test_value8')  # 12
        nd.put('fsdfhxvnxmcv08905xcbfvjksd', 'test_value9')  # 12

        self.assertEqual(nd.get('yery54n77ji'),
                         'test_value11')  # value overwritten
        self.assertEqual(nd.get('fsdfhxvnxmcvnxcbfvjksd'), 'test_value2')
        self.assertEqual(nd.get('ert43564645'), 'test_value3')
        self.assertEqual(nd.get('rtbktut'), 'test_value4')
        self.assertEqual(nd.get('rtbktut'), 'test_value4')
        self.assertEqual(nd.get('ывспмкенкнк'), 'test_value5')
        self.assertEqual(nd.get('fsdfhxvnxmcv08905xcbfvjksd'),
                         'test_value9')  # value overwritten

        self.assertEqual(nd.get('false_key'), None)
        self.assertEqual(nd.get('fsdfhxvn980cvnxcbfvjksd'), None)

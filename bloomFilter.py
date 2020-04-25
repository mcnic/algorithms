class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len ...
        fmt = '{:0' + str(self.filter_len) + 'b}'
        self.idx = int(fmt.format(0))  # обрезаем до длины self.filter_len

    def hash1(self, str1):
        return self.hash(17, str1)

    def hash2(self, str1):
        return self.hash(223, str1)

    def hash(self, num, str1):
        res = 0
        for c in str1:
            res = (res * num + ord(c)) % self.filter_len
        return res

    def add(self, str1):
        '''
        добавляем строку str1 в фильтр:
        выставляем 1 в битах результатов всех хэш-функций
        '''
        bits = (1 << self.hash1(str1)) | (1 << self.hash2(str1))
        self.idx |= bits
        return bits

    def is_value(self, str1):
        '''
        проверка, имеется ли строка str1 в фильтре:
        во всех битах индекса должны быть выставлены биты соответствующие результатам всех хэш-функций
        '''
        bits = (1 << self.hash1(str1)) | (1 << self.hash2(str1))
        index_masked = self.idx & bits
        return index_masked == bits

    def get_idx(self):
        return self.idx

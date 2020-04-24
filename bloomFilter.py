class BloomFilter:

    def __init__(self, f_len):
        '''
        памятка по преобразованию типов
        # num = int('{:032b}'.format(17), 2)  # format as 32 bit
        # print(bin(num))
        # print(f"{17:b}")
        '''
        self.filter_len = f_len
        # создаём битовый массив длиной f_len ...
        fmt = '{:0' + str(self.filter_len) + 'b}'
        self.idx = int(fmt.format(0))  # обрезаем до длины self.filter_len

        self.values = [None] * self.filter_len

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
        добавляем строку str1 в фильтр
        '''
        num = self.get_index(str1)
        # indexes as string - remake to int and byte operation
        #indexes = list(self.idx)
        #indexes[num] = str(1)
        #self.idx = ''.join(indexes)

        self.idx |= 1 << num
        #print(num, '=>', bin(self.idx))
        self.values[num] = str1
        return num

    def is_value(self, str1):
        '''
        проверка, имеется ли строка str1 в фильтре
        '''
        # return self.values[self.get_index(str1)] != None
        index = self.get_index(str1)
        return self.idx & 1 << index != 0

    def get_index(self, str1):
        '''
        вычисляет индекс в массиве на основании всех хэш-функций
        '''
        index = self.hash1(str1) & self.hash2(str1)
        # print(self.format(self.hash1(str1)), '&',
        #      self.format(self.hash2(str1)), '=', self.format(index), '(', index, ')')
        return index

    def get_idx(self):
        return self.idx

    def get_values(self):
        return self.values

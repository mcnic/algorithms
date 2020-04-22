import hashlib
import math


class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.step = 1

    def hash_fun(self, key):
        '''
        в качестве key поступают строки!
        всегда возвращает корректный индекс слота
        '''
        hash = hashlib.sha1()
        hash.update(key.encode())
        hash = int(hash.hexdigest()[:math.ceil(
            self.size / 16)], 16)  # hex to int
        return hash % self.size

    def is_key(self, key):
        '''
        возвращает True если ключ имеется,
        иначе False
        '''
        # return self.slots[self.seek_slot(key)] != None
        return self.slots[self.seek_slot(key)] == key

    def put(self, key, value):
        '''
        гарантированно записываем
        значение value по ключу key.

        при переполнении массива слотов вызывает ошибку TypeError - надо делать resize????
        '''
        slot = self.seek_slot(key)
        # if slot == None:
        #    return None
        self.slots[slot] = key
        self.values[slot] = value
        return slot

    def get(self, key):
        '''
        возвращает value для key,
        или None если ключ не найден
        '''
        slot = self.seek_slot(key)
        if self.slots[slot] == key:
            return self.values[slot]
        else:
            return None

    def seek_slot(self, key):
        '''
        находит индекс пустого слота для значения
        '''
        slot = self.hash_fun(key)
        max_loop = 10 * self.size
        while self.slots[slot] != None and self.slots[slot] != key:
            # repair collision
            max_loop -= 1
            if max_loop < 0:
                return None

            # if abs(self.step) >= self.size:
            #    return None

            slot += self.step
            if slot >= self.size:
                slot -= self.size
        return slot

    def get_slots(self):
        return self.slots

    def get_values(self):
        return self.values

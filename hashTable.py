import hashlib
import math


class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        '''
        в качестве value поступают строки!
        '''
        hash = hashlib.sha1()
        hash.update(value.encode())
        hash = int(hash.hexdigest()[:math.ceil(
            self.size / 16)], 16)  # hex to int
        return hash % self.size

    def seek_slot(self, value):
        '''
        находит индекс пустого слота для значения, или None
        '''
        slot = self.hash_fun(value)
        # reapir collision
        max_loop = 10 * self.size
        while self.slots[slot] != None:
            max_loop -= 1
            if max_loop < 0:
                return None

            if abs(self.step) >= self.size:
                return None

            slot += self.step
            if slot >= self.size:
                slot -= self.size
        return slot

    def put(self, value):
        '''
        записываем значение по хэш-функции
        возвращается индекс слота или None,
        если из-за коллизий элемент не удаётся разместить
        '''
        slot = self.seek_slot(value)
        if slot == None:
            return None
        self.slots[slot] = value
        return slot

    def find(self, value):
        '''
        находит индекс слота со значением, или None
        '''
        slot = self.hash_fun(value)
        max_loop = 100
        while self.slots[slot] != value:
            max_loop -= 1
            if max_loop < 0:
                return None

            if abs(self.step) >= self.size:
                return None

            slot += self.step
            if slot >= self.size:
                slot -= self.size
        return slot

    def get_slots(self):
        return self.slots

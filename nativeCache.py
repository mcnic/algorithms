import hashlib
import math
import copy


class NativeCache:

    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def get_key(self, value):
        '''
        в качестве value поступают строки!
        '''
        hash = hashlib.sha1()
        hash.update(value.encode())
        return hash.hexdigest()

    def hash_fun(self, key):
        '''
        в качестве key поступают строки!
        '''
        #hash = hashlib.sha1()
        # hash.update(key.encode())
        hash = int(key[:math.ceil(
            self.size / 16)], 16)  # hex to int
        return hash % self.size

    def seek_slot(self, key):
        '''
        находит слот(индекс) с значением key, 
        либо пустой слот (если значения нет),
        либо слот с самым маленьким значением hits
        '''
        slot = self.hash_fun(key)
        min_hit_slot = 0
        max_loop = 2
        while max_loop > 0:
            if self.slots[slot] == key:  # seek success
                return slot

            if self.slots[slot] == None:  # seek empty slot
                return slot

            slot += 1
            if slot >= self.size:
                slot -= self.size   # next loop
                max_loop -= 1
                if max_loop < 0:
                    return min_hit_slot

            if self.slots[slot] != None and self.slots[min_hit_slot] != None and self.hits[slot] < self.hits[min_hit_slot]:
                min_hit_slot = slot

        return min_hit_slot

    def put(self, value):
        '''
        записываем значение по хэш-функции
        возвращается индекс слота,
        увеличивает hits для записываемого значения
        '''
        key = self.get_key(value)
        slot = self.seek_slot(key)
        if self.slots[slot] == None:
            self.hits[slot] = 1
        else:
            self.hits[slot] += 1

        self.slots[slot] = key
        self.values[slot] = value

        return slot

    def find(self, key):
        '''
        находит индекс слота со значением, или None
        '''
        slot = self.hash_fun(key)
        max_loop = 2
        while max_loop > 0:
            if self.slots[slot] == key:  # seek success
                return slot

            if self.slots[slot] == None:
                return None

            slot += 1
            if slot >= self.size:
                slot -= self.size
                max_loop -= 1

        return None

    def get(self, value):
        '''
        возвращает значение кеша, если оно имеется,
        иначе None, если его нет
        '''
        key = self.get_key(value)
        slot = self.find(key)
        if slot == None:
            return None
        else:
            self.hits[slot] += 1
            return self.values[slot]

    def get_values(self):
        i = 0
        res = {}
        while i < self.size:
            if self.slots[i] != None:
                res[i] = self.values[i]
            i += 1
        return res

    def get_slots(self):
        return self.slots

    def get_hits(self):
        return self.hits

    def get_hit(self, num):
        return self.hits[num]

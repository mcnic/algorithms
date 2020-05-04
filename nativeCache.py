import hashlib
import math
import copy


class NativeCache:

    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

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
        находит слот(индекс) с значением value, 
        либо пустой слот (если значения нет),
        либо слот с самым маленьким значением hits
        '''
        slot = self.hash_fun(value)
        min_hit_slot = 0
        max_loop = 2
        while max_loop > 0:
            if self.slots[slot] == value:  # seek success
                return slot

            if self.slots[slot] == None:  # seek empty slot
                return slot

            slot += 1
            if slot >= self.size:
                slot -= self.size   # next loop
                max_loop -= 1
                if max_loop < 0:
                    return min_hit_slot

            if self.slots[slot] != None and self.slots[min_hit_slot] != None and self.slots[slot] < self.slots[min_hit_slot]:
                min_hit_slot = slot

        return min_hit_slot

    def put(self, value):
        '''
        записываем значение по хэш-функции
        возвращается индекс слота,
        увеличивает hits для записываемого значения
        '''
        slot = self.seek_slot(value)
        self.slots[slot] = value
        self.hits[slot] += 1

        return slot

    def find(self, value):
        '''
        находит индекс слота со значением, или None
        '''
        slot = self.hash_fun(value)
        max_loop = 2
        while max_loop > 0:
            if self.slots[slot] == value:  # seek success
                return slot

            if self.slots[slot] == None:
                return None

            slot += 1
            if slot >= self.size:
                slot -= self.size
                max_loop -= 1
                if max_loop < 0:
                    return None

        return slot

    def get(self, value):
        '''
        возвращает значение кеша, если оно имеется либо,
        иначе None, если еге нет
        '''
        return True if self.find(value) != None else False

    def get_val(self):
        i = 0
        res = []
        while i < self.size:
            if self.slots[i] != None:
                res.append(self.slots[i])
            i += 1
        return res

    def get_slots(self):
        i = 0
        res = {}
        while i < self.size:
            if self.slots[i] != None:
                res[i] = self.slots[i]
            i += 1
        return res

    def get_hits(self):
        return self.hits

    def get_hit(self, num):
        return self.hits[num]

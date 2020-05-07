import hashlib
import math
import copy


class PowerSet:

    def __init__(self):
        self.len = 20000
        self.step = 33
        self.slots = [None] * self.len
        self._size = 0

    def hash_fun(self, value):
        '''
        в качестве value поступают строки!
        '''
        hash = hashlib.sha1()
        hash.update(value.encode())
        hash = int(hash.hexdigest()[:math.ceil(
            self.len / 16)], 16)  # hex to int
        return hash % self.len

    def seek_slot(self, value):
        '''
        находит слот(индекс) с значением value, 
        либо пустой слот (если значения нет),
        либо None (если не получается выделить новый пустой слот)
        '''
        slot = self.hash_fun(value)

        # repair collision: seek new empty slot or seek value in other slot
        max_loop = 5 * self.len
        while max_loop > 0:
            if self.slots[slot] == value:  # seek success
                return slot

            if self.slots[slot] == None:  # seek empty slot
                return slot

            #print('\nvalue', value, 'slot=', slot, 'buzy is', self.slots[slot], '->', slot + self.step)
            slot += self.step

            if slot >= self.len:
                slot -= self.len
                max_loop -= 1

        return None

    def size(self):
        '''
        количество элементов в множестве
        '''
        return self._size

    def find(self, value):
        '''
        находит индекс слота со значением, или None
        '''
        slot = self.hash_fun(value)
        max_loop = 20
        while self.slots[slot] != value:

            if abs(self.step) >= self.len:
                return None

            slot += self.step
            if slot >= self.len:
                slot -= self.len
                max_loop -= 1
                if max_loop < 0:
                    return None
        return slot

    def put(self, value):
        slot = self.seek_slot(value)

        if slot == None:
            return None

        if self.slots[slot] != value:
            self._size += 1
            self.slots[slot] = value

    def get(self, value):
        '''
        возвращает True если value имеется в множестве,
        иначе False
        '''
        return True if self.find(value) != None else False

    def remove(self, value):
        '''
        возвращает True если value удалено
        иначе False
        '''
        slot = self.hash_fun(value)

        max_loop = 10 * self.len
        while max_loop > 0:
            if self.slots[slot] == value:  # seek success
                self.slots[slot] = None
                self._size -= 1
                return True

            max_loop -= 1
            slot += self.step

            if slot >= self.len:
                slot -= self.len

        return False

    def intersection(self, set2):
        '''
        пересечение текущего множества и set2
        '''
        i = 0
        new_ps = PowerSet()
        while i < self.len:
            if self.slots[i] != None:
                if set2.get(self.slots[i]):
                    new_ps.put(self.slots[i])
            i += 1
        return new_ps

    def union(self, set2):
        '''
        объединение текущего множества и set2
        '''
        new_ps = copy.deepcopy(self)
        for val in set2.get_val():
            new_ps.put(val)
        return new_ps

    def difference(self, set2):
        '''
        разница текущего множества и set2
        '''
        i = 0
        new_ps = PowerSet()
        while i < self.len:
            if self.slots[i] != None:
                if not set2.get(self.slots[i]):
                    new_ps.put(self.slots[i])
            i += 1
        return new_ps

    def issubset(self, set2):
        '''
        возвращает True, если set2 есть
        подмножество текущего множества,
        иначе False
        '''
        for val in set2.get_val():
            if not self.get(val):
                return False
        return True

    def get_val(self):
        i = 0
        res = []
        while i < self.len:
            if self.slots[i] != None:
                res.append(self.slots[i])
            i += 1
        return res

    def get_slots(self):
        i = 0
        res = {}
        while i < self.len:
            if self.slots[i] != None:
                res[i] = self.slots[i]
            i += 1
        return res

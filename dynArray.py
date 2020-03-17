import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def get(self):
        ret_array = []
        for i in range(self.count):
            ret_array.append(self.array[i])
        return ret_array

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_capacity = int(new_capacity)

        if new_capacity < 16:
            new_capacity = 16

        if self.capacity == new_capacity:
            return

        #print('self.count=', self.count, ' self.capacity=', self.capacity, 'new capa=', new_capacity)
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)

        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        # добавляем объект itm в позицию i, начиная с 0
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == self.capacity:
            self.resize(2*self.capacity)

        if i == self.count:     # add in tail
            self.array[i] = itm
        else:                   # >>1 after i-pos
            pos = self.count
            while pos > i:
                self.array[pos] = self.array[pos-1]
                pos -= 1
            self.array[i] = itm

        self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        pos = i+1
        while pos < self.count:
            self.array[pos-1] = self.array[pos]
            pos += 1

        self.count -= 1

        if self.count < self.capacity / 2:
            self.resize(self.capacity // 1.5)

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    '''
        из-за непонятки насчет удаления (по полному совпадению, или используя нестрогий поиск), 
        сделано 2 варианта поиска и 2 варианта удаления
    '''

    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self._len = 0

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

    def add(self, value):
        # if list clear
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self._len = 1
            return

        if self.__ascending == True:
            # value bigger tail value
            if self.compare(value, self.tail.value) == 1:
                node = Node(value)
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                self._len += 1
                return

            # value little head value
            if self.compare(value, self.head.value) == -1:
                node = Node(value)
                node.next = self.head
                self.head.prev = node
                self.head = node
                self._len += 1
                return

            # brute force all value
            el = self.head
            while el != None:
                if self.compare(value, el.value) == -1:
                    node = Node(value)
                    node.next = el
                    node.prev = el.prev
                    node.prev.next = node
                    node.next.prev = node
                    self._len += 1
                    return
                el = el.next

        else:
            # value bigger head value
            if self.compare(value, self.head.value) == 1:
                node = Node(value)
                node.next = self.head
                self.head.prev = node
                self.head = node
                self._len += 1
                return

            # value littles tail value
            if self.compare(value, self.tail.value) == -1:
                node = Node(value)
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                self._len += 1
                return

            # brute force all value
            el = self.tail
            while el != None:
                if self.compare(value, el.value) == -1:
                    node = Node(value)
                    node.prev = el
                    node.next = el.next
                    node.next.prev = node
                    el.next = node
                    self._len += 1
                    return
                el = el.prev

    def find(self, val, strong=False):
        node = self.head
        if strong == False:
            while node != None:
                if self.__ascending == True:
                    if node.value >= val:
                        return node
                else:
                    if node.value <= val:
                        return node
                node = node.next
        else:
            while node != None:
                if node.value == val:
                    return node
                node = node.next

    def delete(self, val, strong=False):
        node = self.find(val, strong)

        if node == None:
            return

        self._len -= 1

        if node == self.head == self.tail:   # 1 element list
            self.head = None
            self.tail = None
            return

        if node == self.head:   # is first
            self.head = node.next
            if self.head != None:
                self.head.prev = None
            return

        if node == self.tail:   # is last
            self.tail = node.prev
            if self.tail != None:
                self.tail.next = None
            return

        if node.prev != None:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self._len = 0

    def len(self):
        return self._len

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def get_all_values(self):
        r = []
        node = self.head
        while node != None:
            r.append(node.value)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip(' ')
        v2 = v2.strip(' ')

        if v1 < v2:
            return -1
        if v1 > v2:
            return 1

        return 0

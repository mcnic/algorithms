class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
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
            self._len += 1
            return

        # 1 elements list
        if self.len() == 1:
            node = Node(value)
            compare_res = self.compare(value, self.head.value)
            if (self.__ascending and compare_res >= 0) or (not self.__ascending and compare_res < 0):
                self.tail = node
            else:
                self.head = node
            self.tail.prev = self.head
            self.head.next = self.tail
            self._len += 1
            return

        self._len += 1

        if self.__ascending:
            # value bigger tail value
            if self.compare(value, self.tail.value) == 1:
                node = Node(value)
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                return

            # value little head value
            if self.compare(value, self.head.value) == -1:
                node = Node(value)
                node.next = self.head
                self.head.prev = node
                self.head = node
                return

            # brute force all value
            el = self.head.next
            while el != None:
                if self.compare(value, el.value) <= 0:
                    node = Node(value)
                    node.next = el
                    node.prev = el.prev
                    node.prev.next = node
                    el.prev = node
                    return
                el = el.next
        # desc
        else:
            # value bigger head value
            if self.compare(value, self.head.value) == 1:
                node = Node(value)
                node.next = self.head
                self.head.prev = node
                self.head = node
                return

            # value littles tail value
            if self.compare(value, self.tail.value) == -1:
                node = Node(value)
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                return

            # brute force all value
            el = self.head.next
            while el != None:
                if self.compare(value, el.value) >= 0:
                    node = Node(value)
                    node.next = el
                    node.prev = el.prev
                    node.prev.next = node
                    el.prev = node
                    return
                el = el.next

    def find(self, val):
        node = self.head
        while node != None:
            if self.compare(node.value, val) == 0:
                return node
            if self.compare(node.value, val) == 1 and self.__ascending:
                return None
            if self.compare(node.value, val) == -1 and not self.__ascending:
                return None

            node = node.next

        return None

    def delete(self, val):
        node = self.find(val)

        if node == None:
            return

        self._len -= 1

        if node == self.head == self.tail:   # 1 element list
            self.head = None
            self.tail = None
            return

        if node == self.head:   # is first
            self.head = node.next
            # if self.head != None:
            self.head.prev = None
            return

        if node == self.tail:   # is last
            self.tail = node.prev
            # if self.tail != None:
            self.tail.next = None
            return

        # if node.prev != None:
        node.prev.next = node.next
        # if node.next != None:
        node.next.prev = node.prev

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self._len = 0

    def len(self):
        return self._len

        node = self.head
        len = 0
        while node != None:
            len += 1
            node = node.next

        if len != self._len:
            raise(SyntaxError)

        return len

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

        if v1 < v2 or len(v1) < len(v2):
            return -1
        if v1 > v2 or len(v1) > len(v2):
            return 1

        return 0

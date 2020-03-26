class Queue:
    def __init__(self):
        self.queue = LinkedList2()
        self._size = 0

    # вставка в хвост
    def enqueue(self, item):
        self.queue.add_in_tail(Node(item))
        self._size += 1

    def peek(self):
        head = self.queue.get_head()
        if head == None:
            return None
        else:
            return head.value

    # выдача из головы
    def dequeue(self):
        head = self.queue.get_head()
        if head == None:
            return None
        else:
            self.queue.delete_head()
            self._size -= 1
            return head.value

    def size(self):
        return self._size

    def get_all(self):
        return self.queue.get_all()


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_all(self):
        res = []
        node = self.head
        while node != None:
            res.append(node.value)
            node = node.next
        return res

    def get_all_nodes(self):
        res = []
        node = self.head
        while node != None:
            res.append(node)
            node = node.next
        return res

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def create_list(self, array_list):
        list1 = LinkedList2()
        for val in array_list:
            list1.add_in_tail(Node(val))
        return list1

    def add_in_tail(self, item):
        if item is None:
            return

        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        res = []
        node = self.head
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, all=False):
        node = self.head

        while node != None:
            if node.value == val:
                if node == self.head:   # is first
                    self.head = node.next
                    if self.head != None:
                        self.head.prev = None

                if node.next == None:   # is last
                    self.tail = node.prev
                    if self.tail != None:
                        self.tail.next = None
                    node = None

                if node != None and node.prev != None:
                    node.prev.next = node.next
                    node.next.prev = node.prev

                if node != None:
                    node = node.next

                if all == False:
                    return
            else:
                node = node.next

    def delete_head(self):
        node = self.head

        if node == None:
            #raise IndexError('Stack is clear')
            return

        self.head = node.next
        if self.head != None:
            self.head.prev = None

    def delete_tail(self):
        node = self.tail

        if node == None:
            #raise IndexError('Stack is clear')
            return

        if node == self.head:   # is first and alone
            self.head = None
            self.tail = None
        else:
            self.tail = node.prev
            if self.tail != None:
                self.tail.next = None

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        len = 0
        node = self.head
        while node is not None:
            node = node.next
            len += 1
        return len

    # if afterNode=None: if list empty - add in head, else add in tail
    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
            return

        if newNode is None:
            return

        newNode.next = afterNode.next
        newNode.prev = afterNode
        if newNode.prev != None:
            newNode.prev.next = newNode
        if newNode.next != None:
            newNode.next.prev = newNode

        if newNode.next is None:
            self.tail = newNode

    def add_in_head(self, newNode):
        if newNode is None:
            return

        if self.tail is None:   # clear
            newNode.prev = None
            newNode.next = None
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            newNode.prev = None

        self.head = newNode

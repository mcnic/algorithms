class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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
        prev_node = None

        while node != None:
            if node.value == val:
                if node == self.head:   # is first
                    self.head = node.next
                    prev_node = None

                if node.next == None:   # is last
                    self.tail = prev_node
                    if prev_node != None:
                        prev_node.next = None
                    node = None

                if prev_node != None and node != None:
                    prev_node.next = node.next

                if node != None:
                    node = node.next

                if all == False:
                    return
            else:
                prev_node = node
                node = node.next

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

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.head = newNode
            else:
                newNode.next = self.head
                self.head = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode

        if newNode.next is None:
            self.tail = newNode

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def create_list(self, array_list):
        list1 = LinkedList()
        for val in array_list:
            list1.add_in_tail(Node(val))
        return list1

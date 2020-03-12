from linkedList import Node, LinkedList


def lists_add(list1, list2):
    if list1.len() != list2.len():
        return False
    else:
        result_list = LinkedList()
        node1 = list1.get_head()
        node2 = list2.get_head()
        while node1 != None:
            result_list.add_in_tail(Node(node1.value + node2.value))
            node1 = node1.next
            node2 = node2.next
        return result_list

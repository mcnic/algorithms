from linkedList import Node, LinkedList


def test_find():
    list2 = LinkedList()
    assert(list2.find(55) == None)
    assert(list2.find(None) == None)
    assert(list2.find_all(None) == [])
    assert(list2.find_all(55) == [])
    assert(list2.get_head() == None)
    assert(list2.get_tail() == None)

    n1 = Node(55)
    n2 = Node(12)
    n3 = Node(55)
    list2.add_in_tail(n1)
    print('\nlist2 =', list2.get_all())
    assert(list2.find(n1.value) == n1)
    assert(list2.find_all(n1.value) == [n1])

    list2.add_in_tail(n2)
    list2.add_in_tail(n3)
    assert(list2.find_all(n3.value) == [n1, n3])
    assert(list2.get_head() == n1)
    assert(list2.get_tail() == n3)


def test_insert():
    list3 = LinkedList()
    n1 = Node(55)
    n2 = Node(12)
    n3 = Node(55)
    list3.add_in_tail(n1)
    list3.add_in_tail(n2)
    list3.add_in_tail(n3)
    print('\nlist3 =', list3.get_all())
    assert(list3.find(55).value == 55)
    assert(list3.find_all(55) == [n1, n3])
    assert(list3.get_head() == n1)
    assert(list3.get_tail() == n3)

    n4 = Node(10)
    list3.insert(n2, n4)
    print('list3 insert 10 after 12 =', list3.get_all())
    assert(list3.get_all() == [55, 12, 10, 55])
    assert(list3.get_head() == n1)
    assert(list3.get_tail() == list3.find_all(55)[1])

    n5 = Node(20)
    list3.insert(None, n5)
    print('list3 insert 20 in head =', list3.get_all())
    assert(list3.get_all() == [20, 55, 12, 10, 55])
    assert(list3.get_head() == n5)
    assert(list3.get_tail() == n3)

    n6 = Node(22)
    list3_tail = list3.get_tail()
    list3.insert(list3_tail, n6)
    print('list3 insert 22 after last =', list3.get_all())
    assert(list3.get_all() == [20, 55, 12, 10, 55, 22])
    assert(list3.get_head() == list3.find(20))
    assert(list3.get_tail() == list3.find(22))

    list3 = LinkedList()
    n44 = Node(11)
    list3.insert(None, n44)
    print('\nlist3 insert in clear list =', list3.get_all())
    assert(list3.get_all() == [n44.value])
    assert(list3.get_head() == n44)
    assert(list3.get_tail() == n44)


def test_delete():
    test_items = [55, 12, 43, 10, 14, 12, 55, 10, 5]
    list1 = LinkedList()
    for val in test_items:
        list1.add_in_tail(Node(val))

    print('\nlist1 =', list1.get_all())
    print('list1 len =', list1.len())
    assert(list1.len() == 9)
    assert(list1.get_all() == [55, 12, 43, 10, 14, 12, 55, 10, 5])
    assert(list1.len() == 9)
    assert(list1.get_head() == list1.find(55))
    assert(list1.get_tail() == list1.find(5))

    print('\nlist1 delete in head 55:')
    list1.delete(55)
    print(list1.get_all())
    assert(list1.get_all() == [12, 43, 10, 14, 12, 55, 10, 5])
    assert(list1.len() == 8)
    assert(list1.get_head() == list1.find(12))
    assert(list1.get_tail() == list1.find(5))

    print('\nlist1 delete in body 43:')
    list1.delete(43)
    print(list1.get_all())
    assert(list1.get_all() == [12, 10, 14, 12, 55, 10, 5])
    assert(list1.len() == 7)
    assert(list1.get_head() == list1.find(12))
    assert(list1.get_tail() == list1.find(5))

    print('\nlist1 delete in head&all 12: ')
    list1.delete(12, True)
    print(list1.get_all())
    assert(list1.get_all() == [10, 14, 55, 10, 5])
    assert(list1.len() == 5)
    assert(list1.get_head() == list1.find(10))
    assert(list1.get_tail() == list1.find(5))

    print('\nlist1 delete in tail 5: ')
    list1.delete(5)
    print(list1.get_all())
    assert(list1.get_all() == [10, 14, 55, 10])
    assert(list1.get_head() == list1.find_all(10)[0])
    assert(list1.get_tail() == list1.find_all(10)[1])

    print('\nlist1 delete wrong data: ')
    list1.delete(77)
    print(list1.get_all())
    assert(list1.get_all() == [10, 14, 55, 10])
    assert(list1.get_head() == list1.find_all(10)[0])
    assert(list1.get_tail() == list1.find_all(10)[1])

    print('\nlist1 delete None: ')
    list1.delete(None)
    print(list1.get_all())
    assert(list1.get_all() == [10, 14, 55, 10])
    assert(list1.len() == 4)
    assert(list1.get_head() == list1.find_all(10)[0])
    assert(list1.get_tail() == list1.find_all(10)[1])

    print('\ntest delete in 1-elements list:')
    list4 = LinkedList()
    n1 = Node(55)
    list4.add_in_tail(n1)
    list4.delete(55)
    print(list4.get_all())
    assert(list4.get_all() == [])
    assert(list4.get_head() == None)
    assert(list4.get_tail() == None)

    list1.clean()
    assert(list1.get_all() == [])
    assert(list1.get_head() == None)
    assert(list1.get_tail() == None)


def compare_list(list1, list2):
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


def test_compare():
    test_data1 = [55, 12, 43, 10, 14, 12, 55, 10, 5]
    test_data2 = [55, 12, 43, 10, 14, 12, 55, 10]

    list1 = LinkedList()
    for val in test_data1:
        list1.add_in_tail(Node(val))

    list1_copy = LinkedList()
    for val in test_data1:
        list1_copy.add_in_tail(Node(val))

    list3 = LinkedList()
    for val in test_data2:
        list3.add_in_tail(Node(val))

    assert(compare_list(list1, list3) == False)
    assert(compare_list(LinkedList(), LinkedList()), [])
    assert(compare_list(list1, list1_copy).get_all() == [
           110, 24, 86, 20, 28, 24, 110, 20, 10])


if __name__ == "__main__":
    test_find()
    test_insert()
    test_delete()

    test_compare()

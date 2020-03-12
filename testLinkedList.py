from linkedList import Node, LinkedList
from LinkedListAdd import *


def create_list(array_list):
    list1 = LinkedList()
    for val in array_list:
        list1.add_in_tail(Node(val))
    return list1


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
    print('\nlist for find =', list2.get_all())
    assert(list2.find(n1.value) == n1)
    assert(list2.find_all(n1.value) == [n1])

    list2.add_in_tail(n2)
    list2.add_in_tail(n3)
    print('\nlist_2 for find =', list2.get_all())
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
    print('\nlist for insert =', list3.get_all())
    assert(list3.find(55).value == 55)
    assert(list3.find_all(55) == [n1, n3])
    assert(list3.get_head() == n1)
    assert(list3.get_tail() == n3)

    n4 = Node(10)
    list3.insert(n2, n4)
    print('insert 10 after 12 =', list3.get_all())
    assert(list3.get_all() == [55, 12, 10, 55])
    assert(list3.get_head() == n1)
    assert(list3.get_tail() == list3.find_all(55)[1])

    n5 = Node(20)
    list3.insert(None, n5)
    print('insert 20 in head =', list3.get_all())
    assert(list3.get_all() == [20, 55, 12, 10, 55])
    assert(list3.get_head() == n5)
    assert(list3.get_tail() == n3)

    n6 = Node(22)
    list3_tail = list3.get_tail()
    list3.insert(list3_tail, n6)
    print('insert 22 after last =', list3.get_all())
    assert(list3.get_all() == [20, 55, 12, 10, 55, 22])
    assert(list3.get_head() == list3.find(20))
    assert(list3.get_tail() == list3.find(22))

    list3 = LinkedList()
    n44 = Node(11)
    list3.insert(None, n44)
    print('insert in clear list =', list3.get_all())
    assert(list3.get_all() == [n44.value])
    assert(list3.get_head() == n44)
    assert(list3.get_tail() == n44)


def test_delete():
    list1 = create_list([55, 12, 43, 10, 14, 12, 55, 10, 5])

    print('\nlist for delete:\n', list1.get_all())
    assert(list1.len() == 9)
    assert(list1.get_all() == [55, 12, 43, 10, 14, 12, 55, 10, 5])
    assert(list1.len() == 9)
    assert(list1.get_head() == list1.find(55))
    assert(list1.get_tail() == list1.find(5))

    print('delete in head 55:')
    list1.delete(55)
    print(list1.get_all())
    assert(list1.get_all() == [12, 43, 10, 14, 12, 55, 10, 5])
    assert(list1.len() == 8)
    assert(list1.get_head() == list1.find(12))
    assert(list1.get_tail() == list1.find(5))

    print('delete in body 43:')
    list1.delete(43)
    print(list1.get_all())
    assert(list1.get_all() == [12, 10, 14, 12, 55, 10, 5])
    assert(list1.len() == 7)
    assert(list1.get_head() == list1.find(12))
    assert(list1.get_tail() == list1.find(5))

    print('delete in tail 5: ')
    list1.delete(5)
    print(list1.get_all())
    assert(list1.get_all() == [12, 10, 14, 12, 55, 10])
    assert(list1.get_head() == list1.find_all(12)[0])
    assert(list1.get_tail() == list1.find_all(10)[1])

    print('delete wrong data: ')
    list1.delete(77)
    print(list1.get_all())
    assert(list1.get_all() == [12, 10, 14, 12, 55, 10])
    assert(list1.get_head() == list1.find_all(12)[0])
    assert(list1.get_tail() == list1.find_all(10)[1])

    print('delete None: ')
    list1.delete(None)
    print(list1.get_all())
    assert(list1.get_all() == [12, 10, 14, 12, 55, 10])
    assert(list1.len() == 6)
    assert(list1.get_head() == list1.find_all(12)[0])
    assert(list1.get_tail() == list1.find_all(10)[1])

    print('delete in 1-elements list:')
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

    print('delete 5 from clean list: ')
    list1.delete(5)
    print(list1.get_all())
    assert(list1.get_all() == [])
    assert(list1.len() == 0)
    assert(list1.get_head() == None)
    assert(list1.get_tail() == None)


def test_delete_multiple():
    list1 = create_list([55, 7, 12, 43, 10, 14, 12, 55, 10, 5, 5, 55])
    print('\nlist for delete_multiple:\n', list1.get_all())

    print('delete_multiple 55 in head, body and tail: ')
    list1.delete(55, True)
    print(list1.get_all())
    assert(list1.get_all() == [7, 12, 43, 10, 14, 12, 10, 5, 5])
    assert(list1.len() == 9)
    assert(list1.get_head() == list1.find(7))
    assert(list1.get_tail() == list1.find_all(5)[1])

    print('delete_multiple 7 in head: ')
    list1.delete(7, True)
    print(list1.get_all())
    assert(list1.get_all() == [12, 43, 10, 14, 12, 10, 5, 5])
    assert(list1.len() == 8)
    assert(list1.get_head() == list1.find(12))
    assert(list1.get_tail() == list1.find_all(5)[1])

    print('delete_multiple 10 in body: ')
    list1.delete(10, True)
    print(list1.get_all())
    assert(list1.get_all() == [12, 43,  14, 12,  5, 5])
    assert(list1.len() == 6)
    assert(list1.get_head() == list1.find(12))
    assert(list1.get_tail() == list1.find_all(5)[1])

    print('delete_multiple 5 in tail: ')
    list1.delete(5, True)
    print(list1.get_all())
    assert(list1.get_all() == [12, 43,  14, 12])
    assert(list1.len() == 4)
    assert(list1.get_head() == list1.find(12))
    assert(list1.get_tail() == list1.find_all(12)[1])

    print('delete_multiple wrong data 77: ')
    list1.delete(77, True)
    print(list1.get_all())
    assert(list1.get_all() == [12, 43,  14, 12])
    assert(list1.len() == 4)
    assert(list1.get_head() == list1.find(12))
    assert(list1.get_tail() == list1.find_all(12)[1])

    list1 = create_list([5])
    print('delete_multiple 5 in 1-elements list:', list1.get_all())
    list1.delete(5, True)
    print(list1.get_all())
    assert(list1.get_all() == [])
    assert(list1.len() == 0)
    assert(list1.get_head() == None)
    assert(list1.get_tail() == None)

    print('delete_multiple 5 in clear list: ')
    list1.delete(5, True)
    print(list1.get_all())
    assert(list1.get_all() == [])
    assert(list1.len() == 0)
    assert(list1.get_head() == None)
    assert(list1.get_tail() == None)


def test_delete_multiple1():
    list1 = create_list([12, 43,  14, 12, 5, 5])
    print('\ntest_delete_multiple:\n', list1.get_all())

    print('delete_multiple 5 in tail: ')
    list1.delete(5, True)
    print(list1.get_all())
    assert(list1.get_all() == [12, 43,  14, 12])
    assert(list1.len() == 4)
    assert(list1.get_head() == list1.find(12))
    assert(list1.get_tail() == list1.find_all(12)[1])

    list1 = create_list([5, 5])
    print('\ntest_delete_multiple 2:\n', list1.get_all())

    print('delete_multiple 5: ')
    list1.delete(5, True)
    print(list1.get_all())
    assert(list1.get_all() == [])
    assert(list1.len() == 0)
    assert(list1.get_head() == None)
    assert(list1.get_tail() == None)


def test_lists_add():
    test_data1 = [55, 12, 43, 10, 14, 12, 55, 10, 5]
    test_data2 = [55, 12, 43, 10, 14, 12, 55, 10]

    list1 = create_list(test_data1)
    list1_copy = create_list(test_data1)
    list3 = create_list(test_data2)

    assert(lists_add(list1, list3) == False)
    assert(lists_add(LinkedList(), LinkedList()), [])
    assert(lists_add(list1, list1_copy).get_all() == [
           110, 24, 86, 20, 28, 24, 110, 20, 10])


if __name__ == "__main__":
    test_find()
    test_insert()
    test_delete()
    test_delete_multiple()
    test_delete_multiple1()

    test_lists_add()

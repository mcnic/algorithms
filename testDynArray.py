import unittest
from dynArray import DynArray


class TestLinkedList(unittest.TestCase):

    def get_test_dyn_array(self, size):
        dynArray = DynArray()

        for i in range(size):
            dynArray.append(i)
        return dynArray

    def get_array_from_range(self, size):
        ret_array = []
        for i in range(size):
            ret_array.append(i)
        return ret_array

    def test_array16(self):
        dynArray = self.get_test_dyn_array(16)
        self.assertEqual(dynArray.get(), self.get_array_from_range(16))
        self.assertEqual(dynArray.count, 16)
        self.assertEqual(dynArray.capacity, 16)

    def test_add(self):
        dynArray = self.get_test_dyn_array(15)

        dynArray.append(16)
        self.assertEqual(dynArray.count, 16)
        self.assertEqual(dynArray.capacity, 16)

        dynArray.append(17)
        self.assertEqual(dynArray.count, 17)
        self.assertEqual(dynArray.capacity, 32)  # capacity *=2

    def test_insert_wrong(self):
        dynArray = self.get_test_dyn_array(15)

        with self.assertRaises(IndexError):
            dynArray.insert(16, 100)

        with self.assertRaises(IndexError):
            dynArray.insert(-1, 100)

        dynArray.insert(1, None)

    def test_insert_head(self):
        dynArray = self.get_test_dyn_array(15)
        old_capacity = dynArray.capacity

        dynArray.insert(0, 55)
        self.assertEqual(dynArray.get(), [
                         55, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(dynArray.count, 16)
        self.assertEqual(dynArray.capacity, old_capacity)

    def test_insert_head_oversize(self):
        dynArray = self.get_test_dyn_array(16)
        old_capacity = dynArray.capacity

        dynArray.insert(0, 77)
        self.assertEqual(dynArray.get(), [
                         77, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(dynArray.count, 17)
        self.assertEqual(dynArray.capacity, old_capacity*2)

    def test_insert_body(self):
        dynArray = self.get_test_dyn_array(15)
        old_capacity = dynArray.capacity

        dynArray.insert(5, 88)
        self.assertEqual(dynArray.get(), [
                         0, 1, 2, 3, 4, 88, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(dynArray.count, 16)
        self.assertEqual(dynArray.capacity, old_capacity)

    def test_insert_body_oversize(self):
        dynArray = self.get_test_dyn_array(16)
        old_capacity = dynArray.capacity

        dynArray.insert(5, 99)
        self.assertEqual(dynArray.get(), [
                         0, 1, 2, 3, 4, 99, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(dynArray.count, 17)
        self.assertEqual(dynArray.capacity, old_capacity*2)

    def test_insert_tail(self):
        dynArray = self.get_test_dyn_array(15)

        dynArray.insert(dynArray.count, 44)
        self.assertEqual(dynArray.get(), [
                         0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 44])
        self.assertEqual(dynArray.count, 16)
        self.assertEqual(dynArray.capacity, 16)

    def test_insert_tail_oversize(self):
        dynArray = self.get_test_dyn_array(16)

        dynArray.insert(dynArray.count, 33)
        self.assertEqual(dynArray.get(), [
                         0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 33])
        self.assertEqual(dynArray.count, 17)
        self.assertEqual(dynArray.capacity, 32)

    def test_delete_wrong(self):
        dynArray = DynArray()

        with self.assertRaises(IndexError):
            dynArray.delete(0)
        self.assertEqual(dynArray.get(), [])
        self.assertEqual(dynArray.count, 0)
        self.assertEqual(dynArray.capacity, 16)

        dynArray = self.get_test_dyn_array(5)
        with self.assertRaises(IndexError):
            dynArray.delete(-1)
        with self.assertRaises(IndexError):
            dynArray.delete(dynArray.count)

    def test_delete_full(self):
        dynArray = self.get_test_dyn_array(17)

        for i in range(dynArray.count):
            dynArray.delete(0)
        self.assertEqual(dynArray.get(), [])
        self.assertEqual(dynArray.count, 0)
        self.assertEqual(dynArray.capacity, 16)

    def test_delete_head(self):
        dynArray = self.get_test_dyn_array(17)
        old_capacity = dynArray.capacity

        dynArray.delete(0)
        self.assertEqual(dynArray.get(), [
                         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.assertEqual(dynArray.count, 16)
        self.assertEqual(dynArray.capacity, old_capacity)

    def test_delete_head_change_buf(self):
        dynArray = self.get_test_dyn_array(17)
        old_capacity = dynArray.capacity    # 32

        dynArray.delete(0)
        dynArray.delete(0)
        self.assertEqual(dynArray.get(), [
                         2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.assertEqual(dynArray.count, 15)
        self.assertEqual(dynArray.capacity, int(old_capacity // 1.5))

        old_capacity = dynArray.capacity    # 21
        for i in range(5):
            dynArray.delete(0)
        self.assertEqual(dynArray.get(), [
                         7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.assertEqual(dynArray.count, 10)
        self.assertEqual(dynArray.capacity, 16)

    def test_delete_body(self):
        dynArray = self.get_test_dyn_array(15)
        old_capacity = dynArray.capacity

        dynArray.delete(5)
        self.assertEqual(dynArray.get(), [
                         0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(dynArray.count, 14)
        self.assertEqual(dynArray.capacity, old_capacity)

    def test_delete_body_change_buf(self):
        dynArray = self.get_test_dyn_array(17)
        old_capacity = dynArray.capacity

        dynArray.delete(5)
        dynArray.delete(5)
        self.assertEqual(dynArray.get(), [
                         0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.assertEqual(dynArray.count, 15)
        self.assertEqual(dynArray.capacity, int(old_capacity // 1.5))

    def test_delete_tail(self):
        dynArray = self.get_test_dyn_array(15)

        dynArray.delete(dynArray.count-1)
        self.assertEqual(dynArray.get(), [
                         0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        self.assertEqual(dynArray.count, 14)
        self.assertEqual(dynArray.capacity, 16)

    def test_delete_tail_oversize(self):
        dynArray = self.get_test_dyn_array(17)
        old_capacity = dynArray.capacity

        dynArray.delete(dynArray.count-1)
        dynArray.delete(dynArray.count-1)
        self.assertEqual(dynArray.get(), [
                         0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(dynArray.count, 15)
        self.assertEqual(dynArray.capacity, int(old_capacity // 1.5))

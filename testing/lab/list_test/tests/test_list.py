from unittest import TestCase, main

# from project.cat import Cat
# from List.extended_list import IntegerList


class TestIntegerList(TestCase):

    def test_add__when_int__expect_to_add_it(self):
        int_list = IntegerList()
        internal_list = int_list.add(5)
        self.assertEqual([5], internal_list)

    def test_add__when_not_int__expect_exception(self):
        int_list = IntegerList()
        with self.assertRaises(ValueError):
            int_list.add('asd')

    def test_remove_index__when_valid_index__expect_to_remove_and_return_it(self):
        int_list = IntegerList(1, 2, 3, 4)
        result = int_list.remove_index(1)
        self.assertEqual(2, result)
        self.assertListEqual([1, 3, 4], int_list.get_data())

    def test_remove_index__when_not_valid_index__expect_exception(self):
        int_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            int_list.remove_index(4)

    def test_init__when_integers__expect_to_create(self):
        self.assertEqual([1, 2, 3, 4], IntegerList(1, 2, 3, 4).get_data())

    def test_init__when_not_integers__expect_not_to_create(self):
        result = IntegerList('asd')
        self.assertEqual([], result.get_data())

    def test_get__when_valid_index__expect_return_value(self):
        int_list = IntegerList(1, 2, 3, 4)
        self.assertEqual(2, int_list.get(1))

    def test_get__when_not_valid_index__expect_exception(self):
        int_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            int_list.get(4)

    def test_insert__when_not_valid_index__expect_exception(self):
        int_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            int_list.insert(4, 5)

    def test_insert__when_element_not_int__expect_exception(self):
        int_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            int_list.insert(3, 'asd')

    def test_insert__when_valid_element_and_index__expect_to_insert_element(self):
        int_list = IntegerList(1, 2, 3, 4)
        int_list.insert(2, 5)
        self.assertEqual([1, 2, 5, 3, 4], int_list.get_data())

    def test_get_biggest__when_called__expect_biggest_num(self):
        int_list = IntegerList(1, 2, 3, 4)
        result = int_list.get_biggest()
        self.assertEqual(4, result)

    def test_get_index__when_called__expect_element_index(self):
        int_list = IntegerList(1, 2, 3, 4)
        result = int_list.get_index(4)
        self.assertEqual(3, result)


if __name__ == '__main__':
    main()


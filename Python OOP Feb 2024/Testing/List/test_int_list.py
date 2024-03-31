from unittest import TestCase, main


from extended_list import IntegerList


class ListTests(TestCase):
    def setUp(self):
        self.int_list = IntegerList(1.11, 2, 3, 4, "test me")

    def test_init_method_filtering_only_ints(self):
        self.assertEqual([2, 3, 4], self.int_list.get_data())

    def test_add_non_integer_value_to_the_list_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_integer_adds_the_integer_to_the_list(self):
        expected_list = self.int_list.get_data() + [4]

        self.int_list.add(4)

        self.assertEqual(expected_list, self.int_list.get_data())

    def test_remove_method_removing_index_element(self):
        expected_list = [2, 4]
        self.int_list.remove_index(1)
        self.assertEqual(expected_list, self.int_list.get_data())

    def test_remove_method_removing_index_out_of_range_error_throw(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.remove_index(10)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_method_throwing_index_error_if_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.get(3)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_method_index_error_if_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.insert(777, 5)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_method_throw_value_error_if_element_not_int(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.insert(1, "some string")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_get_biggist_method_returning_the_biggest_element(self):
        self.int_list.get_biggest()
        self.assertEqual(4, self.int_list.get_biggest())

    def test_insert_integer_on_valid_index(self):
        expected_list = self.int_list.get_data().copy()

        expected_list.insert(1, 5)
        self.int_list.insert(1, 5)

        self.assertEqual(expected_list, self.int_list.get_data())

    def test_get_index(self):
        result = self.int_list.get_index(3)
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()

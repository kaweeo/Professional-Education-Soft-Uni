from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):

    def setUp(self):
        self.ciela = Bookstore(10)

    def test_init(self):
        self.assertEqual(10, self.ciela.books_limit)
        self.assertEqual({}, self.ciela.availability_in_store_by_book_titles)
        self.assertEqual(0, self.ciela.total_sold_books)

    def test_books_limit(self):
        self.ciela.books_limit = 3
        expected = 3
        actual = self.ciela.books_limit
        self.assertEqual(expected, actual)

    def test_books_limit_setter_raising_error(self):
        with self.assertRaises(ValueError) as ve:
            self.marbella = Bookstore(0)

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test__len_returning_correct_values(self):
        self.ciela.availability_in_store_by_book_titles = {"Pinokio": 3, "RedHat": 5}
        self.assertEqual(8, self.ciela.__len__())

    def test_receive_book_raising_exception_total_books_limit(self):
        self.ciela.availability_in_store_by_book_titles = {"Pinokio": 3, "RedHat": 5}

        with self.assertRaises(Exception) as ex:
            self.ciela.receive_book("Cindarella", 5)

        self.assertEqual(
            "Books limit is reached. Cannot receive more books!",
            str(ex.exception)
        )

    def test_receive_book_if_enough_space(self):
        self.ciela.receive_book("RedHat", 2)
        self.assertEqual({"RedHat": 2}, self.ciela.availability_in_store_by_book_titles)

        self.assertEqual("4 copies of RedHat are available in the bookstore.",
                         self.ciela.receive_book("RedHat", 2))

    def test_sell_book_raising_exception_book_title(self):
        self.ciela.receive_book("RedHat", 2)
        with self.assertRaises(Exception) as ex:
            self.ciela.sell_book("Cindarella", 2)

        self.assertEqual("Book Cindarella doesn't exist!", str(ex.exception))

    def test_sell_book_raising_exeception_not_enough_copies(self):
        self.ciela.receive_book("RedHat", 2)
        with self.assertRaises(Exception) as ex:
            self.ciela.sell_book("RedHat", 3)

        self.assertEqual("RedHat has not enough copies to sell. Left: 2", str(ex.exception))

    def test_sell_book_successfully_v1(self):
        self.ciela.receive_book("RedHat", 4)
        self.assertEqual("Sold 1 copies of RedHat", self.ciela.sell_book("RedHat", 1))
        self.assertEqual(1, self.ciela.total_sold_books)

    def test_sell_book_successfully(self):
        self.ciela.receive_book("heaven", 1)
        expected_return = "Sold 1 copies of heaven"
        actual_return = self.ciela.sell_book("heaven", 1)
        self.assertEqual(expected_return, actual_return)
        expected_sold = 1
        actual_sold = self.ciela.total_sold_books
        self.assertEqual(expected_sold, actual_sold)
        expected_availability = {"heaven": 0}
        actual_availability = self.ciela.availability_in_store_by_book_titles
        self.assertEqual(expected_availability, actual_availability)

    def test___str__(self):
        self.ciela.receive_book("RedHat", 4)
        self.ciela.sell_book("RedHat", 2)
        expected = "Total sold books: 2\nCurrent availability: 2\n - RedHat: 2 copies"
        self.assertEqual(expected, self.ciela.__str__())


if __name__ == "__main__":
    main()

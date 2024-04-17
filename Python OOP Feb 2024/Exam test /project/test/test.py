from project.restaurant import Restaurant
from unittest import TestCase, main


class TestRestaurant(TestCase):

    def setUp(self):
        self.coho = Restaurant("Coho", 5)
        self.coho.add_waiter("John")
        self.coho.add_waiter("Maria")
        self.coho.waiters[0]['total_earnings'] = 100
        self.coho.waiters[1]['total_earnings'] = 200

    def test_correct_init(self):
        self.assertEqual("Coho", self.coho.name)
        self.assertEqual(5, self.coho.capacity)

        expected = [{'name': 'John', 'total_earnings': 100}, {'name': 'Maria', 'total_earnings': 200}]
        self.assertEqual(expected, self.coho.waiters)

    def test_value_error_raised_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            self.mobo = Restaurant(" ", 2)
        self.assertEqual("Invalid name!", str(ve.exception))

    def test_value_error_raised_invalid_capacity(self):
        with self.assertRaises(ValueError) as ve:
            self.mobo = Restaurant("Test", -1)
        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_get_waiters_successfully(self):
        expected = [{'name': 'John', 'total_earnings': 100}, {'name': 'Maria', 'total_earnings': 200}]
        self.assertEqual(expected, self.coho.get_waiters())

    def test_get_waiters_successfully_with_set_values(self):
        expected = [{'name': 'John', 'total_earnings': 100}]
        self.assertEqual(expected, self.coho.get_waiters(50, 150))

        expected = []
        self.assertEqual(expected, self.coho.get_waiters(250, 500))

        self.assertEqual(len(self.coho.get_waiters(max_earnings=150)), 1)
        self.assertEqual(len(self.coho.get_waiters(min_earnings=0)), 2)
        self.assertEqual(len(self.coho.get_waiters(max_earnings=1500)), 2)
        self.assertEqual(len(self.coho.get_waiters(min_earnings=1500)), 0)
        self.assertEqual(len(self.coho.get_waiters(min_earnings=0)), 2)

    def test_add_waiter_successfully(self):
        self.coho.add_waiter("Ana")
        expected = [{'name': 'John', 'total_earnings': 100}, {'name': 'Maria', 'total_earnings': 200}, {'name': 'Ana'}]

        self.assertEqual(expected, self.coho.waiters)
        self.assertEqual(3, len(self.coho.waiters))
        self.assertEqual(self.coho.add_waiter("Mimi"), "The waiter Mimi has been added.")

    def test_add_waiter_raising_errors(self):
        self.coho.capacity = 2
        self.assertEqual("No more places!", self.coho.add_waiter("Ana"))
        self.assertEqual(2, len(self.coho.waiters))

        self.coho.capacity = 5
        expected = f"The waiter John already exists!"
        self.assertEqual(expected, self.coho.add_waiter("John"))
        self.assertEqual(2, len(self.coho.waiters))

    def test_remove_waiter_successfully(self):
        expected = "The waiter John has been removed."
        self.assertEqual(expected, self.coho.remove_waiter("John"))
        self.assertEqual(1, len(self.coho.waiters))

    def test_remove_waiter_no_waiter_found(self):
        expected = "No waiter found with the name Ramirez."
        self.assertEqual(expected, self.coho.remove_waiter("Ramirez"))
        self.assertEqual(2, len(self.coho.waiters))

    def test_get_total_earnings(self):
        self.assertEqual(300, self.coho.get_total_earnings())

        self.mobo = Restaurant("Mobo", 2)
        self.assertEqual(0, self.mobo.get_total_earnings())


if __name__ == "__main__":
    main()

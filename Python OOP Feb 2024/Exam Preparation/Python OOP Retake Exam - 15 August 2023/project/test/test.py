from project.trip import Trip

from unittest import TestCase, main


class TestTrip(TestCase):

    def setUp(self):
        self.vac = Trip(2000, 1, False)
        self.fam_vac = Trip(40000, 4, True)

    def test_class_attribute_dict(self):
        expected_result = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}
        self.assertEqual(expected_result, self.vac.DESTINATION_PRICES_PER_PERSON)

    def test_correct_init(self):
        self.assertEqual(2000, self.vac.budget)
        self.assertEqual(1, self.vac.travelers)
        self.assertEqual(False, self.vac.is_family)
        self.assertEqual({}, self.vac.booked_destinations_paid_amounts)

    def test_incorrect_travelers_value(self):
        with self.assertRaises(ValueError) as ve:
            self.vac_2 = Trip(2000, 0, False)

        expected_value_error = 'At least one traveler is required!'

        self.assertEqual(expected_value_error, str(ve.exception))

    def test_setter_to_set_correct_value_if_incorrect_family_value_must_set_false(self):
        self.vac = Trip(299, 1, True)
        self.assertEqual(False, self.vac.is_family)

    def test_book_a_trip_with_wrong_destination(self):
        expected_result = 'This destination is not in our offers, please choose a new one!'
        self.assertEqual(expected_result, self.vac.book_a_trip("Bali"))

    def test_book_a_trip_with_not_enough_budget(self):
        exp_result = 'Your budget is not enough!'
        self.assertEqual(exp_result, self.vac.book_a_trip('Australia'))

    def test_book_a_trip_successfully_single_trip(self):
        expected_output = f'Successfully booked destination Bulgaria! Your budget left is 1500.00'
        self.assertEqual(expected_output, self.vac.book_a_trip("Bulgaria"))

        self.assertEqual(1500, self.vac.budget)
        self.assertEqual(1, self.vac.travelers)
        self.assertEqual(False, self.vac.is_family)
        self.assertEqual({"Bulgaria": 500}, self.vac.booked_destinations_paid_amounts)

    def test_book_a_trip_successfully_family_trip_w_discount(self):
        expected_output = f'Successfully booked destination New Zealand! Your budget left is 13000.00'
        self.assertEqual(expected_output, self.fam_vac.book_a_trip("New Zealand"))

        self.assertEqual(13000, self.fam_vac.budget)
        self.assertEqual(4, self.fam_vac.travelers)
        self.assertEqual(True, self.fam_vac.is_family)
        self.assertEqual({"New Zealand": 27000}, self.fam_vac.booked_destinations_paid_amounts)

    def test_booking_status_no_bookings_yet(self):
        expected_msg = 'No bookings yet. Budget: 2000.00'
        self.assertEqual(expected_msg, self.vac.booking_status())

    def test_booking_status_with_bookings_sorted(self):
        self.fam_vac.book_a_trip("New Zealand")
        self.fam_vac.book_a_trip("Bulgaria")

        expected_result = 'Booked Destination: Bulgaria\nPaid Amount: 1800.00\n' \
                          'Booked Destination: New Zealand\nPaid Amount: 27000.00\n' \
                          'Number of Travelers: 4\nBudget Left: 11200.00'

        self.assertEqual(expected_result, self.fam_vac.booking_status())




    if __name__ == "__main__":
        main()

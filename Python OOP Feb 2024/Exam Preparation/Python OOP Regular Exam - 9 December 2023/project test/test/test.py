from unittest import TestCase, main
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.shumen = RailwayStation("shumen")
        self.sofia = RailwayStation("sofia")

    def test_correct_init(self):
        self.assertEqual(self.shumen.name, "shumen")
        self.assertEqual(self.shumen.arrival_trains, deque([]))
        self.assertEqual(self.shumen.departure_trains, deque([]))

    def test_validator_of_the_name(self):
        with self.assertRaises(ValueError) as ve:
            self.bu = RailwayStation("bu")
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.bul = RailwayStation("bul")
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_method_with_and_wo_string_parameter(self):
        self.shumen.new_arrival_on_board("")
        self.assertEqual(self.shumen.arrival_trains, deque([""]))
        self.shumen.new_arrival_on_board("a")
        self.assertEqual(self.shumen.arrival_trains, deque(["", "a"]))

    def test_train_has_arrived_method_other_trains_to_arrive(self):
        self.shumen.new_arrival_on_board("")
        self.shumen.new_arrival_on_board("a")
        self.shumen.new_arrival_on_board("b")
        self.shumen.train_has_arrived("b")
        self.assertEqual(self.shumen.train_has_arrived("b"), f"There are other trains to arrive before b.")

    def test_train_has_arrived_method_wo_arrived_train(self):
        with self.assertRaises(IndexError) as ie:
            self.shumen.train_has_arrived("z")
        self.assertEqual("pop from an empty deque", str(ie.exception))

    def test_train_has_arrived_method_w_arrived_train(self):
        self.shumen.new_arrival_on_board("b")
        self.assertEqual(self.shumen.train_has_arrived("b"), f"b is on the platform and will leave in 5 minutes.")

    def test_train_has_left_returning_false(self):
        self.assertFalse(self.shumen.train_has_left("z"))

    def test_train_has_left_returning_false_w_new_on_board(self):
        self.shumen.new_arrival_on_board("a")
        self.assertFalse(self.shumen.train_has_left("z"))

    def test_train_has_left_returning_false_w_other_trains_in_departure_trains(self):
        self.shumen.new_arrival_on_board("a")
        self.shumen.train_has_arrived("a")
        self.assertFalse(self.shumen.train_has_left("z"))

    def test_train_has_left_returning_true(self):
        self.shumen.new_arrival_on_board("a")
        self.shumen.train_has_arrived("a")
        self.assertTrue(self.shumen.train_has_left("a"))

    def test_train_has_left_returning_false_w_more_trains_to_depart(self):
        self.shumen.new_arrival_on_board("a")
        self.shumen.train_has_arrived("a")
        self.shumen.new_arrival_on_board("b")
        self.shumen.train_has_arrived("b")
        self.assertFalse(self.shumen.train_has_left("b"))

    if __name__ == "__main__":
        main()

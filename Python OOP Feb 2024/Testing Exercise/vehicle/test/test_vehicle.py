from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(
            50,
            100
        )

    def test_default_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_init(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)

    def test_drive_method_throwing_correct_ex_and_msg(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(62.3)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_method_working_correctly(self):
        self.vehicle.drive(2)

        self.assertEqual(47.5, self.vehicle.fuel)

    def test_refuel_method_throwing_correct_ex_and_msg(self):
        self.vehicle.fuel = 0
        self.vehicle.capacity = 10

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(11)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_method_working_correctly(self):
        self.vehicle.fuel = 0
        self.vehicle.capacity = 10
        self.vehicle.refuel(9)
        self.assertEqual(9, self.vehicle.fuel)

    def test_str_method_working_correctly(self):
        self.assertEqual(f"The vehicle has {self.vehicle.horse_power} " \
                         f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    main()

from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(50, 200)

    def test_init_expect_correct_attr(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_capacity__when_fuel_is_changed__expect_capacity_remains(self):
        self.assertEqual(50, self.vehicle.capacity)
        self.vehicle.fuel = 20
        self.assertEqual(50, self.vehicle.capacity)

    def test_drive__when_enough_fuel__expect_to_decrease_fuel(self):
        self.vehicle.drive(5)
        self.assertEqual(43.75, self.vehicle.fuel)

    def test_drive__when_not_enough_fuel__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1)
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_refuel__when_fuel_less_then_capacity__expect_fuel_increase(self):
        self.vehicle.drive(5)
        self.assertEqual(43.75, self.vehicle.fuel)
        self.vehicle.refuel(1)
        self.assertEqual(44.75, self.vehicle.fuel)

    def test_refuel__when_fuel_more_then_capacity__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_repr__when_called__expect_correct_str(self):
        self.assertEqual("The vehicle has 200 horse power with 50 fuel left and 1.25 fuel consumption", str(self.vehicle))


if __name__ == 'main':
    main()

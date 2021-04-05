from unittest import TestCase, main

# from CarManager.car_manager import Car


class CarTests(TestCase):
    make = 'Alfa Romeo'
    model = 'GT'
    fuel_consumption = 10
    fuel_capacity = 100

    def setUp(self):
        self.car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_car_init_expect_correct_values(self):
        self.assertEqual(self.make, self.car.make)
        self.assertEqual(self.model, self.car.model)
        self.assertEqual(self.fuel_consumption, self.car.fuel_consumption)
        self.assertEqual(self.fuel_capacity, self.car.fuel_capacity)

    def test_car_make_setter__when_NONE__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.make = None

    def test_car_model_setter__when_NONE__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.model = None

    def test_fuel_consumption_setter__when_0__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = 0

    def test_fuel_consumption_setter__when_negative__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = -1

    def test_fuel_capacity_setter__when_negative__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = -1

    def test_fuel_amount_setter__when_negative__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_amount = -1

    def test_refuel__when_0_given__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.refuel(0)

    def test_refuel__when_negative_given__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_refuel__when_fuel_is_less_then_capacity__expect_fuel_amount_increase(self):
        self.car.refuel(50)
        self.assertEqual(50, self.car.fuel_amount)

    def test_refuel__when_fuel_is_more_then_capacity__expect_fuel_amount_increase(self):
        self.car.refuel(self.fuel_capacity * 2)
        self.assertEqual(self.fuel_capacity, self.car.fuel_amount)

    def test_refuel__when_fuel_is_0__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.refuel(0)

    def test_refuel__when_fuel_is_negative__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.refuel(-1)

    def test_drive__when_enough_fuel__expect_to_drive_and_decreas_fuel_amount(self):
        self.car.refuel(10)
        self.car.drive(100)
        self.assertEqual(0, self.car.fuel_amount)

    def test_drive__when_not_enough_fuel__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.drive(10)


if __name__ == '__main__':
    main()
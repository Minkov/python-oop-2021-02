import unittest

from lab_resources.CarManager.car_manager import Car


class CarTests(unittest.TestCase):
    make = 'make'
    model = 'model'
    fuel_consumption = 10
    fuel_capacity = 100

    def test_car_make_setter__when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.make = None

        self.assertEqual('Make cannot be null or empty!', str(context.exception))

    def test_car_refuel__when_provided_fuel_is_0__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.refuel(0)

    def test_car_refuel__when_provided_fuel_is_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.refuel(-1)

    def test_car_refuel__when_provided_fuel_is_correct__expect_to_increase_fuel_amount_by_provided_fuel(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        fuel = 50
        car.refuel(fuel)
        self.assertEqual(fuel, car.fuel_amount)

    def test_car_refuel__when_provided_fuel_is_more_than_fuel_capacity__expect_to_increase_fuel_amount_to_fuel_capacity(
            self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.refuel(car.fuel_capacity * 2)
        self.assertEqual(car.fuel_capacity, car.fuel_amount)

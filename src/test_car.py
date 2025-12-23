import unittest

from car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("BMW X5", 80)

    def test_refuel_normal(self):
        self.car.refuel(20)
        self.assertEqual(self.car.current_fuel, 20)

    def test_refuel_overfill(self):
        with self.assertRaises(Exception):
            self.car.refuel(90)

    def test_drive_normal(self):
        self.car.refuel(10)
        self.car.drive(50)
        self.assertAlmostEqual(self.car.current_fuel, 6)

    def test_drive_insufficient(self):
        with self.assertRaises(Exception):
            self.car.drive(100)


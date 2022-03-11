import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):

    def test_needs_service(self):
        sensor_values = [0.2, 0, 0.9, 0.5]
        carrigan_tire = CarriganTire(sensor_values)
        self.assertTrue(carrigan_tire.needs_service())

    def test_doesnt_need_service(self):
        sensor_values = [0.2, 0, 0.2, 0.5]
        carrigan_tire = CarriganTire(sensor_values)
        self.assertFalse(carrigan_tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):

    def test_needs_service(self):
        sensor_values = [1, 0.9, 0.2, 1]
        octoprime_tire = OctoprimeTire(sensor_values)
        self.assertTrue(octoprime_tire.needs_service())

    def test_doesnt_need_service(self):
        sensor_values = [0.2, 0, 0.2, 0.5]
        octoprime_tire = OctoprimeTire(sensor_values)
        self.assertFalse(octoprime_tire.needs_service())
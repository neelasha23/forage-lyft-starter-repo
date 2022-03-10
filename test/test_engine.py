import unittest

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):

    def test_needs_service_1(self):
        current_mileage = 30001
        last_service_mileage = 0
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet_engine.needs_service())

    def test_needs_service_2(self):
        current_mileage = 40010
        last_service_mileage = 5000
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet_engine.needs_service())

    def test_doesnt_need_service(self):
        current_mileage = 29987
        last_service_mileage = 0
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet_engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):

    def test_needs_service_1(self):
        current_mileage = 60001
        last_service_mileage = 0
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby_engine.needs_service())

    def test_needs_service_2(self):
        current_mileage = 75000
        last_service_mileage = 10000
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby_engine.needs_service())

    def test_doesnt_need_service(self):
        current_mileage = 50000
        last_service_mileage = 0
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby_engine.needs_service())

class TestSternmanEngine(unittest.TestCase):

    def test_needs_service(self):
        warning_light_is_on = True
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman_engine.needs_service())

    def test_doesnt_need_service(self):
        warning_light_is_on = False
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman_engine.needs_service())


if __name__ == '__main__':
    unittest.main()

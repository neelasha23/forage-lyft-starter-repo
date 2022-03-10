import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):

    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 4)
        nubbin_battery = NubbinBattery(last_service_date, today)
        self.assertTrue(nubbin_battery.needs_service())

    def test_doesnt_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 3)
        nubbin_battery = NubbinBattery(last_service_date, today)
        self.assertFalse(nubbin_battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):

    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 2)
        spindler_battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(spindler_battery.needs_service())

    def test_doesnt_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 1)
        spindler_battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(spindler_battery.needs_service())


if __name__ == '__main__':
    unittest.main()

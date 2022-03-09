import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):

    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 4)
        nubbin_battery = NubbinBattery(last_service_date, today)
        self.assertTrue(nubbin_battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):

    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 4)
        nubbin_battery = NubbinBattery(last_service_date, today)
        self.assertTrue(nubbin_battery.needs_service())


if __name__ == '__main__':
    unittest.main()

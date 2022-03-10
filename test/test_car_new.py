import unittest
from datetime import datetime

from car_factory import CarFactory


class TestCalliope(unittest.TestCase):

    def test_needs_service_engine_battery(self):
        current_mileage = 30001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 2)
        calliope = CarFactory().create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(calliope.needs_service())

    def test_needs_service_engine(self):
        current_mileage = 30001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 1)
        calliope = CarFactory().create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(calliope.needs_service())

    def test_needs_service_battery(self):
        current_mileage = 3001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 2)
        calliope = CarFactory().create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(calliope.needs_service())

    def test_doesnt_need_service(self):
        current_mileage = 3001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 1)
        calliope = CarFactory().create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(calliope.needs_service())

class TestGlissade(unittest.TestCase):

    def test_needs_service_engine_battery(self):
        current_mileage = 60001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 2)
        glissade = CarFactory().create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(glissade.needs_service())

    def test_needs_service_engine(self):
        current_mileage = 60001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 1)
        glissade = CarFactory().create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(glissade.needs_service())

    def test_needs_service_battery(self):
        current_mileage = 6001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 2)
        glissade = CarFactory().create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(glissade.needs_service())

    def test_doesnt_need_service(self):
        current_mileage = 3001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 1)
        glissade = CarFactory().create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(glissade.needs_service())

class TestPalindrome(unittest.TestCase):

    def test_needs_service_engine_battery(self):
        warning_light_is_on = True
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 2)
        palindrome = CarFactory().create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(palindrome.needs_service())

    def test_needs_service_engine(self):
        warning_light_is_on = True
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 1)
        palindrome = CarFactory().create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(palindrome.needs_service())

    def test_needs_service_battery(self):
        warning_light_is_on = False
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 2)
        palindrome = CarFactory().create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(palindrome.needs_service())

    def test_doesnt_need_service(self):
        warning_light_is_on = False
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 1)
        palindrome = CarFactory().create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(palindrome.needs_service())

class TestRorschach(unittest.TestCase):

    def test_needs_service_engine_battery(self):
        current_mileage = 60001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 4)
        rorschach = CarFactory().create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(rorschach.needs_service())

    def test_needs_service_engine(self):
        current_mileage = 60001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 3)
        rorschach = CarFactory().create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(rorschach.needs_service())

    def test_needs_service_battery(self):
        current_mileage = 6001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 4)
        rorschach = CarFactory().create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(rorschach.needs_service())

    def test_doesnt_need_service(self):
        current_mileage = 3001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 1)
        rorschach = CarFactory().create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(rorschach.needs_service())

class TestThovex(unittest.TestCase):

    def test_needs_service_engine_battery(self):
        current_mileage = 30001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 4)
        thovex = CarFactory().create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(thovex.needs_service())

    def test_needs_service_engine(self):
        current_mileage = 30001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 3)
        thovex = CarFactory().create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(thovex.needs_service())

    def test_needs_service_battery(self):
        current_mileage = 3001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 4)
        thovex = CarFactory().create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(thovex.needs_service())

    def test_doesnt_need_service(self):
        current_mileage = 3001
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 1)
        thovex = CarFactory().create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(thovex.needs_service())


if __name__ == '__main__':
    unittest.main()

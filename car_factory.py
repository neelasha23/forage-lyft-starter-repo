from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, Tire, wear_values):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = Tire(wear_values)
        return Car(engine, battery, tire)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, Tire, wear_values):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = Tire(wear_values)
        return Car(engine, battery, tire)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, Tire, wear_values):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = Tire(wear_values)
        return Car(engine, battery, tire)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, Tire, wear_values):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = Tire(wear_values)
        return Car(engine, battery, tire)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, Tire, wear_values):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = Tire(wear_values)
        return Car(engine, battery, tire)
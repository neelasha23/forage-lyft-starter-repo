from .tire import Tire


class OctoprimeTire(Tire):

    def __init__(self, tire_wear_values):
        self.tire_wear_values = tire_wear_values

    def needs_service(self):
        return sum(self.tire_wear_values) >= 3

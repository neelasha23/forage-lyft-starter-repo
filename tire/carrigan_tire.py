from .tire import Tire


class CarriganTire(Tire):

    def __init__(self, tire_wear_values):
        self.tire_wear_values = tire_wear_values

    def needs_service(self):
        return any(val==0.9 for val in self.tire_wear_values)

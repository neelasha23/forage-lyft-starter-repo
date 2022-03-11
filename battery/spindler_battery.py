from datetime import datetime
from .battery import Battery


class SpindlerBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        next_service_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if self.current_date >= next_service_date:
            return True
        else:
            return False

from batteries.spindler import Spindler
from cars.car import Car
from engines.willoughby import Willoughby
from datetime import date

class Glissade(Car):
   def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
       super().__init__("Glissade", {"engine": Willoughby(), "battery": Spindler()}, current_mileage, last_service_mileage, last_service_date)
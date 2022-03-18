from batteries.spindler import Spindler
from cars.car import Car
from engines.capulet import Capulet
from datetime import date

class Calliope(Car):
   def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
       super().__init__("Calliope", {"engine": Capulet(), "battery": Spindler()}, current_mileage, last_service_mileage, last_service_date)
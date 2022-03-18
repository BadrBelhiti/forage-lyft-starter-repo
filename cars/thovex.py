from batteries.nubbin import Nubbin
from cars.car import Car
from engines.capulet import Capulet
from datetime import date

from tires.octoprime import Octoprime

class Thovex(Car):
   def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
       super().__init__("Thovex", {"engine": Capulet(), "battery": Nubbin(), "tires": Octoprime()}, current_mileage, last_service_mileage, last_service_date)
from batteries.nubbin import Nubbin
from cars.car import Car
from engines.willoughby import Willoughby
from datetime import date
from tires.carrigan import Carrigan

class Rorschach(Car):
   def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
       super().__init__("Rorschach", {"engine": Willoughby(), "battery": Nubbin(), "tires": Carrigan()}, current_mileage, last_service_mileage, last_service_date)
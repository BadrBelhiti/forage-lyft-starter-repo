from batteries.spindler import Spindler
from cars.car import Car
from engines.sternman import Sternman
from datetime import date

from tires.carrigan import Carrigan

class Palindrome(Car):
   def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
       super().__init__("Palindrome", {"engine": Sternman(), "battery": Spindler(), "tires": Carrigan()}, current_mileage, last_service_mileage, last_service_date)
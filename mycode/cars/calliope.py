from mycode.cars import Car
from mycode.service.criteria import ServiceCriteria

class Calliope(Car):
   def __init__(self):
       super().__init__("Calliope", ServiceCriteria())
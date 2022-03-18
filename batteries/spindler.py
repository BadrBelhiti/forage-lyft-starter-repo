from components.servicables import Battery
from service.criteria import ServiceCriteria
from service.types import ServiceType

class Spindler(Battery):
    def __init__(self):
        super().__init__("Spindler", ServiceCriteria(ServiceType.TIME, interval=3))
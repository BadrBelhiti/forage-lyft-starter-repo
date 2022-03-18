from components.servicables import Battery
from service.criteria import ServiceCriteria
from service.types import ServiceType

class Nubbin(Battery):
    def __init__(self):
        super().__init__("Nubbin", ServiceCriteria(ServiceType.TIME, interval=4))
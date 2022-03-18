from components.servicables import Tires
from service.criteria import ServiceCriteria
from service.types import ServiceType

class Octoprime(Tires):
    def __init__(self):
        super().__init__("Octoprime", ServiceCriteria(ServiceType.SUM_ARRAY, threshold=3))
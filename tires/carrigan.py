from components.servicables import Tires
from service.criteria import ServiceCriteria
from service.types import ServiceType

class Carrigan(Tires):
    def __init__(self):
        super().__init__("Carrigan", ServiceCriteria(ServiceType.MAX_ARRAY, threshold=0.9))
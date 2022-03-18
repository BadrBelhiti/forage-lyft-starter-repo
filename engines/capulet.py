from components.servicables import Engine
from service.criteria import ServiceCriteria
from service.types import ServiceType

class Capulet(Engine):
    def __init__(self):
        super().__init__("Capulet", ServiceCriteria(ServiceType.MILES, 30_000))
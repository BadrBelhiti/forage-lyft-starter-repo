from components.servicables import Engine
from service.criteria import ServiceCriteria
from service.types import ServiceType

class Sternman(Engine):
    def __init__(self):
        super().__init__("Sternman", ServiceCriteria(ServiceType.LIGHT, ["engine"]))
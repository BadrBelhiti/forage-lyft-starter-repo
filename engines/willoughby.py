from components.servicables import Engine
from service.criteria import ServiceCriteria
from service.types import ServiceType

class Willoughby(Engine):
    def __init__(self):
        super().__init__("Willoughby", ServiceCriteria(ServiceType.MILES, interval=60_000))
from mycode.service.types import ServiceType

from typing import List

class ServiceCriteria():
    def __init__(self, criteria_type: ServiceType, interval: int = 0, lights_needed: List[str] = []):
        self.criteria_type = criteria_type
        self.interval = interval
        self.lights_needed = lights_needed

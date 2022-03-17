from typing import Dict

from mycode.service.criteria import ServiceCriteria
from mycode.service.types import ServiceType

class Servicable():
    def __init__(self, name: str, service_criteria: ServiceCriteria):
        self.name = name
        self.service_criteria = service_criteria
        self.last_service_miles = 0
        self.last_service_date = 0

    def service(self, miles: int, date: int) -> None:
        self.last_service_miles = miles
        self.last_service_date = date

    def needs_service(self, current_miles: int, current_date: int, warning_lights: Dict[str, bool]) -> bool:
        # Check if service is dependent on warning lights
        if self.service_criteria == ServiceType.LIGHT:
            # Check if the warning lights currently on warrant a service
            for light in self.service_criteria.lights_needed:
                if warning_lights[light]:
                    return True

        # Service is dependent upon mileage
        elif self.service_criteria == ServiceType.MILES:
            return current_miles - self.last_service_miles >= self.service_criteria.interval
            
        # Service is dependent upon time
        elif self.service_criteria == ServiceType.TIME:
            return current_date - self.last_service_date >= self.service_criteria.interval
            

class Engine(Servicable):
    def __init__(self, name, service_criteria):
        super().__init__(name, service_criteria)

class Battery(Servicable):
    def __init__(self, name, service_criteria):
        super().__init__(name, service_criteria)
from typing import Dict, List

from service.criteria import ServiceCriteria
from service.types import ServiceType
from datetime import date

class Servicable:
    def __init__(self, name: str, service_criteria: ServiceCriteria):
        self.name = name
        self.service_criteria = service_criteria

    def service(self, miles: int, date: date) -> None:
        self.last_service_miles = miles
        self.last_service_date = date

    def needs_service(self, current_miles: int, current_date: date, warning_lights: Dict[str, bool]) -> bool:
        # Check if service is dependent on warning lights
        if self.service_criteria.criteria_type == ServiceType.LIGHT:
            # Check if the warning lights currently on warrant a service
            for light in self.service_criteria.lights_needed:
                if warning_lights[light]:
                    return True

        # Service is dependent upon mileage
        elif self.service_criteria.criteria_type == ServiceType.MILES:
            return current_miles - self.last_service_miles > self.service_criteria.interval

        # Service is dependent upon time
        elif self.service_criteria.criteria_type == ServiceType.TIME:
            return current_date.replace(year=current_date.year - self.service_criteria.interval) > self.last_service_date
            

class Engine(Servicable):
    def __init__(self, name, service_criteria):
        super().__init__(name, service_criteria)

class Battery(Servicable):
    def __init__(self, name, service_criteria):
        super().__init__(name, service_criteria)

class Tires(Servicable):
    def __init__(self, name, service_criteria):
        super().__init__(name, service_criteria)
        self.wear = [0] * 4

    def get_wear(self) -> List[float]:
        return self.wear

    def set_wear(self, wear: List[float]) -> None:
        self.wear = wear

    def needs_service(self, current_miles: int, current_date: date, warning_lights: Dict[str, bool]) -> bool:
        # Service is dependent upon max of wear array
        if self.service_criteria.criteria_type == ServiceType.MAX_ARRAY:
            return max(self.wear) > self.service_criteria.threshold

        # Service is dependent upon sum of wear array
        elif self.service_criteria.criteria_type == ServiceType.SUM_ARRAY:
            return sum(self.wear) > self.service_criteria.threshold
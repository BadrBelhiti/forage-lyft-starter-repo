from typing import Dict, List
from datetime import datetime, date

from components.servicables import Servicable

class Car:
    def __init__(self, name: str, components: Dict[str, Servicable], current_miles: int, last_service_miles: int, last_service_date: date):
        self._name = name
        self._components = components
        self._warning_lights = {}
        self._miles = current_miles
        self._last_service_miles = last_service_miles
        self._last_service_date = last_service_date

        for component in components.values():
            component.service(self._last_service_miles, self._last_service_date)

    def needs_service(self) -> bool:
        return len(self.get_servicing_needed()) != 0

    def get_servicing_needed(self) -> List[Servicable]:
        servicing_needed: List[Servicable] = []

        # Iterate through all components and check if they need to be serviced
        for component in self._components.values():
            if component.needs_service(self._miles, datetime.today().date(), self._warning_lights):
                servicing_needed.append(component)

        return servicing_needed

    def set_warning_light(self, light: str, on: bool) -> None:
        self._warning_lights[light] = on

    def replace_components(self, component_type: str, component: Servicable) -> None:
        self._components[component_type] = component

    def get_miles(self) -> int:
        return self._miles

    def set_miles(self, miles: int) -> None:
        self._miles = miles
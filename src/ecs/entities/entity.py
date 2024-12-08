# Imma try to make an ECS...
# Fuck this might be hard
from typing import Type
from ecs.components.component import Component
from ecs.systems.system import System


class Entity:
    def __init__(self, components: dict[Type, Component] = {}, systems: dict[Type, System] = {}) -> None:
        self.components: dict[Type, Component] = components
        self.systems = systems

    def get_component(self, component: Type) -> None:
        return self.components.get(component)

    def add_component(self, component) -> None:
        self.components[type(component)] = component

    def get_system(self, system: Type) -> None:
        return self.systems.get(system)

    def add_system(self, system) -> None:
        self.systems[type(system)] = system

    def update(self) -> None:
        for system in self.systems.values():
            system.apply()

    def draw(self) -> None: ...

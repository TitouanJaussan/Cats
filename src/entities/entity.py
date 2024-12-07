# Imma try to make an ECS...
# Fuck this might be hard
from entities.components.component import Component

class Entity:
    def __init__(self, components) -> None:
        self.components: dict[str, Component] = components
    
    def get_component(self, component_name: str) -> None:
        return self.components.get(component_name)
    
    def add_component(self, component, name: str) -> None:
        self.components[name] = component
    
    def update(self) -> None: ...
    def draw(self)   -> None: ...
from typing import Any


class Component:
    """
    A 'template' for the components of the ECS. Not usable directly
    """
    def __init__(self, entity) -> None:
        self.entity = entity
    
    def get_data(self) -> Any: ...
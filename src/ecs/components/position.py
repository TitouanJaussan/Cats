from utils.vector2 import Vector2
from ecs.components.component import Component


class PositionComponent(Component):
    def __init__(self, entity, position: Vector2 = Vector2()) -> None:
        super().__init__(entity)
        self._position = position

    def get_data(self) -> Vector2:
        return self._position

    def set_data(self, new_pos: Vector2) -> None:
        if not isinstance(new_pos, Vector2):
            raise TypeError

        self._position = new_pos

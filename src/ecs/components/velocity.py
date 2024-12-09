from utils.vector2 import Vector2
from ecs.components.component import Component


class VelocityComponent(Component):
    def __init__(self, entity, velocity: Vector2 = Vector2()) -> None:
        super().__init__(entity)
        self._velocity = velocity

    def get_data(self) -> Vector2:
        return self._velocity

    def set_data(self, new_vel: Vector2) -> None:
        if not isinstance(new_vel, Vector2):
            raise TypeError

        self._velocity = new_vel

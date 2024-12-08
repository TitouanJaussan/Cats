import pygame as pg
from utils.vector2 import Vector2
from ecs.systems.system import System
from ecs.components.position import PositionComponent


class KeyboardControllerSystem(System):
    def __init__(self, entity) -> None:
        super().__init__(entity, [PositionComponent])

    def apply(self):
        keys = pg.key.get_pressed()
        pos_comp: PositionComponent = self.entity.get_component(
            PositionComponent)

        pos = pos_comp.get_data()

        if keys[pg.K_LEFT]:
            pos += Vector2(-1, 0)
        if keys[pg.K_RIGHT]:
            pos += Vector2(1, 0)
        if keys[pg.K_UP]:
            pos += Vector2(0, -1)
        if keys[pg.K_DOWN]:
            pos += Vector2(0, 1)

        pos_comp.set_data(pos)

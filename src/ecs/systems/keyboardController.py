import pygame as pg
from utils.vector2 import Vector2
from ecs.systems.system import System
from ecs.components.position import PositionComponent
from ecs.components.velocity import VelocityComponent


class KeyboardControllerSystem(System):
    def __init__(self, entity) -> None:
        super().__init__(entity, [PositionComponent, VelocityComponent])

    def apply(self):
        if not self._check_for_required_components():
            raise Exception("Could not find all required components")
        keys = pg.key.get_pressed()

        vel_component: VelocityComponent = self.entity.get_component(
            VelocityComponent)
        pos_component: PositionComponent = self.entity.get_component(
            PositionComponent)

        vel = vel_component.get_data()
        pos = pos_component.get_data()
        dt = self.entity.app.dt
        speed = 60

        if keys[pg.K_LEFT]:
            vel += Vector2(-speed, 0) * dt * 60
        if keys[pg.K_RIGHT]:
            vel += Vector2(speed, 0) * dt * 60
        if keys[pg.K_UP]:
            vel += Vector2(0, -speed) * dt * 60
        if keys[pg.K_DOWN]:
            vel += Vector2(0, speed) * dt * 60

        vel += (vel * -dt * 10)

        pos += vel.as_int() * dt

        vel_component.set_data(vel.copy())
        pos_component.set_data(pos)

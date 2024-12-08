import pygame as pg
from utils.vector2 import Vector2
from ui.menu.menu import Menu
from game.tile_engine.tileEngine import TileEngine
from ecs.entities.entity import Entity
from ecs.components.position import PositionComponent
from ecs.systems.keyboardController import KeyboardControllerSystem


class MainGameMenu(Menu):
    def __init__(self, menu_manager) -> None:
        super().__init__(menu_manager)
        self.tile_engine = TileEngine(self.menu_manager.app, Vector2(2, 2))

        self.player = Entity()
        self.player.add_component(PositionComponent(self.player))
        self.player.add_system(KeyboardControllerSystem(self.player))

    def update(self) -> None:
        self.player.update()

    def draw(self) -> None:
        self.tile_engine.draw()
        pg.draw.rect(self.menu_manager.app.window, (255, 255, 255),
                     (*self.player.get_component(PositionComponent).get_data(), 10, 10))

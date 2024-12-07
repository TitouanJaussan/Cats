from utils.vector2 import Vector2
from ui.menu.menu import Menu
from game.tile_engine.tileEngine import TileEngine

class MainGameMenu(Menu):
    def __init__(self, menu_manager) -> None:
        super().__init__(menu_manager)
        self.tile_engine = TileEngine(self.menu_manager.app, Vector2(2, 2))
    
    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.tile_engine.draw()
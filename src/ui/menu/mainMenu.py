import pygame as pg
from ui.menu.menu import Menu
from ui.widgets.button import Button
from utils.vector2 import Vector2


class MainMenu(Menu):
    def __init__(self, menu_manager) -> None:
        super().__init__(menu_manager)
        self.add_widget("button", Button(self, Vector2(5, 5), Vector2(10, 5)))
    
    def update(self) -> None:
        self._update_widgets()

    def draw(self) -> None:
        self._draw_widgets()
import pygame as pg
from typing import Callable, Any
from ui.widgets.widget import Widget
from utils.vector2 import Vector2
from utils.hitbox import Hitbox


class Button(Widget):
    def __init__(self, menu, position: Vector2, size: Vector2, callback=None, callback_args: tuple = tuple(), callback_kwargs: dict[str, Any] = {}) -> None:
        super().__init__(menu)

        self.pos = position
        self.size = size
        self.color = (255, 0, 255)
        self.hitbox = Hitbox(position, size)

        self.callback: Callable = callback
        self.callback_args = callback_args
        self.callback_kwargs = callback_kwargs

    def draw(self) -> None:
        pg.draw.rect(self.menu.canvas, self.color, self.hitbox.get_rect())

    def on_click(self) -> None:
        if self.callback != None:
            self.callback(*self.callback_args, **self.callback_kwargs)

    def update(self) -> None:
        if self.hitbox.point_collision(Vector2().mouse_pos()) and pg.mouse.get_pressed()[0]:
            self.on_click()

    def is_focused(self) -> bool:
        return self.hitbox.point_collision(Vector2().mouse_pos())

import pygame as pg
from utils.vector2 import Vector2

class Tile:
    def __init__(self, tex_name, texture: pg.Surface, position: Vector2) -> None:
        self.texture_name = tex_name
        self.texture = texture
        self.position = position
    
    def draw(self, surf: pg.Surface) -> None:
        surf.blit(self.texture, tuple(self.position))
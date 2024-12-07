from utils.vector2 import Vector2
from game.tile_engine.tile import Tile

class TileEngine:
    def __init__(self, app, world_size: Vector2) -> None:
        self.app = app

        self.tiles: list[list[Tile]] = self._make_blank_world()
    
    def _make_blank_world(self) -> list[list[Tile]]:
        return [[Tile() for y in range()] for x in range()]
    
    def update(self) -> None:
        pass

    def draw(self) -> None:
        pass
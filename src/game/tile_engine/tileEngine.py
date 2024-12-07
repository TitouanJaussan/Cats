from utils.vector2 import Vector2
from game.tile_engine.tile import Tile
from game.tile_engine.tileResourceManager import TileResourceManager
from core.logger import Logger

class TileEngine:
    def __init__(self, app, world_size: Vector2) -> None:
        self.app = app
        self.world_size = world_size
        self.logger = Logger("Tile Engine")
        self.resource_manager = TileResourceManager("assets/textures/tiles", self.app.path_manager)

        self.tiles: list[list[Tile]] = self._make_blank_world()

    def _make_blank_world(self) -> list[list[Tile]]:
        world = []

        for x in range(self.world_size.x):
            world.append([])
            for y in range(self.world_size.y):
                name = list(self.resource_manager.textures.keys())[0]
                tex = self.resource_manager.query_texture(name)
                world[x].append(Tile(name, tex, Vector2(x * 16, y * 16)))
        
        return world
    
    def update(self) -> None:
        pass

    def draw(self) -> None:
        for x in range(self.world_size.x):
            for y in range(self.world_size.y):
                self.tiles[x][y].draw(self.app.window)
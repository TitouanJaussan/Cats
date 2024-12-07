import pygame as pg
from os import listdir
from os.path import isfile
from core.logger import Logger
from utils.pathManager import PathManager

class TileResourceManager:
    def __init__(self, tiles_path: str, path_manager: PathManager) -> None:
        self.path = tiles_path
        self.path_manager = path_manager
        self.logger = Logger("Tile Resource Manager")

        self.textures: dict[str, pg.Surface] = {}

        self._load_resources()
    
    def _list_images(self) -> None:
        all_pngs = []

        for file in listdir(self.path):
            if isfile(self.path + self.path_manager.separator + file) and self.path_manager.matches_extension(file, "png"):
                all_pngs.append(self.path_manager.remove_extension(file, "png"))
        
        return all_pngs
    
    def _load_resources(self) -> None:
        images = self._list_images()

        for image_name in images:
            image = pg.image.load(self.path_manager.concatenate(self.path, image_name + ".png"))
            self.textures[image_name] = image

        self.logger.log(self.textures)

    def query_texture(self, tex_name: str) -> pg.Surface | None:
        return self.textures.get(tex_name)
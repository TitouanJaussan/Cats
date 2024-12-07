from sys import exit as sys_exit
from time import time
import pygame as pg
from core.logger import Logger
from core.settingsManager import SettingsManager
from ui.menuManager import MenuManager
from ui.menu.mainMenu import MainMenu
from ui.menu.mainGameMenu import MainGameMenu
from utils.pathManager import PathManager

class KittyGameEngine:
    def __init__(self, main_file) -> None:
        self.path_manager = PathManager(main_file)
        self.logger = Logger(f"Kitty Engine")
        self.logger.log("Launching engine")
        self.logger.log(f"Detected OS: {self.path_manager.os}")
        self.logger.log(f"Loading game at path: {self.path_manager.path}")

        self.pixel_size = 6
        self.window = pg.display.set_mode((1920 // self.pixel_size, 1080 // self.pixel_size), flags=pg.FULLSCREEN | pg.SCALED)
        self.clock = pg.time.Clock()

        self.settings = SettingsManager("game_settings.json")
        self.framerate = self.settings.read_setting("graphics.targetFPS")
        self.menu_manager = MenuManager(self)

        self.menu_manager.add_menu(MainMenu(self.menu_manager))
        self.menu_manager.add_menu(MainGameMenu(self.menu_manager))

        self.menu_manager.switch_menu("maingame")

        # dt
        self.last_time = time()
        self.dt = 0
    
    def _handle_default_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._close_game()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self._close_game()
    
    def _close_game(self) -> None:
        self.logger.log("Closing game")
        self.settings.save_settings()
        pg.quit()
        sys_exit()
    
    def launch(self) -> None:
        self.logger.log("Launching game")
        self._run()
    
    def update_time(self) -> None:
        self.dt = time() - self.last_time
        self.last_time = time()
    
    def update(self) -> None:
        self.menu_manager.update()

    def render(self) -> None:
        self.window.fill((0, 0, 0))
       
        self.menu_manager.draw()

        pg.display.update()

    def _run(self) -> None:
        while True:
            self._handle_default_events()
            self.update()
            self.render()
            self.clock.tick(self.framerate)
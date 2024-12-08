from ui.menu.menu import Menu
from core.logger import Logger


class MenuManager:
    def __init__(self, app) -> None:
        self.app = app
        self.menus: dict[str, Menu] = {}
        self.current_menu = ""
        self.logger = Logger("Menu Manager")

    def add_menu(self, menu: Menu) -> None:
        menu_name = menu.__class__.__name__[
            0:menu.__class__.__name__.index("Menu")].lower()

        if self.menus.get(menu_name) != None:
            self.logger.warning(
                f"Overriding already existing menu: {menu_name}")

        if self.current_menu == "":
            self.current_menu = menu_name

        self.menus[menu_name] = menu

    def switch_menu(self, new_menu: str) -> None:
        if self.menus.get(new_menu) == None:
            self.logger.error(f"Switching to unexisting menu: {new_menu}")
            exit()

        self.current_menu = new_menu

    def update(self) -> None:
        self.menus[self.current_menu].update()

    def draw(self) -> None:
        self.menus[self.current_menu].draw()

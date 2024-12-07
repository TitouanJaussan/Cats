from ui.widgets.widget import Widget
from utils.hitbox import Hitbox


class Menu:
    def __init__(self, menu_manager) -> None:
        self.menu_manager = menu_manager
        self.app = self.menu_manager.app
        self.canvas = self.app.window
        self.widgets: dict[str, Widget] = {}
    
    def add_widget(self, widget_name: str, widget: Widget) -> None:
        self.widgets[widget_name] = widget
    
    def _update_widgets(self) -> None:
        for widget in self.widgets.values():
            widget.update()
    
    def _draw_widgets(self) -> None:
        for widget in self.widgets.values():
            widget.draw()

    def update(self) -> None: ...
    def draw(self)   -> None: ...
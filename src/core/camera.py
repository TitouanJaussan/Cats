from utils.vector2 import Vector2

class Camera:
    def __init__(self, app, position: Vector2 = Vector2()):
        self.app = app
        self.position = position
    
    def update(self) -> None:
        pass
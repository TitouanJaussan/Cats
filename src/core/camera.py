from utils.vector2 import Vector2

class Camera:
    def __init__(self, app, position: Vector2 = Vector2()):
        self.position = position
        self.app = app
    
    def update(self) -> None:
        pass
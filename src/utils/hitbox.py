from utils.vector2 import Vector2


class Hitbox:
    def __init__(self, pos: Vector2, size: Vector2) -> None:
        assert type(pos) == Vector2
        assert type(size) == Vector2

        self.pos = pos
        self.size = size

    def point_collision(self, p: Vector2) -> bool:
        return (p.x >= self.pos.x) and (p.y >= self.pos.y) and (p.x < self.pos.x + self.size.x) and (p.y < self.pos.y + self.size.y)

    def get_rect(self) -> tuple[int | float, int | float, int | float, int | float]:
        return (*self.pos, *self.size)

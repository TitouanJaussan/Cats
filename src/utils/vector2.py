import pygame as pg
from math import sqrt


class Vector2:
    def __init__(self, x: int  | float = 0.0, y: int | float = 0.0):
        self._x = 0
        self._y = 0
        self.length = 0

        self.x = x
        self.y = y

    def _length(self) -> None:
        return sqrt(self._x ** 2 + self._y ** 2)
    
    def _get_x(self) -> int | float:
        return self._x
    
    def _set_x(self, new_x: int | float) -> None:
        if type(new_x) != int and type(new_x) != float:
            raise TypeError(f"Can't set x to a {type(new_x)}")
        
        self._x = new_x
        self.length = self._length()
    
    def _get_y(self) -> int | float:
        return self._y
    
    def _set_y(self, new_y: int | float) -> None:
        if type(new_y) != int and type(new_y) != float:
            raise TypeError(f"Can't set y to a {type(new_y)}")
        
        self._y = new_y
        self.length = self._length()
    
    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)

    def mouse_pos(self):
        return Vector2(*pg.mouse.get_pos())

    # Operators

    def copy(self):
        return Vector2(self._x, self._y)

    def __add__(self, other):
        out = self.copy()

        match other:
            case int() | float():
                out.x += other
                out.y += other
            
            case Vector2():
                out.x += other.x
                out.y += other.y
            
            case _:
                raise TypeError
        
        return out
    
    def __sub__(self, other):
        out = self.copy()

        match other:
            case int() | float():
                out.x -= other
                out.y -= other
            
            case Vector2():
                out.x -= other.x
                out.y -= other.y
            
            case _:
                raise TypeError
        
        return out
    
    def __mul__(self, other):
        out = self.copy()

        match other:
            case int() | float():
                out.x *= other
                out.y *= other
            
            case Vector2():
                out.x *= other.x
                out.y *= other.y
            
            case _:
                raise TypeError
        
        return out
    
    def __div__(self, other):
        out = self.copy()

        match other:
            case int() | float():
                out.x /= other
                out.y /= other
            
            case Vector2():
                out.x /= other.x
                out.y /= other.y

            case _:
                raise TypeError
        
        return out
    
    def __pow__(self, other):
        out = self.copy()

        match other:
            case int() | float():
                out.x **= other
                out.y **= other
            
            case Vector2():
                out.x **= other.x
                out.y **= other.y

            case _:
                raise TypeError
        
        return out
    
    def __iter__(self) -> None:
        yield self._x
        yield self._y
    
    def __repr__(self) -> str:
        return f"Vector2 x: {self.x} y: {self.y}"
    
    def __str__(self) -> str:
        return self.__repr__()
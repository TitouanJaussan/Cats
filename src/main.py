import sys; sys.dont_write_bytecode = True
from core.gameEngine import KittyGameEngine
from platform import system
import os

if __name__ == "__main__":
    game = KittyGameEngine(__file__)
    game.launch()
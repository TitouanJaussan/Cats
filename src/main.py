import sys; sys.dont_write_bytecode = True
from core.gameEngine import KittyGameEngine
import os

if __name__ == "__main__":
    path = os.path.abspath(__file__)
    path = "/".join(path.split("/")[:-2])
    os.chdir(path)

    game = KittyGameEngine(path)
    game.launch()
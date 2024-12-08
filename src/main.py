from core.gameEngine import KittyGameEngine

# Please run the project with python -B main.py
# Don't forget '-B' or else there will be a lot of __pycache__

if __name__ == "__main__":
    game = KittyGameEngine(__file__)
    game.launch()

from src.classes.SceneManager import Scene
from src.game.Terrain import Terrain

# TODO: Make the width and height a variable
terrain = Terrain(1280, 800)


def draw(canvas):
    terrain.draw(canvas)


main = Scene("main", draw)

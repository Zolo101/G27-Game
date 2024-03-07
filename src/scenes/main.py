from src.classes.SceneManager import Scene
from src.game.Sky import Sky
from src.game.Terrain import Terrain

# TODO: Make the width and height a variable
terrain = Terrain(1280, 800)
sky = Sky()


def draw(canvas, clock, frame):
    sky.draw(canvas, clock, frame)
    terrain.draw(canvas)


main = Scene("main", draw)

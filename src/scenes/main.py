from src.classes.SceneManager import Scene
from src.game.Player import Player
from src.game.Sky import Sky
from src.game.Terrain import Terrain
from src.game.Zombie import Zombie

# TODO: Make the width and height a variable
terrain = Terrain(1280, 800)
sky = Sky()
player = Player(600, 400)
zombie = Zombie(200, 400, player,sky)


def draw(canvas, clock, frame, interaction):
    sky.draw(canvas, clock, frame)
    terrain.draw(canvas)
    zombie.draw(canvas)
    player.update(interaction)
    zombie.update()
    player.draw(canvas)


main = Scene("main", draw)

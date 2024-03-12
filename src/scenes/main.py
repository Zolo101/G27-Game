from src.classes.SceneManager import Scene
from src.game.Player import Player
from src.game.Sky import Sky
from src.game.Terrain import Terrain
from src.game.Zombie import Zombie
from src.classes.Clock import Clock

# TODO: Make the width and height a variable
terrain = Terrain(1280, 800)
sky = Sky()
player = Player(600, 400)
zombie = Zombie(600, 400, player)

global timer
timer = 0

zombies = []
clock = Clock()
def draw(canvas, clock, frame, interaction):
    global timer
    timer +=1
    clock.tick()
    sky.draw(canvas, clock, frame)
    if sky.phase < 0.4 and sky.phase > 0.1:
        if timer % 20 == 0:
            zombies.append(Zombie(600, 400, player))
    terrain.draw(canvas)
    for Z in zombies:
        Z.draw(canvas)
        Z.update()
    zombie.draw(canvas)
    player.update(interaction)
    zombie.update()
    player.draw(canvas)


main = Scene("main", draw)

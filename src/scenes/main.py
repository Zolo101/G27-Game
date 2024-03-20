import random

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

global timer
timer = 0

zombies = []
clock = Clock()


def draw(manager, canvas, clock, frame, interaction):
    """ This gets run on every frame. """
    global timer
    timer +=1
    clock.tick()
    sky.draw(canvas, clock, frame)
    if sky.phase < 0:
        if timer % 20 == 0:
            zombies.append(Zombie(-100, 400, player))
            zombies.append(Zombie(1500, 400, player))
    terrain.draw(canvas)
    for Z in zombies:
        Z.draw(canvas)
        Z.update()
    player.update(interaction)
    player.draw(canvas)
    check_collision(player, terrain)

    terrain.remove_dead()


def check_collision(p, t):
    for block in t.blocks.values():
        # block collision
        # collided = (
        #         (block.x <= p.sprite.pos.x <= block.x + 20) and
        #         (block.y <= p.sprite.pos.y <= block.y - 20)
        # )

        collided = (
                (block.x < p.sprite.pos.x) and
                (block.x + 20 > p.sprite.pos.x) and
                (block.y > p.sprite.pos.y) and
                (block.y + 20 < p.sprite.pos.x)
        )

        p.sprite.grounded = collided
        break


main = Scene("main", draw)

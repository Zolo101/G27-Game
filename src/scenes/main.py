import random
import time

from src.classes.SceneManager import Scene
from src.game.Player import Player
from src.game.Sky import Sky
from src.game.Terrain import Terrain
from src.game.Zombie import Zombie
from src.classes.Clock import Clock
from src.scenes.UI import UI

# TODO: Make the width and height a variable
terrain = Terrain(1280, 800)
sky = Sky()
player = Player(600, 400)
ui = UI(player)

global timer
timer = 0

zombies = []
clock = Clock()


def draw(manager, canvas, clock, frame, interaction):
    """ This gets run on every frame. """
    global timer
    timer += 1
    clock.tick()
    sky.draw(canvas, clock, frame)
    # if sky.phase < 0:
    if timer % 40 == 0:
        zombies.append(Zombie(400, -800, player))
        # zombies.append(Zombie(-100, 400, player))
        # zombies.append(Zombie(1500, 400, player))
    terrain.draw(canvas)
    for Z in zombies:
        Z.draw(canvas)
        Z.update()
        # check_collision(Z, terrain)

    player.update(interaction)
    player.draw(canvas)

    # check_collision(player, terrain)

    terrain.remove_dead()

    ui.draw(canvas)


def tick(manager, clock, frame, interaction):
    for zombie in zombies:
        check_collision(zombie, terrain)
    check_collision(player, terrain)


def check_collision(p, t):
    p.sprite.grounded = False

    p.sprite.blocked["up"] = False
    p.sprite.blocked["down"] = False
    p.sprite.blocked["left"] = False
    p.sprite.blocked["right"] = False

    for block in t.blocks.values():
        # block collision
        # collided = (
        #         (block.x <= p.sprite.pos.x <= block.x + 20) and
        #         (block.y <= p.sprite.pos.y <= block.y - 20)
        # )

        # collided = (
        #         (block.x < p.sprite.pos.x) and
        #         (block.x + 20 > p.sprite.pos.x) and
        #         (block.y > p.sprite.pos.y) and
        #         (block.y + 20 < p.sprite.pos.x)
        # )
        dx = p.sprite.pos.x - block.x
        dy = p.sprite.pos.y - block.y

        if abs(dx) < p.size[0] and abs(dy) < p.size[1]:
            down = block.y - 20 <= p.sprite.pos.y + p.size[1]
            up = block.y <= p.sprite.pos.y + p.size[1]
            left = block.x <= p.sprite.pos.x + p.size[0]
            right = block.x + 20 <= p.sprite.pos.x + p.size[0]

            p.sprite.blocked["up"] |= up
            p.sprite.blocked["down"] |= down # and (left or right)
            p.sprite.blocked["left"] |= left
            p.sprite.blocked["right"] |= right

            p.sprite.grounded |= p.sprite.blocked["up"] or p.sprite.blocked["down"] or p.sprite.blocked["left"] or p.sprite.blocked["right"]


main = Scene("main", draw, tick)

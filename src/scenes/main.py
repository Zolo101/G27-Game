import random

from src.classes.SceneManager import Scene
from src.classes.Vector import Vector
from src.game.Player import Player
from src.game.Sky import Sky
from src.game.Terrain import Terrain
from src.game.Zombie import Zombie
from src.classes.Clock import Clock
from src.scenes.UI import UI
from src.classes.Pew import Pew
from src.classes.Shoot import Shoot
from src.classes.Perks import Health
from src.classes.Perks import Speed

# TODO: Make the width and height a variable
terrain = Terrain(1280, 800)
sky = Sky()
player = Player(600, 400)
pew = Pew(player)
ui = UI(player)
shoot = Shoot(player)

global timer
timer = 0
zombies = []
perks = []
clock = Clock()
cur_zom_num = 0
max_zom_num = 1
wave_delay = 10000

def draw(manager, canvas, clock, frame, interaction):
    """ This gets run on every frame. """
    global timer
    timer += 1
    clock.tick()
    sky.draw(canvas, clock, frame)
    if sky.phase < 0:
        if cur_zom_num < max_zom_num:
            if timer % 40 == 0:
                zombies.append(Zombie(400, -000, player,shoot))

                #this line of code crushes the game for some reason
                #responsible for limiting the number of zombies in each wave
                #cur_zom_num += 1


    #makes zombies substantially harder to kill
    if timer % wave_delay == 0:
        for zombie in zombies:
            zombie.progres_dif()

    # zombies.append(Zombie(-100, 400, player))
    # zombies.append(Zombie(1500, 400, player))
    if timer % 70 == 0:
        perks.append(Health(random.randint(0, 1280),player))                                                         # HEALTH PERKS
    if timer % 60 == 0:
        perks.append(Speed(random.randint(0, 1280),player))                                                          # SPEED PERKS

    terrain.draw(canvas)

    shoot.draw(canvas)
    shoot.update(interaction)

    for perk in perks:
        perk.draw(canvas)
        perk.update(interaction)

    for zombie in zombies:
        zombie.draw(canvas)
        zombie.update()

        if not zombie.is_alive():
            zombies.remove(zombie)
            player.earn(100) # money per zombie kill

        # check_collision(zombie, terrain)
        # draw_debug_collisions(canvas, terrain, zombie)


    player.update(interaction)
    player.draw(canvas)

    terrain.remove_dead()

    # bullet collision check
    shoot.check_collision(terrain)

    # out of bounds check
    if player.sprite.pos.y > 800:
        player.take_damage(49)
        player.sprite.pos.x = 600
        player.sprite.pos.y = 400

    # game over check
    if not player.is_alive():
        manager.switch_scene("game_over")

    pew.draw(canvas)
    pew.update(interaction)
    ui.draw(canvas)



    # draw_debug_collisions(canvas, terrain, player)





def draw_cube(canvas, pos, colour="#ffffff"):
    canvas.draw_polygon([
        (pos.x, pos.y),
        (pos.x + 20, pos.y),
        (pos.x + 20, pos.y + 20),
        (pos.x, pos.y + 20)],
        0,
        colour,
        colour
    )


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

    for block in t.visible_blocks.values():
        # block collision

        dx = p.sprite.pos.x - block.x
        dy = p.sprite.pos.y - block.y

        if collision_consensus(dx, dy, p):
            down = block.y - 20 <= p.sprite.pos.y + p.size[1]
            up = block.y <= p.sprite.pos.y + p.size[1]

            p.sprite.blocked["up"] |= up
            p.sprite.blocked["down"] |= down

        if collision_consensus_sides(dx, dy, p):
            bl_pos = p.sprite.pos.copy().add(Vector(0, p.size[1] - 50))
            br_pos = p.sprite.pos.copy().add(Vector(p.size[0], p.size[1] - 50))

            left = block.x <= bl_pos.x
            right = block.x + p.size[0] >= br_pos.x

            p.sprite.blocked["left"] |= left
            p.sprite.blocked["right"] |= right

        p.sprite.grounded |= (p.sprite.blocked["up"] or
                              p.sprite.blocked["down"] or
                              p.sprite.blocked["left"] or
                              p.sprite.blocked["right"])


def collision_consensus(dx, dy, p):
    return p.size[0] - 50 >= abs(dx + 15) - 50 and p.size[1] < abs(dy) < p.size[1] + 20


def collision_consensus_sides(dx, dy, p):
    return abs(dx) - 10 < p.size[0] and p.size[1] - 30 < abs(dy) < p.size[1] - 10


def draw_debug_collisions(canvas, terrain, character):
    for t in terrain.visible_blocks.values():
        dx = character.sprite.pos.x - t.x
        dy = character.sprite.pos.y - t.y

        if collision_consensus(dx, dy, character):
            draw_cube(canvas, Vector(t.x, t.y))

        if collision_consensus_sides(dx, dy, character):
            draw_cube(canvas, Vector(t.x, t.y), "#ff0000")


main = Scene("main", draw, tick)

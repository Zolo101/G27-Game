import random

from src.classes.Builder import Builder
from src.classes.Color import Color
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
from src.classes import Music

# TODO: Make the width and height a variable
terrain = Terrain(1280, 800)
sky = Sky()
player = Player(600, 400)
builder = Builder()
pew = Pew(player)
ui = UI(player, sky)
shoot = Shoot(player)

global timer
global hCount
global sCount
hCount = 0
sCount = 0
timer = 0
zombies = []
perks = []
clock = Clock()
cur_zom_num = 0
max_zom_num = 1
wave_delay = 10000
global night_count
night_count = 0
# zzz = Zombie(400, -000, player,shoot)
def draw(manager, canvas, clock, frame, interaction):
    """ This gets run on every frame. """
    # print(interaction.keys_down())
    max_zom_num = 1
    global timer
    global night_count
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
    if (sky.phase > -1) and (sky.phase < -0.999):
        night_count = night_count + 1
        print(night_count)

    #makes zombies substantially harder to kill
    if timer % wave_delay == 0:
        for zombie in zombies:
            zombie.progres_dif()

    # zombies.append(Zombie(-100, 400, player))
    # zombies.append(Zombie(1500, 400, player))


    rrr = random.randint(0, 600)
    global hCount
    global sCount
    if hCount < 4:
        if rrr == 1:
            perks.append(Health(random.randint(0, 1280), player))  # HEALTH PERKS
            hCount = hCount+1
    if sCount < 4:
        if rrr == 2:
            perks.append(Speed(random.randint(0, 1280), player))  # SPEED PERKS
            sCount = sCount+1

    terrain.draw(canvas)

    shoot.draw(canvas)
    shoot.update(interaction)


    for perk in perks:
        perk.draw(canvas)
        perk.update(interaction)

    for zombie in zombies:
        zombie.draw(canvas)
        zombie.update()

    if len(zombies) > 0:
        for bullet in shoot.bullets:
            for zombie in zombies:
                if (bullet.pos.x < (zombie.sprite.pos.x+20)) and (bullet.pos.x > (zombie.sprite.pos.x-20)):
                    zombies.remove(zombie)
                    player.earn(100) # money per zombie kill
                    player.increaseScore(1) #increase score per zombie kill

                    # the line below crashes sometimes when killing a zombie
                    if bullet in shoot.bullets:
                        shoot.bullets.remove(bullet)

        # check_collision(zombie, terrain)
        # draw_debug_collisions(canvas, terrain, zombie)

    if player.money >= 10:
        if not builder.pos.get_p() in terrain.blocks:
            builder.build(terrain)
            player.money -= 10

    player.update(interaction)
    player.draw(canvas)

    terrain.remove_dead()
    terrain.heal()

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
    builder.draw(canvas, interaction)
    ui.draw(canvas, night_count)

    side_left = (
        Vector(player.sprite.pos.x, player.sprite.pos.y + (player.size[1] - 10))
        .snap(Vector(20, 20))
    )
    side_right = (
        Vector(player.sprite.pos.x + (player.size[0]), player.sprite.pos.y + (player.size[1] - 10))
        .snap(Vector(20, 20))
    )
    bottom_center = (
        Vector(player.sprite.pos.x + (player.size[0] / 2), player.sprite.pos.y + player.size[1] + 10)
        .snap(Vector(20, 20))
    )
    bottom_center_up = (
        Vector(player.sprite.pos.x + (player.size[0] / 2), player.sprite.pos.y + player.size[1] - 10)
        .snap(Vector(20, 20))
    )

    draw_cube(canvas, side_left, "#ff0000")
    draw_cube(canvas, side_right, "#00ff00")
    draw_cube(canvas, bottom_center, "#ffffff")
    draw_cube(canvas, bottom_center_up, "#aaaaaa")



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
    RANGE = 60
    HURT = 0.1

    for zombie in zombies:
        check_collision(zombie, terrain)
        pos = (
            zombie.sprite.pos
            .copy()
            .add(Vector(0, zombie.size[1]))
            .snap(Vector(20, 20))
        )


        for x in range(int(pos.x) - RANGE, int(pos.x) + RANGE, 20):
            for y in range(int(pos.y) - RANGE, int(pos.y) + RANGE, 20):
                block = terrain.blocks.get((x, y))
                if block is not None:
                    # player made blocks only
                    if block.color == Color(156, 156, 156):
                        block.health -= HURT

    check_collision(player, terrain)


def check_collision(s, t):
    # raycast to terrain
    # if collision at side, set blocked side to true
    new_pos = s.sprite.emulate_next_frame()
    s.sprite.grounded = False
    s.sprite.touching = False

    s.sprite.blocked["up"] = False
    s.sprite.blocked["down"] = False
    s.sprite.blocked["left"] = False
    s.sprite.blocked["right"] = False

    side_left = (
        Vector(new_pos.x, new_pos.y + (s.size[1] - 10))
        .snap(Vector(20, 20))
        .get_p()
    )
    side_right = (
        Vector(new_pos.x + (s.size[0]), new_pos.y + (s.size[1] - 10))
        .snap(Vector(20, 20))
        .get_p()
    )
    bottom_center = (
        Vector(new_pos.x + (s.size[0] / 2), new_pos.y + s.size[1] + 10)
        .snap(Vector(20, 20))
        .get_p()
    )

    bottom_center_up = (
        Vector(new_pos.x + (s.size[0] / 2), new_pos.y + s.size[1] + 10)
        .snap(Vector(20, 20))
        .get_p()
    )

    top_center = (
        Vector(new_pos.x + (s.size[0] / 2), new_pos.y)
        .snap(Vector(20, 20))
        .get_p()
    )

    if side_left in t.visible_blocks:
        s.sprite.blocked["left"] = True

    if side_right in t.visible_blocks:
        s.sprite.blocked["right"] = True

    if bottom_center in t.visible_blocks:
        s.sprite.blocked["down"] = True

    if top_center in t.visible_blocks:
        s.sprite.blocked["up"] = True

    # if bottom_center_up in t.visible_blocks:
    #     new_pos.subtract(Vector(0, 20))
    #     s.sprite.vel = Vector(0, 0)
    #     s.sprite.blocked["down"] = True

    s.sprite.grounded = s.sprite.blocked["down"]
    s.sprite.touching |= (s.sprite.blocked["up"] or
                          s.sprite.blocked["down"] or
                          s.sprite.blocked["left"] or
                          s.sprite.blocked["right"])


main = Scene("main", draw, tick)

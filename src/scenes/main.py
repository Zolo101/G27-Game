import random
from src.classes.Builder import Builder
from src.classes.Color import Color
from src.classes.SceneManager import Scene
from src.classes.Vector import Vector
from src.classes.Perks import Health, Speed


def draw(game, canvas):
    """ This gets run on every game.frame. """

    # print(interaction.keys_down())
    max_zom_num = 1
    game.clock.tick()
    game.sky.draw(canvas, game.clock, game.frame)
    if game.sky.phase < 0:
        if game.clock.transition(game.wave_manager.spawn_cooldown):
            game.wave_manager.add_zombie(game.zombies, game.player, game.shoot, game.interaction)

    if game.night_count != game.sky.day and game.night_count != 0:
        # its a new night, and we survived it
        game.wave_manager.new_wave(25, 1)
    game.night_count = game.sky.day

    game.player.night = game.night_count

    # game.zombies.append(Zombie(-100, 400, game.player))
    # game.zombies.append(Zombie(1500, 400, game.player))


    rrr = random.randint(0, 500)
    if game.night_count == 1:
        if game.hCount < 2:
            if rrr == 1:
                game.perks.append(Health(random.randint(80, 1200), game.player))  # HEALTH game.PERKS
                game.hCount += 1
        if game.sCount < 2:
            if rrr == 2:
                game.perks.append(Speed(random.randint(80, 1200), game.player))  # SPEED game.PERKS
                game.sCount += 1
    if game.night_count == 2:
        if game.hCount < 3:
            if rrr == 1:
                game.perks.append(Health(random.randint(80, 1200), game.player))  # HEALTH game.PERKS
                game.hCount += 1
        if game.sCount < 3:
            if rrr == 2:
                game.perks.append(Speed(random.randint(80, 1200), game.player))  # SPEED game.PERKS
                game.sCount += 1
    if game.night_count == 3:
        if game.hCount < 4:
            if rrr == 1:
                game.perks.append(Health(random.randint(80, 1200), game.player))  # HEALTH game.PERKS
                game.hCount += 1
        if game.sCount < 4:
            if rrr == 2:
                game.perks.append(Speed(random.randint(80, 1200), game.player))  # SPEED game.PERKS
                game.sCount += 1
    if game.night_count == 4:
        if game.hCount < 5:
            if rrr == 1:
                game.perks.append(Health(random.randint(80, 1200), game.player))  # HEALTH game.PERKS
                game.hCount += 1
        if game.sCount < 5:
            if rrr == 2:
                game.perks.append(Speed(random.randint(80, 1200), game.player))  # SPEED game.PERKS
                game.sCount += 1
    if game.night_count == 5:
        if game.hCount < 6:
            if rrr == 1:
                game.perks.append(Health(random.randint(80, 1200), game.player))  # HEALTH game.PERKS
                game.hCount += 1
        if game.sCount < 6:
            if rrr == 2:
                game.perks.append(Speed(random.randint(80, 1200), game.player))  # SPEED game.PERKS
                game.sCount += 1


    for perk in game.perks:
        perk.draw(canvas)
        perk.update(game.control)

    for cloud in game.clouds:
        cloud.draw(canvas)
        cloud.update()

    game.terrain.draw(canvas)

    game.shoot.draw(canvas)
    game.shoot.update(game.control)

    for zombie in game.zombies:
        zombie.draw(canvas)
        zombie.update(game.clock)

    if len(game.zombies) > 0:
        for bullet in game.shoot.bullets:
            for zombie in game.zombies:
                if (bullet.pos.x < (zombie.sprite.pos.x+20)) and (bullet.pos.x > (zombie.sprite.pos.x-20)):
                    if zombie.health <= 0:
                        game.zombies.remove(zombie)
                        game.player.earn(100) # money per zombie kill
                        game.player.increaseScore(random.randint(50, 75)) #increase score per zombie kill
                    # the line below crashes sometimes when killing a zombie
                    if bullet in game.shoot.bullets:
                        zombie.zombie_take_damage(5)
                        game.shoot.bullets.remove(bullet)

        # check_collision(zombie, game.terrain)
        # draw_debug_collisions(canvas, game.terrain, zombie)

    if game.player.money >= 10:
        if not game.builder.pos.get_p() in game.terrain.blocks:
            game.builder.build(game.terrain)
            game.player.money -= 10

    game.player.update(game.control)
    game.player.draw(canvas)

    game.terrain.remove_dead()
    game.terrain.heal()

    # bullet collision check
    game.shoot.check_collision(game.terrain)

    # out of bounds check
    if game.player.sprite.pos.y > 800:
        game.player.take_damage(49)
        game.player.sprite.pos.x = 600
        game.player.sprite.pos.y = 0

    # game over check
    if not game.player.is_alive():
        game.manager.switch_scene("game_over")

    if game.night_count >= 5 and game.player.is_alive() and game.sky.moon.pos.x > 1138:
        game.manager.switch_scene("win")

    game.pew.draw(canvas)
    game.pew.update(game.control)
    game.builder.draw(canvas, game.control)


    game.ui.draw(canvas, game.night_count)

    # DEBUG COLLISION STUFF
    # side_left = (
    #     Vector(game.player.sprite.pos.x, game.player.sprite.pos.y + (game.player.size[1] - 10))
    #     .snap(Vector(20, 20))
    # )
    # side_right = (
    #     Vector(game.player.sprite.pos.x + (game.player.size[0]), game.player.sprite.pos.y + (game.player.size[1] - 10))
    #     .snap(Vector(20, 20))
    # )
    # bottom_center = (
    #     Vector(game.player.sprite.pos.x + (game.player.size[0] / 2), game.player.sprite.pos.y + game.player.size[1] + 10)
    #     .snap(Vector(20, 20))
    # )
    # bottom_center_up = (
    #     Vector(game.player.sprite.pos.x + (game.player.size[0] / 2), game.player.sprite.pos.y + game.player.size[1] - 10)
    #     .snap(Vector(20, 20))
    # )
    #
    # draw_cube(game, side_left, "#ff0000")
    # draw_cube(game, side_right, "#00ff00")
    # draw_cube(game, bottom_center, "#ffffff")
    # draw_cube(game, bottom_center_up, "#aaaaaa")

    # draw_debug_collisions(canvas, game.terrain, game.player)


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


def tick(game):
    RANGE = 120
    HURT = 0.1

    for zombie in game.zombies:
        check_collision(zombie, game.terrain)
        pos = (
            zombie.sprite.pos
            .copy()
            .add(Vector(zombie.size[0] / 2, zombie.size[1] / 2))
            .snap(Vector(20, 20))
        )

        for x in range(int(pos.x) - RANGE, int(pos.x) + RANGE, 20):
            for y in range(int(pos.y) - RANGE, int(pos.y) + RANGE, 20):
                block = game.terrain.blocks.get((x, y))
                if block is not None:
                    # game.player made blocks only
                    if block.color == Color(156, 156, 156):
                        block.health -= HURT

    check_collision(game.player, game.terrain)


def check_collision(s, t):
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

    if side_left in t.blocks:
        s.sprite.blocked["left"] = True

    if side_right in t.blocks:
        s.sprite.blocked["right"] = True

    if bottom_center in t.blocks:
        s.sprite.blocked["down"] = True

    if top_center in t.blocks:
        s.sprite.blocked["up"] = True

    s.sprite.grounded = s.sprite.blocked["down"]
    s.sprite.touching |= (s.sprite.blocked["up"] or
                          s.sprite.blocked["down"] or
                          s.sprite.blocked["left"] or
                          s.sprite.blocked["right"])


main = Scene("main", draw, tick)

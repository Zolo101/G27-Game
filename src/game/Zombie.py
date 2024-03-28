from src.classes.Sprite import Sprite
from src.classes.Spritesheet import Spritesheet


JUMP_POWER = 40 / 4

#zombie class
class Zombie:
    def __init__(self, x, y, player,bullets,health = 50, max_health = 50,SPEED = 2,):
        self.bullets = bullets
        self.size = (75, 200)
        self.sprite = Sprite("zombie", x, y)
        self.sprite.sheet = Spritesheet(
            "./assets/zombie_spritesheet.png",
            288,
            256, 9, 8,80,200)

        self.sprite.sheet.pos.x = x
        self.sprite.sheet.pos.y = y
        self.sprite.sheet.frame_index[1] = 1
        self.sprite.sheet.max_c = 2
        self.player = player
        self.health = health
        self.max_health = max_health
        self.SPEED = SPEED
        self.given_damage = 0
        self.since_damaged = 0

    def update(self):
        if self.player.sprite.sheet.pos.x < self.sprite.pos.x:
            self.sprite.pos.x -= self.SPEED
            self.sprite.sheet.frame_index[1] = 5
            self.sprite.sheet.next_frame()

        if self.player.sprite.sheet.pos.x > self.sprite.pos.x:
            self.sprite.pos.x += self.SPEED
            self.sprite.sheet.frame_index[1] = 1
            self.sprite.sheet.next_frame()

        if (self.sprite.pos.x > self.player.sprite.sheet.pos.x) and (self.sprite.pos.x < self.player.sprite.sheet.pos.x + 200) and (self.sprite.pos.y > self.player.sprite.sheet.pos.y - 200) and (self.sprite.pos.y < self.player.sprite.sheet.pos.y + 80) and  self.given_damage == False :
            self.player.take_damage(1)
            self.given_damage = True

        if self.given_damage == True:
            self.since_damaged += 1

        if self.sprite.blocked["left"] or self.sprite.blocked["right"]:
            self.sprite.vel.y -= JUMP_POWER
            self.sprite.sheet.next_frame()

        if  self.given_damage == True and self.since_damaged > 10:
            self.given_damage = False

        if self.since_damaged > 11:
            self.since_damaged = 0
        # self.sprite.sheet.next_frame()
        self.sprite.sheet.max_c = 2
        self.sprite.update()

    def progres_dif(self):
        """ with each wave zombies become tougher """
        self.health += 20
        self.max_health +=20
        self.SPEED += 2

    def zombie_take_damage(self, amount):
        """ reduce zombie hp """
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def draw(self, canvas):
        """ This gets run on every frame. """

        bar_x = self.sprite.pos.x
        bar_y = self.sprite.pos.y + self.size[1] + 5
        health_percentage = self.health / self.max_health
        health_bar_width = health_percentage * 70
        health_bar_height = 10
        health_bar_colour = "Red"

        canvas.draw_polygon([(bar_x, bar_y), (bar_x + health_bar_width, bar_y), (bar_x + health_bar_width, bar_y + health_bar_height), (bar_x, bar_y + health_bar_height)],
                            1, health_bar_colour, health_bar_colour)
        # debug
        # canvas.draw_polygon([
        #     (self.sprite.pos.x, self.sprite.pos.y),
        #     (self.sprite.pos.x + self.size[0], self.sprite.pos.y),
        #     (self.sprite.pos.x + self.size[0], self.sprite.pos.y + self.size[1]),
        #     (self.sprite.pos.x, self.sprite.pos.y + self.size[1])],
        #     0,
        #     "red",
        #     "red"
        # )

        self.sprite.sheet.draw(canvas)

class Zombie1:
    def __init__(self, x, y, player, bullets,health = 50, max_health = 50,SPEED = 50,):
        self.bullets = bullets
        self.size = (1, 270)
        self.sprite = Sprite("zombie1", x, y)
        self.sprite.sheet = Spritesheet(
            "./assets/ccc.png",
            571,
            437, 8, 6,60,150)

        self.sprite.sheet.pos.x = x
        self.sprite.sheet.pos.y = y
        self.sprite.sheet.frame_index[1] = 2
        self.sprite.sheet.max_c = 8
        self.player = player
        self.health = health
        self.max_health = max_health
        self.SPEED = SPEED

    def update(self):
        if self.player.sprite.sheet.pos.x < self.sprite.pos.x:
            self.sprite.pos.x -= self.SPEED
            self.sprite.sheet.frame_index[1] = 5
            self.sprite.sheet.next_frame()
        if self.player.sprite.sheet.pos.x > self.sprite.pos.x:
            self.sprite.pos.x += self.SPEED
            self.sprite.sheet.frame_index[1] = 2
            self.sprite.sheet.next_frame()
        if (self.sprite.pos.x > self.player.sprite.sheet.pos.x) and (self.sprite.pos.x < self.player.sprite.sheet.pos.x + 20) and (self.sprite.pos.y > self.player.sprite.sheet.pos.y - 80) and (self.sprite.pos.y < self.player.sprite.sheet.pos.y + 80) :
            self.player.take_damage(1)
        if self.sprite.blocked["left"] or self.sprite.blocked["right"]:
            self.sprite.vel.y -= JUMP_POWER
            self.sprite.sheet.next_frame()

        # self.sprite.sheet.next_frame()
        self.sprite.sheet.max_c = 8
        self.sprite.update()

    def progres_dif(self):
        """ with each wave zombies become tougher """
        self.health += 20
        self.max_health +=20
        self.SPEED += 2

    def zombie_take_damage(self, amount):
        """ reduce zombie hp """
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def draw(self, canvas):
        """ This gets run on every frame. """

        # debug
        # canvas.draw_polygon([
        #     (self.sprite.pos.x, self.sprite.pos.y),
        #     (self.sprite.pos.x + self.size[0], self.sprite.pos.y),
        #     (self.sprite.pos.x + self.size[0], self.sprite.pos.y + self.size[1]),
        #     (self.sprite.pos.x, self.sprite.pos.y + self.size[1])],
        #     0,
        #     "red",
        #     "red"
        # )

        self.sprite.sheet.draw(canvas)

class Zombie2:
    def __init__(self, x, y, player, bullets,health = 50, max_health = 50,SPEED = 2,):
        self.bullets = bullets
        self.size = (1000, 270)
        self.sprite = Sprite("zombie2", x, y)
        self.sprite.sheet = Spritesheet(
            "./assets/jjj.png",
            352,
            708, 5, 10,90,210)

        self.sprite.sheet.pos.x = x
        self.sprite.sheet.pos.y = y
        self.sprite.sheet.frame_index[1] = 2
        self.sprite.sheet.max_c = 5
        self.player = player
        self.health = health
        self.max_health = max_health
        self.SPEED = SPEED

    def update(self):
        if self.player.sprite.sheet.pos.x < self.sprite.pos.x:
            self.sprite.pos.x -= self.SPEED
            self.sprite.sheet.frame_index[1] = 4
            self.sprite.sheet.next_frame()
        if self.player.sprite.sheet.pos.x > self.sprite.pos.x:
            self.sprite.pos.x += self.SPEED
            self.sprite.sheet.frame_index[1] = 9
            self.sprite.sheet.next_frame()
        if (self.sprite.pos.x > self.player.sprite.sheet.pos.x) and (self.sprite.pos.x < self.player.sprite.sheet.pos.x + 20) and (self.sprite.pos.y > self.player.sprite.sheet.pos.y - 80) and (self.sprite.pos.y < self.player.sprite.sheet.pos.y + 80) :
            self.player.take_damage(1)

        if self.sprite.blocked["left"] or self.sprite.blocked["right"]:
            self.sprite.vel.y -= JUMP_POWER
            self.sprite.sheet.next_frame()

        # self.sprite.sheet.next_frame()
        self.sprite.sheet.max_c = 5
        self.sprite.update()

    def progres_dif(self):
        """ with each wave zombies become tougher """
        self.health += 20
        self.max_health +=20
        self.SPEED += 2

    def zombie_take_damage(self, amount):
        """ reduce zombie hp """
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def draw(self, canvas):
        """ This gets run on every frame. """

        # debug
        # canvas.draw_polygon([
        #     (self.sprite.pos.x, self.sprite.pos.y),
        #     (self.sprite.pos.x + self.size[0], self.sprite.pos.y),
        #     (self.sprite.pos.x + self.size[0], self.sprite.pos.y + self.size[1]),
        #     (self.sprite.pos.x, self.sprite.pos.y + self.size[1])],
        #     0,
        #     "red",
        #     "red"
        # )

        self.sprite.sheet.draw(canvas)

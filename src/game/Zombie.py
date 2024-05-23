from src.classes.Interaction import Interaction
from src.classes.Sprite import Sprite
from src.classes.Spritesheet import Spritesheet
from src.classes.Vector import Vector

JUMP_POWER = 60


class Zombie:
    def __init__(self, x, y, player,bullets, interaction, health = 250, max_health = 250,SPEED = 2,):
        self.bullets = bullets
        self.size = (75, 200)
        self.sprite = Sprite("zombie", x, y)
        self.sprite.size = self.size
        self.interaction = interaction

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

    def update(self, clock):
        center = self.sprite.pos.copy().add(Vector(self.size[0] / 2, self.size[1] / 2))
        player_center = self.player.sprite.pos.copy().add(Vector(self.player.size[0] / 2, self.player.size[1] / 2))
        if clock.transition(12):
            self.sprite.sheet.next_frame()

        distance_to_player = center - player_center

        # no need to move if your already at the player!
        if not self.interaction.sprite_sprite_collision(self.sprite, self.player.sprite):
            if player_center.x < center.x and not self.sprite.blocked["left"]:
                self.sprite.pos.x -= self.SPEED
                self.sprite.sheet.frame_index[1] = 5

            if player_center.x > center.x and not self.sprite.blocked["right"]:
                self.sprite.pos.x += self.SPEED
                self.sprite.sheet.frame_index[1] = 1

            if (self.sprite.blocked["left"] or self.sprite.blocked["right"]) and self.sprite.grounded:
                self.sprite.vel.y -= JUMP_POWER

        if abs(distance_to_player.x) < 70 and abs(distance_to_player.y) < 80 and not self.given_damage:
            self.player.take_damage(1)
            self.given_damage = True

        if self.given_damage:
            self.since_damaged += 1

        if self.given_damage and self.since_damaged > 10:
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

        canvas.draw_polygon([(bar_x, bar_y), (bar_x + 70, bar_y), (bar_x + 70, bar_y + health_bar_height), (bar_x, bar_y + health_bar_height)],
                            1, "Red", "Red")

        canvas.draw_polygon([(bar_x, bar_y), (bar_x + health_bar_width, bar_y), (bar_x + health_bar_width, bar_y + health_bar_height), (bar_x, bar_y + health_bar_height)],
                            1, "Green", "Green")

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

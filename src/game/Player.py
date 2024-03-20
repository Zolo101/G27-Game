from src.classes.Sprite import Sprite
from src.classes.Spritesheet import Spritesheet

SPEED = 15
JUMP_POWER = 24


class Player:
    """
    Contains the `Sprite`, along with the health of the player.
    """

    def __init__(self, x, y, level=1, health=100, max_health=100):
        self.size = (30, 75)
        self.sprite = Sprite("player", x, y)
        # self.sprite.texture.pos.x = 300
        # self.sprite.texture.pos.y = 300
        self.sprite.sheet = Spritesheet(
            "./assets/player_spritesheet.png",
            640,
            420, 4, 2)
        self.sprite.sheet.pos.x = x
        self.sprite.sheet.pos.y = y

        self.level = level
        self.health = health
        self.max_health = max_health

    def update(self, interaction):
        """ This gets run on every frame. """
        # print(interaction.get_key("space"))
        # convert interaction keys to velocity
        if interaction.get_key("space") and self.sprite.grounded:
            self.sprite.vel.y -= JUMP_POWER

        if interaction.get_key("a"):
            self.sprite.pos.x -= SPEED
            self.sprite.sheet.pos.x -= SPEED
            self.sprite.sheet.next_frame()
        if interaction.get_key("d"):
            self.sprite.pos.x += SPEED
            self.sprite.sheet.pos.x += SPEED
            self.sprite.sheet.next_frame()

        self.sprite.update()

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        if self.health <= 0:
            return False

    def level_up(self):
        """ Increments the player level by 1, along with increases their health. """
        self.level += 1
        self.max_health += 10
        self.health = self.max_health

    def __str__(self):
        return f"{self.name} (Level {self.level}) - Health: {self.health}/{self.max_health}"

    def draw(self, canvas):
        """ This gets run on every frame. """

        # self.sprite.draw(canvas)
        # canvas.draw_polygon([
        #     (self.sprite.pos.x, self.sprite.pos.y),
        #     (self.sprite.pos.x + self.size[0], self.sprite.pos.y),
        #     (self.sprite.pos.x + self.size[0], self.sprite.pos.y + self.size[1]),
        #     (self.sprite.pos.x, self.sprite.pos.y + self.size[1])],
        #     0,
        #     "blue",
        #     "blue"
        # )

        self.sprite.sheet.draw(canvas)
        # self.sprite.texture_idle.draw(canvas)
        # self.sprite.texture_right.draw(canvas)

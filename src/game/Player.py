from src.classes.Sprite import Sprite
from src.classes.Spritesheet import Spritesheet
from src.classes import Music

SPEED = 2.5
JUMP_POWER = 24 * 2


class Player:
    """
    Contains the `Sprite`, along with the health of the player.
    """

    def __init__(self, x, y, level=1, health=1000, max_health=1000):
        self.size = (50, 120)
        self.sprite = Sprite("player", x, y)
        self.sprite.sheet = Spritesheet(
            "./assets/player_spritesheet.png",
            640,
            840, 4, 4, 140,213)
        self.sprite.sheet.pos.x = 11111111
        self.sprite.sheet.pos.y = 11111111


        self.level = level
        self.health = health
        self.max_health = max_health

    def update(self, interaction):
        """ This gets run on every frame. """
        # print(interaction.get_key("space"))
        # convert interaction keys to velocity
        self.sprite.sheet.frame_index[1] = 0

        if interaction.get_key("space") and self.sprite.grounded:
            self.sprite.vel.y -= JUMP_POWER

        if interaction.get_key("a") and not self.sprite.blocked["left"]:
            self.sprite.vel.x -= SPEED
            self.sprite.sheet.max_c = 4
            self.sprite.sheet.frame_index[1] = 1                                                        # CHOOSES THE ROW FROM THE SPRITESHEET
            self.sprite.sheet.next_frame()
        if interaction.get_key("d") and not self.sprite.blocked["right"]:
            self.sprite.vel.x += SPEED
            self.sprite.sheet.max_c = 4
            self.sprite.sheet.frame_index[1] = 2                                                        # CHOOSES THH ROW FROM THE SPRITESHEET
            self.sprite.sheet.next_frame()
        if interaction.get_key("left"):
            self.sprite.sheet.frame_index[1] = 1
        if interaction.get_key("right"):
            self.sprite.sheet.frame_index[1] = 2
       
            
            



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
        return self.health > 0

    def level_up(self):
        """ Increments the player level by 1, along with increases their health. """
        self.level += 1
        self.max_health += 10
        self.health = self.max_health

    def __str__(self):
        return f"{self.name} (Level {self.level}) - Health: {self.health}/{self.max_health}"

    def draw(self, canvas):
        """ This gets run on every frame. """

        # print(self.sprite.blocked)

        canvas.draw_polygon([
            (self.sprite.pos.x, self.sprite.pos.y),
            (self.sprite.pos.x + self.size[0], self.sprite.pos.y),
            (self.sprite.pos.x + self.size[0], self.sprite.pos.y + self.size[1]),
            (self.sprite.pos.x, self.sprite.pos.y + self.size[1])],
            0,
            "blue",
            "blue"
        )
        self.sprite.sheet.draw(canvas)

        # self.sprite.sheet.draw(canvas)
        # self.sprite.texture_idle.draw(canvas)
        # self.sprite.texture_right.draw(canvas)
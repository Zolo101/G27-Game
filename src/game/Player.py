from src.classes.Sprite import Sprite

SPEED = 16
JUMP_POWER = 24


class Player:
    def __init__(self, x, y):
        self.size = (30, 75)
        self.sprite = Sprite("player")
        self.sprite.pos.x = x
        self.sprite.pos.y = y

    def update(self, interaction):
        # print(interaction.get_key("space"))
        # convert interaction keys to velocity
        if interaction.get_key("space") and self.sprite.grounded:
            self.sprite.vel.y -= JUMP_POWER
        if interaction.get_key("a"):
            self.sprite.pos.x -= SPEED
        if interaction.get_key("d"):
            self.sprite.pos.x += SPEED

        self.sprite.update()

    def draw(self, canvas):
        # self.sprite.draw(canvas)
        canvas.draw_polygon([
            (self.sprite.pos.x, self.sprite.pos.y),
            (self.sprite.pos.x + self.size[0], self.sprite.pos.y),
            (self.sprite.pos.x + self.size[0], self.sprite.pos.y + self.size[1]),
            (self.sprite.pos.x, self.sprite.pos.y + self.size[1])],
            0,
            "blue",
            "blue"
        )

from src.classes.Sprite import Sprite

SPEED = 2
JUMP_POWER = 40


class Zombie:
    def __init__(self, x, y, player):
        self.size = (60, 120)
        self.sprite = Sprite("zombie", x, y)
        self.sprite.pos.x = x
        self.sprite.pos.y = y
        self.player = player

    def update(self):
        if self.player.sprite.sheet.pos.x < self.sprite.pos.x:
            self.sprite.pos.x -= SPEED
        if self.player.sprite.sheet.pos.x > self.sprite.pos.x:
            self.sprite.pos.x += SPEED

        if self.sprite.blocked["left"] or self.sprite.blocked["right"]:
            self.sprite.vel.y -= JUMP_POWER

        self.sprite.update()

    def draw(self, canvas):
        """ This gets run on every frame. """
        # self.sprite.draw(canvas)
        canvas.draw_polygon([
            (self.sprite.pos.x, self.sprite.pos.y),
            (self.sprite.pos.x + self.size[0], self.sprite.pos.y),
            (self.sprite.pos.x + self.size[0], self.sprite.pos.y + self.size[1]),
            (self.sprite.pos.x, self.sprite.pos.y + self.size[1])],
            0,
            "red",
            "red"
        )

        canvas.draw_polygon([
            (self.sprite.pos.x, self.sprite.pos.y),
            (self.sprite.pos.x + 10, self.sprite.pos.y),
            (self.sprite.pos.x + 10, self.sprite.pos.y + 10),
            (self.sprite.pos.x, self.sprite.pos.y + 10)],
            0,
            "blue",
            "blue"
        )

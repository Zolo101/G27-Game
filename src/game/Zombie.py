from src.classes.Sprite import Sprite

SPEED = 10

class Zombie:
    def __init__(self, x, y, player):
        self.size = (30, 75)
        self.sprite = Sprite("zombie")
        self.sprite.pos.x = x
        self.sprite.pos.y = y
        self.player = player

    def update(self):
        if (self.player.sprite.pos.x < self.sprite.pos.x):
            self.sprite.pos.x = self.sprite.pos.x - 1
        if (self.player.sprite.pos.x > self.sprite.pos.x ):
            self.sprite.pos.x = self.sprite.pos.x + 1

        self.sprite.update()

    def draw(self, canvas):
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
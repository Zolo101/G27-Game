from src.classes.Sprite import Sprite

SPEED = 2

class Zombie:
    def __init__(self, x, y, player):
        self.size = (30, 75)
        self.sprite = Sprite("zombie", True)
        self.sprite.pos.x = x
        self.sprite.pos.y = y
        self.player = player

    def update(self):
        if self.player.sprite.sheet.pos.x < self.sprite.pos.x:
            self.sprite.pos.x -= SPEED
        if self.player.sprite.sheet.pos.x > self.sprite.pos.x:
            self.sprite.pos.x += SPEED

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

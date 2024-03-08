from src.classes.Sprite import Sprite


class Player:
    def __init__(self, x, y):
        self.size = (50, 100)
        self.sprite = Sprite("player")
        self.sprite.pos.x = x
        self.sprite.pos.y = y

    def update(self, interaction):
        # convert interaction keys to velocity
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

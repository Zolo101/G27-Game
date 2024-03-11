from src.classes.Sprite import Sprite
from src.classes.Spritesheet import Spritesheet
from src.game.Sky import Sky

SPEED = 10
class Zombie:
    def __init__(self, x, y, player,sky):
        self.size = (30, 75)
        self.spritesheet = Spritesheet("https://www.cs.rhul.ac.uk/courses/CS1830/sprites/explosion-spritesheet.png",900,900,9,9)
        self.sprite = Sprite("zombie")
        self.sprite.pos.x = x
        self.sprite.pos.y = y
        self.player = player
        self.phase = sky.moon.pos.y



    def update(self):
        if (self.player.sprite.pos.x < self.sprite.pos.x):
            self.sprite.pos.x -= 1
        if (self.player.sprite.pos.x > self.sprite.pos.x ):
            self.sprite.pos.x += 1

        self.sprite.update()

    def draw(self, canvas):
        # if Sky.phase <= 0 :
        #     self.spritesheet.draw(canvas)
        #     self.spritesheet.next_frame()
        if self.phase > 300:                                                                                            # CURRENTLY NOT REACTING TO THE UPDATES OIN THE MOON POSITION
            canvas.draw_polygon([
                (self.sprite.pos.x, self.sprite.pos.y),
                (self.sprite.pos.x + self.size[0], self.sprite.pos.y),
                (self.sprite.pos.x + self.size[0], self.sprite.pos.y + self.size[1]),
                (self.sprite.pos.x, self.sprite.pos.y + self.size[1])],
                0,
                "red",
                "red"
            )
        # canvas.draw_polygon([
        #     (self.sprite.pos.x, self.sprite.pos.y),
        #     (self.sprite.pos.x + self.size[0], self.sprite.pos.y),
        #     (self.sprite.pos.x + self.size[0], self.sprite.pos.y + self.size[1]),
        #     (self.sprite.pos.x, self.sprite.pos.y + self.size[1])],
        #     0,
        #     "red",
        #     "red"
        # )



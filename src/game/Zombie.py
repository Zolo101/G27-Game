from src.classes.Sprite import Sprite
from src.classes.Spritesheet import Spritesheet

SPEED = 10
class Zombie:
    def __init__(self, x, y, player):
        self.size = (30, 75)
        # TO BE CHANGED vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        self.spritesheet = Spritesheet("https://www.cs.rhul.ac.uk/courses/CS1830/sprites/explosion-spritesheet.png",900,900,9,9)
        self.sprite = Sprite("zombie")
        self.sprite.pos.x = x
        self.sprite.pos.y = y
        self.player = player



    def update(self):
        if (self.player.sprite.pos.x < self.sprite.pos.x):
            self.sprite.pos.x -= 1
        if (self.player.sprite.pos.x > self.sprite.pos.x ):
            self.sprite.pos.x += 1

        self.sprite.update()

    def draw(self, canvas):

        self.spritesheet.draw(canvas)
        self.spritesheet.next_frame()

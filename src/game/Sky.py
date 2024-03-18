import math

from src.classes.Color import Color
from src.classes.Sprite import Sprite
from src.classes.Vector import Vector
from src.classes.Spritesheet import Spritesheet

SPEED = 0.001
OFFSET = 500
CENTER = Vector(1280 // 2, 600)


class Sky:
    def __init__(self):
        self.sun = Sprite("Sun", True)
        self.moon = Sprite("Moon", True)
        self.moon_offset = 15
        self.phase = 0
        self.color = Color(135, 206, 235)
        # self.spritesheet = Spritesheet("https://www.cs.rhul.ac.uk/courses/CS1830/sprites/background_clouds.png", 100, 100, 4, 4)

    def draw(self, canvas, clock, frame):
        """ This gets run on every frame. """
        self.sun.pos = CENTER - Vector(
            math.sin(-clock.time * SPEED) * OFFSET,
            math.cos(-clock.time * SPEED) * OFFSET,
        )


        self.moon.pos = CENTER + Vector(
            math.sin(-clock.time * SPEED) * OFFSET,
            math.cos(-clock.time * SPEED) * OFFSET,
        )

        # print(self.moon.pos.y)

        self.phase = math.cos(-clock.time * SPEED)

        x = max(0, (self.sun.pos - CENTER).y) / 1
        self.color = Color(135, 206, 235) - Color(x, x, x)
        canvas.draw_circle(self.sun.pos.get_p(), 1, 100, "Yellow")

        # self.spritesheet.draw(canvas)
        # self.spritesheet.next_frame()
        canvas.draw_circle(self.moon.pos.get_p(), 1, 100, "White")
        canvas.draw_circle((self.moon.pos - Vector(self.moon_offset, self.moon_offset)).get_p(), 1, 100, self.color.__str__())


        frame.set_canvas_background(self.color.__str__())


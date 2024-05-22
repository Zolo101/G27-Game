import math

from src.classes.Vector import Vector

GRAVITY = 1.5
AIR_RESISTANCE = 0.8
TERMINAL_VELOCITY = 10


class Sprite:
    """3
    Base sprite class which contains the position,
    velocity and the texture (spritesheet) of the sprite.
    """

    def __init__(self, name, x=0, y=0, fixed=False):
        self.name = name
        """ The name of the sprite, used to differentiate from other sprites """

        self.pos = Vector(x, y)
        """ Position vector of the sprite """

        self.vel = Vector(0, 0)
        """ Velocity vector of the sprite """

        self.size = Vector(0,0)
        """ Collision size of the sprite """

        self.sheet = None
        """ Spritesheet of the sprite """

        self.fixed = fixed
        """ If true, disables gravity on the sprite. """

        self.grounded = False
        """ True if the sprite is colliding down with the terrain"""

        self.touching = False
        """ True if the sprite is colliding at all with the terrain """

        self.blocked = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
        }
        """ Dictionary of collision states """

        self.frame_index = [1, 4]

    def emulate_next_frame(self):
        next_position = self.pos.copy()
        next_velocity = self.vel.copy()

        if not self.fixed:
            next_velocity.y += GRAVITY

        next_position += next_velocity
        return next_position

    def update(self):
        """ This gets run on every frame. """
        self.pos += self.vel

        if not self.fixed:
            self.vel.y += GRAVITY

        if self.sheet:
            if self.name == "player":
                self.sheet.pos = self.pos.copy().add(Vector(self.sheet.frame_centre_x / 3, self.sheet.frame_centre_y / 3))
            else:
                self.sheet.pos = self.pos.copy().add(Vector(self.sheet.frame_centre_x / 0.4, self.sheet.frame_centre_y / 0.16))

        # debug
        # print(self.name, self.blocked)

        # collision physics
        if self.blocked["down"] or self.blocked["up"]:
            self.vel.y = min(self.vel.y, 0)

        if self.blocked["up"]:
            self.vel.y = 0
            self.pos.y += 20

        if not (self.blocked["left"] or self.blocked["right"]):
            self.vel.x *= AIR_RESISTANCE
        else:
            self.vel.x = 0

        # physics clamping (to stop super jumps)
        self.vel.y = max(self.vel.y, -TERMINAL_VELOCITY)

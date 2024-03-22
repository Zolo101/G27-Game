from src.classes.Vector import Vector

GRAVITY = 2
AIR_RESISTANCE = 0.8


class Sprite:
    """
    Base sprite class which contains the position,
    velocity and the texture of the sprite.
    """

    def __init__(self, name, x=0, y=0, fixed=False):
        self.name = name
        """ The name of the sprite, used to differentiate from other sprites """

        self.pos = Vector(x, y)
        """ Position vector of the sprite """

        self.vel = Vector(0, 0)
        """ Velocity vector of the sprite """

        self.sheet = None
        """ Spritesheet of the sprite """

        self.fixed = fixed
        """ If true, disables gravity on the sprite. """

        self.grounded = False
        """ True if the sprite is colliding with the terrain """

        self.blocked = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
        }
        self.frame_index = [1, 4]

    def update(self):
        """ This gets run on every frame. """
        self.pos += self.vel

        if not self.fixed:
            self.vel.y += GRAVITY

        if self.sheet:
            self.sheet.pos = self.pos.copy().add(Vector(self.sheet.frame_centre_x / 3, self.sheet.frame_centre_y / 3))

        # debug
        # print(self.name, self.blocked)

        # temporary terrain collision
        if self.blocked["down"]:
            self.vel.y = 0

        if not (self.blocked["left"] or self.blocked["right"]):
            self.vel.x *= AIR_RESISTANCE
        else:
            self.vel.x = 0



from src.classes.Vector import Vector

GRAVITY = 2


class Sprite:
    """
    Base sprite class which contains the position,
    velocity and the texture of the sprite.
    """

    def __init__(self, name, fixed=False):
        self.name = name
        """ The name of the sprite, used to differentiate from other sprites """

        self.pos = Vector(0, 0)
        """ Position vector of the sprite """

        self.vel = Vector(0, 0)
        """ Velocity vector of the sprite """

        self.sheet = None
        """ Spritesheet of the sprite """

        self.fixed = fixed
        """ If true, disables gravity on the sprite. """

        self.grounded = False
        """ True if the sprite is colliding with the terrain """

    def update(self):
        """ This gets run on every frame. """
        self.pos += self.vel

        if not self.fixed:
            self.vel.y += GRAVITY

        # temporary terrain collision
        if self.grounded:
            self.vel.y = 0

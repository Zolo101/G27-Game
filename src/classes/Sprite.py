from src.classes.Vector import Vector

GRAVITY = 2


class Sprite:
    def __init__(self, name, fixed=False):
        # TODO: Do we need a name?
        self.name = name

        # The position of the sprite
        self.pos = Vector(0, 0)

        # The velocity of the sprite
        self.vel = Vector(0, 0)

        # The Spritesheet of the sprite
        self.texture = None

        # Affected by gravity?
        self.fixed = fixed

        # On the ground?
        self.grounded = False

    def update(self):
        self.pos += self.vel

        if not self.fixed:
            self.vel.y += GRAVITY

        # temporary terrain collision
        self.grounded = self.pos.y > 540
        if self.grounded:
            self.vel.y = 0

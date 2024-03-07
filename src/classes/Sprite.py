from src.classes.Vector import Vector

GRAVITY = 0.9


class Sprite:
    def __init__(self, name, fixed=True):
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

    def update(self):
        self.pos += self.vel

        if not self.fixed:
            self.vel *= GRAVITY

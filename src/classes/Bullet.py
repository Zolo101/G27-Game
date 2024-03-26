import random

from src.classes.Vector import Vector

BULLET_GRAVITY = 0.1


class Bullet:
    """ Creates the bullet. """
    def __init__(self, pos, vel):
        """ Initialises the bullet's position and velocity """
        self.pos = Vector(pos[0], pos[1])
        self.vel = Vector(vel[0], vel[1])
        self.age = 0

    def update(self):
        """ Updates the bullets position based on its velocity. Making it move """
        self.age += 0.5

        self.pos += self.vel

        q = round(self.age) + 1
        self.pos += Vector(random.randrange(-q, q), random.randrange(-q, q))

        # Bullet drop (like in fortnite 🗿)
        self.vel.y += (BULLET_GRAVITY * self.age)

    def draw(self, canvas):
        """ Creates the bullet. """
        # THIS IS A TEMPORARY BULLET.
        canvas.draw_circle(self.pos.get_p(), 5,10, "Blue")










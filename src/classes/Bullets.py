class Bullets:
    """ Creates the bullet. """
    def __init__(self, pos, vel):
        """ Initialises the bullet's position and velocity """
        self.pos = list(pos)
        self.vel = list(vel)

    def update(self):
        """ Updates the bullets position based on its velocity. Making it move """
        for i in range(1):
            self.pos[i] += self.vel[i]

    def draw(self, canvas):
        """ Creates the bullet. """
        # THIS IS A TEMPORARY BULLET.
        canvas.draw_circle(self.pos, 5,10, "Blue")










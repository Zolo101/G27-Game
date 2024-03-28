import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Cloud:
    def __init__(self):
        self.image = simplegui._load_local_image("./assets/cloud.png")
        self.pos = [random.randrange(-200, 1200), random.randrange(-25, 325)]
        self.vel = [random.randrange(2, 4), 0]
        self.randomSize = random.randint(3, 6)

    def draw(self, canvas):
        canvas.draw_image(self.image, (self.image.get_width()/2, self.image.get_height()/2),
                          (self.image.get_width(), self.image.get_height()), self.pos,
                          (self.image.get_width()/self.randomSize, self.image.get_height()/self.randomSize))

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if self.pos[0] > 1280 + self.image.get_width():
            self.pos = [-100, random.randrange(-25, 325)]
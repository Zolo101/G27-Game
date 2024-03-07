from src.classes.Sprite import Sprite

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Zombie:
    def _init__(self, canvas, name):
        self.sprite = Sprite("zombie")
        self.canvas = canvas
        self.name = name

    def move_towards_player(self):
        # use Interaction class?
        player_coords = self.canvas.coords()
        zombie_coords = self.canvas.coords(self.image)
        if zombie_coords.x < player_coords:
            self.zombie_move_right()
        else:
            self.zombie_move_left()

    def zombie_move_left(self):
        self.sprite.vel.x -= 1

    def zombie_move_right(self):
        self.sprite.vel.x += 1
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from classes.Vector import Vector

class Zombie:
    def _init__(self, spawn_point, movement):
        self.spawn_point = Vector(0,0)
        self.movement = Vector(1,1)
    
    def update(self, canvas):
        canvas.
        
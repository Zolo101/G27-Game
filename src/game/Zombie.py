try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Zombie:
    def _init__(self, canvas, name):
        self.canvas = canvas
        self.name = name
    
    def move_towards_player(self):
        player_coords = self.canvas.coords()
        zombie_coords = self.canvas.coords(self.image)  
        if zombie_coords.x < player_coords:
            zombie_move_right()
        else:
            zombie_move_left()

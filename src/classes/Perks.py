from src.classes.Vector import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from src.classes.Spritesheet import Spritesheet
from src.classes.Sprite import Sprite

class Health:
    def __init__(self,x,player):
        self.falling_perks = []
        self.x = x
        self.falling_perks.append([x, 0])
        self.player = player
        self.image = simplegui._load_local_image("./assets/heart_spritesheet.png")
        # self.sprite.sheet = Spritesheet(
        #     "./assets/heart_spritesheet.png",
        #     1184,
        #     1, 1, 10, 95, 45)
        # img = simplegui._load_local_image("./assets/gun_spritesheet.png")

    def draw(self,canvas):

        for obj in self.falling_perks:
            # self.sprite.sheet.draw(canvas)
            # canvas.draw_circle(obj, 10, 60, "Red")
            canvas.draw_image(self.image, (592,592), (1184,1184), obj, (95, 95))

    #updates
    def update(self,interaction):
        for obj in self.falling_perks:
            obj[1] += 1                                                                                                 # SPEED OF PERK FALLING
            if interaction.get_key("e"):
                if (self.player.sprite.pos - Vector(obj[0], obj[1])).length() < 50:
                    self.falling_perks.remove(obj)
                    self.player.heal(50)
class Speed:
    def __init__(self,x,player):
        self.falling_perks = []
        self.x = x
        self.falling_perks.append([x, 0])
        self.player = player
        self.image = simplegui._load_local_image("./assets/speed_spritesheet.png")

    def draw(self,canvas):
        for obj in self.falling_perks:
            # https://www.spriters-resource.com/resources/sheets/200/202977.png?updated=1690658883
            canvas.draw_image(self.image, (4, 7.5), (8, 15), obj, (40, 75))

    def update(self,interaction):
        for obj in self.falling_perks:
            obj[1] += 1                                                                                                 # SPEED OF PERK FALLING
            if interaction.get_key("e"):
                if (self.player.sprite.pos - Vector(obj[0], obj[1])).length() < 50:
                    self.falling_perks.remove(obj)
                    self.player.flash()



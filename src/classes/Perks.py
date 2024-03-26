from src.classes.Spritesheet import Spritesheet
from src.classes.Sprite import Sprite

class Health:
    def __init__(self,x,player):
        self.falling_perks = []
        self.x = x
        self.falling_perks.append([x, 0])
        self.player = player
        # self.sprite.sheet = Spritesheet(
        #     "./assets/heart_spritesheet.png",
        #     1184,
        #     1, 1, 10, 95, 45)

    def draw(self,canvas):
        for obj in self.falling_perks:
            # self.sprite.sheet.draw(canvas)
            canvas.draw_circle(obj, 10, 60, "Red")
            # canvas.draw_polygon([(200, 260), (1080, 260), (1080, 645), (200, 645)], 2, 'White')

    def update(self,interaction):
        for obj in self.falling_perks:
            obj[1] += 1                                                                                                 # SPEED OF PERK FALLING
            if interaction.get_key("e"):
                if (obj[0] > self.player.sprite.sheet.pos.x) and (obj[0] < self.player.sprite.sheet.pos.x + 50) and (obj[1] > self.player.sprite.sheet.pos.y - 110) and (obj[1] < self.player.sprite.sheet.pos.y + 110) :
                    self.falling_perks.remove(obj)
                    self.player.heal(50)
class Speed:
    def __init__(self,x,player):
        self.falling_perks = []
        self.x = x
        self.falling_perks.append([x, 0])
        self.player = player

    def draw(self,canvas):
        for obj in self.falling_perks:
            canvas.draw_circle(obj, 10, 60, "Yellow")

    def update(self,interaction):
        for obj in self.falling_perks:
            obj[1] += 1                                                                                                 # SPEED OF PERK FALLING
            if interaction.get_key("e"):
                if (obj[0] > self.player.sprite.sheet.pos.x) and (obj[0] < self.player.sprite.sheet.pos.x + 50) and (obj[1] > self.player.sprite.sheet.pos.y - 110) and (obj[1] < self.player.sprite.sheet.pos.y + 110) :
                    self.falling_perks.remove(obj)



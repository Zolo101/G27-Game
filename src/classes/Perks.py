import random

global timer
timer = 0
class Perks:

    def __init__(self,x,player):
        self.falling_perks = []
        self.x = x
        self.falling_perks.append([x, 0])
        self.player = player

    def draw(self,canvas):
        for obj in self.falling_perks:
            canvas.draw_circle(obj, 30, 30, "Purple")

    def update(self,interaction):
        for obj in self.falling_perks:
            obj[1] += 1                                                                                                 # SPEED OF PERK FALLING
            if interaction.get_key("e"):
                if (obj[0] > self.player.sprite.sheet.pos.x) and (obj[0] < self.player.sprite.sheet.pos.x + 50) and (obj[1] > self.player.sprite.sheet.pos.y - 110) and (obj[1] < self.player.sprite.sheet.pos.y + 110) :
                    self.falling_perks.remove(obj)
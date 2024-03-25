from src.classes.Sprite import Sprite
from src.classes.Spritesheet import Spritesheet
from src.classes.Bullets import Bullets

class Shoot:

    def __init__(self,player):
        """ Initialises the bullets list and the player information """
        self.bullets = []
        self.player = player
        self.sprite = Sprite("shoot", self.player.sprite.sheet.pos.x, self.player.sprite.sheet.pos.y)

    def update(self,interaction):
        """ Shoots left or right depending on the user input """
        if interaction.get_key("left"):
            if interaction.get_key("up"):
                self.bullets.append(Bullets([self.player.sprite.sheet.pos.x - 77, self.player.sprite.sheet.pos.y - 7], [-10, 0]))
                if  interaction.get_key("space"):
                    self.bullets.append(
                        Bullets([self.player.sprite.sheet.pos.x - 77, self.player.sprite.sheet.pos.y - 7], [-10, 0]))
        if interaction.get_key("right"):
            if interaction.get_key("up"):
                self.bullets.append(Bullets([self.player.sprite.sheet.pos.x + 77, self.player.sprite.sheet.pos.y - 7], [10, 0]))
                if  interaction.get_key("space"):
                    self.bullets.append(
                        Bullets([self.player.sprite.sheet.pos.x + 77, self.player.sprite.sheet.pos.y - 7], [10, 0]))



        for bullet in self.bullets:
            bullet.update()
    def draw(self, canvas):
        for bullet in self.bullets:
            bullet.draw(canvas)
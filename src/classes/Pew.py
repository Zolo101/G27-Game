from src.classes.Spritesheet import Spritesheet
from src.classes.Sprite import Sprite

#
class Pew:

    def __init__(self,player):
        self.size = (50, 120)
        self.player = player
        self.sprite = Sprite("pew",self.player.sprite.sheet.pos.x,self.player.sprite.sheet.pos.y)
        self.sprite.sheet = Spritesheet(
            "./assets/gun_spritesheet.png",
            50,
            158, 1, 10, 95, 45)
        self.sprite.sheet.pos.x = self.player.sprite.sheet.pos.x
        self.sprite.sheet.pos.y = self.player.sprite.sheet.pos.y



    def update(self, interaction):

        # if interaction.get_key("d"):
        #     self.sprite.sheet.frame_index[1] = 10
        # if interaction.get_key("a"):
        #     self.sprite.sheet.frame_index[1] = 10
        # if interaction.get_key("space"):
        #     self.sprite.sheet.frame_index[1] = 10

        self.sprite.sheet.frame_index[1] = 10

        if interaction.get_key("left"):
            self.sprite.sheet.pos.x = self.player.sprite.sheet.pos.x - 70
            self.sprite.sheet.pos.y = self.player.sprite.sheet.pos.y
            self.sprite.sheet.frame_index[1] = 5
            self.sprite.sheet.max_c = 1
        if interaction.get_key("right"):
            self.sprite.sheet.pos.x = self.player.sprite.sheet.pos.x + 70
            self.sprite.sheet.pos.y = self.player.sprite.sheet.pos.y
            self.sprite.sheet.frame_index[1] = 0
            self.sprite.sheet.max_c = 1

    def draw(self, canvas):
        self.sprite.sheet.draw(canvas)
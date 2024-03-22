from src.classes.Vector import Vector
from src.classes.Spritesheet import Spritesheet
from src.classes.Sprite import Sprite

SPEED = 15
class gun:
    def __init__(self, x,y,player):
        self.size = (20,10)
        self.sprite = Sprite("gun", x,y)
        self.sprite.sheet = Spritesheet("./assets/nelson.png",
            275,
            100, 9, 5,50,100)
        self.player = player
        self.sprite.sheet.pos.x = self.player.sprite.sheet.pos.x 
        self.sprite.sheet.pos.y = self.player.sprite.sheet.pos.y
        self.sprite.sheet.frame_index[1] = 1
        
            
    def update(self,interaction):
        self.sprite.sheet.pos.x = self.player.sprite.sheet.pos.x + 50
        self.sprite.sheet.pos.y = self.player.sprite.sheet.pos.y -10
        if interaction.get_key("a") and not self.sprite.blocked["left"]:
            self.sprite.vel.x -= SPEED
            # self.sprite.sheet.pos.x -= SPEED
            self.sprite.sheet.max_c = 4
            self.sprite.sheet.frame_index[1] = 0                                                       # CHOOSES THE ROW FROM THE SPRITESHEET
            self.sprite.sheet.next_frame()
        if interaction.get_key("d") and not self.sprite.blocked["right"]:
            self.sprite.vel.x += SPEED
            self.sprite.sheet.max_c = 4
            # self.sprite.sheet.pos.x += SPEED

            self.sprite.sheet.frame_index[1] = 1                                                        # CHOOSES THH ROW FROM THE SPRITESHEET
            self.sprite.sheet.next_frame()

         
    def draw(self,canvas):
        self.sprite.sheet.draw(canvas)
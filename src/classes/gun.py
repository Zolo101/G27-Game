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
   
        
            
    def update(self):
        self.sprite.sheet.pos.x = self.player.sprite.sheet.pos.x + 50
        self.sprite.sheet.pos.y = self.player.sprite.sheet.pos.y -10


         
    def draw(self,canvas):
        self.sprite.sheet.draw(canvas)
from src.classes.Vector import Vector
from src.classes.Spritesheet import Spritesheet
from src.classes.Sprite import Sprite
class gun:
    def __init__(self, x,y):
        self.size = (20,10)
        self.sprite = Sprite("gun", x,y)
        self.sprite.sheet = Spritesheet("./assets/guns.png",
            500,
            160, 9, 5,50,100)
        self.sprite.sheet.pos.x = x
        self.sprite.sheet.pos.y = y
            
    def draw(self,canvas):
        self.sprite.sheet.draw(canvas)
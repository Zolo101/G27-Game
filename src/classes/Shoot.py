from src.classes.Sprite import Sprite
from src.classes.Spritesheet import Spritesheet
from src.classes.Bullet import Bullet
from src.classes.Vector import Vector


BULLET_SPEED = 20

class Shoot:
    def __init__(self,player):
        """ Initialises the bullets list and the player information """
        self.bullets = []
        self.player = player
        self.sprite = Sprite("shoot", self.player.sprite.sheet.pos.x, self.player.sprite.sheet.pos.y)

    def update(self,interaction):
        """ Shoots left or right depending on the user input """
        if interaction.get_key("left") and not interaction.get_key("right"):
            if interaction.get_key("up"):
                self.bullets.append(Bullet((self.player.sprite.sheet.pos.x - 77, self.player.sprite.sheet.pos.y - 7), (-BULLET_SPEED, 0)))
                if interaction.get_key("space"):
                    self.bullets.append(
                        Bullet((self.player.sprite.sheet.pos.x - 77, self.player.sprite.sheet.pos.y - 7), (-BULLET_SPEED, 0)))
        if interaction.get_key("right") and not interaction.get_key("left"):
            if interaction.get_key("up"):
                self.bullets.append(Bullet((self.player.sprite.sheet.pos.x + 77, self.player.sprite.sheet.pos.y - 7), (BULLET_SPEED, 0)))
                if interaction.get_key("space"):
                    self.bullets.append(
                        Bullet((self.player.sprite.sheet.pos.x + 77, self.player.sprite.sheet.pos.y - 7), (BULLET_SPEED, 0)))

        for bullet in self.bullets:
            bullet.update()
            print(bullet.pos.x)

    def check_collision(self, terrain):
        for bullet in self.bullets:
            bullet_nearest = bullet.pos.snap(Vector(20, 20))

            conditions = (
                    (bullet_nearest.x, bullet_nearest.y) in terrain.blocks or
                    0 > bullet_nearest.x or
                    1600 < bullet_nearest.x or
                    bullet_nearest.y < 0
            )

            if conditions:
                self.bullets.remove(bullet)

    def draw(self, canvas):
        for bullet in self.bullets:
            bullet.draw(canvas)
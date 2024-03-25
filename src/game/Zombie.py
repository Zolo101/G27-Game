from src.classes.Sprite import Sprite
from src.classes.Spritesheet import Spritesheet


JUMP_POWER = 40 / 4


class Zombie:
    def __init__(self, x, y, player,bullets, health = 50, max_health = 50,SPEED = 2):
        self.bullets = bullets
        self.size = (75, 200)
        self.sprite = Sprite("zombie", x, y)
        self.sprite.sheet = Spritesheet(
            "./assets/zombie_spritesheet.png",
            288,
            256, 9, 8,80,200)


        self.sprite.sheet.pos.x = x
        self.sprite.sheet.pos.y = y
        self.sprite.sheet.frame_index[1] = 1
        self.sprite.sheet.max_c = 2

        # self.sprite.pos.x = x
        # self.sprite.pos.y = y
        self.player = player
        self.health = health
        self.max_health = max_health
        self.SPEED = SPEED

    def update(self):
        if self.player.sprite.sheet.pos.x < self.sprite.pos.x:
            self.sprite.pos.x -= self.SPEED
            # self.sprite.sheet.frame_width = -(self.sprite.sheet.frame_width)
            self.sprite.sheet.frame_index[1] = 5
            self.sprite.sheet.next_frame()
        if self.player.sprite.sheet.pos.x > self.sprite.pos.x:
            self.sprite.pos.x += self.SPEED
            # self.sprite.sheet.frame_width = (self.sprite.sheet.frame_width)
            self.sprite.sheet.frame_index[1] = 1
            self.sprite.sheet.next_frame()
        if (self.sprite.pos.x > self.player.sprite.sheet.pos.x) and (self.sprite.pos.x < self.player.sprite.sheet.pos.x + 20) and (self.sprite.pos.y > self.player.sprite.sheet.pos.y - 80) and (self.sprite.pos.y < self.player.sprite.sheet.pos.y + 80) :
            self.player.take_damage(1)


        if  self.bullets.sprite.pos.x < self.sprite.pos.x:
            self.sprite.sheet.pos.x = 1000
            self.sprite.sheet.next_frame()


        if self.sprite.blocked["left"] or self.sprite.blocked["right"]:
            self.sprite.vel.y -= JUMP_POWER
            self.sprite.sheet.next_frame()

        # self.sprite.sheet.next_frame()
        self.sprite.sheet.max_c = 2
        self.sprite.update()


    def progres_dif(self):
        self.health += 20
        self.max_health +=20
        self.SPEED += 2

    def zombie_take_damage(self, amount):
        self.health -= amount
        
        

    def draw(self, canvas):
        """ This gets run on every frame. """
        # self.sprite.draw(canvas)
        canvas.draw_polygon([
            (self.sprite.pos.x, self.sprite.pos.y),
            (self.sprite.pos.x + self.size[0], self.sprite.pos.y),
            (self.sprite.pos.x + self.size[0], self.sprite.pos.y + self.size[1]),
            (self.sprite.pos.x, self.sprite.pos.y + self.size[1])],
            0,
            "red",
            "red"
        )
        #
        # canvas.draw_polygon([
        #     (self.sprite.pos.x, self.sprite.pos.y),
        #     (self.sprite.pos.x + 10, self.sprite.pos.y),
        #     (self.sprite.pos.x + 10, self.sprite.pos.y + 10),
        #     (self.sprite.pos.x, self.sprite.pos.y + 10)],
        #     0,
        #     "blue",
        #     "blue"
        # )
        self.sprite.sheet.draw(canvas)

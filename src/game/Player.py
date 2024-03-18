from src.classes.Sprite import Sprite
from src.classes.Spritesheet import Spritesheet

SPEED = 15
JUMP_POWER = 24


class Player:
    def __init__(self, x, y, name, level=1, health=100, max_health=100):
        self.size = (30, 75)
        self.sprite = Sprite("player")
        # self.sprite.texture.pos.x = 300
        # self.sprite.texture.pos.y = 300
        self.sprite.sheet = Spritesheet(
            "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8a072d29-42bc-45bb-be7b-cd731544eac2/degnka6-ae982415-ae64-485b-a2e9-04d30aeb9141.png/v1/fill/w_640,h_840/wonderland_player_spritesheet_by_littlestarsowo_degnka6-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODQwIiwicGF0aCI6IlwvZlwvOGEwNzJkMjktNDJiYy00NWJiLWJlN2ItY2Q3MzE1NDRlYWMyXC9kZWdua2E2LWFlOTgyNDE1LWFlNjQtNDg1Yi1hMmU5LTA0ZDMwYWViOTE0MS5wbmciLCJ3aWR0aCI6Ijw9NjQwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.b46AhMWfR3ygLqYMAhNkdrAuIsnDj_iKiV52391Nj5w",
            640,
            210, 4, 1)
        self.sprite.sheet.pos.x = 640
        self.sprite.sheet.pos.y = 560

    def update(self, interaction):
        # print(interaction.get_key("space"))
        # convert interaction keys to velocity
        if interaction.get_key("space") and self.sprite.grounded:
            self.sprite.vel.y -= JUMP_POWER

        if interaction.get_key("a"):
            self.sprite.pos.x -= SPEED
            self.sprite.sheet.pos.x -= SPEED
            self.sprite.sheet.next_frame()
        if interaction.get_key("d"):
            self.sprite.pos.x += SPEED
            self.sprite.sheet.pos.x += SPEED
            self.sprite.sheet.next_frame()

        self.sprite.update()

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        if self.health <= 0:
            return False

    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health

    def __str__(self):
        return f"{self.name} (Level {self.level}) - Health: {self.health}/{self.max_health}"

    def draw(self, canvas):

        # self.sprite.draw(canvas)
        # canvas.draw_polygon([
        #     (self.sprite.pos.x, self.sprite.pos.y),
        #     (self.sprite.pos.x + self.size[0], self.sprite.pos.y),
        #     (self.sprite.pos.x + self.size[0], self.sprite.pos.y + self.size[1]),
        #     (self.sprite.pos.x, self.sprite.pos.y + self.size[1])],
        #     0,
        #     "blue",
        #     "blue"
        # )

        self.sprite.sheet.draw(canvas)
        # self.sprite.texture_idle.draw(canvas)
        # self.sprite.texture_right.draw(canvas)

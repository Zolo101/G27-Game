from src.classes.Sprite import Sprite
from src.classes.Spritesheet import Spritesheet
from src.classes import Music
global SPEED
SPEED = 2.5
JUMP_POWER = 24 * 4

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Player:
    """
    Contains the `Sprite`, along with the health of the player.
    """

    def __init__(self, x, y, level=1, health=100, max_health=100):
        self.size = (50, 120)
        self.sprite = Sprite("player", x, y)
        self.sprite.sheet = Spritesheet(
            "./assets/player_spritesheet.png",
            640,
            840, 4, 4, 140,213)
        # https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8a072d29-42bc-45bb-be7b-cd731544eac2/degnka6-ae982415-ae64-485b-a2e9-04d30aeb9141.png/v1/fill/w_640,h_840/wonderland_player_spritesheet_by_littlestarsowo_degnka6-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODQwIiwicGF0aCI6IlwvZlwvOGEwNzJkMjktNDJiYy00NWJiLWJlN2ItY2Q3MzE1NDRlYWMyXC9kZWdua2E2LWFlOTgyNDE1LWFlNjQtNDg1Yi1hMmU5LTA0ZDMwYWViOTE0MS5wbmciLCJ3aWR0aCI6Ijw9NjQwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.b46AhMWfR3ygLqYMAhNkdrAuIsnDj_iKiV52391Nj5w
        self.sprite.sheet.pos.x = 11111111
        self.sprite.sheet.pos.y = 11111111

        self.level = level
        self.money = 0
        self.score = 0
        self.time_survived = 0
        self.health = health
        self.max_health = max_health
        self.speed = 2.5
        self.night = 0

    def update(self, interaction):
        """ This gets run on every frame. """
        # print(interaction.get_key("space"))
        # convert interaction keys to velocity
        self.sprite.sheet.frame_index[1] = 0

        #jumping
        if interaction.get_key("space") and self.sprite.grounded:
            self.sprite.vel.y -= JUMP_POWER

        #moving left
        if interaction.get_key("a") and not self.sprite.blocked["left"]:
            self.sprite.vel.x -= SPEED
            self.sprite.sheet.max_c = 4
            self.sprite.sheet.frame_index[1] = 1                                                        # CHOOSES THE ROW FROM THE SPRITESHEET
            self.sprite.sheet.next_frame()

        #moving right
        if interaction.get_key("d") and not self.sprite.blocked["right"]:
            self.sprite.vel.x += SPEED
            self.sprite.sheet.max_c = 4
            self.sprite.sheet.frame_index[1] = 2                                                        # CHOOSES THH ROW FROM THE SPRITESHEET
            self.sprite.sheet.next_frame()

        #gun appears to the left of the player
        if interaction.get_key("left"):
            self.sprite.sheet.frame_index[1] = 1

        #gun appear on the right
        if interaction.get_key("right"):
            self.sprite.sheet.frame_index[1] = 2


        self.sprite.update()

    #heals the player
    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    #deals damage to the player
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    #checks if alive
    def is_alive(self):
        return self.health > 0

    #levels up the player
    def level_up(self):
        """ Increments the player level by 1, along with increases their health. """
        self.level += 1
        self.max_health += 10
        self.health = self.max_health

    #earns money
    def earn(self, amount):
        self.money += amount

    #increase score
    def increaseScore(self, amount):
        self.score += amount

    #increase time_survived
    def increaseTimeSurvived(self, amount):
        self.time_survived += amount


    def barry_allen(self):
        global SPEED
        SPEED = 2.5

    def flash(self):
        global SPEED
        SPEED = 4
        timer = simplegui.create_timer(5000, self.barry_allen)
        timer.start()

    def __str__(self):
        return f"{self.name} (Level {self.level}) - Health: {self.health}/{self.max_health}"

    def draw(self, canvas):
        """ This gets run on every frame. """
        self.increaseTimeSurvived(0.02)
        # print(self.sprite.blocked)

        # debug
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

        # self.sprite.sheet.draw(canvas)
        # self.sprite.texture_idle.draw(canvas)
        # self.sprite.texture_right.draw(canvas)
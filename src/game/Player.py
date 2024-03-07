from src.classes.Sprite import Sprite


class Player:
    def __init__(self):
        self.sprite = Sprite("player")

    def update(self, interaction):
        # convert interaction keys to velocity
        self.sprite.update()

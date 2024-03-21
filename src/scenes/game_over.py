from src.classes.SceneManager import Scene


def draw(manager, canvas, clock, frame, interaction):
    """ This gets run on every frame. """
    print("you are drawing the game_over scene!")


def tick():
    pass


game_over = Scene("game_over", draw, tick)

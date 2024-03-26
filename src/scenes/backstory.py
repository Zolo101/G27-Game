from src.classes.SceneManager import Scene


def draw(manager, canvas, clock, frame, interaction):
    """ This gets run on every frame. """
    frame.set_canvas_background('rgb(100,5,25)')


    canvas.draw_text('Press \' space \' to start game', (720, 760), 20, 'Yellow', 'sans-serif')
    canvas.draw_text('Press \' i \' to go back to welcome screen', (320, 760), 20, 'Yellow', 'sans-serif')

    if interaction.get_key("space"):
        manager.switch_scene("main")
    if interaction.get_key("i"):
        manager.switch_scene("welcome")


def tick(manager, clock, frame, interaction):
    pass


backstory = Scene("backstory", draw, tick)

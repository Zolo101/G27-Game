from src.classes.SceneManager import Scene


def draw(manager, canvas, clock, frame, interaction):
    """ This gets run on every frame. """
    frame.set_canvas_background('rgb(255, 0, 10)')
    canvas.draw_text('G A M E  O V E R', (462, 408), 50, 'Black',
                     'sans-serif')  # POSITION IS THE BOTTOM LEFT OF TEXT
    canvas.draw_text('G A M E  O V E R', (465, 410), 50, 'Yellow',
                     'sans-serif')  # POSITION IS THE BOTTOM LEFT OF TEXT
    canvas.draw_text('Press \'p\' to play again', (540, 750), 20, 'Yellow', 'sans-serif')
    # print(frame.get_canvas_textheight('Welcome to Base 27 !',50))
    if interaction.get_key("p"):
        manager.switch_scene("welcome")


def tick(manager, clock, frame, interaction):
    pass


game_over = Scene("game_over", draw, tick)

from src.classes.SceneManager import Scene
from src.scenes.main import player


def draw(manager, canvas, clock, frame, interaction):
    """ This gets run on every frame. """
    frame.set_canvas_background('rgb(255, 0, 10)')
    canvas.draw_text('G A M E  O V E R', (462, 408), 50, 'Black',
                     'sans-serif')  # POSITION IS THE BOTTOM LEFT OF TEXT
    canvas.draw_text('G A M E  O V E R', (465, 410), 50, 'Yellow',
                     'sans-serif')  # POSITION IS THE BOTTOM LEFT OF TEXT
    canvas.draw_text('Press \'c\' to close game', (540, 750), 20, 'Yellow', 'sans-serif')
    # print(frame.get_canvas_textheight('Welcome to Base 27 !',50))

    #Display Score
    canvas.draw_text(f"Score: {player.score}", (522, 488), 60, "Black")
    canvas.draw_text(f"Score: {player.score}", (525, 490), 60, "Yellow")
    # canvas.draw_text(f"Score: {night_count}", (50, 50), 40, 'White', 'sans-serif')

    #Display Time Survived
    canvas.draw_text(f"Time Survived: {player.time_survived}", (422, 568), 60, "Black")
    canvas.draw_text(f"Time Survived: {player.time_survived}", (425, 570), 60, "Yellow") 

    if interaction.get_key("c"):
        # manager.switch_scene("welcome")
        frame.stop()

def tick(manager, clock, frame, interaction):
    pass


game_over = Scene("game_over", draw, tick)

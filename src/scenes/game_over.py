from src.classes.SceneManager import Scene
from src.scenes.main import player
from src.scenes.main import night_count


def draw(manager, canvas, clock, frame, interaction):
    """ This gets run on every frame. """
    frame.set_canvas_background('rgb(204, 14, 10)')
    canvas.draw_text('G A M E  O V E R', (357, 248), 75, 'Black')  # POSITION IS THE BOTTOM LEFT OF TEXT
    canvas.draw_text('G A M E  O V E R', (360, 250), 75, 'Yellow')  # POSITION IS THE BOTTOM LEFT OF TEXT
    canvas.draw_text('Press \'c\' to close game', (540, 750), 20, 'Yellow', 'sans-serif')
    # print(frame.get_canvas_textheight('Welcome to Base 27 !',50))

    #Display Score
    # canvas.draw_text(f"Score: {player.score}", (522, 388), 60, "Black")
    # canvas.draw_text(f"Score: {player.score}", (525, 390), 60, "Yellow")
    if player.night > 1 or player.night==0:
        canvas.draw_text(f"YOU SURVIVED {player.night} NIGHTS", (277, 413), 60, "Black")
        canvas.draw_text(f"YOU SURVIVED {player.night} NIGHTS", (280, 415), 60, "Yellow")

    if player.night == 1:
        canvas.draw_text(f"YOU SURVIVED {player.night} NIGHT", (277, 413), 60, "Black")
        canvas.draw_text(f"YOU SURVIVED {player.night} NIGHT", (280, 415), 60, "Yellow")


    #Display Time Survived
    canvas.draw_text(f"Time Survived: {player.time_survived}", (422, 493), 60, "Black")
    canvas.draw_text(f"Time Survived: {player.time_survived}", (425, 495), 60, "Yellow")

    canvas.draw_text(f"Score: {player.score}", (522, 573), 60, "Black")
    canvas.draw_text(f"Score: {player.score}", (525, 575), 60, "Yellow")
    #
    # canvas.draw_text(f"YOU SURVIVED {player.time_survived} NIGHTS", (277, 548), 60, "Black")
    # canvas.draw_text(f"YOU SURVIVED {player.time_survived} NIGHTS", (280, 550), 60, "Yellow")

    if interaction.get_key("c"):
        # manager.switch_scene("welcome")
        frame.stop()

def tick(manager, clock, frame, interaction):
    pass


game_over = Scene("game_over", draw, tick)

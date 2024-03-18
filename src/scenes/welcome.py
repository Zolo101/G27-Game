from src.classes.SceneManager import Scene
import random

def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

def draw(manager, canvas, clock, frame, interaction):
    """ This gets run on every frame. """
    frame.set_canvas_background('rgb(0,5,25)')
    canvas.draw_text('W e l c o m e  t o  B a s e  2 7 !', (320, 410), 50, 'White','sans-serif')                                        # POSITION IS THE BOTTOM LEFT OF TEXT
    canvas.draw_text('Press \'spacebar\' to start game', (520, 750), 20, 'Yellow', 'sans-serif')
    # print(frame.get_canvas_textheight('Welcome to Base 27 !',50))
    if interaction.get_key("space"):
        manager.switch_scene("main")








welcome = Scene("welcome", draw)

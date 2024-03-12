from src.classes.SceneManager import Scene
import random

def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

def draw(manager, canvas, clock, frame, interaction):
    frame.set_canvas_background('rgb(0,5,25)')
    canvas.draw_text('Welcome to Base 27!', (420, 410), 50, 'White','sans-serif')                                        # POSITION IS THE BOTTOM LEFT OF TEXT
    # print(frame.get_canvas_textheight('Welcome to Base 27 !',50))


    # This is how you would switch to the main scene
    # manager.switch_scene("main")






welcome = Scene("welcome", draw)

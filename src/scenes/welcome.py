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
    canvas.draw_text('W e l c o m e  t o  B a s e  2 7 !', (240, 110), 70, 'White','sans-serif')                                        # POSITION IS THE BOTTOM LEFT OF TEXT

    canvas.draw_text('[ a ]  =  MOVE LEFT ', (225, 310), 40, 'White', 'sans-serif')
    canvas.draw_text('[ d ]  =  MOVE RIGHT ', (225, 450), 40, 'White', 'sans-serif')
    canvas.draw_text('[ space ]  =  JUMP ', (225, 590), 40, 'White', 'sans-serif')
    canvas.draw_text('[ < ]  =  AIM LEFT ', (785, 310), 40, 'White', 'sans-serif')
    canvas.draw_text('[ > ]  =  AIM RIGHT ', (785, 450), 40, 'White', 'sans-serif')
    canvas.draw_text('[ ^ ]  =  SHOOT ', (785, 590), 40, 'White', 'sans-serif')

    canvas.draw_text('Press \'spacebar\' to start game', (520, 750), 20, 'Yellow', 'sans-serif')

    if interaction.get_key("space"):
        manager.switch_scene("main")


def tick(manager, clock, frame, interaction):
    pass


welcome = Scene("welcome", draw, tick)

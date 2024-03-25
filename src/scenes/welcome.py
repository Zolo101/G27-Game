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
    canvas.draw_text('W e l c o m e  t o  B a s e  2 7 !', (247, 110), 70, 'White','sans-serif')                                        # POSITION IS THE BOTTOM LEFT OF TEXT

    canvas.draw_text('CONTROLS', (540, 250), 40, 'White', 'sans-serif')
    canvas.draw_text('[ a ]  =  MOVE LEFT ', (260, 350), 40, 'White', 'sans-serif')
    canvas.draw_text('[ d ]  =  MOVE RIGHT ', (260, 462.5), 40, 'White', 'sans-serif')
    canvas.draw_text('[ space ]  =  JUMP ', (260, 570), 40, 'White', 'sans-serif')
    canvas.draw_text('[ < ]  =  AIM LEFT ', (700, 350), 40, 'White', 'sans-serif')
    canvas.draw_text('[ > ]  =  AIM RIGHT ', (700, 462.5), 40, 'White', 'sans-serif')
    canvas.draw_text('[ ^ ]  =  SHOOT ', (700, 570), 40, 'White', 'sans-serif')

    canvas.draw_text('©GROUP-XXVII', (1185, 793), 15, 'White', 'sans-serif')

    canvas.draw_polygon([(200,260), (1080,260), (1080,645), (200,645)], 2, 'White')

    canvas.draw_text('Press \'spacebar\' to start game', (520, 750), 20, 'Yellow', 'sans-serif')

    if interaction.get_key("space"):
        manager.switch_scene("main")


def tick(manager, clock, frame, interaction):
    pass


welcome = Scene("welcome", draw, tick)

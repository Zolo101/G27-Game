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
    canvas.draw_text('[ a ]  =  MOVE LEFT ', (256, 350), 30, 'White', 'sans-serif')
    canvas.draw_text('[ d ]  =  MOVE RIGHT ', (256, 425), 30, 'White', 'sans-serif')
    canvas.draw_text('[ space ]  =  JUMP ', (256, 500), 30, 'White', 'sans-serif')

    canvas.draw_text('[ < ]  =  AIM LEFT ', (768, 350), 30, 'White', 'sans-serif')
    canvas.draw_text('[ > ]  =  AIM RIGHT ', (768, 425), 30, 'White', 'sans-serif')
    canvas.draw_text('[ ^ ]  =  SHOOT ', (768, 500), 30, 'White', 'sans-serif')

    canvas.draw_text('[ left shift ]  =  BUILD MODE ', (256, 575), 30, 'White', 'sans-serif')
    canvas.draw_text('[ mouse ]  =  BUILD MODE ', (256, 650), 30, 'White', 'sans-serif')

    canvas.draw_text('[ e ]  =  EQUIP PERKS ', (768, 575), 30, 'White', 'sans-serif')
    canvas.draw_text('[ lmb ]  =  PLACE BLOCK ', (768, 650), 30, 'White', 'sans-serif')




    canvas.draw_text('©GROUP-XXVII', (1185, 793), 15, 'White', 'sans-serif')

    # canvas.draw_polygon([(200,260), (1080,260), (1080,645), (200,645)], 2, 'White')

    canvas.draw_text('Press \' space \' to start game', (720, 760), 20, 'Yellow', 'sans-serif')
    canvas.draw_text('Press \' i \' to view game backstory', (320, 760), 20, 'Yellow', 'sans-serif')

    if interaction.get_key("space"):
        manager.switch_scene("main")
    if interaction.get_key("i"):
        manager.switch_scene("backstory")


def tick(manager, clock, frame, interaction):
    pass


welcome = Scene("welcome", draw, tick)

from src.classes.SceneManager import Scene
import random

def randCol():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

def draw(game, canvas):
    """ This gets run on every frame. """
    game.frame.set_canvas_background('black')

    canvas.draw_text('CONTROLS', (520, 80), 40, 'White')

    canvas.draw_text('[ a ]  =  MOVE LEFT ', (256, 250), 30, 'White')
    canvas.draw_text('[ d ]  =  MOVE RIGHT ', (256, 325), 30, 'White')
    canvas.draw_text('[ space ]  =  JUMP ', (256, 400), 30, 'White')
    canvas.draw_text('[ left shift ]  =  BUILD MODE ', (256, 475), 30, 'White')
    canvas.draw_text('[ mouse ]  =  AIM BUILD ', (256, 550), 30, 'White')

    canvas.draw_text('[ < ]  =  AIM LEFT ', (708, 250), 30, 'White')
    canvas.draw_text('[ > ]  =  AIM RIGHT ', (708, 325), 30, 'White')
    canvas.draw_text('[ ^ ]  =  SHOOT ', (708, 400), 30, 'White')
    canvas.draw_text('[ e ]  =  EQUIP PERKS ', (708, 475), 30, 'White')
    canvas.draw_text('[ lmb ]  =  PLACE BLOCK ', (708, 550), 30, 'White')







    canvas.draw_text('©GROUP-XXVII', (1165, 793), 15, 'White', 'sans-serif')

    # canvas.draw_polygon([(200,260), (1080,260), (1080,645), (200,645)], 2, 'White')

    canvas.draw_text('Press \' space \' to start game', (720, 760), 20, 'Yellow', 'sans-serif')
    canvas.draw_text('Press \' o \' to go back to welcome screen', (320, 760), 20, 'Yellow', 'sans-serif')

    if game.control.get_key("space"):
        game.start()
    if game.control.get_key("o"):
        game.manager.switch_scene("welcome")


def tick(game):
    pass


controls = Scene("controls", draw, tick)
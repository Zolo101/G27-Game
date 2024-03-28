from src.classes.SceneManager import Scene
import random

def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

def draw(game, canvas):
    """ This gets run on every frame. """
    game.frame.set_canvas_background('rgb(0,5,25)')
    canvas.draw_text('F I V E  N I G H T S  A T  F O U N D E R S', (147, 110), 55, 'White')
    canvas.draw_text('F.K.A  B A S E  2 7', (560, 158), 20, 'White')


    canvas.draw_text('Welcome to Five Nights at Founders!. Once every 3600 years, ',
                     (218, 305), 30, 'White')
    canvas.draw_text('zombies in Egham come out of hibernation to find humans as a',
                     (218, 340), 30, 'White')
    canvas.draw_text('source of food. Their hunt period lasts for eight days. After three ',
                     (218, 375), 30, 'White')
    canvas.draw_text('days, it was told that no one survived. Or did they...',
                     (218, 410), 30, 'White')
    canvas.draw_text('You will be playing Alex, who is the last person alive in this eight day',
                     (218, 455), 30, 'White')
    canvas.draw_text('apocolypse. You will be tasked to survive the next five nights. To help ',
                     (218, 490), 30, 'White')
    canvas.draw_text('you in your survival journey, you will be equipped with a self made',
                     (218, 525), 30, 'White')
    canvas.draw_text('flamethrower straight from the Bourne Annex and, by using the ',
                     (218, 560), 30, 'White')
    canvas.draw_text('Yendollars you earn from eliminating zombies, you will have the',
                     (218, 595), 30, 'White')
    canvas.draw_text('ability to build defences.',
                     (218, 630), 30, 'White')
    canvas.draw_text('©GROUP-XXVII', (1165, 793), 15, 'White', 'sans-serif')

    canvas.draw_polygon([(200,260), (1080,260), (1080,645), (200,645)], 2, 'White')

    canvas.draw_text('Press \' space \' to start game', (720, 760), 20, 'Yellow', 'sans-serif')
    canvas.draw_text('Press \' i \' to view controls', (320, 760), 20, 'Yellow', 'sans-serif')

    if game.control.get_key("space"):
        game.start()
    if game.control.get_key("i"):
        game.manager.switch_scene("controls")


def tick(game):
    pass


welcome = Scene("welcome", draw, tick)
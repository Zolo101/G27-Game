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
    # canvas.draw_text('His name was John, John Trump. He was a simple man from Barwickia, a small kingdom North of the Uatford Empire. '
    #                  '\nFive years ago John has embarked on a journey that will change his life. The journey is full of betrayal, hope, love and pain. \nJohn has got a fifty year mortgage on a house at nine percent interest rate. This morning however his simple life of working twelve hours a day seven days a week, with 2 weeks of paid vacation, has been interrupted by the zombies.\n Now his very own life is at risk. But John was a very conservative man, as a fiscally responsible adult, he understood the enormity of what was at stake.\n If he gave way to zombies and let them destroy his house, he would have to keep paying for his mortgage and also pay rent for his apartament.\n His credit score would also drop by over two hundred points.\n That John could not allow...',
    #                  (220, 480), 20, 'Yellow', 'sans-serif')
    # print(frame.get_canvas_textheight('Welcome to Base 27 !',50))
    if interaction.get_key("space"):
        manager.switch_scene("main")


def tick(manager, clock, frame, interaction):
    pass


welcome = Scene("welcome", draw, tick)

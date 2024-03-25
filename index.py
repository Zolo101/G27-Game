from src.classes.Clock import Clock
from src.classes.Interaction import Interaction
from src.classes.SceneManager import SceneManager, Scene
from src.scenes.game_over import game_over
from src.scenes.main import main
from src.scenes.welcome import welcome

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# fonts = simplegui.Text.fonts_installed_list()
# player = Spritesheet()
# interaction = Interaction()
WIDTH, HEIGHT = (1280, 800)

frame = simplegui.create_frame("base 27", 2560 / 2, 800, 0)

manager = SceneManager()

manager.add_scene(welcome)
manager.add_scene(main)
# manager.add_scene(upgrades)
manager.add_scene(game_over)

manager.switch_scene("main")

clock = Clock()
interaction = Interaction(simplegui.KEY_MAP)


def e():
    manager.tick(clock, frame, interaction)


timer = simplegui.create_timer(8, e)


def draw(canvas):
    """ This gets run on every frame. """
    manager.draw(canvas, clock, frame, interaction)
    # manager.tick(canvas, clock, frame, interaction)
    # print(clock.time)
    # clock.tick()
    # frame._get_fps_average()


# Start game
frame.set_draw_handler(draw)
frame.set_keydown_handler(interaction.key_down)
frame.set_keyup_handler(interaction.key_up)
timer.start()
frame.start()
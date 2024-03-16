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


def draw(canvas):
    manager.draw(canvas, clock, frame, interaction)
    clock.tick()
    # frame._get_fps_average()


# Start game
frame.set_draw_handler(draw)
frame.set_keydown_handler(interaction.key_down)
frame.set_keyup_handler(interaction.key_up)
frame.start()

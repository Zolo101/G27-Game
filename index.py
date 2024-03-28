from src.classes.Clock import Clock
from src.classes.Interaction import Interaction
from src.classes.SceneManager import SceneManager, Scene
from src.scenes.game_over import game_over
from src.scenes.win import win
from src.scenes.main import main
from src.scenes.welcome import welcome
from src.scenes.backstory import backstory
from src.classes import Music

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
music = Music.music()


def collision_check():
    manager.tick(clock, frame, interaction)

# Start playing music
#music.play_music()

manager.add_scene(welcome)
manager.add_scene(main)
# manager.add_scene(upgrades)
manager.add_scene(game_over)
manager.add_scene(backstory)
manager.add_scene(win)

manager.switch_scene("game_over")

clock = Clock()
interaction = Interaction(simplegui.KEY_MAP | {"shift": 17})

timer = simplegui.create_timer(8, collision_check)


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
frame.set_mouseclick_handler(interaction.mouse_click)
frame.set_mousedrag_handler(interaction.mouse_click)
timer.start()
frame.start()

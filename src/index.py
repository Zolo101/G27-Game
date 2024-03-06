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
WIDTH, HEIGHT = (2560 // 2, 800)


manager = SceneManager()

manager.add_scene(welcome)
manager.add_scene(main)
# manager.add_scene(upgrades)
manager.add_scene(game_over)

manager.switch_scene("main")


def draw(canvas):
    manager.draw(canvas)
    # terrain.draw(canvas)


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("game-27", 2560 / 2, 800, 0)
frame.set_draw_handler(draw)
frame.set_canvas_background("cyan")

# Start the frame animation
frame.start()

from src.game.Terrain import Terrain

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# player = Spritesheet()
# interaction = Interaction()
WIDTH, HEIGHT = (2560 // 2, 800)

terrain = Terrain(WIDTH, HEIGHT)


def draw(canvas):
    terrain.draw(canvas)


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("game-27", 2560 / 2, 800, 0)
frame.set_draw_handler(draw)
frame.set_canvas_background("cyan")


# Start the frame animation
frame.start()

from src.game.Terrain import Terrain

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# player = Spritesheet()
# interaction = Interaction()

terrain = Terrain()


def draw(canvas):
    terrain.draw(canvas)


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("game-27", 600, 400, 0)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()

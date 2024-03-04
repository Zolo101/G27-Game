from Interaction import Interaction
from Vector import Vector
from Spritesheet import Spritesheet

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# player = Spritesheet()
# interaction = Interaction()

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("game-27", 600, 400)
# frame.set_draw_handler()

# Start the frame animation
frame.start()

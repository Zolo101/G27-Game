from src.game.Game import Game

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

game = Game(simplegui)
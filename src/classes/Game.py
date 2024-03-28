from src.classes import Music
from src.classes.Builder import Builder
from src.classes.Clock import Clock
from src.classes.Cloud import Cloud
from src.classes.ControlManager import ControlManager
from src.classes.Interaction import Interaction
from src.classes.Pew import Pew
from src.classes.SceneManager import SceneManager
from src.classes.Shoot import Shoot
from src.game.Player import Player
from src.game.Sky import Sky
from src.game.Terrain import Terrain
from src.game.wavemanager import WaveManager
from src.scenes.UI import UI
from src.scenes.backstory import backstory
from src.scenes.game_over import game_over
from src.scenes.main import main
from src.scenes.welcome import welcome
from src.scenes.win import win


# class DrawHandler:
#     def __init__(self, game, manager):
#         self.game = game
#         self.manager = manager
#
#     def draw(self, canvas):
#         """ This gets run on every frame. """
#         self.manager.draw(self.game, canvas)


class Game:
    def __init__(self, simplegui):
        width = 1280
        height = 800

        self.frame = simplegui.create_frame("base 27", 2560 / 2, 800, 0)

        self.manager = SceneManager()
        self.music = Music.music()

        # Start playing music
        #music.play_music()

        self.manager.add_scene(welcome)
        self.manager.add_scene(main)
        self.manager.add_scene(game_over)
        self.manager.add_scene(backstory)
        self.manager.add_scene(win)

        self.manager.switch_scene("welcome")

        self.clock = Clock()
        self.control = ControlManager(simplegui.KEY_MAP | {"shift": 17})

        self.timer = simplegui.create_timer(8, self.collision_check)

        # Start game
        self.terrain = Terrain(1280, 800)
        self.sky = Sky()
        self.player = Player(600, 0)
        self.builder = Builder()
        self.pew = Pew(self.player)
        self.ui = UI(self.player)
        self.shoot = Shoot(self.player)
        self.timer2 = 0
        self.hCount = 0
        self.sCount = 0
        self.night_count = 0
        self.zombies = []
        self.perks = []
        self.clouds = []
        self.wave_manager = WaveManager()
        self.interaction = Interaction()
        # self.draw_handler = DrawHandler(self, self.manager)

        self.frame.set_draw_handler(self.draw)
        self.frame.set_keydown_handler(self.control.key_down)
        self.frame.set_keyup_handler(self.control.key_up)
        self.frame.set_mouseclick_handler(self.control.mouse_click)
        self.frame.set_mousedrag_handler(self.control.mouse_click)
        self.timer.start()
        self.frame.start()

    def start(self):
        self.terrain = Terrain(1280, 800)
        self.sky = Sky()
        self.player = Player(600, 0)
        self.builder = Builder()
        self.pew = Pew(self.player)
        self.ui = UI(self.player)
        self.shoot = Shoot(self.player)

        self.hCount = 0
        self.sCount = 0
        self.timer2 = 0
        self.night_count = 0
        self.zombies.clear()
        self.perks.clear()
        self.clouds.clear()

        for i in range(1, 20):
            self.clouds.append(Cloud())

        self.wave_manager = WaveManager()

        self.manager.switch_scene("main")

    def collision_check(self):
        self.manager.tick(self)

    def draw(self, canvas):
        """ This gets run on every frame. """
        self.manager.draw(self, canvas)
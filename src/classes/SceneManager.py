# Switches scenes, etc
class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, scene):
        self.scenes[scene.name] = scene

    def switch_scene(self, scene_name):
        self.current_scene = self.scenes[scene_name]
        print(f"Switched to scene: {scene_name}")

    def draw(self, game, canvas):
        """ This gets run on every frame. """
        self.current_scene.draw(game, canvas)

    def tick(self, game):
        """ This gets run every 8ms for time sensitive functions such as collision """
        self.current_scene.tick(game)


# Scene
class Scene:
    def __init__(self, name, draw, tick):
        self.name = name
        self.draw = draw
        self.tick = tick

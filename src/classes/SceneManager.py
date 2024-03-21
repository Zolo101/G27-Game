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

    def draw(self, canvas, clock, frame, interaction):
        """ This gets run on every frame. """
        self.current_scene.draw(self, canvas, clock, frame, interaction)

    def tick(self, clock, frame, interaction):
        """ This gets run every 4 ms for time sensitive functions """
        self.current_scene.tick(self, clock, frame, interaction)


# Scene
class Scene:
    def __init__(self, name, draw, tick):
        self.name = name
        self.draw = draw
        self.tick = tick

# Switches scenes, etc
class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, scene):
        self.scenes[scene.name] = scene

    def switch_scene(self, scene_name):
        self.current_scene = self.scenes[scene_name]

    def draw(self, canvas):
        self.current_scene.draw(canvas)


# Scene
class Scene:
    def __init__(self, name, draw):
        self.name = name
        self.draw = draw
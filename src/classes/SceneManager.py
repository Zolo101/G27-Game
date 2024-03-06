class SceneManager:
    def __init__(self, scene):
        self.go_to(scene)

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self

    def run(self):
        self.scene.run()
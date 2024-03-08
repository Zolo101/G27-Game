class Zombie:
    def _init__(self, spawn_point, movement):
        self.spawn_point = spawn_point
        self.movement = movement
    
    def update(self, canvas):
        self.spawn_point.add(self.velocity)
        canvas.draw_circle((self.spawn_point.x, self.spawn_point.y), 20, 12, "red", "red") 

    def draw(self, canvas):
        canvas.draw_circle((500,500), 20, 12, "red", "red") 
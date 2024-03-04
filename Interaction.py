class Interaction:
    def __init__(self, wall, ball):
        self.ball = ball
        self.wall = wall

    def update(self):
        hit = self.wall.hit(self.ball)
        if hit and not self.ball.in_collision:
            self.ball.bounce(self.wall.normal)

        self.ball.in_collision = hit
        self.ball.update()

    def draw(self, canvas):
        self.update()
        self.ball.draw(canvas)
        self.wall.draw(canvas)
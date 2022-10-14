from ball import Ball
from brick import Brick


class Table:
    def __init__(self):
        self.bricks = [Brick(64, 200, 100, 32)]
        self.balls = [Ball(240, 600)]

    def update(self):
        for ball in self.balls:
            ball.update()

    def draw(self, win):
        for brick in self.bricks:
            brick.draw(win)

        for ball in self.balls:
            ball.draw(win)

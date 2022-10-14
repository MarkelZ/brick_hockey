from ball import Ball
from brick import Brick


class Table:
    def __init__(self):
        self.bricks = []
        self.balls = []

    def update(self):
        for ball in self.balls:
            ball.update()

    def draw(self, win):
        for brick in self.bricks:
            brick.draw(win)

        for ball in self.balls:
            ball.draw(win)

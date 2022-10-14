from ball import Ball
from brick import Brick
from pygame.math import Vector2
import config


class Table:
    def __init__(self):
        self.width = config.screenres[0]
        self.height = config.screenres[1]
        self.bricks = [Brick(100, 100, 100,  num=4),
                       Brick(200, 100, 100,  num=4),
                       Brick(300, 100, 100,  num=4),
                       Brick(400, 100, 100,  num=4),
                       Brick(100, 200, 100,  num=4),
                       Brick(200, 200, 100,  num=4)]
        self.balls = [Ball(self, Vector2(240, 600), Vector2(1, -1))]
        self.balls_to_remove = []
        self.sim_numiters = 1

    def update(self):
        # Update balls
        for ball in self.balls:
            ball.update()

        # Remove depleted bricks
        self.bricks = [b for b in self.bricks if b.num > 0]

        # Remove balls
        self.balls = [b for b in self.balls if b not in self.balls_to_remove]
        self.balls_to_remove = []

    def draw(self, sfc):
        # Draw bricks
        for brick in self.bricks:
            brick.draw(sfc)

        # Draw balls
        for ball in self.balls:
            ball.draw(sfc)

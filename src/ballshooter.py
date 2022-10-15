import pygame.gfxdraw
from ball import Ball
from pygame.math import Vector2
import numpy as np


class BallShooter:
    def __init__(self, table):
        self.table = table
        self.x = table.width / 2
        self.y = table.height - 16
        self.ball = Ball(table, Vector2(self.x, self.y), Vector2(1, 1))

    def _get_mouse_direction(self):
        return pygame.mouse.get_pos() - Vector2(self.x, self.y)

    def update(self):
        # Debug
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.shoot_ball()

    def shoot_ball(self):
        self.table.balls.append(
            Ball(self.table, Vector2(self.x, self.y), self._get_mouse_direction()))

    def draw(self, sfc):
        # Draw laser line
        # Give ball direction towards mouse pointer
        direction = self._get_mouse_direction().normalize()
        self.ball.d = Ball.DEFAULT_SPEED * direction

        # Calculate numsteps amount of steps of the ball
        numsteps = 256
        xx = [self.ball.p.x]
        yy = [self.ball.p.y]
        for _ in range(numsteps):
            self.ball.step(False)
            xx.append(self.ball.p.x)
            yy.append(self.ball.p.y)

        # Draw line segments of laser in reverse order to avoid overlap
        xyb = list(zip(xx, yy, np.linspace(1, 0.5, numsteps)))
        xyb.reverse()
        prev = Vector2(xx[-1], yy[-1])
        for (x, y, bright) in xyb:
            pos = Vector2(x, y)
            pygame.draw.line(sfc, (255 * bright, 0, 0), prev, pos, width=4)
            prev = pos

        # Draw ball
        self.ball.p = Vector2(self.x, self.y)
        self.ball.draw(sfc)

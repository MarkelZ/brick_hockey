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
        self.num_balls = 10
        self.balls_to_shoot = 0
        self.is_shooting = False
        self.shoot_delay = 3
        self.shoot_ctr = 0
        self.shoot_direction = None

    def _get_mouse_direction(self):
        return pygame.mouse.get_pos() - Vector2(self.x, self.y)

    def update(self):
        if self.is_shooting:
            if self.balls_to_shoot <= 0:
                self.is_shooting = False
            else:
                if self.shoot_ctr <= 0:
                    self.shoot_ctr = self.shoot_delay
                    self.table.balls.append(
                        Ball(self.table, Vector2(self.x, self.y), self.shoot_direction))
                    self.balls_to_shoot -= 1
                else:
                    self.shoot_ctr -= 1

    def shoot_balls(self):
        self.is_shooting = True
        self.balls_to_shoot = self.num_balls
        self.shoot_direction = self._get_mouse_direction()

    def draw(self, sfc, draw_laser=False):
        # Draw laser line
        if draw_laser:
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

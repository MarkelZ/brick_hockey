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
        self.shoot_timer = 0
        self.shoot_direction = None
        self.min_slope = -0.1

    def _get_mouse_direction(self):
        direction = pygame.mouse.get_pos() - Vector2(self.x, self.y)
        # If the slope of the direction is too horizontal,
        # then return a vector with the minimum allowed slope
        if direction.x != 0 and direction.y / abs(direction.x) >= self.min_slope:
            return Vector2(np.sign(direction.x), self.min_slope)
        else:
            return direction

    def update(self):
        if self.is_shooting:
            # If there are no balls to shoot left, stop shooting
            if self.balls_to_shoot <= 0:
                self.is_shooting = False
            else:
                # If timer is at 0, shoot
                if self.shoot_timer <= 0:
                    ball = Ball(self.table, Vector2(self.x, self.y),
                                self.shoot_direction)
                    self.table.balls.append(ball)
                    self.balls_to_shoot -= 1
                    self.shoot_timer = self.shoot_delay
                # If timer is not at 0, decrease timer by 1
                else:
                    self.shoot_timer -= 1

    # Start shooting balls (self.num_balls many)
    def shoot_balls(self):
        self.is_shooting = True
        self.balls_to_shoot = self.num_balls
        self.shoot_direction = self._get_mouse_direction()

    # Draw ballshooter
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

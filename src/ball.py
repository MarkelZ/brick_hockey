import pygame.gfxdraw
from pygame.math import Vector2


class Ball:
    DEFAULT_RADIUS = 4
    DEFAULT_SPEED = 10.0
    DEFAULT_COLOR = (255, 255, 255)

    def __init__(self, table, position, direction):
        self.table = table
        self.p = position
        self.d = Ball.DEFAULT_SPEED * Vector2.normalize(direction)
        self.radius = Ball.DEFAULT_RADIUS
        self.color = Ball.DEFAULT_COLOR

    def update(self):
        for _ in range(self.table.sim_numiters):
            self.step()

    def step(self, damage_brick=True):
        # Move ball
        self.p = self.p + self.d

        # Check if colliding with any of the bricks
        for brick in self.table.bricks:
            # (bx, by) is the position of the brick after moving ball to origin
            bx = brick.x - self.p.x
            by = brick.y - self.p.y
            # (bw, bh) is brick's bottom-right corner after moving ball to origin
            bw = bx + brick.size
            bh = by + brick.size
            # Check if ball is colliding with brick
            if bx < 0 and bw > 0 and by < 0 and bh > 0:
                # if damage_brick, subtract one point from brick
                if damage_brick:
                    brick.num -= 1

                # Determine in which direction the collision happened
                absx = abs(bx)
                absy = abs(by)
                mincolpoint = min(absx, absy, bw, bh)
                # Correct position and speed depending on
                # the direction in which the collision happened
                if absx == mincolpoint:
                    self.p.x = brick.x
                    self.d.x *= -1
                elif absy == mincolpoint:
                    self.p.y = brick.y
                    self.d.y *= -1
                elif bw == mincolpoint:
                    self.p.x = brick.x + brick.size
                    self.d.x *= -1
                else:
                    self.p.y = brick.y + brick.size
                    self.d.y *= -1

        # Bounce if ball is colliding with screen edges
        if self.p.x < 0:
            self.p.x = 0
            self.d.x *= -1
        if self.p.y < 0:
            self.p.y = 0
            self.d.y *= -1
        if self.p.x > self.table.width:
            self.p.x = self.table.width
            self.d.x *= -1

        # If the ball hits the bottom of the screen, delete
        if self.p.y > self.table.height:
            self.table.balls_to_remove.append(self)

    def draw(self, sfc):
        pygame.gfxdraw.aacircle(sfc, round(self.p.x), round(self.p.y),
                                self.radius, self.color)
        pygame.gfxdraw.filled_circle(
            sfc, round(self.p.x), round(self.p.y), self.radius, self.color)

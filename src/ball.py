from turtle import distance
import pygame.gfxdraw
from pygame.math import Vector2


class Ball:
    DEFAULT_RADIUS = 4
    DEFAULT_SPEED = 16.0
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

    def cross(v, w):
        return v.x * w.y - v.y * w.x

    # Get point of collision with collider
    # In case of no collision, return None
    # Source: https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
    def get_collision(self, prevpos, collider):
        p = prevpos
        r = self.p - prevpos
        q = Vector2(collider.x0, collider.y0)
        s = Vector2(collider.x1, collider.y1) - q
        crs = Ball.cross(r, s)

        # Lines are parallel
        if crs == 0:
            return None

        pq = q - p
        t = Ball.cross(pq, s) / crs
        u = Ball.cross(pq, r) / crs

        # Check if intersection is in both segments
        alpha = 0.000001
        if alpha < t < 1-alpha and alpha < u < 1-alpha:
            col = p + t * r
            return col
        else:
            return None

    def step(self, damage_brick=True):
        # Move ball
        prevpos = self.p
        self.p = self.p + self.d

        # Get collision points with bricks and screen edges
        collisions = [(self.get_collision(prevpos, col), col)
                      for col in self.table.colliders]
        collisions = [u for u in collisions if u[0] != None]

        # If there are any collisions, solve
        if len(collisions) > 0:
            # Find the closest collision
            mincol = min(collisions,
                         key=lambda u: prevpos.distance_squared_to(u[0]))

            # Move ball to collision point
            self.p = mincol[0]

            # Bounce ball
            if mincol[1].is_vertical:
                self.d.x *= -1
            else:
                self.d.y *= -1

            # Decrease brick's number
            if damage_brick and mincol[1].colobj != None:
                mincol[1].colobj.damage()

        # If the ball hits the bottom of the screen, delete
        if self.p.y > self.table.height:
            self.table.balls_to_remove.append(self)

    def draw(self, sfc):
        pygame.gfxdraw.aacircle(sfc, round(self.p.x), round(self.p.y),
                                self.radius, self.color)
        pygame.gfxdraw.filled_circle(
            sfc, round(self.p.x), round(self.p.y), self.radius, self.color)

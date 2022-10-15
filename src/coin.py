import pygame.gfxdraw
from pygame.math import Vector2


class Coin:
    def __init__(self, x, y):
        self.p = Vector2(x, y)
        self.radius = 24
        self.color = [255, 226, 128]
        self.triggered = False

    def update(self):
        pass

    def draw(self, sfc):
        pygame.gfxdraw.aacircle(sfc, round(self.p.x), round(self.p.y),
                                self.radius, self.color)
        pygame.gfxdraw.filled_circle(
            sfc, round(self.p.x), round(self.p.y), self.radius, self.color)

import pygame.gfxdraw


class Ball:
    DEFAULT_RADIUS = 8

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = Ball.DEFAULT_RADIUS
        self.color = (255, 255, 255)

    def update(self):
        pass

    def draw(self, win):
        pygame.gfxdraw.aacircle(win, self.x, self.y, self.radius, self.color)
        pygame.gfxdraw.filled_circle(
            win, self.x, self.y, self.radius, self.color)

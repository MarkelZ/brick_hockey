import pygame


class Brick:

    def __init__(self, num, x, y, size):
        self.num = num
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 100, 0)
        self.txtcolor = (0, 0, 0)
        self.font = pygame.font.Font('content/sans.ttf', round(size * 0.5))

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.size, self.size))
        textsurface = self.font.render(str(self.num), True, self.txtcolor)
        marginw = (self.size - textsurface.get_width()) / 2.0
        marginh = (self.size - textsurface.get_height()) / 2.0
        win.blit(textsurface, (self.x + marginw, self.y + marginh))

import pygame
from debugwriter import Debugwriter
import config


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(config.title)
        self.win = pygame.display.set_mode(config.screenres)
        self.dw = Debugwriter()

    def run(self):
        run = True
        while run:
            pygame.time.delay(round(1000 * config.spt))

            self.update()
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

    def update(self):
        self.dw.clear()
        self.dw.writeln('debug text here')

    def draw(self):
        self.dw.draw(self.win)
        pygame.display.update()

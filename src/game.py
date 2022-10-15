import imp
import pygame
from math import floor

from debugwriter import Debugwriter
from table import Table
from ball import Ball
from ballshooter import BallShooter
import config


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(config.title)
        self.win = pygame.display.set_mode(config.screenres)
        self.dw = Debugwriter()
        self.table = Table()
        self.bs = BallShooter(self.table)

    def run(self):
        run = True
        while run:
            pygame.time.delay(floor(1000 * config.spt))

            self.update()
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

    def update(self):
        self.dw.clear()

        self.bs.update()
        self.table.update()
        self.dw.writeln('Balls: ' + str(len(self.table.balls)))
        self.dw.writeln('Bricks: ' + str(len(self.table.bricks)))

    def draw(self):
        self.win.fill((0, 0, 0))
        self.bs.draw(self.win)
        self.table.draw(self.win)
        self.dw.draw(self.win)
        pygame.display.update()

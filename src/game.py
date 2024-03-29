import pygame
from math import floor

from gamestate import GameState
import config


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(config.title)
        self.win = pygame.display.set_mode(config.screenres)
        self.gamestate = GameState()
        self.clock = pygame.time.Clock()

    def run(self):
        run = True
        while run:
            self.clock.tick(config.tps)

            self.update()
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    self.gamestate.key_pressed(event.key)

    def update(self):
        self.gamestate.update()

    def draw(self):
        self.win.fill((0, 0, 0))
        self.gamestate.draw(self.win)
        pygame.display.update()

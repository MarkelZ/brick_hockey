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

    def run(self):
        run = True
        while run:
            pygame.time.delay(floor(1000 * config.spt))

            self.update()
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                # This is for debugging
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.gamestate.bs.shoot_ball()

    def update(self):
        self.gamestate.update()

    def draw(self):
        self.win.fill((0, 0, 0))
        self.gamestate.draw(self.win)
        pygame.display.update()

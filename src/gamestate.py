from lzma import is_check_supported
import pygame
from table import Table
from ballshooter import BallShooter
from debugwriter import DebugWriter


class GameState:
    def __init__(self):
        self.table = Table()
        self.bs = BallShooter(self.table)
        self.dw = DebugWriter()
        self.is_shooting = False

    def update(self):
        self.dw.clear()
        self.bs.update()
        self.table.update()
        self.dw.writeln(
            'Balls: ' + str(self.bs.num_balls if self.is_shooting else self.bs.balls_to_shoot))

        if self.is_shooting:
            # If space is pressed, shoot balls
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.bs.shoot_balls()
                self.is_shooting = False
        else:
            # If all balls are gone, switch to shooting state
            if len(self.table.balls) == 0 and not self.bs.is_shooting:
                self.is_shooting = True

    def draw(self, sfc):
        self.bs.draw(sfc, draw_laser=self.is_shooting)
        self.table.draw(sfc)
        self.dw.draw(sfc)

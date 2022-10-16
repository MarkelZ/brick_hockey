import pygame
from enum import Enum

from table import Table
from ballshooter import BallShooter
from debugwriter import DebugWriter


class State(Enum):
    SHOOTING = 0
    BOUNCING = 1


class GameState:
    def __init__(self):
        self.table = Table(self)
        self.bs = BallShooter(self.table)
        self.dw = DebugWriter()
        self.state = State.SHOOTING

    def update(self):
        self.dw.clear()
        self.bs.update()
        self.table.update()
        self.dw.writeln(
            'Balls: ' + str(self.bs.balls_to_shoot if self.state == State.BOUNCING else self.bs.num_balls))

        if self.state == State.SHOOTING:
            # If space is pressed, shoot balls
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.state = State.BOUNCING
                self.bs.shoot_balls()
        elif self.state == State.BOUNCING:
            # If all balls are gone, switch to shooting state
            if len(self.table.balls) == 0 and not self.bs.is_shooting:
                self.state = State.SHOOTING
                self.table.generate_and_shift_bricks()

    def draw(self, sfc):
        self.bs.draw(sfc, draw_laser=self.state == State.SHOOTING)
        self.table.draw(sfc)
        self.dw.draw(sfc)

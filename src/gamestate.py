import pygame
from table import Table
from ballshooter import BallShooter
from debugwriter import DebugWriter


class GameState:
    def __init__(self):
        self.table = Table()
        self.bs = BallShooter(self.table)
        self.dw = DebugWriter()

    def update(self):
        self.dw.clear()
        self.bs.update()
        self.table.update()
        self.dw.writeln('Balls: ' + str(len(self.table.balls)))
        self.dw.writeln('Bricks: ' + str(len(self.table.bricks)))

    def draw(self, sfc):
        self.bs.draw(sfc)
        self.table.draw(sfc)
        self.dw.draw(sfc)

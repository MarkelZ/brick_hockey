from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE
from ball import Ball
from brick import Brick
from coin import Coin
import pygame
from pygame.math import Vector2
import config


# Line-segment collider object
class Collider:
    def __init__(self, x0, y0, x1, y1, colobj, is_vertical):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.colobj = colobj
        self.is_vertical = is_vertical


class Table:
    def __init__(self):
        # Initialize vars
        self.width = config.screenres[0]
        self.height = config.screenres[1]
        self.bricks = []
        self.coins = []
        self.balls = []
        self.balls_to_remove = []
        self.colliders = []
        self.sim_numiters = 1

        # Collision with edges of the screen
        self.colliders += [Collider(0, 0, 0, self.height, None, True),
                           Collider(self.width, 0, self.width,
                                    self.height, None, True),
                           Collider(0, 0, self.width, 0, None, False)]

        # Debug: add some bricks for testing
        bb = [Brick(100, 100, size=100,  num=128),
              Brick(200, 100, size=100,  num=128),
              Brick(300, 100, size=100,  num=128),
              Brick(400, 100, size=100,  num=128),
              Brick(100, 200, size=100,  num=128),
              Brick(200, 200, size=100,  num=128)]
        for b in bb:
            self.addbrick(b)

        coin = Coin(50, 150)
        self.coins.append(coin)

    # Add brick and its colliders to table
    def addbrick(self, brick):
        self.bricks.append(brick)
        self.colliders.append(
            Collider(brick.x, brick.y,
                     brick.x, brick.y + brick.size,
                     brick, True))
        self.colliders.append(
            Collider(brick.x + brick.size, brick.y,
                     brick.x + brick.size, brick.y + brick.size,
                     brick, True))
        self.colliders.append(
            Collider(brick.x, brick.y,
                     brick.x + brick.size, brick.y,
                     brick, False))
        self.colliders.append(
            Collider(brick.x, brick.y + brick.size,
                     brick.x + brick.size, brick.y + brick.size,
                     brick, False))

    # Remove bricks with number less than or equal to 0
    def purge_bricks(self):
        depleted_bricks = [b for b in self.bricks if b.num <= 0]
        self.colliders = [
            col for col in self.colliders if col.colobj not in depleted_bricks]
        self.bricks = [b for b in self.bricks if b.num > 0]

    def update(self):
        # Update balls
        for ball in self.balls:
            ball.update()

        # Update bricks
        for brick in self.bricks:
            brick.update()

        # Remove depleted bricks
        self.purge_bricks()

        # Remove balls
        self.balls = [b for b in self.balls if b not in self.balls_to_remove]
        self.balls_to_remove = []

    def draw(self, sfc):
        # Draw bricks
        for brick in self.bricks:
            brick.draw(sfc)

        # Draw balls
        for ball in self.balls:
            ball.draw(sfc)

        # Draw coins
        for coin in self.coins:
            coin.draw(sfc)

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
    def __init__(self, gamestate):
        # Initialize vars
        self.gamestate = gamestate
        self.width = config.screenres[0]
        self.height = config.screenres[1]
        self.gridwidth = 7
        self.gridheight = 7
        self.bricksize = self.width / self.gridwidth
        self.bricks = []
        self.coins = []
        self.coins_to_remove = []
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
        for i in range(4):
            for j in range(1, 3):
                b = Brick(i * self.bricksize, j * self.bricksize,
                          size=self.bricksize + 1, num=128)
                self.addbrick(b)

        coin = Coin(self.bricksize * 0.5, self.bricksize * 3.5)
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
    def _purge_bricks(self):
        depleted_bricks = [b for b in self.bricks if b.num <= 0]
        self.colliders = [
            col for col in self.colliders if col.colobj not in depleted_bricks]
        self.bricks = [b for b in self.bricks if b.num > 0]

    # Shift all bricks downwards and generate next row.
    # Happens right before gamestate switches to shooting state
    def generate_and_shift_bricks(self):
        # Shift bricks
        for brick in self.bricks:
            brick.y += self.bricksize

        for coin in self.coins:
            coin.p.y += self.bricksize

        for col in self.colliders[4:]:
            col.y0 += self.bricksize
            col.y1 += self.bricksize

        # TODO: If bricks reach the player, game over

        # Generate new bricks

    def update(self):
        # Update balls
        for ball in self.balls:
            ball.update()

        # Update bricks
        for brick in self.bricks:
            brick.update()

        # Update coins
        for coin in self.coins:
            coin.update()

        # Remove depleted bricks
        self._purge_bricks()

        # Remove balls
        self.balls = [
            b for b in self.balls if b not in self.balls_to_remove]
        self.balls_to_remove = []

        # Remove coins
        self.coins = [
            c for c in self.coins if c not in self.coins_to_remove]
        self.coins_to_remove = []

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

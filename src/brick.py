import pygame
from math import log2, ceil


class Brick:

    def __init__(self, x, y, size, num):
        self.num = num
        self.x = x
        self.y = y
        self.size = size
        self.txtcolor = (0, 0, 0)
        self.font = pygame.font.Font('content/sans.ttf', round(size * 0.5))
        self._update_base_color()
        self.color = self.base_color
        self.is_animation = False
        self.animation_ctr = 0
        self.animation_time = 10

    def _update_base_color(self):
        # Choose color's hue based on num
        color_range = 2
        value = ceil(log2(self.num))
        color_channel = (value // color_range) % 3
        hue = 255 - round(255.0 * (value % color_range) / color_range)
        color = [0, 0, 0]
        color[color_channel] = hue
        color[(color_channel + 1) % 3] = 255 - hue

        # Make color a bit brighter
        color = [c + 50 for c in color]
        color = [255 if c > 255 else c for c in color]

        self.base_color = color

    def damage(self):
        self.num -= 1
        self.is_animation = True
        self.animation_ctr = 0
        if self.num > 0:
            self._update_base_color()

    def update(self):
        if self.is_animation:
            self.animation_ctr += 1

            brightness = 128.0 * (1 - self.animation_ctr / self.animation_time)
            self.color = [c + brightness for c in self.base_color]
            self.color = [255 if c > 255 else c for c in self.color]

            if self.animation_ctr >= self.animation_time:
                self.is_animation = False
                self.color = self.base_color

    def draw(self, sfc):
        # Draw rectangle
        pygame.draw.rect(
            sfc, self.color, (self.x, self.y, self.size, self.size))

        # Draw centered text
        textsurface = self.font.render(str(self.num), True, self.txtcolor)
        marginw = (self.size - textsurface.get_width()) / 2.0
        marginh = (self.size - textsurface.get_height()) / 2.0
        sfc.blit(textsurface, (self.x + marginw, self.y + marginh))

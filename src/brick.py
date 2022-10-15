import pygame


class Brick:

    def __init__(self, x, y, size, num):
        self.num = num
        self.x = x
        self.y = y
        self.size = size
        self.txtcolor = (0, 0, 0)
        self.font = pygame.font.Font('content/sans.ttf', round(size * 0.5))
        self._calculate_color()

    def _calculate_color(self):
        # Choose color's hue based on num
        color_range = 100
        color_channel = (self.num // color_range) % 3
        hue = 255 - round(255.0 * (self.num % color_range) / color_range)
        color = [0, 0, 0]
        color[color_channel] = hue
        color[(color_channel + 1) % 3] = 255 - hue

        # Make color a bit brighter
        color = [c + 50 for c in color]
        color = [255 if c > 255 else c for c in color]

        self.color = color

    def damage(self):
        self.num -= 1
        self._calculate_color()
        # Do hit animation

    def draw(self, sfc):
        # Draw rectangle
        pygame.draw.rect(
            sfc, self.color, (self.x, self.y, self.size, self.size))

        # Draw centered text
        textsurface = self.font.render(str(self.num), True, self.txtcolor)
        marginw = (self.size - textsurface.get_width()) / 2.0
        marginh = (self.size - textsurface.get_height()) / 2.0
        sfc.blit(textsurface, (self.x + marginw, self.y + marginh))

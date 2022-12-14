from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
import pygame
import config


class DebugWriter:
    def __init__(self):
        self.stack = []
        self.debugfont = pygame.font.Font(config.debugfontpath, 24)

    def writeln(self, text):
        self.stack.append(text)

    def clear(self):
        self.stack = []

    def draw(self, win, color=(255, 255, 255)):
        separation = 16
        height = 0
        for i in range(len(self.stack)):
            textsurface = self.debugfont.render(
                self.stack[i], True, color)
            win.blit(textsurface, (0, height))
            height += separation

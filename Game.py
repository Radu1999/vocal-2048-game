
import pygame
import sys
from pygame.locals import *

from NumberSquare import NumberSquare
from Constants import *

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("2048")

        self.gameObjects = []

        self.gameObjects += [NumberSquare(self, [100, 100], [0, 0])]

    def input(self):
        events = pygame.event.get()
        for obj in self.gameObjects:
            obj.input(events)

    def update(self):
        for obj in self.gameObjects:
            obj.update()

    def draw(self):
        self.window.fill(WHITE)

        for obj in self.gameObjects:
            obj.draw()

        pygame.display.update()

        pygame.time.Clock().tick(30)

    def run(self):
        while True:
            self.input()
            self.update()
            self.draw()

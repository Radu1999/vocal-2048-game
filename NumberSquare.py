
import pygame
import sys
from pygame.locals import *

from GameObject import GameObject
from Constants import *

class NumberSquare(GameObject):
    def __init__(self, game, position, velocity):
        super().__init__(game, position, velocity)
        self.value = 2

    def input(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_a:
                    self.velocity[0] = -self.max_velocity
                if event.key == K_d:
                    self.velocity[0] = self.max_velocity
            if event.type == KEYUP:
                if event.key == K_a:
                    self.velocity[0] = 0
                if event.key == K_d:
                    self.velocity[0] = 0
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        print(self.velocity[0])
        if self.position[0] < 0:
            self.position[0] = WIDTH
        if self.position[0] > WIDTH:
            self.position[0] = 0

        if self.position[1] < 0:
            self.position[1] = HEIGHT
        if self.position[1] > HEIGHT:
            self.position[1] = 0

    def draw(self):
        pygame.draw.rect(self.game.window, GREEN, pygame.Rect(self.position[0],self.position[1],60,60))
    
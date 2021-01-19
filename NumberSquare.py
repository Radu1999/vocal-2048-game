
import pygame

from GameObject import GameObject


class NumberSquare(GameObject):
    def __init__(self, game, position, image, value, column, row):
        super().__init__(game, position)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.value = value
        self.column = column
        self.row = row

    def set_image(self, image):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (150, 150))

    def update(self):
        self.position[0] = 20 + self.column * 160
        self.position[1] = 20 + self.row * 160

    def draw(self):
        self.game.window.blit(self.image, self.position)


import pygame
import sys
from pygame.locals import *

from NumberSquare import NumberSquare
from Constants import *
from ButtonObject import Button

pygame.init()
class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("2048 with extra steps")

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

    def main_menu(self):
        ok = 0
        difficulty = 0

        # create play button
        play = Button(WHITE, 235, 400, 45, 45, "play")

        # create difficulty buttons
        _2048 = Button(WHITE, 130, 300, 45, 45, "2048")
        _1024 = Button(WHITE, 200, 300, 45, 45, "1024")
        _512  = Button(WHITE, 270, 300, 45, 45, "512")
        _256  = Button(WHITE, 340, 300, 45, 45, "256")
        
        # pygame loop for start screen
        while True:
            self.window.fill(BLACK)

            self.window.blit(pygame.transform.scale(
            pygame.image.load("images/icon.ico"), (200, 200)), (155, 50))

            font = pygame.font.SysFont("Verdana", 20, bold=True)

            diff_text = font.render("Difficulty: ", 1, WHITE)
            self.window.blit(diff_text, (30, 310))


            font_buttons = pygame.font.SysFont("Comic Sans MS", 14, bold=True)

            play.draw(self.window, BLACK, font_buttons)
            _256.draw(self.window, BLACK, font_buttons)
            _512.draw(self.window, BLACK, font_buttons)
            _1024.draw(self.window, BLACK, font_buttons)
            _2048.draw(self.window, BLACK, font_buttons)

            pygame.display.update()
            for event in pygame.event.get():
            # store mouse position (coordinates)
                pos = pygame.mouse.get_pos()
                if event.type == QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == K_q):
                # exit if q is pressed 
                    pygame.quit()
                    sys.exit()

                # check if a button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if _2048.isOver(pos):
                    _2048.colour = YELLOW
                    _1024.colour = WHITE
                    _512.colour = WHITE
                    _256.colour = WHITE
                    difficulty = 2048
                
                if _1024.isOver(pos):
                    _1024.colour = YELLOW
                    _2048.colour = WHITE
                    _512.colour = WHITE
                    _256.colour = WHITE
                    difficulty = 1024
                
                if _512.isOver(pos):
                    _512.colour = YELLOW
                    _1024.colour = WHITE
                    _2048.colour = WHITE
                    _256.colour = WHITE
                    difficulty = 512
                
                if _256.isOver(pos):
                    _256.colour = YELLOW
                    _1024.colour = WHITE
                    _512.colour = WHITE
                    _2048.colour = WHITE
                    difficulty = 256

                if not play.isOver(pos) and \
                    not _2048.isOver(pos) and \
                    not _1024.isOver(pos) and \
                    not _512.isOver(pos) and \
                    not _256.isOver(pos):

                    difficulty = 0

                    _2048.colour = WHITE
                    _1024.colour = WHITE
                    _512.colour = WHITE
                    _256.colour = WHITE
                
                if play.isOver(pos) and difficulty != 0:
                        ok = 1
            
            if play.isOver(pos):
                        play.colour = YELLOW
            else:
                        play.colour = WHITE 
              
            if ok == 1:
                break



    def run(self):
        self.main_menu()
        while True:
            self.input()
            self.update()
            self.draw()

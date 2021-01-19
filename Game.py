import pygame
import sys
from pygame.locals import *
import random
import math
from NumberSquare import NumberSquare
from Board import Board
from Constants import *
import speech_recognition as sr
from ButtonObject import Button


class Game:
    def __init__(self):
        self.vocal_exit = pygame.event.Event(pygame.USEREVENT, attr1='vocal_exit')
        self.vocal_right = pygame.event.Event(pygame.USEREVENT, attr1='vocal_right')
        self.vocal_left = pygame.event.Event(pygame.USEREVENT, attr1='vocal_left')
        self.vocal_up = pygame.event.Event(pygame.USEREVENT, attr1='vocal_up')
        self.vocal_down = pygame.event.Event(pygame.USEREVENT, attr1='vocal_down')
        self.r = sr.Recognizer()

    def initialise(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("2048")
        self.board = Board(self, self.difficulty)
        self.gameObjects = []
        self.steps = 0
        for i in range(4):
            for j in range(4):
                self.gameObjects.append(self.board.game_board[i][j])

    def WIN(self):
        font = pygame.font.SysFont("Verdana", 20, bold=True)
        while True:
            # Fill the window with a transparent background
            s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            s.fill([238, 228, 218, 200])
            self.window.blit(s, (0, 0))
            message = "YOU WIN"

            self.window.blit(font.render(message, 1, BLACK), (280, 180))
            # Ask user to play again
            self.window.blit(font.render(
                "Play again? (yes/ no)", 1, BLACK), (230, 255))

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT or \
                        (event.type == pygame.KEYDOWN and event.key == K_n):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == K_y:
                        pygame.quit()
                        sys.exit()

    def get_command(self, recognizer):
        with sr.Microphone() as source:
            print(f"{self.steps}. Say next command or exit to end:")
            self.steps += 1
            audio = recognizer.record(source, duration=2.5)
            try:
                command = recognizer.recognize_google(audio)
                if 'exit' in command:
                    pygame.event.post(self.vocal_exit)
                elif 'right' in command:
                    pygame.event.post(self.vocal_right)
                elif 'left' in command:
                    pygame.event.post(self.vocal_left)
                elif 'up' in command:
                    pygame.event.post(self.vocal_up)
                elif 'down' in command:
                    pygame.event.post(self.vocal_down)
            except sr.UnknownValueError:
                pass

    def LOSE(self):
        font = pygame.font.SysFont("Verdana", 20, bold=True)
        while True:
            # Fill the window with a transparent background
            s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            s.fill([238, 228, 218, 200])
            self.window.blit(s, (0, 0))
            message = "YOU LOSE"

            self.window.blit(font.render(message, 1, BLACK), (280, 180))
            # Ask user to play again
            self.window.blit(font.render(
                "Play again? (yes/ no)", 1, BLACK), (230, 255))

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT or \
                        (event.type == pygame.KEYDOWN and event.key == K_n):
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN and event.key == K_y:
                        self.run()
    
    def input(self):
        events = pygame.event.get()
        for event in events:
            if event == self.vocal_exit or event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_d:
                    self.board.move_right()
                    self.board.get_random_empty_square()
                    self.board.check_state()
                if event.key == K_a:
                    self.board.move_left()  
                    self.board.get_random_empty_square()
                    self.board.check_state()    
                if event.key == K_w:
                    self.board.move_up()
                    self.board.get_random_empty_square()
                    self.board.check_state()
                if event.key == K_s:
                    self.board.move_down()
                    self.board.get_random_empty_square()
                    self.board.check_state()
            if event == self.vocal_right:
                self.board.move_right()
                self.board.get_random_empty_square()
                self.board.check_state()
            if event == self.vocal_left:
                self.board.move_left()
                self.board.get_random_empty_square()
                self.board.check_state()
            if event == self.vocal_up:
                self.board.move_up()
                self.board.get_random_empty_square()
                self.board.check_state()
            if event == self.vocal_down:
                self.board.move_down()
                self.board.get_random_empty_square()
                self.board.check_state()

    def update(self):
        for obj in self.gameObjects:
            obj.update()

    def draw(self):
        state = self.board.state
        if state == "PLAY":
            self.window.fill(WHITE)

            for obj in self.gameObjects:
                obj.draw()

            pygame.display.update()

            pygame.time.Clock().tick(30)
        elif state == "WON":
            self.WIN()
            pass
        else:
            self.LOSE()
            pass

    def main_menu(self):
        self.window = pygame.display.set_mode((500, 500))
        ok = 0
        self.difficulty = 0

        # create play button
        play = Button(WHITE, 235, 400, 45, 45, "Play")

        # create difficulty buttons
        _2048 = Button(WHITE, 130, 300, 45, 45, "2048")
        _1024 = Button(WHITE, 200, 300, 45, 45, "1024")
        _512 = Button(WHITE, 270, 300, 45, 45, "512")
        _256 = Button(WHITE, 340, 300, 45, 45, "256")

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
                    self.difficulty = 2048

                if _1024.isOver(pos):
                    _1024.colour = YELLOW
                    _2048.colour = WHITE
                    _512.colour = WHITE
                    _256.colour = WHITE
                    self.difficulty = 1024

                if _512.isOver(pos):
                    _512.colour = YELLOW
                    _1024.colour = WHITE
                    _2048.colour = WHITE
                    _256.colour = WHITE
                    self.difficulty = 512

                if _256.isOver(pos):
                    _256.colour = YELLOW
                    _1024.colour = WHITE
                    _512.colour = WHITE
                    _2048.colour = WHITE
                    self.difficulty = 256

                if not play.isOver(pos) and \
                        not _2048.isOver(pos) and \
                        not _1024.isOver(pos) and \
                        not _512.isOver(pos) and \
                        not _256.isOver(pos):
                    self.difficulty = 0

                    _2048.colour = WHITE
                    _1024.colour = WHITE
                    _512.colour = WHITE
                    _256.colour = WHITE

                if play.isOver(pos) and self.difficulty != 0:
                    ok = 1

            if play.isOver(pos):
                play.colour = YELLOW
            else:
                play.colour = WHITE

            if ok == 1:
                break

    def run(self):
        self.main_menu()
        self.initialise()
        while True:
            self.input()
            self.update()
            self.draw()
            self.get_command(self.r)

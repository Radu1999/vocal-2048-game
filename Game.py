import pygame
import sys
from pygame.locals import *
import random
import math
from NumberSquare import NumberSquare
from Constants import *
import speech_recognition as sr


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("2048")
        self.game_board = []
        self.gameObjects = []
        self.vocal_exit = pygame.event.Event(pygame.USEREVENT, attr1='vocal_exit')
        self.vocal_right = pygame.event.Event(pygame.USEREVENT, attr1='vocal_right')
        self.vocal_left = pygame.event.Event(pygame.USEREVENT, attr1='vocal_left')
        self.vocal_up = pygame.event.Event(pygame.USEREVENT, attr1='vocal_up')
        self.vocal_down = pygame.event.Event(pygame.USEREVENT, attr1='vocal_down')
        self.r = sr.Recognizer()
        for r, y in enumerate(range(20, 660, 160)):
            row = []
            for c, x in enumerate(range(20, 660, 160)):
                number_square = NumberSquare(self, [x, y], "images/0.png", 0, c, r)
                row.append(number_square)
                self.gameObjects += [number_square]
            self.game_board.append(row)
        self.get_random_empty_square()
        self.get_random_empty_square()

    def get_random_empty_square(self):
        empty_list = []
        for square in self.gameObjects:
            if square.value == 0:
                empty_list.append(square)
        square = random.choice(empty_list)
        value = int(math.pow(2, random.randint(1, 3)))
        square.value = value
        image = "images/" + str(value) + ".png"
        square.set_image(image)

    def move_right(self):
        for i in range(4):
            last_r = i
            last_c = 3
            for j in range(2, -1, -1):
                square = self.game_board[i][j]
                if square.value != 0:
                    last_square = self.game_board[last_r][last_c]
                    if last_square.value == 0:
                        square.column = last_c
                        last_square.column = j
                        temp = last_square
                        self.game_board[last_r][last_c] = square
                        self.game_board[i][j] = temp
                    elif last_square.value == square.value:
                        last_square.value += square.value
                        new_image = "images/" + str(last_square.value) + ".png"
                        last_square.set_image(new_image)
                        square.value = 0
                        square.set_image("images/0.png")
                    else:
                        last_square = self.game_board[last_r][last_c - 1]
                        square.column = last_c - 1
                        last_square.column = j
                        last_c = last_c - 1
                        temp = last_square
                        self.game_board[last_r][last_c] = square
                        self.game_board[i][j] = temp

    def move_left(self):
        for i in range(4):
            last_r = i
            last_c = 0
            for j in range(1, 4):
                square = self.game_board[i][j]
                if square.value != 0:
                    last_square = self.game_board[last_r][last_c]
                    if last_square.value == 0:
                        square.column = last_c
                        last_square.column = j
                        temp = last_square
                        self.game_board[last_r][last_c] = square
                        self.game_board[i][j] = temp
                    elif last_square.value == square.value:
                        last_square.value += square.value
                        new_image = "images/" + str(last_square.value) + ".png"
                        last_square.set_image(new_image)
                        square.value = 0
                        square.set_image("images/0.png")
                    else:
                        last_square = self.game_board[last_r][last_c + 1]
                        square.column = last_c + 1
                        last_square.column = j
                        last_c = last_c + 1
                        temp = last_square
                        self.game_board[last_r][last_c] = square
                        self.game_board[i][j] = temp

    def move_up(self):
        for j in range(4):
            last_r = 0
            last_c = j
            for i in range(1, 4):
                square = self.game_board[i][j]
                if square.value != 0:
                    last_square = self.game_board[last_r][last_c]
                    if last_square.value == 0:
                        square.row = last_r
                        last_square.row = i
                        temp = last_square
                        self.game_board[last_r][last_c] = square
                        self.game_board[i][j] = temp
                    elif last_square.value == square.value:
                        last_square.value += square.value
                        new_image = "images/" + str(last_square.value) + ".png"
                        last_square.set_image(new_image)
                        square.value = 0
                        square.set_image("images/0.png")
                    else:
                        last_square = self.game_board[last_r + 1][last_c]
                        square.row = last_r + 1
                        last_square.row = i
                        last_r = last_r + 1
                        temp = last_square
                        self.game_board[last_r][last_c] = square
                        self.game_board[i][j] = temp

    def move_down(self):
        for j in range(4):
            last_r = 3
            last_c = j
            for i in range(2, -1, -1):
                square = self.game_board[i][j]
                if square.value != 0:
                    last_square = self.game_board[last_r][last_c]
                    if last_square.value == 0:
                        square.row = last_r
                        last_square.row = i
                        temp = last_square
                        self.game_board[last_r][last_c] = square
                        self.game_board[i][j] = temp
                    elif last_square.value == square.value:
                        last_square.value += square.value
                        new_image = "images/" + str(last_square.value) + ".png"
                        last_square.set_image(new_image)
                        square.value = 0
                        square.set_image("images/0.png")
                    else:
                        last_square = self.game_board[last_r - 1][last_c]
                        square.row = last_r - 1
                        last_square.row = i
                        last_r = last_r - 1
                        temp = last_square
                        self.game_board[last_r][last_c] = square
                        self.game_board[i][j] = temp

    def get_command(self, recognizer):
        with sr.Microphone() as source:
            print("Say next command or exit to end:")
            audio = recognizer.record(source, duration=2)
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

    def input(self):
        events = pygame.event.get()
        for event in events:
            if event == self.vocal_exit or event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event == self.vocal_right:
                self.move_right()
                self.get_random_empty_square()
            if event == self.vocal_left:
                self.move_left()
                self.get_random_empty_square()
            if event == self.vocal_up:
                self.move_up()
                self.get_random_empty_square()
            if event == self.vocal_down:
                self.move_down()
                self.get_random_empty_square()

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
            self.get_command(self.r)

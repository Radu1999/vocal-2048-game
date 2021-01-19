import pygame
import sys
from pygame.locals import *
import random
import math
from NumberSquare import NumberSquare
from Constants import *
from ButtonObject import Button

class Board:
    def __init__(self, game, difficulty):
        self.game_board = []
        self.game = game
        self.difficulty = difficulty
        self.state = "PLAY"
        for r, y in enumerate(range(20, 660, 160)):
            row = []
            for c, x in enumerate(range(20, 660, 160)):
                number_square = NumberSquare(self.game, [x, y], "images/0.png", 0, c, r)
                row.append(number_square)
            self.game_board.append(row)
        self.get_random_empty_square()
        self.get_random_empty_square()

    def get_random_empty_square(self):
        empty_list = []
        for i in range(4):
            for j in range(4):
                if self.game_board[i][j].value == 0:
                    empty_list.append(self.game_board[i][j])
        if len(empty_list) == 0:
            return
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

    def check_state(self):
        game_ended = True
        for i in range(4):
            for j in range(4):
                if self.difficulty == self.game_board[i][j].value:
                    self.state = "WON"
                    return
                if (self.game_board[i][j].value == 0):
                    game_ended = False
                if game_ended == True:
                    if i != 3 and self.game_board[i][j].value == self.game_board[i+1][j].value:
                        game_ended = False
                    elif j != 3 and self.game_board[i][j].value == self.game_board[i][j+1].value:
                        game_ended = False
                    elif i != 0 and self.game_board[i][j].value == self.game_board[i-1][j].value:
                        game_ended = False
                    elif j != 0 and self.game_board[i][j].value == self.game_board[i][j-1].value:
                        game_ended = False
        if game_ended == True:
            print("Lost")
            self.state = "LOST"
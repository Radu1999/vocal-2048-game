
import pygame
import sys
from pygame.locals import *
import random
import math
from NumberSquare import NumberSquare
from Constants import *
from ButtonObject import Button

class Game:
    def __init__(self):
        pygame.display.set_caption("2048")
        self.game_board = []
        self.gameObjects = []
        self.state = "PLAY"
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

    def chech_state(self):
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
            self.state = "LOST"

    def input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == KEYUP:
                if event.key == K_d:
                    self.move_right()
                    self.chech_state()
                    self.get_random_empty_square()
                if event.key == K_a:
                    self.move_left()
                    self.chech_state()
                    self.get_random_empty_square()
                if event.key == K_w:
                    self.move_up()
                    self.chech_state()
                    self.get_random_empty_square()
                if event.key == K_s:
                    self.move_down()
                    self.chech_state()
                    self.get_random_empty_square()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        for obj in self.gameObjects:
            obj.update()

    def draw(self):
        if self.state == "PLAY":
            self.window.fill(WHITE)

            for obj in self.gameObjects:
                obj.draw()

            pygame.display.update()

            pygame.time.Clock().tick(30)
        elif self.state == "WON":
            # TODO won_screen
            pass
        else:
            # TODO lost_screen
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
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        while True:
            self.input()
            self.update()
            self.draw()

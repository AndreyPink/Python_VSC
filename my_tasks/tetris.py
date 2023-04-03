# НЕ РАБОТАЕТ

import pygame
import random

# Инициализация Pygame
pygame.init()

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Размеры окна
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500

# Размеры блока и поля
BLOCK_SIZE = 20
PLAY_WIDTH = 10 * BLOCK_SIZE
PLAY_HEIGHT = 20 * BLOCK_SIZE

# Скорость падения фигур
FPS = 60
INITIAL_SPEED = 0.5

# Отступ сверху и слева
TOP_PADDING = 30
LEFT_PADDING = (WINDOW_WIDTH - PLAY_WIDTH) // 2

# Определение фигур
FIGURES = [
    [[1, 1, 1],
     [0, 1, 0]],
    [[0, 2, 2],
     [2, 2, 0]],
    [[3, 3, 0],
     [0, 3, 3]],
    [[4, 0, 0],
     [4, 4, 4]],
    [[0, 0, 5, 0],
     [0, 5, 5, 5]],
    [[6, 6],
     [6, 6]],
    [[7, 7, 7, 7]]
]

# Класс для фигуры
class Figure:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.row = 0
        self.column = PLAY_WIDTH // 2 - len(shape[0]) // 2

    def rotate(self):
        self.shape = [[self.shape[y][x] for y in range(len(self.shape))] for x in range(len(self.shape[0])-1, -1, -1)]

    def move(self, row, column):
        self.row = row
        self.column = column

    def copy(self):
        return Figure(self.shape, self.color)

# Класс для игры
class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.play_surface = pygame.Surface((PLAY_WIDTH, PLAY_HEIGHT))
        self.clock = pygame.time.Clock()

        self.score = 0
        self.level = 1
        self.speed = INITIAL_SPEED
        self.figure = self.get_new_figure()

        self.field = [[0] * 10 for _ in range(20)]

    def get_new_figure(self):
        shape = random.choice(FIGURES)
        color = random.randint(1, 7)
        return Figure(shape, color)

    def draw_block(self, row, column, color):
        pygame.draw.rect(self.play_surface, color, (column * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_figure(self, figure):
        for row in range(len(figure.shape)):
            for column in range(len(figure.shape[row])):
                if figure.shape[row][column] != 0:
                    self.draw_block(figure.row + row, figure.column + column, figure.color)

    def erase_figure(self, figure):
        for row in range(len(figure.shape)):
            for column in range(len(figure.shape[row])):
                if figure.shape[row][column] != 0:
                    self.draw_block(figure.row + row, figure.column + column, BLACK)

def check_collision(self, figure):
    for row in range(len(figure.shape)):
        for column in range(len(figure.shape[row])):
            if figure.shape[row][column] != 0:
                if figure.row + row < 0 or figure.row + row >= 20 or figure.column + column < 0 or figure.column + column >= 10 or self.field[figure.row + row][figure.column + column] != 0:
                    return True
    return False

def place_figure(self, figure):
    for row in range(len(figure.shape)):
        for column in range(len(figure.shape[row])):
            if figure.shape[row][column] != 0:
                self.field[figure.row + row][figure.column + column] = figure.color

def check_full_rows(self):
    full_rows = []
    for row in range(len(self.field)):
        if all(self.field[row]):
            full_rows.append(row)
    return full_rows

def remove_rows(self, rows):
    for row in rows:
        self.field.pop(row)
        self.field.insert(0, [0] * 10)
    self.score += len(rows) ** 2 * 100
    self.level = (self.score // 1000) + 1
    self.speed = INITIAL_SPEED + (self.level - 1) * 0.1

def draw_field(self):
    for row in range(len(self.field)):
        for column in range(len(self.field[row])):
            self.draw_block(row, column, self.field[row][column])

def run(self):
    running = True
    while running:
        self.clock.tick(FPS)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_figure = self.figure.copy()
                    new_figure.move(self.figure.row, self.figure.column - 1)
                    if not self.check_collision(new_figure):
                        self.erase_figure(self.figure)
                        self.figure.move(self.figure.row, self.figure.column - 1)
                        self.draw_figure(self.figure)
                if event.key == pygame.K_RIGHT:
                    new_figure = self.figure.copy()
                    new_figure.move(self.figure.row, self.figure.column + 1)
                    if not self.check_collision(new_figure):
                        self.erase_figure(self.figure)
                        self.figure.move(self.figure.row, self.figure.column + 1)
                        self.draw_figure(self.figure)
                if event.key == pygame.K_UP:
                    new_figure = self.figure.copy()
                    new_figure.rotate()
                    if not self.check_collision(new_figure):
                        self.erase_figure(self.figure)
                        self.figure.rotate()
                        self.draw_figure(self.figure)
                if event.key == pygame.K_DOWN:
                    new_figure = self.figure.copy()
                    new_figure.move(self.figure.row + 1, self.figure.column)
                    if not self.check_collision(new_figure):
                        self.erase_figure(self.figure)
                        self.figure.move(self.figure.row + 1, self.figure.column)
                        self.draw_figure(self.figure)
                if event.key == pygame.K_SPACE:
                    while not self.check_collision(self.figure.copy().move(self.figure.row + 1, self.figure.column)):
                        self.erase_figure(self.figure)
                        self.figure.move(self.figure.row + 1, self.figure.column)
                        self.draw_figure(self.figure)
                    self.place_figure(self.figure)
                    self.erase_figure(self.figure)
                    self.figure.move(self.figure.row + 1, self.figure.column)
                    if self.check_collision(self.figure):
                        self.place_figure(self.figure)
                        full_rows = self.check_full_rows()
                        if full_rows:
                            self.remove_rows(full_rows)
                        self.spawn_figure()
                        if self.check_collision(self.figure):
                            running = False
                    self.draw_figure(self.figure)
                    self.draw_field()
                    self.draw_info()
                    pygame.display.update()

    # pygame.quit()
    game = Tetris()
    game.run()

                    

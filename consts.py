import os
import pygame

WIDTH = 1000
HEIGHT = 500
GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
IMAGE_WIDTH = 100
IMAGE_HEIGHT = 80
FPS = 60
SQUARE_LENGTH = 20

SOLDIER_IMAGE = pygame.image.load(os.path.join('pics', 'soldier.png'))
SOLDIER = pygame.transform.scale(SOLDIER_IMAGE, (40,80))
FLAG_IMAGE = pygame.image.load(os.path.join('pics', 'flag.png'))
FLAG = pygame.transform.scale(FLAG_IMAGE, (IMAGE_WIDTH, IMAGE_HEIGHT))
GRASS_IMAGE = pygame.image.load(os.path.join('pics', 'grass.png'))
GRASS = pygame.transform.scale(GRASS_IMAGE, (IMAGE_WIDTH, IMAGE_HEIGHT))
MINE_IMAGE = pygame.image.load(os.path.join('pics', 'mine.png'))
MINE = pygame.transform.scale(MINE_IMAGE, (60, 20))

FONT_NAME = "Calibri"

LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION = \
    (0.2 * WIDTH, HEIGHT / 2 - (LOSE_FONT_SIZE / 2))

WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * WIDTH, HEIGHT / 2 - (WIN_FONT_SIZE / 2))

START_SOLDIER_LEGS_LOCATION = (1, 4)
RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3

BACKGROUND_COLOR = (0, 100, 0)
MATRIX_ROWS = 50
MATRIX_COLS = 25
import pygame
import random
import consts
import MineField
import os

WIN = pygame.display.set_mode((consts.WIDTH,consts.HEIGHT))
pygame.display.set_caption("The Flag")

# BORDER = pygame.Rect(WIDTH/2, 0, 10, HEIGHT)

SOLDIER_IMAGE = pygame.image.load(os.path.join('pics', 'soldier.png'))
SOLDIER = pygame.transform.scale(SOLDIER_IMAGE, (40,80))
FLAG_IMAGE = pygame.image.load(os.path.join('pics', 'flag.png'))
FLAG = pygame.transform.scale(FLAG_IMAGE, (consts.IMAGE_WIDTH, consts.IMAGE_HEIGHT))
GRASS_IMAGE = pygame.image.load(os.path.join('pics', 'grass.png'))
GRASS = pygame.transform.scale(GRASS_IMAGE, (consts.IMAGE_WIDTH, consts.IMAGE_HEIGHT))
MINE_IMAGE = pygame.image.load(os.path.join('pics', 'mine.png'))
MINE = pygame.transform.scale(MINE_IMAGE, (60, 20))

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 10)
text_surface = my_font.render('Welcome to The Flag game. Have Fun!', True, consts.WHITE)

multi_grass = []
multi_grass_pos = []

multi_mine = []
multi_mine_pos = []

for i in range(20):
    multi_grass.append(GRASS)
    pos = [random.randint(0,900), random.randint( 0, 400)]
    multi_grass_pos.append(pos)

for i in range(20):
    multi_mine.append(MINE)
    pos = [random.randint(0, 900), random.randint(0, 400)]
    multi_mine_pos.append(pos)

def draw_window(player_soldier, flag):
    WIN.fill(consts.GREEN)
    WIN.blit(text_surface, (40,0))
    WIN.blit(SOLDIER, (player_soldier.x, player_soldier.y))
    WIN.blit(FLAG, (flag.x, flag.y))
    for i in range(len(multi_grass)):
        WIN.blit(multi_grass[i], (multi_grass_pos[i][0], multi_grass_pos[i][1]))
    pygame.display.update()

def draw_grid(player_soldier):
    WIN.fill(consts.BLACK)
    blockSize = 20  # Set the size of the grid block
    for x in range(0, consts.WIDTH, blockSize):
        for y in range(0, consts.HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(WIN, consts.GREEN, rect, 1)
    WIN.blit(SOLDIER, (player_soldier.x, player_soldier.y))
    for i in range(len(multi_mine)):
        MineField.mines_locations((multi_mine_pos[i][0], multi_mine_pos[i][1]))
        WIN.blit(multi_mine[i], (multi_mine_pos[i][0], multi_mine_pos[i][1]))
    pygame.display.update()

# def soldier_movement(player_soldier, keys_pressed):
#     if keys_pressed[pygame.K_LEFT] and player_soldier.x - consts.SQUARE_LENGTH > 0:  # left
#         player_soldier.x -= consts.SQUARE_LENGTH
#     if keys_pressed[pygame.K_RIGHT] and player_soldier.x + consts.SQUARE_LENGTH+ player_soldier.width < consts.WIDTH:  # right
#         player_soldier.x += consts.SQUARE_LENGTH
#     if keys_pressed[pygame.K_UP] and player_soldier.y - consts.SQUARE_LENGTH > 0:  # up
#         player_soldier.y -= consts.SQUARE_LENGTH
#     if keys_pressed[pygame.K_DOWN] and player_soldier.y + consts.SQUARE_LENGTH + player_soldier.height < consts.HEIGHT:  # down
#         player_soldier.y += consts.SQUARE_LENGTH

def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    WIN.blit(text_img, location)

def draw_game():
    pass
    # player_soldier = pygame.Rect(0,0,40,80)
    # flag = pygame.Rect(consts.WIDTH-consts.IMAGE_WIDTH, consts.HEIGHT-consts.IMAGE_HEIGHT,consts.IMAGE_WIDTH,consts.IMAGE_HEIGHT)
    # clock = pygame.time.Clock()
    # run = True
    # while run:
    #     clock.tick(consts.FPS)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             run = False
    #     keys_pressed = pygame.key.get_pressed()
    #     soldier_movement(player_soldier,keys_pressed)
    #     draw_window(player_soldier, flag)
    # pygame.quit()

# if __name__ == '__main__':
#     main()
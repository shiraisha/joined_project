import time

import pygame
import random
import consts
import MineField

WIN = pygame.display.set_mode((consts.WIDTH,consts.HEIGHT))
pygame.display.set_caption("The Flag")

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 10)
text_surface = my_font.render('Welcome to The Flag game. Have Fun!', True, consts.WHITE)

multi_grass = []
multi_grass_pos = []

multi_mine = []

for i in range(20):
    multi_grass.append(consts.GRASS)
    pos = [random.randint(0,900), random.randint( 0, 400)]
    multi_grass_pos.append(pos)

for i in range(20):
    multi_mine.append(consts.MINE)
mine_list = MineField.generate_mines_positions()

# regular screen
def draw_window(player_soldier, flag):
    WIN.fill(consts.GREEN)
    WIN.blit(text_surface, (40,0))
    WIN.blit(consts.SOLDIER, (player_soldier.x, player_soldier.y))
    WIN.blit(consts.FLAG, (flag.x, flag.y))
    for i in range(len(multi_grass)):
        WIN.blit(multi_grass[i], (multi_grass_pos[i][0], multi_grass_pos[i][1]))
    pygame.display.update()

# slots screen with mines
def draw_grid(player_soldier):
    WIN.fill(consts.BLACK)
    blockSize = 20  # Set the size of the grid block
    for x in range(0, consts.WIDTH, blockSize):
        for y in range(0, consts.HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(WIN, consts.GREEN, rect, 1)
    WIN.blit(consts.SOLDIER, (player_soldier.x, player_soldier.y))
    for i in range(len(multi_mine)):
        WIN.blit(multi_mine[i], (mine_list[i][0]*20, mine_list[i][1]*20))
    pygame.display.update()


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

def draw_game(game_state,player_soldier):
    # player_soldier = pygame.Rect(0, 0, 40, 80)
    flag = pygame.Rect(consts.WIDTH-consts.IMAGE_WIDTH, consts.HEIGHT-consts.IMAGE_HEIGHT,consts.IMAGE_WIDTH,consts.IMAGE_HEIGHT)
    # WIN.fill(consts.BACKGROUND_COLOR)
    draw_window(player_soldier, flag)

    if game_state["pressed_key_enter"]:
        draw_grid(player_soldier)
        time.sleep(1)

    elif game_state["state"] == consts.LOSE_STATE:
        draw_lose_message()

    elif game_state["state"] == consts.WIN_STATE:
        draw_win_message()

    pygame.display.flip()
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
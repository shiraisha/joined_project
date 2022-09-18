import pygame
import random
import os

WIDTH, HEIGHT = 1000,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("The Flag")
GREEN = (0,100,0)
BLACK = (0,0,0)
IMAGE_WIDTH , IMAGE_HEIGHT = 70, 80

BORDER = pygame.Rect(WIDTH/2, 0, 10, HEIGHT)

FPS = 60

SOLDIER_IMAGE = pygame.image.load(os.path.join('pics', 'soldier.png'))
SOLDIER = pygame.transform.scale(SOLDIER_IMAGE, (40,80))
FLAG_IMAGE = pygame.image.load(os.path.join('pics', 'flag.png'))
FLAG = pygame.transform.scale(FLAG_IMAGE, (IMAGE_WIDTH,IMAGE_HEIGHT))
GRASS_IMAGE = pygame.image.load(os.path.join('pics', 'grass.png'))
GRASS = pygame.transform.scale(GRASS_IMAGE, (IMAGE_WIDTH,IMAGE_HEIGHT))
MINE_IMAGE = pygame.image.load(os.path.join('pics', 'mine.png'))
MINE = pygame.transform.scale(MINE_IMAGE, (IMAGE_WIDTH,IMAGE_HEIGHT))

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
    WIN.fill(GREEN)
    # WIN.fill(BLACK)
    # blockSize = 20  # Set the size of the grid block
    # for x in range(0, WIDTH, blockSize):
    #     for y in range(0, HEIGHT, blockSize):
    #         rect = pygame.Rect(x, y, blockSize, blockSize)
    #         pygame.draw.rect(WIN, GREEN, rect, 1)
    WIN.blit(SOLDIER, (player_soldier.x, player_soldier.y))
    WIN.blit(FLAG, (flag.x, flag.y))
    pygame.display.update()

def draw_grid(player_soldier):
    WIN.fill(BLACK)
    blockSize = 20  # Set the size of the grid block
    for x in range(0, WIDTH, blockSize):
        for y in range(0, HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(WIN, GREEN, rect, 1)
    WIN.blit(SOLDIER, (player_soldier.x, player_soldier.y))
    for i in range(len(multi_mine)):
        WIN.blit(multi_mine[i], (multi_mine_pos[i][0], multi_mine_pos[i][1]))
    pygame.display.update()

def soldier_movement(player_soldier, keys_pressed):
    if keys_pressed[pygame.K_LEFT] and player_soldier.x - 5 > 0:  # left
        player_soldier.x -= 5
    if keys_pressed[pygame.K_RIGHT] and player_soldier.x + 3.1 + player_soldier.width < WIDTH:  # right
        player_soldier.x += 3.1
    if keys_pressed[pygame.K_UP] and player_soldier.y - 5 > 0:  # up
        player_soldier.y -= 5
    if keys_pressed[pygame.K_DOWN] and player_soldier.y + 5 + player_soldier.height < HEIGHT:  # down
        player_soldier.y += 5

def random_position_grass():
    rnd_width = random.randint(1,1000)
    rnd_height = random.randint(1,500)
    grass = pygame.Rect(rnd_width, rnd_height,IMAGE_WIDTH,IMAGE_HEIGHT)
    WIN.blit(GRASS, (grass.x, grass.y))
    pygame.display.update()

def main():
    player_soldier = pygame.Rect(0,0,40,80)
    flag = pygame.Rect(WIDTH-IMAGE_WIDTH, HEIGHT-IMAGE_HEIGHT,IMAGE_WIDTH,IMAGE_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        soldier_movement(player_soldier,keys_pressed)
        # draw_window(player_soldier, flag)
        # for i in range(len(multi_grass)):
        #     WIN.blit(multi_grass[i], (multi_grass_pos[i][0], multi_grass_pos[i][1]))
        # pygame.display.update()
        draw_grid(player_soldier)
    pygame.quit()

if __name__ == "__main__":
    main()
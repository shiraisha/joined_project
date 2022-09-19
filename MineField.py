import random

import consts

def enter_mine_to_matrix(position, num_of_mine):
    game_surface_matrix[position[0]][position[1]] = 'mine' + str(num_of_mine)
    game_surface_matrix[position[0]][position[1] + 1] = 'mine' + str(num_of_mine)
    game_surface_matrix[position[0]][position[1] + 2] = 'mine' + str(num_of_mine)

def check_if_three_indexes_are_not_empty(position):
    if game_surface_matrix[position[0]][position[1]] == 'empty':
        if game_surface_matrix[position[0]][position[1] + 1] == 'empty':
            if game_surface_matrix[position[0]][position[1] + 2] == 'empty':
                return False
    return True
"""-----------------------------------------------------------------------------------------------------------"""

game_surface_matrix = [['empty'] * (consts.MATRIX_COLS) for i in range(consts.MATRIX_ROWS)]

# entering flag indexes to matrix
for i in range(21, 24):
    for j in range(46, 50):
        game_surface_matrix[i][j] = "flag"

for i in range(0, 4):
    for j in range(0, 2):
        game_surface_matrix[i][j] = "player_start"

for i in range(20):
    position = [random.randint(0, 24), random.randint(0, 47)]
    while check_if_three_indexes_are_not_empty(position):
        position = [random.randint(0, 25), random.randint(0, 47)]
    enter_mine_to_matrix(position, i)



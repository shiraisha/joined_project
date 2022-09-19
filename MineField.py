import random

import consts

game_surface_matrix = [['empty'] * (consts.MATRIX_COLS) for i in range(consts.MATRIX_ROWS)]
matrix_mine_pos = []

def enter_flag_to_matrix():
    # entering flag indexes to matrix
    for i in range(46, 50):
        for j in range(21, 24):
            game_surface_matrix[i][j] = "flag"
    enter_start_player_location_to_matrix()

def enter_start_player_location_to_matrix():
    for i in range(0, 2):
        for j in range(0, 4):
            game_surface_matrix[i][j] = "player_start"
    enter_mines()

def enter_mines():
    for i in range(20):
        position = [random.randint(0, 47), random.randint(0, 24)]
        while check_if_three_indexes_are_not_empty(position):
            position = [random.randint(0, 47), random.randint(0, 24)]
        enter_mine_to_matrix(position, i)
        matrix_mine_pos.append(position)

def enter_mine_to_matrix(position, num_of_mine):
    game_surface_matrix[position[0]][position[1]] = 'mine' + str(num_of_mine)
    game_surface_matrix[position[0] + 1][position[1]] = 'mine' + str(num_of_mine)
    game_surface_matrix[position[0] + 2][position[1]] = 'mine' + str(num_of_mine)

def check_if_three_indexes_are_not_empty(position):
    if game_surface_matrix[position[0]][position[1]] == 'empty':
        if game_surface_matrix[position[0] + 1][position[1]] == 'empty':
            if game_surface_matrix[position[0] + 2][position[1]] == 'empty':
                return False
    return True

def generate_mines_positions():
    enter_flag_to_matrix()
    return matrix_mine_pos

"""-----------------------------------------------------------------------------------------------------------"""




import pygame

import MineField
import Screen
import Soldier
import consts

state = {
    "state": consts.RUNNING_STATE,
    "soldier_legs_location": [[3, 0], [3, 1]],
    "is_window_open": True,
    "pressed_key_enter": False,
    "pressed_key_up": False,
    "pressed_key_down": False,
    "pressed_key_left": False,
    "pressed_key_right": False
}

soldier_legs_location = [[3, 0], [3, 1]]

def main():
    pygame.init()
    soldier = Soldier.player()
    player_soldier = pygame.Rect(soldier["position_x"], soldier["position_y"], soldier["width"], soldier["height"])
    clock = pygame.time.Clock()

    while state["is_window_open"]:
        clock.tick(consts.FPS)
        initialize_key_states()
        handle_user_events(player_soldier)

        if is_lose():
            state["state"] = consts.LOSE_STATE

        elif is_win():
            state["state"] = consts.WIN_STATE

        Screen.draw_game(state, player_soldier)


def handle_user_events(player_soldier):
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if keys_pressed[pygame.K_RETURN]:
            state["pressed_key_enter"] = True

        else:
            soldier_movement(player_soldier, keys_pressed)
            copy_returned_position(Soldier.legs_location(state, soldier_legs_location))
            print_matrix(Soldier.legs_location(state, soldier_legs_location))

def copy_returned_position(pos):
    for i in range(len(soldier_legs_location)):
        for j in range(len(soldier_legs_location[i])):
            soldier_legs_location[i][j] = pos[i][j]

def soldier_movement(player_soldier, keys_pressed):
    if keys_pressed[pygame.K_LEFT] and player_soldier.x - consts.SQUARE_LENGTH >= 0:  # left
        player_soldier.x -= consts.SQUARE_LENGTH
        state["pressed_key_left"] = True

    if keys_pressed[pygame.K_RIGHT] and player_soldier.x + consts.SQUARE_LENGTH + player_soldier.width < consts.WIDTH:  # right
        player_soldier.x += consts.SQUARE_LENGTH
        state["pressed_key_right"] = True

    if keys_pressed[pygame.K_UP] and player_soldier.y - consts.SQUARE_LENGTH >= 0:  # up
        player_soldier.y -= consts.SQUARE_LENGTH
        state["pressed_key_up"] = True

    if keys_pressed[pygame.K_DOWN] and player_soldier.y + consts.SQUARE_LENGTH + player_soldier.height < consts.HEIGHT:  # down
        player_soldier.y += consts.SQUARE_LENGTH
        state["pressed_key_down"] = True

def initialize_key_states():
    state["pressed_key_enter"] = False
    state["pressed_key_up"] = False
    state["pressed_key_down"] = False
    state["pressed_key_left"] = False
    state["pressed_key_right"] = False

def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end=" ")
        print()

def is_lose():
    game_surface = Screen.return_game_table()
    # print_matrix(game_surface)
    # print()
    for i in range(len(soldier_legs_location)):
        if game_surface[soldier_legs_location[i][1]][soldier_legs_location[i][0]] == "mine":
            return True
    return False

def is_win():
    pass

if __name__ == '__main__':
    main()
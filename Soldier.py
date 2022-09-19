import consts
import math


def player():
    player_soldier = {"image": consts.SOLDIER,
            "position_x": 0,
            "position_y": 0,
            "width": 40,
            "height": 80}
    return player_soldier

def legs_location(game_state, pos):
    # check current pos and update to new pos
        if game_state["pressed_key_up"]:
            pos[0][0] -= 1
            pos[1][0] -= 1
        elif game_state["pressed_key_left"]:
            pos[0][1] -= 1
            pos[1][1] -= 1
        elif game_state["pressed_key_down"]:
            pos[0][0] += 1
            pos[1][0] += 1
        elif game_state["pressed_key_right"]:
            pos[0][1] += 1
            pos[1][1] += 1
        return pos

def body_location(game_state,pos):
        initail = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]
        if game_state["pressed_key_up"]:
            pos[0][0] -= 1
            pos[1][0] -= 1
            pos[2][0] -= 1
            pos[3][0] -= 1
            pos[4][0] -= 1
            pos[5][0] -= 1
        elif game_state["pressed_key_down"]:
            pos[0][0] += 1
            pos[1][0] += 1
            pos[2][0] += 1
            pos[3][0] += 1
            pos[4][0] += 1
            pos[5][0] += 1
        elif game_state["pressed_key_right"]:
            pos[0][1] += 1
            pos[1][1] += 1
            pos[2][1] += 1
            pos[3][1] += 1
            pos[4][1] += 1
            pos[5][1] += 1
        elif game_state["pressed_key_left"]:
            pos[0][1] -= 1
            pos[1][1] -= 1
            pos[2][1] -= 1
            pos[3][1] -= 1
            pos[4][1] -= 1
            pos[5][1] -= 1
        return pos
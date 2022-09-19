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
    # borders
    pos_legs_first_corner = [[3,0],[3,1]]
    pos_legs_second_corner = [[3, 48], [3, 49]]
    pos_legs_third_corner = [[24,0],[24,1]]
    pos_legs_fourth_corner = [[24,48],[24,49]]
    # check current pos and update to new pos
    if compare_list(pos,pos_legs_first_corner) and compare_list(pos,pos_legs_second_corner):
        if game_state["pressed_key_up"]:
            pos[0][0] -= 1
            pos[1][0] -= 1
    elif compare_list(pos,pos_legs_first_corner) and compare_list(pos,pos_legs_third_corner):
        if game_state["pressed_key_left"]:
            pos[0][1] -= 1
            pos[1][1] -= 1
    elif compare_list(pos,pos_legs_third_corner) and compare_list(pos,pos_legs_fourth_corner):
        if game_state["pressed_key_down"]:
            pos[0][0] += 1
            pos[1][0] += 1
    elif compare_list(pos,pos_legs_second_corner) and compare_list(pos,pos_legs_fourth_corner):
        if game_state["pressed_key_right"]:
            pos[0][1] += 1
            pos[1][1] += 1
    return pos

def compare_list(pos1, pos2):
    check_list = True
    for i in range(len(pos1)):
        for j in range(len(pos1[i])):
            if pos1[i][j] != pos2[i][j]:
                check_list = True
            else:
                return False
    return check_list


def body_location(game_state,pos):
    initial_pos_body = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]
    second_pos_body = [[0,48],[0,49],[1,48],[1,49],[2,48],[2,49]]
    third_pos_body = [[21,0],[21,1],[22,0],[22,1],[23,0],[23,1]]
    if compare_list(pos,initial_pos_body) and compare_list(pos,second_pos_body):
        if game_state["pressed_key_up"]:
            pos[0][0] -= 1
            pos[1][0] -= 1
            pos[2][0] -= 1
            pos[3][0] -= 1
            pos[4][0] -= 1
            pos[5][0] -= 1
    elif compare_list(pos,third_pos_body):
        if game_state["pressed_key_down"]:
            pos[0][0] += 1
            pos[1][0] += 1
            pos[2][0] += 1
            pos[3][0] += 1
            pos[4][0] += 1
            pos[5][0] += 1
    elif compare_list(pos,second_pos_body):
        if game_state["pressed_key_right"]:
            pos[0][1] += 1
            pos[1][1] += 1
            pos[2][1] += 1
            pos[3][1] += 1
            pos[4][1] += 1
            pos[5][1] += 1
    elif compare_list(pos,initial_pos_body) and compare_list(pos,third_pos_body):
        if game_state["pressed_key_left"]:
            pos[0][1] -= 1
            pos[1][1] -= 1
            pos[2][1] -= 1
            pos[3][1] -= 1
            pos[4][1] -= 1
            pos[5][1] -= 1
    return pos
import consts
import math


def player():
    return {"image": consts.SOLDIER,
            "position_x": 0,
            "position_y": 0,
            "width": 40,
            "height": 80}

def legs_location(game_state, pos):
    # borders
    pos_legs_first_corner = [[3,0],[3,1]]
    pos_legs_second_corner = [[3, 48], [3, 49]]
    pos_legs_third_corner = [[24,0],[24,1]]
    pos_legs_fourth_corner = [[24,48],[24,49]]
    # check current pos and update to new pos
    if pos != pos_legs_first_corner and pos != pos_legs_second_corner :
        if game_state["pressed_key_up"]:
            pos[0][0] -= 1
            pos[1][0] -= 1
    elif pos != pos_legs_first_corner and pos != pos_legs_third_corner:
        if game_state["pressed_key_left"]:
            pos[0][1] -= 1
            pos[1][1] -= 1
    elif pos != pos_legs_third_corner and pos != pos_legs_fourth_corner:
        if game_state["pressed_key_down"]:
            pos[0][0] += 1
            pos[1][0] += 1
    elif pos != pos_legs_second_corner and pos != pos_legs_fourth_corner:
        if game_state["pressed_key_right"]:
            pos[0][1] += 1
            pos[1][1] += 1
    return pos


def body_location(game_state,pos):
    initial_pos_body = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]
    second_pos_body = [[0,48],[0,49],[1,48],[1,49],[2,48],[2,49]]
    third_pos_body = [[21,0],[21,1],[22,0],[22,1],[23,0],[23,1]]
    if pos != initial_pos_body and pos != second_pos_body:
        if game_state["pressed_key_up"]:
            pos[0][0] -= 1
            pos[1][0] -= 1
            pos[2][0] -= 1
            pos[3][0] -= 1
            pos[4][0] -= 1
            pos[5][0] -= 1
    elif pos != third_pos_body:
        if game_state["pressed_key_down"]:
            pos[0][0] += 1
            pos[1][0] += 1
            pos[2][0] += 1
            pos[3][0] += 1
            pos[4][0] += 1
            pos[5][0] += 1
    elif pos != second_pos_body:
        if game_state["pressed_key_right"]:
            pos[0][1] += 1
            pos[1][1] += 1
            pos[2][1] += 1
            pos[3][1] += 1
            pos[4][1] += 1
            pos[5][1] += 1
    elif pos !=initial_pos_body and pos != third_pos_body:
        if game_state["pressed_key_left"]:
            pos[0][1] -= 1
            pos[1][1] -= 1
            pos[2][1] -= 1
            pos[3][1] -= 1
            pos[4][1] -= 1
            pos[5][1] -= 1
    return pos
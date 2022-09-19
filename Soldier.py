import consts
import math


def player():
    return {"image": consts.SOLDIER,
            "pos": [0,0]}
def first_legs_location(player,game_state):
    pos_legs = [[3,0],[3,1]]
    # if game_state["pressed_key_up"]:
    #     pos_legs[0][0] -= 1
    #     pos_legs[1][0] -= 1
    if game_state["pressed_key_down"]:
        pos_legs[0][0] += 1
        pos_legs[1][0] += 1
    elif game_state["pressed_key_right"]:
        pos_legs[0][1] += 1
        pos_legs[1][1] += 1
    # elif game_state["pressed_key_left"]:
    #     pos_legs[0][1] -= 1
    #     pos_legs[1][1] -= 1
    return pos_legs

def first_legs_location(player,game_state,pos):
    if game_state["pressed_key_up"]:
        pos[0][0] -= 1
        pos[1][0] -= 1
    elif game_state["pressed_key_down"]:
        pos[0][0] += 1
        pos[1][0] += 1
    elif game_state["pressed_key_right"]:
        pos[0][1] += 1
        pos[1][1] += 1
    elif game_state["pressed_key_left"]:
        pos[0][1] -= 1
        pos[1][1] -= 1
    return pos

def body_location(player,game_state):
    initial_pos_body = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]
    if game_state["pressed_key_up"]:
        initial_pos_body[0][0] -= 1
        initial_pos_body[1][0] -= 1
    elif game_state["pressed_key_down"]:
        initial_pos_body[0][0] += 1
        initial_pos_body[1][0] += 1
    elif game_state["pressed_key_right"]:
        initial_pos_body[0][1] += 1
        initial_pos_body[1][1] += 1
    elif game_state["pressed_key_left"]:
        initial_pos_body[0][1] -= 1
        initial_pos_body[1][1] -= 1
    return initial_pos_body
import consts
import math


def player():
    return {"image": consts.SOLDIER,
            "pos": [0,0]}

def first_legs_location(game_state, pos):
    pos_legs = [[3,0],[3,1]]
    if pos != pos_legs:
        if game_state["pressed_key_up"]:
            pos[0][0] -= 1
            pos[1][0] -= 1
        elif game_state["pressed_key_left"]:
            pos[0][1] -= 1
            pos[1][1] -= 1
    if game_state["pressed_key_down"]:
        pos[0][0] += 1
        pos[1][0] += 1
    elif game_state["pressed_key_right"]:
        pos[0][1] += 1
        pos[1][1] += 1
    return pos

# def legs_location(player,game_state,pos):
#     if player.x/20 != 0 and player.y/20 != 0:
#         if game_state["pressed_key_up"]:
#             pos[0][0] -= 1
#             pos[1][0] -= 1
#         elif game_state["pressed_key_left"]:
#             pos[0][1] -= 1
#             pos[1][1] -= 1
#     elif game_state["pressed_key_down"]:
#         pos[0][0] += 1
#         pos[1][0] += 1
#     elif game_state["pressed_key_right"]:
#         pos[0][1] += 1
#         pos[1][1] += 1
#     return pos

def body_location(game_state,pos):
    initial_pos_body = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]
    if game_state["pressed_key_up"]:
        initial_pos_body[0][0] -= 1
        initial_pos_body[1][0] -= 1
        initial_pos_body[2][0] -= 1
        initial_pos_body[3][0] -= 1
        initial_pos_body[4][0] -= 1
        initial_pos_body[5][0] -= 1
    elif game_state["pressed_key_down"]:
        initial_pos_body[0][0] += 1
        initial_pos_body[1][0] += 1
        initial_pos_body[2][0] += 1
        initial_pos_body[3][0] += 1
        initial_pos_body[4][0] += 1
        initial_pos_body[5][0] += 1
    elif game_state["pressed_key_right"]:
        initial_pos_body[0][1] += 1
        initial_pos_body[1][1] += 1
        initial_pos_body[2][1] += 1
        initial_pos_body[3][1] += 1
        initial_pos_body[4][1] += 1
        initial_pos_body[5][1] += 1
    elif game_state["pressed_key_left"]:
        initial_pos_body[0][1] -= 1
        initial_pos_body[1][1] -= 1
        initial_pos_body[2][1] -= 1
        initial_pos_body[3][1] -= 1
        initial_pos_body[4][1] -= 1
        initial_pos_body[5][1] -= 1
    return initial_pos_body
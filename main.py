import pygame

import Screen
import consts

state = {
    "state": consts.RUNNING_STATE,
    "soldier_legs_location": consts.START_SOLDIER_LEGS_LOCATION,
    "is_window_open": True,
    "pressed_key_enter": False,
    "pressed_key_up": False,
    "pressed_key_down": False,
    "pressed_key_left": False,
    "pressed_key_Right": False
}

def main():
    pygame.init()
    Screen.draw_game()

    while state["is_window_open"]:
        handle_user_events()

def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False


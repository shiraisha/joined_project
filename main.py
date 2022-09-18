import pygame

import Screen
import consts

state = {
    "state": consts.RUNNING_STATE,
    "soldier_legs_location": consts.START_SOLDIER_LEGS_LOCATION,
    "is_window_open": True
}

def the_right_main():
    pygame.init()
    Screen.main()

    while state["is_window_open"]

import pygame as pg

def mode_choose_draw(easy_button, hard_button, medium_button):
    easy_button.create_button()
    hard_button.create_button()
    medium_button.create_button()
    pg.display.update()

def mode_choose_make(mouse_x, mouse_y):
    if 244 < mouse_x < 545 and 65 < mouse_y < 150:
        hardness = 0

    if 244 < mouse_x < 545 and 408 < mouse_y < 495:
        hardness = 2

    if 244 < mouse_x < 545 and 249 < mouse_y < 332:
        hardness = 1

    return hardness, False, True


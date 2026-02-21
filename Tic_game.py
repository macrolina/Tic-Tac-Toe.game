import pygame as pg

from Sprites import Sprites
from parameters import *
from events import Event
from menu.Easy_mode import EasyMode
from menu.Medium_mode import MediumMode
from menu.Hard_mode import HardMode
from mode_choose import *
from moves import move

pg.init()
pg.display.set_caption("Tic-Tac-Toe")
screen = pg.display.set_mode((WIDTH, HEIGHT))
surface= pg.Surface((WIDTH, HEIGHT))
screen.fill(WHITE)
pg.display.flip()

all_sprites = pg.sprite.Group()

def draw():
    screen.fill(WHITE)
    pg.draw.line(screen, BLACK, (283, 77), (283, 606), 2)
    pg.draw.line(screen, BLACK, (490, 77), (490, 606), 2)
    pg.draw.line(screen, BLACK, (112, 242), (654, 242), 2)
    pg.draw.line(screen, BLACK, (654, 430), (112, 430), 2)
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.update()

easy_button = EasyMode(screen, all_sprites, draw)
medium_button = MediumMode(screen, all_sprites, draw)
hard_button = HardMode(screen, all_sprites, draw)

while running:
    if not mode_choose:
        for event in pg.event.get():

            if draw_allowed:
                draw()
                draw_allowed=False

            if event.type == pg.QUIT:
                pg.quit()
                running = False

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                secret=move(hardness, all_sprites, screen, draw)

                if secret=='win':
                    hardness, mode_choose, draw_allowed=-1, True, False

    else:
        screen.fill(WHITE)
        mode_choose_draw(easy_button, hard_button, medium_button)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                running = False

            elif event.type == pg.MOUSEBUTTONDOWN:

                mouse_x, mouse_y=pg.mouse.get_pos()
                hardness, mode_choose, draw_allowed=mode_choose_make(mouse_x, mouse_y)



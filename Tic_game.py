import pygame as pg

from Sprites import Sprites
from parameters import *
from events import Event
from menu.Easy_mode import EasyMode
from menu.Medium_mode import MediumMode
from menu.Hard_mode import HardMode
from moves import move

pg.init()
pg.display.set_caption("Tic-Tac-Toe")
screen = pg.display.set_mode((WIDTH, HEIGHT))
surface= pg.Surface((WIDTH, HEIGHT))
screen.fill(WHITE)
pg.display.flip()

all_sprites = pg.sprite.Group()

def draw():
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
            if event.type == pg.QUIT:
                pg.quit()
                running = False

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                move(hardness, all_sprites, screen, draw)

    else:
        easy_button.create_button()
        hard_button.create_button()
        medium_button.create_button()
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                running = False

            elif event.type == pg.MOUSEBUTTONDOWN:

                mouse_x, mouse_y = pg.mouse.get_pos()

                if 244 < mouse_x < 545 and 65 < mouse_y < 150:
                    hardness=0
                    mode_choose=False
                    screen.fill(WHITE)
                    pg.display.update()
                    draw()

                if 244 < mouse_x < 545 and 408 < mouse_y < 495:
                    hardness=2
                    mode_choose=False
                    screen.fill(WHITE)
                    pg.display.update()
                    draw()

                if 244 < mouse_x < 545 and 249 < mouse_y < 332:
                    hardness=1
                    mode_choose=False
                    screen.fill(WHITE)
                    pg.display.update()
                    draw()
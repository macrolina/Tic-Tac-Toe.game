import pygame as pg
from Bot import bot_hard as hard
from Sprites import Sprites
from Event_check import Game, game_check
from parameters import *
from events import Event

pg.init()
pg.display.set_caption("Tic-Tac-Toe")
screen = pg.display.set_mode((WIDTH, HEIGHT))
surface= pg.Surface((WIDTH, HEIGHT))
screen.fill(WHITE)
pg.display.flip()

all_sprites = pg.sprite.Group()
action_sprites=pg.sprite.Group()
pg.draw.line(screen, BLACK, (283, 77), (283, 606), 2)
pg.draw.line(screen, BLACK, (490, 77), (490, 606), 2)
pg.draw.line(screen, BLACK, (112, 242), (654, 242), 2)
pg.draw.line(screen, BLACK, (654, 430), (112, 430), 2)
all_sprites.update()
all_sprites.draw(screen)
pg.display.update()

action=Event(screen)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            cross = Sprites.Cross(0, 0)
            circle = Sprites.Circle(0, 0)
            hard_mode=hard.BotHardMode("circle", place_game, circle, all_sprites, choose, action)
            #easy_mode=easy.BotEasyMode("circle", place_game, circle, all_sprites, choose, action)

            if cross.player == True:
                if 120 < mouse_x < 281 and 80 < mouse_y < 240 and place_game[0][0] == None:
                    cross.rect.x = 100
                    cross.rect.y = 62
                    place_game[0][0]='X'
                    choose[0][0]=None
                    all_sprites.add(cross)
                elif 285 < mouse_x < 488 and 80 < mouse_y < 240 and place_game[0][1] == None:
                    cross.rect.x = 300
                    cross.rect.y = 62
                    place_game[0][1]='X'
                    choose[0][1]=None
                    all_sprites.add(cross)
                elif 492<mouse_x<740 and 80<mouse_y< 240 and place_game[0][2]==None:
                    cross.rect.x = 500
                    cross.rect.y = 62
                    place_game[0][2] = 'X'
                    choose[0][2] = None
                    all_sprites.add(cross)

                elif 120 < mouse_x < 281 and 244 < mouse_y < 428 and place_game[1][0] == None:
                    cross.rect.x = 100
                    cross.rect.y = 250
                    place_game[1][0]='X'
                    choose[1][0]=None
                    all_sprites.add(cross)
                elif 285 < mouse_x < 488 and 244 < mouse_y < 428 and place_game[1][1] == None:
                    cross.rect.x = 300
                    cross.rect.y = 250
                    place_game[1][1] = 'X'
                    choose[1][1] = None
                    all_sprites.add(cross)
                elif 492 < mouse_x < 740 and 244 < mouse_y < 428 and place_game[1][2] == None:
                    cross.rect.x = 500
                    cross.rect.y = 250
                    place_game[1][2] = 'X'
                    choose[1][2] = None
                    all_sprites.add(cross)

                elif 120 < mouse_x < 281 and 432 < mouse_y < 600 and place_game[2][0] == None:
                    cross.rect.x = 100
                    cross.rect.y = 438
                    place_game[2][0]='X'
                    choose[2][0]=None
                    all_sprites.add(cross)
                elif 285 < mouse_x < 500 and 432 < mouse_y < 600 and place_game[2][1] == None:
                    cross.rect.x = 300
                    cross.rect.y = 438
                    place_game[2][1] = 'X'
                    choose[2][1] = None
                    all_sprites.add(cross)
                elif 492 < mouse_x < 740 and 432 < mouse_y < 600 and place_game[2][2] == None:
                    cross.rect.x = 500
                    cross.rect.y = 438
                    place_game[2][2] = 'X'
                    choose[2][2] = None
                    all_sprites.add(cross)

                hard_mode.bot_move()

                if game_check(place_game)=="won":
                    screen.fill(WHITE)
                    Game(place_game, action)
                    pg.display.update()

                elif game_check(place_game)==None and place_game[0].count(None)==0 and place_game[1].count(None)==0 and place_game[2].count(None)==0:
                    screen.fill(WHITE)
                    action.equally()
                    pg.display.update()

                else:
                    all_sprites.update()
                    all_sprites.draw(screen)
                    pg.display.update()

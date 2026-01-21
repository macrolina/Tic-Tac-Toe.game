import pygame as pg
from parameters import *
from Sprites import Sprites
from Bot.bot_easy import BotEasyMode
from Bot.bot_medium import BotMediumMode
from Bot.bot_hard import BotHardMode
from events import Event
from Event_check import game_check, Game
from menu.again_button import Start_AgainButton

def move(hardness: int, all_sprites, screen, draw):
    global place_game
    global choose

    mouse_x, mouse_y = pg.mouse.get_pos()
    cross = Sprites.Cross(0, 0)
    circle = Sprites.Circle(0, 0)

    action=Event(screen)

    easy=BotEasyMode("circle", place_game, circle, all_sprites, choose, event=Event(screen))
    medium=BotMediumMode("circle", place_game, circle, all_sprites, choose, event=Event(screen))
    hard=BotHardMode("circle", place_game, circle, all_sprites, choose, event=Event(screen))

    start_again = Start_AgainButton(screen, all_sprites, draw)

    if cross.player == True:
        if 120 < mouse_x < 281 and 80 < mouse_y < 240 and place_game[0][0] == None:
            cross.rect.x = 100
            cross.rect.y = 62
            place_game[0][0 ] ='X'
            choose[0][0 ] =None
            all_sprites.add(cross)
        elif 285 < mouse_x < 488 and 80 < mouse_y < 240 and place_game[0][1] == None:
            cross.rect.x = 300
            cross.rect.y = 62
            place_game[0][1 ] ='X'
            choose[0][1 ] =None
            all_sprites.add(cross)
        elif 492 <mouse_x <740 and 80 <mouse_y< 240 and place_game[0][2]==None:
            cross.rect.x = 500
            cross.rect.y = 62
            place_game[0][2] = 'X'
            choose[0][2] = None
            all_sprites.add(cross)

        elif 120 < mouse_x < 281 and 244 < mouse_y < 428 and place_game[1][0] == None:
            cross.rect.x = 100
            cross.rect.y = 250
            place_game[1][0 ] ='X'
            choose[1][0 ] =None
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
            place_game[2][0 ] ='X'
            choose[2][0 ] =None
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

        if hardness==0:
            easy.bot_move()
        elif hardness==1:
            medium.bot_move()
        elif hardness==2:
            hard.bot_move()

        if game_check(place_game )=="won":
            screen.fill(WHITE)
            Game(place_game, action)
            start_again.create_button()
            pg.display.update()

            if 280 <mouse_x <530 and 560 <mouse_y <620:
                place_game = [[None for i in range(3)] for j in range(3)]
                choose = [[[100, 62], [300, 62], [500, 62]],
                          [[100, 250], [300, 250], [500, 250]],
                          [[100, 438], [300, 438], [500, 438]]]
                all_sprites.empty()
                pg.display.update()
                start_again.start_again()

        elif game_check(place_game)==None and place_game[0].count(None)==0 and place_game[1].count(None)==0 and place_game[2].count(None)==0:
            screen.fill(WHITE)
            action.equally()
            start_again.create_button()
            pg.display.update()

            if 280 <mouse_x <530 and 560 <mouse_y <620:
                place_game = [[None for i in range(3)] for j in range(3)]
                choose = [[[100, 62], [300, 62], [500, 62]],
                          [[100, 250], [300, 250], [500, 250]],
                          [[100, 438], [300, 438], [500, 438]]]
                all_sprites.empty()
                pg.display.update()
                start_again.start_again()

        else:
            all_sprites.update()
            all_sprites.draw(screen)
            pg.display.update()

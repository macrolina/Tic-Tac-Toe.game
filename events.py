import pygame as pg
from parameters import RED, GREEN, BLACK, HEIGHT, WIDTH, GREY
class Event:
    def __init__(self, screen):
        self.screen=screen
        self.font=pg.font.Font("ComicRelief.ttf", 30)

    def won(self):
        win_text=self.font.render("Congratulation! You won!", True, BLACK)
        win_rect=win_text.get_rect()
        win_rect.center=(WIDTH//2, 60)
        pg.draw.rect(self.screen, GREEN, pg.Rect((200, 15), (WIDTH//2, 100)))
        self.screen.blit(win_text, win_rect)

    def lose(self):
        lose_text=self.font.render("Oh... You lose..", True, BLACK)
        lose_rect=lose_text.get_rect()
        lose_rect.center=(WIDTH//2, 60)
        pg.draw.rect(self.screen, RED, pg.Rect((200, 15), (WIDTH//2, 100)))
        self.screen.blit(lose_text, lose_rect)

    def equally(self):
        equally_text=self.font.render("Equally", True, BLACK)
        equally_rect=equally_text.get_rect()
        equally_rect.center=(WIDTH//2, 60)
        pg.draw.rect(self.screen, GREY, pg.Rect((200, 15), (WIDTH//2, 100)))
        self.screen.blit(equally_text, equally_rect)



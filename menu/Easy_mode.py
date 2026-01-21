import pygame as pg
#from mode import Mode

class Mode:
    def __init__(self, screen, all_sprites, draw):
        self.font = pg.font.SysFont("Arial", 45)

        self.screen = screen
        self.sprites = all_sprites
        self.draw = draw
        #self.mode=mode

    def click(self):
        self.game_star()

    def game_start(self):
        self.screen.fill((255, 255, 255))
        self.draw()

        mode.bot_move()

    def create_button(self):
        pass

class EasyMode(Mode):
    def __init__(self, screen, all_sprites, draw):
        super().__init__(screen, all_sprites, draw)

    def click(self):
        super().click()
        return 1

    def create_button(self):
        easy_text=self.font.render("Easy mode", True, (0, 0, 0))
        easy_rect=easy_text.get_rect()
        easy_rect.center=(394, 100)
        pg.draw.rect(self.screen, (0, 255, 0), pg.Rect((245, 65), (300, 85)))
        self.screen.blit(easy_text, easy_rect)

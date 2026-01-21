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

class HardMode(Mode):
    def __init__(self, screen, all_sprites, draw):
        super().__init__(screen, all_sprites, draw)

    def click(self):
        super().click()
        return 3

    def create_button(self):
        hard_text=self.font.render("Hard mode", True, (0, 0, 0))
        hard_rect=hard_text.get_rect()
        hard_rect.center=(394, 444)
        pg.draw.rect(self.screen, (255, 0, 0), pg.Rect((245, 409), (300, 85)))
        self.screen.blit(hard_text, hard_rect)


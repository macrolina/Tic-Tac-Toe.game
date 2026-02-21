import pygame as pg

class ChooseModeAgain:
    def __init__(self, screen, all_sprites):
        self.font=pg.font.SysFont("Arial", 45)

        self.screen=screen
        self.sprites=all_sprites

    def create_button(self):
        mode_text=self.font.render("Choose mode", True, (0, 0, 0))
        mode_rec=mode_text.get_rect()
        mode_rec.center=(400, 488)
        pg.draw.rect(self.screen, (253, 218, 13), pg.Rect((280, 460), (250, 60)))
        self.screen.blit(mode_text, mode_rec)

import pygame as pg

class Start_AgainButton:
    def __init__(self, screen, all_sprites, draw):
        self.font=pg.font.SysFont("Arial", 45)

        self.screen=screen
        self.sprites=all_sprites
        self.draw=draw

    def click(self):
        self.start_again()

    def start_again(self):
        self.screen.fill((255, 255, 255))

        self.draw()


    def create_button(self):
        start_text=self.font.render("Start again", True, (0, 0, 0))
        start_rect=start_text.get_rect()
        start_rect.center=(400, 588)
        pg.draw.rect(self.screen, (255, 255, 0), pg.Rect((280, 560), (250, 60)))
        self.screen.blit(start_text, start_rect)

# x 280-530
# y 560-620












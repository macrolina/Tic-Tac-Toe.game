from pygame import font
class Mode:
    def __init__(self, screen, all_sprites, draw):
        self.font = font.SysFont("Arial", 45)

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
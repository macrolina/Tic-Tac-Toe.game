from pygame import display

place_game = [[None for i in range(3)] for j in range(3)]
choose = [[[100, 62], [300, 62], [500, 62]],
          [[100, 250], [300, 250], [500, 250]],
          [[100, 438], [300, 438], [500, 438]]]

WIDTH = 800
HEIGHT = 700
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (120, 120, 120)

running = True
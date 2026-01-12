import pygame as pg

size=(175, 175)

cross_picture_old = pg.image.load("Picture/Cross.png")
cross_picture = pg.transform.scale(cross_picture_old, size)
circle_picture_old = pg.image.load("Picture/Circle.png")
circle_picture = pg.transform.scale(circle_picture_old, size)

class Cross(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.bot = False
        self.player = True

        self.image = cross_picture
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

class Circle(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.bot = False
        self.player = False

        self.image = circle_picture
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
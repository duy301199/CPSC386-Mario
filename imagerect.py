import pygame as pg

class ImageRect:
    def __init__(self, screen, height, width):
        self.screen = screen
        self.height = height
        self.width = width

        self.image = pg.Surface((self.height, self.width))
        sprite_sheet = pg.image.load('images/allsprites.png')

        self.image.blit(sprite_sheet, (0,0), (60, 0, self.height, self.width))
        self.image = pg.transform.scale(self.image, (self.height, self.width))

        self.rect = self.image.get_rect()


    def __str__(self):
        return 'imagerect(' + str(self.image) + str(self.rect) + ')'

    def draw(self):
        self.screen.blit(self.image, self.rect)
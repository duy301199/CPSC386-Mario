import pygame as pg
from pygame.sprite import Sprite


class Pole(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        self.image = pg.Surface((20, 200))
        sprite_sheet = pg.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sprite_sheet, (0, 0), (320, 0, 20, 150))
        self.image = pg.transform.scale(self.image, (60, 550))
        self.rect = self.image.get_rect()
        self.rect.x = 8002
        self.rect.y = 148

    def draw(self):
        self.screen.blit(self.image, self.rect)
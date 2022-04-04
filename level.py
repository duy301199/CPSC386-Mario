import pygame as pg

class Level:
    def __init__(self, screen, settings, level_map, bricks):
        self.screen = screen
        self.settings = settings
        self.bricks = bricks
        self.level_map = level_map
        self.image = pg.image.load('images/level_bg.png')
        self.image = pg.transform.scale(self.image, (10910, self.settings.screen_height))
        self.rect = self.image.get_rect()

        self.shift_level = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def shifting_level(self, shifting_x):
        self.shift_level += shifting_x
        self.rect.x += shifting_x

        for brick in self.bricks:
            brick.rect.x += shifting_x
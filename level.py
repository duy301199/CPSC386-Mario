import pygame as pg

class Level:
    def __init__(self, screen, settings, pipes, level_map, bricks, upper, flags, poles):
        self.screen = screen
        self.settings = settings
        self.pipes = pipes
        self.flags = flags
        self.poles = poles
        self.bricks = bricks
        self.upper = upper
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

        for flag in self.flags:
            flag.rect.x += shifting_x
        for pole in self.poles:
            pole.rect.x += shifting_x
        for pipe in self.pipes:
            pipe.rect.x += shifting_x
        for brick in self.bricks:
            brick.rect.x += shifting_x
        for upper in self.upper:
            upper.rect.x += shifting_x

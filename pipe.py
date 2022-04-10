import pygame as pg
from pygame.sprite import Sprite


class Pipe(Sprite):
    def __init__(self, screen, settings, num):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.num = num
        self.screen_rect = screen.get_rect()

        self.pipe = []

        self.pipe_loc = [1150, 1450, 1800, 2260, 6600, 7200, 600, 550]
        self.height = [83, 125, 167, 167, 83, 83, 520, 264]
        self.image = pg.Surface((40, 200))
        sprite_sheet = pg.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sprite_sheet, (0, 0), (200, 0, 40, 40))
        self.image = pg.transform.scale(self.image, (120, 100))
        self.rect = self.image.get_rect()

        # small pipe
        pipe_image = pg.Surface((32, 33))
        pipe_image.set_colorkey((0, 0, 0))
        pipe_image.blit(sprite_sheet, (0, 0), (200, 0, 40, 40))
        small_pipe = pg.transform.scale(pipe_image, (80, 85))

        # medium pipe
        med_pipe_image = pg.Surface((32, 100))
        med_pipe_image.set_colorkey((0, 0, 0))
        med_pipe_image.blit(sprite_sheet, (0, 0), (200, 40, 40, 50))
        med_pipe = pg.transform.scale(med_pipe_image, (80, 260))

        # tall pipe
        tall_pipe_image = pg.Surface((32, 200))
        tall_pipe_image.set_colorkey((0, 0, 0))
        tall_pipe_image.blit(sprite_sheet, (0, 0), (200, 90, 40, 80))
        tall_pipe = pg.transform.scale(tall_pipe_image, (80, 520))

        # underground pipe top part
        top_under_pipe_image = pg.Surface((30, 100))
        top_under_pipe_image.set_colorkey((0, 0, 0))
        top_under_pipe_image.blit(sprite_sheet, (0, 0), (273, 0, 30, 144))
        top_under_pipe = pg.transform.scale(top_under_pipe_image, (65, 260))

        # underground pipe bottom part
        bot_under_pipe_image = pg.Surface((60, 40))
        bot_under_pipe_image.set_colorkey((0, 0, 0))
        bot_under_pipe_image.blit(sprite_sheet, (0, 0), (250, 144, 60, 50))
        bot_under_pipe = pg.transform.scale(bot_under_pipe_image, (130, 90))

        # stores pipes in list
        self.pipe.append(small_pipe)
        self.pipe.append(med_pipe)
        self.pipe.append(tall_pipe)
        self.pipe.append(tall_pipe)
        self.pipe.append(small_pipe)
        self.pipe.append(small_pipe)
        self.pipe.append(top_under_pipe)
        self.pipe.append(bot_under_pipe)

        self.image = self.pipe[self.num]
        self.rect = self.image.get_rect()
        self.rect.x = self.pipe_loc[self.num]
        self.rect.y = self.settings.base_level - self.height[self.num]

    def blitme(self):
        self.screen.blit(self.image, self.rect)
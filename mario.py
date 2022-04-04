import pygame as pg
from pygame.sprite import Sprite


class Mario(Sprite):
    def __init__(self, screen, settings, bricks, stats, ground, invisible_bricks):
        super(Mario, self).__init__()

        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.ground = ground
        self.invisible_bricks = invisible_bricks
        self.bricks = bricks
        self.screen_rect = screen.get_rect()
        self.x_change = 0
        self.y_change = 0

        self.mario = []
        self.image = pg.Surface((16,16))
        sprite_sheet = pg.image.load('images/allsprites.png')
        self.rect = self.image.get_rect()

        self.move_left = False
        self.move_right = False
        self.jump = False
        self.face_right = False
        self.crouch = False

        for i in range(0,13):
            mario_img = pg.Surface((17,16))
            mario_img.blit(sprite_sheet, (0,0), (59,i*20, 17, 16))
            img = pg.transform.scale(mario_img, (40,40))
            self.mario.append(img)

    def move(self):
        if not self.stats.underground_level:
            brick_collide = pg.sprite.spritecollide(self, self.bricks, False)
            for brick in brick_collide:
                if self.rect.right >= brick.rect.left and brick.rect.bottom == self.rect.bottom:
                    self.x_change = 0
                if self.rect.left <= brick.rect.right and brick.rect.bottom == self.rect.bottom:
                    self.x_change = 0

            brick_collide = pg.sprite.spritecollide(self, self.bricks, False)
            for brick in brick_collide:
                if self.y_change > 0:
                    self.rect.bottom = brick.rect.top
                elif self.y_change < 0:
                    self.rect.top = brick.rect.bottom
                self.y_change = 0

        if self.stats.underground_level:
            brick_collide = pg.sprite.spritecollide(self, self.invisible_bricks, False)
            for brick in brick_collide:
                if self.rect.right >= brick.rect.left and brick.rect.bottom == self.rect.bottom:
                    self.x_change = 0
                if self.rect.left <= brick.rect.right and brick.rect.bottom == self.rect.bottom:
                    self.x_change = 0

            brick_collide = pg.sprite.spritecollide(self, self.invisible_bricks, False)
            for brick in brick_collide:
                if self.y_change > 0:
                    self.rect.bottom = brick.rect.top
                elif self.y_change < 0:
                    self.rect.top = brick.rect.bottom
                self.y_change = 0

    def move_left(self):
        if self.rect.left <= 20:
            self.x_change = 0
        else:
            self.x_change = -3
        self.move_left = True
        self.face_right = False

    def move_right(self):
        self.x_change = 3
        self.move_right = True
        self.face_right = True

    def stop(self):
        self.x_change = 0
        self.move_left = False
        self.move_right = False

    def mario_jump(self):
        self.y_change = -6
        self.jump = True

    def draw(self):
        self.screen.blit(self.mario[0], self.rect)

    def reset(self):
        self.bricks.empty()

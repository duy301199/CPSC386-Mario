import pygame as pg
from pygame.sprite import Sprite


class Brick(Sprite):

    BRICK_SIZE = 50

    def __init__(self, screen, settings, block_type):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.block_type = block_type
        self.swap_brick = False

        self.size_brick = Brick.BRICK_SIZE
        self.brick = "images/Red_Brick.png"
        self.item_brick = "images/Item_Brick.png"
        self.stone = "images/Ground_Brick.png"
        self.stair_brick = "images/Stair_Brick.png"
        self.empty_brick = "images/Empty_Brick.png"
        self.invisible_brick = "images/Invisible_Block.png"
        self.blue_brick = "images/Blue_Brick.png"
        self.blue_stone = "images/Blue_Stone.png"

        if block_type == 0:
            self.image = pg.image.load(self.brick)
        if block_type == 1:
            self.image = pg.image.load(self.item_brick)
        if block_type == 2:
            self.image = pg.image.load(self.item_brick)
        if block_type == 3:
            self.image = pg.image.load(self.stone)
        if block_type == 4:
            self.image = pg.image.load(self.stair_brick)
        if block_type == 5:
            self.image = pg.image.load(self.brick)
        if block_type == 6:
            self.image = pg.image.load(self.invisible_brick)
        if block_type == 7:
            self.image = pg.image.load(self.blue_brick)
        if block_type == 8:
            self.image = pg.image.load(self.blue_stone)
        if block_type == 9:
            self.image = pg.image.load(self.brick)

        self.image = pg.transform.scale(self.image, (self.size_brick, self.size_brick))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.position = self.rect.y
        self.frame_counter = 0
        self.bounce = False

    def change(self):
        self.image = pg.image.load(self.empty_brick)
        self.image = pg.transform.scale(self.image, (self.size_brick, self.size_brick))

    def update(self):
        if self.bounce:
            if self.frame_counter <= 5:
                self.rect.y -= 1
            elif self.frame_counter <= 10:
                self.rect.y += 1
            else:
                self.frame_counter = 0
                self.bounce = False
            self.frame_counter += 1
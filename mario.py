import pygame as pg
from pygame.sprite import Sprite
from map import Map
from upper import UPPER
from level import Level

class Mario(Sprite):
    def __init__(self, screen, settings, pipes, bricks, upper, stats, poles, invisible_bricks, invisible_pipes, ground):
        super(Mario, self).__init__()

        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.ground = ground
        self.invisible_bricks = invisible_bricks
        self.bricks = bricks
        self.poles = poles
        self.upper = upper
        self.pipes = pipes
        self.invisible_pipes = invisible_pipes
        #self.level = level
        self.screen_rect = screen.get_rect()
        #self.x_change = 0
        #self.y_change = 0

        self.small_mario = []
        self.small_star_mario = []
        self.shroom_mario = []
        self.flower_mario = []
        self.star_mario = []
        self.image = pg.Surface((16, 16))
        sprite_sheet = pg.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sprite_sheet, (0, 0), (59, 0, 17, 16))
        self.image = pg.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

        # Movement Flags
        self.move_left = False
        self.move_right = False
        self.jump = False
        self.face_right = True
        self.crouch = False

        for i in range(0,13):
            mario_img = pg.Surface((17,16))
            mario_img.set_colorkey((0, 0, 0))
            mario_img.blit(sprite_sheet, (0,0), (59,i * 20, 17, 16))
            img = pg.transform.scale(mario_img, (40,40))
            self.small_mario.append(img)

            mario_img = pg.Surface((17, 16))
            mario_img.set_colorkey((0, 0, 0))
            mario_img.blit(sprite_sheet, (0, 0), (80, i * 20, 17, 16))
            img = pg.transform.scale(mario_img, (40, 40))
            self.small_star_mario.append(img)

            mario_img = pg.Surface((17, 16))
            mario_img.set_colorkey((0, 0, 0))
            mario_img.blit(sprite_sheet, (0, 0), (100, i * 20, 17, 16))
            img = pg.transform.scale(mario_img, (40, 40))
            self.small_star_mario.append(img)

            mario_img = pg.Surface((17, 32))
            mario_img.set_colorkey((0, 0, 0))
            mario_img.blit(sprite_sheet, (0, 0), (120, i * 40, 17, 32))
            img = pg.transform.scale(mario_img, (40, 60))
            self.shroom_mario.append(img)

            mario_img = pg.Surface((17, 32))
            mario_img.set_colorkey((0, 0, 0))
            mario_img.blit(sprite_sheet, (0, 0), (140, i * 40, 17, 32))
            img = pg.transform.scale(mario_img, (40, 60))
            self.flower_mario.append(img)
            self.star_mario.append(img)

            mario_img = pg.Surface((17, 32))
            mario_img.set_colorkey((0, 0, 0))
            mario_img.blit(sprite_sheet, (0, 0), (160, i * 40, 17, 32))
            img = pg.transform.scale(mario_img, (40, 60))
            self.star_mario.append(img)

        mario_img = pg.Surface((17,16))
        mario_img.set_colorkey((0,0,0))
        mario_img.blit(sprite_sheet, (0,0), (59,260,17,16))
        img = pg.transform.scale(mario_img, (40,40))
        self.small_mario.append(img)

        self.image = self.small_mario[0]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.x_change = 0
        self.y_change = 0

        self.frame_counter = 0
        self.flash_frame = 0
        self.star_timer = 0
        self.invincible_time = 0

        self.inv = False

        self.dead =  False
        self.shroomed = False
        self.star_pow = False

        self.count = 0

    def update(self, stats, level):
        self.invincible()
        if self.dead:
            self.image = self.small_mario[12]
            self.die_animate(stats, level)
        else:
            if not self.shroomed and not self.star_pow:
                self.update_small()
            elif self.star_pow and not self.shroomed:
                self.update_star()
            elif self.shroomed and not self.star_pow:
                self.update_shroomed()

    def update_small(self):
        self.move()
        if self.rect.y == self.settings.base_level - self.rect.height:
            self.jump = False

        if not self.move_right and not self.move_left and not self.jump:
            if self.face_right:
                self.image = self.small_mario[0]
            else:
                self.image = self.small_mario[6]
        if self.move_right and not self.jump:
            self.right_animate()
        if self.face_right and self.jump:
            self.image = self.small_mario[5]
        if self.move_left and not self.jump:
            self.left_animate()
        if not self.face_right and self.jump:
            self.image = self.small_mario[11]

    def update_shroomed(self):
        self.move()
        if self.rect.y == self.settings.base_level - self.rect.height:
            self.jump = False

        if not self.move_right and not self.move_left and not self.jump:
            if self.face_right:
                self.image = self.shroom_mario[0]
            else:
                self.image = self.shroom_mario[6]
        if self.move_right and not self.jump:
            self.big_right_animate()
        if self.face_right and self.jump:
            self.image = self.shroom_mario[5]
        if self.move_left and not self.jump:
            self.big_left_animate()
        if not self.face_right and self.jump:
            self.image = self.shroom_mario[11]

    def update_star(self):
        self.move()
        if self.rect.y == self.settings.base_level - self.rect.height:
            self.jump = False

        if not self.move_right and not self.move_left and not self.jump:
            self.star_flash()
        if self.move_right and not self.jump:
            self.right_star_flash()
        if self.face_right and self.jump:
            self.right_star_jump()
        if self.move_left and not self.jump:
            self.left_star_flash()
        if not self.face_right and self.jump:
            self.left_star_jump()

    def star_flash(self):
        if self.frame_counter <= 50:
            if self.face_right:
                self.image = self.small_star_mario[0]
            else:
                self.image = self.small_star_mario[12]
        elif self.frame_counter <= 100:
            if self.face_right:
                self.image = self.small_star_mario[1]
            else:
                self.image = self.small_star_mario[13]
        elif self.frame_counter <= 150:
            if self.face_right:
                self.image = self.small_mario[0]
            else:
                self.image = self.small_mario[6]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def move(self):
        if pg.sprite.spritecollide(self, self.poles, False):
            self.stats.reached_pole = True
            self.frame_counter = 0
            if self.rect.y != 508:
                self.rect.y += 1
            self.rect.x += self.x_change
        else:
            self.fall()
            if self.rect.left > 20:
                self.rect.x += self.x_change
            else:
                self.rect.x = 22
            if not self.stats.underground_level:
                pipe_collide = pg.sprite.spritecollide(self, self.pipes, False)
                for pipe in pipe_collide:
                    if self.x_change > 0:
                        self.rect.right = pipe.rect.left
                    if self.x_change < 0:
                        self.rect.left = pipe.rect.right
                self.rect.y += self.y_change

                pipe_collide = pg.sprite.spritecollide(self, self.pipes, False)
                for pipe in pipe_collide:
                    if self.y_change > 0:
                        self.rect.bottom = pipe.rect.top
                        if pipe.num == 3 and self.crouch:
                            self.stats.at_underground = True
                            self.stats.underground_level = True
                    elif self.y_change < 0:
                        self.rect.top = pipe.rect.bottom
                    self.y_change = 0

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

                    if brick.rect.x - 20 < self.rect.x < brick.rect.x + 20 and brick.rect.y < self.rect.y \
                            and brick.block_type == 5 and not brick.change_brick:
                        brick.change_brick = True
                        up = UPPER(self.screen, self.settings, self.pipes, self.bricks, brick.rect.x, brick.rect.y - 20,3)
                        self.upper.add(up)
                        brick.change()

                    if brick.rect.x - 20 < self.rect.x < brick.rect.x + 20 and brick.rect.y < self.rect.y \
                            and brick.block_type == 6 and not brick.change_brick:
                        brick.change_brick = True
                        up = UPPER(self.screen, self.settings, self.pipes, self.bricks, brick.rect.x, brick.rect.y - 20,2)
                        self.upper.add(up)
                        brick.change()

                    if brick.rect.x - 20 < self.rect.x < brick.rect.x + 20 and brick.rect.y < self.rect.y \
                            and brick.block_type == 2:
                        brick.change()
                        if brick.block_type == 2 and not brick.change_brick and brick.rect.y < self.rect.y \
                                and not self.shroomed:
                            brick.change_brick = True
                            up = UPPER(self.screen, self.settings, self.pipes, self.bricks, brick.rect.x, brick.rect.y - 20,0)
                            self.upper.add(up)
                        if brick.block_type == 2 and not brick.change_brick and brick.rect.y < self.rect.y \
                                and self.shroomed:
                            brick.change_brick = True
                            up = UPPER(self.screen, self.settings, self.pipes, self.bricks, brick.rect.x, brick.rect.y - 40,1)
                            self.upper.add(up)

                    if brick.rect.x - 20 < self.rect.x < brick.rect.x + 20 and brick.rect.y < self.rect.y \
                            and brick.block_type == 1:
                        brick.change()
                        self.stats.coins += 1

                    if brick.rect.x - 20 < self.rect.x < brick.rect.x + 20 and brick.rect.y < self.rect.y \
                            and brick.block_type == 9 and not brick.change_brick:
                        if self.count != 4:
                            self.stats.coins += 1
                            self.count += 1
                        else:
                            brick.change_brick = True
                            brick.change()




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

    def check_collision(self, screen, stats, display):
        # Checks if Mario ate the mushroom, fire flower, or star and if he did set the corresponding flag to true
        upper_collide = pg.sprite.spritecollide(self, self.upper, True)
        for up in upper_collide:
            if up.up_type == 0:
                self.shroomed = True
                display.give_score(screen, stats, up.rect.x, up.rect.y, 1000)
            if up.up_type == 1 and self.shroomed:
                self.fired = True
                display.give_score(screen, stats, up.rect.x, up.rect.y, 1000)
            if up.up_type == 2:
                self.stats.lives += 1
                display.give_score(screen, stats, up.rect.x, up.rect.y, 1000)
            if up.up_type == 3:
                self.star_pow = True
                display.give_score(screen, stats, up.rect.x, up.rect.y, 1000)
            if up.up_type == 4:
                self.stats.coins += 1
                self.stats.score += 200

    def right_animate(self):
        if self.frame_counter <= 50:
            self.image = self.small_mario[1]
        elif self.frame_counter <= 100:
            self.image = self.small_mario[2]
        elif self.frame_counter <= 150:
            self.image = self.small_mario[3]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def left_animate(self):
        if self.frame_counter <= 50:
            self.image = self.small_mario[7]
        elif self.frame_counter <= 100:
            self.image = self.small_mario[8]
        elif self.frame_counter <= 150:
            self.image = self.small_mario[9]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def right_star_flash(self):
        if self.frame_counter <= 50:
            self.image = self.small_star_mario[2]
        elif self.frame_counter <= 100:
            self.image = self.small_star_mario[5]
        elif self.frame_counter <= 150:
            self.image = self.small_mario[3]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def right_star_jump(self):
        if self.frame_counter <= 50:
            self.image = self.small_star_mario[10]
        elif self.frame_counter <= 100:
            self.image = self.small_star_mario[11]
        elif self.frame_counter <= 150:
            self.image = self.small_mario[5]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def left_star_jump(self):
        if self.frame_counter <= 50:
            self.image = self.small_star_mario[22]
        elif self.frame_counter <= 100:
            self.image = self.small_star_mario[23]
        elif self.frame_counter <= 150:
            self.image = self.small_mario[11]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def left_star_flash(self):
        if self.frame_counter <= 50:
            self.image = self.small_star_mario[14]
        elif self.frame_counter <= 100:
            self.image = self.small_star_mario[17]
        elif self.frame_counter <= 150:
            self.image = self.small_mario[9]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def big_left_animate(self):
        if self.frame_counter <= 50:
            self.image = self.shroom_mario[7]
        elif self.frame_counter <= 100:
            self.image = self.shroom_mario[8]
        elif self.frame_counter <= 150:
            self.image = self.shroom_mario[9]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def big_right_animate(self):
        if self.frame_counter <= 50:
            self.image = self.shroom_mario[1]
        elif self.frame_counter <= 100:
            self.image = self.shroom_mario[2]
        elif self.frame_counter <= 150:
            self.image = self.shroom_mario[3]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def invincible(self):
        if self.invincible_time < 100 and self.inv:
            self.invincible_time += 1
        else:
            self.inv = False
            self.invincible_time = 0

    def fall(self):
        if self.y_change == 0:
            self.y_change = 1
        else:
            self.y_change += .1

    def moving_left(self):
        if self.rect.left <= 20:
            self.x_change = 0
        else:
            self.x_change = -3
        self.move_left = True
        self.face_right = False

    def moving_right(self):
        self.x_change = 3
        self.move_right = True
        self.face_right = True

    def stoping(self):
        self.x_change = 0
        self.move_left = False
        self.move_right = False

    def jumping(self):
        self.y_change = -6
        self.jump = True

    def draw(self):
        if self.frame_counter <= 100:
            self.frame_counter += 5
            self.screen.blit(self.small_mario[13], self.rect)
        else:
            if not self.shroomed:
                self.screen.blit(self.image, self.rect)
            elif self.shroomed:
                big_rect = pg.Rect(self.rect.x, self.rect.y-20, self.rect.width, self.rect.height)
                self.screen.blit(self.image, big_rect)

    def die_animate(self, stats, level):
        self.image = self.small_mario[12]
        if self.frame_counter <= 100:
            self.rect.y -= 2
        elif self.frame_counter <= 200:
            self.rect.y += 2
        else:
            if stats.lives > 1:
              self.dead = False
              self.reset_mario(level)
              stats.lives -= 1
            else:
                stats.game_over = True
                if self.frame_counter >= 400:
                    stats.game_over = False
                    stats.reset_stats()
        self.frame_counter += 1

    def reset(self):
        self.bricks.empty()
        level.shifting_level(-level.shift_level)
        level_map = Map(self.screen, self.settings, self.bricks, self, self.ground, self.upper, self.stats, self.invisible_bricks)
        level_map.build_brick()
        self.rect.x = 100
        self.rect.y = 100

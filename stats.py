import pygame as pg

import os


class Stats:

    def __init__(self):

        self.game_active = True
        self.game_over = False

        self.at_underground = False
        self.at_main_level = True
        self.underground_level = False
        self.main_level = True
        self.return_main_level = False

        self.score = 0
        self.time = 400
        self.lives = 3
        self.timer = 0

        self.highscore = self.load_high_score()
        self.tick = pg.time.get_ticks()


    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except:
            return 0

    def save_high_score(self):
        try:
            with open("highscore.txt", "w+") as f:
                f.write(str(round(self.highscore, -1)))
        except:
            print("highscore.txt not found...")

    def update_time(self):
        seconds = (pg.time.get_ticks() - self.tick)/1000
        if seconds > 1:
            self.tick = pg.time.get_ticks()
            self.time -= 1
        if self.time == 0:
            self.game_over = True
        elif self.time < -2:
            self.game_over = False
            self.reset_stats()

    def reset_stats(self):
        self.score = 0
        self.time = 400
        self.lives = 3
        self.game_over = False
        self.at_underground = False
        self.at_main_level = True
        self.underground_level = False
        self.main_level = True
        self.return_main_level = False
import pygame as pg
import game_functions as gf
from stats import Stats
from sound import Sound
from pygame.sprite import Group
from map import Map
from mario import Mario
from level import Level
from settings import Settings


def run_game():
    pg.init()
    settings = Settings()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption("Super Mario")

    bricks = Group()
    invisible_bricks = Group()
    ground = Group()
    stats = Stats()
    sound = Sound()

    mario = Mario(screen, settings, bricks, stats, invisible_bricks, ground)
    level_map = None
    level = Level(screen, settings, level_map, bricks)
    sound.play_background()

    while True:

        if stats.at_main_level:
            level_map = Map(screen, settings, bricks, mario, ground, stats, invisible_bricks)
            level_map.build_brick()
            stats.at_main_level = False

        if stats.at_underground:
            level_map = Map(screen, settings, bricks, mario, ground, stats, invisible_bricks)
            level_map.build_brick()
            stats.at_underground = False
            stats.main_level = False

        if stats.game_active:
            gf.check_events(mario)
        gf.update(screen, mario, settings, level, bricks, stats, invisible_bricks)
        pg.display.flip()

run_game()
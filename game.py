import pygame as pg
import game_functions as gf
from stats import Stats
from sound import Sound
from pygame.sprite import Group
from map import Map
from mario import Mario
from level import Level
from display import Display
from settings import Settings
from flag import Flag
from pole import Pole
from pipe import Pipe


def run_game():
    pg.init()
    settings = Settings()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption("Super Mario")

    bricks = Group()
    invisible_bricks = Group()
    invisible_pipes = Group()
    ground = Group()
    stats = Stats()
    sound = Sound()
    upper = Group()
    poles = Group()
    flags = Group()
    pipes = Group()

    for i in range(6,8):
        pipe = Pipe(screen, settings, i)
        invisible_pipes.add(pipe)

    flag = Flag(screen, settings, stats)
    flags.add(flag)
    pole = Pole(screen, settings)
    poles.add(pole)

    mario = Mario(screen, settings, pipes, bricks, upper, stats, poles, invisible_bricks, invisible_pipes, ground)
    level_map = None
    level = Level(screen, settings, pipes, level_map, bricks, upper, flags, poles)
    display = Display(screen, stats)
    sound.play_background()

    while True:

        if stats.at_main_level:
            level_map = Map(screen, settings, bricks, pipes, mario, ground, upper, stats, invisible_bricks)
            level_map.build_brick()
            for i in range(0,6):
                pipe = Pipe(screen, settings, i)
                pipes.add(pipe)
            flag = Flag(screen, settings, stats)
            flags.add(flag)
            pole = Pole(screen, settings)
            poles.add(pole)
            stats.at_main_level = False

        if stats.at_underground:
            pipes.empty()
            bricks.empty()
            poles.empty()
            flags.empty()
            level_map = Map(screen, settings, bricks, pipes, mario, ground, upper, stats, invisible_bricks)
            level_map.build_brick()
            stats.at_underground = False
            stats.main_level = False

        if stats.game_active:
            if mario.rect.right >= 600 and stats.main_level:
                diff = mario.rect.right - 600
                mario.rect.right = 600
                level.shifting_level(-diff)

            gf.check_events(mario, stats)
            gf.update(screen, mario, settings, level, pipes, display, stats, bricks, upper, flags, poles, invisible_bricks, invisible_pipes)
            pg.display.flip()

run_game()
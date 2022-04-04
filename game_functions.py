import sys
import pygame as pg


def update(screen,mario, settings, level, bricks, stats, invisible_bricks):

    screen.fill(settings.bg_color)

    mario.update(stats,level)
    bricks.update()
    level.draw()
    bricks.draw(screen)

    if not stats.underground_level:
        level.draw()
        bricks.draw(screen)

    if stats.underground_level:
        invisible_bricks.draw(screen)

    mario.draw()
    stats.update_time()
    stats.save_high_score()

    if stats.game_over is True:
        screen.fill((0, 0, 0))
    pg.display.flip()

def check_events(mario):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                sys.exit()
            elif event.key == pg.K_LEFT:
                if mario.rect.left >= 20:
                    mario.move_left()
            elif event.key == pg.K_RIGHT:
                if mario.rect.right >= 20:
                    mario.move_right()
            elif event.key == pg.K_DOWN:
                mario.crouch = True
            elif event.key == pg.K_SPACE:
                if mario.y_change == 0:
                    mario.mario_jump()

        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                mario.stop()
            elif event.key == pg.K_RIGHT:
                mario.stop()
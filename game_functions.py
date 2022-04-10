import sys
import pygame as pg


def update(screen, mario, settings, level, pipes, display, stats, bricks, upper, flags, poles, invisible_bricks, invisible_pipes):

    screen.fill(settings.bg_color)
    if stats.flag_reach_bot and stats.timer <= 100:
        mario.moving_right()
        stats.timer += 1
    if stats.timer >= 100:
        mario.stop()
    mario.update(stats,level)
    flags.update()
    upper.update()
    bricks.update()
    mario.check_collision(screen, stats, display)

    if not stats.underground_level:
        level.draw()
        bricks.draw(screen)
        pipes.draw(screen)
        poles.draw(screen)
        flags.draw(screen)

    if stats.underground_level:
        invisible_bricks.draw(screen)
        invisible_pipes.draw(screen)

    mario.draw()
    upper.draw(screen)
    display.score_blit(screen,stats)
    stats.update_time()
    stats.save_high_score()

    if stats.game_over is True:
        screen.fill((0, 0, 0))
        display.over_blit(screen)
    pg.display.flip()

def check_events(mario, stats):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                sys.exit()
            elif event.key == pg.K_LEFT:
                if not stats.reached_pole:
                    if mario.rect.left >= 20:
                        mario.moving_left()
            elif event.key == pg.K_RIGHT:
                if not stats.reached_pole:
                    mario.moving_right()
            elif event.key == pg.K_DOWN:
                mario.crouch = True
            elif event.key == pg.K_SPACE:
                if not stats.reached_pole:
                    if mario.y_change == 0:
                        mario.jumping()

        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                mario.stoping()
            elif event.key == pg.K_RIGHT:
                mario.stoping()
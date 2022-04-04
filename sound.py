import pygame as pg

class Sound:
    def __init__(self):
        pg.mixer.init()

        self.background = pg.mixer.Sound('sounds/bg_music.wav')
        self.block_bump = pg.mixer.Sound('sounds/block_bump.wav')
        self.brick_break = pg.mixer.Sound('sounds/brick_break.wav')
        self.coin = pg.mixer.Sound('sounds/coin.wav')
        self.death = pg.mixer.Sound('sounds/death.wav')
        self.extra_life = pg.mixer.Sound('sounds/extra_life.wav')
        self.fireball = pg.mixer.Sound('sounds/fireball.wav')
        self.jump = pg.mixer.Sound('sounds/jump.wav')
        self.kill = pg.mixer.Sound('sounds/kill.wav')
        self.pipe = pg.mixer.Sound('sounds/pipe.wav')
        self.power_spawn = pg.mixer.Sound('sounds/power_spawn.wav')
        self.power_up = pg.mixer.Sound('sounds/powerup.wav')
        self.stage_clear = pg.mixer.Sound('sounds/stage_clear.wav')
        self.star = pg.mixer.Sound('sounds/star.wav')

    def play_music(self, music, volume=0.3):
        pg.mixer.music.unload()
        pg.mixer.music.load(music)
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.play(-1,0.0)

    def busy(self): return pg.mixer.get_busy()

    def play_sound(self, sound):
        pg.mixer.Sound.play(sound)

    def stop(self):
        pg.mixer.stop()

    def play_background(self): self.play_music('sounds/bg_music.wav')

    def stop_bg(self): pg.mixer.music.stop()

    def play_gameover(self):
        self.stop_bg()
        self.play_sound(self.death)
        while self.busy():
            pass

    def play_block_pump(self): self.play_sound(self.block_bump)
    def play_brick_break(self): self.play_sound(self.brick_break)

    def play_death(self):
        pg.mixer.stop()
        self.play_sound(self.death)

    def play_coin(self): self.play_sound(self.coin)
    def play_extra_life(self): self.play_sound(self.extra_life)
    def play_fireball(self): self.play_sound(self.fireball)
    def play_jump(self): self.play_sound(self.jump)
    def play_kill(self): self.play_sound(self.kill)
    def play_pipe(self): self.play_sound(self.pipe)
    def play_power_spawn(self): self.play_sound(self.power_spawn)
    def play_power_up(self): self.play_sound(self.power_up)
    def play_stage_clear(self): self.play_sound(self.stage_clear)
    def play_star(self): self.play_sound(self.star)


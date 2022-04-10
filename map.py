from brick import Brick
from upper import UPPER

class Map:

    BRICK_SIZE = 40

    def __init__(self, screen, settings, bricks, pipes, mario, ground, upper, stats, invisible_bricks):
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.pipes = pipes
        self.bricks = bricks
        self.mario = mario
        self.upper = upper
        self.invisible_bricks = invisible_bricks
        self.ground = ground
        self.main_level = 'images/level_loc.txt'
        self.underground_level = 'images/Underground_level.txt'

        if not self.stats.at_underground:
            with open(self.main_level, 'r') as o:
                self.rows = o.readlines()
                if self.stats.return_main_level:
                    self.mario.rect.x = 7210
                    self.mario.rect.y = 500
        if self.stats.at_underground:
            with open(self.underground_level, 'r') as o:
                self.rows = o.readlines()
                self.mario.rect.x = 100
                self.mario.rect.y = 100


        self.brick = None
        self.coin = None
        self.deltax = self.deltay = Map.BRICK_SIZE



    def build_brick(self):
        dx,dy = self.deltax, self.deltay

        for n in range(len(self.rows)):
            row = self.rows[n]
            for c in range(len(row)):
                col = row[c]
                if col == 'B':
                    Map.create_brick(self, c*dx, n*dy, 0)
                if col == '?':
                    Map.create_brick(self, c*dx, n*dy, 1)
                if col == 'X':
                    Map.create_brick(self, c*dx, n*dy, 3)
                if col == 'M':
                    Map.create_brick(self, c*dx, n*dy, 2)
                if col == 'R':
                    Map.create_brick(self, c*dx, n*dy, 4)
                if col == 'S':
                    Map.create_brick(self, c*dx, n*dy, 5)
                if col == 'I':
                    Map.create_brick(self, c*dx, n*dy, 6)
                if col == 'A':
                    Map.create_invisible_brick(self, c*dx, n*dy, 7)
                if col == 'N':
                    Map.create_invisible_brick(self, c*dx, n*dy, 8)
                if col == 'L':
                    Map.create_brick(self, c*dx, n*dy, 9)
    def draw(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)

    def create_brick(self, x, y, num):
        self.brick = Brick(self.screen, self.settings, num)
        self.brick.rect.x = x
        self.brick.rect.y = y
        self.bricks.add(self.brick)
        if num == 4:
            self.ground.add(self.brick)

    def create_invisible_brick(self, x, y, num):
        self.brick = Brick(self.screen, self.settings, num)
        self.brick.rect.x = x
        self.brick.rect.y = y
        self.invisible_bricks.add(self.brick)

    def create_coin(self, x,y,num):
        self.coin = UPPER(self.screen, self.settings, self.bricks, x,y,num)
        self.upper.add(self.coin)
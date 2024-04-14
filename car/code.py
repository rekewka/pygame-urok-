import pygame as pg
import random

pg.init()

screen = pg.display.set_mode((400, 600))

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(48, 352)
        self.image = pg.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(48, 352), 93)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom >= 600:
            self.rect.top = 93
            self.rect.center = (random.randint(48, 352), 93)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Main(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (200, 504)

    def update(self):
        pressed = pg.key.get_pressed()

        if self.rect.right < 400:
            if pressed[pg.K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.left > 0:
            if pressed[pg.K_LEFT] :
                self.rect.move_ip(-5, 0)




    def draw(self, surface):
        surface.blit(self.image, self.rect)

FPS = pg.time.Clock()
done = False

black = pg.Color(0,0,0)
white = pg.Color(255,255,255)
grey = pg.Color(128, 128, 128)
red = pg.Color(255, 0, 0)

car = Main()
enemy = Enemy()

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True


    car.update()
    enemy.move()

    screen.fill((255, 255, 255))
    car.draw(screen)
    enemy.draw(screen)

    pg.display.flip()
    FPS.tick(60)

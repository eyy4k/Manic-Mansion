import pygame as pg
from constants import *
from objekt import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

platforms = []

platform1 = pg.Rect((100, 100, 100, 20))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    vindu.fill(BLUE)
    pg.draw.rect(vindu, PURPLE, (0, 700, VINDU_BREDDE, (VINDU_BREDDE- 750)))

    


    pg.display.flip()
    clock.tick(FPS)

pg.quit()
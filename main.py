import pygame as pg
from constants import *
from objekt import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()



running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    vindu.fill(BLACK)

    


    pg.display.flip()
    clock.tick(FPS)

pg.quit()
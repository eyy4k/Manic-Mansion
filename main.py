import pygame as pg
from constants import *
from objekt import *

pg.init()
pg.mixer.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

coin_sound = pg.mixer.Sound("gulllyd.mp3")
coin_sound.set_volume(0.5)

gull_liste = [
    Gullmynter(300, 200),
    Gullmynter(400, 300),
    Gullmynter(600, 150)
]

platforms = []

platform1 = pg.Rect((100, 100, 100, 20))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    vindu.fill(BLUE)
    pg.draw.rect(vindu, PURPLE, (0, 700, VINDU_BREDDE, (VINDU_BREDDE- 750)))

    

    for gull in gull_liste:
        gull.tegn(vindu)
    

    pg.display.flip()
    clock.tick(FPS)

pg.quit()
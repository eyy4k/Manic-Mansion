import pygame as pg
from constants import *
from objekt import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

platforms = [
    pg.Rect((100, 100, 100, 20)),
    pg.Rect((300, 250, 150, 20)),
    pg.Rect((300, 200, 200, 20))
]

spøkelse1 = Spøkelse(200,200)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    vindu.fill(BLUE)
    pg.draw.rect(vindu, PURPLE, (0, 700, VINDU_BREDDE, (VINDU_BREDDE- 750)))
    
    #Tegner hindringer
    for p in platforms:
        pg.draw.rect(vindu, PURPLE, p)

    #Tegner spøkelser
    spøkelse1.tegn(vindu)
    spøkelse1.flytt()
    


    pg.display.flip()
    clock.tick(FPS)

pg.quit()
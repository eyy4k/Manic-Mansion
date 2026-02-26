import pygame as pg
from constants import *
from objekt import *

pg.init()
pg.mixer.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

coin_sound = pg.mixer.Sound("bilder/gulllyd.mp3")
coin_sound.set_volume(0.5)

gull_liste = [
    Gullmynter(900, 300),
    Gullmynter(800, 400),
    Gullmynter(850, 150)
]

platforms = []

spøkelse1 = Spøkelse(200,200)

spiller = Spiller(100,100)

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

    #Tegner Spiller
    spiller.tegnspiller(vindu)
    spiller.flytt()
    spiller.kolisjon(VINDU_BREDDE, VINDU_HOYDE)
    

    for gull in gull_liste[:]:
        if spiller.rect.colliderect(gull.rect):
            spiller.coins += 1
            coin_sound.play()
            gull_liste.remove(gull)

    
    
    #Tegner Gull
    for gull in gull_liste:
        gull.tegn(vindu)
    

    pg.display.flip()
    clock.tick(FPS)

pg.quit()
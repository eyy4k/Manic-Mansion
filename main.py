import pygame as pg
from constants import *
from objekt import *
from typing import List

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

platforms: List[Platform] = []

for _ in range(5):
    bredde = rd.randint(50, 150)
    hoyde = 20
    x = rd.randint(0, VINDU_BREDDE - bredde)
    y = rd.randint(50, VINDU_HOYDE - hoyde)
    
    platforms.append(Platform(x,y,bredde,hoyde))




spøkelser: List[Spøkelse] = []
for i in range(3):
    rand_x = rd.randint(VINDU_BREDDE//3, (VINDU_BREDDE//3 *2 ))
    rand_y = rd.randint(0, VINDU_HOYDE)
    spøkelse1 = Spøkelse(rand_x,rand_y)
    spøkelser.append(spøkelse1)


spiller = Spiller(rd.randint(0,VINDU_BREDDE//3),rd.randint(0, VINDU_HOYDE))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    vindu.fill(BLUE)
    pg.draw.rect(vindu, PURPLE, (0, 700, VINDU_BREDDE, (VINDU_BREDDE- 750)))
    
    #Tegner hindringer
    for p in platforms:
        p.tegn(vindu)

    #Tegner spøkelser
    for s in spøkelser:
        s.tegn(vindu)
        s.flytt(platforms)

    #Tegner Spiller
    spiller.tegnspiller(vindu)
    spiller.flytt(platforms)
    spiller.kolisjon(VINDU_BREDDE, VINDU_HOYDE)
    
    #kollksjon gull
    for gull in gull_liste[:]:
        if spiller.rect.colliderect(gull.rect):
            spiller.coins += 1
            coin_sound.play()
            gull_liste.remove(gull)
    """
    #kollisjon mellom spøkelser 
    for i in range(len(spøkelser)):
        for j in range(i + 1, len(spøkelser)):
            s1 = spøkelser[i]
            s2 = spøkelser[j]
            
            if s1.rect.colliderect(s2.rect):
                #bytter fart med hverandre
                s1.vx, s2.vx = s2.vx, s1.vx
                s1.vy, s2.vy = s2.vy, s1.vy
                
                #dytter dem litt for å hindre at de sticker sammen
                s1.rect.x += s1.vx
                s1.rect.x += s2.vx
                s1.rect.y += s1.vy
                s2.rect.y += s2.vy
    """
    
    #kollisjon mellom spøkelser og Spiller
    if spiller.kollisjon_spøkelse(spøkelser):
        #TODO vet ikke hva som skal skje etter kollisjon 
        print("traff en spøkelse")
        
            
                 
    #Tegner Gull
    for gull in gull_liste:
        gull.tegn(vindu)
    

    pg.display.flip()
    clock.tick(FPS)

pg.quit()
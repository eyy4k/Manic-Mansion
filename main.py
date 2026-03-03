import pygame as pg
from constants import *
from objekt import *
from typing import List
from pathlib import Path

pg.init()
pg.mixer.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

bgsti = Path(__file__).parent / "bilder" / "image.png"
original_bg = pg.image.load(bgsti).convert_alpha()

width, height = original_bg.size
print(width, height)


coin_sound = pg.mixer.Sound("bilder/gulllyd.mp3")
coin_sound.set_volume(0.5)

endesone_sound = pg.mixer.Sound("bilder/forsvinne.mp3")
endesone_sound.set_volume(0.5)

gull_liste: List[Gullmynter] = []
for i in range(3):
    rand_x = rd.randint(VINDU_BREDDE//3*2, VINDU_BREDDE)
    rand_y = rd.randint(0, VINDU_HOYDE)
    mynter = Gullmynter(rand_x,rand_y)
    gull_liste.append(mynter)



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
endesone = pg.Rect(10, 350, 125, 125)
tekst = pg.font.SysFont("arial", 30)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    vindu.fill(BLUE)
    pg.draw.rect(vindu, PURPLE, (0, 700, VINDU_BREDDE, (VINDU_BREDDE- 750)))

    vindu.blit(original_bg, (0,0))
    #Tegner Endesone
    pg.draw.rect(vindu, (75, 50, 100), endesone)
    
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
        if spiller.rect.colliderect(gull.rect) and spiller.carriescoin == False:
            coin_sound.play()
            spiller.carriescoin = True
            gull_liste.remove(gull)

    if spiller.rect.colliderect(endesone) and spiller.carriescoin:
        spiller.carriescoin = False
        spiller.coins += 1
        endesone_sound.play()

        #Legger til en spøkelse
        spøkelse1 = Spøkelse(rd.randint(VINDU_BREDDE//3, (VINDU_BREDDE//3 *2 )),rd.randint(0, VINDU_HOYDE))
        spøkelser.append(spøkelse1)
        
        #Legger til en hindring
        bredde = rd.randint(50, 150)
        hoyde = 20
        x = rd.randint(0, VINDU_BREDDE - bredde)
        y = rd.randint(50, VINDU_HOYDE - hoyde)
        platforms.append(Platform(x,y,bredde,hoyde))
        
        
        

    
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
        #slutter programmet
        running = False
        
                 
    #Tegner Gull
    for gull in gull_liste:
        gull.tegn(vindu)

    
    # Tegner poeng
    Poeng = tekst.render(f"Poeng: {spiller.coins}", True, (255, 255, 255))
    vindu.blit(Poeng, (20, 20))

    pg.display.flip()
    clock.tick(FPS)

pg.quit()
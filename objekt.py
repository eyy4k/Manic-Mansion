import pygame as pg
import random as rd
from typing import List
from constants import *

class Platform: 
    def __init__(self, x: int, y: int, bredde: int, hoyde: int, farge: tuple[int, int, int] =(100, 100, 255) ):
        self.bredde = bredde
        self.hoyde = hoyde
        self.farge = farge
        self.rect = pg.Rect(x,y,bredde, hoyde)
        
    def tegn(self, vindu: pg.Surface):
        pg.draw.rect(vindu, self.farge, self.rect)          

class Spøkelse:
    def __init__(self, x: int, y: int):
        self.image = pg.image.load("bilder/spøkelse.png").convert_alpha()
        self.image = pg.transform.scale(
            self.image,
            (75, 75)
    
        )
        self.rect = self.image.get_rect(topleft=(x, y))
        self.flytt_timer = 0
        self.vy = rd.choice([-2, 0, 2])
        self.vx = rd.choice([-2, 0, 2])

    def flytt(self, platforms: List[Platform]):
        
        self.flytt_timer += 1 
        
        if self.flytt_timer > 60:
            self.vy = rd.choice([-2, 0, 2])
            self.vx = rd.choice([-2, 0, 2])
            self.flytt_timer = 0
        
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        if self.rect.left <= VINDU_BREDDE // 3:
            self.rect.left = VINDU_BREDDE // 3
            self.vx *= -1
        
        elif self.rect.right >= (VINDU_BREDDE // 3) * 2:
           self.rect.right = (VINDU_BREDDE // 3) * 2
           self.vx *= -1
            
        if self.rect.top <= 0:
            self.rect.top = 0
            self.vy*= -1 
        elif self.rect.bottom >= VINDU_HOYDE:
            self.rect.bottom = VINDU_HOYDE
            self.vy*= -1 
            
        #kollisjon platformer
        for p in platforms: 
            if self.rect.colliderect(p.rect):
                if self.vy > 0 and self.rect.bottom > p.rect.top: #faller på platfom
                    self.rect.bottom = p.rect.top
                    self.vy *= -1
                elif self.vy < 0 and self.rect.top < p.rect.bottom: #kollisjon underifra
                    self.rect.top = p.rect.bottom
                    self.vy *= -1
                    
                if self.vx > 0 and self.rect.right > p.rect.left: #venstre
                    self.rect.right = p.rect.left
                    self.vx *= -1
                elif self.vx < 0 and self.rect.left < p.rect.right: #høyre
                    self.rect.left = p.rect.right
                    self.vx *= -1
            
        
    def tegn(self, vindu: pg.Surface):
        vindu.blit(self.image, self.rect)




class Spiller: 
    def __init__(self, x: int, y: int):
        self.image = pg.image.load("bilder/pacman.png").convert_alpha()
        self.image = pg.transform.scale(self.image,
            (75, 75)
    
        )
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.coins = 0
        self.speed = 4
    def flytt(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed
        if keys[pg.K_s]:
            self.rect.y += self.speed
        if keys[pg.K_a]:
            self.rect.x -= self.speed
        if keys[pg.K_d]:
            self.rect.x += self.speed

    def kolisjon(self, x: int, y: int):
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, x)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, y)

    def tegnspiller(self, vindu: pg.Surface):
        vindu.blit(self.image, self.rect)


class Gullmynter:
    def __init__(self, x: int, y: int):
        self.image = pg.image.load("bilder/gull.png").convert_alpha()
        self.image = pg.transform.scale(self.image,
            (50, 50)
    
        )
        self.rect = self.image.get_rect(topleft=(x, y))


    def tegn(self, vindu: pg.Surface):
        vindu.blit(self.image, self.rect)
    
        

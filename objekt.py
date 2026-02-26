import pygame as pg
import random as rd
from constants import *


class Spøkelse:
    def __init__(self, x: int, y: int):
        self.image = pg.image.load("bilder/spøkelse.png").convert_alpha()
        self.image = pg.transform.scale(
            self.image,
            (75, 75)
    
        )
        self.rect = self.image.get_rect(topleft=(x, y))

    def flytt(self):
        
        if rd.randint(1,100) > 30:
            self.rect.x += 1 
        elif rd.randint(1,100) > 30:
            self.rect.y += 1 
        elif rd.randint(1, 100) > 40:
            self.rect.x -= 1 
        elif rd.randint(1, 100) < 20:
            self.rect.y -=1 
         
        
  
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
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed
        if keys[pg.K_s]:
            self.rect.y += self.speed
        if keys[pg.K_a]:
            self.rect.x -= self.speed
        if keys[pg.K_d]:
            self.rect.x += self.speed

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
    
        
        





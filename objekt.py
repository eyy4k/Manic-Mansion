import pygame as pg
from constants import *


class Spøkelse:
    def __init__(self, x: int, y: int):
        self.image = pg.image.load("spøkelse.png").convert_alpha()
        self.image = pg.transform.scale(
            self.image,
            (75, 75)
    
        )
        self.rect = self.image.get_rect(topleft=(x, y))

  
    def tegn(self, vindu: pg.Surface):
        vindu.blit(self.image, self.rect)







class Spiller: 
    def __init__(self, x: int, y: int):
        self.image = pg.image.load("pacman.png").convert_alpha()
        self.image = pg.transform.scale(self.image,
            (75, 75)
    
        )
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

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

    def draw(self, vindu: pg.Surface):
        vindu.blit(self.image, self.rect)
        






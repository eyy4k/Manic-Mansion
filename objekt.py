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
        self.retning = rd.choice(['venstre', 'opp', 'ned', 'hoyre'])
        self.flytt_timer = 0

    def flytt(self):
        vx = 2
        vy = 2 
        self.flytt_timer += 1 
        
        if self.flytt_timer > 60:
            self.retning = rd.choice(['venstre', 'opp', 'ned', 'hoyre'])
        
        if self.retning == 'venstre':
            self.rect.x -= vx
        if self.retning == 'hoyre':
            self.rect.x += vx
        if self.retning == 'ned':
            self.rect.y += vy
        if self.retning == 'opp':
            self.rect.y += vy
        
        #TODO
        #Kollisjon mellom VINDU_BREDDE 
        
        if self.rect.left <= VINDU_BREDDE // 3 or self.rect.right >= (VINDU_BREDDE // 3) * 2:
           vx *= -1
        
        self.rect.x += vx
    
  
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
    
        
        





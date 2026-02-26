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
    def flytt(self, platforms: List[Platform]):
        keys = pg.key.get_pressed()
        dx = dy = 0
        if keys[pg.K_w]:
            dy -= self.speed
        if keys[pg.K_s]:
            dy += self.speed
        if keys[pg.K_a]:
            dx -= self.speed
        if keys[pg.K_d]:
            dx += self.speed
            
        #kollisjon platform
        self.rect.x += dx
        for p in platforms: 
            if self.rect.colliderect(p.rect):
                if dx > 0: 
                    self.rect.right = p.rect.left 
                elif dx < 0:
                    self.rect.left = p.rect.right
                    
        self.rect.y += dy
        for p in platforms: 
            if self.rect.colliderect(p.rect):
                if dy > 0: 
                    self.rect.bottom = p.rect.top
                elif dy < 0:
                    self.rect.top = p.rect.bottom
                   

    def kolisjon(self, x: int, y: int):
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, x)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, y)
    
    def kollisjon_spøkelse(self, spøkelser: List[Spøkelse]):
        for s in spøkelser:
            if self.rect.colliderect(s.rect):
                return True
            return False

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
    
        

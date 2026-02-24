import pygame
import sys

pygame.init()
running = True

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class hus:
    def __init__(self, h_høyde, h_lengde, background_color):
        self.h_høyde = h_høyde
        self.h_lengde = h_lengde
        self.background_color = background_color

    def draw(self, screen):
        screen.fill(self.background_color)

rom = {
    "literom1": hus(100, 150, (50, 50, 100)),
    "stortrom": hus(150, 200, (75, 100, 125))
}

current_room = rom["literom1"]

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_room.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
"""
leeyeunu
2025-03-06
"""
import pygame
import sys

X = 600
Y = 600
pygame.init()
SURFACE = pygame.display.set_mode((X,Y))
FPSCLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 36)
pygame.display.set_caption("pygame 1234")

i = 0
j = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    SURFACE.fill((0,255,255))
    pygame.draw.rect(SURFACE, (255, 255, j), (300, i, 50, 50))
    pygame.draw.ellipse(SURFACE, (j, 0, 255), (i, 500, 50, 50))

    text = FONT.render(f"i: {i}", True, (0, 0, 0))
    SURFACE.blit(text, (30, 30))
    
    j += 5
    if j>254:
        j = 0
    i += 1
    if i > Y:
        i = 0
    
    pygame.display.update()
    FPSCLOCK.tick(30)

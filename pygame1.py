"""
leeyeunu
2025-03-06
"""
import pygame
import sys

X = 600
Y = 400
pygame.init()
SURFACE = pygame.display.set_mode((X,Y))
FPSCLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 36)
pygame.display.set_caption("파이게임 해보기")

i = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    SURFACE.fill((111,111,111))
    pygame.draw.rect(SURFACE, (255, 0, 0), (100, i, 50, 50))
    pygame.draw.ellipse(SURFACE, (0, 0, 255), (i, 100, 50, 50))

    text = FONT.render(f"i: {i}", True, (0, 0, 0))
    SURFACE.blit(text, (30, 30))
    
    i += 1
    if i > Y:
        i = 0
    
    pygame.display.update()
    FPSCLOCK.tick(50)

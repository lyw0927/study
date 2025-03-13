import pygame
import sys
from pygame.locals import Rect
from random import randint

X = 1000
Y = 800

pygame.init()

SURFACE = pygame.display.set_mode((X, Y))

FPSCLOCK = pygame.time.Clock()

SMALLFONT = pygame.font.Font(None, 30)
BIGFONT = pygame.font.Font(None, 100)

pygame.display.set_caption("파이게임 해보기")

def getEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            return "keydown"

        elif event.type == pygame.KEYUP:
            return "keyup"
    return None

def main():
    player = Rect(X/2, Y - 90, 60, 60)
    playerColor = (255, 0, 255)
    
    obstacle = Rect(X / 2 + 60, 0, 60, 500)
    obstacleColor = (255, 0, 0)
    
    plane = Rect(0, Y - 30, X, 30)
    planeColor = (0, 255, 0)

    player.centerx = X / 2
    player.bottom = Y -30
    obstacle.centerx = randint(0, X)
    obstacle.bottom = 0
    counter = 0 
    point = 0

    def update(rendered, pos):
        SURFACE.fill((255, 255, 255))
        pygame.draw.rect(SURFACE, planeColor, plane)
        pygame.draw.rect(SURFACE, obstacleColor, obstacle)
        pygame.draw.rect(SURFACE, playerColor, player)
        SURFACE.blit(rendered, pos)
        pygame.display.update()
        FPSCLOCK.tick(60)

    while True:
        getEvent()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.move_ip(-10, 0)

        if keys[pygame.K_RIGHT] and player.right < X:
            player.move_ip(10, 0)

        obstacle.move_ip(0, counter)
        if obstacle.top > Y:
            point += 1
            obstacle.centerx = randint(0, X)
            obstacle.bottom = 0
            counter = 0
        else:
            counter += 1

        if player.colliderect(obstacle):
            gameOver = BIGFONT.render(f"Game Over: {point}", True, (0, 0, 0))
            titlePos = gameOver.get_rect()
            titlePos.centerx = X/2
            titlePos.centery = Y/2

            while True:
                update(gameOver, titlePos)
                getEvent()

        text = SMALLFONT.render(f"Point: {point}", True, (0, 0, 0))
        update(text, (50, 50))

if __name__ == "__main__":
    main()

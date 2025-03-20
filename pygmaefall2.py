import pygame
import random
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
    return None

def main():
    counter = 0 
    point = 0
    running = True

    while running:
        player = Rect(X/2, Y - 90, 60, 60)
        playerColor = (255, 0, 255)
        obstacle = Rect(randint(0, X - 60), 0, 60, 500)
        obstacleColor = (255, 0, 0)
        plane = Rect(0, Y - 30, X, 30)
        planeColor = (0, 255, 0)

        while True:
            keys = pygame.key.get_pressed()
            getEvent()

            if keys[pygame.K_LEFT] and player.left > 0:
                player.move_ip(-10, 0)
            if keys[pygame.K_RIGHT] and player.right < X:
                player.move_ip(10, 0)

            obstacle.move_ip(0, counter)
            if obstacle.top > Y:
                point += 1
                obstacle.centerx = randint(0, X - 60)
                obstacle.bottom = 0
                counter = random.randrange(1, 5)
            else:
                counter += random.randrange(0, 5)

            if player.colliderect(obstacle):
                gameOver = BIGFONT.render(f"Game Over: {point} - Up to Retry", True, (0, 0, 0))
                titlePos = gameOver.get_rect()
                titlePos.centerx = X / 2
                titlePos.centery = Y / 2

                while True:
                    SURFACE.fill((255, 255, 255))
                    SURFACE.blit(gameOver, titlePos)
                    pygame.display.update()
                    keys = pygame.key.get_pressed()

                    if event.key == pygame.K_r:
                        break
            
            update(player, obstacle, point)

def update(player, obstacle, point):
    SURFACE.fill((255, 255, 255))
    plane = Rect(0, Y - 30, X, 30)
    planeColor = (0, 255, 0)

    pygame.draw.rect(SURFACE, planeColor, plane)
    pygame.draw.rect(SURFACE, (255, 0, 0), obstacle)
    pygame.draw.rect(SURFACE, (255, 0, 255), player)

    text = SMALLFONT.render(f"Point: {point}", True, (0, 0, 0))
    SURFACE.blit(text, (50, 50))

    pygame.display.update()
    FPSCLOCK.tick(60)

if __name__ == "__main__":
    main()

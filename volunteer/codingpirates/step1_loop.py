import pygame
pygame.init()

screen = pygame.display.set_mode((900, 600))
screen.fill((255, 255, 255))
for i in range(200):
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), [100 + i * 5, 100 + i * 5], 50, 0)
    pygame.display.flip()
    pygame.time.wait(20)

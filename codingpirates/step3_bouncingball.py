import pygame
pygame.init()

X = 600
Y = 400

RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Pygame Presentation by Coding Pirates")
screen.fill(RED)

clock = pygame.time.Clock()

x = 100
y = 110
dx = 2
dy = 3
radius = 30

while True:
    clock.tick(70)
    screen.fill(RED)
    pygame.draw.circle(screen, BLUE, [x, y], radius, 0)
    x += dx
    y += dy
    if x > X - radius or x < radius:
        dx = -dx
    if y > Y - radius or y < radius:
        dy = - dy
    pygame.display.flip()

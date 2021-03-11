import pygame, sys
pygame.init()

X = 600
Y = 400

RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Pygame Presentation by Coding Pirates")
screen.fill(RED)

radius = 30
pygame.draw.circle(screen, BLUE, [100, 100], radius, 0)

down = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            down = True
            location = event.pos
            screen.fill(RED)
            pygame.draw.circle(screen, BLUE, location, radius, 0)
        elif event.type == pygame.MOUSEBUTTONUP:
            down = False
        elif event.type == pygame.MOUSEMOTION and down:
            location = event.pos
            screen.fill(RED)
            pygame.draw.circle(screen, BLUE, location, radius, 0)

    pygame.display.flip()

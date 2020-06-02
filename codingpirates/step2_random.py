import pygame, random
pygame.init()

X = 900
Y = 600

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK =(0, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE =(255, 0, 255)
ORANGE = (255, 126, 80)
GREY = (200, 200, 200)

allColors = [RED, BLUE, GREEN, BLACK, CYAN, YELLOW, PURPLE, ORANGE, GREY]

screen = pygame.display.set_mode((X, Y))
screen.fill(WHITE)
for i in range(200):
    x_pos = random.randint(1, X)
    y_pos = random.randint(1, Y)
    color = random.choice(allColors)
    pygame.draw.circle(screen, color, [x_pos, y_pos], 50, 0)
    pygame.display.flip()

import pygame, sys, random
pygame.init()

X = 600
Y = 400

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

allColors = [BLUE, GREEN, PURPLE, CYAN] # list of ball colors
color_index = 0
color = BLUE

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Pygame Presentation by Coding Pirates")
screen.fill(RED)

clock = pygame.time.Clock()

# ball data
x = 400
y = 110
dx = -2
dy = 3
radius = 30
lives = 3

# bat data
bat_x = 10
bat_y = 60
bat_pos = 0

up = False
down = False

line_pos = X - 50

while True:
    # event handling
    clock.tick(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
            elif event.key == pygame.K_DOWN:
                down = True
        elif event.type == pygame.KEYUP:
            up = False
            down = False

    # drawing            
    screen.fill(RED)
    pygame.draw.rect(screen, YELLOW, [line_pos, bat_pos, bat_x, bat_y], 0)
    pygame.draw.line(screen, BLACK, (line_pos, 0), (line_pos, Y), 1)
    pygame.draw.circle(screen, color, [x, y], radius, 0)

    # move bat
    if down and bat_pos < Y - bat_y:
        bat_pos += 5
    if up and bat_pos > 0:
        bat_pos -= 5

    # move ball
    x += dx
    y += dy
    if x < radius:
        dx = -dx
    if y > Y - radius or y < radius:
        dy = - dy
    if line_pos + 5 - radius > x > line_pos - radius and bat_pos < y < bat_pos + bat_y:
        dx = -dx

    # create new ball
    if x > X+radius+5:
        if lives > 1:
            lives -= 1
            pygame.time.wait(1000)
            x = random.randint(100, 400)
            y = random.randint(50, 350)
            dx = random.choice([-2, -3])
            dy = random.randint(2, 6)
            color_index += 1
            color = allColors[color_index]

    pygame.display.flip()

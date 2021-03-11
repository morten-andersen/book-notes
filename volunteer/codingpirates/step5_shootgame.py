import pygame, sys
pygame.init()

X = 1200
Y = 800

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
# pygame.key.set_repeat(100, 30)
screen.fill(RED)

clock = pygame.time.Clock()

# ball data
x = 100
y = 110
dx = 2
dy = 3
radius = 60
left = False
right = False

shooter_x = X//2
shoot = False # no shot fired

while True:
    # event handling
    clock.tick(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and shoot == False:
            shoot = True # shot fired and active
            shoot_y = Y - 180
            shoot_x = shooter_x
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            left = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            right = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            left = False
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            right = False

    if left and shooter_x > 60:
        shooter_x -= 5
    elif right and shooter_x < X-60:
        shooter_x += 5         
        
##    keys = pygame.key.get_pressed() # handles keys constantly pressed (left and right arrow)
##    if keys[pygame.K_LEFT] and shooter_x > 30:
##        shooter_x -= 5
##    elif keys[pygame.K_RIGHT] and shooter_x < X-30:
##        shooter_x += 5

    # drawing            
    screen.fill(RED)
    pygame.draw.polygon(screen, YELLOW, ((shooter_x, Y-140), (shooter_x - 60, Y-20), (shooter_x + 60, Y-20)), 0)
    pygame.draw.line(screen, BLACK, (0, Y-160), (X, Y-160), 1)
    pygame.draw.circle(screen, color, [x, y], radius, 0)

    # shot handling
    if shoot:
        pygame.draw.circle(screen, BLACK, [shoot_x, shoot_y], 5, 0)
        shoot_y -= 5                            # move shot up on screen
        dist = (shoot_x - x)**2 + (shoot_y - y)**2
        if dist < (radius + 5)**2:              # check for collision
            shoot_y = -10                       # prepare to kill the shot
            color_index += 1                    # pick next color-index
            if color_index == len(allColors):   # check for last color in list
                color_index = 0
            color = allColors[color_index]      # pick color

        if shoot_y < -5:                        # kill the shot
            shoot = False                       # allow nex shot

    # move ball
    x += dx
    y += dy
    if x > X - radius or x < radius:
        dx = -dx
    if y > Y - 160 - radius or y < radius:
        dy = - dy

    pygame.display.flip()

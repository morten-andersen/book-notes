import pygame, sys, random
pygame.init()

X = 900
Y = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
TANK_COLUMNS = 5
COLUMNS_SPACING = Y / (TANK_COLUMNS + 2)
MAX_SPEED = 5

screen = pygame.display.set_mode((X, Y))
font = pygame.font.SysFont("comic sans ms", 30, True, True)
font_large = pygame.font.SysFont("comic sans ms", 60, True, True)
tank_hits = 0
lives = 5

# load background image
background = pygame.transform.scale(pygame.image.load('images/background.jpg').convert(), [X, Y])

# load tank image
tank_img = pygame.image.load('images/tank.png').convert_alpha()
tank = { 'x': 100, 'y': Y / 2, 'img': tank_img }
lives_img = pygame.image.load('images/tank_lives.png').convert_alpha()

# load other tank images
enemy_tanks_img= []
for i in range(1, 4):
    enemy_tanks_img.append(pygame.image.load('images/enemy_tank' + str(i) + '.png').convert_alpha())

# a dictionary with a tank for each column
enemy_tanks_columns = []
for i in range(TANK_COLUMNS):
    enemy_tanks_columns.append( {'x': X, 'y': i * COLUMNS_SPACING + COLUMNS_SPACING, 'dx': -random.randint(1, MAX_SPEED), 'img': enemy_tanks_img[random.randint(0, len(enemy_tanks_img) - 1)]})

while True:
    pygame.time.wait(20)
    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # tank movement
            if event.key == pygame.K_UP and tank['y'] > 0:
                tank['y'] -= COLUMNS_SPACING
            elif event.key == pygame.K_DOWN and tank['y'] < (Y - COLUMNS_SPACING):
                tank['y'] += COLUMNS_SPACING
        
    screen.blit(background, [0, 0])
    screen.blit(font.render('Hits: ' + str(tank_hits), True, RED), [X - 200, 20])
    for i in range(lives):
        screen.blit(lives_img, [i * 50 + 20, 25])

    # draw tank
    screen.blit(tank['img'], [tank['x'], tank['y']])

    # draw the rolling enemies
    for i in range(TANK_COLUMNS):
        tank_column = enemy_tanks_columns[i]
        screen.blit(tank_column['img'], [tank_column['x'], tank_column['y']])
        tank_column['x'] += tank_column['dx']

        # check if tank has hit the left edge
        if tank_column['x'] < 0:
            tank_column['x'] = X
            tank_column['dx'] = -random.randint(1, MAX_SPEED)
            tank_column['img'] = enemy_tanks_img[random.randint(0, len(enemy_tanks_img) - 1)]

    if lives <= 0:
        break

    # collision detection

    pygame.display.flip()


import pygame, sys, random
pygame.init()

X = 900
Y = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BALL_COLUMNS = 10
COLUMNS_SPACING = X / (BALL_COLUMNS + 2)
MAX_SPEED = 5

screen = pygame.display.set_mode((X, Y))
font = pygame.font.SysFont("comic sans ms", 30, True, True)
font_large = pygame.font.SysFont("comic sans ms", 60, True, True)
presents = 0
lives = 5

class Snow():
        def __init__(self):
            self.yPos = 1
            self.xPos = random.randint(2, X-2)
    
        def fall(self):
            self.yPos += 2
    
        def draw(self):
            pygame.draw.circle(screen, WHITE, (self.xPos, self.yPos), 3, 0)

# load background image
background = pygame.transform.scale(pygame.image.load('images/background.jpeg').convert(), [X, Y])

# load santa image
santa_img_left = pygame.image.load('images/santa.png').convert_alpha()
santa_img_right = pygame.transform.flip(santa_img_left, True, False)
santa = { 'x': X / 2, 'y': Y - 100, 'img': santa_img_left }
lives_img = pygame.image.load('images/santa_lives.png').convert_alpha()

# load present image
present_img = pygame.image.load('images/present.png').convert_alpha()

# load ball images
balls = []
for i in range(1, 10):
    balls.append(pygame.image.load('images/ball' + str(i) + '.png').convert_alpha())

# a dictionary with a ball for each column
ball_columns = []
for i in range(BALL_COLUMNS):
    ball_columns.append( {'x': i * COLUMNS_SPACING + COLUMNS_SPACING, 'y': 0, 'dy': random.randint(1, MAX_SPEED), 'ball': balls[random.randint(0, len(balls) - 1)], 'present': False })

# load and play music
pygame.mixer.music.load('sound/jinglebells.ogg')
pygame.mixer.music.play(-1)

# load breaking glass sound
collision_sound = pygame.mixer.Sound('sound/glass.ogg')

# load present sound
present_sound = pygame.mixer.Sound('sound/present.ogg')

allSnow = []

while True:
    pygame.time.wait(20)
    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # santa movement
            if event.key == pygame.K_LEFT and santa['x'] > 0:
                santa['x'] -= COLUMNS_SPACING
                santa['img'] = santa_img_left
            elif event.key == pygame.K_RIGHT and santa['x'] < (X - COLUMNS_SPACING):
                santa['x'] += COLUMNS_SPACING
                santa['img'] = santa_img_right
        
    screen.blit(background, [0, 0])
    screen.blit(font.render('Presents: ' + str(presents), True, RED), [X - 220, 20])
    for i in range(lives):
        screen.blit(lives_img, [i * 30 + 20, 20])

    allSnow.append(Snow())
    for s in allSnow:
        s.fall()
        s.draw()
        if s.yPos > Y:
            allSnow.remove(s)

    # draw santa
    screen.blit(santa['img'], [santa['x'], santa['y']])

    # draw the falling xmas balls
    for i in range(BALL_COLUMNS):
        ball_column = ball_columns[i]
        screen.blit(ball_column['ball'], [ball_column['x'], ball_column['y']])
        ball_column['y'] += ball_column['dy']
        # random flip horisontally on 10% of the cases
        if random.random() < 0.1:
            ball_column['ball'] = pygame.transform.flip(ball_column['ball'], True, False)

        # check if ball has hit the lower edge
        if ball_column['y'] > Y - 100:
            ball_column['y'] = 0
            ball_column['dy'] = random.randint(1, MAX_SPEED)
            # every 15% is a present
            if random.random() < 0.15:
                ball_column['ball'] = present_img
                ball_column['present'] = True
            else:
                ball_column['ball'] = balls[random.randint(0, len(balls) - 1)]
                ball_column['present'] = False

    if lives <= 0:
        break

    # collision detection
    for i in range(BALL_COLUMNS):
        ball_column = ball_columns[i]
        if ball_column['ball'].get_rect(left=ball_column['x'], top=ball_column['y']).colliderect(santa['img'].get_rect(left=santa['x'], top=santa['y'])):
            if ball_column['present']:
                present_sound.play()
                presents += 1
                if presents % 10 == 0:
                    lives += 1
            else:
                collision_sound.play()
                lives -= 1
            ball_column['y'] = 0
            ball_column['dy'] = random.randint(1, MAX_SPEED)
            # every 15% is a present
            if random.random() < 0.15:
                ball_column['ball'] = present_img
                ball_column['present'] = True
            else:
                ball_column['ball'] = balls[random.randint(0, len(balls) - 1)]
                ball_column['present'] = False

    pygame.display.flip()

# game over
screen.blit(font_large.render('Game Over', True, RED), [X / 2 - 180, Y / 2 - 60])
pygame.display.flip()
pygame.mixer.music.stop()
while True:
    pygame.time.wait(20)
    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

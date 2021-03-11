import pygame, sys, random
pygame.init()

X = 600
Y = 400

RED = (255, 0, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Pygame Presentation by Coding Pirates")
screen.fill(RED)

clock = pygame.time.Clock()

ball1 = { 'color': BLUE, 'x': random.randint(100, 500),
          'y': random.randint(100, 300),
          'dx': random.randint(-3, 3), 'dy': random.randint(-3, 3),
          'radius': random.randint(20, 40) }
ball2 = { 'color': GREEN, 'x': random.randint(100, 500),
          'y': random.randint(100, 300),
          'dx': random.randint(-3, 3), 'dy': random.randint(-3, 3),
          'radius': random.randint(20, 40) }

def drawBall(ball):
    pygame.draw.circle(screen, ball['color'],
                       [ball['x'], ball['y']], ball['radius'], 0)
    ball['x'] += ball['dx']
    ball['y'] += ball['dy']
    if ball['x'] > X - ball['radius'] or ball['x'] < ball['radius']:
        ball['dx'] = -ball['dx']
    if ball['y'] > Y - ball['radius'] or ball['y'] < ball['radius']:
        ball['dy'] = -ball['dy']

def collision(ball1, ball2):
    a = ball1['x'] - ball2['x']
    b = ball1['y'] - ball2['y']
    c = ball1['radius'] + ball2['radius']
    if (a**2 + b**2) < c**2:
        # collision
        ball1['dx'] = -ball1['dx']
        ball1['dy'] = -ball1['dy']
        ball2['dx'] = -ball2['dx']
        ball2['dy'] = -ball2['dy']

while True:
    clock.tick(70)
    screen.fill(RED)
    collision(ball1, ball2)
    drawBall(ball1)
    drawBall(ball2)
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

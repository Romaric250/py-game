import pygame


pygame.init()
screen = pygame.display.set_mode((1250,750))
clock = pygame.time.Clock()
running = True 
dt = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('purple')

    pygame.display.flip()
    clock.tick(60)
pygame.quit
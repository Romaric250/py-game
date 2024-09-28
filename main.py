import pygame


pygame.init()
screen = pygame.display.set_mode((750,500))
clock = pygame.time.Clock()
running = True 
dt = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('purple')

    pygame.draw.circle(screen, 'pink',(100,500),30)





    pygame.display.flip()
    clock.tick(60)
pygame.quit
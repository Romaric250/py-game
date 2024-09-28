import pygame


pygame.init()
screen = pygame.display.set_mode((750,500))
clock = pygame.time.Clock()
running = True 
dt = 0


position_item = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('purple')

    pygame.draw.circle(screen, 'pink',position_item,30)
    pygame.draw.aaline(screen,'red',(screen.get_width()/2,0), (screen.get_width(),screen.get_height()/2))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_m]:
        position_item.y -= 5
    if keys[pygame.K_s]:
        position_item.y +=5
    if keys[pygame.K_a]:
        position_item.x -=5
    if keys[pygame.K_d]:
        position_item.x += 5
    if keys[pygame.K_DELETE]:
        pygame.quit()





    pygame.display.flip()
    clock.tick(60)
pygame.quit()
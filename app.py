import pygame
from pygame import *

pygame.init()
screen = pygame.display.set_mode((750,500))


clock = time.Clock()
running = True 
dt = 0
position_item = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('brown')

    pygame.draw.circle(screen, 'gray',position_item,30)
    pygame.draw.line(screen,'white', (750,500),(round(screen.get_width()/2), round(screen.get_height()/2)))
  
    print(screen.get_height())
    pygame.draw.aaline(screen,'red',(screen.get_height()/2,screen.get_width()/2,), (screen.get_width(),screen.get_height()/2))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if position_item.y == round(screen.get_width()/2):
             continue
        position_item.y -= 1
        

    if keys[pygame.K_s]:
        if position_item.y >=500:
            continue
        position_item.y +=5
    if keys[pygame.K_a]:
        if position_item.x >=1000:
            continue
        position_item.x -=5
    if keys[pygame.K_d]:
        if position_item.x >=1000:
                    continue
        position_item.x += 5
        
        
    if keys[pygame.K_DELETE]:
        pygame.quit()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
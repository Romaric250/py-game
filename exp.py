import pygame 
from pygame import *

pygame.init()
screen = pygame.display.set_mode((500,650))


clock = time.Clock()
isrunning = True 

dt = 0


position= pygame.Vector2(screen.get_width()/2,screen.get_height()/2)

while isrunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrunning = False
        screen.fill('pink')

pygame.display.flip()

from pygame import *
import random


def StartGame():
    return True

def RandomiseFoodLocation(screenwidth,screenheight)->tuple:
    if type(screenheight) != 'Int' or 'Float' and type(screenwidth) != 'Int' or 'Float':
        return tuple(0,0)

    return tuple(random.randint(20,screenwidth-20),random.randint(20,screenheight-20))

def SetBoundariesforEater(screenwidth,screenheight)->bool:
    
    if screenheight <=20 and screenwidth<=20 or screenheight <=20 and screenwidth >= screenwidth - 20 or screenheight >= screenheight - 20 and screenwidth <=20 or screenheight >= screenheight-20 and screenwidth >= screenwidth-20:
        return True 
    else:
        return False
        
    




init()

screen1 = display.set_mode((600,600))
clockin = time.Clock()
isrunning = True

initialposition = Vector2(screen1.get_width()/2,screen1.get_height()/2)

while isrunning:
    for events in event.get():
        if events.type == QUIT:
            isrunning = False
    screen1.fill('gray')

    draw.circle(screen1,'red',initialposition,20)

    keys = key.get_pressed()

    

    if keys[K_s]:
       
       IsEaterOutOfRange = SetBoundariesforEater(initialposition.x,initialposition.y)
       print(initialposition)
       if IsEaterOutOfRange:
           initialposition.y += 2
    
    if keys[K_w]:
       
       IsEaterOutOfRange = SetBoundariesforEater(initialposition.x,initialposition.y)
       print(initialposition)
       if IsEaterOutOfRange:
           initialposition.y -= 2
    
    if keys[K_w]:
       
       IsEaterOutOfRange = SetBoundariesforEater(initialposition.x,initialposition.y)
       print(initialposition)
       if IsEaterOutOfRange:
           initialposition.y -= 2

    if keys[K_d]:
       IsEaterOutOfRange = SetBoundariesforEater(initialposition.x,initialposition.y)
       print(initialposition)
       
       if IsEaterOutOfRange:
           
        initialposition.x += 2

    if keys[K_a]:
       IsEaterOutOfRange = SetBoundariesforEater(initialposition.x,initialposition.y)
       print(initialposition)
       
       if IsEaterOutOfRange:
           
        initialposition.x -= 2



           
           











    display.flip()
    clockin.tick(60)

quit()


from pygame import *
import random



newtuple = (3,4)
oldtuple = (3,4)

print(newtuple == oldtuple)

def StartGame():
    return True

def RandomiseFoodLocation(screenwidth,screenheight):

    return {random.randint(20,screenwidth.__floor__()-20),random.randint(20,screenheight.__floor__()-20)}
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

   

    for i in range(1,200):
        draw.line(screen1,'yellow',(40*i,i),(i,40*i))

    for j in range(2,100):
        draw.line(screen1,'black',(20*j,j),(j,20*j))

    draw.circle(screen1,'red',initialposition,20)

    draw.circle(screen1,'green',(200,200),10)


    keys = key.get_pressed()

    
    if key[any]:
        print('Any key was pressed')

    if keys[K_s]:
       
       IsEaterOutOfRange = SetBoundariesforEater(initialposition.x,initialposition.y)
       print(initialposition)
       if initialposition.y >= 580:
           continue
       else:
            
            initialposition.y += 4
    
    if keys[K_w]:
       
       IsEaterOutOfRange = SetBoundariesforEater(initialposition.x,initialposition.y)
       print(initialposition)
       if initialposition.x <= 300 and initialposition.y <= 20:
           continue
       else:
          if initialposition.y == 200 and initialposition.x == 200:
              continue
          else:
              
            initialposition.y -= 4
    
   
    if keys[K_d]:
       IsEaterOutOfRange = SetBoundariesforEater(initialposition.x,initialposition.y)
       print(initialposition)
       print(initialposition)
       if initialposition.x >= 580:
           continue
       else:
          initialposition.x += 4

          x= RandomiseFoodLocation(initialposition.x,initialposition.y)
          print(x)
          
        

    if keys[K_a]:
       IsEaterOutOfRange = SetBoundariesforEater(initialposition.x,initialposition.y)
       print(initialposition)
      

      
       if initialposition.x <=20:
           continue
       else:
          initialposition.x -= 4
    display.flip()
    clockin.tick(60)

quit()


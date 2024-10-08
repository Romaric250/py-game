from pygame import *
import random
import time as Time


newtuple = (4,4)
oldtuple = (3,4)





def StartGame():
    return True

def RandomiseFoodLocation(screenwidth,screenheight):

    return Vector2(random.randint(20,screenwidth.__floor__()-20),random.randint(20,screenheight.__floor__()-20))
def SetBoundariesforEater(screenwidth,screenheight)->bool:
    
    if screenheight <=20 and screenwidth<=20 or screenheight <=20 and screenwidth >= screenwidth - 20 or screenheight >= screenheight - 20 and screenwidth <=20 or screenheight >= screenheight-20 and screenwidth >= screenwidth-20:
        return True 
    else:
        return False

def Collision():
    pass
init()

screen1 = display.set_mode((600,600))
clockin = time.Clock()
isrunning = True

users_score = 0
fonts = font.SysFont('arial',70)



initialposition = Vector2(screen1.get_width()/2,screen1.get_height()/2)
initialfood = Vector2(screen1.get_width()/3,screen1.get_height()/3)

start_game_timer = Time.time()

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

    food = draw.circle(screen1,'pink',initialfood,10)
    food1 = draw.circle(screen1,'green',(400,200),10)
    


    keys = key.get_pressed()

    
    for ke in keys:
        if ke:
            print("any key has been pressed")

            iswidth_small = abs(initialfood.x - initialposition.x)

            isheight_small = abs(initialfood.y - initialposition.y)

            print({
                'width_to_colide':iswidth_small,
                'heigth_to_colide':isheight_small
            })

            if iswidth_small <= 8 and isheight_small <= 8:
                print('colision occured')

                newfood = RandomiseFoodLocation(screen1.get_width(),screen1.get_height())
                initialfood = newfood
                users_score = users_score+1
                
                
            print({
                'userscore_here':users_score,
                

            })
    
    
    if keys[K_s]:
       
       IsEaterOutOfRange = SetBoundariesforEater(initialposition.x,initialposition.y)
       print({
        'eater':initialposition,
        'food':initialfood
       })
       if initialposition.y >= 580:
           continue
       else:
            
            initialposition.y += 4
            # Time.sleep(2)
    
    if keys[K_w]:
       IsEaterOutOfRange = SetBoundariesforEater(initialposition.x,initialposition.y)
       print({
        'eater':initialposition,
        'food':initialfood
       })
       if initialposition.x <= 300 and initialposition.y <= 20:
           continue
       else:
          if initialposition.y == 200 and initialposition.x == 200:
              continue
          else:
              
            initialposition.y -= 4
            # Time.sleep(2)
            
    
   
    if keys[K_d]:
       IsEaterOutOfRange = SetBoundariesforEater(initialposition.x,initialposition.y)
       print({
        'eater':initialposition,
        'food':initialfood
       })
       if initialposition.x >= 580:
           continue
       else:
          initialposition.x += 4

          x= RandomiseFoodLocation(initialposition.x,initialposition.y)
          print(x)
          
        

    if keys[K_a]:
       IsEaterOutOfRange = SetBoundariesforEater(initialposition.x,initialposition.y)
       print({
        'eater':initialposition,
        'food':initialfood
       })
      

      
       if initialposition.x <=20:
           continue
       else:
          initialposition.x -= 4

    text = fonts.render(f'Score:{users_score}',True,(0,0,255))
    screen1.blit(text,(0,500))

    timercounter = fonts.render(f'Time:{abs(start_game_timer-Time.time())}',True,(0,0,255))
    screen1.blit(timercounter,(300,500))
    display.flip()
    clockin.tick(30)

quit()

end_game = Time.time()

print({
    'score':users_score,
    'time taken': f'{round(end_game-start_game_timer)}s'
})


# def User_data(userinfor:list[{
#     "name":"John doe",
#     "email":"email here"
# }]):
#     return {
#         "username":"username-here",
#         "scores":['score1','score2','score3','score4']
#     }
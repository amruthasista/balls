import pygame
import random #import random to use randint and ect.

#initialize pygame
pygame.init()

#screen setup
WIDTH,HEIGHT=600,600 #set the size
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #display to screen
pygame.display.set_caption('Catch the falling ball') #.set_caption makes the title

#colours
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)

#fonts
font=pygame.font.SysFont(None,36) #to set the font and font size

#game variables
basket=pygame.Rect(WIDTH//2-50,HEIGHT-30,100,20) #make rectangles/squares
ball=pygame.Rect(random.randint(0,WIDTH-20),0,20,20)
basket_speed=10 #speed of the basket
ball_speed=5 #speed of the ball
score=0 #your scores starting point
lives=3 #your lives starting point

#game loop control
running=True
clock=pygame.time.Clock()

#game loop
while running:
    screen.fill(WHITE) #colour of the screen

    #functions
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]: #this is the left key to move the basket left
        basket.x-=basket_speed

    if keys[pygame.K_RIGHT]: #this is the right key to move the basket
        basket.x+=basket_speed  

    if basket.left<0:
        basket.left=0

    if basket.right>WIDTH:
        basket.right=WIDTH

    ball.y+=ball_speed

    if ball.colliderect(basket): #.colliderect is the function the makes rectangles/squares collide
        score+=1 #the make score go up by 1
        ball.x=random.randint(0,WIDTH-20) #randint means random integer
        ball.y=0

    if ball.top>HEIGHT:
        lives-=1 # this will take 1 live away if the ball hits the bottom of the screen
        ball.x=random.randint(0,WIDTH-20)
        ball.y=0   

    if lives==0: #once lives = 0
        running=False #it will quit and will close the screen

    #draw objects
    pygame.draw.rect(screen,BLACK,basket) #draws the rectagle/square
    pygame.draw.ellipse(screen,RED,ball) #draw the circle/ball

    score_text=font.render('Score:'+str(score),True,BLACK) #.render prints stuff
    lives_text=font.render('Lives:'+str(lives),True,BLACK)

    screen.blit(score_text,(10,10)) #overlaps rectangles/squares
    screen.blit(lives_text,(480,10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit() #closes the screen
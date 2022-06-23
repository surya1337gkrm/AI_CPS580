import pygame as pg
import os


pg.init()
SCOREFONT=pg.font.SysFont('calibri bold',40)
score=0

#as a convention, we use capitalised variables to denote constant values 
WIDTH,HEIGHT=900,500 #set the height & width
BORDER=pg.Rect(WIDTH/2-5,0,10,HEIGHT)
WIN=pg.display.set_mode((WIDTH,HEIGHT)) #create a window/surface object

WHITE=(255,255,255)
BLACK=(0,0,0)
FPS=60
SPACESHIP_WIDTH,SPACESHIP_HEIGHT=35,40
VEL=5

pg.display.set_caption('Intro to PYGAME')

icon=pg.image.load(os.path.join('Assets','Icon.png'))
pg.display.set_icon(icon)

SPACESHIP_YELLOW=pg.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOWSHIP=pg.transform.scale(SPACESHIP_YELLOW,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
# YELLOWSHIP=pg.transform.rotate(pg.transform.scale(SPACESHIP_YELLOW,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
SPACESHIP_RED=pg.image.load(os.path.join('Assets','spaceship_red.png'))
REDSHIP=pg.transform.rotate(pg.transform.scale(SPACESHIP_RED,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
SPACE=pg.transform.scale(pg.image.load(os.path.join('Assets','space.jpg')),(WIDTH,HEIGHT))



#game-window 
def drawWindow(p1,p2=None):

    WIN.fill(WHITE)  #fill the window with white color
   
    WIN.blit(SPACE,(0,0))
    # pg.draw.rect(WIN,BLACK,BORDER)
    scoreText=SCOREFONT.render('SCORE : '+str(score),1,WHITE)
    pg.draw.rect(WIN,(200,111,212),pg.Rect(795,5,100,30))
    buttonText=SCOREFONT.render('RESET',1,WHITE)
    WIN.blit(scoreText,(10,10))
    WIN.blit(buttonText,(800,10))
    
    WIN.blit(YELLOWSHIP,(p1.x,p1.y))
    # WIN.blit(REDSHIP,(p2.x,p2.y))
    pg.display.update()   #update the window   


def handleKeyPressYellow(keyspressed,yellow):
   
    if keyspressed[pg.K_a] and yellow.x-VEL>0: #left
        yellow.x-=VEL
    if keyspressed[pg.K_d]: #right
        yellow.x+=VEL
    if keyspressed[pg.K_w]: #up
        yellow.y-=VEL
    if keyspressed[pg.K_s]: #down
        yellow.y+=VEL

    if keyspressed[pg.K_i]: #down
        global score
        score+=1     

# def handleKeyPressRed(keyspressed,red):
    
#     if keyspressed[pg.K_LEFT]: #left
#         red.x-=VEL
#     if keyspressed[pg.K_RIGHT]: #right
#         red.x+=VEL
#     if keyspressed[pg.K_UP]: #up
#         red.y-=VEL
#     if keyspressed[pg.K_DOWN]: #down
#         red.y+=VEL            


def main():
    #define positions of the ships using pygame.Rect
    #boundaries of the ships
    
    yellow=pg.Rect(WIDTH/2,HEIGHT-SPACESHIP_HEIGHT,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red=pg.Rect(700,100,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)


    clock=pg.time.Clock()
    run=True
    while run: #to show the window, we create a inifinte loop
        clock.tick(60) #maintains the framerate to 60fps
        mouse = pg.mouse.get_pos() #stores mouse position
        for event in pg.event.get():
            # print(event)
            if event.type==pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN: 
                print('mouse anywhere')
                print(mouse)
            #if the mouse is clicked on the
            # button the game is terminatedz
                if(mouse[0]>795 and mouse[0]<895 and mouse[1]>5 and mouse[1]<35):
                    print('Button Clicked')

        
        
        keyspressed=pg.key.get_pressed()
        handleKeyPressYellow(keyspressed,yellow)
        # handleKeyPressRed(keyspressed,red)
        drawWindow(yellow,red)

    pg.quit()            

if __name__=='__main__':
    main()    
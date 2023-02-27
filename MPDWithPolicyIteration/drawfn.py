import pygame
pygame.init()
screen = pygame.display.set_mode((1080, 620))
screen.fill(pygame.Color(255, 255, 255))
pygame.display.set_caption("MDP")
from cell import states
east = pygame.image.load('imgs\\east.png').convert_alpha()
south = pygame.image.load('imgs\\south.png').convert_alpha()
west = pygame.image.load('imgs\\west.png').convert_alpha()
north = pygame.image.load('imgs\\north.png').convert_alpha()
checked=pygame.image.load('imgs\\checkbox_checked.png').convert_alpha()
checked=pygame.transform.scale(checked,(20,20))
unchecked=pygame.image.load('imgs\\checkbox_unchecked.png').convert_alpha()
unchecked=pygame.transform.scale(unchecked,(20,20))
radio=pygame.image.load('imgs\\radio_button.png').convert_alpha()
radio=pygame.transform.scale(radio,(20,20))
radioSelect=pygame.image.load('imgs\\radio_select.png').convert_alpha()
radioSelect=pygame.transform.scale(radioSelect,(20,20))


arrows={
    0:east,
    1:south,
    2:west,
    3:north
}


def drawX():
    for x in range(30,391,180):
        pygame.draw.line(screen,pygame.Color(0,0,0),(x,30),(x+180,210),2)
        pygame.draw.line(screen,pygame.Color(0,0,0),(x+180,30),(x,210),2)
        if x!=210:
            pygame.draw.line(screen,pygame.Color(0,0,0),(x,210),(x+180,390),2)
            pygame.draw.line(screen,pygame.Color(0,0,0),(x+180,210),(x,390),2) 
    for x in range(30,571,180):
            pygame.draw.line(screen,pygame.Color(0,0,0),(x,390),(x+180,570),2)
            pygame.draw.line(screen,pygame.Color(0,0,0),(x+180,390),(x,570),2)

def drawPolicy():
    for i in range(0,3):
        for j in range(0,4):
            if ((i==1 and j==1) or (i==0 and j==3) or (i==1 and j==3)):
                continue
            else:
                (x,y)=states[i][j].location
                index=states[i][j].q_values.index(states[i][j].state_value)
                img=arrows[index]
                screen.blit(img,(x*180+47,y*180+47))

def drawPolicy2():
    for i in range(0,3):
        for j in range(0,4):
            if ((i==1 and j==1) or (i==0 and j==3) or (i==1 and j==3)):
                continue
            else:
                (x,y)=states[i][j].location
                index=states[i][j].policy
                img=arrows[index]
                screen.blit(img,(x*180+47,y*180+47))

def drawGrid():
    for x in range(0,5):
        pygame.draw.line(screen,pygame.Color(0,0,0),(x*180+30,30),(x*180+30,570),2)
    for x in range(0,4):
        pygame.draw.line(screen,pygame.Color(0,0,0),(30,x*180+30),(750,x*180+30),2)
    # pygame.draw.line(screen,pygame.Color(0,0,0),(30,30),(570,570),2)

    #Draw Rectangles 
    pygame.draw.rect(screen,pygame.Color(105,105,105),(210,210,180,180),0)
    pygame.draw.rect(screen,pygame.Color(166,241,166),(580,40,160,160),0)
    pygame.draw.rect(screen,pygame.Color(228,108,108),(580,220,160,160),0)

    fnt = pygame.font.SysFont("Bahnschrift", 50)
    text = fnt.render("+1", 1, (0,0,0))
    screen.blit(text, (640,90))

    text2 = fnt.render("-1", 1, (0,0,0))
    screen.blit(text2, (640,270))

    fnt = pygame.font.SysFont("Bahnschrift", 20)
# i,j in for loop : represents i for row, j for column
#location[0]: x co-ordinate,location[1]:y co-ordinate
    for i in range(0,3):
        for j in range(0,4):
            if ((i==1 and j==1) or (i==0 and j==3) or (i==1 and j==3)):
                continue
            else:
                text=fnt.render(str(format((states[i][j].state_value),'.4f')),True,'black')
                screen.blit(text,(states[i][j].location[0]*180+90,states[i][j].location[1]*180+110))
    pygame.display.update()

def drawGridCross():
    for x in range(0,5):
        pygame.draw.line(screen,pygame.Color(0,0,0),(x*180+30,30),(x*180+30,570),2)
    for x in range(0,4):
        pygame.draw.line(screen,pygame.Color(0,0,0),(30,x*180+30),(750,x*180+30),2)
    # pygame.draw.line(screen,pygame.Color(0,0,0),(30,30),(570,570),2)

    #Draw Rectangles 
    pygame.draw.rect(screen,pygame.Color(105,105,105),(210,210,180,180),0)
    pygame.draw.rect(screen,pygame.Color(166,241,166),(580,40,160,160),0)
    pygame.draw.rect(screen,pygame.Color(228,108,108),(580,220,160,160),0)

    fnt = pygame.font.SysFont("Bahnschrift", 50)
    text = fnt.render("+1", 1, (0,0,0))
    screen.blit(text, (640,90))

    text2 = fnt.render("-1", 1, (0,0,0))
    screen.blit(text2, (640,270))

    # drawX()
    for i in range(0,3):
        for j in range(0,4):
            if ((i==1 and j==1) or (i==0 and j==3) or (i==1 and j==3)):
                continue
            else:
                q0=states[i][j].q_values[0]
                q1=states[i][j].q_values[1]
                q2=states[i][j].q_values[2]
                q3=states[i][j].q_values[3]

                fnt = pygame.font.SysFont("Bahnschrift", 20)
                textq0=fnt.render(str(format((q0),'.4f')),True,'black')
                screen.blit(textq0,(states[i][j].location[0]*180+140,states[i][j].location[1]*180+110))

                textq1=fnt.render(str(format((q1),'.4f')),True,'black')
                screen.blit(textq1,(states[i][j].location[0]*180+90,states[i][j].location[1]*180+170))

                textq2=fnt.render(str(format((q2),'.4f')),True,'black')
                screen.blit(textq2,(states[i][j].location[0]*180+40,states[i][j].location[1]*180+110))

                textq3=fnt.render(str(format((q3),'.4f')),True,'black')
                screen.blit(textq3,(states[i][j].location[0]*180+90,states[i][j].location[1]*180+50))
    pygame.display.update()

check1=False
check2=False
radio1=True
radio2=False
def draw():
    if radio1:
        if check1 and check2:
            screen.fill(pygame.Color(255,255,255),pygame.Rect(0,0,750,570))
            drawX()
            drawPolicy()
            drawGridCross()
            
        elif not check1 and check2:
            screen.fill(pygame.Color(255,255,255),pygame.Rect(0,0,750,570))
            drawPolicy()
            drawGrid()
        elif check1 and not check2:
            screen.fill(pygame.Color(255,255,255),pygame.Rect(0,0,750,570))
            drawX()
            drawGridCross()
        else:
            screen.fill(pygame.Color(255,255,255),pygame.Rect(0,0,750,570))
            drawGrid()
    else:
        if check2:
            screen.fill(pygame.Color(255,255,255),pygame.Rect(0,0,750,570))
            screen.blit(unchecked,(820,150))
            screen.blit(unchecked if not check2 else checked, (820,200))
            drawPolicy2()
            drawGrid()
        
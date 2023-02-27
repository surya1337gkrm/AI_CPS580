import pygame
from cell import states
from MDP import onGo,policyIteration

pygame.init()
pygame.font.init()
import drawfn

def main():
    idx=0
    
    fnt = pygame.font.SysFont("Bahnschrift", 25)
    title= fnt.render("MDP Process", 1, (0,0,0))
    drawfn.screen.blit(title, (820,60))

    fnt = pygame.font.SysFont("Bahnschrift", 20)
    title= fnt.render("Show Q-values", 1, (0,0,0))
    drawfn.screen.blit(drawfn.unchecked if not drawfn.check1 else drawfn.checked, (820,150))
    drawfn.screen.blit(title,(850,150))

    
    fnt = pygame.font.SysFont("Bahnschrift", 18)
    title= fnt.render("Show Policy", 1, (0,0,0))
    drawfn.screen.blit(title, (850,200))
    drawfn.screen.blit(drawfn.unchecked,(820,200))

    fnt = pygame.font.SysFont("Bahnschrift", 18)
    title= fnt.render("Value Iteration", 1, (0,0,0))
    drawfn.screen.blit(title, (850,251))
    drawfn.screen.blit(drawfn.radioSelect if drawfn.radio1 else drawfn.radio,(820,250))

    fnt = pygame.font.SysFont("Bahnschrift", 18)
    title= fnt.render("Policy Iteration", 1, (0,0,0))
    drawfn.screen.blit(title, (850,281))
    drawfn.screen.blit(drawfn.radioSelect if drawfn.radio2 else drawfn.radio,(820,280))

    fnt = pygame.font.SysFont("Bahnschrift", 20)
    iterText = fnt.render("Iterations: "+str(idx), 1, (0,0,0))
    drawfn.screen.blit(iterText, (300,580))

    pygame.draw.rect(drawfn.screen, (0,255,0), [850, 350, 75 , 35])
    smallfont = pygame.font.SysFont('Bahnschrift',25) 
    text = smallfont.render('Play' , True , 'black')
    drawfn.screen.blit(text , (865 , 355))

    drawfn.drawGrid()
    
    # pygame.display.update()

    # run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 820<=pos[0]<=840 and 150<=pos[1]<=170:
                    if not drawfn.radio2:
                        drawfn.check1=not drawfn.check1
                        drawfn.screen.blit(drawfn.unchecked if not drawfn.check1 else drawfn.checked, (820,150))
                        drawfn.draw()
                
                if 820<=pos[0]<=840 and 200<=pos[1]<=220:
                    if not drawfn.radio2:
                        drawfn.check2=not drawfn.check2
                        drawfn.screen.blit(drawfn.unchecked if not drawfn.check2 else drawfn.checked, (820,200))
                        drawfn.draw()

                if 820<=pos[0]<=840 and 250<=pos[1]<=270:
                    if drawfn.radio1:
                        pass
                    else:
                        drawfn.radio1=True
                        drawfn.radio2=False
                        drawfn.screen.blit(drawfn.radioSelect if drawfn.radio1 else drawfn.radio,(820,250))
                        drawfn.screen.blit(drawfn.radioSelect if drawfn.radio2 else drawfn.radio,(820,280))
                        drawfn.draw()

                if 820<=pos[0]<=840 and 280<=pos[1]<=300:
                    if drawfn.radio2:
                        pass
                    else:
                        drawfn.radio2=True
                        drawfn.check2=True
                        drawfn.check1=False
                        drawfn.radio1=False
                        drawfn.screen.blit(drawfn.radioSelect if drawfn.radio1 else drawfn.radio,(820,250))
                        drawfn.screen.blit(drawfn.radioSelect if drawfn.radio2 else drawfn.radio,(820,280))
                        drawfn.draw()


                if 850<=pos[0]<=925 and 350<=pos[1]<=385:
                    print('Play')
                    if drawfn.radio1 and not drawfn.radio2:
                        while idx<=100:
                            b=onGo(idx)
                            drawfn.draw()
                            pygame.time.delay(100)
                            idx=idx+1
                            if not b:
                                print("Ideal Policy Obtained.")
                                break
                    else:
                        policyIteration()             
            pygame.display.update()
    pygame.quit()
main()
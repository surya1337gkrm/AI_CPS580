import pygame
from MDP import onGo
import drawfn

pygame.init()
pygame.font.init()

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
                    drawfn.check1=not drawfn.check1
                    drawfn.screen.blit(drawfn.unchecked if not drawfn.check1 else drawfn.checked, (820,150))
                    drawfn.draw()
                
                if 820<=pos[0]<=840 and 200<=pos[1]<=220:
                    drawfn.check2=not drawfn.check2
                    drawfn.screen.blit(drawfn.unchecked if not drawfn.check2 else drawfn.checked, (820,200))
                    drawfn.draw()


                if 850<=pos[0]<=925 and 350<=pos[1]<=385:
                    print('Play')
                    while idx<=100:
                        b=onGo(idx,drawfn.screen)
                        drawfn.draw()
                        pygame.time.delay(100)
                        idx=idx+1
                        if not b:
                            break            
            pygame.display.update()
    pygame.quit()
main()
import random
from cell import states
import pygame

ACTION_EAST=0
ACTION_SOUTH=1
ACTION_WEST=2
ACTION_NORTH=3


TRANSITION_SUCCEED=0.8 #The probability that by taking action A, it moves to the expected destination state S'. Here the state S' represents the new state that the action A aims to move to.
TRANSITION_FAIL=0.2 #The probability that by taking action A, it moves to an unexpected destination state S'. For example, by taking action East, you may moves to the neighboring direction North or South. So the probability of going to North or South is 0.1. We assume the two directions evenly split the value of TRANSITION_FAIL 0.2
GAMMA=0.9 #the discount factor
ACTION_REWARD=-0.1 #The instantaneous for taking each action (we assume the four actions (N/E/W/S) has the same reward)
CONVERGENCE=0.0000001 #The threshold for convergence to determine a stop sign
cur_convergence=100


#Implement this function
def computeQValue(s,action):
    print("Compute Q Values")


#Implement this function    
def valueIteration():
    print('Value Iteration')

                
################# Don't modify the code below################################################
def onGo(idx,screen):
        # global idx
        if(idx<=100 and cur_convergence>CONVERGENCE):
            valueIteration()
            screen.fill(pygame.Color(255,255,255),pygame.Rect(300,580,150,20))
            fnt = pygame.font.SysFont("Bahnschrift", 20)
            iterText = fnt.render("Iterations: "+str(idx), 1, (0,0,0))
            screen.blit(iterText, (300,580))
            return True
        else:
            return False

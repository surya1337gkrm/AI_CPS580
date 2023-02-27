from cell import states
import pygame
import drawfn

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

#####Implement the below functions ############################
def computeQValue(s,action):
    print('Compute Q Values')
        
def valueIteration():
    print('Value Iteration.')

def policyEvaluation():
    print('Policy Evaluation')


def policyImprovement():
    print('Policy Improvement.')


################################# Dont modify the code below ###########################
def policyIteration():
    drawfn.check2=True
    drawfn.radio1=False
    drawfn.radio2=True
    policies={}
    for s in states:
        for cell in s:
            policies[cell.location]=cell.policy
    #policies should be a dictionary with states[][].location as it's key and states[][].policy as value
    i=0
    while True:
        i+=1
        oldPolicy=policies.copy()
        policyEvaluation()
        policyImprovement()
        for s in states:
            for cell in s:
                if ((cell.location[0] == 1 and cell.location[1] == 1) or (cell.location[0] == 3 and cell.location[1] == 0) or  (cell.location[0] == 3 and cell.location[1] == 1)):
                    continue
                else:
                    policies[cell.location]=cell.policy

        drawfn.draw()
        pygame.time.delay(200)
        drawfn.screen.fill(pygame.Color(255,255,255),pygame.Rect(300,580,150,20))
        fnt = pygame.font.SysFont("Bahnschrift", 20)
        iterText = fnt.render("Iterations: "+str(i), 1, (0,0,0))
        drawfn.screen.blit(iterText, (300,580))
        pygame.display.update()
        
        if all(oldPolicy[key] == policies[key] for key in policies):
            print('Ideal Policy Obtained.')
            break
  
def onGo(idx):
        # global idx
        if(idx<=100 and cur_convergence>CONVERGENCE):
            valueIteration()
            drawfn.screen.fill(pygame.Color(255,255,255),pygame.Rect(300,580,150,20))
            fnt = pygame.font.SysFont("Bahnschrift", 20)
            iterText = fnt.render("Iterations: "+str(idx), 1, (0,0,0))
            drawfn.screen.blit(iterText, (300,580))
            return True
        else:
            return False

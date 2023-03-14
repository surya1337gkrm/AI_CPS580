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


def computeQValue(s,action):
    q0 = 0 
    q1 = 0
    q2 = 0
    q3 = 0
    global cur_convergence
     #for action east
    if(action == 0):
        #From (0,1) taking east = towards wall | bounces back and stays in same block
        if(s.location[0]==0 and s.location[1]==1):
            #q0
            q0 =  (ACTION_REWARD+GAMMA*TRANSITION_SUCCEED *(states[s.location[1]][s.location[0]].state_value))
        #q1
            q1 = (ACTION_REWARD + GAMMA *TRANSITION_FAIL*0.5 *  (states[s.location[1]+1][s.location[0]].state_value))
        #q3
            q3 = (ACTION_REWARD + GAMMA * TRANSITION_FAIL*0.5 * (states[s.location[1] - 1][s.location[0]].state_value))
            if (cur_convergence < abs(s.q_values[0]-(q0+q1+q3))):
                cur_convergence = abs(s.q_values[0] - (q0+q1 + q3))
            
            s.q_values[0] = q0+q1 + q3

        elif (s.location[0] == 2):
        #q0
            q0 = (ACTION_REWARD + GAMMA * TRANSITION_SUCCEED * (states[s.location[1]][s.location[0] + 1].state_value))
        #q1
            if (s.location[1] != 2):
                q1 =  (ACTION_REWARD + GAMMA * TRANSITION_FAIL * 0.5 *(states[s.location[1] + 1][s.location[0]].state_value))
            else:
                q1 =  (ACTION_REWARD + GAMMA * TRANSITION_FAIL * 0.5 *(states[s.location[1]][s.location[0]].state_value))
        #q3
            if (s.location[1] == 0):
                q3 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1]][s.location[0]].state_value))
            else:
                q3 =  (ACTION_REWARD + GAMMA * TRANSITION_FAIL * 0.5 *(states[s.location[1]-1][s.location[0]].state_value))
            
            if (cur_convergence < abs(s.q_values[0] - (q0+q1+q3))):
                cur_convergence = abs(s.q_values[0] - (q0+q1+q3))
            s.q_values[0] = q0 + q1 + q3
        elif(s.location[1]==2 and s.location[0]!=2):
        #q0
            if (s.location[0] == 3):
                q0 =  (ACTION_REWARD + GAMMA * TRANSITION_SUCCEED *(states[s.location[1]][s.location[0]].state_value))
            else:
                q0 = (ACTION_REWARD + GAMMA * TRANSITION_SUCCEED * (states[s.location[1]][s.location[0]+1].state_value))
        #q1
            q1 =  (ACTION_REWARD + GAMMA * TRANSITION_FAIL * 0.5 *(states[s.location[1]][s.location[0]].state_value))
            
        #q3
            if (s.location[0] != 1):
                q3 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1]-1][s.location[0]].state_value))
            else:
                q3 =  (-1 + GAMMA * TRANSITION_FAIL * 0.5 *(states[s.location[1]][s.location[0]].state_value))
            if (cur_convergence < abs(s.q_values[0] - (q0 + q1 + q3))):
                cur_convergence = abs(s.q_values[0] - (q0 + q1 + q3))
            s.q_values[0] = q0 + q1 + q3
        elif(s.location[1]==0 and s.location[0] != 2):
            q0=  (ACTION_REWARD + GAMMA *TRANSITION_SUCCEED * (states[s.location[1]][s.location[0] + 1].state_value))
            if (s.location[0] == 0):
                q1=  (ACTION_REWARD + GAMMA * TRANSITION_FAIL * 0.5 *(states[s.location[1] + 1][s.location[0]].state_value))
            else:
                q1 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1] ][s.location[0]].state_value))
            q3 = (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 *  (states[s.location[1]][s.location[0]].state_value))
            
            if (cur_convergence < abs(s.q_values[0] - (q0 + q1+q3))):
                cur_convergence = abs(s.q_values[0] - (q0 + q1 + q3))
            s.q_values[0] = q0 + q1 + q3

#for action south
    elif (action == 1):
        if ((s.location[0] == 1 and s.location[1] == 0) or s.location[1] == 2):
            q1 =  (ACTION_REWARD + (GAMMA *TRANSITION_SUCCEED * states[s.location[1]][s.location[0]].state_value))
            if (s.location[0] != 3):
                q0=  (ACTION_REWARD + (GAMMA *TRANSITION_FAIL * 0.5 * states[s.location[1]][s.location[0] + 1].state_value))
            else:
                q0 = (ACTION_REWARD + (GAMMA *TRANSITION_FAIL * 0.5 *  states[s.location[1]][s.location[0]].state_value))
            if (s.location[0] != 0):
                q2 =  (ACTION_REWARD + (GAMMA *TRANSITION_FAIL * 0.5 * states[s.location[1]][s.location[0]-1].state_value))
            else:
                q2 =  (ACTION_REWARD + (GAMMA *TRANSITION_FAIL * 0.5 * states[s.location[1]][s.location[0]].state_value))
            if (cur_convergence < abs(s.q_values[1] - (q1 + q0+q2))):
                cur_convergence = abs(s.q_values[1] - (q1 + q0 + q2))
            s.q_values[1] = q1 + q0 + q2
        if (s.location[0] == 0 and s.location[1]!=2):
            q2 =  (ACTION_REWARD+(GAMMA*TRANSITION_SUCCEED *states[s.location[1]][s.location[0]].state_value))
            q1 =  (ACTION_REWARD + (GAMMA * TRANSITION_FAIL * 0.5 *states[s.location[1] + 1][s.location[0]].state_value))

            if (s.location[1] == 0):
                q0= (ACTION_REWARD + (GAMMA * TRANSITION_FAIL * 0.5*states[s.location[1]][s.location[0]+1].state_value))
            
            else:
                q0 =  (ACTION_REWARD + (GAMMA * TRANSITION_FAIL * 0.5 *states[s.location[1]][s.location[0]].state_value))

            
            if (cur_convergence < abs(s.q_values[1] - (q0+q1 + q2))):
                cur_convergence = abs(s.q_values[1] - (q0 + q1 + q2))
            
            s.q_values[1] = q0 + q1 + q2
        
        if (s.location[0] == 2 and s.location[1] != 2):
            q0 =  (ACTION_REWARD + (GAMMA *TRANSITION_FAIL * 0.5 * states[s.location[1]][s.location[0] + 1].state_value))
            q1=  (ACTION_REWARD + (GAMMA *TRANSITION_SUCCEED * states[s.location[1] + 1][s.location[0]].state_value))
            if (s.location[1] == 0):
                q2 =  (ACTION_REWARD + (GAMMA *TRANSITION_FAIL * 0.5 * states[s.location[1]][s.location[0] -1].state_value))
            
            if (s.location[1] == 1):
                q2 =  (ACTION_REWARD + (GAMMA *TRANSITION_FAIL * 0.5 * states[s.location[1]][s.location[0]].state_value))
            
            if (cur_convergence < abs(s.q_values[1] - (q0 + q1 + q2))):
                cur_convergence = abs(s.q_values[1] - (q0 + q1 + q2))
            
            s.q_values[1] = q0 + q1 + q2
        

#for action west
    elif (action == 2):
        if (s.location[0] == 0 or s.location[1] == 1):
            q2 =  (ACTION_REWARD + GAMMA *TRANSITION_SUCCEED * (states[s.location[1]][s.location[0]].state_value))
            if (s.location[1] != 2):
                q1 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1]+1][s.location[0]].state_value))
            
            else:
                q1 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1]][s.location[0] + 1].state_value))
            
            if (s.location[1] != 0):
                q3 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1] - 1][s.location[0]].state_value))
            else:
                q3 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1]][s.location[0]].state_value))
            if (cur_convergence < abs(s.q_values[2] - (q2 + q1+q3))):
                cur_convergence = abs(s.q_values[2] - (q2 + q1 + q3))
            
            s.q_values[2] = q2 + q1 + q3
        
        elif (s.location[0] == 1):
            q2 =  (ACTION_REWARD+GAMMA*TRANSITION_SUCCEED *(states[s.location[1]][s.location[0] - 1].state_value))
            q1 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL*0.5 * (states[s.location[1]][s.location[0]].state_value))
            q3 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1]][s.location[0]].state_value))      
            if (cur_convergence < abs(s.q_values[2] - (q2 + q1+q3 ))):
                cur_convergence = abs(s.q_values[2] - (q2 + q1 + q3))
            
            s.q_values[2] = q2 + q1 + q3
        
        elif (s.location[0] == 2 and s.location[1]!=1):
            q2 =  (ACTION_REWARD + GAMMA *TRANSITION_SUCCEED * (states[s.location[1]][s.location[0] - 1].state_value))
            if (s.location[1] == 0):
                q1 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1] + 1][s.location[0]].state_value))
                q3 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1]][s.location[0]].state_value))
            
            else:
                q1 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1]][s.location[0]].state_value))
                q3 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1]-1][s.location[0]].state_value))
            
            if (cur_convergence < abs(s.q_values[2] - (q2 + q1 + q3))):
                cur_convergence = abs(s.q_values[2] - (q2 + q1 + q3))
            
            s.q_values[2] = q2 + q1 + q3
        
        else:
            q1=  (ACTION_REWARD + GAMMA *TRANSITION_FAIL*0.5 * (states[s.location[1]][s.location[0]].state_value))
            q2 =  (ACTION_REWARD + GAMMA * TRANSITION_SUCCEED *(states[s.location[1]][s.location[0] - 1].state_value))
            q3 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL*0.5 * (states[s.location[1] - 1][s.location[0]].state_value))
            if (cur_convergence < abs(s.q_values[2] - (q1+q2  + q3))):
                cur_convergence = abs(s.q_values[2] - (q1+q2 + q3))
                
            s.q_values[2] = q1+q2 + q3
        
    
#for action north
    else:
        if (s.location[1] == 0 or s.location[0] == 1):
            q3 =  (ACTION_REWARD + GAMMA * TRANSITION_SUCCEED *(states[s.location[1]][s.location[0]].state_value))
            q0 =  (ACTION_REWARD + GAMMA*TRANSITION_FAIL * 0.5 *(states[s.location[1]][s.location[0]+1].state_value))
            if (s.location[0] != 0):
                q2=  (ACTION_REWARD + GAMMA*TRANSITION_FAIL * 0.5 *(states[s.location[1]][s.location[0] - 1].state_value))
            
            else:
                q2 = (ACTION_REWARD + GAMMA* TRANSITION_FAIL * 0.5 *(states[s.location[1]][s.location[0]].state_value))
            
            if (cur_convergence < abs(s.q_values[3] - (q3 + q0+q2))):
                cur_convergence = abs(s.q_values[3] - (q3 + q0 + q2))
            
            s.q_values[3] = q3 + q0 + q2
        
        elif (s.location[0] == 0 and s.location[1]!=0):
            q3 =  (ACTION_REWARD + GAMMA *TRANSITION_SUCCEED * (states[s.location[1]-1][s.location[0]].state_value))
            q2=  (ACTION_REWARD + GAMMA*TRANSITION_FAIL * 0.5 *(states[s.location[1]][s.location[0]].state_value))
            if (s.location[1] == 1):
                q0 =  (ACTION_REWARD + GAMMA*TRANSITION_FAIL * 0.5 *(states[s.location[1]][s.location[0]].state_value))
            
            else:
                q0=  (ACTION_REWARD + GAMMA*TRANSITION_FAIL * 0.5 *(states[s.location[1] ][s.location[0]+1].state_value))
            
            if (cur_convergence < abs(s.q_values[3] - (q3 + q2+q0))):
                cur_convergence = abs(s.q_values[3] - (q3 + q2 + q0))
            
            s.q_values[3] = q3 + q2 + q0
        
        elif (s.location[0] == 2 and s.location[1]!=0):
            q3 =  (ACTION_REWARD + GAMMA *TRANSITION_SUCCEED * (states[s.location[1] - 1][s.location[0]].state_value))
            q0= (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5* (states[s.location[1]][s.location[0] + 1].state_value))
            if (s.location[1] == 1):
                q2 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1]][s.location[0]].state_value))
            
            else:
                q2 =  (ACTION_REWARD + GAMMA * TRANSITION_FAIL *0.5*(states[s.location[1]][s.location[0]-1].state_value))
            
            if (cur_convergence < abs(s.q_values[3] - (q3 + q2 + q0))):
                cur_convergence = abs(s.q_values[3] - (q3 + q2 + q0))
            
            s.q_values[3] = q3 + q2 + q0
        
        else:

            q3 =  (ACTION_REWARD + GAMMA *TRANSITION_SUCCEED * (states[s.location[1] - 1][s.location[0]].state_value))
            q0 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1]][s.location[0]].state_value))
            q2 =  (ACTION_REWARD + GAMMA *TRANSITION_FAIL * 0.5 * (states[s.location[1]][s.location[0]-1].state_value))
            if (cur_convergence < abs(s.q_values[3] - (q3 + q0+q2 ))):
                cur_convergence = abs(s.q_values[3] - (q3 + q0+q2))
            s.q_values[3] = q3 + q0+q2 
        
def valueIteration():
    global cur_convergence
    cur_convergence = 0
    #for iterating through the gridworld
    for i in range(0,3):
        for j in range(0,4):
            #skip the special blocks : wall,diamond,pit
            if ((i == 1 and j == 1) or (i == 0 and j == 3) or (i == 1 and j == 3)):
                continue
            else:
                for action in range(0,4):
                    computeQValue(states[i][j], action); 

    #update max q values
    for i in range(0,3):
        for j in range(0,4):
            #skip the special blocks : wall,diamond,pit
            if ((i == 1 and j == 1) or (i == 0 and j == 3) or (i == 1 and j == 3)):
                continue
            else:
                states[i][j].state_value = max(states[i][j].q_values)

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


def policyEvaluation():
    for s in states:
        for cell in s:
           if ((cell.location[0] == 1 and cell.location[1] == 1) or (cell.location[0] == 3 and cell.location[1] == 0) or  (cell.location[0] == 3 and cell.location[1] == 1)):
               continue
           else:
               if(cell.policy==0):
                   if((cell.location[0]==0 and cell.location[1]==1)):
                        v0=TRANSITION_SUCCEED*cell.state_value
                        v1=TRANSITION_FAIL*0.5*states[cell.location[1]+1][cell.location[0]].state_value
                        v3=TRANSITION_FAIL*0.5*states[cell.location[1]-1][cell.location[0]].state_value
                        cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v3)
                   elif((cell.location[0]==3 and cell.location[1]==2)):
                        v0=TRANSITION_SUCCEED*cell.state_value
                        v1=TRANSITION_FAIL*0.5*cell.state_value
                        v3=TRANSITION_FAIL*0.5*(-1)
                        cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v3)
                   elif(cell.location[1]==2):
                       if(cell.location[0]==1):
                           v0=TRANSITION_SUCCEED*states[cell.location[1]][cell.location[0]+1].state_value
                           v1=TRANSITION_FAIL*0.5*cell.state_value
                           v3=v1
                           cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v3)
                       else:
                         v0=TRANSITION_SUCCEED*states[cell.location[1]][cell.location[0]+1].state_value
                         v1=TRANSITION_FAIL*0.5*cell.state_value
                         v3=TRANSITION_FAIL*0.5*states[cell.location[1]-1][cell.location[0]].state_value
                         cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v3)
                   elif(cell.location[1]==0):
                      if(cell.location[0]==1):
                        v0=TRANSITION_SUCCEED*states[cell.location[1]][cell.location[0]+1].state_value
                        v1=TRANSITION_FAIL*0.5*cell.state_value
                        v3=v1
                        cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v3)
                      else:
                         v0=TRANSITION_SUCCEED*states[cell.location[1]][cell.location[0]+1].state_value
                         v1=TRANSITION_FAIL*0.5*states[cell.location[1]+1][cell.location[0]].state_value
                         v3=TRANSITION_FAIL*0.5*cell.state_value
                         cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v3)
                   else:
                     v0=TRANSITION_SUCCEED*(-1)
                     v1=TRANSITION_FAIL*0.5*states[cell.location[1]+1][cell.location[0]].state_value
                     v3=TRANSITION_FAIL*0.5*states[cell.location[1]-1][cell.location[0]].state_value
                     cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v3)
               elif(cell.policy==1):
                   if(cell.location[1]==2):
                       v1=TRANSITION_SUCCEED*cell.state_value
                       if(cell.location[0]==1 or cell.location[0]==2):
                           v0=TRANSITION_FAIL*0.5*states[cell.location[1]][cell.location[0]+1].state_value
                           v2=TRANSITION_FAIL*0.5*states[cell.location[1]][cell.location[0]-1].state_value
                           cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v2)
                       elif(cell.location[0]==0):
                           v0=TRANSITION_FAIL*0.5*states[cell.location[1]][cell.location[0]+1].state_value
                           v2=TRANSITION_FAIL*0.5*cell.state_value
                           cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v2)
                       else:
                           v0=TRANSITION_FAIL*0.5*cell.state_value
                           v2=TRANSITION_FAIL*0.5*states[cell.location[1]][cell.location[0]-1].state_value
                           cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v2)
                   elif(cell.location[1]==1):
                       if(cell.location[0]==0):
                           v0=TRANSITION_FAIL*0.5*cell.state_value
                           v1=TRANSITION_SUCCEED*states[cell.location[1]+1][cell.location[0]].state_value
                           v2=TRANSITION_FAIL*0.5*cell.state_value
                           cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v2)
                       else:
                           v0=TRANSITION_FAIL*0.5*(-1)
                           v1=TRANSITION_SUCCEED*states[cell.location[1]+1][cell.location[0]].state_value
                           v2=TRANSITION_FAIL*0.5*cell.state_value
                           cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v2)
                   elif(cell.location[1]==0):
                       v0=TRANSITION_FAIL*0.5*states[cell.location[1]][cell.location[0]+1].state_value
                       if(cell.location[0]==0):
                           v1=TRANSITION_SUCCEED*states[cell.location[1]+1][cell.location[0]].state_value
                           v2=TRANSITION_FAIL*0.5*cell.state_value
                           cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v2)
                       else:
                           v2=TRANSITION_FAIL*0.5*states[cell.location[1]][cell.location[0]-1].state_value
                           if(cell.location[0]==1):
                               v1=TRANSITION_SUCCEED*cell.state_value
                               cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v2)
                           else:
                               v1=TRANSITION_SUCCEED*states[cell.location[1]+1][cell.location[0]].state_value
                               cell.state_value=ACTION_REWARD+GAMMA*(v0+v1+v2)
               elif(cell.policy==2):
                   if(cell.location[1]==2):
                       v1=TRANSITION_FAIL*0.5*cell.state_value
                       v2=0
                       v3=0
                       if(cell.location[0]==0):
                           v2=TRANSITION_SUCCEED*cell.state_value
                       else:
                           v2=TRANSITION_SUCCEED*states[cell.location[1]][cell.location[0]-1].state_value
                       if(cell.location[0]==1):
                           v3=TRANSITION_FAIL*0.5*cell.state_value
                       else:
                           v3=TRANSITION_FAIL*0.5*states[cell.location[1]-1][cell.location[0]].state_value
                       cell.state_value=ACTION_REWARD+GAMMA*(v1+v2+v3)
                   if(cell.location[1]==1):
                       v1=TRANSITION_FAIL*0.5*states[cell.location[1]+1][cell.location[0]].state_value
                       v2=TRANSITION_SUCCEED*cell.state_value
                       v3=TRANSITION_FAIL*0.5*states[cell.location[1]-1][cell.location[0]].state_value
                       cell.state_value=ACTION_REWARD+GAMMA*(v1+v2+v3)
                   if(cell.location[1]==0):
                       v3=TRANSITION_FAIL*0.5*cell.state_value
                       v1=0
                       v2=0
                       if(cell.location[0]==0):
                           v2=TRANSITION_SUCCEED*cell.state_value
                       else:
                           v2=TRANSITION_SUCCEED*states[cell.location[1]][cell.location[0]-1].state_value
                       if(cell.location[0]==1):
                           v1=TRANSITION_FAIL*0.5*cell.state_value
                       else:
                           v1=TRANSITION_FAIL*0.5*states[cell.location[1]+1][cell.location[0]].state_value
               elif(cell.policy==3):
                   if(cell.location[1]==2):
                       v0=0
                       v2=0
                       v3=0
                       if(cell.location[0]==3):
                           v0=TRANSITION_FAIL*0.5*cell.state_value
                       else:
                           v0=TRANSITION_FAIL*0.5*states[cell.location[1]][cell.location[0]+1].state_value
                       if(cell.location[0]==0):
                           v2=TRANSITION_FAIL*0.5*cell.state_value
                       else:
                           v2=TRANSITION_FAIL*0.5*states[cell.location[1]][cell.location[0]-1].state_value
                       if(cell.location[0]==1):
                           v3=TRANSITION_SUCCEED*cell.state_value
                       else:
                           v3=TRANSITION_SUCCEED*states[cell.location[1]-1][cell.location[0]].state_value
                       cell.state_value=ACTION_REWARD+GAMMA*(v0+v2+v3)
                   elif(cell.location[1]==1):
                       v3= TRANSITION_SUCCEED*states[cell.location[1]-1][cell.location[0]].state_value    
                       v0=0
                       v2=0
                       if(cell.location[0]==0):
                           v0=TRANSITION_FAIL*0.5*cell.state_value
                           v2=v0
                       else:
                           v0=TRANSITION_FAIL*0.5*(-1)
                           v2= TRANSITION_FAIL*0.5*cell.state_value
                       cell.state_value=ACTION_REWARD+GAMMA*(v0+v2+v3)
                   else:
                       v3=TRANSITION_SUCCEED*cell.state_value
                       v0=TRANSITION_FAIL*0.5*states[cell.location[1]][cell.location[0]+1].state_value
                       v2=0
                       if(cell.location[0]==0):
                           v2=TRANSITION_FAIL*0.5*cell.state_value
                       else:
                           v2=TRANSITION_FAIL*0.5*states[cell.location[1]][cell.location[0]-1].state_value

                       cell.state_value=ACTION_REWARD+GAMMA*(v0+v2+v3)


def policyImprovement():
    valueIteration()
    for s in states:
        for cell in s:
            if ((cell.location[0] == 1 and cell.location[1] == 1) or (cell.location[0] == 3 and cell.location[1] == 0) or  (cell.location[0] == 3 and cell.location[1] == 1)):
               continue
            else:
                cell.policy=cell.q_values.index(cell.state_value)


    
def onGo(idx):
        # global idx
        if(idx<100 and cur_convergence>CONVERGENCE):
            valueIteration()
            drawfn.screen.fill(pygame.Color(255,255,255),pygame.Rect(300,580,150,20))
            fnt = pygame.font.SysFont("Bahnschrift", 20)
            iterText = fnt.render("Iterations: "+str(idx), 1, (0,0,0))
            drawfn.screen.blit(iterText, (300,580))
            return True
        else:
            return False

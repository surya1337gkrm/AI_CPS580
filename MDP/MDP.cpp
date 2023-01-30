//
//  MDP.cpp
//  AI_GridWorld
//
//  Created by cpsfaculty on 11/13/17.
//  Copyright (c) 2017 ___Ju Shen___. All rights reserved.
//

#include <stdio.h>

#include "MDP.h"
#include<iostream>
#include <algorithm>
#include<map>
using namespace std;

/*************************************************************** Below are the two functions you need to implement ****************************************************/


/*Compute a Q-value for a given state and its action
  Input: state variable s; action (go to East/North/West/South), the corresponding interger value for each action is defined in the "MDP.h" Macros definition on the top
  Output: you need to update the corresponding q_values of the input state variable s
 */



void MDP::computeQValue(State &s, const int action)
{
    float q0 = 0; 
    float q1 = 0;
    float q2 = 0;
    float q3 = 0;

    //for action east
    if (action == 0) {
    //From (0,1) taking east = towards wall | bounces back and stays in same block
        if(s.location.x==0 && s.location.y==1){
            
            // q0
            q0 = TRANSITION_SUCCEED * (ACTION_REWARD+GAMMA*(states[s.location.y][s.location.x].state_value));
            //q1
            q1 = TRANSITION_FAIL*0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y+1][s.location.x].state_value));
            //q3
            q3 = TRANSITION_FAIL*0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y - 1][s.location.x].state_value));
            if (cur_convergence < abs(s.q_values[0]-(q0+q1+q3))) {
                cur_convergence = abs(s.q_values[0] - (q0+q1 + q3));
            }
            s.q_values[0] = q0+q1 + q3;

        }
        else if (s.location.x == 2) {
            //q0
            q0 = TRANSITION_SUCCEED * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x + 1].state_value));
            //q1
            if (s.location.y != 2) {
                q1 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y + 1][s.location.x].state_value));
            }
            else {
                q1 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));
            }
            //q3
            if (s.location.y == 0) {
                q3 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));
            }
            else {
                q3 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y-1][s.location.x].state_value));
            }
            
            if (cur_convergence < abs(s.q_values[0] - (q0+q1+q3))) {
                cur_convergence = abs(s.q_values[0] - (q0+q1+q3));
            }
            s.q_values[0] = q0 + q1 + q3;
        }
        else if(s.location.y==2 && s.location.x!=2) {
            //q0
            if (s.location.x == 3) {
                q0 = TRANSITION_SUCCEED * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));
            }
            else {
                q0 = TRANSITION_SUCCEED * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x+1].state_value));
            }
            //q1
             q1 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));
            
            //q3
            if (s.location.x != 1) {
             q3 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y-1][s.location.x].state_value));
            }
            else{
                q3 = TRANSITION_FAIL * 0.5 * (-1 + GAMMA * (states[s.location.y][s.location.x].state_value));
            }
            if (cur_convergence < abs(s.q_values[0] - (q0 + q1 + q3))) {
                cur_convergence = abs(s.q_values[0] - (q0 + q1 + q3));
            }
            s.q_values[0] = q0 + q1 + q3;
        }
        else if(s.location.y==0 && s.location.x != 2) {
            q0= TRANSITION_SUCCEED * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x + 1].state_value));
            if (s.location.x == 0) {
                q1= TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y + 1][s.location.x].state_value));
            }
            else {
                q1 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y ][s.location.x].state_value));
            }
            q3 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));
            
            if (cur_convergence < abs(s.q_values[0] - (q0 + q1+q3))) {
                cur_convergence = abs(s.q_values[0] - (q0 + q1 + q3));
            }
            s.q_values[0] = q0 + q1 + q3;
        }
    }

    //for action south
    else if (action == 1) {
        
        if ((s.location.x == 1 && s.location.y == 0) || s.location.y == 2) {
            q1 = TRANSITION_SUCCEED * (ACTION_REWARD + (GAMMA * states[s.location.y][s.location.x].state_value));
            if (s.location.x != 3) {
                q0= TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (GAMMA * states[s.location.y][s.location.x + 1].state_value));
            }
            else {
                q0 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (GAMMA * states[s.location.y][s.location.x].state_value));

            }
            if (s.location.x != 0) {
                q2 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (GAMMA * states[s.location.y][s.location.x-1].state_value));

            }
            else {
                q2 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (GAMMA * states[s.location.y][s.location.x].state_value));

            }
            if (cur_convergence < abs(s.q_values[1] - (q1 + q0+q2))) {
                cur_convergence = abs(s.q_values[1] - (q1 + q0 + q2));
            }
            s.q_values[1] = q1 + q0 + q2;
        };
        if (s.location.x == 0 && s.location.y!=2) {
            q2 = TRANSITION_SUCCEED * (ACTION_REWARD+(GAMMA*states[s.location.y][s.location.x].state_value));
            q1 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (GAMMA * states[s.location.y + 1][s.location.x].state_value));

            if (s.location.y == 0) {
                q0= TRANSITION_FAIL * 0.5*(ACTION_REWARD + (GAMMA * states[s.location.y][s.location.x+1].state_value));
            }
            else {
                q0 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (GAMMA * states[s.location.y][s.location.x].state_value));

            }
            if (cur_convergence < abs(s.q_values[1] - (q0+q1 + q2))) {
                cur_convergence = abs(s.q_values[1] - (q0 + q1 + q2));
            }
            s.q_values[1] = q0 + q1 + q2;
        }
        if (s.location.x == 2 && s.location.y != 2) {
            q0 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (GAMMA * states[s.location.y][s.location.x + 1].state_value));
            q1= TRANSITION_SUCCEED * (ACTION_REWARD + (GAMMA * states[s.location.y + 1][s.location.x].state_value));
            if (s.location.y == 0) {
                q2 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (GAMMA * states[s.location.y][s.location.x -1].state_value));
            }
            if (s.location.y == 1) {
                q2 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (GAMMA * states[s.location.y][s.location.x].state_value));
            }
            if (cur_convergence < abs(s.q_values[1] - (q0 + q1 + q2))) {
                cur_convergence = abs(s.q_values[1] - (q0 + q1 + q2));
            }
            s.q_values[1] = q0 + q1 + q2;
        }

    }

    //for action west
    else if (action == 2) {
        if (s.location.x == 0 || s.location.y == 1) { 
            q2 = TRANSITION_SUCCEED * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));
            if (s.location.y != 2) {
                q1 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y+1][s.location.x].state_value));
            }
            else {
                q1 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x + 1].state_value));
            }
            if (s.location.y != 0) {
                q3 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y - 1][s.location.x].state_value));

            }
            else {
                q3 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));

            }
            if (cur_convergence < abs(s.q_values[2] - (q2 + q1+q3))) {
                cur_convergence = abs(s.q_values[2] - (q2 + q1 + q3));
            }
            s.q_values[2] = q2 + q1 + q3;
        }
        else if (s.location.x == 1) {
            q2 = TRANSITION_SUCCEED * (ACTION_REWARD+GAMMA*(states[s.location.y][s.location.x - 1].state_value));
            q1 = TRANSITION_FAIL*0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));
            q3 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));      
            if (cur_convergence < abs(s.q_values[2] - (q2 + q1+q3 ))) {
                cur_convergence = abs(s.q_values[2] - (q2 + q1 + q3));
            }
            s.q_values[2] = q2 + q1 + q3;
        }
        else if (s.location.x == 2 && s.location.y!=1) {
            q2 = TRANSITION_SUCCEED * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x - 1].state_value));
            if (s.location.y == 0) {
                q1 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y + 1][s.location.x].state_value));
                q3 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));
            }
            else {
                q1 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));
                q3 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y-1][s.location.x].state_value));
            }
            if (cur_convergence < abs(s.q_values[2] - (q2 + q1 + q3))) {
                cur_convergence = abs(s.q_values[2] - (q2 + q1 + q3));
            }
            s.q_values[2] = q2 + q1 + q3;
        }
        else {
            q1= TRANSITION_FAIL * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));
            q2 = TRANSITION_SUCCEED * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x - 1].state_value));
            q3 = TRANSITION_FAIL * (ACTION_REWARD + GAMMA * (states[s.location.y - 1][s.location.x].state_value));
                if (cur_convergence < abs(s.q_values[2] - (q1+q2  + q3))) {
                    cur_convergence = abs(s.q_values[2] - (q1+q2 + q3));
                }
            s.q_values[2] = q1+q2 + q3;
        }
    }
    //for action north
    else {
        if (s.location.y == 0 || s.location.x == 1) {
            q3 = TRANSITION_SUCCEED * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));
            q0 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (states[s.location.y][s.location.x+1].state_value));
            if (s.location.x != 0) {
                q2= TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (states[s.location.y][s.location.x - 1].state_value));
            }
            else {
                q2 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (states[s.location.y][s.location.x].state_value));
            }
            if (cur_convergence < abs(s.q_values[3] - (q3 + q0+q2))) {
                cur_convergence = abs(s.q_values[3] - (q3 + q0 + q2));
            }
            s.q_values[3] = q3 + q0 + q2;
        }
        else if (s.location.x == 0 && s.location.y!=0) {
            q3 = TRANSITION_SUCCEED * (ACTION_REWARD + GAMMA * (states[s.location.y-1][s.location.x].state_value));
            q2= TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (states[s.location.y][s.location.x].state_value));
            if (s.location.y == 1) {
                q0 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (states[s.location.y][s.location.x].state_value));
            }
            else {
                q0= TRANSITION_FAIL * 0.5 * (ACTION_REWARD + (states[s.location.y ][s.location.x+1].state_value));
            }
            if (cur_convergence < abs(s.q_values[3] - (q3 + q2+q0))) {
                cur_convergence = abs(s.q_values[3] - (q3 + q2 + q0));
            }
            s.q_values[3] = q3 + q2 + q0;
        }
        else if (s.location.x == 2 && s.location.y!=0) {
            q3 = TRANSITION_SUCCEED * (ACTION_REWARD + GAMMA * (states[s.location.y - 1][s.location.x].state_value));
            q0= TRANSITION_FAIL * 0.5*(ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x + 1].state_value));
            if (s.location.y == 1) {
                q2 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));
            }
            else {
                q2 = TRANSITION_FAIL *0.5* (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x-1].state_value));
            }
            if (cur_convergence < abs(s.q_values[3] - (q3 + q2 + q0))) {
                cur_convergence = abs(s.q_values[3] - (q3 + q2 + q0));
            }
            s.q_values[3] = q3 + q2 + q0;
        }
        else {

            q3 = TRANSITION_SUCCEED * (ACTION_REWARD + GAMMA * (states[s.location.y - 1][s.location.x].state_value));
            q0 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x].state_value));
            q2 = TRANSITION_FAIL * 0.5 * (ACTION_REWARD + GAMMA * (states[s.location.y][s.location.x-1].state_value));
            if (cur_convergence < abs(s.q_values[3] - (q3 + q0+q2 ))) {
                cur_convergence = abs(s.q_values[3] - (q3 + q0+q2));
            }
            s.q_values[3] = q3 + q0+q2 ;
        }
    }
}



/*There is no return value, actually you need to use the computing result to update the state values of all the states defined as data member "State states[3][4]". Of course, you don't need to update the wall state: states[1][1], the diamond state: states[0][3], and pitfall state: states[1][3] */
void MDP::valueIteration()
{
    cur_convergence = 0;
    //for iterating through the gridworld
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            //skip the special blocks : wall,diamond,pit
            if ((i == 1 && j == 1) || (i == 0 && j == 3) || (i == 1 && j == 3)) {
                continue;
            }
            else { 
                for (int action = 0; action < 4; action++) { 
                    computeQValue(states[i][j], action); 
                } 
            } 
        }
    }

    //update max q values
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            //skip the special blocks : wall,diamond,pit
            if ((i == 1 && j == 1) || (i == 0 && j == 3) || (i == 1 && j == 3)) {
                continue;
            }
            else {
                    states[i][j].state_value = *max_element(begin(states[i][j].q_values),end(states[i][j].q_values));
                };
        }
    }
}


/**********************************************************************	End of Assignment *********************************************************************/


MDP::MDP()
{
    /*Initialize all the state with 0.0 state_value and 0.0 Q_values*/
    for(int y = 0; y < 3; y++)
    {
        for(int x = 0; x < 4; x++)
        {
            states[y][x].location.x = x; //specify the location for this state
            states[y][x].location.y = y;
            
            states[y][x].state_value = 0.0; //define the state value
            states[y][x].q_values[0] = 0.0; //define the Q value
            states[y][x].q_values[1] = 0.0;
            states[y][x].q_values[2] = 0.0;
            states[y][x].q_values[3] = 0.0;
        }
    }
    
    /* Reset the values for the two special states: diamonds (0, 3), pitfall (1, 3). Actually there are no Q-values for these two states as these two states represents the final state of the game. Similarly, for the wall (1, 1), it does not have any state value or Q values. So make sure not to update these three states during your program*/
    states[0][3].state_value = 1.0;
    states[1][3].state_value = -1.0;
    
    
    
    /*Set the current convergence to a big number initially*/
    cur_convergence = 100; //the reason this value is set to a big value is to ensure 
    
    
}


MDP::~MDP()
{
    
}

/*Reset the current computed state and Q values*/
void MDP::resetData()
{
    /*Initialize all the state with 0.0 state_value and 0.0 Q_values*/
    for(int y = 0; y < 3; y++)
    {
        for(int x = 0; x < 4; x++)
        {
            states[y][x].location.x = x; //specify the location for this state
            states[y][x].location.y = y;
            
            states[y][x].state_value = 0.0; //define the state value
            states[y][x].q_values[0] = 0.0; //define the Q value
            states[y][x].q_values[1] = 0.0;
            states[y][x].q_values[2] = 0.0;
            states[y][x].q_values[3] = 0.0;
        }
    }
    
    /* Reset the values for the two special states: diamonds (0, 3), pitfall (1, 3). Actually there are no Q-values for these two states as these two states represents the final state of the game. Similarly, for the wall (1, 1), it does not have any state value or Q values. So make sure not to update these three states during your program*/
    states[0][3].state_value = 1.0;
    states[1][3].state_value = -1.0;
    
    
    
    /*Set the current convergence to a big number initially*/
    cur_convergence = 100; //the reason this value is set to a big value is to ensure
    
    
}

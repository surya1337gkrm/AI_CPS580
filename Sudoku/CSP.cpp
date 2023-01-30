//
//  CSP.cpp
//  Sudoku
//
//  Created by cpsfaculty on 02/10/18.
//  Copyright (c) 2018 ___Ju Shen___. All rights reserved.
//

#include <stdio.h>

#include "CSP.h"

/************************************** Below are the three functions you need to implement ***************************************/

/*Check whether current state satisfy the constraints*/
bool CSP::goalCheck(const State state)
{
    //Elements shouldn't repeat in row,column and 3*3 Block.
    //check[0][9][9] will have a 9*9 block representing row wise checking.
    //check[1][9][9] will have a 9*9 block representing column wise checking.
    //check[2][9][9] will have a 9*9 block representing 3*3 square wise checking.
    int check[3][9][9] = {};

    for (int row = 0; row < 9; row++)
    {
        for (int col = 0; col < 9; col++)
        {
            //check for empty values
            if (!state.values[row][col]) return false;

            //checking rows for duplicate
            //while row checking, row constant
            if (check[0][row][state.values[row][col] - 1]) {
                return false;
            }
            check[0][row][state.values[row][col] - 1]++;

            //checking columns for duplicates

            if (check[1][col][state.values[row][col] - 1]) {
                return false;
            }
            check[1][col][state.values[row][col] - 1]++;

            //checking for duplicates in 3*3 Square using for loops
            /*int gridStartRow = row - row % 3;
            int gridStartCol = col - col % 3;
            int valToCheck = state.values[row][col];
            for (int r = 0; r < 3; r++) {
                for (int c = 0; c < 3; c++) {
                    if (!(gridStartRow + r == row && gridStartCol + c ==  col)) {
                        if (state.values[gridStartRow + r][gridStartCol + c] == valToCheck) {
                            return false;
                        }
                    }
                }
            }*/

            if (check[2][3 * (row / 3) + (col / 3)][state.values[row][col] - 1]) {
                return false;
            }
            check[2][3 * (row / 3) + (col / 3)][state.values[row][col] - 1]++;
        }
    }
    return true;
}

vector<int> a1 = { 1,2,3 };
//using vector methods to get the common elements between 2 vectors
vector<int> getIntersection(vector<int> domain1, vector<int> domain2) {
    sort(domain1.begin(), domain1.end());
    sort(domain2.begin(), domain2.end());

    vector<int> intersection;
    set_intersection(domain1.begin(), domain1.end(), domain2.begin(), domain2.end(), back_inserter(intersection));

    return intersection;
};

//update row,column and 3*3 Square Block domains
vector<int> getDomain(int row, int col, State state, int(*checkArray)[9][9]) {

    vector<int> rowDomain;
    vector<int> colDomain;
    vector<int> subgridDomain;


    for (int i = 0; i < 9; i++) {
        //rows
        if (!checkArray[0][row][i]) {
            rowDomain.push_back(i + 1);
        }
        //columns
        if (!checkArray[1][col][i]) {
            colDomain.push_back(i + 1);
        }
        //3*3 Blocks
        if (!checkArray[2][3 * (row / 3) + (col / 3)][i]) {
            subgridDomain.push_back(i + 1);
        }
    }
    vector<int> rcDomain = getIntersection(rowDomain, colDomain);
    return getIntersection(rcDomain, subgridDomain);
}


/*Update Domain for the forward checking*/
void CSP::updateDomain(const State state)
{
    int checkAssigned[3][9][9] = {};
    //check if the values are not empty. if they aren't empty update the check matrix.
    //if they are empty,SKIP.
    //and update rows,columns and 3*3 Square blocks.
    for (int row = 0; row < 9; row++) {
        for (int col = 0; col < 9; col++) {
            if (!state.values[row][col]) continue;
            checkAssigned[0][row][state.values[row][col] - 1]++;
            checkAssigned[1][col][state.values[row][col] - 1]++;
            checkAssigned[2][3 * (row / 3) + (col / 3)][state.values[row][col] - 1]++;
        }
    }

    //for each element, check if it's empty and if it isn't update the domain for each variable.
    /*We shouldn't update the variables domain in previous for-for loop
    as checkAssigned can be empty and it throws an Error*/
    for (int row = 0; row < 9; row++) {
        for (int col = 0; col < 9; col++) {
            if (!state.values[row][col])
            {
                variables[row][col].domain = getDomain(row, col, state, checkAssigned);
            }

        }
    }
}



/*Arc consistency use : Pending*/
void CSP::arcConsistency(const State state)
{

}


/************************************************	End of Assignment ***********************************************/




CSP::CSP()
{
    /*Initially assign the domain, assignment for each variable and initialize the current state*/
    for (int y = 0; y < 9; y++)
    {
        for (int x = 0; x < 9; x++)
        {
            variables[y][x].assignement = 0; //Initialize the assignment

            /*Initialize the domain*/
            for (int i = 1; i <= 9; i++)
            {
                variables[y][x].domain.push_back(i);
            }

            cur_state.values[y][x] = 0; //Initizlize the current state

        }
    }

    alg_opt = 1; //initially set it as back track

    srand(time(NULL));
    random = 0;
}


CSP::~CSP()
{

}




void CSP::setData(int* data)
{
    for (int y = 0; y < 9; y++)
    {
        for (int x = 0; x < 9; x++)
        {
            int idx = y * 9 + x;
            variables[y][x].assignement = data[idx]; //Initialize the assignment
            cur_state.values[y][x] = data[idx]; //Initizlize the current state

        }
    }
}

void CSP::clearData()
{
    /*Initially assign the domain, assignment for each variable and initialize the current state*/
    for (int y = 0; y < 9; y++)
    {
        for (int x = 0; x < 9; x++)
        {
            variables[y][x].assignement = 0; //Initialize the assignment

            /*Initialize the domain*/
            variables[y][x].domain.clear();
            for (int i = 1; i <= 9; i++)
            {
                variables[y][x].domain.push_back(i);
            }

            cur_state.values[y][x] = 0; //Initizlize the current state

        }
    }

    /*Check whether a random domain is use*/
    if (random == 1)
        reshuffleDomain();

    repeating_list.clear();
    while (!assigned_variables.empty())
    {
        assigned_variables.pop();
        repeating_list.clear();
    }

}


void CSP::reshuffleDomain()
{
    for (int i = 0; i < 81; i++)
    {
        int y = i / 9;
        int x = i % 9;

        std::random_shuffle(variables[y][x].domain.begin(), variables[y][x].domain.end());
    }
}

void CSP::sortDomain()
{
    for (int i = 0; i < 81; i++)
    {
        int y = i / 9;
        int x = i % 9;

        std::sort(variables[y][x].domain.begin(), variables[y][x].domain.end());
    }
}

/*Cancel last assignment*/
int CSP::goBack(int* chosen_cell)
{
    if (assigned_variables.size() > 0)
    {
        int cur_id = assigned_variables.top(); /*Remove last options*/
        assigned_variables.pop(); //pop out last option
        int y = cur_id / 9;
        int x = cur_id % 9;

        variables[y][x].assignement = 0; //assign the cell to zero
        cur_state.values[y][x] = 0; //update the assignment
        *chosen_cell = cur_id;

        // printf("(%d, %d)\n", y, x);
        if (alg_opt == 2)
        {
            updateDomain(cur_state);
        }
        else if (alg_opt == 3)
        {
            arcConsistency(cur_state);
        }

    }

    return goalCheck(cur_state);

}


bool CSP::arcCheckingOrder(int* chosen_cell)
{
    arcConsistency(cur_state);



    /*First go through all the variables and do backtrack if there is no empty domain */
    for (int i = 0; i < 81; i++)
    {
        int y = i / 9;
        int x = i % 9;


        if (cur_state.values[y][x] == 0 && variables[y][x].domain.size() == 0)
        {
            int available_assignemnt = 0; //an indicatior whether there are possible possible varaibles to be re-assigned
            while (available_assignemnt == 0) {
                int cur_id = assigned_variables.top();
                int y = cur_id / 9;
                int x = cur_id % 9;
                variables[y][x].assignement = 0;
                cur_state.values[y][x] = 0;
                arcConsistency(cur_state);


                for (int i = 0; i < variables[y][x].domain.size(); i++)
                {
                    State temp_state;
                    temp_state = cur_state;
                    temp_state.values[y][x] = variables[y][x].domain[i];
                    if (std::find(repeating_list.begin(), repeating_list.end(), temp_state) == repeating_list.end()) //if not in the repeating list
                    {
                        cur_state = temp_state;
                        variables[y][x].assignement = variables[y][x].domain[i];
                        repeating_list.push_back(temp_state);
                        available_assignemnt = 1;
                        *chosen_cell = cur_id;
                        arcConsistency(cur_state);
                        return false; //get out of the current varaible assignment
                    }
                }

                if (available_assignemnt == 0) //if all the domain values have been tried for current variable
                {
                    variables[y][x].assignement = 0;
                    cur_state.values[y][x] = 0;
                    assigned_variables.pop();

                }
            }

        }

    }

    /*If there is no variable that has empty domain, then assign variable here*/
    /*First go through all the variables and do backtrack if there is no empty domain */
    int count = 0;
    while (count < 81)
    {
        /*Find the index of minimum number of domain*/
        int min_idx = 0;
        int min_num = 10; //because the maximum number of domain is 10
        for (int i = 0; i < 81; i++)
        {
            int y = i / 9;
            int x = i % 9;
            if (cur_state.values[y][x] == 0 && variables[y][x].domain.size() > 0)
            {
                if (variables[y][x].domain.size() < min_num) {
                    min_idx = i;
                    min_num = variables[y][x].domain.size();
                }
            }
        }

        int y = min_idx / 9;
        int x = min_idx % 9;

        /*If there is any varable has not been assigned yet, assign it and return it*/
        if (cur_state.values[y][x] == 0 && variables[y][x].domain.size() > 0)
        {
            /*Find the smalles number in domain to assign it. Here no update domain for bracktrack*/
            int id_min = 0;
            cur_state.values[y][x] = variables[y][x].domain[id_min];
            variables[y][x].assignement = variables[y][x].domain[id_min];
            assigned_variables.push(min_idx); //push the variable into stack, which will be used for backtrack (or DFS)
            repeating_list.push_back(cur_state); //make this state into the repeat_list
            *chosen_cell = 9 * y + x;

            arcConsistency(cur_state); //Every time modify the assignment update the domain

            return false;
        }

        count++;

    }

    if (goalCheck(cur_state))
    {
        printf("find the goal\n");
        return true;
    }
    else
    {
        int available_assignemnt = 0; //an indicatior whether there are possible varaibles to be re-assigned
        while (available_assignemnt == 0) {
            int cur_id = assigned_variables.top();
            int y = cur_id / 9;
            int x = cur_id % 9;
            variables[y][x].assignement = 0;
            cur_state.values[y][x] = 0;
            arcConsistency(cur_state);
            for (int i = 0; i < variables[y][x].domain.size(); i++)
            {
                State temp_state;
                temp_state = cur_state;
                temp_state.values[y][x] = variables[y][x].domain[i];
                if (std::find(repeating_list.begin(), repeating_list.end(), temp_state) == repeating_list.end()) //if not in the repeating list
                {
                    cur_state = temp_state;
                    variables[y][x].assignement = variables[y][x].domain[i];
                    repeating_list.push_back(cur_state);
                    available_assignemnt = 1;
                    *chosen_cell = cur_id;
                    break; //get out of the current varaible assignment
                }
            }

            if (available_assignemnt == 0) //if all the domain values have been tried for current variable
            {

                assigned_variables.pop();

            }
        }

        return false;
    }
    return false;

}



/*arcChecking without ordering*/
bool CSP::arcChecking(int* chosen_cell)
{
    arcConsistency(cur_state);



    /*First go through all the variables and do backtrack if there is no empty domain */
    for (int i = 0; i < 81; i++)
    {
        int y = i / 9;
        int x = i % 9;

        if (cur_state.values[y][x] == 0 && variables[y][x].domain.size() == 0)
        {
            int available_assignemnt = 0; //an indicatior whether there are possible possible varaibles to be re-assigned
            while (available_assignemnt == 0) {
                int cur_id = assigned_variables.top();
                int y = cur_id / 9;
                int x = cur_id % 9;
                variables[y][x].assignement = 0;
                cur_state.values[y][x] = 0;
                arcConsistency(cur_state);


                for (int i = 0; i < variables[y][x].domain.size(); i++)
                {
                    State temp_state;
                    temp_state = cur_state;
                    temp_state.values[y][x] = variables[y][x].domain[i];
                    if (std::find(repeating_list.begin(), repeating_list.end(), temp_state) == repeating_list.end()) //if not in the repeating list
                    {
                        cur_state = temp_state;
                        variables[y][x].assignement = variables[y][x].domain[i];
                        repeating_list.push_back(temp_state);
                        available_assignemnt = 1;
                        *chosen_cell = cur_id;
                        arcConsistency(cur_state);
                        return false; //get out of the current varaible assignment
                    }
                }

                if (available_assignemnt == 0) //if all the domain values have been tried for current variable
                {
                    variables[y][x].assignement = 0;
                    cur_state.values[y][x] = 0;
                    assigned_variables.pop();

                }
            }

        }
    }

    /*If there is no variable that has empty domain, then assign variable here*/
    for (int i = 0; i < 81; i++)
    {
        int y = i / 9;
        int x = i % 9;

        /*If there is any varable has not been assigned yet, assign it and return it*/
        if (cur_state.values[y][x] == 0 && variables[y][x].domain.size() > 0)
        {
            /*Find the smalles number in domain to assign it. Here no update domain for bracktrack*/
            int id_min = 0;
            cur_state.values[y][x] = variables[y][x].domain[id_min];
            variables[y][x].assignement = variables[y][x].domain[id_min];
            assigned_variables.push(i); //push the variable into stack, which will be used for backtrack (or DFS)
            repeating_list.push_back(cur_state); //make this state into the repeat_list
            *chosen_cell = 9 * y + x;

            arcConsistency(cur_state); //Every time modify the assignment update the domain

            return false;
        }

    }

    if (goalCheck(cur_state))
    {
        printf("find the goal\n");
        return true;
    }
    else
    {
        int available_assignemnt = 0; //an indicatior whether there are possible varaibles to be re-assigned
        while (available_assignemnt == 0) {
            int cur_id = assigned_variables.top();
            int y = cur_id / 9;
            int x = cur_id % 9;
            variables[y][x].assignement = 0;
            cur_state.values[y][x] = 0;
            arcConsistency(cur_state);
            for (int i = 0; i < variables[y][x].domain.size(); i++)
            {
                State temp_state;
                temp_state = cur_state;
                temp_state.values[y][x] = variables[y][x].domain[i];
                if (std::find(repeating_list.begin(), repeating_list.end(), temp_state) == repeating_list.end()) //if not in the repeating list
                {
                    cur_state = temp_state;
                    variables[y][x].assignement = variables[y][x].domain[i];
                    repeating_list.push_back(cur_state);
                    available_assignemnt = 1;
                    *chosen_cell = cur_id;
                    break; //get out of the current varaible assignment
                }
            }

            if (available_assignemnt == 0) //if all the domain values have been tried for current variable
            {

                assigned_variables.pop();

            }
        }

        return false;
    }
    return false;

}



/*Forward Checking algorithm*/
bool CSP::forwardChecking(int* chosen_cell)
{
    updateDomain(cur_state); //the first step is based on current setting to update the domain



    /*First go through all the variables and do backtrack whether there is an empty domain */
    for (int i = 0; i < 81; i++)
    {
        int y = i / 9;
        int x = i % 9;

        if (cur_state.values[y][x] == 0 && variables[y][x].domain.size() == 0)
        {
            int available_assignemnt = 0; //an indicatior whether there are possible possible varaibles to be re-assigned
            while (available_assignemnt == 0) {
                int cur_id = assigned_variables.top();
                int y = cur_id / 9;
                int x = cur_id % 9;
                variables[y][x].assignement = 0;
                cur_state.values[y][x] = 0;
                updateDomain(cur_state);
                for (int i = 0; i < variables[y][x].domain.size(); i++)
                {
                    State temp_state;
                    temp_state = cur_state;
                    temp_state.values[y][x] = variables[y][x].domain[i];
                    if (std::find(repeating_list.begin(), repeating_list.end(), temp_state) == repeating_list.end()) //if not in the repeating list
                    {
                        cur_state = temp_state;
                        variables[y][x].assignement = variables[y][x].domain[i];
                        repeating_list.push_back(temp_state);
                        available_assignemnt = 1;
                        *chosen_cell = cur_id;
                        updateDomain(cur_state);
                        return false; //get out of the current varaible assignment
                    }
                }

                if (available_assignemnt == 0) //if all the domain values have been tried for current variable
                {
                    variables[y][x].assignement = 0;
                    cur_state.values[y][x] = 0;
                    assigned_variables.pop();

                }
            }

        }
    }

    /*If there is no variable that has empty domain, then assign variable here*/
    for (int i = 0; i < 81; i++)
    {
        int y = i / 9;
        int x = i % 9;

        /*If there is any varable has not been assigned yet, assign it and return it*/
        if (cur_state.values[y][x] == 0 && variables[y][x].domain.size() > 0)
        {
            /*Find the smalles number in domain to assign it. Here no update domain for bracktrack*/
            int id_min = 0;
            cur_state.values[y][x] = variables[y][x].domain[id_min];
            variables[y][x].assignement = variables[y][x].domain[id_min];
            assigned_variables.push(i); //push the variable into stack, which will be used for backtrack (or DFS)
            repeating_list.push_back(cur_state); //make this state into the repeat_list
            *chosen_cell = 9 * y + x;

            updateDomain(cur_state); //Every time modify the assignment update the domain

            return false;
        }

    }

    if (goalCheck(cur_state))
    {
        printf("find the goal\n");
        return true;
    }
    else
    {
        int available_assignemnt = 0; //an indicatior whether there are possible varaibles to be re-assigned
        while (available_assignemnt == 0) {
            int cur_id = assigned_variables.top();
            int y = cur_id / 9;
            int x = cur_id % 9;
            variables[y][x].assignement = 0;
            cur_state.values[y][x] = 0;
            updateDomain(cur_state);
            for (int i = 0; i < variables[y][x].domain.size(); i++)
            {
                State temp_state;
                temp_state = cur_state;
                temp_state.values[y][x] = variables[y][x].domain[i];
                if (std::find(repeating_list.begin(), repeating_list.end(), temp_state) == repeating_list.end()) //if not in the repeating list
                {
                    cur_state = temp_state;
                    variables[y][x].assignement = variables[y][x].domain[i];
                    repeating_list.push_back(cur_state);
                    available_assignemnt = 1;
                    *chosen_cell = cur_id;
                    break; //get out of the current varaible assignment
                }
            }

            if (available_assignemnt == 0) //if all the domain values have been tried for current variable
            {

                assigned_variables.pop();

            }
        }

        return false;
    }
    return false;

}


/*Forward Checking algorithm*/
bool CSP::forwardCheckingOrder(int* chosen_cell)
{

    updateDomain(cur_state); //the first step is based on current setting to update the domain



    /*First go through all the variables and do backtrack whether there is an empty domain */
    for (int i = 0; i < 81; i++)
    {
        int y = i / 9;
        int x = i % 9;

        if (cur_state.values[y][x] == 0 && variables[y][x].domain.size() == 0)
        {
            int available_assignemnt = 0; //an indicatior whether there are possible possible varaibles to be re-assigned
            while (available_assignemnt == 0) {
                int cur_id = assigned_variables.top();
                int y = cur_id / 9;
                int x = cur_id % 9;
                variables[y][x].assignement = 0;
                cur_state.values[y][x] = 0;
                updateDomain(cur_state);
                for (int i = 0; i < variables[y][x].domain.size(); i++)
                {
                    State temp_state;
                    temp_state = cur_state;
                    temp_state.values[y][x] = variables[y][x].domain[i];
                    if (std::find(repeating_list.begin(), repeating_list.end(), temp_state) == repeating_list.end()) //if not in the repeating list
                    {
                        cur_state = temp_state;
                        variables[y][x].assignement = variables[y][x].domain[i];
                        repeating_list.push_back(temp_state);
                        available_assignemnt = 1;
                        *chosen_cell = cur_id;
                        updateDomain(cur_state);
                        return false; //get out of the current varaible assignment
                    }
                }

                if (available_assignemnt == 0) //if all the domain values have been tried for current variable
                {
                    variables[y][x].assignement = 0;
                    cur_state.values[y][x] = 0;
                    assigned_variables.pop();

                }
            }

        }
    }


    int count = 0;
    while (count < 81)
    {
        /*Find the index of minimum number of domain*/
        int min_idx = 0;
        int min_num = 10; //because the maximum number of domain is 10
        for (int i = 0; i < 81; i++)
        {
            int y = i / 9;
            int x = i % 9;
            if (cur_state.values[y][x] == 0 && variables[y][x].domain.size() > 0)
            {
                if (variables[y][x].domain.size() < min_num) {
                    min_idx = i;
                    min_num = variables[y][x].domain.size();
                }
            }
        }

        int y = min_idx / 9;
        int x = min_idx % 9;

        /*If there is any varable has not been assigned yet, assign it and return it*/
        if (cur_state.values[y][x] == 0 && variables[y][x].domain.size() > 0)
        {
            /*Find the smalles number in domain to assign it. Here no update domain for bracktrack*/
            int id_min = 0;
            cur_state.values[y][x] = variables[y][x].domain[id_min];
            variables[y][x].assignement = variables[y][x].domain[id_min];
            assigned_variables.push(min_idx); //push the variable into stack, which will be used for backtrack (or DFS)
            repeating_list.push_back(cur_state); //make this state into the repeat_list
            *chosen_cell = 9 * y + x;

            updateDomain(cur_state); //Every time modify the assignment update the domain

            return false;
        }

        count++;
    }

    if (goalCheck(cur_state))
    {
        printf("find the goal\n");
        return true;
    }
    else
    {
        int available_assignemnt = 0; //an indicatior whether there are possible varaibles to be re-assigned
        while (available_assignemnt == 0) {
            int cur_id = assigned_variables.top();
            int y = cur_id / 9;
            int x = cur_id % 9;
            variables[y][x].assignement = 0;
            cur_state.values[y][x] = 0;
            updateDomain(cur_state);
            for (int i = 0; i < variables[y][x].domain.size(); i++)
            {
                State temp_state;
                temp_state = cur_state;
                temp_state.values[y][x] = variables[y][x].domain[i];
                if (std::find(repeating_list.begin(), repeating_list.end(), temp_state) == repeating_list.end()) //if not in the repeating list
                {
                    cur_state = temp_state;
                    variables[y][x].assignement = variables[y][x].domain[i];
                    repeating_list.push_back(cur_state);
                    available_assignemnt = 1;
                    *chosen_cell = cur_id;
                    break; //get out of the current varaible assignment
                }
            }

            if (available_assignemnt == 0) //if all the domain values have been tried for current variable
            {

                assigned_variables.pop();

            }
        }

        return false;
    }

    return false;

}



/*Back Track to solve the proble*/
bool CSP::backTrack(int* chosen_cell)
{



    for (int i = 0; i < 81; i++)
    {
        int y = i / 9;
        int x = i % 9;


        /*If there is any varable has not been assigned yet, assign it and break*/
        if (cur_state.values[y][x] == 0)
        {

            /*Find the smalles number in domain to assign it. Here no update domain for bracktrack*/
            int id_min = 0;
            cur_state.values[y][x] = variables[y][x].domain[id_min];
            variables[y][x].assignement = variables[y][x].domain[id_min];
            assigned_variables.push(i); //push the variable into stack, which will be used for backtrack (or DFS)
            repeating_list.push_back(cur_state); //make this state into the repeat_list
            *chosen_cell = 9 * y + x;
            return false;

        }
    }

    /*If all the the variable are assigned*/
    {
        if (assigned_variables.size() == 0)//reset all the variables if there are no any varaibles assigned yet
        {
            for (int i = 0; i < 81; i++)
            {
                assigned_variables.push(i);
            }
        }

        if (goalCheck(cur_state))
        {
            printf("find the goal\n");
            return true;
        }
        else
        {
            int available_assignemnt = 0; //an indicatior whether there are possible varaibles to be re-assigned
            while (available_assignemnt == 0) {
                int cur_id = assigned_variables.top();
                int y = cur_id / 9;
                int x = cur_id % 9;


                for (int i = 0; i < variables[y][x].domain.size(); i++)
                {
                    State temp_state;
                    temp_state = cur_state;
                    temp_state.values[y][x] = variables[y][x].domain[i];
                    if (std::find(repeating_list.begin(), repeating_list.end(), temp_state) == repeating_list.end()) //if not in the repeating list
                    {
                        cur_state = temp_state;
                        variables[y][x].assignement = variables[y][x].domain[i];
                        repeating_list.push_back(cur_state);
                        available_assignemnt = 1;
                        *chosen_cell = cur_id;
                        break; //get out of the current varaible assignment
                    }
                }

                if (available_assignemnt == 0) //if all the domain values have been tried for current variable
                {
                    variables[y][x].assignement = 0;
                    cur_state.values[y][x] = 0;
                    assigned_variables.pop();

                }
            }

            return false;
        }
    }
}
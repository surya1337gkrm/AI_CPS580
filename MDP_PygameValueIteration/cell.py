import random
class Cell:
    def __init__(self,x,y):
        self.q_values=[0.0,0.0,0.0,0.0]
        self.location=(x,y)
        self.state_value=max(self.q_values)

states=[]
for j in range(0,3):
    l=[]
    for i in range(0,4):
        l.append(Cell(i,j))
    states.append(l)
states[0][3].state_value=1
states[1][3].state_value=-1


#Uncomment this code and run this file to understand looping over the states data.
# for i in range(0,3):
#     for j in range(0,4):
#         print(i,j,states[i][j].location,states[i][j].state_value)
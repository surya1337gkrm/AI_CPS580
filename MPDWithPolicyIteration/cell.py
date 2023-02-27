import random
class Cell:
    def __init__(self,x,y):
        self.q_values=[0.0,0.0,0.0,0.0]
        self.location=(x,y)
        self.state_value=max(self.q_values)
        self.policy=0

states=[]
for j in range(0,3):
    l=[]
    for i in range(0,4):
        cell=Cell(i,j)
        if ((i == 1 and j == 1) or (i == 3 and j == 0) or (i == 3 and j == 1)):
            pass
        else:
            cell.policy=random.randint(0,3)
        l.append(cell)
    states.append(l)
states[0][3].state_value=1
states[1][3].state_value=-1



# for i in range(0,3):
#     for j in range(0,4):
#         print(i,j,states[i][j].location,states[i][j].state_value)
# policies=[]
# for j in range(0,3):
#     l=[]
#     for i in range(0,4):
#         cell=Cell(i,j)
#         cell.policy=random.randint(0,3)
#         l.append(cell)
#     policies.append(l)
# policies[0][3].state_value=1
# policies[1][3].state_value=-1
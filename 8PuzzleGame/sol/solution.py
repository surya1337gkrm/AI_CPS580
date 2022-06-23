from copy import deepcopy
from collections import deque
from game.Node import Node
from queue import PriorityQueue
import time

childEle={
    0:[1,3],
    1:[0,2,4],
    2:[1,5],
    3:[0,4,6],
    4:[1,3,5,7],
    5:[2,4,8],
    6:[3,7],
    7:[4,6,8],
    8:[5,7]
}
goalState=[0,1,2,3,4,5,6,7,8]

#here you need to implement the Breadth First Search Method

def mapState(state):
    return ''.join(str(i) for i in state)

def goalTesting(node):
    if node.puzzle == goalState :
        print('Solution Found')
        return True
    return False    

def backtracing(node):
    path=[]
    path.append(node.puzzle.index(8))
    parent=node.parent
    if parent !=None:
        while parent:
            path.append(parent.puzzle.index(8))
            parent=parent.parent       
    if len(path)<10:
        print(path)
    print('Number of Moves required : ',len(path)-1)
    path.reverse()   
    return path

def getChild(ele,child):
    childNode=Node(ele,None,ele.cost+1)
    curr_state=deepcopy(ele.puzzle)
    currIdx8=curr_state.index(8)
    curr_state[currIdx8],curr_state[child]=curr_state[child],curr_state[currIdx8]
    childNode.puzzle=curr_state
    childNode.children=childEle[childNode.puzzle.index(8)]   
    return childNode 


def bfs(puzzle):
    start=time.time()
    list = []
    visitedNode=set()

    initNode=Node(None,puzzle,0)
    idx8=puzzle.index(8)
    initNode.children=childEle[idx8]

    queue=deque([initNode])

    while queue:
       
        frontEle=queue.popleft()
        if(goalTesting(frontEle)):
            list=backtracing(frontEle)
            print('BFS: ',(time.time()-start)*1000,' ms')
            return list

        if mapState(frontEle.puzzle) not in visitedNode:   
            visitedNode.add(mapState(frontEle.puzzle))
           

        paths=frontEle.children
        for child in paths:
            childNode=getChild(frontEle,child)

            if goalTesting(childNode):
                list=backtracing(childNode)
                print('BFS: ',(time.time()-start)*1000,' ms')
                return list
            
            else:    
                if(mapState(childNode.puzzle) not in visitedNode):
                    visitedNode.add(mapState(childNode.puzzle))
                    queue.append(childNode)

#here you need to implement the Depth First Search Method
def dfs(puzzle):
    list = []
    visitedNode=set()

    initNode=Node(None,puzzle,0)
    idx8=puzzle.index(8)
    initNode.children=childEle[idx8]
   

    stack=deque([initNode])
    while stack:
        topEle=stack.pop()
 
        if goalTesting(topEle):
            list=backtracing(topEle)
            return list

        if mapState(topEle.puzzle) not in visitedNode :

            visitedNode.add(mapState(topEle.puzzle))

            paths=topEle.children

            for child in paths:
                childNode=getChild(topEle,child)

                if childNode not in stack:
                    stack.append(childNode)
                    if goalTesting(childNode):
                        list=backtracing(childNode)
                        return list


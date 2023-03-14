# This is the only file you need to work on. You do NOT need to modify other files
import collections
import time

# Below are the functions you need to implement. For the first project, you only need to finish implementing bfs() and dfs()
import game.Node


class FringeNode:
    def __init__(self, value, parent, move, hCost, gCost):
        self.value = value
        self.parent = parent
        self.children = []
        self.move = move
        self.hCost = hCost
        self.gCost = gCost
        self.status = 1


class Tree:

    def createNode(self, data, parent, move, cost):
        return game.Node.Node(data, parent, move, cost)

    def createFringeNode(self, value, parent, move, hCost, gCost):
        return FringeNode(value, parent, move, hCost, gCost)

    def insert(self, data, parent, move, cost):
        if parent is None:
            return self.createNode(data, None, None, None)
        else:
            tempNode = game.Node.Node(data, parent, move, cost)
            parent.children.append(tempNode)
        return tempNode

    def insertFringeNode(self, value, parent, move, hCost, gCost):
        if parent is None:
            return self.createNode(value, parent, move, hCost, gCost)
        else:
            temp = FringeNode(value, parent, move, hCost, gCost)
            parent.children.append(temp)
            return temp


arr = []
fringe = []
fringeTemp = []
tree = Tree()
goalState = "012345678"


def createTree(state):
    arr.clear()
    arr.append(state)
    root = tree.insert(state, None, None, None)
    return root




def generateChildren(state, node):
    idx = getIndex(state)
    if idx == 0:
        newState1 = swapPosition(0, 1, state)
        if newState1 not in arr:
            arr.append(newState1)
            tree.insert(newState1, node, 1, None)

        newState2 = swapPosition(0, 3, state)
        if newState2 not in arr:
            arr.append(newState2)
            tree.insert(newState2, node, 3, None)
    if idx == 1:
        newState1 = swapPosition(1, 0, state)
        if newState1 not in arr:
            arr.append(newState1)
            tree.insert(newState1, node, 0, None)

        newState2 = swapPosition(1, 2, state)
        if newState2 not in arr:
            arr.append(newState2)
            tree.insert(newState2, node, 2, None)

        newState3 = swapPosition(1, 4, state)
        if newState3 not in arr:
            arr.append(newState3)
            tree.insert(newState3, node, 4, None)

    if idx == 2:
        newState1 = swapPosition(2, 1, state)
        if newState1 not in arr:
            arr.append(newState1)
            tree.insert(newState1, node, 1, None)

        newState2 = swapPosition(2, 5, state)
        if newState2 not in arr:
            arr.append(newState2)
            tree.insert(newState2, node, 5, None)

    if idx == 3:
        newState1 = swapPosition(3, 0, state)
        if newState1 not in arr:
            arr.append(newState1)
            tree.insert(newState1, node, 0, None)

        newState2 = swapPosition(3, 4, state)
        if newState2 not in arr:
            arr.append(newState2)
            tree.insert(newState2, node, 4, None)

        newState3 = swapPosition(3, 6, state)
        if newState3 not in arr:
            arr.append(newState3)
            tree.insert(newState3, node, 6, None)

    if idx == 4:
        newState1 = swapPosition(4, 1, state)
        if newState1 not in arr:
            arr.append(newState1)
            tree.insert(newState1, node, 1, None)

        newState2 = swapPosition(4, 3, state)
        if newState2 not in arr:
            arr.append(newState2)
            tree.insert(newState2, node, 3, None)

        newState3 = swapPosition(4, 5, state)
        if newState3 not in arr:
            arr.append(newState3)
            tree.insert(newState3, node, 5, None)

        newState4 = swapPosition(4, 7, state)
        if newState4 not in arr:
            arr.append(newState4)
            tree.insert(newState4, node, 7, None)

    if idx == 5:
        newState1 = swapPosition(5, 2, state)
        if newState1 not in arr:
            arr.append(newState1)
            tree.insert(newState1, node, 2, None)

        newState2 = swapPosition(5, 4, state)
        if newState2 not in arr:
            arr.append(newState2)
            tree.insert(newState2, node, 4, None)

        newState3 = swapPosition(5, 8, state)
        if newState3 not in arr:
            arr.append(newState3)
            tree.insert(newState3, node, 8, None)

    if idx == 6:
        newState1 = swapPosition(6, 3, state)
        if newState1 not in arr:
            arr.append(newState1)
            tree.insert(newState1, node, 3, None)

        newState2 = swapPosition(6, 7, state)
        if newState2 not in arr:
            arr.append(newState2)
            tree.insert(newState2, node, 7, None)

    if idx == 7:
        newState1 = swapPosition(7, 6, state)
        if newState1 not in arr:
            arr.append(newState1)
            tree.insert(newState1, node, 6, None)

        newState2 = swapPosition(7, 4, state)
        if newState2 not in arr:
            arr.append(newState2)
            tree.insert(newState2, node, 4, None)

        newState3 = swapPosition(7, 8, state)
        if newState3 not in arr:
            arr.append(newState3)
            tree.insert(newState3, node, 8, None)

    if idx == 8:
        newState1 = swapPosition(8, 5, state)
        if newState1 not in arr:
            arr.append(newState1)
            tree.insert(newState1, node, 5, None)

        newState2 = swapPosition(8, 7, state)
        if newState2 not in arr:
            arr.append(newState2)
            tree.insert(newState2, node, 7, None)

#  returns minimum cost node from the fringe
def getMinFromFringe():
    queue = collections.deque(sorted(list(fringeTemp), key=lambda node: node.gCost+node.hCost))
    return queue.popleft()


# generates children for a node in A* search
def generateChildrenInFringe(state, node):
    idx = getIndex(state)
    children = []
    if idx == 0:
        newState1 = swapPosition(0, 1, state)
        if newState1 not in arr:
            arr.append(newState1)
            tempNode = tree.insertFringeNode(newState1, node, 1, getHCost(newState1), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState2 = swapPosition(0, 3, state)
        if newState2 not in arr:
            arr.append(newState2)
            tempNode = tree.insertFringeNode(newState2, node, 3, getHCost(newState2), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

    if idx == 1:
        newState1 = swapPosition(1, 0, state)
        if newState1 not in arr:
            arr.append(newState1)
            tempNode = tree.insertFringeNode(newState1, node, 0, getHCost(newState1), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState2 = swapPosition(1, 4, state)
        if newState2 not in arr:
            arr.append(newState2)
            tempNode = tree.insertFringeNode(newState2, node, 4, getHCost(newState2), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState3 = swapPosition(1, 2, state)
        if newState3 not in arr:
            arr.append(newState3)
            tempNode = tree.insertFringeNode(newState3, node, 2, getHCost(newState3), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

    if idx == 2:
        newState1 = swapPosition(2, 1, state)
        if newState1 not in arr:
            arr.append(newState1)
            tempNode = tree.insertFringeNode(newState1, node, 1, getHCost(newState1), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState2 = swapPosition(2, 5, state)
        if newState2 not in arr:
            arr.append(newState2)
            tempNode = tree.insertFringeNode(newState2, node, 5, getHCost(newState2), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

    if idx == 3:
        newState1 = swapPosition(3, 0, state)
        if newState1 not in arr:
            arr.append(newState1)
            tempNode = tree.insertFringeNode(newState1, node, 0, getHCost(newState1), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState2 = swapPosition(3, 4, state)
        if newState2 not in arr:
            arr.append(newState2)
            tempNode = tree.insertFringeNode(newState2, node, 4, getHCost(newState2), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState3 = swapPosition(3, 6, state)
        if newState3 not in arr:
            arr.append(newState3)
            tempNode = tree.insertFringeNode(newState3, node, 6, getHCost(newState3), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

    if idx == 4:
        newState1 = swapPosition(4, 1, state)
        if newState1 not in arr:
            arr.append(newState1)
            tempNode = tree.insertFringeNode(newState1, node, 1, getHCost(newState1), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState2 = swapPosition(4, 3, state)
        if newState2 not in arr:
            arr.append(newState2)
            tempNode = tree.insertFringeNode(newState2, node, 3, getHCost(newState2), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState3 = swapPosition(4, 5, state)
        if newState3 not in arr:
            arr.append(newState3)
            tempNode = tree.insertFringeNode(newState3, node, 5, getHCost(newState3), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState4 = swapPosition(4, 7, state)
        if newState4 not in arr:
            arr.append(newState4)
            tempNode = tree.insertFringeNode(newState4, node, 7, getHCost(newState4), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

    if idx == 5:
        newState1 = swapPosition(5, 2, state)
        if newState1 not in arr:
            arr.append(newState1)
            tempNode = tree.insertFringeNode(newState1, node, 2, getHCost(newState1), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState2 = swapPosition(5, 4, state)
        if newState2 not in arr:
            arr.append(newState2)
            tempNode = tree.insertFringeNode(newState2, node, 4, getHCost(newState2), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState3 = swapPosition(5, 8, state)
        if newState3 not in arr:
            arr.append(newState3)
            tempNode = tree.insertFringeNode(newState3, node, 8, getHCost(newState3), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

    if idx == 6:
        newState1 = swapPosition(6, 3, state)
        if newState1 not in arr:
            arr.append(newState1)
            tempNode = tree.insertFringeNode(newState1, node, 3, getHCost(newState1), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState2 = swapPosition(6, 7, state)
        if newState2 not in arr:
            arr.append(newState2)
            tempNode = tree.insertFringeNode(newState2, node, 7, getHCost(newState2), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

    if idx == 7:
        newState1 = swapPosition(7, 6, state)
        if newState1 not in arr:
            arr.append(newState1)
            tempNode = tree.insertFringeNode(newState1, node, 6, getHCost(newState1), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)


        newState2 = swapPosition(7, 4, state)
        if newState2 not in arr:
            arr.append(newState2)
            tempNode = tree.insertFringeNode(newState2, node, 4, getHCost(newState2), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState3 = swapPosition(7, 8, state)
        if newState3 not in arr:
            arr.append(newState3)
            tempNode = tree.insertFringeNode(newState3, node, 8, getHCost(newState3), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

    if idx == 8:
        newState1 = swapPosition(8, 5, state)
        if newState1 not in arr:
            arr.append(newState1)
            tempNode = tree.insertFringeNode(newState1, node, 5, getHCost(newState1), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

        newState2 = swapPosition(8, 7, state)
        if newState2 not in arr:
            arr.append(newState2)
            tempNode = tree.insertFringeNode(newState2, node, 7, getHCost(newState2), node.gCost + 1)
            fringe.append(tempNode)
            fringeTemp.append(tempNode)
            children.append(tempNode)

    return children

#  returns index of 8
def getIndex(value):
    return value.index("8")

#  swaps the positions of a with b in data
def swapPosition(a, b, data):
    s = list(data)
    s[a], s[b] = s[b], s[a]
    return ''.join(s)

#  to return the Heuristic cost
def getHCost(state):
    return 8 - getIndex(state)


# here you need to implement the Breadth First Search Method
def bfs(puzzle):
    startTime = time.time()
    moves = []
    list = []
    queue = []
    count = 0
    strlist = [str(i) for i in puzzle]
    puzzle = ''.join(strlist)
    goalStateNode = None
    root = createTree(puzzle)
    queue.append(root)
    while queue:
        temp = queue.pop(0)
        if temp.value == goalState:
            goalStateNode = temp
            list.append(goalStateNode)
            break
        else:
            count = count + 1
            generateChildren(temp.value, temp)
            for item in temp.children:
                queue.append(item)
    while goalStateNode.parent:
        list.append(goalStateNode.parent)
        goalStateNode = goalStateNode.parent
    for item in list:
        moves.append(item.move)
    moves.reverse()
    moves.pop(0)
    endTime = time.time()
    print("Time taken to perform BFS is ")
    print(str((endTime - startTime)*1000) + " ms")
    print("number of nodes parsed is "+str(count))
    return moves


# here you need to implement the Depth First Search Method
def dfs(puzzle):
    startTime = time.time()
    count = 0
    moves = []
    list = []
    stack = []
    strlist = [str(i) for i in puzzle]
    puzzle = ''.join(strlist)
    goalStateNode = None
    root = createTree(puzzle)
    stack.append(root)
    while goalStateNode == None:
        count = count + 1
        temp = stack.pop()
        if temp.value == goalState:
            print(temp.value)
            goalStateNode = temp
            list.append(goalStateNode)
            break
        else:
            generateChildren(temp.value, temp)
            for item in temp.children:
                stack.append(item)
    while goalStateNode.parent:
        list.append(goalStateNode.parent)
        goalStateNode = goalStateNode.parent
    for item in list:
        moves.append(item.move)
    moves.reverse()
    moves.pop(0)
    endTime = time.time()
    print("Time taken to perform dfs is ")
    print(endTime - startTime)
    print("Traversed through " +str(count)+ " Nodes")
    return moves


# This is to perform A* search
def astar(puzzle):
    count = 0  # to store number of nodes created
    startTime = time.time()
    moves = []
    arr.clear()
    fringe.clear()
    goalStateNode = None
    strlist = [str(i) for i in puzzle]
    puzzle = ''.join(strlist)
    arr.append(puzzle)

    root = tree.createFringeNode(puzzle, None, 0, getHCost(puzzle), 0)  # creating root node with initial data
    fringe.append(root)  # appending to fringe
    fringeTemp.append(root)
    while goalStateNode is None:  # to create a tree until goal node is reached
        fringeNode = getMinFromFringe()  # gets node from fringe with minimum cost
        count = count + 1
        children = generateChildrenInFringe(fringeNode.value, fringeNode)  # expands the node
        fringeTemp.remove(fringeNode)  # removes expanded node from fringe
        for item in children:  # check for goal node
            if item.value == goalState:
                goalStateNode = item
                moves.append(goalStateNode.move)
                break

    while goalStateNode.parent:  # to capture the moves to goal state
        moves.append(goalStateNode.parent.move)
        goalStateNode = goalStateNode.parent

    moves.reverse()
    moves.pop(0)
    endTime = time.time()
    print("Time taken to perform A* Search is")
    print(str((endTime - startTime)*1000) + " ms")
    print("parsed through " + str(count))
    return moves

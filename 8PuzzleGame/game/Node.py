import time
from collections import deque
import heapq
import math

class Node:
    def __init__(self, value, parent, move, cost):
        self.parent = parent
        self.value = value
        self.children = []
        self.move = move
        self.cost = cost


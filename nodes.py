class Node:
    def __init__(self, x, y, cost):
        self.position = (x, y)
        self.cost = cost
        self.children = []

"""

"""
def step(stack, grid):
    node = stack[-1]
    #down
    
    #right

    #left

    #up

"""

"""
def arrayToTree(filename: str):
    #open the file as a 2d array
    maze = open(filename, "r").readlines()

    #find the starting node in the top row
    for n, cell in enumerate(maze[0]):
        if cell == "-":
            startpoint = (n, 0)

    #create a stack
    stack = [startpoint]
    #step through each possible node
    while stack:
        step(stack)

    print(startpoint)
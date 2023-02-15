#by taking the direct distance from the entrance to the exit node, 
#all shorter paths can be eliminated.

class Node:
    def __init__(self, x, y):
        self.children = []
        self.position = (x, y)

    def addChild(self, child):
        self.children.append(child)

    def popChild(self, child):
        self.children.remove(child)

    def PrintTree(self):
        print(self.value)
        print("Children" + self.children)

"""
Arguments: the name of a text file containing a maze.

Output: a tree with 
"""
def createTree(filename: str) -> Node:
    maze = open(filename, "r").readlines()
    
    
"""

"""
def dfs(start: int, end: int, node: Node) -> list:
    pass

"""

"""
def mazeSolver(filename: str) -> list:
    pass
    #create the 2d array of the maze
    #find the starting node
    #find the end node

if __name__ == "__main__":
    print("Hi")
    
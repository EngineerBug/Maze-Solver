'''
Attributes:
    - position: the x and y co-ordanates of the node in the maze
    - cost: the distance in nodes from the start point
    - parent: the previous node in the tree
'''
class Node:
    def __init__(self, x, y, cost):
        self.position = {'x': x, 'y': y }
        self.cost = cost
        self.parent = None

'''
Arguments:
    - node: a node in the tree 
    - grid: the 2d maze

Check the four positions adjacent to the argument node.
If they are marked as a path ('-'), add them to the tree.

Output: a list of neighbouring nodes to the input node
'''
def step(node: Node, grid: list) -> list:
    #create a list of new nodes to add to the stack
    newNodes = []
    #save time by saving the current co-ords
    x = node.position['x']
    y = node.position['y']
    #up
    if grid[y-1][x] == '-':
        newNodes.append( Node(x, y-1, node.cost+1) )
    #left
    if grid[y][x-1] == '-':
        newNodes.append(Node(x-1, y, node.cost+1))
    #right
    if grid[y][x+1] == '-':
        newNodes.append(Node(x+1, y, node.cost+1))
    #down
    if grid[y+1][x] == '-':
        newNodes.append(Node(x, y+1, node.cost+1))
    
    return newNodes

'''
Arguments:
    - text: a text file which needs to be turned into a 2d array

Output:
    - a 2d array containing only '-' and '#'
'''
def mazePrep(text: list) -> list:
    maze = []
    for row in text:
        if row.split() != []:
            maze.append(row.split())

    return maze

if __name__ == "__main__":
    print(mazePrep(open('./mazes/maze-easy.txt', 'r').readlines()))
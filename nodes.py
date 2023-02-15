'''

'''
class Node:
    def __init__(self, x, y, cost):
        self.position = {'x': x, 'y': y }
        self.cost = cost
        self.parent = None

'''

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

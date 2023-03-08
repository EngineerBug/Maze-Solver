from time import perf_counter
from nodes import Node, step, mazePrep

def heuristicSearch(filename: str) -> None:
    timestart = perf_counter()

    graph = makeGraph(filename)
    #perform the elimination algorithm
    heuristicgraph = eliminate(graph[0], graph[2])
    #perform the search algorithm
    print (heuristicgraph)

    timestop = perf_counter()

def eliminate(startpoint: Node, heuristic: int) -> None:
    queue = [startpoint]
    while queue:
        currentNode = queue.pop(0)
        #for each child of the current node, remove all leaves that have a cost less than the heuristic
        for child in currentNode.children:
            if child.cost < heuristic and child.children == []:
                currentNode.children.remove(child)
            else:
                queue.append(child)
        #if the children are all eliminated, this node should be reevaluated against the heuristic
        if currentNode.children == []:
            queue.append(currentNode.parent)
    


'''
Arguments: the name of the file containing the maze

This method constructs a full graph of the maze.


Output: a tuple containing the start node, the end node, and the heuristic distance between them
'''
def makeGraph(filename: str) -> tuple:
    text = open(filename, 'r').readlines()      #open the file as a list of strings
    maze = mazePrep(text)                       #turn the list into a valid 2d maze

    #find the starting node in the top row
    for n, cell in enumerate(maze[0]):
        if cell == '-':
            startpoint = Node(n, 0, 1)

    queue = [startpoint]                        #create a queue to store unvisited nodes
    
    while queue:                                #step through each possible node
        currentNode = queue.pop(0)              #remove the front node from the queue
        maze[currentNode.position['y']][currentNode.position['x']] = 'x' #mark currentNode as visited

        #check if the current node is the goal node
        if currentNode.position['y'] == len(maze)-1:
            lastNode = currentNode
            minlength = ((startpoint.position['x'] - lastNode.position['x'])**2 + (startpoint.position['y'] - lastNode.position['y'])**2 )**0.5

        newNodes = step(currentNode, maze)      #find all the children of the node
        currentNode.children.append(newNodes)   #add the children to the currentNode's children list
        queue.extend(newNodes)                  #add the children to the queue

        #so that the path can be found, give each node the identity of its parent
        for node in newNodes:
            node.parent = currentNode

    print('No solution was found.')
    return (startpoint, lastNode, minlength)

if __name__ == '__main__':
    default = heuristicSearch('./mazes/tests/default.txt')
from time import perf_counter
from nodes import Node, step, mazePrep
from queue import PriorityQueue

'''
Arguments: the name of a text file containing a maze

Calculate the start and end points of the maze.
Create a priority queue to store unvisited nodes.
Create a count to keep track of the number of nodes visited.
While there is a node in the nodeList:
    Find the node with the lowest heuristic value and mark it as the next node to be visited
    If the node is the goal node (indicated by it's self.position['y'] value)
        Print metrics about the performance

Output: the number of nodes visited, the length of the solution path, and the solution path
'''
def heuristicSearch(filename: str) -> None:
    timestart = perf_counter()
    text = open(filename, 'r').readlines()
    maze = mazePrep(text)

    #find the exit node in the bottom row
    for n, cell in enumerate(maze[-1]):
        if cell == '-':
            endpoint = Node(n, len(maze)-1, None)
    #find the starting node in the top row
    for n, cell in enumerate(maze[0]):
        if cell == '-':
            startpoint = Node(n, 0, 1)
            startpoint.calcHeuristic(endpoint)
    
    count = 1                                           #create a count of total nodes visited
    nodeList = PriorityQueue()                          #create a nodeList to store unvisited nodes
    nodeList.put(startpoint)    #add the starting node to the nodeList

    while nodeList:
        #find the node with the lowest heuristic value and mark it as the next node to be visited
        currentNode = nodeList.get(0)
        maze[currentNode.position['y']][currentNode.position['x']] = 'x'

        #since the only '-' character on the bottom line is stated to be the exit, the check is quite simple
        if currentNode.position['y'] == len(maze)-1:
            timestop = perf_counter()
            solutionLength = currentNode.cost
            print('Exit found for ' + filename)
            print('Time: ' + str( round((timestop-timestart), 5)) + 'secs')
            print('Total Nodes visited: ' + str(count))
            print('Solution Length: ' + str(solutionLength))

            pathNode = currentNode
            path = []
            #calculate the solution path:
            while pathNode.cost != 1:
                path.append('(' + str(pathNode.position['x']) + ',' + str(pathNode.position['y']) + ')')
                pathNode = pathNode.parent

            #write the solution path to a file in lines of 20 coordinates
            path.append('(' + str(startpoint.position['x']) + ',' + str(startpoint.position['y']) + ')')
            path.reverse()
            with open(filename+'-output.txt', 'w') as f:
                for n, point in enumerate(path):
                    if(n % 20 == 0):
                        f.write(point + '\n')
                    else:
                        f.write(point + ' ')

            return (count, solutionLength, path)

        #if the node is not the goal node, find the nodes that can be reached from it
        newNodes = step(currentNode, maze)
        count += 1

        #so that the path can be found, give each node the identity of its parent and the heuristic value
        for node in newNodes:
            nodeList.put(node)
            node.parent = currentNode
            node.calcHeuristic(endpoint)
    
    #if the nodeList is empty, no solution was found
    print('No exit found for ' + filename)

if __name__ == '__main__':
    #heuristicSearch('./mazes/tests/default.txt')
    #heuristicSearch('./mazes/tests/dead-ends.txt')
    #heuristicSearch('./mazes/tests/change-direction.txt')
    heuristicSearch('./mazes/maze-Easy.txt')
    heuristicSearch('./mazes/maze-Medium.txt')
    heuristicSearch('./mazes/maze-Large.txt')
    heuristicSearch('./mazes/maze-VLarge.txt')
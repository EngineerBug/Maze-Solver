from nodes import Node, step

'''

'''
def bfs(filename: str):
    #open the file as a 2d array
    maze = open(filename, 'r').readlines()

    #find the starting node in the top row
    for n, cell in enumerate(maze[0]):
        if cell == '-':
            startpoint = Node(n, 0, 1)

    count = 1                                   #create a count of total nodes visited
    queue = [startpoint]                        #create a queue to store unvisited nodes
    
    while queue:                                #step through each possible node
        currentNode = queue.pop(0)              #remove the front node from the queue
        print( 'x ' + str(currentNode.position['x']) + ', y ' + str(currentNode.position['y']))

        #since the only '-' character on the bottom line is stated to be the exit, the check is quite simple
        if currentNode.position['y'] == len(maze)-1:
            print('Exit found!')
            print('Time: [pending]')
            print('Nodes visited: ' + str(count))
            print('Solution Length: ' + str(currentNode.cost))
            
            pathNode = currentNode
            path = []
            #calculate the solution path:
            while pathNode.cost != 1:
                path.append('(' + str(pathNode.position['x']) + ',' + str(pathNode.position['y']) + ')')
                pathNode = pathNode.parent      #point to the previous node

            print('The path to the goal:' + str(path))

            return

        newNodes = step(currentNode, maze)      #find all the children of the node
        queue.extend(newNodes)                  #add the children to the queue
        count += 1                              #increment the count

        #so that the path can be found, give each node the identity of its parent
        for node in newNodes:
            node.parent = currentNode

    print('No solution was found.')
    return


if __name__ == '__main__':
    bfs('./mazes/maze-test.txt')
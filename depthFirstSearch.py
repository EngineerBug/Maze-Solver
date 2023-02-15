from nodes import Node, step, mazePrep

'''

'''
def dfs(filename: str):
    text = open(filename, 'r').readlines()      #open the file as a list of strings
    maze = mazePrep(text)                       #turn the list into a valid 2d maze

    #find the starting node in the top row
    for n, cell in enumerate(maze[0]):
        if cell == '-':
            startpoint = Node(n, 0, 1)

    count = 1                                   #create a count of total nodes visited
    stack = [startpoint]                        #create a stack to store unvisited nodes
    
    while stack:                                #step through each possible node
        currentNode = stack.pop()               #remove the top node from the stack
        maze[currentNode.position['y']][currentNode.position['x']] = 'x'
        #print( 'x ' + str(currentNode.position['x']) + ', y ' + str(currentNode.position['y']))

        #since the only '-' character on the bottom line is stated to be the exit, the check is quite simple
        if currentNode.position['y'] == len(maze)-1:
            print('Exit found!')
            print('Time: [pending]')
            print('Total Nodes visited: ' + str(count))
            print('Solution Length: ' + str(currentNode.cost))
            
            pathNode = currentNode
            path = []
            #calculate the solution path:
            while pathNode.cost != 1:
                path.append('(' + str(pathNode.position['x']) + ',' + str(pathNode.position['y']) + ')')
                pathNode = pathNode.parent      #point to the previous node
    
            path.append('(' + str(startpoint.position['x']) + ',' + str(startpoint.position['y']) + ')')
            path.reverse()
            print('The path to the goal:' + str(path))

            return

        newNodes = step(currentNode, maze)      #find all the children of the node
        stack.extend(newNodes)                  #add the children to the stack
        count += 1                              #increment the count

        #so that the path can be found, give each node the identity of its parent
        for node in newNodes:
            node.parent = currentNode

    print('No solution was found.')
    return


if __name__ == '__main__':
    #dfs('./mazes/tests/default.txt')
    #dfs('mazes/tests/change-direction.txt')
    #dfs('./mazes/tests/dead-ends.txt')
    dfs('./mazes/maze-Easy.txt')
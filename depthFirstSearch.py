from nodes import Node, step, mazePrep

'''
Arguments:
    - filename: a string pointing to a '.txt' file containing a maze layout

Read in a text file and turn it into a 2d array (with nodes.mazePrep())
Find the starting node which we know is in the top row.
Create a stack to store nodes and a node counter.
While the stack is not empty:
    Remove the top node from the stack and mark it as visited
    If the node is the goal node (indicated by it's self.position['y'] value)
        Print metrics about the performance
        Print the path.
        Return
    Else
        Find all the children of the current node and add them to the stack
        Assign the children their parent.
    If the stack is empty and the goal has not been found, tell the user.
    Return

Output: 
    - The total number of nodes visited
    - the number of nodes in the solution
'''
def dfs(filename: str) -> tuple:
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
        maze[currentNode.position['y']][currentNode.position['x']] = 'x' #mark currentNode as visited
        #print( 'x ' + str(currentNode.position['x']) + ', y ' + str(currentNode.position['y']))

        #since the only '-' character on the bottom line is stated to be the exit, the check is quite simple
        if currentNode.position['y'] == len(maze)-1:
            solutionLength = currentNode.cost
            print('Exit found!')
            print('Time: [pending]')
            print('Total Nodes visited: ' + str(count))
            print('Solution Length: ' + str(solutionLength))
            
            pathNode = currentNode
            path = []
            #calculate the solution path:
            while pathNode.cost != 1:
                path.append('(' + str(pathNode.position['x']) + ',' + str(pathNode.position['y']) + ')')
                pathNode = pathNode.parent      #point to the previous node
    
            path.append('(' + str(startpoint.position['x']) + ',' + str(startpoint.position['y']) + ')')
            path.reverse()
            print('The path to the goal:' + str(path))

            return (count, solutionLength)

        newNodes = step(currentNode, maze)      #find all the children of the node
        stack.extend(newNodes)                  #add the children to the stack
        count += 1                              #increment the count

        #so that the path can be found, give each node the identity of its parent
        for node in newNodes:
            node.parent = currentNode

    print('No solution was found.')
    return (0, 0)


if __name__ == '__main__':
    #dfs('./mazes/tests/default.txt')
    #dfs('mazes/tests/change-direction.txt')
    #dfs('./mazes/tests/dead-ends.txt')
    dfs('./mazes/maze-Easy.txt')
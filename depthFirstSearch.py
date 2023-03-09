from time import perf_counter
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
    - the ordered list of nodes leading from the start ot the goal
'''
def dfs(filename: str) -> tuple:
    timestart = perf_counter()                  #begin the stopwatch for the program
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

        #since the only '-' character on the bottom line is stated to be the exit, the check is quite simple
        if currentNode.position['y'] == len(maze)-1:
            timestop = perf_counter()            #stop the stopwatch for the program
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
                pathNode = pathNode.parent      #point to the previous node
    
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

        newNodes = step(currentNode, maze)      #find all the children of the node
        stack.extend(newNodes)                  #add the children to the stack
        count += 1                              #increment the count

        #so that the path can be found, give each node the identity of its parent
        for node in newNodes:
            node.parent = currentNode

    print('No solution was found.')
    return (0, 0, [])


if __name__ == '__main__':
    default = dfs('./mazes/tests/default.txt')
    assert default[0] == 10
    assert default[1] == 10
    assert len(default[2]) == default[1]
    direction = dfs('./mazes/tests/change-direction.txt')
    assert direction[0] == 15
    assert direction[1] == 15
    assert len(direction[2]) == direction[1]
    deadend = dfs('./mazes/tests/dead-ends.txt')
    assert deadend[0] == 10
    assert deadend[1] == 9
    assert len(deadend[2]) == deadend[1]
    
    dfs('./mazes/maze-Easy.txt')
    dfs('./mazes/maze-Medium.txt')
    dfs('./mazes/maze-Large.txt')
    dfs('./mazes/maze-VLarge.txt')
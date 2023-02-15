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

def arrayToTree(filename: str):
    #open the file as a 2d array
    maze = open(filename, "r").readlines()

    #find the starting node in the 
    for n, cell in enumerate(maze[0]):
        if cell == "-":
            startpoint = (n, 0)
    print(startpoint)

if __name__ == "__main__":
    arrayToTree("./mazes/maze-test.txt")
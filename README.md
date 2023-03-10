## Python Maze Solver

This is a maze solver using various search methods to solve a
maze imported from a text file.

#### Notes for use:

- nodes.py contains code vital to run other python scripts in this project so keep them in the same directory.
- The full path to the goal node will be output in the same folder as the input file, with the
  same name as the input file, but with the addition "-output.txt".
- At the bottom of each file there is a selection of commented lines to run different mazes.
- Running the project: 
    - Run in terminal: python3 \[filename\].py
    - Run in IDLE: Press F5
- All results can be viewed in the "results.png" or "results.xlsx" files.
- Please note that these results were obtained on a 3.1GHz quad-core processor.
- Github link: https://github.com/EngineerBug/Maze-Solver

![](results.png)

### Questions:

#### 1.1: Maze Solver as a Search Problem

A maze can be described as a set of positions, each of which have one-or-
more neighbours. The maze solver can be considered as a tree searcher, beginning
at an entrance node, where each node points to its neighbours and each
branch is every possible route to a dead end (or the exit). The maze solver
then descends the tree until the exit node is found.

#### 1.2.1: Depth-First-Search

A depth-first algorithm is a uniform method of searching a tree for the goal
node where each branch is searched before the next. Our maze
solver could use this method to search every possible path in the maze until
it finds a dead end, then go back to the last intersection and look down
another path.

#### 1.2.2: Using DFS to Solve maze-Easy.txt (Refer to depthFirstSearch.py)

Path:

(1,0), (1,1), (2,1), (3,1), (4,1), (5,1), 
(5,2), (5,3), (5,4), (5,5), (6,5), (7,5), 
(8,5), (8,6), (9,6), (10,6), (11,6), (12,6), 
(13,6), (14,6), (15,6), (16,6), (17,6), (17,7), 
(17,8), (18,8), (18,9)

#### 1.2.3: DFS Analysis (Refer to depthFirstSearch.py)

Time: about 0.00035 seconds (under a millisecond)

Total Nodes Visited: 46

Solution Length: 27

#### 1.2.4: DFS Generalisation (Refer to depthFirstSearch.py)

**maze-Medium**

Time: 0.00529secs (about 5 milliseconds)

Total Nodes visited: 2499

Solution Length: 339

**maze-Large**

Time: 0.04967secs (about 40 milliseconds)

Total Nodes visited: 10311

Solution Length: 1092

**maze-VLarge**

Time: 0.29635secs (about 300 milliseconds)

Total Nodes visited: 113365

Solution Length: 3737

#### 1.3.1: Alterative Algorithm

An alternative algorithm to solve the maze would be breadth-first-search, a
uninformed method of searching a tree where instead of choosing the next node
based on a stack, BFS chooses based on a queue. I.e. it searches the tree by
layer instead of by branch.

BFS has high time comlexity and space complexity, 
however BFS is complete and is guaranteed to return the optimal solution.
Therefore, I expect that BFS will return a shorter path than DFS.

#### 1.3.2: Implement Alternative Algorithm (Refer to breadthFirstSearch.py)

Implementing BFS is rather simple after DFS is already being used. I simply
replaced the stack used by DFS with a queue. I did this by changing the 
algorithm to take the first element of a list instead of the last.

#### 1.3.3: Analyse Alternative Algorithm (Refer to breadthFirstSearch.py)

**maze-Small**

Time: 0.00042secs (less than a millisecond)

Total Nodes visited: 86

Solution Length: 27

The path to the goal:

(1,0), (1,1), (2,1), (3,1), (4,1), (5,1), 
(5,2), (5,3), (5,4), (5,5), (6,5), (7,5), 
(8,5), (8,6), (9,6), (10,6), (11,6), (12,6), 
(13,6), (14,6), (15,6), (16,6), (17,6), (17,7), 
(17,8), (18,8), (18,9)

**maze-Medium**

Time: 0.30505secs (about 300 milliseconds)

Total Nodes visited: 143514

Solution Length: 321

**maze-Large**

Time: 0.33146secs (about 300 milliseconds)

Total Nodes visited: 162509

Solution Length: 974

**maze-VLarge**

Time: 4.06394secs (about 4000 milliseconds)

Total Nodes visited: 1603843

Solution Length: 3691

#### 1.3.4: Algorithm Comparison (Refer to breadthFirstSearch.py and depthFirstSearch.py)

The question of whether BFS 'improves' upon the performance of DFS depends 
on what is meant by improvement. BFS will give a better time only 
when the goal is close to the root of the search tree, which is not the 
case with a maze that starts in the top left and ends at the bottom right.

However, BFS consistently returned a shorter path to the goal node than DFS.
Therefore, it is arguable that if the maze were real, the time waisted by 
using BFS could be saved by the reduced time traversing the maze. 

#### Further Experimentation, Depth of Analysis and Discussion (Refer to nodes.py and heuristicSearch.py)

##### Messing With Previous Algorithms

I tested changing the order I added new nodes to the data-structure 
in each search algorithm, for BFS this did not greatly affect the performance, 
likely because BFS is almost guaranteed to check all of a nodes neighbours 
so the order is irrelevant.

The time complexity of DFS was greatly improved by prioritising neighbours, 
this is likely because it led the process to branches pointing toward where the exit 
was known to be (bottom right corner) and eliminated dead branches pointing 
away from the goal. This was the best order I found:
1. Down
2. Right
3. Left
4. Up

##### Heuristic Search V1 (Refer to heuristicSearch.py)

I also implemented a heuristic search (greedy) which would take the co-ordinates 
of the each node calculate the direct distance to the goal node. Then, instead of a queue or stack,
I used a priority queue which would always put the node with the shortest heuristic at the front,
(I modified the Node class to be comparable by their heuristic).

The first thing I noticed was that the algorithm visited the fewest nodes in maze-Easy.txt, 
which was a promising start. This trend continued, with the greedy search only searching 40% of the nodes DFS 
did and only 3% the nodes of BFS (for the VLarge maze).

However, the algorithm found a path of the same length as DFS but was slightly slower than DFS. 
This is likely because python's priority queue is not blazingly fast, so if I were able to 
implement a more efficient method of choosing the node with the lowest heuristic, I could 
possibly make this algorithm faster than DFS.

##### Heuristic Search V2 (Refer to heuristicSearchV2.py)

I then made a slight change to the algorithm where instead of using python's priority queue, 
I used a list and searched it for the node with the lowest heuristic.

Unfortunately this produced an algorithm with O(k^n) because it was ok for the smaller mazes, 
but suddenly shot up for Large.txt and VLarge.txt. As for the other metrics, it was completely unpredictable.
Sometimes it would return the DFS solution, other times it would find the BFS solution. Therefore, I would say that
this algorithm is not very reliable and V1 is superior.
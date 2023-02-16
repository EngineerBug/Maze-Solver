
## Python Maze Solver

This is a maze solver using depth first and breadth first searches to solve a
maze imported from a text file.

Notes for use:

- nodes.py is designed to contain all code common to other files in the project.
- nodes.py is imported into depthFirstSearch.py and breadthFirstSearch.py
- There is a Node class in nodes.py which is used to construct a search tree, 
    - therefore do not run either without nodes.py

Questions:

#### 1.1: MAze Solver as a Search Problem

A maze can be described as a set of positions, each of which have one-or-
more neighbours. The maze can be considered as a tree searcher, beginning
at an entrance node, where each node points to its neighbours and each
branch is every possible route to a dead end (or the exit). The maze solver
then follows each branch to its conclusion or until the ”exit node” is found.

#### 1.2.1: Depth-First-Search

A depth-first algorithm is a uniform method of searching a tree for the goal
node where each individual branch is searched before the next. Our maze
solver could use this method to search every possible path in the maze until
it finds a dead end, then go back to the last unsearched intersection and
look down another path.

#### 1.2.2: Using DFS to Solve maze-Easy.txt

Path:
(1,0), (1,1), (2,1), (3,1), (4,1), (5,1), 
(5,2), (5,3), (5,4), (5,5), (6,5), (7,5), 
(8,5), (8,6), (9,6), (10,6), (11,6), (12,6), 
(13,6), (14,6), (15,6), (16,6), (17,6), (17,7), 
(17,8), (18,8), (18,9)

#### 1.2.3: DFS Analysis

Solution Length: 27
Total Nodes Visited: 46
Time: about 0.00035 seconds (under a millisecond)

#### 1.2.4: DFS Generalisation

**maze-Medium**

**maze-Large**

**maze-VLarge**

#### 1.3.1: Alterative Algorithm

An alternative algorithm to solve the maze would be breadth-first-search, a
uniform method of searching a tree where instead of choosing the next node
based on a stack, BFS chooses based on a queue. I.e. it searches by tree
layer instead of by branch.

This can improve performance when the goal is close to the root. However, if
the goal is far away from the root, BFS can take longer than DFS assuming
the correct branch is checked early on.

#### 1.3.2: Impement Alternative Algorithm

#### 1.3.3: Analyse Alternative Algorithm

#### 1.3.4: Algorithm Comparrison
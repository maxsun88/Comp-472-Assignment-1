Sources: http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html#:~:text=On%20a%20grid%2C%20there%20are,Diagonal%20distance%20(L%E2%88%9E)

Comp 472 Assignment 1
Members:
Julie Pierrisnard - 40077165
Ningyuan - 40124859

#####################################################
BUILD INSTRUCTIONS

numpy and matplotlib need to be installed.
https://numpy.org/
https://matplotlib.org/

The program is run by building python3 main.py in your IDE or
navigating to the file's directory in the command prompt then >>>python main.py

######################################################
PURPOSE

Our program finds the shortest (cost) path between a start point and any valid location using A* algorithm.
If you are playing as a covid patient ('c'), a valid location is a quarantine place.
If you are playing as a vaccination patient ('v'), a valid location is a vaccination center.
You cannot play as the role P.

Based on user input, a random map is generated and you will be asked to select (click) a start and valid destination location depending on your player type.

######################################################
SEARCH ALGORITHM

Our search algorithm is A*.
A* is implemented in the run(start) function located in mapUtility.py.

Our heuristic functions are implemented in setHeuristic() function in mapUtility.py.
We use two different heuristic functions depending on the type of player 'c' or 'v'.
The 'c' player heuristic function is the Manhattan distance.
The 'v' player's heuristic function is the Diagonal distance.
Source: http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html#:~:text=On%20a%20grid%2C%20there%20are,Diagonal%20distance%20(L%E2%88%9E)

The heuristic values are computed using multiple goals: all valid destinations are a potential goal. For example, all vaccination centers are a potential goal for the player 'v'.
All goals have h=0.
A* stops when it has encountered the first goal and returns that goal as well as its cost and its path.
Hence the destination entered by the user is not guaranteed to be the goal returned by A* because it is not guaranteed to be the closest in terms of cost.
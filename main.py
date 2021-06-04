import numpy as np
import math
from plot import *

##################################################################################################################

# Global Variable of player
PLAYER = "V"

# Number of rows and columns TODO: Change to USER INPUT
row_num = 10
col_num = 10

# generate char_map of locations
char_map = []
# Create Randomized Map
for i in range(row_num):
    row = []
    for j in range(col_num):
        rd = random.randint(1, 4)
        if rd == 1:
            row.append("p")
        elif rd == 2:
            row.append("q")
        elif rd == 3:
            row.append("v")
        else:
            row.append("n")
    char_map.append(row)
# print(char_map)

##################################################################################################################
# generate an array of points pointArr for path finding

pointArr_row = row_num + 1
pointArr_col = col_num + 1

nbPoints = pointArr_row * pointArr_col
pointList = []

for i in range(nbPoints):
    pointList.append(i + 1)

tempPointArr = np.asarray(pointList)
pointArr = np.reshape(tempPointArr, (pointArr_row, pointArr_col))


# print("array of points:")
# print(pointArr)

##################################################################################################################
# PEEKING FUNCTIONS
# checks if the index is in bounds of an array
# takes an array and a point (i,j)
def isInBounds(arr, index):
    arr = np.asarray(arr)
    row, col = arr.shape
    if index[0] >= 0 and index[0] < row and index[1] >= 0 and index[1] < col:
        return True
    else:
        return False


# get costs correlating each kind of areas
def getLocationCost(tuple):
    i, j = tuple
    c_dic = {  # costs for role C - patient
        "p": 3,
        "q": 0,
        "v": 2,
        "n": 1
    }
    v_dic = {  # costs for role V - vaccine receiver
        "p": 1,
        "q": 3,
        "v": 0,
        "n": 2
    }
    if PLAYER.lower() == 'c':  # Covid patient
        return c_dic[char_map[i][j]]
    elif PLAYER.lower() == 'v':
        return v_dic[char_map[i][j]]


# peeks right and returns the cost of moving right, without heuristic
# moving right along an edge requires us to fetch the locations at the top and at the bottom of the edge and returning the average
# takes a point (i,j)
def peekRight(origin):
    dest = (origin[0], origin[1] + 1)
    if (isInBounds(pointArr, dest)):  # make sure the place we want to go exists first
        top = (origin[0] - 1, origin[1])
        bot = (origin[0], origin[1])
        if not isInBounds(char_map, top):
            # DEBUG: print('returning bot')
            return getLocationCost(bot)
        if not isInBounds(char_map, bot):
            # DEBUG: print('returning top')
            return getLocationCost(top)
        # DEBUG: print('returning average')
        return (getLocationCost(top) + getLocationCost(bot)) / 2
    else:
        pass


# peeks left and returns the cost of moving left, without heuristic
# moving left along an edge requires us to fetch the locations at the top and at the bottom of the edge and returning the average
# takes a point (i,j)
def peekLeft(origin):
    dest = (origin[0], origin[1] - 1)
    if (isInBounds(pointArr, dest)):  # make sure the place we want to go exists first
        top = (dest[0] - 1, dest[1])
        bot = (dest[0], dest[1])
        if not isInBounds(char_map, top):
            # DEBUG: print('returning bot')
            return getLocationCost(bot)
        if not isInBounds(char_map, bot):
            # DEBUG: print('returning top')
            return getLocationCost(top)
        # DEBUG: print('returning average')
        return (getLocationCost(top) + getLocationCost(bot)) / 2
    else:
        pass


# peeks up and returns the cost of moving up, without heuristic
# moving up along an edge requires us to fetch the locations at the left and at the right of the edge and returning the average
# takes a point (i,j)
def peekUp(origin):
    dest = (origin[0] - 1, origin[1])
    if (isInBounds(pointArr, dest)):  # make sure the place we want to go exists first
        left = (dest[0], dest[1] - 1)
        right = (dest[0], dest[1])
        if not isInBounds(char_map, left):
            # DEBUG: print('returning right')
            return getLocationCost(right)
        if not isInBounds(char_map, right):
            # DEBUG: print('returning left')
            return getLocationCost(left)
        # DEBUG: print('returning average')
        return (getLocationCost(left) + getLocationCost(right)) / 2
    else:
        pass


# peeks down and returns the cost of moving down, without heuristic
# moving down along an edge requires us to fetch the locations at the left and at the right of the edge and returning the average
# takes a point (i,j)
def peekDown(origin):
    dest = (origin[0] + 1, origin[1])
    if (isInBounds(pointArr, dest)):  # make sure the place we want to go exists first
        left = (origin[0], origin[1] - 1)
        right = (origin[0], origin[1])
        if not isInBounds(char_map, left):
            # DEBUG: print('returning right')
            return getLocationCost(right)
        if not isInBounds(char_map, right):
            # DEBUG: print('returning left')
            return getLocationCost(left)
        # DEBUG: print('returning average')
        return (getLocationCost(left) + getLocationCost(right)) / 2
    else:
        pass


# returns the cost of the upper left diagonal, without heuristic
def peekUpperLeftDiag(origin):
    dest = (origin[0] - 1, origin[1] - 1)
    if (isInBounds(pointArr, dest)):
        # first triangle
        edge1 = peekLeft(origin)
        edge2 = peekDown(dest)
        first_cost = math.sqrt(edge1 ** 2 + edge2 ** 2)
        # second triangle
        edge1 = peekUp(origin)
        edge2 = peekRight(dest)
        second_cost = math.sqrt(edge1 ** 2 + edge2 ** 2)
        return max(first_cost, second_cost)
    else:
        pass


# returns the cost of the upper right diagonal, without heuristic
def peekUpperRightDiag(origin):
    dest = (origin[0] - 1, origin[1] + 1)
    if (isInBounds(pointArr, dest)):
        # first triangle
        edge1 = peekRight(origin)
        edge2 = peekDown(dest)
        first_cost = math.sqrt(edge1 ** 2 + edge2 ** 2)
        # second triangle
        edge1 = peekUp(origin)
        edge2 = peekLeft(dest)
        second_cost = math.sqrt(edge1 ** 2 + edge2 ** 2)
        return max(first_cost, second_cost)
    else:
        pass


# returns the cost of the lower left diagonal, without heuristic
def peekLowerLeftDiag(origin):
    dest = (origin[0] + 1, origin[1] - 1)
    if (isInBounds(pointArr, dest)):
        # first triangle
        edge1 = peekLeft(origin)
        edge2 = peekUp(dest)
        first_cost = math.sqrt(edge1 ** 2 + edge2 ** 2)
        # second triangle
        edge1 = peekDown(origin)
        edge2 = peekRight(dest)
        second_cost = math.sqrt(edge1 ** 2 + edge2 ** 2)
        return max(first_cost, second_cost)
    else:
        pass


# returns the cost of the lower right diagonal, without heuristic
def peekLowerRightDiag(origin):
    dest = (origin[0] + 1, origin[1] + 1)
    if (isInBounds(pointArr, dest)):
        # first triangle
        edge1 = peekRight(origin)
        edge2 = peekUp(dest)
        first_cost = math.sqrt(edge1 ** 2 + edge2 ** 2)
        # second triangle
        edge1 = peekDown(origin)
        edge2 = peekLeft(dest)
        second_cost = math.sqrt(edge1 ** 2 + edge2 ** 2)
        return max(first_cost, second_cost)
    else:
        pass


##################################################################################################################
# A*

visitedPoints = {}  # dictionary containing all the points that have been visited already  {(i, j): (heuristic+cost, cost, (i_parent, j_parent))}
dist = {}  # dictionary containing all the explored  points and their distances {(i, j): (heuristic+cost, cost, (i_parent, j_parent))}
index_list = []  # Calculated Path, a list of indexes on 2d array of pointArr
start = ()  # start point TODO:user input
end = ()  # end point TODO:user input

#gets heuristic from a given point to our end destination
#heuristic changes depending on the player
def getHeuristic(point, end):
    #manhattan
    if(PLAYER.lower() == "c"):
        h_displacement = abs(end[1] - point[1])
        v_displacement = abs(end[0] - point[0])
        return (h_displacement + v_displacement)*0.5 #the maximum edge cost is 3
    #eucledian??
    if PLAYER.lower() == "v":
        D = 3
        D_d = 1.414  # Diagonal cost
        dx = abs(end[1] - point[1])
        dy = abs(end[0] - point[0])
        # return D * (dx + dy) + (D_d - 2 * D) * min(dx, dy)
        return 0

def setHeuristic(pointArr):
    #shared first part: setting all corners to h=0
    
    #if patient = c; loop for all h=0 for mahnattan
    
    #if patient = v; loop for all h=0 for diagonal
    pass

# visits a point with the lowest distance by adding removing it from dist{} and adding it to visitedPoints{} then returns the point
def visitMinDist():
    smallestEntryKey = min(dist, key=dist.get)
    visitedPoints[smallestEntryKey] = dist[
        smallestEntryKey]  # creates a new entry identical to the smallest entry in dist
    del dist[smallestEntryKey]  # remove it from dist
    return smallestEntryKey


# explores neighbour points and updates their distance value in dist{}
def exploreNeighbours(origin):
    neighbor_list = []
    # Right
    point_right = (origin[0], origin[1] + 1)
    cost_right = peekRight(origin)
    neighbor_list.append((point_right, cost_right))
    # Left
    point_left = (origin[0], origin[1] - 1)
    cost_left = peekLeft(origin)
    neighbor_list.append((point_left, cost_left))
    # Up
    point_up = (origin[0] - 1, origin[1])
    cost_up = peekUp(origin)
    neighbor_list.append((point_up, cost_up))
    # Down
    point_down = (origin[0] + 1, origin[1])
    cost_down = peekDown(origin)
    neighbor_list.append((point_down, cost_down))
    if PLAYER.lower() == 'v':  # if the player is a covid patient then we can also explore diagonal paths
        # Upper Left
        point_upperLeft = (origin[0] - 1, origin[1] - 1)
        cost_upperLeft = peekUpperLeftDiag(origin)
        neighbor_list.append((point_upperLeft, cost_upperLeft))
        # Upper Right
        point_upperRight = (origin[0] - 1, origin[1] + 1)
        cost_upperRight = peekUpperRightDiag(origin)
        neighbor_list.append((point_upperRight, cost_upperRight))
        # Lower Left
        point_lowerLeft = (origin[0] + 1, origin[1] - 1)
        cost_lowerLeft = peekLowerLeftDiag(origin)
        neighbor_list.append((point_lowerLeft, cost_lowerLeft))
        # Lower Right
        point_lowerRight = (origin[0] + 1, origin[1] + 1)
        cost_lowerRight = peekLowerRightDiag(origin)
        neighbor_list.append((point_lowerRight, cost_lowerRight))
    # Update information for each neighbor
    for neighbor in neighbor_list:
        updateNeighbor(neighbor[0], neighbor[1], origin)
    print(neighbor_list)


# update neighboring node's path information
def updateNeighbor(point, cost, origin):
    if cost is not None and point not in visitedPoints:
        total_cost = visitedPoints[origin][1] + cost
        updateDistance(point, origin, total_cost)


# updates distance and parent value in dist{} if it is lower than the current one
# takes heuristic into account
def updateDistance(point, parent, newCost):
    if point in dist:
        if (newCost + getHeuristic(point, end)) < dist[point][0]:
            dist[point] = (newCost + getHeuristic(point, end), newCost, parent)

#TODO:finished when h=0
# checks if algorithm is finished
# finished if our end point has been explored (its distance is no longer infinity)
def isFinished(end):
    if dist[end][0] != float("inf"):
        return True
    else:
        return False


# Create a list of indexes according to the order of visits
def constructPathIndexList():
    temp_pt = end
    while temp_pt != start:
        index_list.insert(0, temp_pt)
        temp_pt = visitedPoints[temp_pt][2]
    index_list.insert(0, temp_pt)


def printPathInfo():
    print("Path Taken:", end=" ")
    print(*index_list, sep=" -> ")
    print("Total Cost: {}".format(visitedPoints[end][1]))


# runs the algorithm
def run(start, end):
    for i in range(pointArr_row):
        for j in range(pointArr_col):
            dist[(i, j)] = (float("inf"), float("inf"), ())
    dist[start] = (getHeuristic(start, end) + 0, 0, ())  # the cost of our starting point is set to 0
    while isFinished(end) is False:
        minDist = visitMinDist()  # visit point with minimum distance in dist{}
        exploreNeighbours(minDist)  # we explore all its neighbours and update their distance values
    visitedPoints[end] = dist[end]  # adding the end point to the visitedPoints
    del dist[end]  # remove end point from dist
    constructPathIndexList()  # create index list
    printPathInfo()


start = (8, 3)
end = (2, 10)
run(start, end)

# display map to screen
displayMap(char_map, row_num, col_num, index_list)

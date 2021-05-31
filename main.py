import numpy as np
from plot import *

##################################################################################################################
# generate char_map of locations

# Number of rows and columns TODO: Change to USER INPUT
row_num = 5
col_num = 6

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

print(char_map)

# display map to screen
displayMap(char_map, row_num, col_num)

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
    row, col = arr.shape
    if index[0] >= 0 and index[0] < row and index[1] >= 0 and index[1] < col:
        return True
    else:
        return False


# TODO: write function that converts a letter in char_map into a value depending on the type of player
def getLocationCost(player):
    pass


# peeks right and returns the cost of moving right
# moving right along an edge requires us to fetch the locations at the top and at the bottom of the edge and returning the average
# takes a point (i,j)
def peekRight(origin):
    dest = (origin[0], origin[1] + 1)
    if (isInBounds(pointArr, dest)):  # make sure the place we want to go exists first
        top = (origin[0] - 1, origin[1])
        bot = (origin[0], origin[1])
        if not isInBounds(char_map, top):
            # DEBUG: print('returning bot')
            return char_map[bot]
        if not isInBounds(char_map, bot):
            # DEBUG: print('returning top')
            return char_map[top]
        # DEBUG: print('returning average')
        return (char_map[top] + char_map[bot]) / 2
    else:
        pass


# peeks left and returns the cost of moving left
# moving left along an edge requires us to fetch the locations at the top and at the bottom of the edge and returning the average
# takes a point (i,j)
def peekLeft(origin):
    dest = (origin[0], origin[1] - 1)
    if (isInBounds(pointArr, dest)):  # make sure the place we want to go exists first
        top = (dest[0] - 1, dest[1])
        bot = (dest[0], dest[1])
        if not isInBounds(char_map, top):
            # DEBUG: print('returning bot')
            return char_map[bot]
        if not isInBounds(char_map, bot):
            # DEBUG: print('returning top')
            return char_map[top]
        # DEBUG: print('returning average')
        return (char_map[top] + char_map[bot]) / 2
    else:
        pass


# peeks up and returns the cost of moving up
# moving up along an edge requires us to fetch the locations at the left and at the right of the edge and returning the average
# takes a point (i,j)
def peekUp(origin):
    dest = (origin[0] - 1, origin[1])
    if (isInBounds(pointArr, dest)):  # make sure the place we want to go exists first
        left = (dest[0], dest[1] - 1)
        right = (dest[0], dest[1])
        if not isInBounds(char_map, left):
            # DEBUG: print('returning right')
            return char_map[right]
        if not isInBounds(char_map, right):
            # DEBUG: print('returning left')
            return char_map[left]
        # DEBUG: print('returning average')
        return (char_map[left] + char_map[right]) / 2
    else:
        pass


# peeks down and returns the cost of moving down
# moving down along an edge requires us to fetch the locations at the left and at the right of the edge and returning the average
# takes a point (i,j)
def peekDown(origin):
    dest = (origin[0] + 1, origin[1])
    if (isInBounds(pointArr, dest)):  # make sure the place we want to go exists first
        left = (origin[0], origin[1] - 1)
        right = (origin[0], origin[1])
        if not isInBounds(char_map, left):
            # DEBUG: print('returning right')
            return char_map[right]
        if not isInBounds(char_map, right):
            # DEBUG: print('returning left')
            return char_map[left]
        # DEBUG: print('returning average')
        return (char_map[left] + char_map[right]) / 2
    else:
        pass


##################################################################################################################
# DIJKSTRA ALGORITHM????
# start at beginning and put the first point in the visited list
# explore all neighbour points
# update the total distance of the points explored if the total distance is smaller than their current value
# visit the point with the lowest distance
# repeat
# end when we find our destination

visitedPoints = {}  # dictionary containing all the points that have been visited already  {(i, j): (cost, (i_parent, j_parent))}
dist = {}  # dictionary containing all the explored  points and their distances (initially infinity??)  {(i, j): (cost, (i_parent, j_parent))}
start = ()  # start point TODO:user input
end = ()  # end point TODO:user input


# visits a point with the lowest distance by adding removing it from dist{} and adding it to visitedPoints{} then returns the point
def visitMinDist():
    smallestEntryKey = min(dist, key=dist.get)
    visitedPoints[smallestEntryKey] = dist[
        smallestEntryKey]  # creates a new entry identical to the smallest entry in dist
    del dist[smallestEntryKey]  # remove it from dist
    return smallestEntryKey


# explores neighbour points and updates their distance value in dist{}
def exploreNeighbours(origin):
    point_right = (origin[0], origin[1] + 1)
    cost_right = peekRight(origin)
    if (
            cost_right is not None and point_right not in visitedPoints):  # make sure the cost of going right isn't None and the point has not already been visited
        total_cost_right = visitedPoints[origin][0] + cost_right  # the distance is cumulative
        updateDistance(point_right, origin, total_cost_right)

    point_left = (origin[0], origin[1] - 1)
    cost_left = peekLeft(origin)
    if (cost_left is not None and point_left not in visitedPoints):
        total_cost_left = visitedPoints[origin][0] + cost_left
        updateDistance(point_left, origin, total_cost_left)

    point_up = (origin[0] - 1, origin[1])
    cost_up = peekUp(origin)
    if (cost_up is not None and point_up not in visitedPoints):
        total_cost_up = visitedPoints[origin][0] + cost_up
        updateDistance(point_up, origin, total_cost_up)

    point_down = (origin[0] + 1, origin[1])
    cost_down = peekDown(origin)
    if (cost_down is not None and point_down not in visitedPoints):
        total_cost_down = visitedPoints[origin][0] + cost_down
        updateDistance(point_down, origin, total_cost_down)


# updates distance and parent value in dist{} if it is lower than the current one
def updateDistance(point, parent, newValue):
    if point in dist:
        if newValue < dist[point][0]:
            dist[point][0] = newValue
            dist[point][1] = parent


# checks if algorithm is finished
# finished if our end point has been explored (its distance is no longer infinity)
def isFinished():
    if dist[end][0] is not float("inf"):
        return True
    else:
        return False


# runs the algorithm
def run(start, end):
    for i in range(pointArr_row):
        for j in range(pointArr_col):
            dist[(i, j)] = (float("inf"), ())

    dist[start][0] = 0  # the cost of our starting point is set to 0 so that it is picked first

    while isFinished is False:
        minDist = visitMinDist()  # visit point with minimum distance in dist{}
        exploreNeighbours(minDist)  # we explore all its neighbours and update their distance values

# now we have found the end point
# TODO: write function that stores/displays the path taken and the total cost


# TESTING STUFF
# test = {(1, 2): (200, (0,0)), (3, 0): (100, (100,0))}
# test2 = {}
# print(test)
# move minimum value from test to test2
# smallestEntryKey = min(test, key = test.get)
# test2[smallestEntryKey] = test[smallestEntryKey] #creates a new entry identical to the smallest entry in dist
# del test[smallestEntryKey] #remove it from dist
# print(test)
# print(test2)
# prints the cost
# print(test[1, 2][0])
# prints the parent point
# print(test[1,2][1])
# if (1, 2) in test:
# 	print('heck yeah')
# adding new point and value
# test[(0,1)] = 400, (0,0)
# print(test)

# testing = {}

# for i in range(pointArr_row):
# 	for j in range(pointArr_col):
# 		testing[(i,j)] = (float("inf"), ())

# print(testing)


##################################################################################################################
# HEURISTIC FUNCTIONS

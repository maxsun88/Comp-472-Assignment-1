import random

import numpy as np
import math

PLAYER = ""
char_map = []
pointArr = []
row_num = 0
col_num = 0
pointArr_row = 0
pointArr_col = 0
start = ()
index_list = []


def initializeMap(player, charmap, rownum, colnum, startpt, indexlist):
    global PLAYER, char_map, pointArr, row_num, col_num, start, index_list, pointArr_row, pointArr_col
    PLAYER = player
    char_map = charmap
    row_num = rownum
    col_num = colnum
    start = startpt
    index_list = indexlist
    ##################################################################################################################
    # generate an array of points pointArr for path finding
    pointArr_row = row_num + 1
    pointArr_col = col_num + 1
    nbPoints = pointArr_row * pointArr_col
    pointList = []
    for i in range(nbPoints):
        pointList.append(float("inf"))
    tempPointArr = np.asarray(pointList)
    pointArr = np.reshape(tempPointArr, (pointArr_row, pointArr_col))


# Create randomized map representing the areas
def generateCharMap(rownum, colnum):
    char_map = []
    for i in range(rownum):
        row = []
        for j in range(colnum):
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
    # char_map = [['n', 'n', 'v', 'n', 'n', 'p', 'n', 'p'],
    #             ['n', 'p', 'v', 'p', 'v', 'p', 'n', 'p'],
    #             ['p', 'p', 'n', 'p', 'v', 'p', 'v', 'v'],
    #             ['p', 'v', 'q', 'p', 'p', 'n', 'n', 'p'],
    #             ['p', 'p', 'v', 'q', 'v', 'q', 'q', 'p'],
    #             ['q', 'q', 'q', 'v', 'p', 'q', 'p', 'q'],
    #             ['v', 'q', 'n', 'v', 'p', 'q', 'p', 'n'],
    #             ['n', 'n', 'q', 'p', 'v', 'v', 'p', 'q']]
    return char_map


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


# stores heuristic values in pointArr
# multiple goals heuristic
def setHeuristic():
    # setting all corners to h=0 and storing them
    listOfEndPoints = []
    for i in range(row_num):
        for j in range(col_num):
            if (PLAYER.lower() == "c" and char_map[i][j] == "q") or (PLAYER.lower() == "v" and char_map[i][j] == "v"):
                pointArr[i][j] = 0
                listOfEndPoints.append((i, j))
                pointArr[i + 1][j] = 0
                listOfEndPoints.append((i + 1, j))
                pointArr[i][j + 1] = 0
                listOfEndPoints.append((i, j + 1))
                pointArr[i + 1][j + 1] = 0
                listOfEndPoints.append((i + 1, j + 1))

        for endPoint in listOfEndPoints:  # loop based on all the end points
            for i in range(pointArr_row):
                for j in range(pointArr_col):
                    if pointArr[i][j] != 0:  # make sure we are not changing the heuristic value of an end point
                        # if covid patient, loop manhattan
                        if PLAYER.lower() == "c":
                            h_displacement = abs(endPoint[0] - i)
                            v_displacement = abs(endPoint[1] - j)
                            result = (h_displacement + v_displacement) * 0.5
                            if result < pointArr[i][j]:
                                pointArr[i][j] = result
                        # if vaccine patient, loop Chebyshev distance
                        if PLAYER.lower() == "v":
                            D = 0.5
                            D_d = 1.414 / 2  # Diagonal cost
                            dx = abs(endPoint[0] - i)
                            dy = abs(endPoint[1] - j)
                            result = D * (dx + dy) + (D_d - 2 * D) * min(dx, dy)
                            if result < pointArr[i][j]:
                                pointArr[i][j] = result


# returns heuristic at a point (i,j)
def getHeuristic(point):
    return pointArr[point[0]][point[1]]


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
    if PLAYER.lower() == 'v':  # if the player is a vaccine receiver then we can also explore diagonal paths
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
    # print(neighbor_list)


# update neighboring node's path information
def updateNeighbor(point, cost, origin):
    if cost is not None and point not in visitedPoints:
        total_cost = visitedPoints[origin][1] + cost
        updateDistance(point, origin, total_cost)


# updates distance and parent value in dist{} if it is lower than the current one
# takes heuristic into account
def updateDistance(point, parent, newCost):
    if point in dist:
        if (newCost + getHeuristic(point)) < dist[point][0]:
            dist[point] = (newCost + getHeuristic(point), newCost, parent)


# checks if algorithm is finished
# finished when we've explored a point where h=0
def isFinished():
    for point in dist:
        if (dist[point][0] != float("inf") and pointArr[point[0]][point[1]] == 0):
            return True
    return False


# returns our final destination which is the first point that was found with h=0
def getFinalDestination():
    for point in dist:
        if (dist[point][0] != float("inf") and pointArr[point[0]][point[1]] == 0):
            return point
    return False


# Create a list of indexes according to the order of visits
def constructPathIndexList(end):
    temp_pt = end
    while temp_pt != start:
        index_list.insert(0, temp_pt)
        temp_pt = visitedPoints[temp_pt][2]
    index_list.insert(0, temp_pt)


def printPathInfo(end):
    print("Path Taken:", end=" ")
    print(*index_list, sep=" -> ")
    print("Total Cost: {}".format(visitedPoints[end][1]))


# runs the algorithm
def run(start):
    setHeuristic()
    # print(pointArr)
    for i in range(pointArr_row):
        for j in range(pointArr_col):
            dist[(i, j)] = (float("inf"), float("inf"), ())  # {(i, j): (heuristic+cost, cost, (i_parent, j_parent))}
    dist[start] = (getHeuristic(start) + 0, 0, ())
    while isFinished() is False:
        minDist = visitMinDist()  # visit point with minimum distance in dist{}
        exploreNeighbours(minDist)  # we explore all its neighbours and update their distance values
    final_end = getFinalDestination()
    visitedPoints[final_end] = dist[final_end]  # adding the end point to the visitedPoints
    del dist[final_end]  # remove end point from dist
    print("We found this location with lowest cost at: ", final_end)
    constructPathIndexList(final_end)  # create index list
    printPathInfo(final_end)

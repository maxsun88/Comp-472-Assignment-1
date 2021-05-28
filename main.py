import numpy as np
from plot import *

##################################################################################################################
#generate char_map of locations

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

#display map to screen
displayMap(char_map, row_num, col_num)

##################################################################################################################
#generate an array of points pointArr for path finding

pointArr_row = row_num +1
pointArr_col = col_num +1

nbPoints = pointArr_row * pointArr_col
pointList = []

for i in range(nbPoints):
	pointList.append(i+1)

tempPointArr = np.asarray(pointList)
pointArr = np.reshape(tempPointArr, (pointArr_row, pointArr_col))

print("array of points:")
print(pointArr)

##################################################################################################################
#PEEKING FUNCTIONS
#checks if the index is in bounds of an array
#takes an array and a point (i,j)
def isInBounds(arr, index):
	row, col = arr.shape
	if index[0] >= 0 and index[0] < row and index[1] >= 0 and index[1] < col:
		return True
	else:
		return False


#peeks right and returns the cost of moving right
#moving right along an edge requires us to fetch the locations at the top and at the bottom of the edge and returning the average
#takes a point (i,j)
def peekRight(origin):
	dest = (origin[0], origin[1]+1)
	if(isInBounds(pointArr, dest)): #make sure the place we want to go exists first
		top = (origin[0]-1, origin[1])
		bot = (origin[0], origin[1])
		if not isInBounds(locArr, top):
			#DEBUG: print('returning bot')
			return locArr[bot]
		if not isInBounds(locArr, bot):
			#DEBUG: print('returning top')
			return locArr[top]
		#DEBUG: print('returning average')
		return (locArr[top] + locArr[bot]) /2
	else:
		pass


#peeks left and returns the cost of moving left
#moving left along an edge requires us to fetch the locations at the top and at the bottom of the edge and returning the average
#takes a point (i,j)
def peekLeft(origin):
	dest = (origin[0], origin[1]-1)
	if(isInBounds(pointArr, dest)): #make sure the place we want to go exists first
		top = (dest[0]-1, dest[1])
		bot = (dest[0], dest[1])
		if not isInBounds(locArr, top):
			#DEBUG: print('returning bot')
			return locArr[bot]
		if not isInBounds(locArr, bot):
			#DEBUG: print('returning top')
			return locArr[top]
		#DEBUG: print('returning average')
		return (locArr[top] + locArr[bot]) /2
	else:
		pass


#peeks up and returns the cost of moving up
#moving up along an edge requires us to fetch the locations at the left and at the right of the edge and returning the average
#takes a point (i,j)
def peekUp(origin):
	dest = (origin[0]-1, origin[1])
	if(isInBounds(pointArr, dest)): #make sure the place we want to go exists first
		left = (dest[0], dest[1]-1)
		right = (dest[0], dest[1])
		if not isInBounds(locArr, left):
			#DEBUG: print('returning right')
			return locArr[right]
		if not isInBounds(locArr, right):
			#DEBUG: print('returning left')
			return locArr[left]
		#DEBUG: print('returning average')
		return (locArr[left] + locArr[right]) /2
	else:
		pass


#peeks down and returns the cost of moving down
#moving down along an edge requires us to fetch the locations at the left and at the right of the edge and returning the average
#takes a point (i,j)
def peekDown(origin):
	dest = (origin[0]+1, origin[1])
	if(isInBounds(pointArr, dest)): #make sure the place we want to go exists first
		left = (origin[0], origin[1]-1)
		right = (origin[0], origin[1])
		if not isInBounds(locArr, left):
			#DEBUG: print('returning right')
			return locArr[right]
		if not isInBounds(locArr, right):
			#DEBUG: print('returning left')
			return locArr[left]
		#DEBUG: print('returning average')
		return (locArr[left] + locArr[right]) /2
	else:
		pass


##################################################################################################################
#DIJKSTRA ALGORITHM????
#start at beginning and put the first point in the visited list
#explore all neighbour points
#update the total distance of the points explored if the total distance is smaller than their current value
#visit the point with the lowest distance
#repeat
#end when we find our destination

visitedPoints = {} #dictionary containing all the points that have been visited already
dist = {} #dictionary containing all the explored  points and their distances (initially infinity??)


#visits a point with the lowest distance by adding removing it from dist{} and adding it to visitedPoints{}
def visitMinDist():
	pass


#explores neighbour points and updates their distance value in dist{}
def exploreNeighbours(origin):
	point_right = (origin[0], origin[1]+1)
	cost_right = peekRight(origin)
	if (cost_right is not None and point_right not in visitedPoints): #make sure the cost of going right isn't None and the point has not already been visited
		total_cost_right = visitedPoints[origin] + cost_right  #the distance is cumulative
		updateDistance(point_right, total_cost_right)

	point_left = (origin[0], origin[1]-1)
	cost_left = peekLeft(origin)
	if (cost_left is not None and point_left not in visitedPoints):
		total_cost_left = visitedPoints[origin] + cost_left
		updateDistance(point_left, total_cost_left)

	point_up = (origin[0]-1, origin[1])
	cost_up = peekUp(origin)
	if (cost_up is not None and point_up not in visitedPoints):
		total_cost_up = visitedPoints[origin] + cost_up
		updateDistance(point_up, total_cost_up)

	point_down = (origin[0]+1, origin[1])
	cost_down = peekDown(origin)
	if (cost_down is not None and point_down not in visitedPoints):
		total_cost_down = visitedPoints[origin] + cost_down
		updateDistance(point_down, total_cost_down)


#updates distance value in dist{} if it is lower than the current one
def updateDistance(point, newValue):
	if point in dist : #if the point is already explored then we just compare the value
		if newValue > dist[point]:
			dist[point] = newValue
	else: #otherwise the point was not previously explored so we add it to dist{}
		dist[point] = newValue


#testing dictionaries
# test = {(1, 2): 10, (3, 0): 100}
# print(test)
# if (1, 2) in test:
# 	print('heck yeah')
# #adding new point and value
# test[(0,1)] = 400
# print(test)
# #updating value
# test[(0,1)] = 60
# print(test[(0,1)])


##################################################################################################################
#HEURISTIC FUNCTIONS
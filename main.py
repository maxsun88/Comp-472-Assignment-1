import numpy as np

##################################################################################################################
#for testing purposes, locArr represents the cost of each location
locArr = np.array([[1, 2],
				   [3, 4]])

print("array of location costs:")
print(locArr, "\n")
##################################################################################################################
#from the size of locArr, generate an array of points pointArr that will be used for path finding
locArr_row, locArr_col = locArr.shape
pointArr_row = locArr_row +1
pointArr_col = locArr_col +1

nbPoints = pointArr_row * pointArr_col
pointList = []

for i in range(nbPoints):
	pointList.append(i+1)

tempPointArr = np.asarray(pointList)
pointArr = np.reshape(tempPointArr, (pointArr_row, pointArr_col))

print("array of points:")
print(pointArr)

##################################################################################################################
#functions
#checks if the index is in bounds
def isInBounds(arr, index):
	row, col = arr.shape
	if index[0] >= 0 and index[0] < row and index[1] >= 0 and index[1] < col:
		return True
	else:
		return False

#peeks right and returns the cost of moving right
#moving right along an edge requires us to fetch the locations at the top and at the bottom of the edge and returning the average
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

#print(peekRight((2,0)))

#peeks left and returns the cost of moving left
#moving left along an edge requires us to fetch the locations at the top and at the bottom of the edge and returning the average
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

#print(peekLeft((1,1)))

#peeks up and returns the cost of moving up
#moving up along an edge requires us to fetch the locations at the left and at the right of the edge and returning the average
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

#print(peekUp((1,1)))

#peeks down and returns the cost of moving down
#moving down along an edge requires us to fetch the locations at the left and at the right of the edge and returning the average
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

#print(peekDown((0,1)))
import math

PLAYER = ""
char_map = []
pointArr = []
row_num = 0
col_num = 0
width = 0
height = 0


def initializeInputUtil(player, charmap, rownum, colnum, w, h):
    global PLAYER, char_map, pointArr, row_num, col_num, width, height
    PLAYER = player
    char_map = charmap
    row_num = rownum
    col_num = colnum
    width = w
    height = h


# user input
def isCoordInBound(coord):
    X_LOWER_BOUND = 0
    X_UPPER_BOUND = col_num * width
    Y_LOWER_BOUND = 0
    Y_UPPER_BOUND = row_num * height
    if X_LOWER_BOUND <= coord[0] <= X_UPPER_BOUND and \
            Y_LOWER_BOUND <= coord[1] <= Y_UPPER_BOUND:
        return True
    else:
        return False


# Transform user' input into index on the array of nodes, e.g (0.1,0.05) -> 7,1
def coordinateToIndex(coord):
    if PLAYER.lower() == 'c':
        # the upper right node of the current block
        return row_num - int(math.ceil(coord[1] / height)), int(math.ceil(coord[0] / width))
    if PLAYER.lower() == 'v':
        # the lower right node
        return row_num - int(math.ceil(coord[1] / height)) + 1, int(math.ceil(coord[0] / width))


# Check if the ending point is the correlating one to the player role
def checkDestination(coord):
    pointArrIndex = (row_num - int(math.ceil(coord[1] / height)), int(math.ceil(coord[0] / width)))
    charMapIndex = (pointArrIndex[0], pointArrIndex[1]-1)
    if charMapIndex[0] > row_num - 1:  # make sure no array out of bound error
        charMapIndex = (row_num - 1, charMapIndex[1])
    if charMapIndex[0] < 0:
        charMapIndex = (0, charMapIndex[1])
    if charMapIndex[1] > col_num - 1:
        charMapIndex = (charMapIndex[0], col_num - 1)
    if charMapIndex[1] < 0:
        charMapIndex = (charMapIndex[0], 0)
    char = char_map[charMapIndex[0]][charMapIndex[1]]
    if PLAYER.lower() == 'c' and char == 'q':
        return True
    elif PLAYER.lower() == 'v' and char == 'v':
        return True
    else:
        return False

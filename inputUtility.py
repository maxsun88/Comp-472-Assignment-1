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
    return row_num - int(math.ceil(coord[1] / height)), int(math.ceil(coord[0] / width))


# Function to handle user input of a coordinate, return a tuple of coordinate, e.g. (0.15,0.2)
def inputCoordinate(message):
    print(message + ", use comma in between x and y ( e.g. 0.2,0.1 ):")
    while True:
        coord_str = input(">>>")
        coord_arr = coord_str.split(",")
        coord = (float(coord_arr[0]), float(coord_arr[1]))
        if not isCoordInBound(coord):
            print("Point Out of Bound! Please try again")
            continue
        else:
            break
    return coord


# Check if the ending point is the correlating one to the player role
def checkDestination(coord):
    pointArrIndex = coordinateToIndex(coord)
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

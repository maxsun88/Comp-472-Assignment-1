import plot
from inputUtility import *
from plot import *
from mapUtility import *

##################################################################################################################

# Global Variable of player
PLAYER = "C"
# Number of rows and columns TODO: Change to USER INPUT
row_num = 8
col_num = 8
# Map representing different areas
char_map = []
start = ()  # start point TODO:user input
index_list = []  # Calculated Path, a list of indexes on 2d array of pointArr

print("**************************************************************************")
print("Please indicate the number of rows and columns, divided by comma, e.g. 3,5")
rowcol_str = input(">>>")
rowcol_arr = rowcol_str.split(",")
row_num = int(rowcol_arr[0])
col_num = int(rowcol_arr[1])

# generate char_map of locations
char_map = generateCharMap(row_num, col_num)
# show map on screen
displayMap(char_map, row_num, col_num, index_list)
initializeInputUtil(PLAYER, char_map, row_num, col_num, plot.width, plot.height)

print("")
print("Please select your role")
print("Covid Patient - C")
print("Vaccine Receiver - V")

while True:
    PLAYER = input(">>>")
    if PLAYER.lower() == 'c' or PLAYER.lower() == 'v':
        break
    else:
        print("Wrong Input, please try again")
        continue

print("")
START_COORD = inputCoordinate("Enter the coordinate of the starting point")
print("Your start coordinate is {}".format(START_COORD))
start = coordinateToIndex(START_COORD)
print("Starting point's map index is {}".format(start))

while True:
    print("")
    END_COORD = inputCoordinate("Enter the coordinate of the ending point")
    if checkDestination(END_COORD):
        print("Correct Destination, program running...")
        break
    else:
        print("Your destination doesn't match your role, please try again")
        continue


initializeMap(PLAYER, char_map, row_num, col_num, start, index_list)
run(start)

# display map to screen
displayMap(char_map, row_num, col_num, index_list)

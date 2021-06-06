# -------------------------------------------------------
# Assignment 1
# Written by Julie Pierrisnard 40077165, Ningyuan Sun 40124859
# For COMP 472 – Summer 2021
# --------------------------------------------------------

import threading
import time

import plot
from inputUtility import *
from plot import *
from mapUtility import *

clickedCoordinate = ()  # Store the clicked Coordinate


# Function to listen to clicking event
def onclick(event):
    ix, iy = event.xdata, event.ydata
    global clickedCoordinate
    clickedCoordinate = (ix, iy)


##################################################################################################################
# Global Variable of player
PLAYER = ""
# Number of rows and columns
row_num = 0
col_num = 0
# Map representing different areas
char_map = []
start = ()  # start point
index_list = []  # Calculated Path, a list of indexes on 2d array of pointArr

# Input for number of rows and columns
print("**************************************************************************")
print("Please indicate the number of rows and columns, divided by comma, e.g. 3,5")
rowcol_str = input(">>>")
rowcol_arr = rowcol_str.split(",")
row_num = int(rowcol_arr[0])
col_num = int(rowcol_arr[1])
# generate char_map of locations
char_map = generateCharMap(row_num, col_num)
# show map on screen
fig = displayMap(char_map, row_num, col_num, index_list)
plt.show(block=False)

# Input for role selection
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

# Now the program has all the information it needs for checking further inputs
initializeInputUtil(PLAYER, char_map, row_num, col_num, plot.width, plot.height)

# Click to indicate start point
print("")
print("Please press inside a block to indicate where to start")
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.waitforbuttonpress()
print("Your start coordinate is {}".format(clickedCoordinate))
start = coordinateToIndex(clickedCoordinate)
print("Starting point's map index is {}".format(start))

# Click to indicate end point
while True:
    print("")
    print("Please press inside a block to indicate where you want to go")
    plt.waitforbuttonpress()
    END_COORD = clickedCoordinate
    if checkDestination(END_COORD):
        print("Correct Destination, program running...")
        break
    else:
        print("Your destination doesn't match your role, please try again")
        continue

time.sleep(1)

initializeMap(PLAYER, char_map, row_num, col_num, start, index_list)
run(start)

# display map to screen, with the calculated path marked
displayMap(char_map, row_num, col_num, index_list)
plt.show()


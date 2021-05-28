import random
import numpy as np
import matplotlib.pyplot as plt

# Color Values
q_color = 4  # quarantine area
p_color = 2  # playground area
v_color = 3  # vaccine area
n_color = 1  # neutral area

# Number of rows and columns TODO: Change to USER INPUT
row_num = 4
col_num = 5

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

# Create color map for UI purpose only
color_map = []
for i in range(row_num):
    row = []
    for j in range(col_num):
        if char_map[i][j] == "p":
            row.append(p_color)
        elif char_map[i][j] == "q":
            row.append(q_color)
        elif char_map[i][j] == "v":
            row.append(v_color)
        else:
            row.append(n_color)
    color_map.append(row)
color_map = np.array(color_map)

plt.imshow(color_map, extent=[0, 1.0, 0, 0.4], aspect='auto', interpolation='none')
plt.yticks(np.arange(0, 0.4, 0.1))
plt.grid(color='white', linestyle='-.', linewidth=3)

# Draw the Paths

x2, y2 = [0.0, 0.2], \
         [0.3, 0.3]
plt.plot(x2, y2, 'r', marker='o', linewidth=4)

x2, y2 = [0.2, 0.2], \
         [0.3, 0.2]
plt.plot(x2, y2, 'r', marker='o', linewidth=4)

x2, y2 = [0.2, 0.4], \
         [0.2, 0.2]
plt.plot(x2, y2, 'r', marker='o', linewidth=4)

plt.show()

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.cm as cm


def displayMap(char_map, row_num, col_num):
    # Color Values
    color_vals = [
        ["quarantine", 1],
        ["playground", 2],
        ["vaccine", 3],
        ["neutral", 4]
    ]

    width = 0.2  # cell width
    height = 0.1  # cell height

    # Create color map for UI purpose only
    color_map = []
    for i in range(row_num):
        row = []
        for j in range(col_num):
            if char_map[i][j] == "q":
                row.append(color_vals[0][1])
            elif char_map[i][j] == "p":
                row.append(color_vals[1][1])
            elif char_map[i][j] == "v":
                row.append(color_vals[2][1])
            else:
                row.append(color_vals[3][1])
        color_map.append(row)
    color_map = np.array(color_map)

    plt.figure(figsize=(10, 5))
    plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.1)
    im = plt.imshow(color_map, extent=[0, col_num * width, 0, row_num * height], cmap=cm.tab20c, aspect='auto',
                    interpolation='none')

    # Draw legends
    # colormap used by imshow
    colors = [im.cmap(im.norm(value[1])) for value in color_vals]
    # create a patch (proxy artist) for every color
    patches = [mpatches.Patch(color=colors[i], label=color_vals[i][0]) for i in range(len(color_vals))]
    # put those patched as legend-handles into the legend
    plt.legend(handles=patches, loc=4, bbox_to_anchor=(1.27, 0), prop={'size': 12}, borderaxespad=0.3)

    # create indexes shown on plot
    index_markers = []
    for i in range(row_num + 1):
        for j in range(col_num + 1):
            text = "{i},{j}".format(i=i, j=j)
            x_coord = j * width  # x coordinate
            y_coord = (row_num - i) * height  # y coordinate
            plt.text(x_coord, y_coord, text,
                     ha="center", va="center", bbox=dict(boxstyle=f"circle,pad=0.2", fc="white"))

    # create markers for different areas
    for i in range(row_num):
        for j in range(col_num):
            text = char_map[i][j]
            x_coord = (j + 0.5) * width  # x coordinate
            y_coord = (row_num - i - 0.5) * height  # y coordinate
            plt.text(x_coord, y_coord, text, fontsize=16, ha="center", va="center")

    # make the grids according to the cell sizes
    plt.xticks(np.arange(0, col_num * width, width))
    plt.yticks(np.arange(0, row_num * height, height))
    plt.grid(color='white', linestyle='-.', linewidth=3)

    # Draw the Paths TODO: Provide a function
    # x2, y2 = [0.0, 0.2], \
    #          [0.3, 0.3]
    # plt.plot(x2, y2, 'r', marker='o', linewidth=4)
    #
    # x2, y2 = [0.2, 0.2], \
    #          [0.3, 0.2]
    # plt.plot(x2, y2, 'r', marker='o', linewidth=4)
    #
    # x2, y2 = [0.2, 0.4], \
    #          [0.2, 0.2]
    # plt.plot(x2, y2, 'r', marker='o', linewidth=4)

    plt.show()

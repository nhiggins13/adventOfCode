import os
from common import INPUT_PATH

def get_num_trees(map_filename, right, down):
    num_tree = 0
    lines = open(os.path.join(INPUT_PATH, map_filename)).readlines()

    i = down
    j = right

    width = len(lines[0]) - 1
    while i < len(lines):
        if j >= width:
            j -= width

        if lines[i][j] == '#':
            num_tree += 1

        i += down
        j += right

    return num_tree

print(get_num_trees('map.txt', 3, 1))

print(get_num_trees('map.txt', 1, 1)*get_num_trees('map.txt', 3, 1)*get_num_trees('map.txt', 5, 1)*get_num_trees('map.txt', 7, 1)*get_num_trees('map.txt', 1, 2))

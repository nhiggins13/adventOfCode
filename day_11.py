import os
from copy import deepcopy

import numpy

from common import INPUT_PATH


DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def count_neighbors(seating_map, i, j):

    m, n= len(seating_map), len(seating_map[0])
    n_count = 0
    for r, c in DIRECTIONS:
        if (-1 < (i+r) < m) and (-1 < (j+c) < n):
            if seating_map[(i+r)][(j+c)] == '#':
                n_count += 1

    return n_count

def count_neighbors_in_sight(seating_map, i, j):
    m, n = len(seating_map), len(seating_map[0])
    n_count = 0
    for r, c in DIRECTIONS:
        row = (i + r)
        col = (j + c)
        while (-1 < row < m) and (-1 < col < n):
            if seating_map[row][col] == '#':
                n_count += 1
                break
            elif seating_map[row][col] == 'L':
                break

            row += numpy.sign(r)*1
            col += numpy.sign(c)*1

    return n_count


def update_seating(seating_map, max_to_leave=4, count_func=count_neighbors):
    copy_map = deepcopy(seating_map)

    for row in range(len(seating_map)):
        for col in range(len(seating_map[0])):
            curr_seat = seating_map[row][col]
            if curr_seat != '.':
                n_count = count_func(seating_map, row, col)

                if curr_seat == 'L' and n_count == 0:
                    copy_map[row][col] = '#'
                elif curr_seat == '#' and n_count >= max_to_leave:
                    copy_map[row][col] = 'L'

    return copy_map


def get_rounds(seating_map, max_to_leave=4, count_func=count_neighbors):
    round_count = 0
    prev = []

    while seating_map != prev:
        prev = deepcopy(seating_map)
        seating_map = update_seating(seating_map, max_to_leave, count_func)
        round_count += 1

    return round_count, seating_map, sum([col == '#' for row in seating_map for col in row])


f = open(os.path.join(INPUT_PATH, 'seating_map.txt'))
seating = [list(row.strip()) for row in f.readlines()]
f.close()

# rounds, smap, occupied = get_rounds(deepcopy(seating))
# print(occupied)
_, _, occupied2 = get_rounds(deepcopy(seating), 5, count_neighbors_in_sight)
print(occupied2)
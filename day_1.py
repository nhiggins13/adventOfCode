import os
from math import prod
from common import PATH, INPUT_PATH

num_dict = {}
with open(os.path.join(INPUT_PATH, "log_file.txt"), 'r') as f:
    for num in f:
        num_dict[int(num)] = None


def find_parts(num_dict, end_sum):
    for n in num_dict:
        looking_for = end_sum - n
        if looking_for in num_dict:
            return (n, looking_for)

print("Part one: ", prod(find_parts(num_dict, 2020)))

for num in num_dict:
    parts = find_parts(num_dict, 2020-num)
    if parts:
        print(num, parts)

        print(num*prod(parts))
        break


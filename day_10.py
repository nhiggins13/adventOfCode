import os
from collections import defaultdict
from common import INPUT_PATH
from itertools import permutations

def get_voltage_diff_count(adapters):
    volt_diff_count = defaultdict(int)
    last_adapter = 0
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    for adapter in adapters:
        diff = adapter - last_adapter
        volt_diff_count[diff] += 1
        last_adapter = adapter

    return volt_diff_count


def get_configurations_count(adapters):
    cache = defaultdict(int)

    def get_possible_adapts(curr, left):
        possible = []
        for a in left:
            if a > curr and (a - curr) < 4:
                possible.append(a)
            else:
                break

        return possible

    def get_count(curr_adapt, left):
        if len(left) == 0:
            return 1
        else:
            poss = get_possible_adapts(curr_adapt, left)
            key = (curr_adapt, tuple(poss))
            if key in cache:
                return cache[key]

            if len(poss) == 0:
                return 0

            count = 0
            for a in poss:
                new_left = left[left.index(a) + 1:]
                count += get_count(a, new_left)

            cache[(curr_adapt, tuple(poss))] = count
            return count

    adapters.sort()
    adapters = adapters + [adapters[-1] + 3]

    return get_count(0, adapters)


f = open(os.path.join(INPUT_PATH, "adapters.txt"))
adapter_list = [int(adapter.strip()) for adapter in f.readlines()]
f.close()


jolt_diff_counts = get_voltage_diff_count(adapter_list)
print(jolt_diff_counts[1] * jolt_diff_counts[3])

print(get_configurations_count(adapter_list))



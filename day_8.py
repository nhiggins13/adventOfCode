import os
from common import INPUT_PATH


def get_lines(filename):
    f = open(os.path.join(INPUT_PATH, filename))
    lines = [line.strip() for line in f.readlines()]
    f.close()

    return lines


def sign_addition(value, sign, added_to):
    if sign == '-':
        added_to -= value
    else:
        added_to += value

    return added_to


def accumulator_before_loop(lines, change_to_nop_pos=None):
    seen = set()
    pos = 0
    accumulator = 0

    jump_positions = []
    while pos not in seen and pos < len(lines):
        seen.add(pos)
        action = lines[pos][:3]
        value = int(lines[pos][5:])
        sign = lines[pos][4]

        if change_to_nop_pos and change_to_nop_pos == pos:
            action = 'nop'
        if action == 'acc':
            accumulator = sign_addition(value, sign, accumulator)
            pos += 1
        elif action == 'jmp':
            jump_positions.append(pos)
            pos = sign_addition(value, sign, pos)
        else:
            pos += 1

    return accumulator, jump_positions, pos >= len(lines)

def find_acc(lines, jump_positions):
    for jmp in jump_positions:
        acc, _, completed = accumulator_before_loop(lines, jmp)
        if completed:
            return acc

lines = get_lines('boot_file.txt')
print(accumulator_before_loop(lines))
_, jumps, _ = accumulator_before_loop(lines)

print("jumps: ",jumps)
print(find_acc(lines, jumps))


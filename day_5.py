import os
from common import INPUT_PATH


def binary_search(code, n, front_letter='F'):

    f = 0
    b = n

    for letter in code[:-1]:

        mid = (f + b - 1) // 2
        if letter == front_letter:
            b = mid
        else:
            f = mid + 1

    return f if code[-1] == front_letter else b


def find_seat(code, num_rows=128, num_cols=8):

    row_code = code[:num_cols-1]
    col_code = code[num_cols-1:]

    row = binary_search(row_code, n=num_rows-1)
    col = binary_search(col_code, n=num_cols-1, front_letter='L')

    return row * num_cols + col

seats = []
with open(os.path.join(INPUT_PATH, "boarding_passes.txt"), 'r') as f:
    for bp in f:
        seats.append(find_seat(bp.rstrip()))

print('Max seat: ', max(seats))

seats.sort()
last_seat = seats[0]
for curr_seat in seats[1:]:
    if curr_seat != last_seat + 1:
        print("My seat: ", curr_seat - 1)
        break

    last_seat = curr_seat


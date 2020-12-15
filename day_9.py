import os
from common import INPUT_PATH


def check_valid(preamble, num):
    for n in preamble:
        looking_for = num - n
        if looking_for != n:
            if looking_for in preamble:
                return True

    return False


def find_first_invalid(numbers):

    curr_pos = 25
    for n in numbers[25:]:
        preamble = numbers[curr_pos-25:curr_pos]
        if not check_valid(preamble, n):
            return n

        curr_pos +=1


def contigous_set(numbers, num):

    for i, n in enumerate(numbers[:-1]):
        end = i+1
        sum_of_cont = 0
        while end < len(numbers) and sum_of_cont < num:
            sum_of_cont = sum(numbers[i:end])
            if sum_of_cont == num:
                return min(numbers[i:end]) + max(numbers[i:end])

            end += 1

f = open(os.path.join(INPUT_PATH, "encrypted.txt"))
nums = [int(line.rstrip()) for line in f.readlines()]
f.close()

print(find_first_invalid(nums))

sum_num = find_first_invalid(nums)

print(contigous_set(nums, sum_num))


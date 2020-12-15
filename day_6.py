import os
from common import INPUT_PATH


def count_group_any(group_string):
    letters_seen = [False] * 26

    for letter in group_string.lower():
        letters_seen[ord(letter) - 97] = True

    return sum(letters_seen)

def count_group_all(group_string, group_size):
    letter_counts = [0] * 26

    for letter in group_string.lower():
        letter_counts[ord(letter) - 97] += 1

    return sum([count == group_size for count in letter_counts])


count_any = 0
count_all = 0
group_answers = ''
group_size = 0
with open(os.path.join(INPUT_PATH, 'customs_declarations.txt'), 'r') as f:
    for line in f:
        if line == '\n':
            count_any += count_group_any(group_answers)
            count_all += count_group_all(group_answers, group_size)
            group_answers = ''
            group_size = 0
        else:
            group_answers += line.rstrip()
            group_size += 1

    count_any += count_group_any(group_answers)
    count_all += count_group_all(group_answers, group_size)


print("Any", count_any)
print("All", count_all)

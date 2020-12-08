import os
import re
from common import INPUT_PATH
from collections import defaultdict

REGEX = r'(\d+)-(\d+) ([a-z]): ([a-z]+)'

def get_valid(password_filename):
    valid = []
    with open(os.path.join(INPUT_PATH, password_filename), 'r') as f:
        for line in f:
            match = re.match(REGEX, line)

            if not match:
                continue

            low, high, ch, password = match.group(1, 2, 3, 4)

            char_dict = defaultdict(int)
            for c in password:
                char_dict[c] += 1

            if int(high) >= char_dict[ch] >= int(low):
                valid.append(password)

    return valid

def get_valid2(password_filename):
    valid_count = 0
    with open(os.path.join(INPUT_PATH, password_filename), 'r') as f:
        for line in f:
            match = re.match(REGEX, line)

            high = int(match.group(1)) - 1
            low = int(match.group(2)) - 1
            ch = match.group(3)
            password = match.group(4)

            valid_count += int((password[high] == ch) ^ (password[low] == ch))

    return valid_count




print("Part one: ", len(get_valid("passwords.txt")))
print("Part two: ", get_valid2("passwords.txt"))
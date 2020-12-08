import os
import re
import copy
from common import INPUT_PATH

NEEDED = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])


def check_valid(passport, optional, detailed=False):
    remaining = NEEDED - set(passport.keys())

    valid = False
    if len(remaining) == 0:
        valid = True
    elif len(optional) == 0:
        valid = False
    else:
        valid = all([r in optional for r in remaining])

    check_detailed = check_valid_detailed(passport, optional) if detailed else True

    return valid and check_detailed



def height_check(val):
    m = re.match(r'^(\d+)(in|cm)$', val)
    if m:
        ht = int(m.group(1))
        metric = m.group(2)
        if metric == 'in':
            return 77 > ht > 58
        else:
            return 194 > ht > 149

    return False

CHECKS = {
    'byr': lambda val: 2002 >= int(val) >= 1920,
    'iyr': lambda val: 2020 >= int(val) >= 2010,
    'eyr': lambda val: 2030 >= int(val) >= 2020,
    'hgt': height_check,
    'hcl': lambda val: re.match(r'^#{1}[0-9a-f]{6}$', val),
    'ecl': lambda val: val in ['amb', 'blu', 'brn', 'gry','grn', 'hzl', 'oth'],
    'pid': lambda val: re.match(r'^\d{9}$', val),
    'cid': lambda val: True,
}

def check_valid_detailed(passport, optional):
    checks = copy.copy(CHECKS)
    for k in optional:
        if k in checks:
            checks[k] = lambda val: True

    for key, val in passport.items():
        if not checks[key](val):
            return False

    return True

def count_valid(batch_file, optional=[], detailed=True):
    valid_count = 0
    curr_passport = {}
    valid = []
    with open(os.path.join(INPUT_PATH, batch_file), 'r') as f:
        for line in f:
            if line == "\n":
                if check_valid(curr_passport, optional, detailed):
                    valid_count += 1
                    valid.append(curr_passport)

                curr_passport = {}
            else:
                line = line.replace('\n','')
                for pair in line.split(" "):
                    key, value = pair.split(':')
                    curr_passport[key] = value

    if check_valid(curr_passport, optional):
        valid_count += 1

    return valid_count


print(count_valid('batch_passport2.txt', ['cid']))
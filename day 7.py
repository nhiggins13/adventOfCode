import os
import re
from common import INPUT_PATH
from collections import defaultdict, deque

def get_rule_dict(rule_filename):
    regex_outer = r'(.+?) bag[s]? contain (\d+) (.+?) bag[s]?'
    regex_inner = r' (\d+) (.+?) bag[s]?'
    rules = defaultdict(list)
    with open(os.path.join(INPUT_PATH, rule_filename)) as f:
        for line in f:
            line_split = line.split(",")
            for i, split in enumerate(line_split):
                if i == 0:
                    m = re.match(regex_outer, split)
                    if m:
                        outer_bag, num_bags, inner_bag = m.groups([1, 2, 3])
                    else:
                        rules[split[:split.find(" bag")]] = []
                        continue
                else:
                    num_bags, inner_bag = re.match(regex_inner, split).groups([1, 2])

                rules[outer_bag.strip()].append((inner_bag.strip(), int(num_bags)))

    return rules


def get_bags_that_hold(rules, bag):
    outer_bags = set()
    checked = set()

    def check_bags(looking_for, curr_bag, holdings, outers=[]):
        if curr_bag in outer_bags:
            return [curr_bag]

        if curr_bag in checked:
            return

        if looking_for in holdings:
            outers.append(curr_bag)
            return outers

        for b in holdings:
            if b in outer_bags:
                outers.append(curr_bag)
                return outers

        for next_bag in holdings:
            next_holdings = [h[0] for h in rules.get(next_bag, [])]
            c = check_bags(looking_for, next_bag, next_holdings, outers+[curr_bag])
            if c:
                return c

        checked.add(curr_bag)

    for outer, val in rules.items():
        holdings = [v[0] for v in val]
        check = check_bags(bag, outer, holdings)
        if check:
            outer_bags.update(check)

    return outer_bags


def get_num_bags_needed(rules, bag):
    know_counts = {}

    def count_bags(curr_bag, num, holdings):
        if curr_bag in know_counts:
            return know_counts[curr_bag]

        if len(holdings) == 0:
            know_counts[curr_bag] = 1
            return 1

        count = 0
        for inner_bag, n in holdings:
            if inner_bag in know_counts:
                count += know_counts[inner_bag] * n
            else:
                count += n * count_bags(inner_bag, n, rules[inner_bag])

        know_counts[curr_bag] = count + 1
        return count + 1

    total = 0
    for b, num_bags in rules[bag]:
        total += num_bags * count_bags(b, num_bags, rules[b])

    return total




# rules = get_rule_dict('bag_rules.txt')

# results = get_bags_that_hold(rules, 'shiny gold')
#
# print(len(rules))
# print(sorted(results))
# print(len(results))

rules2 = get_rule_dict('bag_rules.txt')
print(get_num_bags_needed(rules2, 'shiny gold'))

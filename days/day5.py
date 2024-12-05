from util import read_file


def part1():
    input_list = read_file()
    updates = []
    rules = {}
    sum = 0

    for line in input_list[input_list.index("") + 1:]:
        updates.append([int(num) for num in line.split(",")])

    for line in input_list[:input_list.index("")]:
        x, y = [int(num) for num in line.split("|")]
        rules.setdefault(x, []).append(y)

    for update in updates:
        if is_correct(update, rules): sum += update[len(update) // 2]

    return sum


def is_correct(update, rules):
    for i in range(len(update)):
        if rules.get(update[i]) is None: continue
        rule_list = rules.get(update[i])
        for rule in rule_list:
            if update.count(rule) == 0: continue
            if i > update.index(rule): return False

    return True


def part2():
    input_list = read_file()
    updates = []
    rules = {}
    sum = 0

    for line in input_list[input_list.index("") + 1:]:
        updates.append([int(num) for num in line.split(",")])

    for line in input_list[:input_list.index("")]:
        x, y = [int(num) for num in line.split("|")]
        rules.setdefault(x, []).append(y)

    for update in updates:
        if not is_correct(update, rules):
            fixed = fix(update, rules)
            sum += fixed[len(update) // 2]

    return sum


def fix(update, rules):
    changed = False
    for i in range(len(update)):
        if rules.get(update[i]) is None: continue
        rule_list = rules.get(update[i])
        for z in range(len(rule_list)):
            if update.count(rule_list[z]) == 0: continue
            index_of_apir = update.index(rule_list[z])
            if i > index_of_apir:
                hold = update[i]
                update[i] = rule_list[z]
                update[index_of_apir] = hold
                changed = True
    return update if not changed else fix(update, rules)
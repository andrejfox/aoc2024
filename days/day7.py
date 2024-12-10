from util import read_file


def part1():
    input_list = read_file()
    parsed_list = []
    ret_sum = 0

    for line in input_list:
        split1 = line.split(":")
        parsed_list.append((int(split1[0]), [int(num) for num in split1[1].split(" ") if num != ""]))

    for value, numbers in parsed_list:
        cur_values = []
        get_possible_values1(numbers, 0, 0, cur_values)
        if cur_values.count(value) != 0:
            ret_sum += value

    return ret_sum


def part2():
    input_list = read_file()
    parsed_list = []
    ret_sum = 0

    for line in input_list:
        split1 = line.split(":")
        parsed_list.append((int(split1[0]), [int(num) for num in split1[1].split(" ") if num != ""]))

    for value, numbers in parsed_list:
        cur_values = []
        get_possible_values2(numbers, 0, 0, cur_values)
        if cur_values.count(value) != 0:
            ret_sum += value

    return ret_sum


def get_possible_values1(numbers, i, carry, ret_lsit):
    if i == len(numbers):
        return carry
    add = get_possible_values1(numbers, i + 1, carry + int(numbers[i]), ret_lsit)
    if add is not None: ret_lsit.append(add)
    add = get_possible_values1(numbers, i + 1, carry * int(numbers[i]) if carry != 0 else numbers[i], ret_lsit)
    if add is not None: ret_lsit.append(add)


def get_possible_values2(numbers, i, carry, ret_lsit):
    if i == len(numbers):
        return carry
    add = get_possible_values2(numbers, i + 1, carry + int(numbers[i]), ret_lsit)
    if add is not None: ret_lsit.append(add)
    add = get_possible_values2(numbers, i + 1, carry * int(numbers[i]) if carry != 0 else numbers[i], ret_lsit)
    if add is not None: ret_lsit.append(add)
    add = get_possible_values2(numbers, i + 1, combine_ints(carry, int(numbers[i])) if carry != 0 else numbers[i], ret_lsit)
    if add is not None: ret_lsit.append(add)

def combine_ints(num1, num2):
    len_first = len(str(num2))
    return num2 + num1 * pow(10, len_first)
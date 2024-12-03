import re

from util import read_file


def part1():
    input_list = read_file()
    matches = []
    ret_sum = 0

    for line in input_list:
        matches += re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)

    for match in matches:
        ret_sum += mul(match)

    return ret_sum

def mul(match: str):
    x, y = match[4:-1].split(",")
    return int(x) * int(y)

def part2():
    matches = []
    enable = True
    ret_sum = 0

    for line in read_file():
        matches += re.findall(
            r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)",
            line
        )

    for match in matches:
        if match == "do()": enable = True
        elif match == "don't()": enable = False
        else:
            if enable:
                ret_sum += mul(match)

    return ret_sum
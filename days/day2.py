from util import read_file


def part1():
    input_list = read_file()
    reports = [[int(num) for num in line.split()] for line in input_list]
    counter = 0

    for report in reports:
        if safety_check(report): counter += 1

    return counter


def safety_check(arr):
    increasing = arr[0] < arr[1]
    for i in range(1, len(arr)):
        dif = abs(arr[i - 1] - arr[i])
        if dif > 3 or dif < 1:
            return False
        if (arr[i - 1] < arr[i]) ^ increasing:
            return False
    return True


def part2():
    input_list = read_file()
    reports = [[int(num) for num in line.split()] for line in input_list]
    counter = 0

    for report in reports:
        if unsafer_safety_check(report): counter += 1

    return counter


def unsafer_safety_check(arr):
    increasing = arr[0] < arr[1]
    for i in range(1, len(arr)):
        dif = abs(arr[i - 1] - arr[i])
        if dif > 3 or dif < 1:
            return try_without_one(arr)
        if (arr[i - 1] < arr[i]) ^ increasing:
            return try_without_one(arr)
    return True


def try_without_one(arr):
    for i in range(len(arr)):
        num = arr[i]
        arr.pop(i)
        if safety_check(arr): return True
        arr.insert(i, num)
    return False

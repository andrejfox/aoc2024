from util import read_file

def part1():
    input_list = read_file()
    left_list = []
    right_list = []
    total_distance = 0

    for line in input_list:
        nums = [int(num) for num in line.split()]
        left_list.append(nums[0])
        right_list.append(nums[1])

    left_list.sort()
    right_list.sort()

    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)

    return total_distance

def part2():
    input_list = read_file()
    left_list = []
    right_list = []
    similarity_score = 0

    for line in input_list:
        nums = [int(num) for num in line.split()]
        left_list.append(nums[0])
        right_list.append(nums[1])

    for element in left_list:
        similarity_score += right_list.count(element) * element

    return similarity_score
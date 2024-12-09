from util import read_file


def part1():
    input_map = read_file()
    directions = ["^", ">", "V", "<"]
    x, y = 0, 0
    ret_sum = 0

    for i, line in enumerate(input_map):
        x_, y = [line.find(x) for x in directions if x in line], i
        if len(x_) != 0:
            x = x_[0]
            break

    direction = input_map[y][x]

    while not at_wall(input_map, x, y, direction):
        if at_obstruction(input_map, x, y, direction):
            direction = directions[directions.index(direction) + 1] if direction != "<" else "^"
            input_map[y] = replace_char(input_map[y], x, direction)
        else:
            input_map[y] = replace_char(input_map[y], x, "X")
            input_map, x, y = move(input_map, x, y, direction)

    for line in input_map:
        for char in line:
            if char == "X":
                ret_sum += 1

    return ret_sum + 1


def part2():
    input_map = read_file()
    directions = ["^", ">", "V", "<"]
    x, y = 0, 0
    ret_sum = 0

    for i, line in enumerate(input_map):
        x_, y = [line.find(x) for x in directions if x in line], i
        if len(x_) != 0:
            x = x_[0]
            break

    sx, sy = x, y

    direction = input_map[y][x]
    start_direction = direction

    while not at_wall(input_map, x, y, direction):
        if at_obstruction(input_map, x, y, direction):
            direction = directions[directions.index(direction) + 1] if direction != "<" else "^"
            input_map[y] = replace_char(input_map[y], x, direction)
        else:
            input_map[y] = replace_char(input_map[y], x, "X")
            input_map, x, y = move(input_map, x, y, direction)

    input_map[y] = replace_char(input_map[y], x, "X")
    input_map[sy] = replace_char(input_map[sy], sx, start_direction)

    for yy, line in enumerate(input_map):
        for xx, char in enumerate(line):
            if char != "X":
                continue

            copy_map = input_map[:]
            copy_map[yy] = replace_char(copy_map[yy], xx, "#")

            x, y = sx, sy
            direction = start_direction

            count = 0
            loop = True
            while count < 10000:
                if not at_wall(copy_map, x, y, direction):
                    count += 1
                    if at_obstruction(copy_map, x, y, direction):
                        direction = directions[directions.index(direction) + 1] if direction != "<" else "^"
                        copy_map[y] = replace_char(copy_map[y], x, direction)
                    else:
                        copy_map[y] = replace_char(copy_map[y], x, "X")
                        copy_map, x, y = move(copy_map, x, y, direction)
                else:
                    loop = False
                    count = 100000

            if loop:
                ret_sum += 1

    return ret_sum


def at_wall(input_map, x, y, direction):
    if direction == "^":
        if y < 1:
            return True
    elif direction == ">":
        if x == len(input_map[y]) - 1:
            return True
    elif direction == "V":
        if y == len(input_map) - 1:
            return True
    elif direction == "<":
        if x < 1:
            return True
    else: return False


def at_obstruction(input_map, x, y, direction):
    if direction == "^":
        if input_map[y - 1][x] == "#":
            return True
    elif direction == ">":
        if input_map[y][x + 1] == "#":
            return True
    elif direction == "V":
        if input_map[y + 1][x] == "#":
            return True
    elif direction == "<":
        if input_map[y][x - 1] == "#":
            return True
    else: return False


def move(input_map, x, y, direction):
    if direction == "^":
        input_map[y - 1] = replace_char(input_map[y - 1], x, "^")
        return input_map, x, y - 1
    elif direction == ">":
        input_map[y] = replace_char(input_map[y], x + 1, ">")
        return input_map, x + 1, y
    elif direction == "V":
        input_map[y + 1] = replace_char(input_map[y + 1], x, "V")
        return input_map, x, y + 1
    else:
        input_map[y] = replace_char(input_map[y], x - 1, "<")
        return input_map, x - 1, y


def replace_char(string, index, new_char):
    if 0 <= index < len(string):
        return string[:index] + new_char + string[index + 1:]
    else:
        raise IndexError("Index out of range")
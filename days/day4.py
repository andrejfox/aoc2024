from util import read_file


def part1():
    input_list = read_file()
    sum = 0
    for i in range(len(input_list)):
        cur_hit = input_list[i].find("X")
        processed_hits = set()
        while cur_hit != -1:
            if cur_hit in processed_hits:
                cur_hit = input_list[i].find("X", cur_hit + 1)
                continue
            possibles = get_possible_lines(input_list, cur_hit, i)
            for possible in possibles:
                possible = "".join(possible)
                if "XMAS" in possible or "SAMX" in possible:
                    print(f"y:{i} x:{cur_hit} {possible}")
                sum += 1 if "XMAS" in possible else 0
                sum += 1 if "SAMX" in possible else 0
            processed_hits.add(cur_hit)
            cur_hit = input_list[i].find("X", cur_hit + 1)
    return sum


def get_possible_lines(input_list, x, y):
    ret = []
    list_len = len(input_list)
    line_len = len(input_list[0])

    min_x = max(0, x - 3)
    max_x = min(line_len, x + 4)
    min_y = max(0, y - 3)
    max_y = min(list_len, y + 4)

    ret.append([line[x] for line in input_list[min_y:max_y]])
    ret.append([input_list[y][curr_x] for curr_x in range(min_x, max_x)])

    ret.append([
        input_list[y + i][x + i]
        for i in range(-3, 4)
        if 0 <= y + i < list_len and 0 <= x + i < line_len
    ])

    ret.append([
        input_list[y - i][x + i]
        for i in range(-3, 4)
        if 0 <= y - i < list_len and 0 <= x + i < line_len
    ])

    return ret


def part2():
    input_list = read_file()
    sum = 0

    for i in range(len(input_list)):
        cur_hit = input_list[i].find("A")
        while cur_hit != -1:
            if i - 1 < 0 or cur_hit - 1 < 0 or i + 1 > len(input_list) - 1 or cur_hit + 1 > len(input_list[0]) - 1:
                input_list[i] = input_list[i][:cur_hit] + "*" + input_list[i][cur_hit + 1:]
                cur_hit = input_list[i].find("A")
            else:
                diagonal1 = "".join([input_list[i - 1][cur_hit - 1],
                                     "A",
                                     input_list[i + 1][cur_hit + 1]
                                     ])
                diagonal2 = "".join([input_list[i + 1][cur_hit - 1],
                                     "A",
                                     input_list[i - 1][cur_hit + 1]
                                     ])
                if diagonal1.count("SAM") + diagonal1.count("MAS") > 0 and diagonal2.count("SAM") + diagonal2.count("MAS") > 0:
                    sum += 1
                    print(f"sum: {sum} | y: {i} x: {cur_hit} | d1: {diagonal1} d2: {diagonal2}")
                input_list[i] = input_list[i][:cur_hit] + "*" + input_list[i][cur_hit + 1:]
                cur_hit = input_list[i].find("A")

    return  sum
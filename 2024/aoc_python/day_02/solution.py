import re

def part1(input_data) -> int:
    total = 0
    parsed_input = re.findall(r'mul\((\d+),(\d+)\)', input_data)
    # [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]
    for pair in parsed_input:
        total += abs(int(pair[0]) * int(pair[1]))
    return total

def part2(input_data):
    parsed_input = [''.join(t) if t[0] == '' else (t[0], t[1]) for t in re.findall(r'mul\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\)', input_data)]
    # [('2', '4'), "don't", ('5', '5'), ('11', '8'), 'do', ('8', '5')]
    isEnable = True
    total = 0

    for item in parsed_input:
        if item == "do":
            isEnable = True
        elif item == "don't":
            isEnable = False
        else:
            if isEnable:
                total += abs(int(item[0]) * int(item[1]))
    return total


def main():
    input_data = open("input.txt", "r").read()
    print("Solution for day 3")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))


main()
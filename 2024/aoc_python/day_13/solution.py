import time
from pprint import pprint as pp
import re 

def parse_input(input_data):
    groups = input_data.split("\n\n")
    ecuations = []
    for g in groups:
        first_line, second_line, third_line = g.split("\n")

        first_line = re.findall(r"(\d+)", first_line)

        first_line = (int(first_line[0]), int(first_line[1]))
        second_line = re.findall(r"(\d+)", second_line)
        second_line = (int(second_line[0]), int(second_line[1]))

        third_line = re.findall(r"(\d+)", third_line)
        third_line = (int(third_line[0]), int(third_line[1]))

        ecuations.append((first_line, second_line, third_line))
    return ecuations


def is_valid(x, y, letters_map):
    return x >= 0 and y >= 0 and x < len(letters_map) and y < len(letters_map[0])



def part1(input_data):
    ecuations = parse_input(input_data)
    solutions = []
    for e in ecuations:
        first, second, third = e

        a1 = first[0] / second[0]
        a2 = first[1] / second[1]

        c1 = third[0] / second[0]
        c2 = third[1] / second[1]


        diff_s = a1 - a2
        diff_x = c1 - c2
        diff_y = (a1 * c2) - (a2 * c1)

        x = round(diff_x / diff_s, 2)
        y = round(diff_y / diff_s, 2)

        if x % 1 == 0 and y % 1 == 0:
            solutions.append((x, y))
    total = 0

    for s in solutions:
        if s[0] >= 0 and s[1] >= 0 and s[0] <= 100 and s[1] <= 100:
            total += s[0]*3 + s[1]

    return int(total)
def part2(input_data):
    ecuations = parse_input(input_data)
    solutions = []
    for e in ecuations:
        first, second, third = e

        a1 = first[0] / second[0]
        a2 = first[1] / second[1]

        c1 = (third[0] + 10000000000000) / second[0] 
        c2 = (third[1] + 10000000000000) / second[1]


        diff_s = a1 - a2
        diff_x = c1 - c2
        diff_y = (a1 * c2) - (a2 * c1)

        x = round(diff_x / diff_s, 2)
        y = round(diff_y / diff_s, 2)

        if x % 1 == 0 and y % 1 == 0:
            solutions.append((x, y))
    total = 0

    for s in solutions:
        if s[0] >= 0 and s[1] >= 0:
            total += s[0]*3 + s[1]

    return int(total)


def main():
    st = time.time()

    input_data = open("./input.txt", "r").read()
    print("Solution for day 13")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))

    et = time.time()

    print("Execution time in seconds: ", et-st)


main()

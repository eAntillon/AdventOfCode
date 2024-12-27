import time
from pprint import pprint


def parse_input(input_data):
    patterns, designs = input_data.split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.split("\n")
    patterns.sort(key=lambda x:  x.count("g"), reverse=True)

    return patterns, designs


def is_valid(memory, position):
    x, y = position
    return x >= 0 and y >= 0 and y < len(memory) and x < len(memory[0])


def validate_pattern(current_pattern, patterns_applied, patterns, design: str):
    patterns_applied.append(current_pattern)
    design = design.replace(current_pattern, "0")
    solutions = []
    if design.count("0") == len(design):
        solutions.append(patterns_applied)
        return solutions
    for p in patterns:
        if p in design and p not in patterns_applied:
            new_solutions = validate_pattern(
                p, patterns_applied.copy(), patterns, design)
            if len(new_solutions) >= 1:
                solutions.append(new_solutions)
    return solutions


def part1(input_data):
    patterns, designs = parse_input(input_data)
    # print(patterns, len(patterns))
    correct = {}

    for design in designs:
        for p in patterns:
            if p in design:
                solutions = validate_pattern(
                    p, [], patterns, design)
                if len(solutions) >= 1:
                    correct[design] = solutions

    possible = 0
    for k, v in correct.items():
        possible += len(v)

    print("Possible: ", possible)

    pprint(correct)
    return len(correct.items())


def part2(input_data):
    pass


if __name__ == "__main__":
    st = time.perf_counter()

    input_data = open("./input.txt", "r").read()
    print("Solution for day 19")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))

    et = time.perf_counter()

    print("Execution time in seconds: ", et-st)

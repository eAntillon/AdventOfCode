import time
import re

STEPS = 100
MAX_X = 101
MAX_Y = 103


def parse_input(input_data):
    lines = input_data.split("\n")
    robots = []
    for line in lines:
        numbers = [int(x) for x in re.findall(r"(-?\d+)", line)]
        robots.append((numbers[0], numbers[1], numbers[2], numbers[3]))

    return robots


def is_valid(x, y, letters_map):
    return x >= 0 and y >= 0 and x < len(letters_map) and y < len(letters_map[0])


def get_robots(robots, steps=STEPS, part1=True):
    total = 0
    final_positions = []

    for r in robots:
        x, y, dx, dy = r
        steps_x = (dx * steps) % MAX_X
        steps_y = (dy * steps) % MAX_Y

        while steps_x > 0:
            if x == MAX_X - 1:
                x = 0
            else:
                x += 1
            steps_x -= 1
        while steps_y > 0:
            if y == MAX_Y - 1:
                y = 0
            else:
                y += 1
            steps_y -= 1
        
        final_positions.append((x, y))

    if not part1:
        return final_positions

    if part1:
        total = 0
        middle_x = MAX_X // 2
        middle_y = MAX_Y // 2
        
        q1_x = range(0, middle_x)
        q1_y = range(0, middle_y)

        q2_x = range(middle_x, MAX_X)
        q2_y = range(0, middle_y)

        q3_x = range(0, middle_x)
        q3_y = range(middle_y, MAX_Y)

        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0

        for pos in final_positions:
            if pos[0] == middle_x or pos[1] == middle_y:
                continue
            if pos[0] in q1_x and pos[1] in q1_y:
                q1 += 1
            elif pos[0] in q2_x and pos[1] in q2_y:
                q2 += 1
            elif pos[0] in q3_x and pos[1] in q3_y:
                q3 += 1
            else:
                q4 += 1

        total = q1 * q2 * q3 * q4
        return total


def part1(input_data):
    robots = parse_input(input_data)
    total = get_robots(robots)
    return total


def part2(input_data):
    search = "#" * 10
    original = ["." for _ in range(MAX_X)]
    robots = parse_input(input_data)
    result = 0
    for i in range(7338, 10_000):
        print("Iteration: ", i)
        positions = get_robots(robots, i, part1=False)
        for j in range(MAX_Y):
            line = original.copy()
            insterted = 0
            for k in range(MAX_X):
                if (k, j) in positions:
                    line[k] = "#"
                    insterted += 1
            if insterted > 10:
                if "".join(line).find(search) != -1:
                    result = i
            print("".join(line))
        print("\n\n")
        if result != 0:
            break
    return result


if __name__ == "__main__":
    st = time.time()

    input_data = open("./input.txt", "r").read()
    print("Solution for day 14")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))

    et = time.time()

    print("Execution time in seconds: ", et-st)

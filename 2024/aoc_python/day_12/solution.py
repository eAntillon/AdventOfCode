import time
from pprint import pprint as pp


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def parse_input(input_data):
    return [list(x) for x in input_data.split("\n")]


def is_valid(x, y, letters_map):
    return x >= 0 and y >= 0 and x < len(letters_map) and y < len(letters_map[0])


def add_area(letter, area, letters_map):
    if letter not in letters_map:
        letters_map[letter] = {
            "area": set(),
            "perimeter": []
        }
    letters_map[letter]["area"].add(area)


def add_perimeter(letter, perimeter, letters_map):
    if letter not in letters_map:
        letters_map[letter] = {
            "area": set(),
            "perimeter": []
        }
    letters_map[letter]["perimeter"].append(perimeter)


def close_area(letter, letters_map):
    if letter not in letters_map:
        return 0
    c = letters_map[letter]
    del letters_map[letter]

    print("Letter: ", letter)
    # count sides of the area, not the perimeter

    print("Perimetes", c["perimeter"])
    lines = set()
    for p in c["perimeter"]:
        # search in any four directions to find the complete side
        find_line = []

        # search in i direction
        
        # for i in range(len(directions)):
        #     neighbor_x = p[0] + directions[i][0]
        #     neighbor_y = p[1] + directions[i][1]
        #     if (neighbor_x, neighbor_y) in c["perimeter"]:
        #         find_line.append((neighbor_x, neighbor_y))
        #         break
        # sort array of tuples
        find_line.sort()
        print("Find line: ", find_line)

    return len(c["area"]) * len(c["perimeter"])


def part1(input_data):
    garden = parse_input(input_data)
    q = []
    q.append((0, 0))
    visited = set()
    total = 0

    other_letter_q = []
    letters_map = {}

    while q:
        x, y = q.pop(0)
        letter = garden[x][y]

        if (x, y) in visited:
            if len(q) == 0 and len(other_letter_q) > 0:
                next_letter = other_letter_q.pop(0)
                q.append(next_letter)
                total += close_area(letter, letters_map)

            continue
        add_area(letter, (x, y), letters_map)
        visited.add((x, y))

        for i in range(len(directions)):
            neighbor_x = x + directions[i][0]
            neighbor_y = y + directions[i][1]
            if is_valid(neighbor_x, neighbor_y, garden):
                if garden[neighbor_x][neighbor_y] == letter:
                    add_area(letter, (neighbor_x, neighbor_y), letters_map)
                    if (neighbor_x, neighbor_y) not in visited:
                        q.append((neighbor_x, neighbor_y))
                else:
                    add_perimeter(letter, (neighbor_x, neighbor_y), letters_map)
                    other_letter_q.append((neighbor_x, neighbor_y))
            else:
                add_perimeter(letter, (neighbor_x, neighbor_y), letters_map)

        if len(q) == 0:
            next_letter = other_letter_q.pop(0)
            q.append(next_letter)
            total += close_area(letter, letters_map)

    for k, v in letters_map.items():
        total += len(v["area"]) * len(v["perimeter"])
    return total

def part2(input_data):
    pass


def main():
    st = time.time()

    input_data = open("./input.txt", "r").read()
    print("Solution for day 12")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))

    et = time.time()

    print("Execution time in seconds: ", et-st)


main()

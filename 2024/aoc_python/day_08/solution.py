
def parse_input(input_data):
    input_map = [list(x) for x in input_data.split("\n")]
    antenas_positions = {}
    for i in range(len(input_map)):
        for j in range(len(input_map[i])):
            if input_map[i][j] != ".":
                if antenas_positions.get(input_map[i][j]) is None:
                    antenas_positions[input_map[i][j]] = [(i, j)]
                else:
                    antenas_positions[input_map[i][j]].append((i, j))

    return input_map, antenas_positions


def is_valid_position(pos, input_map):
    i, j = pos
    return 0 <= i < len(input_map) and 0 <= j < len(input_map[0])


def part1(input_data):
    input_map, antenas_positions = parse_input(input_data)
    antinodes = set()
    for _, v in antenas_positions.items():
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                first_antena = v[i]
                second_antena = v[j]

                distance_i = abs(first_antena[0] - second_antena[0])
                distance_j = abs(first_antena[1] - second_antena[1])

                first_antinode = (
                    first_antena[0] + (distance_i if first_antena[0] > second_antena[0] else -distance_i),
                    first_antena[1] + (distance_j if first_antena[1] > second_antena[1] else -distance_j)
                )
                second_antinode = (
                    second_antena[0] + (-distance_i if first_antena[0] > second_antena[0] else distance_i),
                    second_antena[1] + (-distance_j if first_antena[1] > second_antena[1] else distance_j)
                )
                if is_valid_position(first_antinode, input_map):
                    input_map[first_antinode[0]][first_antinode[1]] = "#"
                    antinodes.add(first_antinode)

                if is_valid_position(second_antinode, input_map):
                    input_map[second_antinode[0]][second_antinode[1]] = "#"
                    antinodes.add(second_antinode)

    return len(antinodes)


def part2(input_data):
    input_map, antenas_positions = parse_input(input_data)
    antinodes = set()
    for _, v in antenas_positions.items():
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                first_antena = v[i]
                second_antena = v[j]
                antinodes.add(first_antena)
                antinodes.add(second_antena)

                distance_i = abs(first_antena[0] - second_antena[0])
                distance_j = abs(first_antena[1] - second_antena[1])

                first_antinode = (
                    first_antena[0] + (distance_i if first_antena[0] > second_antena[0] else -distance_i),
                    first_antena[1] + (distance_j if first_antena[1] > second_antena[1] else -distance_j)
                )
                second_antinode = (
                    second_antena[0] + (-distance_i if first_antena[0] > second_antena[0] else distance_i),
                    second_antena[1] + (-distance_j if first_antena[1] > second_antena[1] else distance_j)
                )

                while is_valid_position(first_antinode, input_map):
                    antinodes.add(first_antinode)
                    input_map[first_antinode[0]][first_antinode[1]] = "#"
                    first_antinode = (
                        first_antinode[0] + (distance_i if first_antena[0] > second_antena[0] else -distance_i),
                        first_antinode[1] + (distance_j if first_antena[1] > second_antena[1] else -distance_j)
                    )

                while is_valid_position(second_antinode, input_map):
                    antinodes.add(second_antinode)
                    input_map[second_antinode[0]][second_antinode[1]] = "#"
                    second_antinode = (
                        second_antinode[0] + (-distance_i if first_antena[0] > second_antena[0] else distance_i),
                        second_antinode[1] + (-distance_j if first_antena[1] > second_antena[1] else distance_j)
                    )

    return len(antinodes)

def main():
    input_data = open("./input.txt", "r").read()
    print("Solution for day 8")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))


main()

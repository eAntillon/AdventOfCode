

def parse_input(input_data):
    lines = [list(x) for x in input_data.strip().split("\n")]
    lines = [list(map(lambda x: int(x), x)) for x in lines]
    return lines

def is_valid(topo_map, i, j):
    if i < 0 or i >= len(topo_map):
        return False
    if j < 0 or j >= len(topo_map[i]):
        return False
    return True

def part1(input_data):
    topo_map = parse_input(input_data)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    total_paths = 0
    for i in range(len(topo_map)):
        for j in range(len(topo_map[i])):
            if topo_map[i][j] == 0:
                q = []
                q.append((i, j))
                hiking_trail = set()

                paths = 0
                while len(q) > 0:
                    x, y = q.pop(0)
                    current_value = topo_map[x][y]
                    for k in range(0, 4):
                        if is_valid(topo_map, x + directions[k][0], y + directions[k][1]):
                            if topo_map[x + directions[k][0]][y + directions[k][1]] == current_value + 1:
                                if topo_map[x + directions[k][0]][y + directions[k][1]] == 9:
                                    # comment this if line for part 2 solution
                                    if (x + directions[k][0], y + directions[k][1]) not in hiking_trail:
                                        hiking_trail.add((x + directions[k][0], y + directions[k][1]))
                                        paths += 1
                                    continue
                                else:
                                    q.append((x + directions[k][0], y + directions[k][1]))
                total_paths += paths 
    return total_paths

# def part2(input_data):
#    pass

def main():
    input_data = open("./input.txt", "r").read()
    print("Solution for day 10")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part1(input_data))


main()

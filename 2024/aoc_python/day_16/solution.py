import time


def parse_input(input_data):
    maze = [list(x) for x in input_data.split("\n")]
    return maze


def is_valid(pool, position):
    x, y = position
    return x >= 0 and y >= 0 and x < len(pool) and y < len(pool[0])


def add_parents(dict, p, c):
    if c not in dict:
        dict[c] = []
    dict[c].append(p)


def part1(input_data):
    maze = parse_input(input_data)
    s = (0, 0)
    e = (0, 0)

    parents = {}

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                s = (i, j, 0, "RIGHT")
            if maze[i][j] == "E":
                e = (i, j)
    visited = {
        (s[0], s[1]): 0
    }
    q = [s]

    for i in [(0, 1, "RIGHT"), (1, 0, "UP"), (0, -1, "LEFT"), (-1, 0, "UP")]:
        x = s[0] + i[0]
        y = s[1] + i[1]
        d = i[2]
        if is_valid(maze, (x, y)) and maze[x][y] != "#":
            c = 1
            if d != "RIGHT":
                c += 1000
            q.append((x, y, c, d))
            add_parents(parents, (s[0], s[1]), (x, y, d))

    # print("Starting positions", q)
    solutions = []
    while q:
        x, y, c, d = q.pop(0)

        if (x, y) == e:
            solutions.append((x, y, c, d))
            continue

        if (x, y) in visited and visited[(x, y)] < c:
            continue
        else:
            visited[(x, y)] = c

        if is_valid(maze, (x+1, y)) and maze[x+1][y] != "#" and d != "UP":  # DOWN
            new_c = c + 1
            if d != "DOWN":
                new_c += 1000
            q.append((x+1, y, new_c, "DOWN"))
            add_parents(parents, (x, y, new_c), (x+1, y))

        if is_valid(maze, (x-1, y)) and maze[x-1][y] != "#" and d != "DOWN":  # UP
            new_c = c + 1
            if d != "UP":
                new_c += 1000
            q.append((x-1, y, new_c, "UP"))
            add_parents(parents, (x, y, new_c), (x-1, y))

        # RIGHT
        if is_valid(maze, (x, y+1)) and maze[x][y+1] != "#" and d != "LEFT":
            new_c = c + 1
            if d != "RIGHT":
                new_c += 1000
            q.append((x, y+1, new_c, "RIGHT"))
            add_parents(parents, (x, y, new_c), (x, y+1))

        if is_valid(maze, (x, y-1)) and maze[x][y-1] != "#" and d != "RIGHT":  # LEFT
            new_c = c + 1
            if d != "LEFT":
                new_c += 1000
            q.append((x, y-1, new_c, "LEFT"))
            add_parents(parents, (x, y, new_c), (x, y-1))

    min_sol = min(solutions, key=lambda x: x[2])

    sits = get_sits((min_sol[0], min_sol[1], min_sol[2]),
                    parents, min_sol[2], set())
    for s in sits:
        maze[s[0]][s[1]] = "O"
    for m in maze:
        print("".join(m))

    print("Part 1: ", min_sol[2])
    print("Part 2: ", len(sits)+1)
    return min_sol[2]


def get_sits(pos, parents, solution, sits):
    new_sits = set()
    # print("-"*70)
    # print(f"Getting sits for {pos} - {solution}")
    pos_key = (pos[0], pos[1])
    pos_cost = pos[2]
    # print("Parents: ")

    if pos_key not in parents:
        # print("No parents found for:", pos)
        return new_sits
    pos_parents = list(set(parents[pos_key]))  # get parents
    # pprint(pos_parents)

    for p in pos_parents:
        parent_cost = p[2]
        if (p[0], p[1]) in sits:
            continue
        if (p[0], p[1]) == pos:
            continue
        if pos_cost == solution:
            if parent_cost == pos_cost or parent_cost == pos_cost - 1 or parent_cost == pos_cost - 1000:
                new_sits.add((p[0], p[1]))
                parent_sits = get_sits(
                    p, parents, pos_cost, new_sits.union(sits))
                new_sits = new_sits.union(parent_sits)
        else:
            if parent_cost+1 == solution or parent_cost+1001 == solution or parent_cost == pos_cost-1 or parent_cost == pos_cost-1001:
                new_sits.add((p[0], p[1]))
                parent_sits = get_sits(
                    p, parents, pos_cost, new_sits.union(sits))
                new_sits = new_sits.union(parent_sits)

    return new_sits


def part2(input_data):
    pass


if __name__ == "__main__":
    st = time.perf_counter()

    input_data = open("./input.txt", "r").read()
    print("Solution for day 16")
    # print("Part 1: ", part1(input_data))
    # print("Part 2: ", part2(input_data))
    part1(input_data)

    et = time.perf_counter()

    print("Execution time in seconds: ", et-st)

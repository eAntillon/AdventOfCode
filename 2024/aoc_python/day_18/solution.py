import time


def parse_input(input_data):
    lines = input_data.split("\n")
    cords = []
    for line in lines:
        x, y = line.split(",")
        cords.append((int(x), int(y)))
    return cords


def is_valid(memory, position):
    x, y = position
    return x >= 0 and y >= 0 and y < len(memory) and x < len(memory[0])


def part1(input_data):
    cords = parse_input(input_data)
    corrupted_bytes = 1024

    memory = [["." for _ in range(71)] for _ in range(71)]

    end = (70, 70)

    directions = [(0, 1, "DOWN"), (1, 0, "RIGHT"),
                  (0, -1, "UP"), (-1, 0, "LEFT")]

    i = 0
    while i < corrupted_bytes:
        x, y = cords[i]
        memory[y][x] = "#"
        i += 1

    q = []

    for dir in directions:
        q.append((0, 0, 0, dir[2]))

    visited = {}
    parents = {}

    while q:
        x, y, c, d = q.pop(0)
        if (x, y, d) in visited:
            if c < visited[(x, y, d)]:
                visited[(x, y, d)] = c
            else:
                continue
        else:
            visited[(x, y, d)] = c

        if (x, y) == end:
            break

        for dx, dy, dd in directions:
            nx = x + dx
            ny = y + dy
            nd = dd
            nc = c + 1
            if is_valid(memory, (nx, ny)) and memory[ny][nx] == ".":
                parents[(nx, ny)] = (x, y, c, d)
                q.append(((nx, ny, nc, nd)))

    for row in memory:
        print("".join(row))

    for k, v in visited.items():
        x, y, d = k
        c = v
        if (x, y) == end:
            print(f"End: {x}, {y}, {d}, {c}")
            return c
    return 0


def part2(input_data):
    print("Part 2")
    cords = parse_input(input_data)
    n = 1024
    corrupted_bytes = 1024
    memory = [["." for _ in range(71)] for _ in range(71)]
    end = (70, 70)
    directions = [(0, 1, "DOWN"), (1, 0, "RIGHT"),
                  (0, -1, "UP"), (-1, 0, "LEFT")]

    # first 1024 corrupted bytes added
    i = 0
    while i < corrupted_bytes:
        x, y = cords[i]
        memory[y][x] = "#"
        i += 1

    while True:
        if n > 1024:
            print(f"Adding {cords[n - 1]} corrupted bytes")
            x, y = cords[n - 1]
            memory[y][x] = "#"

        q = []
        for dir in directions:
            q.append((0, 0, 0, dir[2]))
        visited = {}
        parents = {}
        while q:
            x, y, c, d = q.pop(0)
            if (x, y, d) in visited:
                if c < visited[(x, y, d)]:
                    visited[(x, y, d)] = c
                else:
                    continue
            else:
                visited[(x, y, d)] = c

            if (x, y) == end:
                break

            for dx, dy, dd in directions:
                nx = x + dx
                ny = y + dy
                nd = dd
                nc = c + 1
                if is_valid(memory, (nx, ny)) and memory[ny][nx] == ".":
                    parents[(nx, ny)] = (x, y, c, d)
                    q.append(((nx, ny, nc, nd)))

        # for row in memory:
        #     print("".join(row))

        result = None
        for k, v in visited.items():
            x, y, d = k
            c = v
            if (x, y) == end:
                # print(f"End: {x}, {y}, {d}, {c}")
                result = c
        if result is None:
            return cords[n - 1]

        n += 1


if __name__ == "__main__":
    st = time.perf_counter()

    input_data = open("./input.txt", "r").read()
    print("Solution for day 18")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))

    et = time.perf_counter()

    print("Execution time in seconds: ", et-st)

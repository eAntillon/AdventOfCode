from functools import lru_cache

input_lines = open("./input/day21.txt", "r").readlines()
input_lines = [[*line.strip()] for line in input_lines]
start = (0, 0)
for i in input_lines:
    if "S" in i:
        start = (i.index("S"), input_lines.index(i))

valid_positions = []
available_steps = 64


@lru_cache(maxsize=None)
def get_neighbours(pos):
    i, j = pos
    neighbours = []
    extra_i = None
    extra_j = None

    if i < 0:
        extra_i = i
        i = len(input_lines) - (abs(i) % len(input_lines))

    if i >= len(input_lines):
        extra_i = i
        i = i % len(input_lines) - 1

    if j < 0:
        extra_j = j
        j = len(input_lines[0]) - (abs(j) % len(input_lines[0]))

    if j >= len(input_lines[0]):
        extra_j = j
        j = j % len(input_lines[0]) - 1

    if extra_i is None:
        extra_i = i
    if extra_j is None:
        extra_j = j

    if i > 0:
        if input_lines[i - 1][j] != "#":
            neighbours.append((extra_i - 1, extra_j))
    else:
        if input_lines[len(input_lines) - 1][j] != "#":
            neighbours.append((extra_i - 1, extra_j))
    if i < len(input_lines) - 1:
        if input_lines[i + 1][j] != "#":
            neighbours.append((extra_i + 1, extra_j))
    else:
        if input_lines[0][j] != "#":
            neighbours.append((extra_i + 1, extra_j))
    if j > 0:
        if input_lines[i][j - 1] != "#":
            neighbours.append((extra_i, extra_j - 1))
    else:
        if input_lines[i][len(input_lines[0]) - 1] != "#":
            neighbours.append((extra_i, extra_j - 1))
        
    if j < len(input_lines[0]) - 1:
        if input_lines[i][j + 1] != "#":
            neighbours.append((extra_i, extra_j + 1))
    else:
        if input_lines[i][0] != "#":
            neighbours.append((extra_i, extra_j + 1))
    
    return neighbours


@lru_cache(maxsize=None)
def get_path(pos, steps):
    if steps == available_steps:
        if pos not in valid_positions:
            valid_positions.append(pos)
        return True
    for neighbour in get_neighbours(pos):
        get_path(neighbour, steps + 1)
    return False


print(get_path(start, 0))


new_map = input_lines.copy()
for i in valid_positions:
    new_map[i[0]][i[1]] = "0"
for i in new_map:
    print("".join(i))

print(valid_positions)
print(len(valid_positions))

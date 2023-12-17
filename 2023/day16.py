from enum import Enum

input_lines = open("./input/day16.txt").read().split("\n")


def direction_to_arrow(direction):
    if direction == "up":
        return "^"
    elif direction == "down":
        return "v"
    elif direction == "left":
        return "<"
    elif direction == "right":
        return ">"


cpy = input_lines.copy()

cpy = [list(i) for i in cpy]


# enum
class DIRECTIONS(Enum):
    up = 0
    right = 1
    down = 2
    left = 3


def addBeam(start, layout, states):
    i = start[0]
    j = start[1]
    direction = start[2]
    visited = states
    new_beams = []
    if i >= len(layout) or j >= len(layout[0]):
        return [visited, new_beams]
    while (i, j, direction) not in visited or layout[i][j] != ".":
        # print(
        #     f"From {layout[i][j]} ({i}, {j}) in direction {DIRECTIONS(direction).name}",
        #     end=" ",
        # )
        if layout[i][j] == "\\":
            if direction == DIRECTIONS.up:
                direction = DIRECTIONS.left
            elif direction == DIRECTIONS.down:
                direction = DIRECTIONS.right
            elif direction == DIRECTIONS.left:
                direction = DIRECTIONS.up
            elif direction == DIRECTIONS.right:
                direction = DIRECTIONS.down
        elif layout[i][j] == "/":
            if direction == DIRECTIONS.up:
                direction = DIRECTIONS.right
            elif direction == DIRECTIONS.down:
                direction = DIRECTIONS.left
            elif direction == DIRECTIONS.left:
                direction = DIRECTIONS.down
            elif direction == DIRECTIONS.right:
                direction = DIRECTIONS.up
        elif layout[i][j] == "-":
            if direction == DIRECTIONS.up or direction == DIRECTIONS.down:
                # split in two
                direction = DIRECTIONS.left
                new_beams.append((i, j + 1, DIRECTIONS.right))
            elif direction == DIRECTIONS.left or direction == DIRECTIONS.right:
                # just pass
                pass
        elif layout[i][j] == "|":
            if direction == DIRECTIONS.up or direction == DIRECTIONS.down:
                # just pass
                pass
            elif direction == DIRECTIONS.left or direction == DIRECTIONS.right:
                # split in two
                direction = DIRECTIONS.up
                new_beams.append((i + 1, j, DIRECTIONS.down))
        visited[(i, j, direction)] = True
        if layout[i][j] == ".":
            cpy[i][j] = direction_to_arrow(DIRECTIONS(direction).name)
        if direction == DIRECTIONS.up:
            if i == 0:
                break
            i -= 1
        elif direction == DIRECTIONS.down:
            if i == len(layout) - 1:
                break
            i += 1
        elif direction == DIRECTIONS.left:
            if j == 0:
                break
            j -= 1
        elif direction == DIRECTIONS.right:
            if j == len(layout[0]) - 1:
                break
            j += 1
        if (i, j, direction) == start:
            break
        # print(
        #     f"to {layout[i][j]} ({i}, {j})  in direction {DIRECTIONS(direction).name}"
        # )

    return [visited, new_beams]


visited, new_beams = addBeam((0, 0, DIRECTIONS.right), input_lines, {})

peding = new_beams
while len(peding) > 0:
    new_beams = []
    for i in peding:
        # print("\nStart from", i)
        visited, n = addBeam(i, input_lines, visited)
        new_beams += n
    new_beams = list(set(new_beams))
    new_beams = [x for x in new_beams if x not in peding]
    peding = new_beams

filter_visited = []
for i in visited:
    if (i[0], i[1]) not in filter_visited:
        filter_visited.append((i[0], i[1]))

print("Part 1: ",len(filter_visited))


# produce a list of all top, bottom, left and right edges
top = [(0, x, DIRECTIONS.down) for x in range(len(input_lines[0]))]
top.append((0, 0, DIRECTIONS.right))
top.append((0, len(input_lines[0]) - 1, DIRECTIONS.left))
bottom = [(len(input_lines) - 1, x, DIRECTIONS.up) for x in range(len(input_lines[0]))]
bottom.append((len(input_lines) - 1, 0, DIRECTIONS.right))
bottom.append((len(input_lines) - 1, len(input_lines[0]) - 1, DIRECTIONS.left))
left = [(x, 0, DIRECTIONS.right) for x in range(len(input_lines))]
left.append((0, 0, DIRECTIONS.down))
left.append((len(input_lines) - 1, 0, DIRECTIONS.up))
right = [(x, len(input_lines[0]) - 1, DIRECTIONS.left) for x in range(len(input_lines))]
right.append((0, len(input_lines[0]) - 1, DIRECTIONS.down))
right.append((len(input_lines) - 1, len(input_lines[0]) - 1, DIRECTIONS.up))

edges = top + bottom + left + right
max_visited = 0
for i in edges:
    # print(f"{round((edges.index(i) / len(edges)) * 100, 2)}%", end="\r")

    visited, new_beams = addBeam(i, input_lines, {})
    peding = new_beams
    while len(peding) > 0:
        new_beams = []
        for i in peding:
            visited, n = addBeam(i, input_lines, visited)
            new_beams += n
        new_beams = list(set(new_beams))
        new_beams = [x for x in new_beams if x not in peding]
        peding = new_beams

    filter_visited = []
    for i in visited:
        if (i[0], i[1]) not in filter_visited:
            filter_visited.append((i[0], i[1]))

    if len(filter_visited) > max_visited:
        max_visited = len(filter_visited)
print("Part 2: ", max_visited)




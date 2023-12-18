input_lines = open("./input/day18.txt").read().split("\n")
points = []
#  create points
x = 0
y = 0

for line in input_lines:
    dir, steps, color = line.split(" ")
    steps = int(steps)
    match dir:
        case "R":
            for i in range(steps):
                x += 1
                points.append((x, y))
        case "L":
            for i in range(steps):
                x -= 1
                points.append((x, y))
        case "U":
            for i in range(steps):
                y += 1
                points.append((x, y))
        case "D":
            for i in range(steps):
                y -= 1
                points.append((x, y))

max_x = max(points, key=lambda x: x[0])[0]
min_x = min(points, key=lambda x: x[0])[0]
max_y = max(points, key=lambda x: x[1])[1]
min_y = min(points, key=lambda x: x[1])[1]

grid = [[0 for i in range(max_x - min_x + 1)] for j in range(max_y - min_y + 1)]

for point in points:
    x, y = point
    grid[y - min_y][x - min_x] = 1


# starting at middle
x = len(grid[0]) // 2
y = len(grid) // 2

grid[y][x] = 2


stack = [(x, y)]
visited = set()
# count 0 while not encountered 1
while len(stack) > 0:
    x, y = stack.pop()

    if grid[y][x] == 1:
        continue
    if (x, y) in visited:
        continue
    visited.add((x, y))
    # add all neighbors
    if x > 0:
        stack.append((x - 1, y))
    if y > 0:
        stack.append((x, y - 1))
    if x < len(grid[0]) - 1:
        stack.append((x + 1, y))
    if y < len(grid) - 1:
        stack.append((x, y + 1))

for i in visited:
    x, y = i
    grid[y][x] = 3

print(len(visited) + len(points))


# Part 2
points = []
#  create points
x = 0
y = 0
points_count = 0
for line in input_lines:
    _, _, color = line.split(" ")
    color = color[1 : len(color) - 1]
    hex = color[1:6]
    # hex to int
    n = int(hex, 16)
    dir = color[-1]
    print(color,hex, n, dir)
    points_count += n 
    match dir:
        case "0":
            x += n
            points.append((x, y))
        case "2":
            x -= n
            points.append((x, y))
        case "3":
            y += n
            points.append((x, y))
        case "1":
            y -= n
            points.append((x, y))

from shapely.geometry import Polygon

polygon = Polygon(points)
# I = (2A - B + 2) / 2 
area = polygon.area
b = points_count
i = (2 * area - b + 2) / 2
# print(i)
print(i + points_count)


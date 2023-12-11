input_lines = open("./input/day11.txt", "r", encoding="utf-8").read().split("\n")


class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.paths = {}

galaxies = []

for i in range(len(input_lines)):
    line = input_lines[i]
    for j in range(len(line)):
        char = line[j]
        if char == "#":
            galaxies.append(Galaxy(i, j))

not_galaxy_i = [x for x in range(len(input_lines))]
not_galaxy_j = [x for x in range(len(input_lines[0]))]

for galaxy in galaxies:
    if galaxy.x in not_galaxy_i:
        not_galaxy_i.remove(galaxy.x)
    if galaxy.y in not_galaxy_j:
        not_galaxy_j.remove(galaxy.y)

print(f"not_galaxy_i: {not_galaxy_i} not_galaxy_j: {not_galaxy_j}")


# part 1
# size_empy = 2

# part 2
size_empy = 1000000
for galaxy in galaxies:
    not_galaxy_i_less = [x for x in not_galaxy_i if x < galaxy.x]
    galaxy.x = galaxy.x + (len(not_galaxy_i_less)*(size_empy-1))

    not_galaxy_j_less = [x for x in not_galaxy_j if x < galaxy.y]
    galaxy.y = galaxy.y + (len(not_galaxy_j_less)*(size_empy-1))


for galaxy in galaxies:
    id = f"{galaxy.x},{galaxy.y}"
    for galaxy2 in galaxies:
        id2 = f"{galaxy2.x},{galaxy2.y}"
        if id != id2 and id not in galaxy2.paths:
            path = abs(galaxy.x - galaxy2.x) + abs(galaxy.y - galaxy2.y)
            galaxy.paths[id2] = path

acc = 0
for galaxy in galaxies:
    for path in galaxy.paths:
        acc += galaxy.paths[path]

print(f"acc: {acc}")

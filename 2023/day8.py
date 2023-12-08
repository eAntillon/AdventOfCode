input_lines = open("./input/day8.txt").read().split("\n")
maps = {}
coords = {}
instructions = [*input_lines[0].strip()]
index = 0
for line in input_lines[2:]:
    line = line.split("=")
    L, R = line[1].strip().replace("(", "").replace(")", "").replace(" ", "").split(",")
    key = line[0].strip()
    maps[key] = index
    coords[key] = (L, R)
    index += 1

for k, v in coords.items():
    coords[k] = (maps[v[0]], maps[v[1]])

reversed_maps = dict(map(reversed, maps.items()))

start = maps["AAA"]
end = maps["ZZZ"]
current = start
steps = 0
while True:
    i = 0
    while i < len(instructions) and current != end:
        key = reversed_maps[current]
        if instructions[i] == "L":
            current = coords[key][0]
        elif instructions[i] == "R":
            current = coords[key][1]
        i += 1
        steps += 1
    if current == end:
        break

print("Part 1:", steps)

# Part 2
start_nodes = []
end_nodes = []

for k in maps.keys():
    if k.endswith("A"):
        start_nodes.append(maps[k])
    elif k.endswith("Z"):
        end_nodes.append(maps[k])

# print("\033[91m" + "Start nodes: " + "\033[0m" + str(start_nodes))
def getStepsToZ(start):
    current = start
    steps = 0
    while True:
        for i in range(len(instructions)):
            key = reversed_maps[current]
            if instructions[i] == "L":
                current = coords[key][0]
            elif instructions[i] == "R":
                current = coords[key][1]
            steps += 1
        if current in end_nodes:
            return steps
steps = []
for n in start_nodes:
    steps.append(getStepsToZ(n))
from math import lcm
print("Part 2:", lcm(*steps))
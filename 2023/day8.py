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

# start = maps["AAA"]
# end = maps["ZZZ"]
# current = start
# steps = 0
# while True:
#     i = 0
#     while i < len(instructions) and current != end:
#         key = reversed_maps[current]
#         if instructions[i] == "L":
#             current = coords[key][0]
#         elif instructions[i] == "R":
#             current = coords[key][1]
#         i += 1
#         steps += 1
#     if current == end:
#         break

# print("Part 1:", steps)


# Part 2

start_nodes = []
end_nodes = []

# print in red

def switchInstruction(nodes, instruccion):
    new_nodes = []
    for node in nodes:
        key = reversed_maps[node]
        # print("\033[92m" + "Node: " + "\033[0m" + str(i) + " " + str(key) + " " + str(coords[key]))
        if instruccion == "L":
            new_nodes.append(coords[key][0])
        elif instruccion == "R":
            new_nodes.append(coords[key][1])
    return new_nodes


def allNodesAreIn(nodes, target):
    count = 0
    for node in nodes:
        if node in target:
            count += 1
        else:
            if count > 1:
                print(f"\033[95m %%%% Found: {count} in end \033[0m")
            return False
    return True

for k in maps.keys():
    if k.endswith("A"):
        start_nodes.append(maps[k])
    elif k.endswith("Z"):
        end_nodes.append(maps[k])

# print("\033[91m" + "Start nodes: " + "\033[0m" + str(start_nodes))
# print("\033[91m" + "End nodes: " + "\033[0m" + str(end_nodes))
steps = 1
all_in_end = False
while True:
    for i in range(len(instructions)):
        # print("\033[93m" + "Instruction: " + "\033[0m" + str(instructions[i]))
        start_nodes = switchInstruction(start_nodes, instructions[i])
        # print("\033[91m" + "New start nodes: " + "\033[0m" + str(start_nodes))
        if allNodesAreIn(start_nodes, end_nodes):
            all_in_end = True
            break
        steps += 1
    if all_in_end:
        break
# print("\033[91m" + "End nodes: " + "\033[0m" + str(end_nodes))
print("Part 2:", steps)

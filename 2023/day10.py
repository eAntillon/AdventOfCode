input_lines = open("./input/day10.txt", "r").read().split("\n")

# f = open("./day10_out.txt", "w", encoding='utf-8')
# new = input_lines.replace("|", "│").replace("-", "─").replace("L", "└").replace("J", "┘").replace("7", "┐").replace("F", "┌")
# f.write(new)

maps = {}
start = None
for i in range(len(input_lines)):
    for j in range(len(input_lines[i])):
        if input_lines[i][j] == "L":
            if i > 0:
                if j < len(input_lines[i]) - 1:
                    maps[(i, j)] = [(i - 1, j), (i, j + 1)]
                else:
                    maps[(i, j)] = [(i - 1, j)]
            else:
                maps[(i, j)] = [(i, j + 1)]
        elif input_lines[i][j] == "J":
            if i > 0:
                if j > 0:
                    maps[(i, j)] = [(i - 1, j), (i, j - 1)]
                else:
                    maps[(i, j)] = [(i - 1, j)]
            else:
                maps[(i, j)] = [(i, j - 1)]
        elif input_lines[i][j] == "7":
            if i < len(input_lines) - 1:
                if j > 0:
                    maps[(i, j)] = [(i + 1, j), (i, j - 1)]
                else:
                    maps[(i, j)] = [(i + 1, j)]
            else:
                maps[(i, j)] = [(i, j - 1)]
        elif input_lines[i][j] == "F":
            if i < len(input_lines) - 1:
                if j < len(input_lines[i]) - 1:
                    maps[(i, j)] = [(i + 1, j), (i, j + 1)]
                else:
                    maps[(i, j)] = [(i + 1, j)]
            else:
                maps[(i, j)] = [(i, j + 1)]
        elif input_lines[i][j] == "|":
            if i > 0 and i < len(input_lines) - 1:
                maps[(i, j)] = [(i - 1, j), (i + 1, j)]
            elif i > 0:
                maps[(i, j)] = [(i - 1, j)]
            else:
                maps[(i, j)] = [(i + 1, j)]
        elif input_lines[i][j] == "-":
            if j > 0 and j < len(input_lines[i]) - 1:
                maps[(i, j)] = [(i, j - 1), (i, j + 1)]
            elif j > 0:
                maps[(i, j)] = [(i, j - 1)]
            else:
                maps[(i, j)] = [(i, j + 1)]
        elif input_lines[i][j] == "S":
            start = (i, j)
        elif input_lines[i][j] == ".":
            maps[(i, j)] = []

paths_containing_start = {}
for k, v in maps.items():
    to_remove = []
    for conection in v:
        if conection not in maps.keys():
            cpy = v.copy()
            cpy.remove(conection)
            paths_containing_start[k] = cpy
            to_remove.append(conection)
            continue
        if k not in maps[conection]:
            to_remove.append(conection)
    for i in to_remove:
        maps[k].remove(i)

print(paths_containing_start)
print("End: ", start)
current = list(paths_containing_start.keys())[0]
last = current
steps=0
print("#"*10)
while True:
    print(f"Current: {current}")
    next_tube = maps[current]
    print(f"Next: {next_tube}")
    for i in next_tube:
        if i != last:
            last = current
            current = i
            steps += 1
            break
    if current in paths_containing_start.keys():
        break

print(steps/2 + 1)
# path = find_path(maps, start)
# print(path)
# print(len(path))

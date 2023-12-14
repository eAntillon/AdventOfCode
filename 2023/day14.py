input_lines = open("./input/day14.txt", "r").read().split("\n")
# input_lines = open("./input/day14_test.txt", "r").read().split("\n")

def process_cycle(arr):
    input_lines = arr.copy()
    for i in range(len(input_lines)):
        j = i
        while j > 0:
            for k in range(len(input_lines)):
                current = input_lines[j - 1][k]
                next = input_lines[j][k]
                if current == "." and next == "O":
                    input_lines[j - 1] = (
                        input_lines[j - 1][:k] + "O" + input_lines[j - 1][k + 1 :]
                    )
                    input_lines[j] = input_lines[j][:k] + "." + input_lines[j][k + 1 :]
            j -= 1
    return input_lines

def get_north_load(input_lines):
    acc = 0
    for i in range(len(input_lines)):
        count_o = input_lines[i].count("O")
        acc += count_o * (len(input_lines) - i)
    return acc

def get_transpose(input_lines):
    return ["".join(x) for x in zip(*input_lines)]

def get_north_to_east_cycle(last_north):
    north = process_cycle(last_north)
    west = process_cycle(get_transpose(north))
    south = process_cycle(get_transpose(west)[::-1])
    east = process_cycle(get_transpose(south[::-1])[::-1])
    return east


visited_states = {}
last_north = input_lines
cycles = 0
while cycles < 1000000000:
    last_north = get_north_to_east_cycle(last_north)
    # from east to north
    last_north = get_transpose(last_north[::-1])
    if "\n".join(last_north) in visited_states.keys():
        # print("Found", cycles, visited_states["\n".join(last_north)])
        # print("\n".join(last_north))
        cycles += (cycles - visited_states["\n".join(last_north)])*((1000000000 - cycles) // (cycles - visited_states["\n".join(last_north)]))
    else:
        # print("Not found", cycles)
        # print("\n".join(last_north))
        visited_states["\n".join(last_north)] = cycles
    print(cycles)
    cycles += 1

print(get_north_load(last_north))
    


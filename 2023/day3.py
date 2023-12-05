import re

data = open("./input/day3.txt", "r").read().split("\n")
lines = len(data)
i = 0
acc = 0
while i < lines:
    j = 0
    buff = ""
    first_j = 0
    last_j = 0
    while j < len(data[i]):
        char = data[i][j]
        first_j = j
        if char.isnumeric():
            while True:
                if char.isnumeric():
                    buff += char
                    j += 1
                    last_j = j
                    if j >= len(data[i]):
                        break
                    char = data[i][j]
                else:
                    break
            # print(f"number: {buff} line:{i} f:{first_j} l:{last_j}")
            # search for adyacent symbol in
            #   [i-1][first_j-1 --- last_j+1]
            #   [i][first_j-1]    [i][last_j+1]
            #   [i+1][first_j-1 --- last_j+1]

            valid_number = False
            if i > 0:
                f = first_j
                l = last_j
                if first_j > 0:
                    f -= 1
                if last_j < len(data[i]):
                    l += 1
                if re.search(r"[^.\d]", data[i - 1][f:l]) is not None:
                    # print(
                    #     f"valid {buff} {data[i - 1][f:l]} i:{i-1} {first_j}  {last_j}"
                    # )
                    valid_number = True
            if first_j > 0 and not valid_number:
                if re.search(r"[^.\d]", data[i][first_j - 1]) is not None:
                    # print(
                    #     f"valid {buff} {data[i][first_j-1]}    i:{i} {first_j}  {last_j}"
                    # )
                    valid_number = True
            if last_j < len(data[i]) and not valid_number:
                if re.search(r"[^.\d]", data[i][last_j]) is not None:
                    # print(
                    #     f"valid {buff} {data[i][last_j]}    i:{i} {first_j}  {last_j}"
                    # )
                    valid_number = True
            if i + 1 < lines and not valid_number:
                if first_j > 0:
                    first_j -= 1
                if last_j < len(data[i]):
                    last_j += 1
                if re.search(r"[^.\d]", data[i + 1][first_j:last_j]) is not None:
                    # print(f"valid {buff} {data[i + 1][first_j: last_j]}")
                    valid_number = True
            if valid_number:
                acc += int(buff)
            buff = ""
        j += 1
    i += 1
print("Part1:", acc)

# part 2
i = 0
acc = 0
while i < lines:
    j = 0
    while j < len(data[i]):
        char = data[i][j]
        if char == "*":
            adyacent = []
            # print with color
            # print(f"\033[1;31;40msymbol * line:{i} j:{j} \033[0m")
            if i > 0:
                numbers = re.finditer(r"\d+", data[i - 1])
                # print(f"top numbers")
                for x in numbers:
                    # print(f"----> {x.group()} s:{x.start()} end:{x.end()}")
                    if x.start() <= j <= x.end() or x.end() == j or x.start() == j+1:
                        adyacent.append(x)
            if j > 0:
                numbers = re.finditer(r"\d+", data[i])
                # left
                # print(f"left numbers")
                for x in numbers:
                    # print(f"----> {x.group()} {x.start()} {x.end()}")
                    if x.start() == j or x.end() == j:
                        adyacent.append(x)
            if j < len(data[i]):
                numbers = re.finditer(r"\d+", data[i])
                # right
                # print(f"right numbers")
                for x in numbers:
                    # print(f"----> {x.group()} {x.start()} {x.end()}")
                    if x.start() == j+1:
                        adyacent.append(x)
            if i < lines:
                numbers = re.finditer(r"\d+", data[i + 1])
                # print(f"bottom numbers")
                for x in numbers:
                    if x.start() <= j <= x.end() or x.end() == j or x.start() == j+1:
                        # print(f"----> {x.group()} {x.start()} {x.end()}")
                        adyacent.append(x)
            # print with color green
            # print(f"\033[1;32;40madyacent {[x.group() for x in adyacent]} \033[0m")
            if len(adyacent) == 2:
                acc += int(adyacent[0].group()) * int(adyacent[1].group())
                # print(f"\033[1;32;40madding {int(adyacent[0].group()) * int(adyacent[1].group())} \033[0m")

        j += 1
    i += 1
print("Part2:", acc)

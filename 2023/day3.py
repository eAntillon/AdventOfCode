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
            print(f"number: {buff} line:{i} f:{first_j} l:{last_j}")
            # search for adyacent symbol in
            #   [i-1][first_j-1 --- last_j+1]
            #   [i][first_j-1]    [i][last_j+1]
            #   [i+1][first_j-1 --- last_j+1]

            valid_number = False
            if i > 0:
                f = first_j
                l = last_j
                if first_j > 0: f-=1
                if last_j < len(data[i]): l+=1 
                if (
                    re.search(r"[^.\d]", data[i - 1][f:l])
                    is not None
                ):
                    print(f"valid {buff} {data[i - 1][f:l]} i:{i-1} {first_j}  {last_j}")
                    valid_number = True
            if first_j > 0 and not valid_number:
                if re.search(r"[^.\d]", data[i][first_j-1]) is not None:
                    print(f"valid {buff} {data[i][first_j-1]}    i:{i} {first_j}  {last_j}")
                    valid_number = True
            if last_j < len(data[i]) and not valid_number:
                if re.search(r"[^.\d]", data[i][last_j]) is not None:
                    print(  
                        f"valid {buff} {data[i][last_j]}    i:{i} {first_j}  {last_j}"
                    )
                    valid_number = True
            if i + 1 < lines and not valid_number:
                if first_j > 0: first_j-=1
                if last_j < len(data[i]): last_j+=1 
                if (
                    re.search(r"[^.\d]", data[i + 1][first_j: last_j])
                    is not None
                ):
                    print(f"valid {buff} {data[i + 1][first_j: last_j]}")
                    valid_number = True
            if valid_number:
                acc += int(buff)
            buff = ""
        j += 1
    i += 1
print(acc)

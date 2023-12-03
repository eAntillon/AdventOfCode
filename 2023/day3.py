import re

data = open('./input/day3.txt', 'r').readlines()
lines = len(data)
cols = len(data[0])
i = 0
acc = 0
while i < lines:
    j = 0
    buff = ''
    first_j = 0
    last_j = 0
    while j < cols:
        print(f" i{i} j{j}")
        char = data[i][j]
        first_j = j
        if char.isnumeric():
            while True:
                if char.isnumeric():
                    buff += char
                    j += 1
                    last_j = j
                    char = data[i][j]
                else:
                    break
            print(f"number: {buff} i:{i} f:{first_j} l:{last_j}")
            # search for adyacent symbol in 
            #   [i-1][first_j-1 --- last_j+1]
            #   [i][first_j-1]    [i][last_j+1]
            #   [i+1][first_j-1 --- last_j+1]
            if i > 0:
                if re.search(r"[^.\d]",data[i-1][first_j-1:last_j+1]) is not None:
                    acc += int(buff)
                    buff = ''
                    continue
            if first_j > 0:
                if re.search(r"[^.\d]", data[i][first_j-1]) is not None:
                    acc += int(buff)
                    buff = ''
                    continue
            try:
                if last_j < cols-1:
                    if re.search(r"[^.\d]", data[i][last_j+1]) is not None:
                        acc += int(buff)
                        buff = ''
                        continue
            except Exception:
                print(f"lastj error {last_j} cols: {cols}" )
            if i < lines -1:
                if re.search(r"[^.\d]", data[i+1][first_j-1:last_j+1]) is not None:
                    acc += int(buff)
                    buff = ''
                    continue
        j += 1
    i += 1
print(acc)
        
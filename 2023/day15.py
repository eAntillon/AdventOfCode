input = open("./input/day15.txt", "r").read()

def get_hash(s):
    hash = 0
    for letter in s:
        hash += ord(letter)
        hash = (hash*17) % 256
    return hash


sum = 0
for step in input.split(","):
    hash = get_hash(step)
    sum += hash 
    # print( sum)

# Part 1
print("Part: 1", sum)

# Part 2

from collections import deque

boxes = [{} for i in range(256)]

for step in input.split(","):
    index = step.find("-")
    if index == -1:
        index = step.find("=")
        value = step[index+1:]
    label = step[:index]
    op = step[index]
    
    hash = get_hash(label)

    if op == "=":
        boxes[hash][label] = value

    elif op == "-":
        if label in boxes[hash]:
            index = boxes[hash][label]
            del boxes[hash][label]


# for i in range(256):
#     if len(boxes[i]) > 0:
#         print(i, boxes[i])

acc = 0 
for i in range(len(boxes)):
    if len(boxes[i]) == 0:
        continue
    boxes[i] = list(boxes[i].items())
    result = 0
    for j in range(len(boxes[i])):
        r = (i+1) * (j+1) * int(boxes[i][j][1])
        # print(f"{i+1} * {j+1} * {boxes[i][j][1]} = {r}")
        result += r
    acc += result

print("Part 2:", acc)   
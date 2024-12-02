input = open("input.txt", "r").read().split("\n")

# Part 1
firstList = []
secondList = []

for line in input:
    elements = line.split("   ")
    firstList.append(elements[0])
    secondList.append(elements[1])

firstList.sort()
secondList.sort()

pairs = list(zip(firstList, secondList))

total = 0
for pair in pairs:
    total += abs(int(pair[0]) - int(pair[1]))


print("Part 1: ", total)

# Part 2

appearances = {}

for line in input:
    elements = line.split("   ")
    second = int(elements[1])

    if second not in appearances:
        appearances[second] = 1
    else:
        appearances[second] += 1

similarityScore = 0

for n in firstList:
    if int(n) in appearances:
        similarityScore += int(n) * appearances[int(n)]

print("Part 2: ", similarityScore)
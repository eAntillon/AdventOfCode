input_lines = open("./input/day9.txt", "r").read().split("\n")

def getDirences(arr):
    differences = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    if sum(differences) == 0:
        return 0
    return differences[-1] + getDirences(differences)

acc1 = 0
acc2 = 0
for i in range(len(input_lines)):
    arr = input_lines[i].split(" ")
    arr = [int(x) for x in arr]
    prediction_part1 = arr[-1] + getDirences(arr)
    # part 2
    arr.reverse()
    prediction_part2 = arr[-1] + getDirences(arr)

    acc1 += prediction_part1
    acc2 += prediction_part2
    # print("Case #" + str(i + 1) + ": " + str(prediction))


print("Part 1: " + str(acc1))
print("Part 2: " + str(acc2))

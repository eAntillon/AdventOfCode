data = open("./input/day4.txt", "r").readlines()
acc = 0
# part 1
for line in data:
    winners, numbers = line[10:].split("|")
    winners = winners.strip().split(" ")
    numbers = numbers.strip().split(" ")
    match = set(winners).intersection(set(numbers))
    if "" in match:
        match.remove("")
    if len(match) > 0:
        points = (1 * (2 ** len(match))) / 2
        acc += points
print(acc)

# part 2
copies = [0 for x in range(len(data) + 1)]
for line in data:
    id = int(line.split(":")[0].split(" ")[-1])
    winners, numbers = line[9:].split("|")
    winners = winners.strip().split(" ")
    numbers = numbers.strip().split(" ")
    match = set(winners).intersection(set(numbers))
    if "" in match:
        match.remove("")

    if len(match) > 0:
        for i in range(len(match)):
            copies[id + i + 1] += 1
    
    if copies[id] > 0:
        for i in range(copies[id]):
            for i in range(len(match)):
                copies[id + i + 1] += 1

print(sum(copies) + len(data))

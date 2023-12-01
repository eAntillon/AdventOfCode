# part 1
data = open("input/day1.txt").readlines()

acc = 0
for line in data:
    i = 0
    j = len(line) - 1
    first = None
    last = None

    while i <= len(line):
        if first is None:
            if line[i].isnumeric():
                first = line[i]
            i += 1
        if last is None:
            if line[j].isnumeric():
                last = line[j]
            j -= 1
        if first is not None and last is not None:
            break
    if first is None:
        first = ""
    if last is None:
        last = ""
    # print(f"- {first}{last} - {line}")
    acc += int(first + last)
# solution part 1
print(acc)


# part 2
import re

acc = 0

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
for line in data:
    occurences = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
    first = occurences[0]
    last = occurences[-1]
    if first in numbers.keys():
        first = numbers[first]
    if last in numbers.keys():
        last = numbers[last]
    print(f"- {first}{last} - {occurences} - {line}")
    acc += int(f"{first}{last}")

# solution part 2
print(acc)

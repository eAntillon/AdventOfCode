import re

input = open("./input/day6.txt", "r").read().split("\n")
times = [int(x) for x in re.sub(r"\s+", " ", input[0].split(":")[1].strip()).split(" ")]
records = [
    int(x) for x in re.sub(r"\s+", " ", input[1].split(":")[1].strip()).split(" ")
]

acc = 1
for time, record in zip(times, records):
    times_max = []
    count = 0
    while count < time:
        if count * (time - count) > record:
            times_max.append(count)
        count += 1
    acc *= len(times_max)
print(f"Part 1: {acc}")

time = int(re.sub(r"\s+", "", input[0].split(":")[1].strip()))
distance = int(re.sub(r"\s+", "", input[1].split(":")[1].strip()))

# import complex math module
import cmath
sol1 = -(-time - cmath.sqrt(((time**2) - (4 * distance)))) / 2
sol2 = -(-time + cmath.sqrt(((time**2) - (4 * distance)))) / 2

print(f"Part 2: {int(sol1.real) - int(sol2.real)}")

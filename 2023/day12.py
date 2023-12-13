import re
input_lines = open("./input/day12.txt").read().split("\n")


def isValid(string, pattern):
    valid_cases = 0
    # count ocurrences of ?
    max = string.count("?")
    count = 0
    get_bin = lambda x: format(x, 'b').zfill(max)
    # generate all possible combinations
    while count < 2**max:
        bin_string = get_bin(count)
        new_string = string
        for i in bin_string:
            # replace ? with . if is 0 and with # if is 1
            if i == "0":
                new_string = new_string.replace("?", ".", 1)
            else:
                new_string = new_string.replace("?", "#", 1)
        count += 1
        groups = [len(x) for x  in re.findall(r'[#]+', new_string) ]
        if groups == pattern:
            valid_cases += 1

    return valid_cases

# part 2 

lines_p2 = []

acc = 0
count = 1
for line in input_lines:
    data, groups = line.split(" ")
    data = (data+"?")*5
    data = data[:-1]
    groups = (groups+",")*5
    groups = groups[:-1]
    groups = [int(x) for x in groups.split(",")]
    count += 1
    acc += isValid(data, groups)
    print(acc)

print(acc)
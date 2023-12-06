import pprint

pp = pprint.PrettyPrinter(indent=4)

data = open("./input/day5_test.txt", "r").read().split("\n\n")
seeds = data[0].split(":")[1].strip().split(" ")
seeds = [int(x) for x in seeds]

maps = []
for map in data[1:]:
    text_map = map.split("\n")[1:]
    new_map = []
    # print("\033[92m###### MAP \033[0m")
    for line in text_map:
        # print in green
        # print(f"--- {line} ---")
        new_set = [int(x) for x in line.split(" ")]
        new_map.append(new_set)
        # print(f"--- {new_set} ---")
    maps.append(new_map)


def mapSeeds(seeds):
    current_seeds = seeds.copy()
    for map in maps:
        edited_seeds = [0 for x in range(len(current_seeds))]
        for line in map:
            output, start, length = line[0], line[1], line[2]
            for i in range(len(current_seeds)):
                seed = current_seeds[i]
                if seed >= start and seed < start + length and edited_seeds[i] == 0:
                    current_seeds[i] = output + (seed - start)
                    edited_seeds[i] = 1

    return min(current_seeds)


# part 1
print("Part 1:", mapSeeds(seeds))

# part 2
p2_seeds = []


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.processed = False

    def __repr__(self):
        return f"Range({self.start}, {self.end})"


for i in range(len(seeds)):
    if (i + 1) % 2 == 0 and i > 0:
        p2_seeds.append(Range(seeds[i - 1], seeds[i - 1] + seeds[i]))

p2_seeds.sort(key=lambda x: x.start)
print("\033[92m###### INITIAL SEEDS RANGES \033[0m")
for seed in p2_seeds:
    print(seed.start, seed.end)

print("\033[92m###### \033[0m")


def mapSeedsRange(seeds):
    current_seeds = seeds.copy()

    # map filter
    for map in maps:
        # line of the map
        for seed in current_seeds:
            seed.processed = False
        for line in map:
            print("\033[95m###### LINE MAP \033[0m")
            print(line)
            print("\033[95m###### \033[0m")
            output, start, length = line[0], line[1], line[2]
            for i in range(len(current_seeds)):
                current_range = current_seeds[i]
                range_start, range_end, processed = (
                    current_range.start,
                    current_range.end,
                    current_range.processed,
                )
                print(f"\033[91m###### WORKING RANGE {current_range} \033[0m")
                if range_start >= start and processed is False:
                    if range_end < start + length:
                        # if the current range fit inside the current line
                        # transform the start and end of the range of the current line
                        print(
                            f"\033[93m###### VALID RANGE {current_range} fit ({start},{start+length}) \033[0m"
                        )
                        converted_range = Range(
                            output + (range_start - start),
                            output + (range_end - start),
                        )
                        converted_range.processed = True
                        current_seeds[i] = converted_range
                        print(f"\033[93m###### converter to {converted_range}\033[0m")
                    else:
                        # else, if the current range start fits, but the end doesn't
                        # split the current range in two and insert the second part after the current one
                        print(
                            f"\033[94m###### EVALUATE RANGE ({start},{start+length}) \033[0m"
                        )

                        valid_range = Range(
                            range_start,
                            start + length - 1,
                        )
                        end_cut = start + length - 1

                        print(
                            f"\033[93m###### SPLIT RANGE {current_range} in {valid_range} and {Range(end_cut, range_end)} \033[0m"
                        )
                        valid_range = Range(
                            output + (range_start - start), (output + length)
                        )
                        new_range = Range(end_cut, range_end)
                        valid_range.processed = True
                        current_seeds[i] = valid_range
                        current_seeds.insert(i, new_range)
                else:
                    print(
                        f"\033[93m###### INVALID RANGE {current_range} not in ({start},{start+length}) \033[0m"
                    )
        # print("\033[91m###### OUTPUT RANGES \033[0m")
        # pp.pprint(current_seeds)
    # return de min of the start of the ranges
    current_seeds.sort(key=lambda x: x.start)
    print(current_seeds)
    return current_seeds[0].start


print("Part 2:", mapSeedsRange(p2_seeds[0:1]))
# print("Part 2:", mapSeeds(p2_seeds))

import pprint

pp = pprint.PrettyPrinter(indent=4)


# def mapSeeds(seeds):
#     current_seeds = seeds.copy()
#     for map in maps:
#         edited_seeds = [0 for x in range(len(current_seeds))]
#         for line in map:
#             output, start, length = line[0], line[1], line[2]
#             for i in range(len(current_seeds)):
#                 seed = current_seeds[i]
#                 if seed >= start and seed < start + length and edited_seeds[i] == 0:
#                     current_seeds[i] = output + (seed - start)
#                     edited_seeds[i] = 1

#     return min(current_seeds)

# # part 1
# print("Part 1:", mapSeeds(seeds))

# part 2


import sys
import time
from multiprocessing import Pool
from signal import signal, SIGINT
from sys import exit

data = open("./input/day5.txt", "r").read().split("\n\n")
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

def handler(signal_received, frame):
    # Handle any cleanup here
    print("SIGINT or CTRL-C detected. Exiting gracefully")
    exit(0)


def getSeedLocation(seeds_range):
    print(f"\033[91m###### Working on seed range {seeds_range} \033[0m")
    min = sys.maxsize
    signal(SIGINT, handler)

    for seed in range(seeds_range[0], seeds_range[1]):
        # print(f"\033[91m###### Working on seed {seed} \033[0m")
        current_value = seed
        # print(f"Maping {seed}")
        for map in maps:
            processed = False
            # print("\033[95m###### LINE MAP \033[0m")
            # print(map)
            for line in map:
                output, start, length = line[0], line[1], line[2]
                if (
                    current_value >= start
                    and current_value < start + length
                    and not processed
                ):
                    # print(f"Maped {current_value} to", end=" ")
                    # print(f" {current_value} in {line}")
                    current_value = output + (current_value - start)
                    processed = True
                    break
        # print(f"\033[91m###### Result {current_value} \033[0m")
        if current_value < min:
            # print(f"Maped {seed} to {current_value}")
            min = current_value
            # print progress
            print(f"\033[92m###### Worked {current_value} {min} \033[0m")
    return min


start_time = time.time()
if __name__ == "__main__":
    p2_seeds = []
    for i in range(len(seeds)):
        if (i + 1) % 2 == 0 and i > 0:
            p2_seeds.append([seeds[i - 1], seeds[i - 1] + seeds[i]])
    print("\033[92m###### INITIAL SEEDS RANGES \033[0m")
    for seed in p2_seeds:
        print(seed)
    for i in range(len(p2_seeds)):
        seed_range = p2_seeds[i]
        middle = (seed_range[1] + seed_range[0]) // 2
        p2_seeds[i] = [seed_range[0], middle]
        p2_seeds.insert(i + 1, [middle + 1, seed_range[1]])
    print("\033[92m###### SPLITED SEEDS RANGES \033[0m")
    for seed in p2_seeds:
        print(seed)


    with Pool(8) as pool:
        results = pool.imap(getSeedLocation, p2_seeds)
        # print(results)
        # pool.terminate()
        # pool.join()
        print("Part 2:", min(results))
    print("--- %s seconds ---" % (time.time() - start_time))

import time


blinking_times = 75

cache = {}

def get_stones_map(input):
    stones = [int(x) for x in input.split(" ")]
    stones_map = {}
    for stone in stones:
        if stone in stones_map:
            stones_map[stone] += 1
        else:
            stones_map[stone] = 1
    return stones_map

def get_stones(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        length = len(stone_str)
        left = int(stone_str[:length // 2])
        right = int(stone_str[length // 2:])
        return [left, right]
    else:

        return [stone * 2024]


def part1(input_data):
    stones_map = get_stones_map(input_data)
    for _ in range(25):
        result_stones = {}
        for stone, times in stones_map.items():
            result = []
            if stone in cache:
                result = cache[stone]
            else:
                result = get_stones(stone)
                cache[stone] = result
            for new_stone in result:
                if new_stone in result_stones:
                    result_stones[new_stone] += times
                else:
                    result_stones[new_stone] = times

        stones_map = result_stones
    total = 0
    for stone, times in stones_map.items():
        total += times
    return total


def part2(input_data):
    stones_map = get_stones_map(input_data)
    for _ in range(blinking_times):
        result_stones = {}
        for stone, times in stones_map.items():
            result = get_stones(stone)
            for new_stone in result:
                if new_stone in result_stones:
                    result_stones[new_stone] += times
                else:
                    result_stones[new_stone] = times

        stones_map = result_stones
    total = 0
    for stone, times in stones_map.items():
        total += times
    return total


def main():
    st = time.time()

    input_data = open("./input.txt", "r").read()
    print("Solution for day 11")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))

    et = time.time()

    print("Execution time in seconds: ", et-st)

main()

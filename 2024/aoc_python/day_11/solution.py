
blinking_times = 75

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


def get_next_blink_status(stone, i, max_blinks):
    if i == max_blinks:
        return [stone]
    if stone == 0:
        result = get_next_blink_status(1, i + 1, max_blinks)
        return result
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        length = len(stone_str)
        left = int(stone_str[:length // 2])
        right = int(stone_str[length // 2:])
        stones = []
        stones.extend(get_next_blink_status(left, i+1, max_blinks))
        stones.extend(get_next_blink_status(right, i+1, max_blinks))
        return stones
    else:
        result = get_next_blink_status(stone * 2024, i+1, max_blinks)
        return result

def part1(input_data):
    stones = [int(x) for x in input_data.split(" ")]
    sorted_stones = sorted(stones)
    total_stones = []
    for stone in sorted_stones:
        total_stones.extend(get_next_blink_status(stone, 0, 25))
    return len(total_stones)



def part2(input_data):
    stones = [int(x) for x in input_data.split(" ")]
    stones_map = {}
    for stone in stones:
        if stone in stones_map:
            stones_map[stone] += 1
        else:
            stones_map[stone] = 1

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
    input_data = open("./input.txt", "r").read()
    print("Solution for day 11")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))


main()

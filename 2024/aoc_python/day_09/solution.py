
def get_disk_map(input_data):
    disk_map = []
    i = 0
    id_iterator = 0
    for n in list(input_data.strip()):
        n = int(n)
        if i % 2 == 0:
            disk_map.extend([id_iterator for x in range(n)])
            id_iterator += 1
        else:
            disk_map.extend([-1 for x in range(n)])
        i += 1
    return disk_map


def part1(input_data):
    disk = get_disk_map(input_data)
    i = 0
    j = len(disk) - 1
    while i < j:
        if disk[i] == -1:
            while disk[j] == -1:
                j -= 1
            if j <= i:
                break
            disk[i] = disk[j]
            disk[j] = -1
            j -= 1
        i += 1

    acc = 0
    for n in range(i+1):
        if disk[n] == -1:
            continue
        acc += disk[n] * n
    return acc


def part2(input_data):
    disk = get_disk_map(input_data)
    j = len(disk) - 1

    while j >= 0:
        if disk[j] == -1:
            j -= 1
            continue
        file_blocks_group = [disk[j]]
        j -= 1
        while disk[j] != -1 and disk[j] == file_blocks_group[0]:
            file_blocks_group.append(disk[j])
            j -= 1
        j += 1

        i = 0
        start_free_space = -1
        end_free_space = -1
        while i < len(disk) - 1:
            if disk[i] == -1:
                if start_free_space == -1:
                    start_free_space = i
                end_free_space = i
            else:
                if start_free_space != -1:
                    if end_free_space - start_free_space + 1 >= len(file_blocks_group):
                        break
                    else:
                        start_free_space = -1
                        end_free_space = -1
            i += 1

        if start_free_space == -1 or end_free_space == -1 or end_free_space - start_free_space + 1 < len(file_blocks_group) or j <= start_free_space:
            j -= 1
            continue
        else:
            k = 0
            while k < len(file_blocks_group):
                disk[start_free_space + k] = file_blocks_group[k]
                disk[j + k] = -1
                k += 1
            file_blocks_group = []
    acc = 0
    for n in range(len(disk)):
        if disk[n] == -1:
            continue
        acc += disk[n] * n
    return acc


def main():
    input_data = open("./input.txt", "r").read()
    print("Solution for day 9")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))


main()

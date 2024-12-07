from enum import Enum
import copy
from pprint import pprint as pp


visited = []


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)


def isValidPosition(i, j, labMap):
    if i < len(labMap) and i >= 0 and j < len(labMap[i]) and j >= 0:
        return True
    return False


def move_and_check(i, j, current_direction, new_direction, labMap):
    ni = i + current_direction.value[0]
    nj = j + current_direction.value[1]
    if isValidPosition(ni, nj, labMap) and labMap[ni][nj] == "#":
        return i + new_direction.value[0], j + new_direction.value[1], new_direction
    return ni, nj, None


def part1(input_data) -> int:
    labMap = input_data.split("\n")
    labMap = [list(x) for x in labMap]
    guardPosition = (0, 0)
    for i in range(len(labMap)):
        for j in range(len(labMap[i])):
            if labMap[i][j] == "^":
                guardPosition = (i, j)
                break

    i = guardPosition[0]
    j = guardPosition[1]
    direction = Direction.UP

    while isValidPosition(i, j, labMap):
        visited.append((i, j, direction))
        visited_cord = []
        match direction:
            case Direction.UP:
                ni, nj, new_direction = move_and_check(
                    i, j, Direction.UP, Direction.RIGHT, labMap)
                if new_direction:
                    direction = new_direction
                    yi, yj, new_direction = move_and_check(
                        i, j, Direction.RIGHT, Direction.DOWN, labMap)
                    if new_direction:
                        direction = new_direction
                        nj = yj
                        ni = yi
                i = ni
                j = nj
                visited_cord = [i, j, direction]

            case Direction.RIGHT:
                ni, nj, new_direction = move_and_check(
                    i, j, Direction.RIGHT, Direction.DOWN, labMap)
                if new_direction:
                    direction = new_direction
                    yi, yj, new_direction = move_and_check(
                        i, j, Direction.DOWN, Direction.LEFT, labMap)
                    if new_direction:
                        direction = new_direction
                        nj = yj
                        ni = yi
                i = ni
                j = nj
                visited_cord = [i, j, direction]
            case Direction.DOWN:
                ni, nj, new_direction = move_and_check(
                    i, j, Direction.DOWN, Direction.LEFT, labMap)
                if new_direction:
                    direction = new_direction
                    yi, yj, new_direction = move_and_check(
                        i, j, Direction.LEFT, Direction.UP, labMap)
                    if new_direction:
                        direction = new_direction
                        nj = yj
                        ni = yi
                i = ni
                j = nj
                visited_cord = [i, j, direction]

            case Direction.LEFT:
                ni, nj, new_direction = move_and_check(
                    i, j, Direction.LEFT, Direction.UP, labMap)
                if new_direction:
                    direction = new_direction
                    yi, yj, new_direction = move_and_check(
                        i, j, Direction.UP, Direction.RIGHT, labMap)
                    if new_direction:
                        direction = new_direction
                        nj = yj
                        ni = yi
                i = ni
                j = nj
                visited_cord = [i, j, direction]
        if isValidPosition(i, j, labMap):
            visited.append(tuple(visited_cord))
    # for i in visited:
    #     match i[2]:
    #         case Direction.UP:
    #             labMap[i[0]][i[1]] = "^"
    #         case Direction.RIGHT:
    #             labMap[i[0]][i[1]] = ">"
    #         case Direction.DOWN:
    #             labMap[i[0]][i[1]] = "v"
    #         case Direction.LEFT:
    #             labMap[i[0]][i[1]] = "<"
    # for i in labMap:
    #     print("".join(i))
    mapped = map(lambda x: (x[0], x[1]), visited)
    return len(set(mapped))


# Part 2
def get_loop(labMap, guardPosition=(0, 0)):
    i = guardPosition[0]
    j = guardPosition[1]
    direction = Direction.UP
    v = []
    while isValidPosition(i, j, labMap):
        if (i, j, direction) in v and len(v) > 1:
            return True
        # v.append((i, j, direction))
        # match direction:
        #     case Direction.UP:
        #         i, j, new_direction = move_and_check(
        #             i, j, Direction.UP, Direction.RIGHT, labMap)
        #         if new_direction:
        #             v.append((i, j, new_direction))
        #             direction = new_direction
        #             i, j, new_direction = move_and_check(
        #                 i, j, Direction.RIGHT, Direction.DOWN, labMap)
        #             if new_direction:
        #                 direction = new_direction
        #     case Direction.RIGHT:
        #         i, j, new_direction = move_and_check(
        #             i, j, Direction.RIGHT, Direction.DOWN, labMap)
        #         if new_direction:
        #             v.append((i, j, new_direction))
        #             direction = new_direction
        #             i, j, new_direction = move_and_check(
        #                 i, j, Direction.DOWN, Direction.LEFT, labMap)
        #             if new_direction:
        #                 direction = new_direction
        #     case Direction.DOWN:
        #         i, j, new_direction = move_and_check(
        #             i, j, Direction.DOWN, Direction.LEFT, labMap)
        #         if new_direction:
        #             v.append((i, j, new_direction))
        #             direction = new_direction
        #             i, j, new_direction = move_and_check(
        #                 i, j, Direction.LEFT, Direction.UP, labMap)
        #             if new_direction:
        #                 direction = new_direction
        #     case Direction.LEFT:
        #         i, j, new_direction = move_and_check(
        #             i, j, Direction.LEFT, Direction.UP, labMap)
        #         if new_direction:
        #             v.append((i, j, new_direction))
        #             direction = new_direction
        #             i, j, new_direction = move_and_check(
        #                 i, j, Direction.UP, Direction.RIGHT, labMap)
        #             if new_direction:
        #                 direction = new_direction
        v.append((i, j, direction))
        
        match direction:
            case Direction.UP:
                ni, nj, new_direction = move_and_check(
                    i, j, Direction.UP, Direction.RIGHT, labMap)
                if new_direction:
                    direction = new_direction
                    yi, yj, new_direction = move_and_check(
                        i, j, Direction.RIGHT, Direction.DOWN, labMap)
                    if new_direction:
                        direction = new_direction
                        nj = yj
                        ni = yi
                i = ni
                j = nj
                

            case Direction.RIGHT:
                ni, nj, new_direction = move_and_check(
                    i, j, Direction.RIGHT, Direction.DOWN, labMap)
                if new_direction:
                    direction = new_direction
                    yi, yj, new_direction = move_and_check(
                        i, j, Direction.DOWN, Direction.LEFT, labMap)
                    if new_direction:
                        direction = new_direction
                        nj = yj
                        ni = yi
                i = ni
                j = nj
                
            case Direction.DOWN:
                ni, nj, new_direction = move_and_check(
                    i, j, Direction.DOWN, Direction.LEFT, labMap)
                if new_direction:
                    direction = new_direction
                    yi, yj, new_direction = move_and_check(
                        i, j, Direction.LEFT, Direction.UP, labMap)
                    if new_direction:
                        direction = new_direction
                        nj = yj
                        ni = yi
                i = ni
                j = nj
                

            case Direction.LEFT:
                ni, nj, new_direction = move_and_check(
                    i, j, Direction.LEFT, Direction.UP, labMap)
                if new_direction:
                    direction = new_direction
                    yi, yj, new_direction = move_and_check(
                        i, j, Direction.UP, Direction.RIGHT, labMap)
                    if new_direction:
                        direction = new_direction
                        nj = yj
                        ni = yi
                i = ni
                j = nj
                
        
    return False


def part2(input_data):
    labMap = input_data.split("\n")
    labMap = [list(x) for x in labMap]

    obstructions = []
    positions_visited = map(lambda x: (x[0], x[1]), visited)

    guardPosition = (0, 0)
    for i in range(len(labMap)):
        for j in range(len(labMap[i])):
            if labMap[i][j] == "^":
                guardPosition = (i, j)
                break
    print_map = copy.deepcopy(labMap)
    for p in positions_visited:
        c = labMap[p[0]][p[1]]
        labMap[p[0]][p[1]] = "#"
        if get_loop(labMap, guardPosition):
            print_map[p[0]][p[1]] = "O"
            obstructions.append(p)
        labMap[p[0]][p[1]] = c
        
    for i in print_map:
        print("".join(i))

    print("-"*20)
    for i in visited:
        match i[2]:
            case Direction.UP:
                labMap[i[0]][i[1]] = "^"
            case Direction.RIGHT:
                labMap[i[0]][i[1]] = ">"
            case Direction.DOWN:
                labMap[i[0]][i[1]] = "v"
            case Direction.LEFT:
                labMap[i[0]][i[1]] = "<"
    for i in labMap:
        print("".join(i))
    mapped = map(lambda x: (x[0], x[1]), obstructions)
    return len(set(mapped))


def main():
    input_data = open("./input.txt", "r").read()
    print("Solution for day 6")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))


main()

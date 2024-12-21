import time


def parse_input(input_data):
    pool, moves = input_data.split("\n\n")
    pool = [list(x) for x in pool.split("\n")]
    moves = list(moves)
    return pool, moves


def is_valid(pool, position):
    x, y = position
    return x >= 0 and y >= 0 and x < len(pool) and y < len(pool[0])


def make_move(pool, position, move):

    x, y = position
    next_i, next_j = x, y
    symbol = pool[x][y]

    if pool[x][y] == "#":
        return x, y

    if move == ">":
        next_j += 1
    elif move == "<":
        next_j -= 1
    elif move == "^":
        next_i -= 1
    elif move == "v":
        next_i += 1

    if is_valid(pool, (next_i, next_j)):
        if pool[next_i][next_j] == "O":
            new_x, new_y = make_move(pool, (next_i, next_j), move)
            if new_x == -1 and new_y == -1:
                if symbol == "@":
                    return x, y
                else:
                    return -1, -1
            pool[x][y] = "."
            pool[new_x][new_y] = symbol
            if symbol == "@":
                return new_x, new_y
            else:
                return x, y

        elif pool[next_i][next_j] == "#":
            return -1, -1

        else:
            if symbol == "@":
                pool[x][y] = "."
                pool[next_i][next_j] = "@"
                return next_i, next_j
            else:
                pool[x][y] = "."
                pool[next_i][next_j] = symbol
                return x, y

    return x, y


def part1(input_data):
    pool, moves = parse_input(input_data)

    initial_position = (0, 0)

    for i in range(len(pool)):
        for j in range(len(pool[i])):
            if pool[i][j] == "@":
                initial_position = (i, j)

    print("Initial position: ", initial_position)
    while len(moves) > 0:
        move = moves.pop(0)
        c = initial_position
        initial_position = make_move(pool, initial_position, move)
        if initial_position == (-1, -1):
            initial_position = c

    final_positions = []
    for i in range(len(pool)):
        for j in range(len(pool[i])):
            if pool[i][j] == "O":
                final_positions.append((i, j))

    total = 0
    for f in final_positions:
        punctuation = f[0] * 100 + f[1]
        total += punctuation
    return total


def make_move_2(pool, position, move):
    x, y = position
    next = (x, y)
    symbol = pool[x][y]

    if pool[x][y] == "#" or symbol == ".":
        return x, y

    if move == ">":
        next[1] += 1
    elif move == "<":
        next[1] -= 1
    elif move == "^":
        next[0] -= 1
    elif move == "v":
        next[0] += 1

    next_simbol = pool[next[0]][next[1]]

    if not is_valid(pool, next):
        return x, y

    if next_simbol in ["[", "]"] and move in [">", "<"]:
        new_x, new_y = make_move_2(pool, next, move)
        if new_x == -1 and new_y == -1:
            if symbol == "@":
                return x, y
            else:
                return -1, -1
        if symbol == "[" and move == ">":
            pool[x][y] = "."
        elif symbol == "]" and move == "<":
            pool[x][y] = "."
        elif symbol == "[" and move == "<":
            pool[x][y] = "]"
        elif symbol == "]" and move == ">":
            pool[x][y] = "["
        elif symbol == "@":
            pool[x][y] = "."

        pool[new_x][new_y] = symbol

        if symbol == "@":
            return new_x, new_y
        else:
            return x, y

    if next_simbol in ["[", "]"] and move in ["^", "v"]:
        new_x, new_y = make_move_2(pool, next, move)
        if new_x == -1 and new_y == -1:
            if symbol == "@":
                return x, y
            else:
                return -1, -1
        if symbol == "[" and move == "^":
            pool[x][y] = "."
        elif symbol == "]" and move == "v":
            pool[x][y] = "."
        elif symbol == "[" and move == "v":
            pool[x][y] = "]"
        elif symbol == "]" and move == "^":
            pool[x][y] = "["
        elif symbol == "@":
            pool[x][y] = "."

        pool[new_x][new_y] = symbol

        if symbol == "@":
            return new_x, new_y
        else:
            return x, y
    return x, y


def part2(input_data):
    pool, moves = input_data.split("\n\n")
    moves = list(moves)
    transformed = pool.replace("#", "##")
    transformed = transformed.replace(".", "..")
    transformed = transformed.replace("O", "[]")
    transformed = transformed.replace("@", "@.")

    new_pool = [list(x) for x in transformed.split("\n")]

    initial_position = (0, 0)
    for i in range(len(new_pool)):
        for j in range(len(new_pool[i])):
            if new_pool[i][j] == "@":
                initial_position = (i, j)

    while len(moves) > 0:
        move = moves.pop(0)
        print("Move: ", move)   
        c = initial_position
        pending_changes = []
        initial_position = make_move_2(new_pool, initial_position, move, pending_changes)
        if initial_position == (-1, -1):
            initial_position = c
        
        for x in range(len(new_pool)):
            print("".join(new_pool[x]))
        print("\n")
    return 0


if __name__ == "__main__":
    st = time.time()

    input_data = open("./input.txt", "r").read()
    print("Solution for day 15")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))

    et = time.time()

    print("Execution time in seconds: ", et-st)

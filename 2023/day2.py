data = open("./input/day2.txt", "r").readlines()

bag = {"red": 12, "green": 13, "blue": 14}

acc = 0

# part 1
for line in data:
    # Game 1: 1 blue, 2 green, 3 red; ...
    game_id, game_data = line.split(":")
    game_id = game_id.split(" ")[1]
    game_sets = game_data.split(";")
    valid = True
    for game_set in game_sets:
        # 1 blue, 2 green, 3 red; 7 red, 8 green; 1 green, 2 red, 1 blue; ...
        cubes = game_set.strip().split(",")
        if valid is False:
            break
        for c in cubes:
            # 1 blue
            number, color = c.strip().split(" ")
            if int(number) > bag[color]:
                valid = False
                break
    if valid:
        acc += int(game_id)

print(acc)


# part 2
acc = 0
for line in data:
    # Game 1: 1 blue, 2 green, 3 red; ...
    _, game_data = line.split(":")
    game_sets = game_data.split(";")
    max = {"red": 0, "green": 0, "blue": 0}
    for game_set in game_sets:
        # 1 blue, 2 green, 3 red; 7 red, 8 green; 1 green, 2 red, 1 blue; ...
        cubes = game_set.strip().split(",")
        for c in cubes:
            # 1 blue
            number, color = c.strip().split(" ")
            if int(number) > max[color]:
                max[color] = int(number)
    acc += max["blue"] * max["green"] * max["red"]

print(acc)
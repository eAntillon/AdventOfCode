input = open("./input/day7.txt", "r").read().split("\n")

rank = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}

hands = {
    "one pair": 1,  # 1
    "two pairs": 2,  # 2
    "three of a kind": 3,  # 3
    "full house": 4,  # 3 y 2
    "four of a kind": 5,  # 4
    "five of a kind": 6,  # 5
}

sorted_plays = []
cards_arr = []
for line in input:
    cards, bid = line.split(" ")
    cards = [*cards]
    bid = int(bid)
    hand = 0
    cards_count = {}
    strength_per_position = []
    for card in cards:
        if card in cards_count:
            cards_count[card] += 1
        else:
            cards_count[card] = 1
        strength_per_position.append(rank[card])

    card_counts_values = list(cards_count.values())
    if 5 in card_counts_values:
        hand = hands["five of a kind"]
    elif 4 in card_counts_values:
        hand = hands["four of a kind"]
    elif 3 in card_counts_values:
        if 2 in card_counts_values:
            hand = hands["full house"]
        else:
            hand = hands["three of a kind"]
    elif 2 in card_counts_values:
        if card_counts_values.count(2) == 2:
            hand = hands["two pairs"]
        else:
            hand = hands["one pair"]
    else:
        hand = 0
    # print(f" c:{cards} h:{hand} b:{bid} spp:{strength_per_position}")
    cards_arr.append((bid, hand, strength_per_position, cards))

    sorted_plays.append((bid, hand, strength_per_position, cards))

sorted_plays = sorted(sorted_plays, key=lambda x: (x[1], x[2][0], x[2][1], x[2][2], x[2][3], x[2][4] ))

acc = 0
for i in range(len(sorted_plays)):
    acc += sorted_plays[i][0] * (i+1)

print(f"Part 1: {acc}")

# part 2

rank["J"] = 0
sorted_plays = []
cards_arr = []
for line in input:
    cards, bid = line.split(" ")
    cards = [*cards]
    bid = int(bid)
    hand = 0
    cards_count = {}
    strength_per_position = []
    for card in cards:
        if card in cards_count:
            cards_count[card] += 1
        else:
            cards_count[card] = 1
        strength_per_position.append(rank[card])

    max = (0, 0)
    if "J" in cards:
        card_count_dict = cards_count.items()
        for card_key, c in card_count_dict:
            if card_key == "J":
                continue
            if c > max[1]:
                max = (card_key, c)
    if max[0] != 0:
        cards_count[max[0]] += cards_count["J"]
        cards_count["J"] = 0

    card_counts_values = list(cards_count.values())
    if 5 in card_counts_values:
        hand = hands["five of a kind"]
    elif 4 in card_counts_values:
        hand = hands["four of a kind"]
    elif 3 in card_counts_values:
        if 2 in card_counts_values:
            hand = hands["full house"]
        else:
            hand = hands["three of a kind"]
    elif 2 in card_counts_values:
        if card_counts_values.count(2) == 2:
            hand = hands["two pairs"]
        else:
            hand = hands["one pair"]
    else:
        hand = 0
    # print(f" c:{cards} h:{hand} b:{bid} spp:{strength_per_position}")
    cards_arr.append((bid, hand, strength_per_position, cards))

    sorted_plays.append((bid, hand, strength_per_position, cards))

sorted_plays = sorted(sorted_plays, key=lambda x: (x[1], x[2][0], x[2][1], x[2][2], x[2][3], x[2][4] ))

acc = 0
for i in range(len(sorted_plays)):
    acc += sorted_plays[i][0] * (i+1)

print(f"Part 2: {acc}")
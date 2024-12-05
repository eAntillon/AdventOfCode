

def parse_input(input_data):
    orderingRules = input_data.split("\n\n")[0].split("\n")
    orderingRules = [(x.split("|")[0], x.split("|")[1]) for x in orderingRules]
    pageUpdates = input_data.split("\n\n")[1].split("\n")
    pageUpdates = [x.split(",") for x in pageUpdates]

    rulesDict = {}
    for rule in orderingRules:
        rulesDict[rule] = True
    return rulesDict, pageUpdates


def get_rules(rulesDict, pageUpdates):
    validUpdates = []
    invalidUpdates = []
    for update in pageUpdates:
        left, right = 0, len(update) - 1
        while left < right and left + 1 <= right - 1:
            leftRule = (update[left], update[left + 1])
            rightRule = (update[right - 1], update[right])

            if leftRule in rulesDict and rightRule in rulesDict:
                if update[left+1] == update[right-1]:
                    validUpdates.append(update)
                    break
                else:
                    left += 1
                    right -= 1
            else:
                invalidUpdates.append(update)
                break

    return validUpdates, invalidUpdates


def part1(input_data) -> int:
    rulesDict, pageUpdates = parse_input(input_data)
    validUpdates, _ = get_rules(rulesDict, pageUpdates)
    total = 0
    for update in validUpdates:
        total += int(update[len(update) // 2])
    return total


def part2(input_data):
    rulesDict, pageUpdates = parse_input(input_data)
    _, invalidUpdates = get_rules(rulesDict, pageUpdates)
    total = 0
    for update in invalidUpdates:
        i = 0
        while i < len(update) - 1:
            reversedRule = (update[i+1], update[i])
            if reversedRule in rulesDict:
                update[i], update[i+1] = update[i+1], update[i]
                i = 0
            else:
                i += 1
        total += int(update[len(update) // 2])
    return total


def main():
    input_data = open("./input.txt", "r").read()
    print("Solution for day 5")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))


main()

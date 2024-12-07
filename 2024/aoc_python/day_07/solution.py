
from functools import reduce


def get_cases(input_data):
    operations = input_data.split("\n")
    cases = []

    for i in operations:
        test_value, equation = i.split(": ")
        test_value = int(test_value)
        equation_numbers = [int(x) for x in equation.split(" ")]
        cases.append((test_value, equation_numbers))

    return cases


def get_equation_results(acc, numbers):
    if len(numbers) == 1:
        return [acc + numbers[0], acc * numbers[0]]

    results = []

    if acc == -1:
        results.extend(get_equation_results(numbers[0], numbers[1:]))
    else:
        sum_results = get_equation_results(acc + numbers[0], numbers[1:])
        mul_results = get_equation_results(acc * numbers[0], numbers[1:])
        results.extend(sum_results)
        results.extend(mul_results)

    return results


def get_equation_results_with_concats(acc, numbers, target_value):

    if acc > target_value:
        return []
    if len(numbers) == 1:
        return [acc + numbers[0], acc * numbers[0], int(f"{acc}{numbers[0]}")]

    results = []

    if acc == -1:
        results.extend(get_equation_results_with_concats(numbers[0], numbers[1:], target_value))
    else:
        sum_eval = acc + numbers[0]
        if sum_eval <= target_value:
            sum_results = get_equation_results_with_concats(sum_eval, numbers[1:], target_value)
            results.extend(sum_results)
            
        mul_eval = acc * numbers[0]
        if mul_eval <= target_value:
            mul_results = get_equation_results_with_concats(mul_eval, numbers[1:], target_value)
            results.extend(mul_results)

        concat_eval = int(f"{acc}{numbers[0]}")
        if concat_eval <= target_value:
            concat_results = get_equation_results_with_concats(concat_eval, numbers[1:], target_value)
            results.extend(concat_results)

    return results


def part1(input_data) -> int:
    cases = get_cases(input_data)
    valid_cases = []

    for n in cases:
        test_value, numbers = n
        results = get_equation_results(-1, numbers)
        if test_value in results:
            valid_cases.append(test_value)

    return reduce(lambda x, y: x + y, valid_cases)


def part2(input_data):
    cases = get_cases(input_data)
    valid_cases = []

    for n in cases:
        test_value, numbers = n
        results = get_equation_results_with_concats(-1, numbers, test_value)
        if test_value in results:
            valid_cases.append(test_value)

    return reduce(lambda x, y: x + y, valid_cases)


def main():
    input_data = open("./input.txt", "r").read()
    print("Solution for day 7")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))


main()

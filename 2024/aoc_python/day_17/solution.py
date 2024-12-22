import time


def parse_input(input_data):
    input_registries, input_program = input_data.split("\n\n")

    registries = {
        "A": 0,
        "B": 0,
        "C": 0,
    }
    for registry in input_registries.split("\n"):
        registry, value = registry.split(": ")
        registries[registry[-1]] = int(value)

    program = []
    for n in input_program.split(": ")[1].split(","):
        program.append(int(n))

    return registries, program


output = []


def get_combo_operand(registries, operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return registries["A"]
    elif operand == 5:
        return registries["B"]
    elif operand == 6:
        return registries["C"]
    elif operand == 7:
        return ValueError("Invalid operand")


def adv(registries, operand):
    numerator = registries["A"]
    denominator = 2 ** get_combo_operand(registries, operand)
    registries["A"] = numerator // denominator


def bxl(registries, operand):
    registries["B"] = registries["B"] ^ operand


def bst(registries, operand):
    result = get_combo_operand(registries, operand) % 8
    registries["B"] = result


def jnz(registries, operand, pointer):
    if registries["A"] == 0:
        return pointer
    else:
        return operand


def bxc(registries, operand):
    result = registries["B"] ^ registries["C"]
    registries["B"] = result


def out(registries, operand):
    output.append(get_combo_operand(registries, operand) % 8)


def bdv(registries, operand):
    numerator = registries["A"]
    denominator = 2 ** get_combo_operand(registries, operand)
    registries["B"] = numerator // denominator


def biv(registries, operand):
    numerator = registries["A"]
    denominator = 2 ** get_combo_operand(registries, operand)
    registries["C"] = numerator // denominator


def run(registries, program):
    pointer = 0
    while pointer < len(program) - 1:
        instruction = program[pointer]
        operand = program[pointer + 1]
        match instruction:
            case 0:
                adv(registries, operand)
            case 1:
                bxl(registries, operand)
            case 2:
                bst(registries, operand)
            case 3:
                c = pointer
                pointer = jnz(registries, operand, pointer)
                if c == pointer:
                    pointer += 1
                continue
            case 4:
                bxc(registries, operand)
            case 5:
                out(registries, operand)
            case 6:
                bdv(registries, operand)
            case 7:
                biv(registries, operand)
        pointer += 2


def part1(input_data):
    output.clear()
    registries, program = parse_input(input_data)
    run(registries, program)
    return ",".join(map(str, output))


def part2(input_data):
    output.clear()
    target = [2, 4, 1, 3, 7, 5, 1, 5, 0, 3, 4, 2, 5, 5, 3, 0]
    # ever 2^3 changes one position, 2*45 gets an output of len 16,
    # start search from there, then if matches the last n elements of target,
    # update the "a" (start) value and reduce the exponent by 3

    a = 216584205979176
    _, program = parse_input(input_data)
    while True:
        run({"A": a, "B": 0, "C": 0}, program)
        # print(f"A: {a}, program output: {output}")
        if output == target:
            # print(f"Found a match for A: {a}")
            return a
        a += 1
        output.clear()


if __name__ == "__main__":
    st = time.perf_counter()

    input_data = open("./input.txt", "r").read()
    print("Solution for day 17")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))

    et = time.perf_counter()

    print("Execution time in seconds: ", et-st)

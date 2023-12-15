input_lines = open("./input/day13.txt").read().split("\n\n")


def get_transposed(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed.append("")
        for j in range(len(matrix)):
            transposed[i] += matrix[j][i]
    print("--------" * 2)
    for i in transposed:
        print(i)
    return transposed


def get_lines_outside_simetric(lines):
    # horizontal simetric
    simetric_lines = 0
    s = 0
    e = 1
    while e < len(lines):
        if lines[s] == lines[e]:
            simetric_lines += 1
            if s > 0 and e < len(lines) - 1:
                s -= 1 
                e += 1
            else:
                break
        else:
            s += 1
            e += 1
    return (simetric_lines, max(len(lines) - s, len(lines) - e))


acc = 0
for m in input_lines:
    m = m.split("\n")
    print("H")
    for i in m:
        print(i)
    h_simetric_lines = get_lines_outside_simetric(m)
    v_simetric_lines = get_lines_outside_simetric(get_transposed(m))
    if v_simetric_lines[1] > h_simetric_lines[1]:
        acc += v_simetric_lines[0]
    else:
        acc += h_simetric_lines[0] * 100
    print(f"simetric lines: h:{h_simetric_lines} v:{v_simetric_lines}")

print(f"acc: {acc}")

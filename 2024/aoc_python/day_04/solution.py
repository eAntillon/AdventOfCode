

# UP, RIGHT, DOWN, LEFT, UP-RIGHT, DOWN-RIGHT, DOWN-LEFT, UP-LEFT
directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

xmas = {
    "X": "M",
    "M": "A",
    "A": "S",
    "S": "E", # end
}

# validate if the pos tuple is a valid position in the matrix
def validPosition(pos, row, col):
    i, j = pos
    return i >= 0 and j >= 0 and i < row and j < col

# Part 1 - Search for the word "XMAS" in the matrix in all 8 directions
def searchWord(lettersMatrix, i, j, row, col):
    foundWord = 0
    q = []
    q.append((i, j, "X", directions))  # x, y, letter, direction
    while len(q):
        i, j, letter, direction = q.pop(0)
        if letter == "S":
            foundWord += 1
        if letter == "X":
            for n in range(8):
                a = i + direction[n][0]
                b = j + direction[n][1]
                if (
                    validPosition((a, b), row, col)
                    and lettersMatrix[a][b] == "M"
                ):
                    q.append((a, b, lettersMatrix[a][b], direction[n]))
        else:
            nextLetter = xmas[letter]
            a = i + direction[0]
            b = j + direction[1]
            if (
                validPosition((a, b), row, col)
                and lettersMatrix[a][b] == nextLetter
            ):
                q.append((a, b, lettersMatrix[a][b], direction))
    return foundWord




def masSearch(m, i, j, row, col):
    # UP-RIGHT, DOWN-RIGHT, DOWN-LEFT, UP-LEFT
    upRight = [i+1, j+1]
    downRight = [i-1, j+1]
    downLeft = [i-1, j-1]
    upLeft = [i+1, j-1]

#   [1.2]
#   [.a.]
#   [2.1]

    valid = False
    if validPosition(upRight, row, col) and validPosition(downLeft, row, col):
        a,b = upRight
        c,d = downLeft
        # check if the letters are M and S are on the positions up right and down left
        if m[a][b] == "M" and m[c][d] == "S" or m[a][b] == "S" and m[c][d] == "M":
            if validPosition(downRight, row, col) and validPosition(upLeft, row, col):
                a,b = downRight
                c,d = upLeft
                # check if the letters are M and S are on the positions down right and up left
                if m[a][b] == "M" and m[c][d] == "S" or m[a][b] == "S" and m[c][d] == "M":
                    valid = True
    return valid

def part1(input_data: list) -> int:
    lettersMatrix = [list(x) for x in input_data]

    row = len(lettersMatrix)
    col = len(lettersMatrix[0])
    total = 0

    for i in range(row):
        for j in range(col):
            if lettersMatrix[i][j] == "X":
                total += searchWord(lettersMatrix, i, j, row, col)
    return total


def part2(input_data):
    lettersMatrix = [list(x) for x in input_data]

    row = len(lettersMatrix)
    col = len(lettersMatrix[0])
    total = 0

    for i in range(row):
        for j in range(col):
            if lettersMatrix[i][j] == "A":
                total += 1 if masSearch(lettersMatrix, i, j, row, col) else 0
    return total


def main():
    input_data = open("./input.txt", "r").read().split("\n")
    print("Solution for day 4")
    print("Part 1: ", part1(input_data))
    print("Part 2: ", part2(input_data))


main()

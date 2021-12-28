import time
from typing import final

start_time = time.perf_counter()

archivo = open("input10.txt").read().split("\n")
# archivo = open("test.txt").read().split("\n")


types = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


final_scores = []

for line  in [list(i.strip()) for i in archivo]:
    append = True
    open_brakets = []
    for i in line:
        if i in ["(","[","{","<"]:
            open_brakets.append(i)
        else:
            if open_brakets[-1] != types[i]:
                # corrupted
                append = False
                break
            else:
                open_brakets.pop()
    if append and len(open_brakets) > 0:
        end_string = ""
        end_score = 0
        for br in open_brakets:
            end_string = types[br] + end_string
        for char in end_string:
            end_score *= 5
            end_score += scores[char]
        final_scores.append(end_score)
final_scores.sort()
print(final_scores[round(len(final_scores)/2)])
print("--- %s seconds ---" % (time.perf_counter() - start_time))
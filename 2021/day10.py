import time

start_time = time.perf_counter()

archivo = open("input10.txt").read().split("\n")
# archivo = open("test.txt").read().split("\n")


types = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

times = {
    ")": 0,
    "]": 0,
    "}": 0,
    ">": 0,
}


for line  in [list(i.strip()) for i in archivo]:
    open_brakets = []
    for i in line:
        if i in ["(","[","{","<"]:
            open_brakets.append(i)
        else:
            if open_brakets[-1] != types[i]:
                # corrupted
                times[i] += 1
                break
            else:
                open_brakets.pop()
        
total = times[")"] * 3 + times["]"] * 57  + times["}"] * 1197 + times[">"] * 25137
print(total)
print("--- %s seconds ---" % (time.perf_counter() - start_time))
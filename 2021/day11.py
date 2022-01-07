import time
start_time = time.perf_counter()


archivo = open("input11.txt").read().split("\n")
# archivo = open("test.txt").read().split("\n")
def toIntArray(string):
    arr  = list(string.strip())
    return [int(i) for i in arr]

data = [toIntArray(i) for i in archivo]

# PARAMETER
STEPS = 500
total_steps = 0
MAX_ROW = len(data)-1
MAX_COL = len(data[0])-1
total_falshes = 0

def addPoint(n,m,flashed):
    global data, total_falshes
    if (n,m) not in flashed:
        data[n][m] += 1
        if data[n][m] > 9:
            evaluatePoint(n,m,flashed)

def evaluatePoint(i,j,flashed):
    global data
    global total_falshes
    if data[i][j] < 9 and ((i,j) not in flashed): 
        data[i][j] += 1
    elif data[i][j] >= 9 and ((i,j) not in flashed):
        data[i][j] = 0
        total_falshes += 1
        # Add flashed point to list
        flashed.append((i,j))
        # Increment adyacent points
        # UP
        if i > 0:
            addPoint(i-1,j,flashed)
            # UP RIGTH
            if  j < MAX_COL:
                addPoint(i-1,j+1,flashed)
            # UP LEFT
            if j > 0:
                addPoint(i-1,j-1,flashed)
        # LEFT 
        if j > 0:
            addPoint(i,j-1,flashed)
        # RIGHT 
        if j < MAX_COL:
            addPoint(i,j+1,flashed)
        # DOWN
        if i< MAX_ROW:
            addPoint(i+1,j,flashed)
            # UP RIGTH
            if j < MAX_COL:
                addPoint(i+1,j+1,flashed)
            # UP LEFT
            if j > 0:
                addPoint(i+1,j-1,flashed)

# PART 2 STEP VARAIBLE
firts_step_all = 0

for n in range(STEPS):
    flashed = []
    for k1, v1 in enumerate(data):
        for k2, v2 in enumerate(v1):
            evaluatePoint(k1,k2,flashed)
    if len(flashed) >= len(data)**2 and firts_step_all==0:
        firts_step_all = n+1

print(f"PART 1: {total_falshes}")
print(f"PART 2: {firts_step_all}")
print("--- %s seconds ---" % (time.perf_counter() - start_time))
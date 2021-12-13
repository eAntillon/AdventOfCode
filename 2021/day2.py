datos = open('input2.txt').read().split("\n")
datos = [i.split(" ") for i in datos]

horizontal = 0
aim = 0
profundidad = 0
for i in datos:
    if i[0] == 'forward':
        valor = int(i[1])
        profundidad += aim * valor
        horizontal += valor
    elif i[0] == 'up':
        aim -= int(i[1])
    elif i[0] == 'down':
        aim += int(i[1])
        
print(horizontal*profundidad)
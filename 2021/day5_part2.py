import time
start_time = time.time()

input = open("input5.txt").read().split("\n")
lineas = []

xsize = 0
ysize = 0

# Separar en lineas y calcular las dimensiones del array
for i in input:
    linea = i.split(" -> ")
    inicio = [int(x) for x in linea[0].split(",")]
    fin = [int(x) for x in linea[1].split(",")]
    if inicio[0] > xsize: xsize = inicio[0]
    if fin[0] > xsize: xsize = fin[0]
    if inicio[1] > ysize: ysize = inicio[1]
    if fin[1] > ysize: ysize = fin[1]
    lineas.append([inicio, fin])

xsize += 1
ysize += 1
# Array 1 dimension
puntos = [0]*(xsize*ysize)

for linea in lineas:
    # Posicion de inicio
    inicio_y = linea[0][1]
    # Posicion final
    fin_y = linea[1][1]
    # Determina si se iran incrementando o reduciendo
    signo_y = True
    if linea[0][1] > linea[1][1]:
        signo_y = False
        
    inicio_x = linea[0][0]
    fin_x = linea[1][0]
    signo_x = True
    if linea[0][0] > linea[1][0]:
        signo_x = False

    while(True):
        # Aumentar el valor de ese punto en el array de 1 dim
        puntos[(inicio_y*xsize) + inicio_x] += 1
        # Si ambos valores de inicio son iguales al valor final
        if fin_x == inicio_x and fin_y == inicio_y:
            break
        # Determinar si se incrementa o se reduce el valor de inicio
        if fin_x != inicio_x:
            if signo_x:
                inicio_x += 1
            else:
                inicio_x -= 1 
        if fin_y != inicio_y:
            if signo_y:
                inicio_y += 1
            else:
                inicio_y -= 1
                
# Contar mayores a 2
total = 0
for p in puntos:
    if p >= 2: total +=1
print(total)

print("--- %s seconds ---" % (time.time() - start_time))
import time
start_time = time.time()

input = open("input5.txt").read().split("\n")
lineas = []

xsize = 0
ysize = 0

for i in input:
    linea = i.split(" -> ")
    inicio = [int(x) for x in linea[0].split(",")]
    fin = [int(x) for x in linea[1].split(",")]
    if inicio[0] == fin[0] or inicio[1] == fin[1]:
        if inicio[0] > xsize: xsize = inicio[0]
        if fin[0] > xsize: xsize = fin[0]
        if inicio[1] > ysize: ysize = inicio[1]
        if fin[1] > ysize: ysize = fin[1]
        lineas.append([inicio, fin])
xsize += 1
ysize += 1
puntos = [0]*(xsize*ysize)
for linea in lineas:
    if linea[0][0] == linea[1][0]:
        # Marcar linea en y
        inicio_y = linea[0][1]
        fin_y = linea[1][1]
        nivel_x = linea[0][0]
        if linea[0][1] > linea[1][1]:
            # Cambiar orden si es necesario
            inicio_y = linea[1][1]
            fin_y = linea[0][1]
        # Aumentar puntos en array
        while(inicio_y <= fin_y):
            puntos[(inicio_y*ysize) + nivel_x] += 1
            inicio_y +=1
    else:
        #Marcar linea en x
        inicio_x = linea[0][0]
        fin_x = linea[1][0]
        nivel_y = linea[0][1] - 1
        if linea[0][0] > linea[1][0]:
            # Cambiar orden si es necesario
            inicio_x = linea[1][0]
            fin_x = linea[0][0]
        # Aumentar puntos en array
        while(inicio_x <= fin_x):
            puntos[(nivel_y*xsize) + inicio_x ] += 1
            inicio_x +=1

# Contar mayores a 2
total = 0
for p in puntos:
    if p >= 2: total +=1

print(total)

print("--- %s seconds ---" % (time.time() - start_time))
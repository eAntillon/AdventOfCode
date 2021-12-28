import time
import heapq

start_time = time.perf_counter()

archivo = open("input9.txt").read().split("\n")
# archivo = open("test.txt").read().split("\n")

def toIntArray(lista):
    return [int(i) for i in lista]

datos = [toIntArray(list(i.strip())) for i in archivo]

low_points = []
MAX_ROW = len(datos)-1
MAX_COL = len(datos[0])-1
for k1,v1 in enumerate(datos):
    for k2, v2 in enumerate(v1):
        # arriba
        adyacentes = 0
        menores = 0
        if v2 == 10: continue
        if k1 > 0:
            adyacentes +=1
            if v2 < datos[k1-1][k2]:
                menores += 1
            # arriba izquierda
            if k2 > 0:
                adyacentes +=1
                if v2 < datos[k1-1][k2-1]:
                    menores += 1
            # arriba derecha
            if k2 < MAX_COL:
                adyacentes +=1
                if v2 < datos[k1-1][k2+1]:
                    menores += 1
        # abajo
        if k1 < MAX_ROW:
            adyacentes +=1
            if v2 < datos[k1+1][k2]:
                menores += 1
            # abajo izquierda
            if k2 > 0:
                adyacentes +=1
                if v2 < datos[k1+1][k2-1]:
                    menores += 1
            # abajo derecha
            if k2 < MAX_COL:
                adyacentes +=1
                if v2 < datos[k1+1][k2+1]:
                    menores += 1
        # izquierda
        if k2 > 0:
            adyacentes +=1
            if v2 < datos[k1][k2-1]:
                menores += 1
        # derecha
        if k2 < MAX_COL:
            adyacentes +=1
            if v2 < datos[k1][k2+1]:
                menores += 1
        if menores >= adyacentes:
            low_points.append((k1,k2))
sizes = []

for point in low_points:
    visited = []
    toVisit = [point]
    while len(toVisit) > 0:
        if toVisit[0] in visited:
            toVisit.pop(0)
            continue
        row, col = toVisit[0]
        # arriba
        if row > 0:
            if datos[row-1][col] != 9 and (row-1,col) not in visited:
                toVisit.append((row-1,col))
        # abajo
        if row < MAX_ROW:
            if datos[row+1][col] != 9 and (row+1,col) not in visited:
                toVisit.append((row+1,col))
        # izquierda
        if col > 0:
            if datos[row][col-1] != 9 and (row,col-1) not in visited:
                toVisit.append((row,col-1))
        # derecha
        if col < MAX_COL:
            if datos[row][col+1] != 9 and (row,col+1) not in visited:
                toVisit.append((row,col+1))
        visited.append((row,col))
        toVisit.pop(0)
    sizes.append(len(visited))

mayores = heapq.nlargest(3, sizes)
print( mayores[0] * mayores[1] * mayores[2] )
print("--- %s seconds ---" % (time.perf_counter() - start_time))
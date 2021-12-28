import time

start_time = time.perf_counter()

archivo = open("input9.txt").read().split("\n")
# archivo = open("test.txt").read().split("\n")

def toIntArray(lista):
    return [int(i) for i in lista]

datos = [toIntArray(list(i.strip())) for i in archivo]

low = []
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
            low.append(v2)
sum = 0
for i in low:
    sum += i+1
print(sum)

print("--- %s seconds ---" % (time.perf_counter() - start_time))
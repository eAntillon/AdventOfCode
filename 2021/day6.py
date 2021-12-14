import time
import collections

start_time = time.perf_counter()

datos = open("input6.txt").read().split(",")
datos = [int(i) for i in datos]
conteos_dict = {}
# Insertar llaves (0-9) en diccionario vacio
for i in range(9):
    conteos_dict[i] = 0

conteos = dict(collections.Counter(datos))
conteos = sorted(conteos.items())
# Agregar valores contados al diccionario con las llaves
for k,v in conteos:
    conteos_dict[k] = v

temporal = 0
for x in range(256):
    for k,v in conteos_dict.items():
        if k == 0:
            temporal = v
        if k == 8:
            conteos_dict[k] = temporal
            continue
        conteos_dict[k] = conteos_dict[k+1]
    conteos_dict[6] += temporal
    
total = 0
for v in conteos_dict.values():
    total += v
print(total)
print("--- %s seconds ---" % (time.perf_counter() - start_time))
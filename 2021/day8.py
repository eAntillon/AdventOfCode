import time
start_time = time.perf_counter()

archivo = open("input8.txt").read().split("\n")
datos = []
for linea in archivo:
    aux = [i.split(" ") for i in linea.split(" | ")]
    datos.append(aux)

contador = 0
for input, output in datos:
    for cadena in output:
        if len(cadena) == 2 or len(cadena) == 3 or len(cadena) == 4 or len(cadena) == 7:
            contador += 1               

print(contador)
print("--- %s seconds ---" % (time.perf_counter() - start_time))
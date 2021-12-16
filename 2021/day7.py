import time
import collections

start_time = time.perf_counter()

datos = open("input7.txt").read().split(",")
datos = [int(i) for i in datos]

conteos = dict(collections.Counter(datos))
datos = sorted(conteos.items())
limite_inferior = datos[0][0]
limite_superior = datos[-1][0]
rango = limite_inferior - limite_superior
if rango < 0: rango *= -1
medio = -(-rango//2)
def calcular_distancia(punto, lista):
    total = 0
    for i in lista:
        valor, rep = i
        distancia = punto - valor
        if distancia < 0: distancia *= -1
        # Parte 2 en parte 2
        distancia = (distancia * (distancia + 1))/2
        total += distancia * rep
    return total

menor  = 0
while (True):
    combustible_punto = calcular_distancia(medio, datos)
    menor = combustible_punto
    if medio > rango: break
    combustible_derecha = calcular_distancia(medio+1, datos)
    if medio == 0: break
    combustible_izquierda = calcular_distancia(medio-1, datos)
    if combustible_izquierda < combustible_punto and combustible_izquierda < combustible_derecha:
        limite_superior = medio-1
        aux = (medio-1-limite_inferior)
        medio  = -(-aux//2) + limite_inferior
        menor = combustible_izquierda
    elif combustible_derecha < combustible_punto and combustible_derecha < combustible_izquierda:
        limite_inferior = medio+1
        aux = (limite_superior - medio)
        medio  = -(-aux//2) + medio
        menor = combustible_derecha
    else:
        break

        
print(int(menor))
print("--- %s seconds ---" % (time.perf_counter() - start_time))

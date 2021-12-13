import numpy as np
import time
start_time = time.time()

def convertir_string_array(tableros):
    tableros_res = []
    for i in range(len(tableros)):
        linea = tableros[i]
        arr = linea.split("\n")
        for i in range(len(arr)):
            arr_aux = list(filter(lambda x: x != '', arr[i].split(" ")))
            arr[i] = arr_aux
        tableros_res.append(arr)
    return tableros_res

def insertar_numero(tablero, numero):
    arr = []
    for i in range(len(tablero)):
        linea = tablero[i]
        for j in range(len(linea)):
            num = linea[j]
            if num == numero:
                linea[j] = 'x'
        arr.append(linea)
    return arr

def validar_tablero(tablero):
    for linea in tablero:
        cadena = 'xxxxx'
        if cadena == ''.join(linea):
            return tablero
    tablero_transpuesto = np.transpose(tablero)
    for linea in tablero_transpuesto:
        cadena = 'xxxxx'
        if cadena == ''.join(linea):
            return tablero
    return False

def contar_puntaje(tablero):
    suma = 0
    for linea in tablero:
        for num in linea:
            if num != 'x':
                suma += int(num)
    return suma

datos = open("input4.txt").read().split("\n\n")

numeros = datos[0].split(",")
tableros = datos[1:]

res = 0

tableros = convertir_string_array(tableros)
encontrado = False

for i in numeros:
    if encontrado: break
    for tab in tableros:
        insertar_numero(tab, i)
        validacion = validar_tablero(tab)
        if validacion != False:
            res = contar_puntaje(validacion) * int(i)
            encontrado = True
            break

print("Part1: ",res)

for i in numeros:
    if len(tableros) == 0: break
    borrar = []
    for tab in tableros:
        tab_copy = tab
        tab_copy = insertar_numero(tab_copy, i)
        validacion = validar_tablero(tab_copy)
        if validacion != False:
            res = contar_puntaje(validacion) * int(i)
            borrar.append(tab)
    for b in borrar:
        tableros.remove(b)
print("Part2: ",res)

print("--- %s seconds ---" % (time.time() - start_time))

import numpy as np

def split(word):
    return [ch for ch in word]

def calcular_common(lista, n):
    transpuesta = np.transpose(lista)
    common = -1
    conteo_1 = 0
    conteo_0 = 0 
    for j in transpuesta[n]:
        if j == "1":
            conteo_1 += 1
        else:
            conteo_0 += 1
    if conteo_1 > conteo_0:
        common = "1"
    elif conteo_0 > conteo_1:
        common = "0"
    return common
        

datos = open('input3.txt').read().split("\n")
datos = [split(i) for i in datos]
lista_oxigeno = datos
lista_co2 = datos

oxygen = ''
co2 = ''

'''LLENAR OXIGENO'''
for n in range(len(datos[0])):
    if len(lista_oxigeno) == 1:
        oxygen = "".join(lista_oxigeno[0])
        break
    common = calcular_common(lista_oxigeno, n)
    lista_oxigeno_temp=[]
    for i in lista_oxigeno:
        if i[n] == common or (common == -1 and i[n] == "1"):
            lista_oxigeno_temp.append(i)
    lista_oxigeno = lista_oxigeno_temp
print(oxygen)

'''LLENAR CO2'''
for n in range(len(datos[0])):
    if len(lista_co2) == 1:
        co2 = "".join(lista_co2[0])
        break
    common = calcular_common(lista_co2, n)
    lista_co2_temp=[]
    for i in lista_co2:
        if (common == -1 and i[n] == "0") or (common != -1 and i[n] != common):
            lista_co2_temp.append(i)
    lista_co2 = lista_co2_temp
print(co2)

oxygen_decimal = 0
for digit in oxygen:
    oxygen_decimal = oxygen_decimal*2 + int(digit)

co2_decimal = 0
for digit in co2:
    co2_decimal = co2_decimal*2 + int(digit)

print('oxygen: ', oxygen_decimal, " co2: ", co2_decimal, " total: ", oxygen_decimal * co2_decimal)
import numpy as np

def split(word):
    return [ch for ch in word]

datos = open('input3.txt').read().split("\n")
datos = [split(i) for i in datos]
datos = np.transpose(datos)

gamma = ''
epsilon = ''

for i in datos:
    conteo_1 = 0
    conteo_0 = 0 
    for j in i:
        if j == "1":
            conteo_1 += 1
        else:
            conteo_0 += 1
    if conteo_1 > conteo_0:
        gamma += "1"
        epsilon +="0"
    else:
        gamma += "0"
        epsilon +="1"


gamma_decimal = 0
for digit in gamma:
    gamma_decimal = gamma_decimal*2 + int(digit)

epsilon_decimal = 0
for digit in epsilon:
    epsilon_decimal = epsilon_decimal*2 + int(digit)

print('gamma: ', gamma_decimal, " epsilon: ", epsilon_decimal, " total: ", gamma_decimal * epsilon_decimal)
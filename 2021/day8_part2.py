import time
import pprint

start_time = time.perf_counter()
pp = pprint.PrettyPrinter(depth=4)

archivo = open("input8.txt").read().split("\n")
datos = []
for linea in archivo:
    aux = [i.split(" ") for i in linea.split(" | ")]
    datos.append(aux)

# Valores numericos a sumar
valores_decifrados = []
for linea in datos:
    num = {}
    grupo5 = []
    grupo6 = []
    # Asginar los valores simples de tamaño fijo 1,4,7,8
    for signal in linea[0]:
        if len(signal) == 2:
            num[1] = list(signal)
        elif len(signal) == 3:
            num[7] = list(signal)
        elif len(signal) == 4:
            num[4] = list(signal)
        elif len(signal) == 5:
            grupo5.append(list(signal))
        elif len(signal) == 6:
            grupo6.append(list(signal))
        elif len(signal) == 7:
            num[8] = list(signal)
    # Encontrar el numero 3
    for signal in grupo5:
        coincidencias = set(signal).intersection(set(num[1]))
        if len(coincidencias) == 2:
            num[3] = signal
            grupo5.remove(signal)
            # Encontrar el numero 9 en base al 3
            for signal in grupo6:
                coincidencias = set(signal).intersection(set(num[3]))
                if len(coincidencias) == 5:
                    num[9] = signal
                    grupo6.remove(signal)
    
    # Encontrar el numero 5 en base al 9
    for signal in grupo5:
        coincidencias = set(signal).intersection(set(num[9]))
        if len(coincidencias) == 5:
            num[5] = signal
            grupo5.remove(signal)
            # Encontrar el numero 6 en base al 5
            for signal in grupo6:
                coincidencias = set(signal).intersection(set(num[5]))
                if len(coincidencias) == 5:
                    num[6] = signal
                    grupo6.remove(signal)
    num[2] = grupo5[0]   
    num[0] = grupo6[0]

    numero = ""
    for digito in linea[1]:
        for k,v in num.items():
            diferencia = set(list(digito)).symmetric_difference(v)
            if  len(diferencia) == 0:
                numero += str(k)
                break
    valores_decifrados.append(int(numero))

suma = 0
for i in valores_decifrados:
    suma += i
print(suma)
print("--- %s seconds ---" % (time.perf_counter() - start_time))

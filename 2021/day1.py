datos = open('input1.txt').read().split("\n")

datos = [int(i) for i in datos]

mayor = datos[0]
conteo = 0

for i in datos:
    if i > mayor:
        conteo +=1
    mayor = i

print(conteo)
#Questão 04

matriz = []
diagonal = []

matriz = [[0]] * 3
for indice in range(3):
    matriz[indice] = [0] * 3

for indiceX in range(3):
    for indiceY in range(3):
        matriz[indiceX][indiceY] = int(input("Insira um valor: "))

for indiceX in range(3):
    for indiceY in range(3):
        if indiceY == indiceX:
            diagonal.append(matriz[indiceX][indiceY])
            break

for indice in range(len(matriz)):
    print(matriz[indice])

print(sum(diagonal))

print(max(diagonal))

print(min(diagonal))
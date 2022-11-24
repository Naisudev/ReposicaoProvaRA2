#Questão 02

valores = [0] * 10

for indice in range(10):
    valores[indice] = int(input("Insira um número: "))

def Pares():
    print("Pares")
    for indice in range(10):
        if valores[indice] % 2 == 0:
            print(valores[indice])

def Impares():
    print("Ímpares")
    for indice in range(10):
        if valores[indice] % 2 != 0:
            print(valores[indice])

Pares()
Impares()
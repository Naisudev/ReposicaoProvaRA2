#Questão 03

def Circulo():
    raio = float(input("raio = "))
    resultado = 3.1415 * raio * raio
    print("A area é ",resultado)

def Quadrado():
    lado = float(input("lado = "))
    resultado = lado * lado
    print("A area é ",resultado)

def Retangulo():
    base = float(input("base = "))
    altura = float(input("altura = "))
    resultado = base * altura
    print("A area é ",resultado)

while True:
    print("1 - Círculo")
    print("2 - Quadrado")
    print("3 - Retângulo")
    print("4 - Sair")
    escolha = int(input("-> "))
    if escolha == 1:
        Circulo()
    elif escolha == 2:
        Quadrado()
    elif escolha == 3:
        Retangulo()
    elif escolha == 4:
        break
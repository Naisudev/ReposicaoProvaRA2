#Questão 01

nomes = [''] * 5
notas = [''] * 5

for indice in range(5):
    nomes[indice] = str(input("Insira o nome do(a) aluno(a): "))

for indice in range(5):
    notas[indice] = float(input("Insira a nota do(a) aluno(a): "))

def CalcularNota(nota):
    if nota > 7:
        return "foi aprovado(a)"
    elif nota < 7 and nota > 4:
        return "está em recuperação"
    else:
        return "foi reprovado(a)"

for indice in range(5):
    print(nomes[indice], " ", CalcularNota(notas[indice]), " com nota ", notas[indice])
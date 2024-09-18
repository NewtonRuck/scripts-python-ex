import random
n1 = str(input('Nome do aluno: '))
n2 = str(input('Nome do aluno: '))
n3 = str(input('Nome do aluno: '))
n4 = str(input('Nome do aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem escolhida foi ')
print(lista)
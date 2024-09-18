import random
pri = str(input('Digite o nome do primeiro aluno '))
seg = str(input('Digite o nome do segundo aluno '))
ter = str(input('Digite o nome do terceiro aluno '))
qua = str(input('Digite o nome do quarto aluno '))
lista = [pri, seg, ter, qua]
sorteio = random.choice(lista)
print('O aluno escolhido é {}.'.format(sorteio))


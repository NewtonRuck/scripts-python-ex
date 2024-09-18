n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
menor = n2
if n1 < n2 and n1 < n3:
    menor = n1
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor é {}.'.format(menor))
maior = n2
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor é {}.'.format(maior))

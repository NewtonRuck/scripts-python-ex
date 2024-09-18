cont = 0
soma = 0
for n in range(1, 7):
    num = int(input('Digite o valor {}: '.format(n)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} número(s) pares, a soma deste(s) resulta em {}'.format(cont, soma))
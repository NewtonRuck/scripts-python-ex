#Contador = cont, Acumulador = soma.
soma = 0
cont = 0
for s in range(1, 501, 2):
    if s % 3 == 0:
        cont += 1
        soma += s
#Caso cont estivesse fora do bloco de for, ele mostraria o número de todos os números ímpares
print('A soma de {} números divisíveis por 3 e ímpares é {}'.format(cont, soma))


from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-='*15)
cont = 0
while True:
    valor = int(input('Diga um valor de 1 a 10: '))
    opcao = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    pc = randint(1, 10)
    resultado = pc + valor
    cont += 1
    print(f'\nVocê jogou {valor} e o computador jogou {pc}. O total deu {resultado}', end=' ')
    print(', que é par' if resultado % 2 == 0 else ', que é ímpar')
    if resultado % 2 == 0 and opcao == 'I':
        break
    if resultado % 2 != 0 and opcao == 'P':
        break
    print('\nVamos jogar novamente...\n')
print(f'\nVocê perdeu com {cont} tentativa(s)')
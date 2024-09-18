n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('\n>>> Qual sua opção? '))
    print('=-' * 20)
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        elif n2 > n1:
            print('O maior número é {}.'.format(n2))
        else:
            print('Os dois valores são iguais!')
#No "opcao == 4", n1 e n2 recebem novos valores e o loop restarta, porém, como em no comando "for", n1 e n2
#serão trabalhados com seus novos valores.
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        from time import sleep
        print('Saindo do programa...')
        sleep(1.5)
    else:
        print('Opção inválida, tente novamente!')
    print('=-'*20)
print('Fim do programa, volte sempre!')
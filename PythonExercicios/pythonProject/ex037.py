num = int(input('Digite um número inteiro: '))
print('''Escolha a base para conversão:
\033[1;34m[ 1 ]\033[m Converter para Binário;
\033[1;34m[ 2 ]\033[m Converter para Octal;
\033[1;34m[ 3 ]\033[m Converter para Hexadecimal.''')
opcao = int(input('Digite o número correspondente a sua opção: '))
if opcao == 1:
    print('O valor \033[1;31m{}\033[m convertido para binário é \033[1;31m{}\033[m'.format(num, bin(num)))
elif opcao == 2:
    print('O valor \033[1;31m{}\033[m convertido para octal é \033[1;31m{}\033[m'.format(num, oct(num)))
elif opcao == 3:
    print('O valor \033[1;31m{}\033[m convertido para hexadecimal é \033[1;31m{}\033[m'.format(num, hex(num)))
else:
    print('\033[1;31mOpção inválida, tente novamente.\033[m')
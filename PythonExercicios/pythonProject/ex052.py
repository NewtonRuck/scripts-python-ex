cont = 0
num = int(input('Digite um número: '))
for primo in range(1, num+1):
    if num % primo == 0:
        print('\033[1;31m {}\033[m'.format(primo), end=' ')
        cont += 1
    else:
        print('\033[1;34m {}\033[m'.format(primo), end=' ')
if cont == 2:
    print('O número {} foi dividido {} vezes, logo é primo.'.format(num, cont))
else:
    print('O número {} foi dividido {} vezes, logo não é primo.'.format(num, cont))
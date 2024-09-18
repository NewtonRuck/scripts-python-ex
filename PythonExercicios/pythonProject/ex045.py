#itens = ('Pedra', 'Papel', 'Tesoura')
#computador = random.randint(0, 2)
#print('O computador jogou {}.'.format(itens[computador]))
#print('O jogador jogou {}.'.format(itens[opcao]))
import random
from time import sleep
print('''Suas opções
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
opcao = int(input('Qual sua escolha? '))
pedra = 1
papel = 2
tesoura = 3
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
sleep(1)
print('-='*20)
jkp = [pedra, papel, tesoura]
from random import choice
resultado = random.choice(jkp)
if opcao == resultado:
    print('Empate')
elif opcao == 1 and resultado == 2:
    print('O computador escolheu papel, você perdeu :(')
elif opcao == 1 and resultado == 3:
    print('O computador escolheu tesoura, parabéns você venceu!')
elif opcao == 2 and resultado == 1:
    print('O computador escolheu pedra, parabéns você venceu!')
elif opcao == 2 and resultado == 3:
    print('O computador escolheu tesoura, você perdeu :(')
elif opcao == 3 and resultado == 1:
    print('O computador escolheu pedra, você perdeu :(')
elif opcao == 3 and resultado == 2:
    print('O computador escolheu papel, você venceu!')
else:
    print('Opção inválida, tente novamente.')
print('-='*20)
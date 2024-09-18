print('=--'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar . . .')
print('=--'*20)
num = int(input('Em qual número eu pensei? '))
from time import sleep
print('PROCESSANDO . . .')
sleep(3)
from random import randint
pc = randint(0, 5)
if num == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(pc, num))


from random import randint
print('\033[1;31mSou seu computador...\033[m')
print('\n\033[1;34mAcabei de pensar em um número entre 0 e 10.\033[m \n\033[1;34mSerá que você consegue adivinhar qual foi?\033[m')
cont = 1
palpite = int(input('\nQual o seu palpite? '))
computador = randint(1, 10)
while palpite != computador:
    cont += 1
    if computador > palpite:
        palpite = int(input('\n\033[1;33mMais...\033[m Qual o seu palpite? '))
    else:
        palpite = int(input('\n\033[1;33mMenos...\033[m Qual seu palpite? '))
print('\n\033[1;35mParabéns!!!\033[m Você conseguiu acertar em \033[1;35m{}\033[m tentativa(s)'.format(cont))
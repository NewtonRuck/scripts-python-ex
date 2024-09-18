print('=-'*15)
print('{:^30}'.format('BANCO DO BRASIL'))
print('=-'*15)
valor = int(input('Qual valor você deseja retirar? R$'))

#ced = 50 pois será retirado 50 até onde conseguirmos do valor inicial
ced = 50
totced = 0

#loop que fará retirar do valor total, a quantidade de cedulas menor que o valor inicial
while True:

    #valor = 100 > 50, valor - 50 = 50 - 50 = 0, 2 vezes
    if valor >= ced:
        valor -= ced
        totced += 1

    #variavel cedula trocando seu valor
    #caso o valor total esteja menor que o valor da cedula utilizada
    else:
        print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if valor == 0:
            break

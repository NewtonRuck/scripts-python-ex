tabuada = 0
while True:
    cont = 0
    num = int(input('Você quer ver a tabuada de qual número? [Número negativo para parar] '))
    if num < 0:
        print('\nObrigado por utilizar nosso programa!')
        break
    while cont < 10:
        cont += 1
        tabuada = num * cont
        print(f'{num} x {cont} = {tabuada}')
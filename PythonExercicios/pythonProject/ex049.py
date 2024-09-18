num = int(input('Digite um número para ver sua tabuada: '))
for t in range (1, 11):
    tabuada = num * t
    print('{} x {} = {}'.format(num, t, tabuada))
#Não é necessário criar uma variável para tabuada, no format basta colocar num * t que funciona igual.
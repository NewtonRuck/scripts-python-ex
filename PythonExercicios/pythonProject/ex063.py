print('-'*40)
print('Sequência de Fibonacci')
print('-'*40)
num = int(input('Quantos termos você quer mostrar? '))
cont = 2
x = 0
y = 1
print('{} → {} →'.format(x, y), end=' ')
while cont < num:
    z = x + y
    print('{} →'.format(z), end=' ')
    x = y
    y = z
    cont += 1
print('FIM')



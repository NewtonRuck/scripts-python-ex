# Forma Alternativa:
#   c = num
#   f = 1
#   while c > 0:
#       f = f * c
#       c = c - 1
num = int(input('Digite um número natural diferente de 0 que irei calcular seu fatorial: '))
num1 = num - 1
num2 = num * num1
fatorial = num
while num1 != 1:
    num1 = num1 - 1
    num2 = num2 * num1
print('Calculando {}! ='.format(num), end=' ')
for fatorial in range(num, 0, -1):
    print('{}'.format(fatorial), end='')
    print(' x ' if fatorial > 1 else ' = ', end='')
    fatorial -= 1
print('{}'.format(num2))

num = int(input('Me diga um número qualquer: '))
par = num % 2
if par == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))
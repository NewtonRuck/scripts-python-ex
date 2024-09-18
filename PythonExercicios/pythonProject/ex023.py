#Com loop ficará mais fácil de fazer esse exercício no formato str
#numero = str(input('Digite um número de 4 algarismos: '))
#print('Analisando o número {}'.format(numero))
#print('Unidade: {}'.format(numero[3]))
#print('Dezena: {}'.format(numero[2]))
#print('Centena: {}'.format(numero[1]))
#print('Milhar: {}'.format(numero[0]))
num = int(input('Informe um número: '))
u = num // 1 % 10 #Divisão inteira por 1, 10, 100 ou 1000 e após isso retira o resto da divisão por 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
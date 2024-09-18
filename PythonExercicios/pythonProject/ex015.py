dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados no veículo? '))
print('O total a pagar é R${:.2f}'.format((60*dias) + (0.15*km)))

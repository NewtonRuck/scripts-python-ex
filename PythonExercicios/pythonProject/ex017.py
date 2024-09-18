from math import hypot
cop = float(input('Qual o cateto oposto? '))
cad = float(input('Qual o cateto adjacente? '))
hip = hypot(cop, cad)
print('A hipotenusa é igual a {}.'.format(hip))

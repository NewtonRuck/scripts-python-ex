d = float(input('Qual a distância da viagem? '))
if d <= 200:
    custo = 0.5*d
else:
    custo = 0.45*d
print('Você está prestes a começar uma viagem de {:.0f}km.\nE O preço da sua passagem será de R${:.2f}'.format(d, custo))
soma = 0
velho = 0
nomevelho = ''
cont = 0
for p in range(1, 5):
    print('{:=^40}'.format(' {}º Pessoa ').format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma += idade
    if p == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome
    if idade > velho and sexo in 'Mm':
            velho = idade
            nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        cont += 1
print('A média de idade entre as pessoas é {:.2f}'.format(soma / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, nomevelho))
print('Há {} mulher(es) com menos de 20 anos.'.format(cont))

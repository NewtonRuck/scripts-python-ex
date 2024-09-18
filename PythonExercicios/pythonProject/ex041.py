from datetime import date
ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano
print('O atleta tem {} anos'.format(idade))
#Ao colocar apenas o "<=" acompanhado do aninhamento de condicionais, você estabelece um limite.
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Júnior')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')
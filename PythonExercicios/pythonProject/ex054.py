from datetime import date
cont_maioridade = 0
cont_minoridade = 0
for pessoas in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(pessoas)))
    if date.today().year - ano >= 18:
        cont_maioridade += 1
    else:
        cont_minoridade += 1
print('Ao todo tivemos {} pessoas maiores de idade e {} menores de idade'.format(cont_maioridade, cont_minoridade))
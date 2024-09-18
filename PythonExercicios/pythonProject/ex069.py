#Iniciando variáveis
mais18 = 0
menos20 = 0
homens = 0

#Loop Formulário
while True:
    print('-'*50)
    print('CADASTRE UMA NOVA PESSOA')
    print('-'*50)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

    #Loop para resposta correta: Sexo
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

    #Condicionais para resposta do print final:
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        menos20 += 1
    if idade > 18:
        mais18 += 1
    print('-' * 50)
    opcao = (input('Quer continuar [S/N]: ')).upper().strip()[0]

    #Loop resposta correta: Opção
    while opcao not in 'SN':
        opcao = (input('Quer continuar [S/N]: ')).upper().strip()[0]
    if opcao in 'N':
        break
print(f'a) {mais18} pessoa(s) são maiores de idade')
print(f'b) {homens} homens foram cadastrados')
print(f'c) {menos20} mulher(es) tem menos de 20 anos')
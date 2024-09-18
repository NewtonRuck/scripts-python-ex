print('=-'*20)
print('LOJA SUPER BARATÃO')
print('=-'*20)
soma = maisqmil = maisbarato = cont = 0
nomebarato = ''
while True:
    nome = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço do produto: R$'))
    opcao = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    soma += preco
    cont += 1
    if preco > 1000:
        maisqmil += 1
    if cont == 1:
        maisbarato = preco
        nomebarato = nome
    else:
        if preco < maisbarato:
            maisbarato = preco
            nomebarato = nome
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if opcao in 'N':
        print('\nFIM DO PROGRAMA...\n')
        break
print(f'{nomebarato} é o nome do produto mais barato, e seu preço é R${maisbarato:.2f}\n{maisqmil} é a quantidade de produtos que custam mais que R$1000.00')
print(f'R${soma:.2f} é o total da compra')

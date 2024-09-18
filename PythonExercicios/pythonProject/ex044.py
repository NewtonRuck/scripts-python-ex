print('{:=^40}'.format(' MARIA FARINHA '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco * 0.9
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 2:
    total = preco * 0.95
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 3:
    total = preco / 2
    print('Sua compra de R${:.2f} vai ser parcelada em 2x de {:.2f} e vai passar a custar R${:.2f} no final.'.format(preco, total, preco))
elif opcao == 4:
    total = preco + (preco * 0.20)
    parc = int(input('Quantas parcelas? '))
    totparc = total/parc
    print('Sua compra será parcelada em {}x de R${:.2f} e agora vai custar R${:.2f} no final(COM JUROS).'.format(parc, totparc, total))
else:
    print('Opção inválida, tente novamente!')
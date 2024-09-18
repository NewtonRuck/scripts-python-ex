valor_casa = float(input('Qual o valor da casa? R$'))
salario_comprador = float(input('Qual o salário do comprador? R$'))
ano_financiamento = int(input('Quantos anos de financiamento? '))
#PRESTAÇÃO MENSAL
prestacao = valor_casa / (12 * ano_financiamento)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor_casa, ano_financiamento, prestacao))
#PRESTAÇÃO MENSAL NÃO PODE EXCEDER 30% DO SALÁRIO
if prestacao >= 0.3 * salario_comprador:
    print('Empréstimo \033[1;31mNEGADO\033[m!')
else:
    print('Empréstimo pode ser \033[1;34mCONCEDIDO\033[m')
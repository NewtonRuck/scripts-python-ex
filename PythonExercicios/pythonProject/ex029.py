v = float(input('Qual a velocidade do carro? '))
m = (v-80)*7
if v > 80:
    print('\nVocê foi multado! Excedeu o limite permitido de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(m))
print('\nTenha um bom dia! Dirija com segurança!')

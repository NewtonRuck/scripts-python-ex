print('{:=^80}'.format(' PROGRESSÃO ARITMÉTICA DE X TERMOS '))
pritermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
qntd = int(input('Digite a quantidade de termos: '))

#for list_termos in range(pritermo, decimo, razao): tbm daria certo
#porém teria de ser criada uma variável que calculasse o décimo termo
for list_termos in range(1, qntd+1):
    termo = pritermo + (list_termos - 1)*razao
    print(termo, '→', end=' ')
print('Acabou!')
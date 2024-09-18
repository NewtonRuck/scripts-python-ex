print('{:=^80}'.format(' PROGRESSÃO ARITMÉTICA DE 10 TERMOS '))
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

#cont = contador limitante para PA de 10
cont = 1
#mais = quantidade de termos a mais (depois de 10)
mais = 10
#total = limitante para quantidade de termos a mais
total = 0

#enquanto mais for diferente de 0(como 10 nasce diferente de 0, o programa nasce rodando)
#total = total + mais (até fazer a PA de 10, total = 10)
while mais != 0:
    total += mais

#enquanto o contador for menor que o total (no começo até chegar em 10 e depois até chegar em (total + mais)
#como o contador permanece inalterado após a pausa, seu valor será adicionado de 1 até chegar em (total + mais)
#após o inicio do programa que o cont ficar = 10, o programa pede um (novo) valor para "mais" que será adicionado
#ao total e será ao novo total (por exemplo, mais = 2, total = 12, contador deve chegar até 12 partindo de 10)
    while cont <= total:
        print(primeiro_termo, '→', end=' ')
        cont += 1
        termo = primeiro_termo + razao
        primeiro_termo = termo
    print('PAUSA')
    mais = int(input('Quantos termos você deseja mostrar a mais? '))

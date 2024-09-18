n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
n3 = float(input('Qual a terceira nota? '))
media = (n1 + n2 + n3)/3
print('Tirando {}, {} e {} sua média é {:.1f}'.format(n1, n2, n3, media))
if 7 > media >= 5:
    print('O aluno está de \033[1;31mRECUPERAÇÃO!\033[m')
elif media < 5:
    print('O aluno está \033[1;31mREPROVADO!\033[m')
else:
    print('O aluno está \033[1;34mAPROVADO!\033[m')
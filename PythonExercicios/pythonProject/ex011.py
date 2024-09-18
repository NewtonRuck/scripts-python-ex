comp = float(input('Qual o comprimento da parede? '))
larg = float(input('Qual a largura da parede? '))
tinta = (comp*larg)/2
print('='*50)
print('Sua parede tem dimensão de {} x {} e sua área é igual a {}m2.'.format(comp, larg, comp*larg))
print('Para pintar a parede por inteiro será necessário {}L de tinta.'.format(tinta))
print('='*50)
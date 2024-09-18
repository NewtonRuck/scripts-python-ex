print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
a = float(input('Primeira coordenada A: '))
b = float(input('Segunda coordenada B: '))
c = float(input('Terceira coordenada C: '))
print('-=-'*20)
from math import fabs
ac = fabs(a-c)
print('O segmento AC mede {}'.format(ac))
ab = fabs(a-b)
print('O segmento AB mede {}'.format(ab))
bc = fabs(b-c)
print('O segmento BC mede {}'.format(bc))
if ac < ab + bc:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
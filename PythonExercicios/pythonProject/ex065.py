#voce digitou x valores e a média entre eles foi y
#o maior valor foi a e o menor foi b
maior = 0
menor = 0
cont = soma = media = 0
r = 'S'
while 'S' in r:
    n = int(input('Digite um valor: '))
    cont += 1
    soma += n
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N]: ')).upper()
media = (soma) / (cont)
print('Você digitou {} número(s), a média entre eles é {:.1f}, o maior digitado foi {} e o menor {}.'.format(cont, media, maior, menor))
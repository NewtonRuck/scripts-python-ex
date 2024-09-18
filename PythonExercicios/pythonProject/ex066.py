cont = 0
soma = 0
num = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} número(s), a soma destes é igual a {soma}' )
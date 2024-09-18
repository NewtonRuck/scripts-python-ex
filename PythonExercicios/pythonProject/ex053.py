frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
#frase[::-1] = frase de trás pra frente
print(frase[::-1])
for letra in range(len(juntar) - 1, -1, -1):
    print(juntar[letra], end='')
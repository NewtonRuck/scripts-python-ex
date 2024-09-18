peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = (peso)/(altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \033[1;34mABAIXO DO PESO NORMAL.\033[m')
elif 18.5 < imc < 25:
    print('Você está no \033[1;32mPESO IDEAL\033[m')
elif 25 < imc < 30:
    print('Você está com \033[1;31mSOBREPESO\033[m')
elif 30 < imc < 40:
    print('Você está com \033[1;31mOBESIDADE\033[m')
else:
    print('Você está com \033[1;31mOBESIDADE MÓRBIDA\033[m')
n1 = int(input('Qual o primeiro número? '))
n2 = int(input('Qual o segundo número? '))
if n1 > n2:
    print('O \033[1;34mPRIMEIRO\033[m número é maior!')
elif n2 > n1:
    print('O \033[1;34mSEGUNDO\033[m número é maior!')
else:
    print('Os números são \033[1;31mIGUAIS\033[m')
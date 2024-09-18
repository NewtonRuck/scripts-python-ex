from math import sin, cos, tan, radians
ang = float(input('Qual o ângulo que deseja? '))
sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('O seno de {}º é aproximadamente: {:.2f}'.format(ang, sen))
print('O cosseno de {}º é aproximadamente: {:.2f}'.format(ang, coss))
print('A tangente de {}º é aproximadamente: {:.2f}'.format(ang, tang))
